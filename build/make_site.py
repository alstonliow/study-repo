#!/usr/bin/env python3
"""Generate the Quarto website sources under site/ from notes/.

- One page per knowledge point: note.md, then example.md, then the problems of
  exercise.md, each followed by its solution (collapsed).
- Cross-page @-references become links; same-page ones stay Quarto xrefs.
- Raw LaTeX drawings (```{=latex} blocks) are compiled to SVG and cached in
  site/tikz/ (keyed by content hash).
- Course scope comes from meta/courses/*.yml through the model (SPEC §13):
  blocks outside a course's scope are wrapped so the course filter can fold them.
- Writes site/notes/**, site/courses/**, site/index.qmd, site/_nav.yml and
  site/site-data.json (all generated).

Read-only with respect to notes/. Never runs git.
"""

from __future__ import annotations

import hashlib
import os
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

import graphs
import summaries
from model import (MATH, NOTES, OPEN, RAW, REF, ROOT, Note, Repo, attrs_of, divs_in, fence_for,
                   load, top_level_divs)

SITE = Path(os.environ.get("STUDY_SITE") or ROOT / "site").resolve()   # tests write elsewhere
OUT_NOTES = SITE / "notes"
OUT_COURSES = SITE / "courses"
TIKZ = SITE / "tikz"
TYPE_WORD = {"def": "Definition", "thm": "Theorem", "prp": "Proposition",
             "lem": "Lemma", "cor": "Corollary", "exm": "Example", "prob": "Exercise", "fig": "Figure",
             "rmk": "Remark", "clm": "Claim"}

FIGURES = (Path(__file__).resolve().parent / "figures.tex").read_text(encoding="utf-8")
TIKZ_PREAMBLE = ("\\documentclass[varwidth=16cm,border=4pt]{standalone}\n"
                 "\\usepackage[utf8]{inputenc}\n" + FIGURES)

def page_url(nid: str) -> str:
    return f"/notes/{nid}.qmd"


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


def link_refs(text: str, here: Note, notes: dict[str, Note], owner: dict[str, str]) -> str:
    """Turn @-references into links, except inside maths, where a Markdown link
    would show as raw text: there the reference becomes its plain title
    (check.py reports such references as errors)."""
    def plain(m):
        ref = m.group(1)
        nid = next((n for n in notes if "sec-" + n.replace("/", "-") == ref), None) if ref.startswith("sec-") else owner.get(ref)
        title = notes[nid].title if nid else ref
        return title.replace("\\", "").replace("{", "").replace("}", "")
    out, last = [], 0
    for m in MATH.finditer(text):
        out.append(REF.sub(lambda r: link_for(r.group(1), here, notes, owner), text[last:m.start()]))
        out.append(REF.sub(plain, m.group(0)))
        last = m.end()
    out.append(REF.sub(lambda r: link_for(r.group(1), here, notes, owner), text[last:]))
    return "".join(out)


def render_problems(note: Note, courses_of=None, keep=None) -> str:
    """Exercises of a note (or review folder) with collapsed solutions.
    courses_of(pid) -> course ids (default: the note's scope); keep(pid) -> bool
    drops problems (used by course summaries)."""
    courses_of = courses_of or (lambda pid: REPO.block_courses(note, pid))
    sols = {a.get("for"): body for a, body in top_level_divs(note.solutions) if "solution" in a["classes"]}
    draft = {a.get("for") for a, _ in top_level_divs(note.solutions)
             if "solution" in a["classes"] and a.get("status") == "draft"}
    out = []
    num = 0
    for a, body in top_level_divs(note.exercises):
        if "problem" not in a["classes"]:
            continue
        pid = a["id"]
        num += 1                      # exercises are numbered 1, 2, 3, ... on each page
        if keep and not keep(pid):
            continue
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
        cs = " ".join(courses_of(pid))
        lv = a.get("level", "")
        out.append(f'{fo} {{.problem-group data-courses="{cs}" data-item="{pid}" data-level="{lv}"}}\n{inner}\n{fo}\n')
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


