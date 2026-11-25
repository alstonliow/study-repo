"""Website page rendering: note pages, exercises, scope folds, branch pages,
prerequisite graphs and the downloads page. make_site.py calls setup() once,
then these page functions; shared logic lives in the model and its helpers
(outline, refs, filters, transforms, summaries, tikz)."""

from __future__ import annotations

import os
import html
import shutil
import textwrap
from pathlib import Path

import yaml
from dataclasses import dataclass
from types import SimpleNamespace
from typing import Callable

import graphs
import kinds
import numbering
import tikz
import refs
import relations
from transforms import (add_example_levels, caption_figures, fix_claims, level_badge, title_blocks,
                        wrap_plain_ids)
from model import (MATH, RAW, REF, ROOT, Coding, Note, Repo, divs_in, fence_for, top_level_divs)

SITE = Path(os.environ.get("STUDY_SITE") or ROOT / "site").resolve()   # tests write elsewhere
OUT_NOTES = SITE / "notes"
OUT_COURSES = SITE / "courses"
TIKZ = SITE / "tikz"

REPO: Repo
RESOLVER: refs.Resolver
NUMBERING: numbering.Numbering
GRAPH: relations.Graph
SVGS: dict[str, str | None] = {}   # drawing source -> compiled SVG file name


def setup(repo: Repo) -> Repo:
    """Prepare the page functions for one build."""
    global REPO, RESOLVER, NUMBERING, GRAPH
    REPO = repo
    RESOLVER = refs.Resolver(repo)
    NUMBERING = numbering.build(repo)
    GRAPH = relations.Graph(repo)
    SVGS.clear()
    BANK_LINKS.clear()
    for c in repo.courses:
        for num, banks in repo.bank_chapters(c).items():
            count: dict[str, int] = {}
            for b in banks:
                for p in b.problems:
                    for t in set(str(p.attrs.get("practises", "")).split()):
                        count[t] = count.get(t, 0) + 1
            for t, k in count.items():
                BANK_LINKS.setdefault(t, []).append((c.id, c.code, num, k))
    return repo


BANK_LINKS: dict[str, list[tuple[str, str, int, int]]] = {}   # note id -> (course, code, chapter, count)


def page_url(nid: str) -> str:
    return f"/notes/{nid}.qmd"


def library_url(rid: str) -> str:
    """A resource's page in the Library (SPEC §17.12.7)."""
    return f"/library/{rid[len('res-'):]}.qmd"


def project_url(pid: str) -> str:
    """A project's page (SPEC §17.13.5)."""
    return f"/projects/{pid[len('prj-'):]}/index.qmd"


# ---------------------------------------------------------------- TikZ -> SVG
def num(number: str, nid: str) -> str:
    """A number on the website, marked with its note so the course filter can
    show the course's number instead (site/_assets/filter.html)."""
    return f'[{number}]{{.num data-note="{nid}"}}'


def anchor(block_id: str) -> str:
    return f'<span id="{block_id}" class="anchor"></span>'


def block_title(d, holder) -> str:
    """'Theorem 8.1.2 (Name)' in Quarto's title style."""
    k = kinds.of(d.id)
    n = NUMBERING.block(d.id)
    inner = f"{k.word if k else ''} {num(n, holder.id)}" if n else (k.word if k else "")
    if d.name:
        inner += f" ({d.name})"
    return f"[**{inner}**]{{.theorem-title}}"


def figure_label(d, holder) -> str:
    n = NUMBERING.block(d.id)
    return f"[**Figure {num(n, holder.id)}:**]{{.fig-label}} " if n else ""


def link_for(ref: str, here) -> str:
    """An @-reference as a link with its numbered label (numbering.label);
    unknown targets stay as written (check.py reports them)."""
    rr = RESOLVER.resource_of(ref)
    if rr:                                   # resources and their nodes live in the Library
        res, _ = rr
        return f"[{res.label(ref)}]({library_url(res.id)}{'' if ref == res.id else '#' + ref})"
    prj = REPO.projects.get(ref)
    if prj:                                  # projects are unnumbered, shown by title (SPEC §17.13.5)
        return f"[{prj.title}]({project_url(prj.id)})"
    t = RESOLVER.find(ref)
    if t is None:
        return "@" + ref
    if t.is_note:
        return f"[{RESOLVER.describe(t)}]({page_url(t.note.id)})"
    label = NUMBERING.label(ref, t.note, here, num) if NUMBERING.block(ref) or (t.kind and t.kind.prefix == "prob") \
        else RESOLVER.describe(t)
    if ref in here.blocks:
        return f"[{label}](#{ref})"
    # synthesis problems have no page of their own; they are on the branch summary
    url = page_url(t.note.id) if t.note.id in REPO.notes else f"/notes/{t.note.branch}/summary.qmd"
    return f"[{label}]({url}#{ref})"


