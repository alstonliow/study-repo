#!/usr/bin/env python3
"""Generate the Quarto website sources under site/ from notes/.

- One page per knowledge point: note.md, then example.md, then the problems of
  exercise.md, each followed by its solution (collapsed).
- Cross-page @-references become links; same-page ones stay Quarto xrefs.
- Raw LaTeX drawings (```{=latex} blocks) are compiled to SVG and cached in
  site/tikz/ (keyed by content hash).
- Writes site/notes/**, site/courses/**, site/index.qmd, site/_nav.yml,
  site/courses.json, site/progress.json (all generated).

Read-only with respect to notes/. Never runs git.
"""

from __future__ import annotations

import hashlib
import html
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
OUT_COURSES = SITE / "courses"
TIKZ = SITE / "tikz"
COURSES = (yaml.safe_load((ROOT / "meta" / "courses.yml").read_text(encoding="utf-8")) or {}).get("courses", [])


def courses_of(keys) -> list[str]:
    """Course ids whose prefix matches any of the given source keys."""
    keys = [str(k) for k in keys or [] if k]
    return [c["id"] for c in COURSES if any(k.startswith(c["prefix"]) for k in keys)]


ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]


def course_key(keys, course: dict) -> tuple:
    """Numeric position of a note inside a course (from its first matching key)."""
    for k in keys or []:
        k = str(k)
        if k.startswith(course["prefix"]):
            nums = re.findall(r"\d+", k[len(course["prefix"]):])
            if nums:
                return tuple(int(n) for n in nums)
    return (999,)

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
             "lem": "Lemma", "cor": "Corollary", "exm": "Example", "prob": "Exercise", "fig": "Figure"}