def lift_plain_ids(text: str) -> str:
    """Quarto treats an id on a remark/claim as a cross-reference target and
    fails on the unnumbered rmk-/clm- prefixes (SPEC §5.1). Move such ids to a
    plain wrapper div, which keeps the anchor in the page."""
    lines = text.split("\n")
    for d in reversed(divs_in(text)):
        if not d.id or d.id.split("-", 1)[0] not in ("rmk", "clm"):
            continue
        i, j = d.line - 1, d.end - 1
        m = OPEN.match(lines[i])
        attrs = re.sub(r"(?:^|\s)#" + re.escape(d.id) + r"(?=\s|$)", "", m.group(2), count=1).strip()
        ind0 = re.match(r"[ \t]*", lines[i]).group(0)
        lines[i] = f"{ind0}{m.group(1)} {{{attrs}}}"
        inner = "\n".join(lines[i:j + 1])
        f = fence_for(inner)
        ind = re.match(r"[ \t]*", lines[i]).group(0)
        lines[i:j + 1] = [f"{ind}{f} {{#{d.id} .block}}"] + lines[i:j + 1] + [f"{ind}{f}"]
    return "\n".join(lines)


def wrap_scope(text: str, note: Note) -> str:
    """Wrap each top-level block (with the proof after it) whose course scope
    differs from its note's, so the course filter can fold it (SPEC §13.5).
    data-courses lists the courses whose scope includes the block."""
    page = REPO.note_courses(note)
    if not page:
        return text
    lines = text.split("\n")
    units: list[list] = []   # [scope id, first line, last line, label]
    for d in divs_in(text):
        if d.depth:
            continue
        if d.has("proof") and not d.has("remark") and units:
            units[-1][2] = d.end - 1
            continue
        word = TYPE_WORD.get((d.id or "").split("-", 1)[0], "")
        label = f"{word}: {d.name}" if word and d.name else word
        units.append([d.id, d.line - 1, d.end - 1, label])
    for bid, i, j, label in reversed(units):
        if bid is None:
            continue
        cs = REPO.block_courses(note, bid)
        if cs == page:
            continue
        inner = "\n".join(lines[i:j + 1])
        f = fence_for(inner)
        lab = label.replace('"', "&quot;")
        kind = bid.split("-", 1)[0]
        lines[i:j + 1] = [f'{f} {{.scope-block data-courses="{" ".join(cs)}" data-kind="{kind}" data-label="{lab}"}}'] + \
            lines[i:j + 1] + [f]
    return "\n".join(lines)


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


SVGS: dict[str, str | None] = {}   # drawing source -> compiled SVG file name (set in main)


def transform(body: str, here) -> str:
    """Turn note Markdown into page Markdown: drawings, plain ids, claims,
    example levels and @-references. `here` is the page's note (or any object
    with `blocks`, for pages that own no blocks)."""
    def raw_sub(m):
        ind = m.group(1)
        if is_algorithm(m.group(2)):
            # algorithms are typeset in the browser by pseudocode.js (site/pseudocode.html)
            src = html.escape(textwrap.dedent(m.group(2)), quote=False)
            return "\n".join(ind + l for l in ["```{=html}", f'<pre class="pseudocode">{src}</pre>', "```"])
        name = SVGS.get(textwrap.dedent(m.group(2)))
        inner = f"![](/tikz/{name}){{width={svg_width(name)}px}}" if name else "*(Figure available in the PDF version.)*"
        return "\n".join(ind + l for l in ["::: {.tikz-figure}", inner, ":::"])
    body = RAW.sub(raw_sub, body)
    body = lift_plain_ids(body)
    body = fix_claims(body)
    body = add_example_levels(body)
    return link_refs(body, here, REPO.notes, REPO.owner)