def link_refs(text: str, here) -> str:
    """Turn @-references into links, except inside maths, where a Markdown link
    would show as raw text: there the reference becomes its plain title
    (check.py reports such references as errors)."""
    out, last = [], 0
    for m in MATH.finditer(text):
        out.append(REF.sub(lambda r: link_for(r.group(1), here), text[last:m.start()]))
        out.append(REF.sub(lambda r: RESOLVER.title(r.group(1)), m.group(0)))
        last = m.end()
    out.append(REF.sub(lambda r: link_for(r.group(1), here), text[last:]))
    return "".join(out)


def render_problems(note: Note, courses_of=None, keep=None, origin: bool = False) -> str:
    """Exercises of a note (or review folder) with collapsed solutions.
    courses_of(pid) -> course ids (default: the note's scope); keep(pid) -> bool
    drops problems (used by course summaries); origin=True notes where each
    exercise comes from (summary pages). Exercises are numbered 1, 2, 3 on the
    page; synthesis problems are Review 8.1, 8.2 (numbering.py)."""
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
        src_label = REPO.sources.label(src) if src else ""
        if REPO.sources.url(src):        # a handout cited by its node id links to the handout (SPEC §6.4)
            src_label = f"[{src_label}]({REPO.sources.url(src)})"
        f = fence_for(body)
        badge = level_badge(a.get("level"))
        is_review = note in REPO.reviews.values()
        word = NUMBERING.exercise_word(note)
        shown = NUMBERING.exercise(note, pid, on_page=True) if is_review else str(num)
        where = [f"from {note.display_title}"] if origin and not is_review else []
        side = " · ".join(where + ([src_label] if src_label else []))
        coding = note.coding.get(pid)
        if coding:                    # statement, starter, tests (SPEC §6.4); runnable.html adds the editor
            badge += "[Code]{.code-badge}"
            body = coding_body(coding)
        group = [f"{f} {{#{pid} .problem}}\n[{word} {shown}]{{.problem-title}}"
                 f"[{side}]{{.problem-source}}{badge}\n\n{body.strip()}\n{f}\n"]
        if a.get("solution") == "withheld":
            group.append("[Solution withheld: the source asks that solutions are not published.]"
                         "{.solution-withheld}\n")
        elif sols.get(pid, "").strip():   # empty TODO stubs are not shown
            sb = sols[pid]
            f2 = fence_for(sb)
            title = "Draft solution (not yet reviewed)" if pid in draft else "Solution"
            group.append(f'{f2} {{.callout-tip collapse="true" appearance="simple" title="{title}"}}\n'
                         f"{sb.strip()}\n{f2}\n")
        inner = "\n".join(group)
        fo = fence_for(inner)
        cs = " ".join(courses_of(pid))
        lv = a.get("level", "")
        kind = ('data-kind="code"' + (f' data-lang="{coding.lang}"' if coding.lang != "python" else "")
                + f' data-packages="{",".join(coding.packages)}"' if coding else 'data-kind="written"')
        res = REPO.sources.resolve(src) if src else None     # the exercise filter groups by resource
        rid = res.resource if res else ""
        rlabel = REPO.resources[rid].title.replace('"', "'") if rid in REPO.resources else "Other"
        year = REPO.resources[rid].year_of(res.node) if res and rid in REPO.resources else ""
        ydata = f' data-year="{year}"' if year else ""          # Year facet (SPEC §17.15.7)
        if note.bank:                                            # bank facets (SPEC §17.15.10)
            ydata += bank_data(a, res)
        out.append(f'{fo} {{.problem-group data-courses="{cs}" data-item="{pid}" data-level="{lv}" {kind} '
                   f'data-source="{rid}" data-source-label="{rlabel}"{ydata}}}\n'
                   f'{inner}\n{fo}\n')
    return "\n".join(out)


