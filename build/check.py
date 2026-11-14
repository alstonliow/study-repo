#!/usr/bin/env python3
"""Repository checks (meta/SPEC.md §11).

Errors make the script exit non-zero. Warnings are printed but do not fail.
Read-only: never modifies files and never runs git write commands.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import yaml

EMPTY_SOL = re.compile(r'^:::+\s*\{[^}]*\.solution[^}]*for="([^"]+)"[^}]*\}\s*\n\s*:::+\s*$', re.M)
ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT / "notes"

REQUIRED_YAML = ["title", "sources", "requires", "status"]
ALLOWED = {"status": {"draft", "done"}}
LEVELS = {"easy", "medium", "hard"}  # optional `level` on problem and example blocks

BLOCK_PREFIXES = "def|thm|lem|cor|prp|exm|rem|prob"
DIV_OPEN = re.compile(r"^:::+\s*\{(?P<attrs>[^}]*)\}\s*$")
ID_ATTR = re.compile(r"(?:^|\s)#([A-Za-z][\w-]*)")
CLASS_ATTR = re.compile(r"(?:^|\s)\.([A-Za-z][\w-]*)")
KV_ATTR = re.compile(r'([A-Za-z][\w-]*)="([^"]*)"')
REF = re.compile(r"(?<![\w@])@((?:%s|sec)-[A-Za-z0-9-]*[A-Za-z0-9])" % BLOCK_PREFIXES)
FORBIDDEN_SUFFIXES = {".pdf", ".aux", ".log", ".toc", ".out", ".fls",
                      ".fdb_latexmk", ".synctex.gz"}

errors: list[str] = []
warnings: list[str] = []


def rel(p: Path) -> str:
    return str(p.relative_to(ROOT))


def strip_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.S)


def read_front_matter(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if not m:
        errors.append(f"{rel(path)}: missing YAML front matter")
        return None
    try:
        data = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as exc:
        errors.append(f"{rel(path)}: invalid YAML ({exc})")
        return None
    return data


def note_dirs() -> list[Path]:
    if not NOTES.exists():
        return []
    return sorted({p.parent for p in NOTES.rglob("*.md")})


def note_id(d: Path) -> str:
    return str(d.relative_to(NOTES))


def sec_label(nid: str) -> str:
    return "sec-" + nid.replace("/", "-")


def check_notes() -> None:
    dirs = note_dirs()
    ids = {note_id(d) for d in dirs}
    sec_labels = {sec_label(i) for i in ids}

    block_ids: dict[str, str] = {}
    problems: dict[str, Path] = {}
    solutions: dict[str, Path] = {}
    empty_solutions: set[str] = set()   # stubs holding only a TODO comment
    refs: list[tuple[Path, str]] = []
    requires: list[tuple[Path, str]] = []

    for d in dirs:
        nid = note_id(d)
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*(?:/[a-z0-9]+(?:-[a-z0-9]+)*)*", nid):
            errors.append(f"{nid}: folder names must be lowercase words joined by hyphens")
        note = d / "note.md"
        if not note.exists():
            errors.append(f"{nid}: missing note.md")
        else:
            fm = read_front_matter(note)
            if fm is not None:
                for key in REQUIRED_YAML:
                    if key not in fm:
                        errors.append(f"{rel(note)}: missing YAML field '{key}'")
                for key, allowed in ALLOWED.items():
                    if key in fm and fm[key] not in allowed:
                        errors.append(f"{rel(note)}: {key}={fm[key]!r} not in {sorted(a for a in allowed if a)}")
                for r in fm.get("requires") or []:
                    requires.append((note, r))

        for md in sorted(d.glob("*.md")):
            text = strip_comments(md.read_text(encoding="utf-8"))
            for lineno, line in enumerate(text.splitlines(), 1):
                m = DIV_OPEN.match(line)
                if not m:
                    continue
                attrs = m.group("attrs")
                classes = CLASS_ATTR.findall(attrs)
                kv = dict(KV_ATTR.findall(attrs))
                attrs_no_kv = KV_ATTR.sub("", attrs)
                bid = ID_ATTR.search(attrs_no_kv)
                where = f"{rel(md)}:{lineno}"
                if bid:
                    b = bid.group(1)
                    if b in block_ids:
                        errors.append(f"{where}: duplicate id '{b}' (also {block_ids[b]})")
                    else:
                        block_ids[b] = where
                if "problem" in classes:
                    if md.name != "exercise.md":
                        errors.append(f"{where}: problem block outside exercise.md")
                    if not bid:
                        errors.append(f"{where}: problem without id")
                    else:
                        problems[bid.group(1)] = md
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
            for m in EMPTY_SOL.finditer(text):
                empty_solutions.add(m.group(1))
            for m in REF.finditer(text):
                refs.append((md, m.group(1)))

    for note, r in requires:
        if r not in ids:
            errors.append(f"{rel(note)}: requires unknown id '{r}'")

    legacy = 0
    for md, r in refs:
        if r.startswith("sec-legacy-"):
            legacy += 1
        elif r.startswith("sec-"):
            if r not in sec_labels:
                errors.append(f"{rel(md)}: broken reference @{r}")
        elif r not in block_ids:
            errors.append(f"{rel(md)}: broken reference @{r}")
    if legacy:
        warnings.append(f"{legacy} reference(s) to not-yet-migrated sections (@sec-legacy-*)")

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
    check_forbidden_files()
    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    print(f"{len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
