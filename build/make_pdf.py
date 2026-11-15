#!/usr/bin/env python3
"""Build PDFs of the notes with Quarto and LaTeX (meta/SPEC.md §15).

    python3 build/make_pdf.py [options]          # one PDF
    python3 build/make_pdf.py --preset NAME      # a named set of options
    python3 build/make_pdf.py --all-presets      # every preset (what CI publishes)

Options
  --scope book | branch:<branch id> | course:<course id>     (default: book)
  --solutions inline | end | separate | none                 (default: end)
  --extra include | omit      content outside a course's scope; needs a course,
                              from --scope course:... or --course   (default: include)
  --course <course id>        course that defines "extra" for book or branch scope
  --only all | summaries | exercises                         (default: all)
  --level easy,medium,hard,unrated   which exercises to print (default: all)
  --paper a4 | letter                                        (default: a4)
  --layout book | document    book: chapters start on a new page, two-sided, title
                              page; document: article style, compact (default: book)
  --margin <cm>               page margins in centimetres            (default: 2.2)
  --style color | plain       color: the website's look (coloured left rule and tint
                              for definitions, results and examples; grey exercises);
                              plain: black and white                  (default: color)
  --name <file name>          output name without .pdf (default: from the options)
  --keep                      keep the generated .qmd/.tex next to the PDF
  --markdown-only             write out/pdf/<name>.qmd only, no LaTeX (used by tests)

Output: out/pdf/<name>.pdf (and <name>-solutions.pdf with --solutions separate).
Figures use the shared styles in build/figures.tex; algorithms use the
`algorithmic` package. References to content that is not printed become plain
text. Read-only with respect to notes/; never runs git.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import textwrap
from pathlib import Path

import yaml

from model import RAW, REF, ROOT, divs_in, fence_for, load
from summaries import statements

OUT = ROOT / "out" / "pdf"
FIGURES = (Path(__file__).resolve().parent / "figures.tex").read_text(encoding="utf-8")
HEADER = FIGURES + r"""
\usepackage{algorithm}
\usepackage{algorithmic}
\providecommand{\INPUT}{\item[\textbf{Input:}]}
\providecommand{\OUTPUT}{\item[\textbf{Output:}]}
% number theorem-like blocks 1, 2, 3, ... through the document (sections are unnumbered)
\makeatletter
\AtBeginDocument{\@for\st@env:=definition,theorem,proposition,lemma,corollary,example\do{%
  \@ifundefined{c@\st@env}{}{\counterwithout{\st@env}{section}%
    \@ifundefined{c@chapter}{}{\counterwithout{\st@env}{chapter}}}}}