def build_page(note: Note, notes: dict[str, Note], owner: dict[str, str], svgs: dict[str, str | None]) -> str:
    body_text = wrap_scope(note.body.strip(), note)
    if note.num:
        counter = iter(range(1, 1000))
        body_text = re.sub(r"(?m)^## (?!#)(.+)$",
                           lambda m: f"## {note.num}.{next(counter)} {m.group(1)}", body_text)
    parts = [body_text]
    if note.examples.strip():
        parts.append("## Examples\n\n" + wrap_scope(note.examples.strip(), note))
    if note.exercises.strip():
        parts.append("## Exercises\n\n" + render_problems(note))
    body = transform("\n\n".join(parts), note)

    meta = []
    if note.front.get("sources"):
        meta.append("Sources: " + ", ".join(f"`{s}`" for s in note.front["sources"]))
    reqs = [r for r in note.front.get("requires") or [] if r in notes]
    if reqs:
        meta.append("Prerequisites: " + ", ".join(f"[{notes[r].display_title}]({page_url(r)})" for r in reqs))
    nexts = REPO.dependents(note.id)
    if nexts:
        meta.append("Leads to: " + ", ".join(f"[{notes[r].display_title}]({page_url(r)})" for r in nexts))
    if note.front.get("status") == "draft":
        meta.append("Status: draft")
    front = {"title": note.display_title}
    if note.aliases:   # redirect pages at the old addresses of a moved note
        front["aliases"] = [f"/notes/{a}.html" for a in note.aliases]
    head = "---\n" + yaml.safe_dump(front, allow_unicode=True) + "---\n\n"
    if meta:
        head += "[" + " · ".join(meta) + "]{.note-meta}\n\n"
    return head + body + "\n"


def branch_page(bid: str, btitle: str, members: list, bnum: int) -> str:
    """Numbered, book-style contents for one branch."""
    nex = sum(len(n.problem_sources) for n in members)
    counts = f"{len(members)} topics" + (f" · {nex} exercises" if nex else "")
    desc = REPO.branch_desc.get(bid, "")
    lines = ["---", yaml.safe_dump({"title": f"{bnum} {btitle}"}, allow_unicode=True).strip(), "---", "",
             f"[{desc + '. ' if desc else ''}{counts}]{{.branch-intro}}", "",
             "::: {.branch-toc}"]
    for n in members:
        items = n.key_items
        shown = " · ".join(items[:6]) + (" · …" if len(items) > 6 else "")
        lines.append(f"- [{n.num}]{{.toc-num}} [{n.title}]({page_url(n.id)})" +
                     (f" [{shown}]{{.toc-desc}}" if shown else ""))
    lines += [":::", "", "[Summary of this branch: definitions, results and all exercises →](summary.qmd)"
              "{.chapter-summary-link}", ""]
    graph = dep_graph([n.id for n in members], f"notes/{bid}/index.html")
    if graph:
        lines += ["## Prerequisites", "",
                  "[Arrows point from a prerequisite to the topics that need it. "
                  "Faded boxes are prerequisites from other branches. Colours follow your progress marks.]"
                  "{.graph-note}", "", graph, ""]
    return "\n".join(lines)


def rel_href(from_page: str, to_page: str) -> str:
    """Relative link between two site pages (raw HTML is not rewritten by Quarto)."""
    import posixpath
    return posixpath.relpath(to_page, posixpath.dirname(from_page))


def dep_graph(ids: list[str], page: str, with_outside: bool = True, across: bool = False) -> str:
    """Raw-HTML block with the prerequisite graph of the notes `ids`; their
    prerequisites outside `ids` are added faded when with_outside."""
    inside = list(ids)
    outside = []
    if with_outside:
        for n in ids:
            for r in REPO.requires(n):
                if r not in inside and r not in outside:
                    outside.append(r)
    nodes = outside + inside
    edges = [(r, n) for n in inside for r in REPO.requires(n) if r in nodes]
    if not edges and len(nodes) < 2:
        return ""
    notes = REPO.notes
    label = {n: notes[n].display_title for n in nodes}
    href = {n: rel_href(page, f"notes/{n}.html") for n in nodes}
    svg = graphs.svg(nodes, edges, label, href, faded=set(outside), across=across)
    raw = "```{=html}\n<div class=\"dep-graph-wrap\">\n" + svg + "\n</div>\n```"
    return f"::: {{.column-screen-inset-right}}\n{raw}\n:::" if across else raw