def bank_data(a: dict, res) -> str:
    """Data attributes of a bank problem for the 题库 page filters: problem type,
    set (the kind of its source node: exercises, review, paper) and the notes it
    practises, with their labels."""
    def q(x: str) -> str:
        return x.replace('"', "'").replace("|", "/")
    out = ""
    pt = REPO.problem_types.get(a.get("type", ""))
    if pt:
        out += f' data-ptype="{pt.id}" data-ptype-label="{q(pt.title_zh)} ({q(pt.title)})"'
    r = REPO.resources.get(res.resource) if res else None
    node = r.nodes.get(res.node) if r and res else None
    if node and node.kind:
        out += f' data-set="{node.kind}"'
    topics = [t for t in str(a.get("practises", "")).split() if t in REPO.notes]
    if topics:
        out += (f' data-topics="{" ".join(topics)}"'
                f' data-topic-labels="{"|".join(q(REPO.notes[t].display_title) for t in topics)}"')
    return out


def bank_page(c, chap, banks: list) -> str:
    """One course chapter's 题库 page (SPEC §17.15.10): its bank folders in
    textbook order, one section each, with the exercise filter bar."""
    title = f"题库 · {c.code} Chapter {chap['num']}" + (f" · {chap['title']}" if chap["title"] else "")
    lines = ["---", yaml.safe_dump({"title": title}, allow_unicode=True).strip(), "---", "",
             "[Textbook exercises, review exercises and past papers for this chapter, for choosing "
             "problems for handouts. Private build only.]{.note-meta}", ""]
    for b in banks:
        found = REPO.bank_node(b)
        heading = found[0].label(found[1].id) if found else b.id
        lines += [f"## {heading}", "", transform(render_problems(b, courses_of=lambda pid: []), b), ""]
    return "\n".join(lines) + "\n"


def bank_url(cid: str, num) -> str:
    return f"/courses/{cid}/bank-{num}.qmd"


def coding_body(c: Coding) -> str:
    """A coding exercise on the website: the statement, then the starter and the
    tests in marked divs that site/_assets/runnable.html turns into an editor
    (Python) or a read-only view with the tests folded (C, SPEC §6.4 item 10)."""
    starter = f"```{c.lang}\n{c.starter}\n```"
    tests = f"```{c.lang}\n{c.tests}\n```"
    return (f"{c.statement}\n\n::: {{.coding-starter}}\n{starter}\n:::\n\n"
            f"::: {{.coding-tests}}\n{tests}\n:::\n")


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
        word = kinds.word(d.id)
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




def transform(body: str, here) -> str:
    """Turn note Markdown into page Markdown: drawings, plain ids, claims,
    example levels and @-references. `here` is the page's note (or any object
    with `blocks`, for pages that own no blocks)."""
    def raw_sub(m):
        ind = m.group(1)
        if tikz.is_algorithm(m.group(2)):
            # algorithms are typeset in the browser by pseudocode.js (site/_assets/pseudocode.html)
            src = html.escape(textwrap.dedent(m.group(2)), quote=False)
            return "\n".join(ind + l for l in ["```{=html}", f'<pre class="pseudocode">{src}</pre>', "```"])
        name = SVGS.get(textwrap.dedent(m.group(2)))
        inner = f"![](/tikz/{name}){{width={tikz.svg_width(name, TIKZ)}px}}" if name else "*(Figure available in the PDF version.)*"
        return "\n".join(ind + l for l in ["::: {.tikz-figure}", inner, ":::"])
    body = add_example_levels(body)
    if getattr(here, "id", None) in REPO.notes:          # numbered titles and captions (numbering.py)
        body = title_blocks(body, lambda d: block_title(d, here), anchor)
        body = caption_figures(body, lambda d: figure_label(d, here), anchor)
    body = RAW.sub(raw_sub, body)
    body = wrap_plain_ids(body)
    body = fix_claims(body)
    return link_refs(body, here)


def at(eid: str) -> str:
    """An @-reference to any entity: blocks by id, notes by their sec- label."""
    n = REPO.notes.get(eid)
    return "@" + (n.sec_label if n else eid)