\makeatother
"""
# --style color: the website's look. Colours are the ones in figures.tex
# (defc blue, thmc terracotta, exc green), so web, figures and PDF match.
COLOR_HEADER = r"""
\usepackage[most]{tcolorbox}
\colorlet{thmheadc}{black}
\makeatletter
\AtBeginDocument{\@ifundefined{thmhead}{}{%
  \let\st@thmhead\thmhead
  \renewcommand{\thmhead}[3]{\textcolor{thmheadc}{\st@thmhead{#1}{#2}{#3}}}}}
\makeatother
\newtcolorbox{stbox}[1]{enhanced, breakable, frame hidden, sharp corners, boxrule=0pt,
  colback=#1!5!white, borderline west={2pt}{0pt}{#1}, left=8pt, right=6pt, top=3pt, bottom=3pt,
  before skip=8pt, after skip=8pt, before upper={\colorlet{thmheadc}{#1}}}
\newtcolorbox{stexercise}{enhanced, breakable, frame hidden, sharp corners, boxrule=0pt,
  colback=black!4!white, left=8pt, right=6pt, top=4pt, bottom=4pt, before skip=8pt, after skip=6pt}
"""
BOX_COLOR = {"def": "defc", "thm": "thmc", "prp": "thmc", "lem": "thmc", "cor": "thmc", "exm": "exc"}
WORD = {"def": "Definition", "thm": "Theorem", "prp": "Proposition", "lem": "Lemma", "cor": "Corollary",
        "exm": "Example", "fig": "Figure", "prob": "Exercise", "rmk": "Remark", "clm": "Claim"}
LEVELS = ("easy", "medium", "hard", "unrated")

# Common versions, built by CI and linked from the website's Downloads page.
PRESETS = {
    "notes-book": dict(scope="book", solutions="end"),
    "fit1058": dict(scope="course:fit1058", solutions="end", extra="omit"),
    "fit1058-summaries": dict(scope="course:fit1058", only="summaries", solutions="none", extra="omit"),
    "fit1058-exercises": dict(scope="course:fit1058", only="exercises", solutions="separate", extra="omit"),
}
BRANCH_PRESETS = True   # plus one PDF per branch: branch-<last part of id>
DESCRIPTIONS = {
    "notes-book": "All notes, every branch, solutions at the end",
    "fit1058": "FIT1058 in course order, course content only, solutions at the end",
    "fit1058-summaries": "FIT1058 chapter summaries: definitions, results and exercises",
    "fit1058-exercises": "FIT1058 exercises only (solutions in a separate file)",
}


class Options(argparse.Namespace):
    scope = "book"
    solutions = "end"
    extra = "include"
    course = None
    only = "all"
    level = ",".join(LEVELS)
    paper = "a4"
    style = "color"
    layout = "book"
    margin = 2.2
    name = None
    keep = False
    markdown_only = False


def parse(argv: list[str]) -> tuple[Options, list[str]]:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--scope", default="book")
    ap.add_argument("--solutions", choices=["inline", "end", "separate", "none"], default="end")
    ap.add_argument("--extra", choices=["include", "omit"], default="include")
    ap.add_argument("--course")
    ap.add_argument("--only", choices=["all", "summaries", "exercises"], default="all")
    ap.add_argument("--level", default=",".join(LEVELS))
    ap.add_argument("--paper", choices=["a4", "letter"], default="a4")
    ap.add_argument("--style", choices=["color", "plain"], default="color")
    ap.add_argument("--layout", choices=["book", "document"], default="book")
    ap.add_argument("--margin", type=float, default=2.2)
    ap.add_argument("--name")
    ap.add_argument("--keep", action="store_true")
    ap.add_argument("--markdown-only", action="store_true")
    ap.add_argument("--preset", action="append", default=[])
    ap.add_argument("--all-presets", action="store_true")
    ns = ap.parse_args(argv, namespace=Options())
    presets = list(ns.preset)
    if ns.all_presets:
        presets = all_presets()
    return ns, presets


def all_presets() -> list[str]:
    repo = load()
    names = list(PRESETS)
    if BRANCH_PRESETS:
        names += [f"branch-{bid.rsplit('/', 1)[-1]}" for _, bs in repo.parts for bid, _ in bs
                  if repo.branch_members(bid)]
    return names


def preset_options(name: str) -> Options:
    o = Options()
    if name in PRESETS:
        for k, v in PRESETS[name].items():
            setattr(o, k, v)
    elif name.startswith("branch-"):
        repo = load()
        slug = name[len("branch-"):]
        bid = next((b for _, bs in repo.parts for b, _ in bs if b.rsplit("/", 1)[-1] == slug), None)
        if not bid:
            raise SystemExit(f"unknown preset {name}")
        o.scope, o.solutions = f"branch:{bid}", "end"
    else:
        raise SystemExit(f"unknown preset {name}; known: {', '.join(all_presets())}")
    o.name = name
    return o


# ---------------------------------------------------------------- content
class Book:
    """Assembles one document from the model according to the options."""

    def __init__(self, repo, o: Options):
        self.repo, self.o = repo, o
        self.levels = {x.strip() for x in o.level.split(",") if x.strip()}
        self.course = None
        cid = o.scope.split(":", 1)[1] if o.scope.startswith("course:") else o.course
        if cid:
            self.course = next((c for c in repo.courses if c.id == cid), None)
            if not self.course:
                raise SystemExit(f"unknown course '{cid}'")
        if o.extra == "omit" and not self.course:
            raise SystemExit("--extra omit needs a course (--scope course:<id> or --course <id>)")
        self.branch_num = repo.number_notes()
        self.chapters = self.plan()
        self.printed: set[str] = set()      # labels present in the document
        self.solutions_end: list[str] = []
        self.solutions_only: list[str] = []

    # which notes, grouped into chapters: [(title, [notes], [review folders])]
    def plan(self):
        r, o = self.repo, self.o
        if o.scope == "book":
            return [(f"{self.branch_num[b]} {t}", r.branch_members(b), [r.reviews[b]] if b in r.reviews else [])
                    for _, bs in r.parts for b, t in bs if r.branch_members(b)]
        if o.scope.startswith("branch:"):
            b = o.scope.split(":", 1)[1]
            title = next((t for _, bs in r.parts for x, t in bs if x == b), None)
            if title is None:
                raise SystemExit(f"unknown branch '{b}'")
            return [(f"{self.branch_num[b]} {title}", r.branch_members(b), [r.reviews[b]] if b in r.reviews else [])]
        if o.scope.startswith("course:"):
            c = self.course
            out, last = [], {}
            for nid, p in c.order:
                last[r.notes[nid].branch] = p.chapter
            for ch in c.chapters:
                notes = [r.notes[nid] for nid, p in c.order if p.chapter == ch["num"]]
                if self.o.extra == "omit":
                    notes = [n for n in notes if r.in_scope(c, n.id)]
                if not notes:
                    continue
                for k, n in enumerate(notes, 1):   # course numbering, as on the website when filtered
                    n.num = f"{ch['num']}.{k}"
                reviews = [r.reviews[b] for b, lc in last.items() if lc == ch["num"] and b in r.reviews]
                out.append((f"{ch['num']} {ch['title']}", notes, reviews))
            return out
        raise SystemExit(f"--scope must be book, branch:<id> or course:<id>, not '{o.scope}'")

    def keep(self, note, bid) -> bool:
        if self.o.extra != "omit" or bid is None:
            return True
        return self.repo.in_scope(self.course, note.id, bid)

    def keep_problem(self, note, pid, level) -> bool:
        lv = level or "unrated"
        if lv not in self.levels:
            return False
        if self.o.extra == "omit":
            if note.id in self.repo.notes:
                return self.repo.in_scope(self.course, note.id, pid)
            return self.course.id in self.repo.review_courses(note.branch, pid)
        return True

    # ---- pieces
    def note_body(self, note) -> str:
        """note.md (+ example.md) without out-of-scope blocks, headings demoted."""
        parts = []
        for text in (note.body, note.examples):
            text = text.strip()
            if not text:
                continue
            lines = text.split("\n")
            drop = []
            last = None
            for d in divs_in(text):
                if d.depth:
                    continue
                owner = last if (d.has("proof") and not d.has("remark")) else d.id
                if not (d.has("proof") and not d.has("remark")):
                    last = d.id
                if owner and not self.keep(note, owner):
                    drop.append((d.line - 1, d.end - 1))
            for a, b in reversed(drop):
                del lines[a:b + 1]
            text = "\n".join(lines)
            text = re.sub(r"(?m)^(#{2,5}) ", lambda m: "#" + m.group(1) + " ", text)   # ## -> ###
            parts.append(text if not parts else "### Examples\n\n" + text)
        body = "\n\n".join(parts)
        for d in divs_in(body):
            if d.id:
                self.printed.add(d.id)
        return body

    def problems(self, note, heading: str) -> str:
        sols = {d.attrs.get("for"): d for d in note.solution_divs}
        out = []
        for k, p in enumerate(note.problems, 1):
            pid, lv = p.id, p.attrs.get("level", "")
            if not self.keep_problem(note, pid, lv):
                continue
            num = pid.rsplit("-", 1)[-1].lstrip("0") or pid
            src = p.attrs.get("source", "")
            m = re.match(r"fit1058-cn-([\d.]+)-q(\d+)", src)
            label = f"FIT1058 CN {m.group(1)} Q{m.group(2)}" if m else src
            tag = f"Exercise {num}" + (f" ({label})" if label else "") + (f" [{lv}]" if lv else "")
            stmt = f"[]{{#{pid}}}\n**{tag}.**\n\n{p.body.strip()}\n"
            if self.o.style == "color":
                stmt = f"```{{=latex}}\n\\begin{{stexercise}}\n```\n\n{stmt}\n```{{=latex}}\n\\end{{stexercise}}\n```\n"
            self.printed.add(pid)
            out.append(stmt)
            sol = sols.get(pid)
            if sol is None or not sol.body.strip() or self.o.solutions == "none":
                continue
            draft = " (draft)" if sol.attrs.get("status") == "draft" else ""
            text = f"*Solution{draft}.*\n\n{sol.body.strip()}\n"
            if self.o.solutions == "inline":
                out.append(text)
            elif self.o.solutions == "end":
                self.solutions_end.append(f"**{heading}, exercise {num}.**\n\n{text}")
            else:
                self.solutions_only.append(f"**{heading}, exercise {num}.**\n\n{p.body.strip()}\n\n{text}")
        return "\n\n".join(out)

    def statements_of(self, note) -> str:
        out = []
        for d in statements(note, lambda bid: self.keep(note, bid)):
            f = fence_for(d.body)
            attrs = "{" + f"#{d.id} ." + d.classes[0] + (f' name="{d.name}"' if d.name else "") + "}"
            out.append(f"{f} {attrs}\n{d.body.strip()}\n{f}")
            self.printed.add(d.id)
        return "\n\n".join(out)

    # ---- document
    def markdown(self) -> str:
        o = self.o
        lines = []
        for title, notes, reviews in self.chapters:
            lines += [f"# {title}", ""]
            if o.only == "summaries":
                lines += ["## Definitions and results", ""]
                for n in notes:
                    st = self.statements_of(n)
                    if st:
                        lines += [f"### {n.display_title}", "", st, ""]
                ex = [(n, self.problems(n, n.display_title)) for n in notes]
                if any(p for _, p in ex):
                    lines += ["## Exercises", ""]
                    for n, p in ex:
                        if p:
                            lines += [f"### {n.display_title}", "", p, ""]
            else:
                for n in notes:
                    self.printed.add(n.sec_label)
                    lines += [f"## {n.display_title} {{#{n.sec_label}}}", ""]
                    if o.only == "all":
                        lines += [self.note_body(n), ""]
                    probs = self.problems(n, n.display_title)
                    if probs:
                        lines += (["### Exercises", ""] if o.only == "all" else []) + [probs, ""]
            syn = [self.problems(rv, f"{title}, synthesis") for rv in reviews]
            syn = [s for s in syn if s]
            if syn:
                lines += ["## Synthesis problems", ""] + syn + [""]
        if self.solutions_end:
            lines += ["# Solutions", ""] + self.solutions_end
        return self.finish("\n".join(lines))

    def finish(self, md: str) -> str:
        """Lift remark ids, turn claims into text, and resolve references."""
        md = lift_plain_ids(md)
        if self.o.style == "color":
            md = boxed(md)
        # LaTeX (unlike MathJax) needs braces for a command as sub/superscript: x_\mathbb{Z}
        md = re.sub(r"([_^])\\((?:math[a-z]+|text[a-z]*|operatorname|bm))\{([^{}]*)\}", r"\1{\\\2{\3}}", md)
        notes, owner = self.repo.notes, self.repo.owner

        def ref(m):
            r = m.group(1)
            pre = r.split("-", 1)[0]
            if r.startswith("sec-"):
                nid = next((x for x in notes if notes[x].sec_label == r), None)
                if r in self.printed:
                    return "@" + r
                return notes[nid].display_title if nid else r
            if pre == "prob":
                nid = owner.get(r)
                where = f" in {notes[nid].display_title}" if nid in notes else ""
                return f"Exercise {r.rsplit('-', 1)[-1].lstrip('0')}{where}"
            if r in self.printed and pre in ("def", "thm", "prp", "lem", "cor", "exm", "fig"):
                return "@" + r
            nid = owner.get(r)
            name = notes[nid].blocks.get(r, "") if nid in notes else ""
            word = WORD.get(pre, "")
            return f"{word} ({name})" if name else (f"{word} in {notes[nid].display_title}" if nid in notes else word)
        return REF.sub(ref, md)


def boxed(md: str) -> str:
    """Wrap each top-level definition, result and example (with the proof that
    follows it) in a coloured box, like the website."""
    lines = md.split("\n")
    units = []
    for d in divs_in(md):
        if d.depth:
            continue
        if d.has("proof") and not d.has("remark") and units and units[-1][2] == d.line - 2:
            units[-1][2] = d.end - 1
            continue
        pre = (d.id or "").split("-", 1)[0]
        if pre in BOX_COLOR:
            units.append([BOX_COLOR[pre], d.line - 1, d.end - 1])
    for color, a, b in reversed(units):
        lines[b + 1:b + 1] = ["", "```{=latex}", "\\end{stbox}", "```"]
        lines[a:a] = ["```{=latex}", f"\\begin{{stbox}}{{{color}}}", "```", ""]
    return "\n".join(lines)


def lift_plain_ids(text: str) -> str:
    """Quarto rejects ids on remarks/claims (rmk-, clm-); drop them for the PDF."""
    return re.sub(r"^(:{3,}\s*\{)#(?:rmk|clm)-[\w-]+\s*", r"\1", text, flags=re.M)


# ---------------------------------------------------------------- render
def default_name(o: Options) -> str:
    parts = [o.scope.replace("course:", "").replace("branch:", "branch-").replace("/", "-")]
    if o.only != "all":
        parts.append(o.only)
    if o.extra == "omit":
        parts.append("no-extra")
    if o.solutions != "end":
        parts.append(f"solutions-{o.solutions}")
    if set(o.level.split(",")) != set(LEVELS):
        parts.append(o.level.replace(",", "-"))
    if o.paper != "a4":
        parts.append(o.paper)
    if o.style != "color":
        parts.append(o.style)
    if o.layout != "book":
        parts.append(o.layout)
    if o.margin != 2.2:
        parts.append(f"margin{o.margin:g}")
    return "-".join(parts)


def render(md: str, title: str, name: str, o: Options) -> Path:
    if o.markdown_only:
        dest = OUT / f"{name}.qmd"
        dest.write_text(f"% {title}\n\n" + md, encoding="utf-8")
        return dest
    work = OUT / f"{name}.build"
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)
    (work / "header.tex").write_text(HEADER + (COLOR_HEADER if o.style == "color" else ""), encoding="utf-8")
    front = {"title": title, "format": {"pdf": {
        "documentclass": "book" if o.layout == "book" else "article",
        "geometry": (["inner=" + str(o.margin + 0.4) + "cm", "outer=" + str(o.margin) + "cm"]
                     if o.layout == "book" else ["left=" + str(o.margin) + "cm", "right=" + str(o.margin) + "cm"])
                    + ["top=" + str(o.margin + 0.3) + "cm", "bottom=" + str(o.margin + 0.5) + "cm"],
        "papersize": o.paper, "toc": True, "toc-depth": 2,
        "number-sections": False, "toc-title": "Contents", "pdf-engine": "xelatex", "include-in-header": "header.tex",
        "fontsize": "11pt", "linkcolor": "black", "urlcolor": "black", "colorlinks": True,
        "keep-tex": bool(o.keep)}},
        "crossref": {"chapters": False}}
    qmd = work / f"{name}.qmd"
    qmd.write_text("---\n" + yaml.safe_dump(front, allow_unicode=True, sort_keys=False) + "---\n\n" + md,
                   encoding="utf-8")
    r = subprocess.run(["quarto", "render", qmd.name, "--to", "pdf"], cwd=work, capture_output=True, text=True)
    pdf = work / f"{name}.pdf"
    if r.returncode != 0 or not pdf.exists():
        log = (r.stdout + r.stderr).strip().splitlines()
        print("\n".join(log[-25:]), file=sys.stderr)
        raise SystemExit(f"PDF build failed for {name} (sources kept in {work})")
    dest = OUT / f"{name}.pdf"
    shutil.copy2(pdf, dest)
    if not o.keep:
        shutil.rmtree(work)
    return dest


def build(o: Options) -> list[Path]:
    repo = load()
    book = Book(repo, o)
    name = o.name or default_name(o)
    scope_title = {"book": "Study Notes"}.get(o.scope) or (
        f"{book.course.code}" if o.scope.startswith("course:") else book.chapters[0][0])
    kind = {"all": "", "summaries": ": Chapter summaries", "exercises": ": Exercises"}[o.only]
    out = [render(book.markdown(), scope_title + kind, name, o)]
    if o.solutions == "separate" and book.solutions_only:
        out.append(render(book.finish("# Solutions\n\n" + "\n\n".join(book.solutions_only)),
                          scope_title + kind + ": Solutions", name + "-solutions", o))
    return out


def main(argv: list[str]) -> int:
    o, presets = parse(argv)
    OUT.mkdir(parents=True, exist_ok=True)
    runs = [preset_options(p) for p in presets] or [o]
    for opts in runs:
        if presets:
            opts.keep, opts.markdown_only = o.keep, o.markdown_only
        for path in build(opts):
            print(f"wrote {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