def write_downloads() -> None:
    """Downloads page for the PDFs in out/pdf/ (built by build/make_pdf.py),
    copied to site/pdf/. Only PDFs that exist are listed."""
    import make_pdf
    src, dest = ROOT / "out" / "pdf", SITE / "pdf"
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    rows = []
    for name in make_pdf.all_presets():
        pdf = src / f"{name}.pdf"
        if not pdf.exists():
            continue
        shutil.copy2(pdf, dest / pdf.name)
        desc = make_pdf.DESCRIPTIONS.get(name) or "Branch: " + name[len("branch-"):].replace("-", " ").capitalize()
        extra = ""
        sol = src / f"{name}-solutions.pdf"
        if sol.exists():
            shutil.copy2(sol, dest / sol.name)
            extra = f" · [solutions](pdf/{sol.name})"
        rows.append(f"| [{name}.pdf](pdf/{pdf.name}){extra} | {desc} | {pdf.stat().st_size // 1024} KB |")
    lines = ["---", "title: PDF downloads", "---", "",
             "Printable versions of the notes, rebuilt with every update of the website.", ""]
    if rows:
        lines += ["| File | Contents | Size |", "|---|---|---|"] + rows
    else:
        lines += ["*No PDFs have been built yet.* Run `make pdf` to build them locally."]
    lines += ["", "## Other combinations", "",
              "Use the [Export](export.qmd) page to tick exactly what you want: save it as a PDF from the "
              "browser, or copy the options for a LaTeX PDF built on GitHub. The same options work locally:", "",
              "```bash",
              "python3 build/make_pdf.py --scope course:fit1058 --solutions separate --extra omit --style plain",
              "python3 build/make_pdf.py --scope branch:math/discrete/graph --only exercises --level medium,hard",
              "```", "",
              "Options: `--scope` book, branch or course · `--solutions` inline, end, separate or none · "
              "`--extra` include or omit · `--only` all, summaries or exercises · `--level` · "
              "`--paper` a4 or letter · `--style` color or plain. See `python3 build/make_pdf.py --help`.", ""]
    (SITE / "downloads.qmd").write_text("\n".join(lines), encoding="utf-8")


def ctx():
    """What summaries.py needs from the site build."""
    from types import SimpleNamespace
    return SimpleNamespace(fence_for=fence_for, page_url=page_url, transform=transform,
                           render_problems=render_problems, dep_graph=dep_graph,
                           block_courses=REPO.block_courses, review_courses=REPO.review_courses)


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


REPO: Repo