TIKZ_PREAMBLE = r"""\documentclass[varwidth=16cm,border=4pt]{standalone}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb,mathtools}
\usepackage[ruled,vlined,linesnumbered]{algorithm2e}
\usepackage{xcolor}
\usepackage{venndiagram}
\usepackage{tikz-cd}
\usepackage{pict2e}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,shapes.gates.logic.US,backgrounds,shapes.geometric,decorations.pathreplacing}
\usepackage[american]{circuitikz}
\definecolor{defc}{HTML}{3B6EA5}
\definecolor{thmc}{HTML}{A5533B}
\definecolor{exc}{HTML}{4E8A5A}
\definecolor{notec}{HTML}{7A7A7A}
% shared figure styles (meta/SPEC.md: figures)
\colorlet{ink}{black!82}
\tikzset{
  every picture/.style={line width=0.6pt, line cap=round, line join=round, >={Stealth[length=5pt,width=4.5pt]}},
  vertex/.style={circle, draw=ink, fill=defc!8, line width=0.7pt, inner sep=1.5pt, minimum size=6.5mm},
  dot/.style={circle, fill=ink, draw=none, inner sep=0pt, minimum size=5.5pt},
  graph/.style={every node/.style={vertex}},
  dotgraph/.style={every node/.style={dot}},
  hl/.style={draw=thmc, line width=1.8pt},
  faint/.style={draw=black!28, line width=0.5pt},
  regionA/.style={fill=defc!10, draw=defc!75, rounded corners=4pt},
  regionB/.style={fill=thmc!10, draw=thmc!75, rounded corners=4pt},
  regionC/.style={fill=exc!12, draw=exc!75, rounded corners=4pt},
  shade/.style={fill=defc!25},
  tintA/.style={fill=defc, fill opacity=0.10},
  tintB/.style={fill=thmc, fill opacity=0.10},
  tintC/.style={fill=exc, fill opacity=0.12},
  tintD/.style={fill=notec, fill opacity=0.12},
  lab/.style={fill=none, draw=none, inner sep=1pt, minimum size=0pt, font=\small},
  set/.style={ellipse, draw=ink, fill=defc!6, minimum width=1.3cm, minimum height=2.5cm},
  map/.style={->, shorten <=3pt, shorten >=3pt},
}
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

KEY_PREFIXES = {"def", "thm", "prp", "lem", "cor"}
OPEN = re.compile(r"^(:{3,})\s*\{(.*)\}\s*$")
CLOSE = re.compile(r"^(:{3,})\s*$")
REF = re.compile(r"(?<![\w@])@((?:def|thm|prp|lem|cor|exm|prob|fig|sec)-[A-Za-z0-9-]*[A-Za-z0-9])")
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
        self.key_items: list[str] = []    # named definitions/theorems, in order
        self.num = ""                      # e.g. "1.4", set in main()
        for text in (self.body, self.examples, self.exercises):
            for line in text.splitlines():
                m = OPEN.match(line)
                if m:
                    a = attrs_of(m.group(2))
                    if a["id"]:
                        self.blocks[a["id"]] = a.get("name", "")
                        if a["id"].split("-", 1)[0] in KEY_PREFIXES and a.get("name"):
                            self.key_items.append(a["name"])

        self.problem_sources = [a.get("source", "") for a, _ in top_level_divs(self.exercises)
                                if "problem" in a["classes"]]
        self.courses = courses_of(list(self.front.get("sources") or []) + self.problem_sources)

    @property
    def display_title(self) -> str:
        return f"{self.num} {self.title}" if self.num else self.title

    @property
    def branch(self) -> str:
        return self.id.rsplit("/", 1)[0]


def link_for(ref: str, here: Note, notes: dict[str, Note], owner: dict[str, str]) -> str:
    if ref.startswith("sec-"):
        nid = next((n for n in notes if "sec-" + n.replace("/", "-") == ref), None)
        if nid is None:
            return "@" + ref
        return f"[{notes[nid].display_title}]({page_url(nid)})"
    if ref in here.blocks:
        return "@" + ref
    nid = owner.get(ref)
    if nid is None:
        return "@" + ref
    word = TYPE_WORD.get(ref.split("-", 1)[0], "")
    name = notes[nid].blocks.get(ref) or ""
    text = f"{word} ({name})" if name else f"{word} in {notes[nid].display_title}"
    return f"[{text}]({page_url(nid)}#{ref})"


def render_problems(note: Note) -> str:
    sols = {a.get("for"): body for a, body in top_level_divs(note.solutions) if "solution" in a["classes"]}
    draft = {a.get("for") for a, _ in top_level_divs(note.solutions)
             if "solution" in a["classes"] and a.get("status") == "draft"}
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
        badge = level_badge(a.get("level"))
        group = [f"{f} {{#{pid} .problem}}\n[Exercise {num}]{{.problem-title}}"
                 f"[{src_label}]{{.problem-source}}{badge}\n\n{body.strip()}\n{f}\n"]
        if sols.get(pid, "").strip():   # empty TODO stubs are not shown
            sb = sols[pid]
            f2 = fence_for(sb)
            title = "Draft solution (not yet reviewed)" if pid in draft else "Solution"
            group.append(f'{f2} {{.callout-tip collapse="true" appearance="simple" title="{title}"}}\n'
                         f"{sb.strip()}\n{f2}\n")
        inner = "\n".join(group)
        fo = fence_for(inner)
        cs = " ".join(courses_of([src]))
        out.append(f'{fo} {{.problem-group data-courses="{cs}"}}\n{inner}\n{fo}\n')
    return "\n".join(out)


def level_badge(level) -> str:
    return f" [{level}]{{.level-badge .level-{level}}}" if level in ("easy", "medium", "hard") else ""


def add_example_levels(text: str) -> str:
    """Put a level badge at the start of example blocks that have `level`."""
    def sub(m):
        a = attrs_of(m.group(2))
        if "example" in a["classes"] and a.get("level"):
            return m.group(0) + "\n" + level_badge(a["level"]).strip()
        return m.group(0)
    return re.sub(r"^(:{3,})\s*\{(.*)\}\s*$", sub, text, flags=re.M)


def fix_claims(text: str) -> str:
    def sub(m):
        a = attrs_of(m.group(2))
        if "claim" not in a["classes"]:
            return m.group(0)
        name = a.get("name")
        head = f"**Claim** ({name})." if name else "**Claim.**"
        return f"{m.group(1)} {{.claim}}\n{head}"
    return re.sub(r"^(:{3,})\s*\{(.*)\}\s*$", sub, text, flags=re.M)


FIG_SCALE = 1.3  # figures are drawn at 10pt; scale up to sit with the larger body text


def svg_width(name: str) -> int:
    """Display width in px for a compiled SVG: its natural size times FIG_SCALE."""
    head = (TIKZ / name).read_text(encoding="utf-8")[:600]
    m = re.search(r'width="([\d.]+)(pt|px)?"', head)
    w = float(m.group(1)) * (4 / 3 if (m.group(2) or "pt") == "pt" else 1) if m else 400
    return round(w * FIG_SCALE)


def is_algorithm(code: str) -> bool:
    """Raw LaTeX blocks in algorithmic syntax, rendered as HTML instead of SVG."""
    return "\\begin{algorithmic}" in code


def build_page(note: Note, notes: dict[str, Note], owner: dict[str, str], svgs: dict[str, str | None]) -> str:
    body_text = note.body.strip()
    if note.num:
        counter = iter(range(1, 1000))
        body_text = re.sub(r"(?m)^## (?!#)(.+)$",
                           lambda m: f"## {note.num}.{next(counter)} {m.group(1)}", body_text)
    parts = [body_text]
    if note.examples.strip():
        parts.append("## Examples\n\n" + note.examples.strip())
    if note.exercises.strip():
        parts.append("## Exercises\n\n" + render_problems(note))
    body = "\n\n".join(parts)

    def raw_sub(m):
        ind = m.group(1)
        if is_algorithm(m.group(2)):
            # algorithms are typeset in the browser by pseudocode.js (site/pseudocode.html)
            src = html.escape(textwrap.dedent(m.group(2)), quote=False)
            return "\n".join(ind + l for l in ["```{=html}", f'<pre class="pseudocode">{src}</pre>', "```"])
        name = svgs.get(textwrap.dedent(m.group(2)))
        inner = f"![](/tikz/{name}){{width={svg_width(name)}px}}" if name else "*(Figure available in the PDF version.)*"
        return "\n".join(ind + l for l in ["::: {.tikz-figure}", inner, ":::"])
    body = RAW.sub(raw_sub, body)
    body = fix_claims(body)
    body = add_example_levels(body)
    body = REF.sub(lambda m: link_for(m.group(1), note, notes, owner), body)

    meta = []
    if note.front.get("sources"):
        meta.append("Sources: " + ", ".join(f"`{s}`" for s in note.front["sources"]))
    reqs = [r for r in note.front.get("requires") or [] if r in notes]
    if reqs:
        meta.append("Prerequisites: " + ", ".join(f"[{notes[r].display_title}]({page_url(r)})" for r in reqs))
    if note.front.get("status") == "draft":
        meta.append("Status: draft")
    head = "---\n" + yaml.safe_dump({"title": note.display_title}, allow_unicode=True) + "---\n\n"
    if meta:
        head += "[" + " · ".join(meta) + "]{.note-meta}\n\n"
    return head + body + "\n"


BRANCH_DESC = {
    "math/discrete/sets": "Sets, subsets, power sets, set operations, partitions",
    "math/discrete/functions": "Functions, injections and bijections, inverses, composition",
    "math/discrete/relations": "Binary relations, their properties, equivalence relations",
    "math/discrete/proof": "Theorems and proofs, proof techniques, induction",
    "math/discrete/logic/propositional": "Connectives, laws of Boolean algebra, normal forms",
    "math/discrete/logic/predicate": "Predicates and quantifiers",
    "math/discrete/sequences": "Recurrences, limits, big-O, sums and series",
    "math/discrete/number-theory": "Divisibility, gcd, modular arithmetic, Diffie–Hellman",
    "math/discrete/counting": "Counting rules, inclusion–exclusion, selections",
    "math/discrete/graph": "Paths, connectivity, trees, planarity",
    "math/probability": "Events, conditional probability, random variables, distributions",
}


def branch_page(bid: str, btitle: str, members: list, bnum: int) -> str:
    """Numbered, book-style contents for one branch."""
    nex = sum(len(n.problem_sources) for n in members)
    counts = f"{len(members)} topics" + (f" · {nex} exercises" if nex else "")
    desc = BRANCH_DESC.get(bid, "")
    lines = ["---", yaml.safe_dump({"title": f"{bnum} {btitle}"}, allow_unicode=True).strip(), "---", "",
             f"[{desc + '. ' if desc else ''}{counts}]{{.branch-intro}}", "",
             "::: {.branch-toc}"]
    for n in members:
        items = n.key_items
        shown = " · ".join(items[:6]) + (" · …" if len(items) > 6 else "")
        lines.append(f"- [{n.num}]{{.toc-num}} [{n.title}]({page_url(n.id)})" +
                     (f" [{shown}]{{.toc-desc}}" if shown else ""))
    lines += [":::", ""]
    return "\n".join(lines)


def contents_block(heading: str, rows: list) -> list[str]:
    """A book-style contents list for the home page: (href, title, desc)."""
    import html
    items = "\n".join(
        f'<li><a href="{href}">'
        + (f'<span class="contents-num">{num}</span>' if num else "")
        + f'{html.escape(title)}</a>'
        + (f'<span class="contents-desc">{html.escape(desc)}</span>' if desc else "")
        + "</li>"
        for href, title, desc, num in rows)
    return ["::: {.contents-field}", f"## {heading}", "", "```{=html}",
            f'<ul class="contents-list">\n{items}\n</ul>', "```", ":::", ""]


def main() -> int:
    folders = sorted(p.parent for p in NOTES.rglob("note.md"))
    notes = {n.id: n for n in (Note(f) for f in folders)}
    owner = {bid: n.id for n in notes.values() for bid in n.blocks}

    # compile drawings
    TIKZ.mkdir(parents=True, exist_ok=True)
    codes = sorted({textwrap.dedent(m.group(2)) for n in notes.values()
                    for t in (n.body, n.examples, n.exercises, n.solutions) for m in RAW.finditer(t)
                    if not is_algorithm(m.group(2))})
    with ThreadPoolExecutor(max_workers=6) as pool:
        svgs = dict(zip(codes, pool.map(compile_svg, codes)))
    failed = sum(1 for v in svgs.values() if v is None)
    print(f"drawings: {len(codes)} ({failed} failed)")

    # numbering: branches 1, 2, ... restarting in each part (field); topics b.k
    branch_num: dict[str, int] = {}
    for _, branches in BRANCHES:
        seq = 0
        for bid, _ in branches:
            members = sorted((n for n in notes.values() if n.branch == bid),
                             key=lambda n: (sort_key(n.front.get("sources")), n.id))
            if not members:
                continue
            seq += 1
            branch_num[bid] = seq
            for k, n in enumerate(members, 1):
                n.num = f"{seq}.{k}"

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
    sidebar = []
    branch_items = {}
    home = ["---", "title: Study Notes", "---", "",
            "Personal study notes, organised by topic rather than by course. "
            "So far: discrete mathematics and discrete probability.", ""]
    for field, branches in BRANCHES:
        sec = {"section": field, "contents": []}
        rows = []
        for bid, btitle in branches:
            members = sorted((n for n in notes.values() if n.branch == bid),
                             key=lambda n: (sort_key(n.front.get("sources")), n.id))
            if not members:
                continue
            branch_items[bid] = [n.id for n in members]
            index = OUT_NOTES / bid / "index.qmd"
            index.parent.mkdir(parents=True, exist_ok=True)
            index.write_text(branch_page(bid, btitle, members, branch_num[bid]), encoding="utf-8")
            sec["contents"].append({"section": f"{branch_num[bid]} {btitle}", "href": f"notes/{bid}/index.qmd",
                                    "contents": [f"notes/{n.id}.qmd" for n in members]})
            rows.append((f"notes/{bid}/index.html", btitle, BRANCH_DESC.get(bid, ""), branch_num[bid]))
        home += contents_block(field, rows)
        sidebar.append(sec)
    # course pages: knowledge points in course order, grouped by chapter
    if OUT_COURSES.exists():
        shutil.rmtree(OUT_COURSES)
    OUT_COURSES.mkdir(parents=True)
    branch_title = {b: bt for _, bs in BRANCHES for b, bt in bs}
    page_courses = {}
    course_rows = []
    course_order = {}  # course id -> [{"title": chapter heading, "pages": [note html paths]}]
    for c in COURSES:
        members = sorted((n for n in notes.values() if c["id"] in n.courses),
                         key=lambda n: (course_key(n.front.get("sources"), c), n.id))
        label = c["code"] + (f" – {c['name']}" if c.get("name") else "")
        lines = ["---", yaml.safe_dump({"title": label}, allow_unicode=True).strip(), "---", "",
                 f"Knowledge points used by {c['code']}, in course order. "
                 "The course filter at the bottom of the sidebar shows only this course's content.", ""]
        # chapter topic = the most common branch among its notes; a topic that
        # spans several chapters gets Roman numerals (Graph Theory I, II)
        topics = {}
        for ch in sorted({course_key(m.front.get("sources"), c)[0] for m in members} - {999}):
            same = [m.branch for m in members if course_key(m.front.get("sources"), c)[:1] == (ch,)]
            topics[ch] = branch_title.get(max(sorted(set(same)), key=same.count), "")
        for t in set(topics.values()):
            chs = [ch for ch in topics if topics[ch] == t]
            if t and len(chs) > 1:
                for i, ch in enumerate(chs):
                    topics[ch] = f"{t} {ROMAN[i]}"
        chapter = None
        for n in members:
            pos = course_key(n.front.get("sources"), c)
            ch = pos[0] if pos != (999,) else None
            if ch != chapter:
                chapter = ch
                topic = topics.get(ch, "")
                heading = f"Chapter {ch}" + (f" · {topic}" if topic else "") if ch else "Other"
                lines += ["", f"## {heading}", ""]
                course_order.setdefault(c["id"], []).append({"title": heading, "num": ch, "pages": []})
            course_order[c["id"]][-1]["pages"].append(f"notes/{n.id}.html")
            keys = [k for k in n.front.get("sources") or [] if str(k).startswith(c["prefix"])]
            nprob = sum(1 for s in n.problem_sources if s.startswith(c["prefix"]))
            extra = f" ({nprob} exercise{'s' if nprob != 1 else ''})" if nprob else ""
            lines.append(f"- [{n.display_title}](/notes/{n.id}.qmd){extra} [{', '.join(keys)}]{{.note-keys}}")
        (OUT_COURSES / f"{c['id']}.qmd").write_text("\n".join(lines) + "\n", encoding="utf-8")
        course_rows.append((f"courses/{c['id']}.html", c["code"],
                            c.get("name") or "Knowledge points in course order", ""))
        page_courses[f"courses/{c['id']}.html"] = [c["id"]]
    if course_rows:
        home += contents_block("Courses", course_rows)
    for n in notes.values():
        page_courses[f"notes/{n.id}.html"] = n.courses

    import json
    (SITE / "courses.json").write_text(json.dumps({
        "courses": [{"id": c["id"], "code": c["code"], "name": c.get("name", "")} for c in COURSES],
        "pages": page_courses, "order": course_order}, ensure_ascii=False, indent=1), encoding="utf-8")

    # progress tracking (site/progress.html): which problems sit on which page
    (SITE / "progress.json").write_text(json.dumps({
        "branches": branch_items,
        "notes": {n.id: [a["id"] for a, _ in top_level_divs(n.exercises) if "problem" in a["classes"]]
                  for n in notes.values()}}, ensure_ascii=False, indent=1), encoding="utf-8")

    (SITE / "index.qmd").write_text("\n".join(home) + "\n", encoding="utf-8")
    navbar = [{"href": "index.qmd", "text": "Home"}]
    (SITE / "_nav.yml").write_text(
        "# Generated by build/make_site.py\n" +
        yaml.safe_dump({"website": {"navbar": {"left": navbar},
                                    "sidebar": {"style": "docked", "collapse-level": 2,
                                                "contents": sidebar}}},
                       allow_unicode=True, sort_keys=False),
        encoding="utf-8")
    old = SITE / "_sidebar.yml"
    if old.exists():
        old.unlink()
    print(f"pages: {len(notes)} notes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
