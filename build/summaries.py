"""Chapter-end summary pages (meta/SPEC.md §14), like the review section at the
end of a textbook chapter.

One page per branch (notes/<branch>/summary.qmd), and one per chapter of each
course (courses/<course>/chapter-<n>.qmd). A page has, in order:

1. the prerequisite graph of its notes, coloured by progress;
2. definitions and results (definition, theorem, proposition, lemma,
   corollary): statements only, each linking back to its note;
3. all exercises of its notes;
4. synthesis problems from the branch's review/ folder.

Every item carries data attributes for the filter bar (site/_assets/summary.html):
data-kind (def, result, exercise, synthesis), data-item (note or problem id),
data-level. Rendering is delegated to make_site (`ctx`), so a summary looks
exactly like the notes it comes from.
"""

from __future__ import annotations

from types import SimpleNamespace

import yaml

from kinds import SUMMARY_PREFIXES, word
NO_BLOCKS = SimpleNamespace(blocks={})   # a summary owns no blocks: every reference becomes a link


def statements(note, keep=lambda bid: True) -> list:
    """Top-level definition and result blocks of a note, in order."""
    f = note.files.get("note.md")
    if not f:
        return []
    out = []
    for d in f.divs:
        if d.depth or not d.id:
            continue
        pre = d.id.split("-", 1)[0]
        if pre in SUMMARY_PREFIXES and keep(d.id):
            out.append(d)
    return out


def item(note, d, ctx, courses: list[str] | None) -> str:
    pre = d.id.split("-", 1)[0]
    kind = "def" if pre == "def" else "result"
    body = d.body.strip()
    fence = ctx.fence_for(body)
    q = lambda t: t.replace('"', "&quot;")       # attribute values
    number = ctx.block_number(d.id, note.id)
    head = f"[{word(d.id)}{' ' + number if number else ''}]{{.summary-kind}}" + (f" {d.name}" if d.name else "") + \
        f" [→]({ctx.page_url(note.id)}#{d.id}){{.summary-src title=\"{q(note.display_title)}\"}}"
    cls = f".summary-item .k-{pre} .scope-block" if courses is not None else f".summary-item .k-{pre}"
    attrs = f'data-kind="{kind}" data-item="{note.id}"' + \
        (f' data-courses="{" ".join(courses)}" data-label="{q(word(d.id) + ": " + d.name)}"' if courses is not None else "")
    return f"{fence} {{{cls} {attrs}}}\n{head}\n\n{body}\n{fence}\n"


def heading(note, ctx) -> str:
    """A plain sub-heading for a note, with a small link to it; the number is
    marked so the course filter can switch it (site/_assets/filter.html)."""
    number = f'[{note.num}]{{.num data-note="{note.id}"}} ' if note.num else ""
    return f"### {number}{note.title} [→]({ctx.page_url(note.id)}){{.summary-src title=\"Open the note\"}}"


def page(title: str, intro: str, notes: list, reviews: list, ctx, page_path: str,
         course=None, in_scope=None) -> str:
    """Markdown for one summary page.

    notes: notes in order; reviews: review folders whose synthesis problems go at
    the end; course: when given (course chapter page), only blocks and problems
    in that course's scope are listed; in_scope(note, bid) decides."""
    keep_block = (lambda n: (lambda bid: in_scope(n, bid))) if course else (lambda n: (lambda bid: True))
    lines = ["---", yaml.safe_dump({"title": title}, allow_unicode=True).strip(), "---", "",
             f"[{intro}]{{.summary-intro}}", "",
             "```{=html}", '<div class="summary-filters" hidden></div>', "```", ""]

    graph = ctx.dep_graph([n.id for n in notes], page_path)
    if graph:
        lines += ["## Prerequisites", "", graph, ""]

    lines += ["## Definitions and results", ""]
    for n in notes:
        items = statements(n, keep_block(n))
        if not items:
            continue
        lines += [heading(n, ctx), ""]
        for d in items:
            courses = None if course else ctx.block_courses(n, d.id)
            lines.append(ctx.transform(item(n, d, ctx, courses), NO_BLOCKS))

    ex = []
    for n in notes:
        keep = (lambda n: lambda pid: in_scope(n, pid))(n) if course else None
        probs = ctx.render_problems(n, keep=keep, origin=True)
        if probs.strip():
            ex += [heading(n, ctx), "", ctx.transform(probs, NO_BLOCKS), ""]
    if ex:
        lines += ["## Exercises", ""] + ex

    syn = []
    for rv in reviews:
        probs = ctx.render_problems(rv, courses_of=lambda pid, b=rv.branch: ctx.review_courses(b, pid))
        if probs.strip():
            syn.append(ctx.transform(probs.replace('{.problem-group ', '{.problem-group .synthesis '), NO_BLOCKS))
    if syn:
        lines += ["## Synthesis problems", "",
                  "[Problems that combine several topics of the chapter.]{.summary-intro}", ""] + syn
    return "\n".join(lines) + "\n"
