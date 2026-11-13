#!/usr/bin/env python3
"""Generate the Quarto website sources under site/ from notes/.

- One page per knowledge point: note.md, then example.md, then the problems of
  exercise.md, each followed by its solution (collapsed).
- Cross-page @-references become links; same-page ones stay Quarto xrefs.
- Raw LaTeX drawings (```{=latex} blocks) are compiled to SVG and cached in
  site/tikz/ (keyed by content hash).
- Writes site/notes/**, site/index.qmd, site/_sidebar.yml (all generated).

Read-only with respect to notes/. Never runs git.
"""

from __future__ import annotations

import hashlib
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT / "notes"
SITE = ROOT / "site"
OUT_NOTES = SITE / "notes"
TIKZ = SITE / "tikz"

BRANCHES = [
    ("Discrete Mathematics", [
        ("math/discrete/sets", "Sets"),
        ("math/discrete/functions", "Functions"),
        ("math/discrete/relations", "Relations"),
        ("math/discrete/proof", "Proof"),
        ("math/discrete/logic/propositional", "Propositional Logic"),
        ("math/discrete/logic/predicate", "Predicate Logic"),
        ("math/discrete/sequences", "Sequences and Series"),
        ("math/discrete/number-theory", "Number Theory"),
        ("math/discrete/counting", "Counting"),
        ("math/discrete/graph", "Graph Theory"),
    ]),
    ("Probability", [
        ("math/probability", "Discrete Probability"),
    ]),
]

TYPE_WORD = {"def": "Definition", "thm": "Theorem", "prp": "Proposition",
             "lem": "Lemma", "cor": "Corollary", "exm": "Example", "prob": "Exercise"}

TIKZ_PREAMBLE = r"""\documentclass[varwidth=16cm,border=4pt]{standalone}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb,mathtools}
\usepackage[ruled,vlined,linesnumbered]{algorithm2e}
\usepackage{xcolor}
\usepackage{venndiagram}
\usepackage{tikz-cd}
\usepackage{pict2e}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,shapes.gates.logic.US,backgrounds}
\usepackage[american]{circuitikz}
\definecolor{defc}{HTML}{3B6EA5}
\definecolor{thmc}{HTML}{A5533B}
\definecolor{exc}{HTML}{4E8A5A}
\definecolor{notec}{HTML}{7A7A7A}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\C}{\mathbb{C}}
\newcommand{\I}{\mathcal{I}}
\newcommand{\power}[1]{\mathcal{P}(#1)}
\DeclareMathOperator{\Collatz}{Collatz}
\DeclareMathOperator{\dom}{dom}
\DeclareMathOperator{\lcmop}{lcm}
"""

OPEN = re.compile(r"^(:{3,})\s*\{(.*)\}\s*$")
CLOSE = re.compile(r"^(:{3,})\s*$")
REF = re.compile(r"(?<![\w@])@((?:def|thm|prp|lem|cor|exm|prob|sec)-[A-Za-z0-9-]*[A-Za-z0-9])")
RAW = re.compile(r"^([ \t]*)```\{=latex\}\n(.*?)\n[ \t]*```", re.S | re.M)


# ---------------------------------------------------------------- utilities
def split_front(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text
    return yaml.safe_load(m.group(1)) or {}, text[m.end():]


def strip_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->\n?", "", text, flags=re.S)


def attrs_of(s: str) -> dict:
    out = {"classes": re.findall(r"(?:^|\s)\.([\w-]+)", s)}
    kv = dict(re.findall(r'([\w-]+)="([^"]*)"', s))
    kv.update(dict(re.findall(r"([\w-]+)='([^']*)'", s)))
    no_kv = re.sub(r'[\w-]+=("[^"]*"|\'[^\']*\')', "", s)
    idm = re.search(r"(?:^|\s)#([\w-]+)", no_kv)
    out["id"] = idm.group(1) if idm else None
    out.update(kv)
    return out


def top_level_divs(text: str):
    """Yield (attrs, body) for top-level fenced divs, in order."""
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        m = OPEN.match(lines[i])
        if not m:
            i += 1
            continue
        depth, j = 1, i + 1
        while j < len(lines) and depth:
            if OPEN.match(lines[j]):
                depth += 1
            elif CLOSE.match(lines[j]):
                depth -= 1
            j += 1
        yield attrs_of(m.group(2)), "\n".join(lines[i + 1:j - 1])
        i = j


def fence_for(body: str) -> str:
    longest = max((len(m.group(1)) for m in re.finditer(r"^(:{3,})", body, re.M)), default=2)
    return ":" * max(3, longest + 1)


def page_url(nid: str) -> str:
    return f"/notes/{nid}.qmd"


def sort_key(sources: list) -> tuple:
    for s in sources or []:
        nums = re.findall(r"\d+", str(s))
        if nums:
            return tuple(int(n) for n in nums)
    return (999,)


# ---------------------------------------------------------------- TikZ -> SVG
def compile_svg(code: str) -> str | None:
    code = re.sub(r"\\begin\{algorithm\}(\[[^\]]*\])?", r"\\begin{algorithm}[H]", code)
    src = TIKZ_PREAMBLE + "\\begin{document}\n" + code + "\n\\end{document}\n"
    key = hashlib.sha1(src.encode()).hexdigest()[:16]
    out = TIKZ / f"{key}.svg"
    if out.exists():
        return out.name
    with tempfile.TemporaryDirectory() as tmp:
        tex = Path(tmp) / "fig.tex"
        tex.write_text(src, encoding="utf-8")
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "fig.tex"],
                           cwd=tmp, capture_output=True, text=True)
        pdf = Path(tmp) / "fig.pdf"
        if r.returncode != 0 or not pdf.exists():
            err = [l for l in r.stdout.splitlines() if l.startswith("!")][:2]
            print(f"  tikz compile failed ({key}): {' '.join(err)}", file=sys.stderr)
            return None
        r = subprocess.run(["pdftocairo", "-svg", str(pdf), str(out)], capture_output=True, text=True)
        if r.returncode != 0:
            print(f"  pdftocairo failed ({key}): {r.stderr.strip()}", file=sys.stderr)
            return None
    return out.name