def note_relations(note: Note) -> list[tuple[str, list[str]]]:
    """Typed relationships written at the note itself (not requires, shown as
    Prerequisites), grouped by type in registry order, for the page's meta line."""
    out = []
    links = [l for l in GRAPH.outgoing(note.id) if l.name != "requires"]
    for name in GRAPH.types:
        targets = [l.other for l in links if l.name == name]
        if targets:
            out.append((name, targets))
    return out


def connections(note: Note) -> str:
    """The page's closing "Connections" section (SPEC §17.6): relationships of
    its blocks (both directions), relationships pointing to the note, and
    references from other pages. Derived from relations.Graph; written as
    @-references, so labels follow numbering and the course filter."""
    def label(eid: str) -> str:
        return "This topic" if eid == note.id else at(eid)
    rel_rows, ref_rows, applied_rows = [], [], []
    for eid in relations.page_entities(note):
        if eid != note.id:                                     # the note's own are in the meta line
            for l in GRAPH.outgoing(eid):
                rel_rows.append(f"- {label(eid)} *{GRAPH.word(l, True)}* {at(l.other)}")
        for l in GRAPH.incoming(eid):
            if l.name == "requires":                           # shown as "Leads to"
                continue
            if l.name == "practises":                          # a count link in the meta line instead
                continue
            if l.name == "applies":                            # its own group (SPEC §17.13.4)
                applied_rows.append(f"- {label(eid)} ← {at(l.other)}")
                continue
            rel_rows.append(f"- {label(eid)} *{GRAPH.word(l, False)}* {at(l.other)}")
        sources: list[str] = []
        for l in GRAPH.referenced_by.get(eid, []):
            src = l.other if l.other in REPO.entities else l.holder
            if l.holder.startswith("bank/"):                   # bank pages are not linked from notes
                continue
            if src not in sources:
                sources.append(src)
        if sources:
            ref_rows.append(f"- {label(eid)} ← " + ", ".join(at(s) for s in sources))
    if not rel_rows and not ref_rows and not applied_rows:
        return ""
    out = ["## Connections", "", "::: {.connections}"]
    if rel_rows:
        out += ["**Relationships**", ""] + rel_rows + [""]
    if applied_rows:
        out += ["**Applied in**", ""] + applied_rows + [""]
    if ref_rows:
        out += ["**Referenced by**", ""] + ref_rows + [""]
    return "\n".join(out + [":::"])


def build_page(note: Note, notes: dict[str, Note], owner: dict[str, str], svgs: dict[str, str | None]) -> str:
    body_text = wrap_scope(note.body.strip(), note)     # headings inside a note are not numbered
    parts = [body_text]
    if note.examples.strip():
        parts.append("## Examples\n\n" + wrap_scope(note.examples.strip(), note))
    if note.code.strip():
        parts.append("## Code\n\n" + wrap_scope(note.code.strip(), note))
    if note.exercises.strip():
        parts.append("## Exercises\n\n" + render_problems(note))
    conn = connections(note)
    if conn:
        parts.append(conn)
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
    for word, targets in note_relations(note):
        meta.append(f"{word.capitalize()}: " + ", ".join(link_refs(at(x), note) for x in targets))
    bank = BANK_LINKS.get(note.id)
    if bank:                                    # private build: count of bank problems (SPEC §17.15.10)
        meta.append("题库: " + ", ".join(f"[{code} Ch {num}: {k}]({bank_url(cid, num)}?topic={note.id})"
                                        for cid, code, num, k in bank))
    if note.front.get("status") == "draft":
        meta.append("Status: draft")
    front: dict[str, object] = {"title": note.display_title}
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


# ---------------------------------------------------------------- page registry
@dataclass
class Page:
    """A generated page outside the notes: its file under site/, its navbar
    text ('' = not in the navbar) and the function that writes its Markdown."""
    file: str
    nav: str
    render: Callable[[], str]


PAGES: list[Page] = []


def page(file: str, nav: str = ""):
    """Register a generated page; the navbar follows the order of registration."""
    def register(fn: Callable[[], str]) -> Callable[[], str]:
        PAGES.append(Page(file, nav, fn))
        return fn
    return register