def main() -> int:
    global REPO
    REPO = load()
    notes = REPO.notes
    owner = REPO.owner
    BRANCHES = REPO.parts
    for n in notes.values():
        n.courses = REPO.note_courses(n)

    # compile drawings
    TIKZ.mkdir(parents=True, exist_ok=True)
    codes = sorted({textwrap.dedent(m.group(2)) for n in notes.values()
                    for t in (n.body, n.examples, n.exercises, n.solutions) for m in RAW.finditer(t)
                    if not is_algorithm(m.group(2))})
    with ThreadPoolExecutor(max_workers=6) as pool:
        svgs = dict(zip(codes, pool.map(compile_svg, codes)))
    SVGS.update(svgs)
    failed = sum(1 for v in svgs.values() if v is None)
    print(f"drawings: {len(codes)} ({failed} failed)")

    branch_num = REPO.number_notes()

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
    summary_courses: dict[str, list[str]] = {}
    home = ["---", "title: Study Notes", "---", "",
            "Personal study notes, organised by topic rather than by course. "
            "So far: discrete mathematics and discrete probability.", ""]
    for field, branches in BRANCHES:
        sec = {"section": field, "contents": []}
        rows = []
        for bid, btitle in branches:
            members = REPO.branch_members(bid)
            if not members:
                continue
            branch_items[bid] = [n.id for n in members]
            index = OUT_NOTES / bid / "index.qmd"
            index.parent.mkdir(parents=True, exist_ok=True)
            index.write_text(branch_page(bid, btitle, members, branch_num[bid]), encoding="utf-8")
            review = [REPO.reviews[bid]] if bid in REPO.reviews else []
            (OUT_NOTES / bid / "summary.qmd").write_text(summaries.page(
                f"{branch_num[bid]} {btitle}: Summary",
                f"Definitions, results and exercises of {btitle}, with synthesis problems at the end. "
                "Use the filters to choose what to see; print this page for a review sheet.",
                members, review, ctx(), f"notes/{bid}/summary.html"), encoding="utf-8")
            summary_courses[f"notes/{bid}/summary.html"] = sorted({c for n in members for c in n.courses})
            sec["contents"].append({"section": f"{branch_num[bid]} {btitle}", "href": f"notes/{bid}/index.qmd",
                                    "contents": [f"notes/{n.id}.qmd" for n in members]
                                    + [f"notes/{bid}/summary.qmd"]})
            rows.append((f"notes/{bid}/index.html", btitle, REPO.branch_desc.get(bid, ""), branch_num[bid]))
        home += contents_block(field, rows)
        sidebar.append(sec)
    # course pages: knowledge points in course order, grouped by the course's chapters
    if OUT_COURSES.exists():
        shutil.rmtree(OUT_COURSES)
    OUT_COURSES.mkdir(parents=True)
    page_courses = {}
    course_rows = []
    course_order = {}  # course id -> [{"title": chapter heading, "num", "pages": [note html paths]}]
    for c in REPO.courses:
        label = c.code + (f" – {c.name}" if c.name else "")
        lines = ["---", yaml.safe_dump({"title": label}, allow_unicode=True).strip(), "---", "",
                 f"Knowledge points used by {c.code}, in course order. "
                 "The course filter at the bottom of the sidebar shows only this course's content.", ""]
        points_of: dict[str, list[str]] = {}
        for p in c.points:
            for ref in p.covers:
                nid = ref if ref in notes else REPO.owner.get(ref)
                if nid and p.id not in points_of.setdefault(nid, []):
                    points_of[nid].append(p.id)
        chapter = None
        course_order[c.id] = []
        for nid, point in c.order:
            n = notes[nid]
            if point.chapter != chapter:
                chapter = point.chapter
                ch = next(x for x in c.chapters if x["num"] == chapter)
                heading = f"Chapter {chapter}" + (f" · {ch['title']}" if ch["title"] else "")
                summary = f"courses/{c.id}/chapter-{chapter}"
                lines += ["", f"## {heading}", "", f"[Chapter summary →](/{summary}.qmd){{.chapter-summary-link}}", ""]
                course_order[c.id].append({"title": heading, "num": chapter, "pages": [],
                                           "summary": summary + ".html"})
            course_order[c.id][-1]["pages"].append(f"notes/{n.id}.html")
            nprob = sum(1 for pr in n.problems if c.id in REPO.block_courses(n, pr.id))
            extra = f" ({nprob} exercise{'s' if nprob != 1 else ''})" if nprob else ""
            pts = ", ".join("§" + x for x in points_of.get(nid, []))
            lines.append(f"- [{n.display_title}](/notes/{n.id}.qmd){extra} [{pts}]{{.note-keys}}")
        (OUT_COURSES / f"{c.id}.qmd").write_text("\n".join(lines) + "\n", encoding="utf-8")
        # chapter summaries: in-scope content only; a branch's synthesis problems
        # go to the last chapter of the course that uses the branch
        last_chapter = {}
        for nid, point in c.order:
            last_chapter[notes[nid].branch] = point.chapter
        (OUT_COURSES / c.id).mkdir(exist_ok=True)
        for chap in course_order[c.id]:
            members = [notes[pg[len("notes/"):-len(".html")]] for pg in chap["pages"]]
            reviews = [REPO.reviews[b] for b, last in last_chapter.items()
                       if last == chap["num"] and b in REPO.reviews]
            (OUT_COURSES / c.id / f"chapter-{chap['num']}.qmd").write_text(summaries.page(
                f"{c.code} {chap['title']}: Summary",
                f"Everything {c.code} needs from this chapter: definitions, results and exercises in course "
                "order, with synthesis problems at the end. Use the filters; print for a review sheet.",
                members, reviews, ctx(), chap["summary"], course=c,
                in_scope=lambda n, bid, c=c: REPO.in_scope(c, n.id, bid)), encoding="utf-8")
            summary_courses[chap["summary"]] = [c.id]
        course_rows.append((f"courses/{c.id}.html", c.code, c.name or "Knowledge points in course order", ""))
        page_courses[f"courses/{c.id}.html"] = [c.id]
    if course_rows:
        home += contents_block("Courses", course_rows)
    for n in notes.values():
        page_courses[f"notes/{n.id}.html"] = n.courses
    page_courses.update(summary_courses)

    # one data file for the page scripts (site/site-data.html): courses, scope,
    # course order, and the topics and exercises used by progress tracking
    import json
    (SITE / "site-data.json").write_text(json.dumps({
        "courses": [{"id": c.id, "code": c.code, "name": c.name, "status": c.status} for c in REPO.courses],
        "pages": page_courses, "order": course_order,
        "branches": branch_items,
        "notes": {n.id: [pr.id for pr in n.problems] for n in notes.values()},
        "aliases": REPO.alias_of,
        # for the Export page (site/export.html)
        "titles": {n.id: n.display_title for n in notes.values()},
        "branchTitles": {bid: f"{branch_num[bid]} {t}" for _, bs in REPO.parts for bid, t in bs if bid in branch_num},
        "reviews": sorted(REPO.reviews),
        "repoUrl": ((yaml.safe_load((SITE / "_quarto.yml").read_text(encoding="utf-8")) or {})
                    .get("website", {}).get("repo-url", "") if (SITE / "_quarto.yml").exists() else ""),
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    for old in ("courses.json", "progress.json"):
        if (SITE / old).exists():
            (SITE / old).unlink()

    (SITE / "index.qmd").write_text("\n".join(home) + "\n", encoding="utf-8")
    all_ids = REPO.topic_order()
    (SITE / "map.qmd").write_text(
        "---\ntitle: Map of topics\n---\n\n"
        "[Every knowledge point and its prerequisites. Arrows point from a prerequisite to the topics "
        "that need it; click a box to open the topic. Colours follow your progress marks.]{.graph-note}\n\n"
        + dep_graph(all_ids, "map.html", with_outside=False, across=True) + "\n", encoding="utf-8")
    write_downloads()
    (SITE / "export.qmd").write_text(
        "---\ntitle: Export\n---\n\n"
        "[Choose what to print. **Save as PDF** prints from the browser, at once and in any combination "
        "(including your progress marks). **LaTeX PDF** gives the options for a typeset PDF built on GitHub.]"
        "{.summary-intro}\n\n"
        "[$\\,$]{.d-none}\n\n"                       # loads MathJax for the assembled content
        "```{=html}\n<div class=\"export-builder\"></div>\n<div id=\"export-output\"></div>\n```\n",
        encoding="utf-8")
    navbar = [{"href": "index.qmd", "text": "Home"}, {"href": "map.qmd", "text": "Map"},
              {"href": "export.qmd", "text": "Export"}, {"href": "downloads.qmd", "text": "PDF"}]
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