# ---------------------------------------------------------------- notes
class Note:
    def __init__(self, folder: Path):
        self.folder = folder
        self.id = str(folder.relative_to(NOTES))
        self.front, body = split_front((folder / "note.md").read_text(encoding="utf-8"))
        self.title = self.front.get("title", self.id.rsplit("/", 1)[-1])
        self.body = strip_comments(body)
        self.examples = strip_comments((folder / "example.md").read_text(encoding="utf-8")) if (folder / "example.md").exists() else ""
        self.exercises = strip_comments((folder / "exercise.md").read_text(encoding="utf-8")) if (folder / "exercise.md").exists() else ""
        self.solutions = strip_comments((folder / "solution.md").read_text(encoding="utf-8")) if (folder / "solution.md").exists() else ""
        self.blocks: dict[str, str] = {}  # id -> name
        for text in (self.body, self.examples, self.exercises):
            for line in text.splitlines():
                m = OPEN.match(line)
                if m:
                    a = attrs_of(m.group(2))
                    if a["id"]:
                        self.blocks[a["id"]] = a.get("name", "")

    @property
    def branch(self) -> str:
        return self.id.rsplit("/", 1)[0]


def link_for(ref: str, here: Note, notes: dict[str, Note], owner: dict[str, str]) -> str:
    if ref.startswith("sec-"):
        nid = next((n for n in notes if "sec-" + n.replace("/", "-") == ref), None)
        if nid is None:
            return "@" + ref
        return f"[{notes[nid].title}]({page_url(nid)})"
    if ref in here.blocks:
        return "@" + ref
    nid = owner.get(ref)
    if nid is None:
        return "@" + ref
    word = TYPE_WORD.get(ref.split("-", 1)[0], "")
    name = notes[nid].blocks.get(ref) or ""
    text = f"{word} ({name})" if name else f"{word} in {notes[nid].title}"
    return f"[{text}]({page_url(nid)}#{ref})"


def render_problems(note: Note) -> str:
    sols = {a.get("for"): body for a, body in top_level_divs(note.solutions) if "solution" in a["classes"]}
    out = []
    for a, body in top_level_divs(note.exercises):
        if "problem" not in a["classes"]:
            continue
        pid = a["id"]
        num = int(pid.rsplit("-", 1)[-1]) if pid.rsplit("-", 1)[-1].isdigit() else ""
        src = a.get("source", "")
        m = re.match(r"fit1058-cn-([\d.]+)-q(\d+)", src)
        src_label = f"FIT1058 CN {m.group(1)} Q{m.group(2)}" if m else src
        f = fence_for(body)
        out.append(f"{f} {{#{pid} .problem}}\n[Exercise {num}]{{.problem-title}}"
                   f"[{src_label}]{{.problem-source}}\n\n{body.strip()}\n{f}\n")
        if pid in sols:
            sb = sols[pid]
            f2 = fence_for(sb)
            out.append(f'{f2} {{.callout-tip collapse="true" appearance="simple" title="Solution"}}\n'
                       f"{sb.strip()}\n{f2}\n")
    return "\n".join(out)