@page("map.qmd", nav="Map")
def map_page() -> str:
    """Two-level map: one card per part, laid out in rows by prerequisite depth,
    with its branches and (on demand) their notes. Part-to-part edges are the
    note-level `requires` summed up; site/_assets/map.html draws and animates them."""
    import json
    esc = html.escape
    part_of = {bid: title for title, bs in REPO.parts for bid, _ in bs}
    field_of = {t: f for f, ts in REPO.fields for t in ts}
    slug = {t: "p-" + "".join(c if c.isalnum() else "-" for c in t.lower()) for t, _ in REPO.parts}
    weight: dict[tuple[str, str], int] = {}
    for n in REPO.topic_order():
        for r in REPO.requires(n):
            a, b = slug[part_of[REPO.notes[r].branch]], slug[part_of[REPO.notes[n].branch]]
            if a != b:
                weight[(a, b)] = weight.get((a, b), 0) + 1
    nodes = list(slug.values())
    dag = graphs.acyclic(weight)
    core = graphs.reduction(nodes, dag)
    pos = graphs.layout(nodes, dag)                     # (layer, order) -> rows top to bottom
    rows: dict[int, list[tuple[int, str]]] = {}
    for title, _ in REPO.parts:
        layer, order = pos[slug[title]]
        rows.setdefault(layer, []).append((order, title))
    branches = dict(REPO.parts)
    out = ['<div class="tmap" id="tmap">',
           '<div class="tmap-tools">'
           '<input type="search" class="tmap-search" placeholder="Find a topic…" aria-label="Find a topic">'
           '<div class="tmap-fields" role="group" aria-label="Field">'
           '<button type="button" class="active" data-field="">All</button>'
           + "".join(f'<button type="button" data-field="{esc(f)}" style="--fc:var(--field-{k % 4})">{esc(f)}</button>'
                     for k, f in enumerate(REPO.field_order()))
           + '</div><span class="tmap-legend"><i class="up"></i>needs <i class="down"></i>leads to</span></div>',
           '<div class="tmap-stage"><svg class="tmap-edges" aria-hidden="true"></svg>']
    k = 0
    for layer in sorted(rows):
        out.append('<div class="tmap-row">')
        for _, title in sorted(rows[layer]):
            field = field_of.get(title, "")
            fk = REPO.field_order().index(field) % 4 if field in REPO.field_order() else 3
            out.append(f'<section class="tmap-card" id="{slug[title]}" data-field="{esc(field)}" '
                       f'style="--i:{k};--fc:var(--field-{fk})" tabindex="-1">'
                       f'<header><span class="tmap-field">{esc(field)}</span><h3>{esc(title)}</h3>'
                       '<svg class="tmap-ring" viewBox="0 0 36 36" aria-hidden="true"><circle class="bg" r="15" cx="18" cy="18"/>'
                       '<circle class="fg" r="15" cx="18" cy="18"/></svg><span class="tmap-pct"></span></header>'
                       '<ul class="tmap-branches">')
            k += 1
            for bid, btitle in branches[title]:
                members = REPO.branch_members(bid)
                notes = "".join(f'<li><a href="{esc(rel_href("map.html", f"notes/{n.id}.html"))}" data-item="{esc(n.id)}">'
                                f'<span class="pg-dot" data-item="{esc(n.id)}"></span>{esc(n.display_title)}</a></li>'
                                for n in members)
                out.append(f'<li class="tmap-branch" data-branch="{esc(bid)}">'
                           f'<button type="button" aria-expanded="false"><span class="name">{esc(btitle)}</span>'
                           f'<span class="cnt">{len(members)}</span><span class="tmap-bar"></span></button>'
                           f'<div class="tmap-notes"><div><ol>{notes}</ol>'
                           f'<a class="tmap-open" href="{esc(rel_href("map.html", f"notes/{bid}/index.html"))}">Open branch →</a>'
                           '</div></div></li>')
            out.append('</ul></section>')
        out.append('</div>')
    data = {"edges": [[a, b, w, (a, b) in core] for (a, b), w in weight.items()]}
    out += ['</div>', f'<script type="application/json" id="tmap-data">{json.dumps(data)}</script>', '</div>']
    return ("---\ntitle: Map of topics\npage-layout: full\n---\n\n"
            "[Each card is a part; lines show which parts build on which (thicker = more links). "
            "Hover a card to trace what it needs and what it leads to; open a branch to see its topics. "
            "Colours follow your progress marks.]{.graph-note}\n\n"
            "```{=html}\n" + "\n".join(out) + "\n```\n")


