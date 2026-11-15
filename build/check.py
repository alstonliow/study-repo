#!/usr/bin/env python3
"""Repository checks (meta/SPEC.md §11), on the model from build/model.py.

Errors make the script exit non-zero. Warnings are printed but do not fail.
Read-only: never modifies files and never runs git write commands.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

from model import ID_PREFIXES, MATH, NOTES, REF, ROOT, load

REQUIRED_YAML = ["title", "sources", "requires", "status"]
ALLOWED = {"status": {"draft", "done"}}
LEVELS = {"easy", "medium", "hard"}  # optional `level` on problem and example blocks
FORBIDDEN_SUFFIXES = {".pdf", ".aux", ".log", ".toc", ".out", ".fls",
                      ".fdb_latexmk", ".synctex.gz"}
NO_ID_CLASSES = {"proof", "solution"}      # SPEC §5.2: these never carry an id

errors: list[str] = []
warnings: list[str] = []
REPO = load()


def rel(p: Path) -> str:
    return str(p.relative_to(ROOT))


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

    for bid, rv in REPO.reviews.items():
        if bid not in REPO.branch_order:
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
                    if kv.get("status", "draft") != "draft":
                        errors.append(f"{where}: solution status must be draft (or omitted once reviewed)")
                    else:
                        solutions[target] = md
                        if not d.body.strip():
                            empty_solutions.add(target)
            for m in re.finditer(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", f.raw):
                line = f.raw[:m.start()].count("\n") + 1
                errors.append(f"{rel(md)}:{line}: invisible control character {m.group(0)!r} (corrupted text?)")
            if f.name in ("exercise.md", "solution.md"):
                for m in re.finditer(r"^[ \t]*#{1,6} ", f.masked, re.M):
                    line = f.masked[:m.start()].count("\n") + 1
                    errors.append(f"{rel(md)}:{line}: no headings inside problems or solutions; use **bold** text")
            for m in REF.finditer(f.text):
                refs.append((md, m.group(1)))
            for m in MATH.finditer(f.masked):
                for r in REF.finditer(m.group(0)):
                    line = f.masked[:m.start()].count("\n") + 1
                    errors.append(f"{rel(md)}:{line}: @{r.group(1)} inside maths cannot be a link; move it out of the formula")

    for path, r in requires:
        if r not in ids:
            errors.append(f"{rel(path)}: requires unknown id '{r}'")

    legacy = 0
    for md, r in refs:
        if r.startswith("sec-legacy-"):
            legacy += 1
        elif r.startswith("sec-"):
            if r not in sec_labels:
                errors.append(f"{rel(md)}: broken reference @{r}")
        elif r.split("-", 1)[0] in ("rmk", "clm", "rem"):
            errors.append(f"{rel(md)}: @{r}: remarks and claims are not cross-referenced (SPEC §5.1)")
        elif r not in block_ids:
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


def check_requires() -> None:
    """requires = direct prerequisites only: no cycles, nothing implied, nothing later."""
    for level, msg in REPO.requires_problems():
        (errors if level == "error" else warnings).append(msg)


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


def check_taxonomy() -> None:
    for msg in REPO.taxonomy_problems():
        errors.append(f"meta/taxonomy.yml: {msg}")


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
        outside = [n.id for n in REPO.notes.values()
                   if c.source_prefix and any(str(k).startswith(c.source_prefix) for k in n.front.get("sources") or [])
                   and not REPO.in_scope(c, n.id)]
        scoped = sum(1 for n in REPO.notes if REPO.in_scope(c, n))
        print(f"course {c.id}: {len(c.points)} outline points, {scoped} notes in scope, "
              f"{len(c.exclude)} excluded blocks ({c.status})")
        for nid in outside:
            print(f"info: {nid}: drawn from {c.code} material but outside its scope")


RAW_LATEX = re.compile(r"^[ \t]*```\{=latex\}\n(.*?)\n[ \t]*```", re.S | re.M)
HARD_CODED = re.compile(
    r"\b(?:defc|thmc|exc|notec|black|gray|red|blue|green)!\d+"      # colour mixes
    r"|\b(?:defc|thmc|exc|notec|gray|red|blue|green)\b"             # raw colour names
    r"|line width=[\d.]+|\b(?:very |ultra )?(?:thick|thin)\b"      # line widths
    r"|font=\\(?:tiny|scriptsize|footnotesize|small|normalsize|large|Large|LARGE|huge|Huge)"
    r"|minimum (?:size|width|height)=|inner sep=|fill opacity=|rounded corners=")


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


def main() -> int:
    check_notes()
    check_taxonomy()
    check_aliases()
    check_requires()
    check_courses()
    check_figures()
    check_forbidden_files()
    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    print(f"{len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
