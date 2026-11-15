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
  --branches a,b,...          with book scope: only these branches (ids or last part)
  --chapters 1,3,...          with course scope: only these course chapters
  --notes id,id,...           only these knowledge points (within the scope)
  --include TYPES             block types to print, comma-separated, from
                              def,result,proof,example,remark,figure,exercise,synthesis
                              (default: all of them)
  --toc yes | no              table of contents                      (default: yes)
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
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

import kinds
from model import ROOT, load

OUT = ROOT / "out" / "pdf"
FIGURES = (Path(__file__).resolve().parent / "figures.tex").read_text(encoding="utf-8")
HEADER = FIGURES + r"""
\usepackage{algorithm}
\usepackage{algorithmic}
\providecommand{\INPUT}{\item[\textbf{Input:}]}
\providecommand{\OUTPUT}{\item[\textbf{Output:}]}
% exercises: "Exercise n" in bold (accent colour in the colour style), source and
% level small and italic on the right; space between exercises, no boxes
\providecommand{\exercisecolor}{black}
\newcommand{\exercisehead}[3]{\par\bigskip\noindent
  {\bfseries\color{\exercisecolor}#1 #2}\hfill{\small\itshape #3}\par\nopagebreak\smallskip}
% numbered titles are written by numbering.py; thmheadc colours them
\colorlet{thmheadc}{black}
"""
# --style color: the website's look. Colours are the ones in figures.tex
# (defc blue, thmc terracotta, exc green), so web, figures and PDF match.
COLOR_HEADER = r"""
\usepackage[most]{tcolorbox}
\newtcolorbox{stbox}[1]{enhanced, breakable, frame hidden, sharp corners, boxrule=0pt,
  colback=#1!5!white, borderline west={2pt}{0pt}{#1}, left=8pt, right=6pt, top=3pt, bottom=3pt,
  before skip=8pt, after skip=8pt, before upper={\colorlet{thmheadc}{#1}}}
\renewcommand{\exercisecolor}{thmc}
"""
LEVELS = ("easy", "medium", "hard", "unrated")
TYPES = tuple(g for g, _ in kinds.GROUPS)

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


from book import Book  # noqa: E402


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
    name: str | None = None
    keep = False
    markdown_only = False
    branches = ""
    chapters = ""
    notes = ""
    include = ",".join(("def", "result", "proof", "example", "remark", "figure", "exercise", "synthesis"))
    toc = "yes"


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
    ap.add_argument("--branches", default="")
    ap.add_argument("--chapters", default="")
    ap.add_argument("--notes", default="")
    ap.add_argument("--include", default=Options.include)
    ap.add_argument("--toc", choices=["yes", "no"], default="yes")
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
        "papersize": o.paper, "toc": o.toc == "yes", "toc-depth": 2,
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
        book.course.code if (o.scope.startswith("course:") and book.course) else book.chapters[0][0])
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
