#!/usr/bin/env python3
"""Repository checks (meta/SPEC.md §11), on the model from build/model.py.

Errors make the script exit non-zero. Warnings are printed but do not fail.
Read-only: never modifies files and never runs git write commands.
"""

from __future__ import annotations

import argparse
import ast
import re
import subprocess
import sys
from pathlib import Path
from typing import Callable

from kinds import ID_PREFIXES, NO_ID_CLASSES
from model import MATH, REF, ROOT, load

REQUIRED_YAML = ["title", "sources", "requires", "status"]
ALLOWED = {"status": {"draft", "done"}}
PY_FENCE = re.compile(r"^```\{?\.?python([^\n]*)\n(.*?)^```", re.M | re.S)
LEVELS = {"easy", "medium", "hard"}  # optional `level` on problem and example blocks
FORBIDDEN_SUFFIXES = {".pdf", ".aux", ".log", ".toc", ".out", ".fls",
                      ".fdb_latexmk", ".synctex.gz"}

errors: list[str] = []
warnings: list[str] = []

# Rule registry: (id, description, function), run in this order. A new check is
# a function decorated with @rule; `check.py --list` shows them all.
RULES: list[tuple[str, str, Callable[[], None]]] = []


def rule(rid: str, desc: str):
    def register(fn: Callable[[], None]) -> Callable[[], None]:
        RULES.append((rid, desc, fn))
        return fn
    return register
REPO = load()


def rel(p: Path) -> str:
    return str(p.relative_to(ROOT))