# ---------------------------------------------------------------- Library (SPEC §17.12.7)
def _links(eids: list[str]) -> str:
    """Comma-separated links to entities, without repeats, in the given order."""
    seen: list[str] = []
    for e in eids:
        if e not in seen:
            seen.append(e)
    nowhere = SimpleNamespace(id=None, blocks={})
    return ", ".join(link_for(at(e)[1:], nowhere) for e in seen)


def node_links(eid: str) -> str:
    """What one resource or node is connected to, from the relationship graph:
    its relationships (covers, ...), the notes and problems citing it, and @
    references to it. Empty when it has none."""
    parts = []
    for name in GRAPH.types:
        out = [l.other for l in GRAPH.outgoing(eid) if l.name == name]
        if out:
            parts.append(f"{name.capitalize()}: " + _links(out))
    for name, t in GRAPH.types.items():
        inc = [l.other for l in GRAPH.incoming(eid) if l.name == name]
        if inc:
            parts.append(f"{t.inverse.capitalize()}: " + _links(inc))
    cited = [l.other for l in GRAPH.cited_by.get(eid, [])]
    if cited:
        parts.append("Cited by: " + _links(cited))
    refd = [l.other if l.other in REPO.entities else l.holder for l in GRAPH.referenced_by.get(eid, [])]
    if refd:
        parts.append("Referenced by: " + _links(refd))
    return " · ".join(parts)


def resource_page(res) -> str:
    """One resource: its details and hierarchy, and for each node what it covers,
    what cites it and what refers to it. Derived from the resource model and the
    relationship graph, like the Connections sections of note pages."""
    nnodes = len(res.nodes)
    courses = [c.code for c in REPO.courses if c.id in (res.meta.get("courses") or [])]
    info = [res.kind.replace("-", " ").capitalize() if res.kind else "Resource",
            f"edition {res.current}" if res.current else "", f"{nnodes} parts" if nnodes else "",
            ("used by " + ", ".join(courses)) if courses else "", "draft" if res.status == "draft" else ""]
    lines = ["---", yaml.safe_dump({"title": res.title}, allow_unicode=True).strip(), "---", "",
             "[" + " · ".join(x for x in info if x) + "]{.note-meta}", ""]
    own = node_links(res.id)
    if own:
        lines += [f"[{own}]{{.node-links}}", ""]

    def node(nid: str, depth: int) -> None:
        n = res.nodes[nid]
        loc = res.locator(nid)
        links = node_links(nid)
        if depth == 0:
            lines.extend([f"## {loc + ' ' if loc else ''}{n.title} {{#{nid}}}", ""])
            if links:
                lines.extend([f"[{links}]{{.node-links}}", ""])
        else:
            f = ":::"
            lines.extend([f"{f} {{#{nid} .resource-node}}",
                          (f"[{loc}]{{.node-loc}} " if loc else "") + f"**{n.title}**"]
                         + ([f"\n[{links}]{{.node-links}}"] if links else []) + [f, ""])
        for c in n.children:
            node(c, depth + 1)
    for root in res.roots:
        node(root, 0)
    return "\n".join(lines) + "\n"


@page("library.qmd", nav="Library")
def library_page() -> str:
    """The Library: public resources (private ones only in a private build, SPEC §17.9)."""
    rows = []
    for res in sorted(REPO.resources.values(), key=lambda r: r.title.lower()):
        covered = sum(1 for n in [res.id, *res.nodes] for l in GRAPH.outgoing(n) if l.name == "covers")
        cited = sum(len(GRAPH.cited_by.get(n, [])) for n in res.nodes)
        desc = " · ".join(x for x in [res.kind.replace("-", " ") if res.kind else "",
                                      f"{len(res.nodes)} parts" if res.nodes else "",
                                      f"{covered} topics covered" if covered else "",
                                      f"{cited} citations" if cited else ""] if x)
        rows.append(f"- [{res.title}]({library_url(res.id)})" + (f" [{desc}]{{.toc-desc}}" if desc else ""))
    return ("---\ntitle: Library\n---\n\n"
            "[Books, course notes and other resources the notes are built on. Each page shows a resource's "
            "chapters and sections, the topics each one teaches, and the notes and exercises that cite it.]"
            "{.summary-intro}\n\n" + ("\n".join(rows) if rows else "*No resources yet.*") + "\n")


