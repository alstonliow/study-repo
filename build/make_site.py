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

import shutil
import sys
import textwrap
from concurrent.futures import ThreadPoolExecutor
from functools import partial

import yaml

import filters
import kinds
import outline
import summaries
import tikz
import web
from model import RAW, load
from web import OUT_COURSES, OUT_NOTES, SITE, TIKZ, branch_page, build_page, contents_block, ctx


def main() -> int:
    REPO = web.setup(load())
    notes = REPO.notes
    owner = REPO.owner
    BRANCHES = REPO.parts
    for n in notes.values():
        n.courses = REPO.note_courses(n)

    # compile drawings
    TIKZ.mkdir(parents=True, exist_ok=True)
    codes = sorted({textwrap.dedent(m.group(2)) for n in notes.values()
                    for t in (n.body, n.examples, n.exercises, n.solutions) for m in RAW.finditer(t)
                    if not tikz.is_algorithm(m.group(2))})
    with ThreadPoolExecutor(max_workers=6) as pool:
        svgs = dict(zip(codes, pool.map(partial(tikz.compile_svg, tikz_dir=TIKZ), codes)))
    web.SVGS.update(svgs)
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
    course_order: dict[str, list] = {}  # course id -> [{"title": chapter heading, "num", "pages": [note html paths]}]
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
        course_order[c.id] = []
        co = outline.course(REPO, c)
        for chap in co.chapters:
            heading = f"Chapter {chap.num}" + (f" · {chap.title}" if chap.title else "")
            summary = f"courses/{c.id}/chapter-{chap.num}"
            lines += ["", f"## {heading}", "", f"[Chapter summary →](/{summary}.qmd){{.chapter-summary-link}}", ""]
            course_order[c.id].append({"title": heading, "num": int(chap.num),
                                       "pages": [f"notes/{n.id}.html" for n in chap.notes],
                                       "summary": summary + ".html"})
            for n in chap.notes:
                nprob = sum(1 for pr in n.problems if c.id in REPO.block_courses(n, pr.id))
                extra = f" ({nprob} exercise{'s' if nprob != 1 else ''})" if nprob else ""
                pts = ", ".join("§" + x for x in points_of.get(n.id, []))
                lines.append(f"- [{n.display_title}](/notes/{n.id}.qmd){extra} [{pts}]{{.note-keys}}")
        (OUT_COURSES / f"{c.id}.qmd").write_text("\n".join(lines) + "\n", encoding="utf-8")
        # chapter summaries: in-scope content only (outline.course puts each
        # branch's synthesis problems in the last chapter that uses the branch)
        (OUT_COURSES / c.id).mkdir(exist_ok=True)
        for chap in co.chapters:
            page = f"courses/{c.id}/chapter-{chap.num}.html"
            (OUT_COURSES / c.id / f"chapter-{chap.num}.qmd").write_text(summaries.page(
                f"{c.code} Chapter {chap.num} · {chap.title}: Summary",
                f"Everything {c.code} needs from this chapter: definitions, results and exercises in course "
                "order, with synthesis problems at the end. Use the filters; print for a review sheet.",
                chap.notes, chap.reviews, ctx(), page, course=c,
                in_scope=filters.Filter(REPO, course=c, omit_extra=True).in_scope), encoding="utf-8")
            summary_courses[page] = [c.id]
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
        **kinds.as_data(),               # block kinds and filter groups (kinds.py)
        # section numbers per outline (numbering.py): topic, and one map per course
        "numbers": {"topic": web.NUMBERING.as_data(),
                    **{c.id: outline.course(REPO, c).numbers() for c in REPO.courses}},
        # for the Export page (site/export.html)
        "titles": {n.id: n.display_title for n in notes.values()},
        "branchTitles": {bid: f"{branch_num[bid]} {t}" for _, bs in REPO.parts for bid, t in bs if bid in branch_num},
        "reviews": sorted(REPO.reviews),
        "repoUrl": ((yaml.safe_load((SITE / "_quarto.yml").read_text(encoding="utf-8")) or {})
                    .get("website", {}).get("repo-url", "") if (SITE / "_quarto.yml").exists() else ""),
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    for stale in ("courses.json", "progress.json"):
        if (SITE / stale).exists():
            (SITE / stale).unlink()

    (SITE / "index.qmd").write_text("\n".join(home) + "\n", encoding="utf-8")
    for pg in web.PAGES:                          # generated pages outside the notes
        (SITE / pg.file).write_text(pg.render(), encoding="utf-8")
    navbar = [{"href": "index.qmd", "text": "Home"}] + \
        [{"href": pg.file, "text": pg.nav} for pg in web.PAGES if pg.nav]
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