def fix_claims(text: str) -> str:
    def sub(m):
        a = attrs_of(m.group(2))
        if "claim" not in a["classes"]:
            return m.group(0)
        name = a.get("name")
        head = f"**Claim** ({name})." if name else "**Claim.**"
        return f"{m.group(1)} {{.claim}}\n{head}"
    return re.sub(r"^(:{3,})\s*\{(.*)\}\s*$", sub, text, flags=re.M)


def build_page(note: Note, notes: dict[str, Note], owner: dict[str, str], svgs: dict[str, str | None]) -> str:
    parts = [note.body.strip()]
    if note.examples.strip():
        parts.append("## Examples\n\n" + note.examples.strip())
    if note.exercises.strip():
        parts.append("## Exercises\n\n" + render_problems(note))
    body = "\n\n".join(parts)

    def raw_sub(m):
        ind = m.group(1)
        name = svgs.get(textwrap.dedent(m.group(2)))
        inner = f"![](/tikz/{name})" if name else "*(Figure available in the PDF version.)*"
        return "\n".join(ind + l for l in ["::: {.tikz-figure}", inner, ":::"])
    body = RAW.sub(raw_sub, body)
    body = fix_claims(body)
    body = REF.sub(lambda m: link_for(m.group(1), note, notes, owner), body)

    meta = []
    if note.front.get("sources"):
        meta.append("Sources: " + ", ".join(f"`{s}`" for s in note.front["sources"]))
    reqs = [r for r in note.front.get("requires") or [] if r in notes]
    if reqs:
        meta.append("Prerequisites: " + ", ".join(f"[{notes[r].title}]({page_url(r)})" for r in reqs))
    if note.front.get("status") == "draft":
        meta.append("Status: draft")
    head = "---\n" + yaml.safe_dump({"title": note.title}, allow_unicode=True) + "---\n\n"
    if meta:
        head += "[" + " · ".join(meta) + "]{.note-meta}\n\n"
    return head + body + "\n"


def main() -> int:
    folders = sorted(p.parent for p in NOTES.rglob("note.md"))
    notes = {n.id: n for n in (Note(f) for f in folders)}
    owner = {bid: n.id for n in notes.values() for bid in n.blocks}

    # compile drawings
    TIKZ.mkdir(parents=True, exist_ok=True)
    codes = sorted({textwrap.dedent(m.group(2)) for n in notes.values()
                    for t in (n.body, n.examples, n.exercises, n.solutions) for m in RAW.finditer(t)})
    with ThreadPoolExecutor(max_workers=6) as pool:
        svgs = dict(zip(codes, pool.map(compile_svg, codes)))
    failed = sum(1 for v in svgs.values() if v is None)
    print(f"drawings: {len(codes)} ({failed} failed)")

    # pages
    if OUT_NOTES.exists():
        shutil.rmtree(OUT_NOTES)
    for n in notes.values():
        path = OUT_NOTES / f"{n.id}.qmd"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(build_page(n, notes, owner, svgs), encoding="utf-8")

    # branch pages, sidebar, home
    known = {b for _, bs in BRANCHES for b, _ in bs}
    stray = sorted({n.branch for n in notes.values()} - known)
    if stray:
        print(f"warning: branches not in BRANCHES: {stray}", file=sys.stderr)
    sidebar, home = [], ["---", "title: Study Notes", "---", "",
                         "Study notes organised by topic. First batch: discrete mathematics (FIT1058 scope) and discrete probability.", ""]
    for field, branches in BRANCHES:
        sec = {"section": field, "contents": []}
        home.append(f"## {field}\n")
        for bid, btitle in branches:
            members = sorted((n for n in notes.values() if n.branch == bid),
                             key=lambda n: (sort_key(n.front.get("sources")), n.id))
            if not members:
                continue
            index = OUT_NOTES / bid / "index.qmd"
            index.parent.mkdir(parents=True, exist_ok=True)
            index.write_text(f"---\ntitle: \"{btitle}\"\n---\n\n" +
                             "\n".join(f"- [{n.title}]({page_url(n.id)})" for n in members) + "\n",
                             encoding="utf-8")
            sec["contents"].append({"section": btitle, "href": f"notes/{bid}/index.qmd",
                                    "contents": [f"notes/{n.id}.qmd" for n in members]})
            home.append(f"- [{btitle}](notes/{bid}/index.qmd) ({len(members)})")
        home.append("")
        sidebar.append(sec)
    (SITE / "index.qmd").write_text("\n".join(home) + "\n", encoding="utf-8")
    (SITE / "_sidebar.yml").write_text(
        "# Generated by build/make_site.py\n" +
        yaml.safe_dump({"website": {"sidebar": {"style": "docked", "collapse-level": 2,
                                                "contents": sidebar}}},
                       allow_unicode=True, sort_keys=False),
        encoding="utf-8")
    print(f"pages: {len(notes)} notes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