@rule("notes", "ids, YAML, blocks, problems and solutions, references")
def check_notes() -> None:
    ids = {n.id for n in REPO.all_notes}
    sec_labels = {n.sec_label for n in REPO.all_notes}

    block_ids: dict[str, str] = {}
    problems: dict[str, Path] = {}
    solutions: dict[str, Path] = {}
    empty_solutions: set[str] = set()   # stubs holding only a TODO comment
    refs: list[tuple[Path, str]] = []
    requires: list[tuple[Path, str]] = []
    missing_ids: list[str] = []

    for branch, rv in REPO.reviews.items():
        if branch not in REPO.branch_order:
            errors.append(f"{rv.id}: review folder is not directly under a branch in meta/taxonomy.yml")
        extra = sorted(set(rv.files) - {"exercise.md", "solution.md"})
        if extra:
            errors.append(f"{rv.id}: a review folder holds only exercise.md and solution.md (found {', '.join(extra)})")

    for note in REPO.all_notes + list(REPO.reviews.values()):
        nid = note.id
        is_review = note in REPO.reviews.values()
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*(?:/[a-z0-9]+(?:-[a-z0-9]+)*)*", nid):
            errors.append(f"{nid}: folder names must be lowercase words joined by hyphens")
        if is_review:
            pass
        elif not note.has_note:
            errors.append(f"{nid}: missing note.md")
        else:
            path = note.files["note.md"].path
            if note.front_error:
                errors.append(f"{rel(path)}: {note.front_error}")
            else:
                fm = note.front
                for key in REQUIRED_YAML:
                    if key not in fm:
                        errors.append(f"{rel(path)}: missing YAML field '{key}'")
                for key, allowed in ALLOWED.items():
                    if key in fm and fm[key] not in allowed:
                        errors.append(f"{rel(path)}: {key}={fm[key]!r} not in {sorted(a for a in allowed if a)}")
                for r in fm.get("requires") or []:
                    requires.append((path, r))

        for f in note.files.values():
            md = f.path
            for d in f.divs:
                classes, kv, bid = d.classes, d.attrs, d.id
                where = f"{rel(md)}:{d.line}"
                if bid:
                    if bid in block_ids:
                        errors.append(f"{where}: duplicate id '{bid}' (also {block_ids[bid]})")
                    else:
                        block_ids[bid] = where
                    if bid.split("-", 1)[0] not in ID_PREFIXES:
                        warnings.append(f"{where}: id '{bid}' has an unknown prefix")
                elif (f.name != "solution.md" and d.depth == 0 and classes
                      and not NO_ID_CLASSES & set(classes) and classes[0] not in ("tikz-figure",)):
                    missing_ids.append(where)
                if "problem" in classes:
                    if md.name != "exercise.md":
                        errors.append(f"{where}: problem block outside exercise.md")
                    if not bid:
                        errors.append(f"{where}: problem without id")
                    else:
                        problems[bid] = md
                    if not kv.get("origin"):
                        errors.append(f"{where}: problem missing origin")
                    elif kv["origin"] not in {"self", "external"}:
                        errors.append(f"{where}: origin must be self or external")
                    if "source" not in kv:
                        errors.append(f"{where}: problem missing source")
                    elif not kv["source"]:
                        warnings.append(f"{where}: problem has empty source (TODO)")
                if "example" in classes and d.depth == 0 and (md.name == "code.md" or "origin" in kv):
                    origin = kv.get("origin")       # SPEC §5.9
                    if origin not in {"self", "external", "adapted"}:
                        errors.append(f"{where}: code example needs origin=\"self|external|adapted\"")
                    elif origin != "self" and not kv.get("source"):
                        errors.append(f"{where}: origin={origin} needs a source key")
                elif md.name == "code.md" and d.depth == 0 and classes:
                    errors.append(f"{where}: code.md holds only example blocks")
                if "difficulty" in kv:
                    errors.append(f"{where}: use level=\"easy|medium|hard\" instead of difficulty")
                if kv.get("level"):
                    if not ({"problem", "example"} & set(classes)):
                        errors.append(f"{where}: level is only for problem and example blocks")
                    elif kv["level"] not in LEVELS:
                        errors.append(f"{where}: level must be easy, medium or hard")
                if "solution" in classes:
                    target = kv.get("for")
                    if not target:
                        errors.append(f"{where}: solution missing 'for'")
                    elif kv.get("status", "draft") != "draft":
                        errors.append(f"{where}: solution status must be draft (or omitted once reviewed)")
                    else:
                        solutions[target] = md
                        if not d.body.strip():
                            empty_solutions.add(target)
            for m in re.finditer(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", f.raw):
                line = f.raw[:m.start()].count("\n") + 1
                errors.append(f"{rel(md)}:{line}: invisible control character {m.group(0)!r} (corrupted text?)")
            if f.name == "code.md":   # Python is parsed, never run (SPEC §5.9)
                for m in PY_FENCE.finditer(f.raw):
                    try:
                        ast.parse(m.group(2))
                    except SyntaxError as exc:
                        line = f.raw[:m.start(2)].count("\n") + (exc.lineno or 1)
                        errors.append(f"{rel(md)}:{line}: Python syntax error ({exc.msg})")
            if f.name in ("exercise.md", "solution.md"):
                # fenced code (a Python comment is not a heading) is blanked, line numbers kept
                text = CODE_FENCE.sub(lambda m: "\n" * m.group(0).count("\n"), f.masked)
                for m in re.finditer(r"^[ \t]*#{1,6} ", text, re.M):
                    line = text[:m.start()].count("\n") + 1
                    errors.append(f"{rel(md)}:{line}: no headings inside problems or solutions; use **bold** text")
            for m in REF.finditer(f.text):
                refs.append((md, m.group(1)))
            for m in MATH.finditer(f.masked):
                for r in REF.finditer(m.group(0)):
                    line = f.masked[:m.start()].count("\n") + 1
                    errors.append(f"{rel(md)}:{line}: @{r.group(1)} inside maths cannot be a link; move it out of the formula")

    for path, r in requires:
        if r in REPO.alias_of:
            errors.append(f"{rel(path)}: requires '{r}', an old id; use the current id '{REPO.alias_of[r]}' (SPEC §17.3)")
        elif r not in ids:
            errors.append(f"{rel(path)}: requires unknown id '{r}'")

    old_labels = {"sec-" + a.replace("/", "-"): cur for a, cur in REPO.alias_of.items()}
    legacy = 0
    for md, r in refs:
        if r.startswith("sec-legacy-"):
            legacy += 1
        elif r.startswith("sec-"):
            if r in old_labels:
                errors.append(f"{rel(md)}: @{r} points to an old id; use @sec-{old_labels[r].replace('/', '-')} (SPEC §17.3)")
            elif r not in sec_labels:
                errors.append(f"{rel(md)}: broken reference @{r}")
        elif r.split("-", 1)[0] in ("rmk", "clm", "rem"):
            errors.append(f"{rel(md)}: @{r}: remarks and claims are not cross-referenced (SPEC §5.1)")
        elif r not in block_ids and not (r.startswith(("res-", "prj-")) and r in REPO.entities):
            errors.append(f"{rel(md)}: broken reference @{r}")
    if legacy:
        warnings.append(f"{legacy} reference(s) to not-yet-migrated sections (@sec-legacy-*)")
    if missing_ids:
        warnings.append(f"{len(missing_ids)} block(s) without an id (SPEC §5.1), e.g. {missing_ids[0]}")

    for pid, md in problems.items():
        if pid not in solutions:
            warnings.append(f"{rel(md)}: problem '{pid}' has no solution")
        elif pid in empty_solutions:
            warnings.append(f"{rel(md)}: problem '{pid}' has an empty solution (TODO)")
    for pid, md in solutions.items():
        if pid not in problems:
            errors.append(f"{rel(md)}: solution for unknown problem '{pid}'")
        elif problems[pid].parent != md.parent:
            errors.append(f"{rel(md)}: solution '{pid}' not in the same folder as its problem")

    print(f"notes: {len(ids)} knowledge points, {len(block_ids)} labelled blocks, "
          f"{len(problems)} problems, {len(solutions) - len(empty_solutions)} solutions "
          f"({len(empty_solutions)} empty)")


@rule("resources", "resource files: ids, nodes, editions, locators")
def check_resources() -> None:
    """Resource files (SPEC §17.12): valid ids, unique node ids and locators,
    editions listed, no id shared with another entity."""
    others = {n.id for n in REPO.all_notes} | set(REPO.owner)
    seen: dict[str, str] = {}
    for r in REPO.resources.values():
        where = rel(r.path)
        for msg in r.problems:
            errors.append(f"{where}: {msg}")
        for eid in [r.id] + list(r.nodes):
            if eid in others:
                errors.append(f"{where}: '{eid}' is also the id of a note or block")
            elif eid in seen and seen[eid] != where:
                errors.append(f"{where}: '{eid}' is also an id in {seen[eid]}")
            seen[eid] = where
    nodes = sum(len(r.nodes) for r in REPO.resources.values())
    print(f"resources: {len(REPO.resources)} ({nodes} nodes)")


@rule("projects", "project files: schema, course, assignment, block ids, references")
def check_projects() -> None:
    """Project files (SPEC §17.13): the schema, a known course, an assignment that
    is a resource node, ids unique across the repository, @-references that
    resolve. `applies` targets are checked with the other relationships."""
    others = {n.id for n in REPO.all_notes} | set(REPO.owner) | {e for e in REPO.entities
                                                                 if not e.startswith("prj-")}
    courses = {c.id for c in REPO.courses}
    seen: dict[str, str] = {}
    for p in REPO.projects.values():
        where = rel(p.path)
        for msg in p.problems:
            errors.append(f"{where}: {msg}")
        if p.id in others:
            errors.append(f"{where}: '{p.id}' is also the id of another entity")
        if p.course and p.course not in courses:
            errors.append(f"{where}: course '{p.course}' is not a course in meta/courses/")
        if p.assignment:
            e = REPO.entities.get(p.assignment)
            if e is None:
                errors.append(f"{where}: assignment unknown id '{p.assignment}'")
            elif e.type != "resource-node":
                errors.append(f"{where}: assignment '{p.assignment}' must be a resource node, not a {e.type}")
            elif e.visibility != "public" and p.visibility == "public":
                errors.append(f"{where}: public project points to private '{p.assignment}' (SPEC §17.9.3)")
        for bid in REPO.project_blocks.get(p.id, []):
            if bid in others or bid in REPO.entities:
                errors.append(f"{where}: duplicate id '{bid}' (also a note, block or entity)")
            elif bid in seen:
                errors.append(f"{where}: duplicate id '{bid}' (also {seen[bid]})")
            seen[bid] = where
        text = MATH.sub("", re.sub(r"<!--.*?-->", "", p.body, flags=re.S))
        for m in REF.finditer(text):
            r = m.group(1)
            ok = (r in REPO.entities or r in seen) if not r.startswith("sec-") else \
                r[4:] in {n.id.replace("/", "-") for n in REPO.notes.values()}
            if not ok:
                errors.append(f"{where}: broken reference @{r}")
    print(f"projects: {len(REPO.projects)}")


@rule("sources", "source keys resolve to a resource node (legacy keys)")
def check_sources() -> None:
    """Every source key resolves to an explicit resource, edition and node (SPEC §17.12.6)."""
    keys = [(n.files["note.md"].path, str(k)) for n in REPO.notes.values() for k in n.front.get("sources") or []]
    keys += [(n.files["exercise.md"].path, p.attrs.get("source", ""))
             for n in list(REPO.notes.values()) + list(REPO.reviews.values()) for p in n.problems]
    keys += [(n.files[name].path, d.attrs.get("source", "")) for n in REPO.notes.values()
             for name in ("note.md", "example.md", "code.md") if name in n.files
             for d in n.files[name].divs if "example" in d.classes]
    for path, key in keys:
        if key:
            msg = REPO.sources.problems(key)
            if msg:
                errors.append(f"{rel(path)}: {msg}")


@rule("requires", "prerequisites: no cycles, nothing implied or later")
def check_requires() -> None:
    """requires = direct prerequisites only: no cycles, nothing implied, nothing later."""
    for level, msg in REPO.requires_problems():
        (errors if level == "error" else warnings).append(msg)


@rule("aliases", "old ids of moved notes are unique")
def check_aliases() -> None:
    """Old ids kept after a move (SPEC §2.6) must not be reused or repeated."""
    seen: dict[str, str] = {}
    for n in REPO.notes.values():
        for a in n.aliases:
            if a in REPO.notes:
                errors.append(f"{n.id}: alias '{a}' is the id of an existing note")
            elif a in seen:
                errors.append(f"{n.id}: alias '{a}' is also an alias of {seen[a]}")
            seen[a] = n.id


@rule("relations", "typed relationships: known types and ids, allowed ends, no cycles")
def check_relations() -> None:
    """Relationships (SPEC §17.5): types from meta/relations.yml, current ids,
    ends the type allows, no cycles in acyclic types, no duplicates."""
    import relations
    g = relations.Graph(REPO)
    for level, msg in g.check():
        (errors if level == "error" else warnings).append(msg)
    typed = sum(1 for r in g.relations if r.type != "requires")
    print(f"relationships: {typed} typed, {len(g.references)} references between pages")


@rule("taxonomy", "every note listed in meta/taxonomy.yml")
def check_taxonomy() -> None:
    for msg in REPO.taxonomy_problems():
        errors.append(f"meta/taxonomy.yml: {msg}")


@rule("courses", "course files resolve; provenance without scope")
def check_courses() -> None:
    """Course files (SPEC §13): references resolve; provenance without scope is reported."""
    if not REPO.courses:
        warnings.append("no course files in meta/courses/")
    for c in REPO.courses:
        where = rel(c.path)
        for level, msg in c.problems:
            (errors if level == "error" else warnings).append(f"{where}: {msg}")
        if c.status not in ("draft", "confirmed"):
            errors.append(f"{where}: status must be draft or confirmed")
        if c.coursework_repo is not None:           # §13 item 7: optional {url: https://...}
            r = c.coursework_repo
            if not isinstance(r, dict) or set(r) != {"url"}:
                errors.append(f"{where}: coursework_repo must be a mapping with only 'url'")
            elif not str(r["url"] or "").startswith("https://"):
                errors.append(f"{where}: coursework_repo.url must be an https URL")
        if not c.field and REPO.field_order():
            warnings.append(f"{where}: no field of knowledge (its covers reach no note in a field)")
        outside = [n.id for n in REPO.notes.values()
                   if c.source_prefix and any(str(k).startswith(c.source_prefix) for k in n.front.get("sources") or [])
                   and not REPO.in_scope(c, n.id)]
        scoped = sum(1 for n in REPO.notes if REPO.in_scope(c, n))
        print(f"course {c.id}: {len(c.points)} outline points, {scoped} notes in scope, "
              f"{len(c.exclude)} excluded blocks ({c.status})")
        for nid in outside:
            print(f"info: {nid}: drawn from {c.code} material but outside its scope")


CODE_FENCE = re.compile(r"^([ \t]*)(`{3,}|~{3,})[^\n]*\n.*?^\1\2[ \t]*$", re.S | re.M)
RAW_LATEX = re.compile(r"^[ \t]*```\{=latex\}\n(.*?)\n[ \t]*```", re.S | re.M)
HARD_CODED = re.compile(
    r"\b(?:defc|thmc|exc|notec|black|gray|red|blue|green)!\d+"      # colour mixes
    r"|\b(?:defc|thmc|exc|notec|gray|red|blue|green)\b"             # raw colour names
    r"|line width=[\d.]+|\b(?:very |ultra )?(?:thick|thin)\b"      # line widths
    r"|font=\\(?:tiny|scriptsize|footnotesize|small|normalsize|large|Large|LARGE|huge|Huge)"
    r"|minimum (?:size|width|height)=|inner sep=|fill opacity=|rounded corners=")


@rule("figures", "figures use the shared styles")
def check_figures() -> None:
    """Figures use the shared styles (meta/SPEC.md §5), not raw colours and sizes."""
    for f in (f for n in REPO.all_notes for f in n.files.values()):
        md, text = f.path, f.masked
        for m in RAW_LATEX.finditer(text):
            code = m.group(1)
            if "\\begin{algorithmic}" in code or "circuitikz" in code:
                continue
            found = sorted(set(HARD_CODED.findall(code)))
            if found:
                line = text[:m.start()].count("\n") + 1
                warnings.append(f"{rel(md)}:{line}: figure hard-codes {', '.join(found)}; use the shared styles")


@rule("widgets", "interactive widgets are attached to existing figures")
def check_widgets() -> None:
    """Every widget in site/_assets/widgets.html names a figure that exists (meta/SPEC.md §5)."""
    path = ROOT / "site" / "_assets" / "widgets.html"
    if not path.exists():
        return
    figs = {d.id for n in REPO.all_notes for f in n.files.values() for d in f.divs if d.id}
    for m in WIDGET_KEY.finditer(path.read_text(encoding="utf-8")):
        if m.group(1) not in figs:
            line = path.read_text(encoding="utf-8")[:m.start()].count("\n") + 1
            errors.append(f"{rel(path)}:{line}: widget for unknown figure {m.group(1)}")


WIDGET_KEY = re.compile(r'^\s*"(fig-[\w-]+)":\s*\{', re.M)


@rule("files", "nothing from raw/, no PDFs or build artefacts")
def check_forbidden_files() -> None:
    """Files that would be committed (tracked or untracked, not ignored)."""
    try:
        out = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout.splitlines()
    except (OSError, subprocess.CalledProcessError) as exc:
        warnings.append(f"could not list files with git ({exc}); skipped forbidden-file check")
        return
    for f in out:
        p = Path(f)
        if p.parts and p.parts[0] in {"raw", "out", "_site"}:
            errors.append(f"{f}: must not be committed")
        elif any(f.endswith(s) for s in FORBIDDEN_SUFFIXES):
            errors.append(f"{f}: build artefact or PDF must not be committed")


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Repository checks (meta/SPEC.md §11).")
    ap.add_argument("--list", action="store_true", help="list the rules and exit")
    ap.add_argument("--only", default="", help="comma-separated rule ids to run")
    ap.add_argument("--skip", default="", help="comma-separated rule ids to skip")
    a = ap.parse_args(argv)
    if a.list:
        for rid, desc, _ in RULES:
            print(f"{rid:10} {desc}")
        return 0
    only = {x for x in a.only.split(",") if x}
    skip = {x for x in a.skip.split(",") if x}
    unknown = (only | skip) - {rid for rid, _, _ in RULES}
    if unknown:
        print(f"unknown rule(s): {', '.join(sorted(unknown))}; see --list")
        return 2
    for rid, _, fn in RULES:
        if (not only or rid in only) and rid not in skip:
            fn()
    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    print(f"{len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