# ---------------------------------------------------------------- Projects (SPEC §17.13.5)
def project_info(prj) -> str:
    """'Course · CS221 · active · draft': kind, course, stage, write-up status."""
    course = next((c.code for c in REPO.courses if c.id == prj.course), prj.course)
    return " · ".join(x for x in [prj.kind.capitalize(), course, prj.stage,
                                  "draft" if prj.status == "draft" else ""] if x)


def project_page(prj) -> str:
    """One project: details, links (assignment, code), the notes it applies and
    its backlinks, then the write-up."""
    dates = " – ".join(x for x in [prj.started, prj.finished] if x)
    lines = ["---", yaml.safe_dump({"title": prj.title}, allow_unicode=True).strip(), "---", "",
             "[" + " · ".join(x for x in [project_info(prj), dates] if x) + "]{.note-meta}", ""]
    nowhere = SimpleNamespace(id=prj.id, blocks={})
    links = []
    if prj.assignment:
        links.append("Assignment: " + link_for(prj.assignment, nowhere))
    if prj.repo.get("url"):
        commit = prj.repo.get("commit", "")
        links.append(f"Code: <{prj.repo['url']}>" + (f" at `{commit[:12]}`" if commit else ""))
    own = node_links(prj.id)
    if own:
        links.append(own)
    if links:
        lines += ["[" + " · ".join(links) + "]{.node-links}", ""]
    return "\n".join(lines) + "\n" + link_refs(prj.body.strip(), nowhere) + "\n"


def project_rows(projects) -> list[str]:
    return [f"- [{p.title}]({project_url(p.id)}) [{project_info(p)}]{{.toc-desc}}"
            for p in sorted(projects, key=lambda p: p.title.lower())]


@page("projects.qmd", nav="Projects")
def projects_page() -> str:
    """The Projects page: public projects by stage (private ones never, SPEC §17.9)."""
    from projects import STAGES
    out = ["---", "title: Projects", "---", "",
           "[Course projects and personal projects: what was built, how, and which topics "
           "it puts to work. Each project's code is in its own repository.]{.summary-intro}", ""]
    for stage in STAGES:
        rows = project_rows(p for p in REPO.projects.values() if p.stage == stage)
        if rows:
            out += [f"## {stage.capitalize()}", ""] + rows + [""]
    if not REPO.projects:
        out += ["*No projects yet.*", ""]
    return "\n".join(out)


@page("export.qmd", nav="Export")
def export_page() -> str:
    return ("---\ntitle: Export\n---\n\n"
            "[Choose what to print. **Save as PDF** prints from the browser, at once and in any combination "
            "(including your progress marks). **LaTeX PDF** gives the options for a typeset PDF built on GitHub.]"
            "{.summary-intro}\n\n"
            "[$\\,$]{.d-none}\n\n"                       # loads MathJax for the assembled content
            "```{=html}\n<div class=\"export-builder\"></div>\n<div id=\"export-output\"></div>\n```\n")


@page("downloads.qmd", nav="PDF")
def downloads_page() -> str:
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
        desc = make_pdf.describe(name)
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
    return "\n".join(lines)


def ctx():
    """What summaries.py needs from the site build."""
    from types import SimpleNamespace
    return SimpleNamespace(fence_for=fence_for, page_url=page_url, transform=transform,
                           render_problems=render_problems, dep_graph=dep_graph,
                           block_number=lambda bid, nid: num(NUMBERING.block(bid), nid) if NUMBERING.block(bid) else "",
                           block_courses=REPO.block_courses, review_courses=REPO.review_courses)


def contents_block(heading: str, rows: list, level: int = 2) -> list[str]:
    """A book-style contents list for the home page: (href, title, desc)."""
    import html
    items = "\n".join(
        f'<li><a href="{href}">'
        + (f'<span class="contents-num">{num}</span>' if num else "")
        + f'{html.escape(title)}</a>'
        + (f'<span class="contents-desc">{html.escape(desc)}</span>' if desc else "")
        + "</li>"
        for href, title, desc, num in rows)
    return ["::: {.contents-field}", f"{'#' * level} {heading}", "", "```{=html}",
            f'<ul class="contents-list">\n{items}\n</ul>', "```", ":::", ""]
