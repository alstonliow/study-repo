#!/usr/bin/env python3
"""Move a knowledge point, or a whole folder of them, to a new id (path).

    python3 build/move_note.py OLD NEW [--dry-run]

OLD is a note id (math/discrete/sets/subsets) or a folder that contains notes
(math/discrete/graph). Every note at or under OLD moves to the same place under
NEW. The script then keeps everything working (meta/SPEC.md §2.6):

- @sec- references in all notes, `requires`, course files (`covers`) and
  meta/taxonomy.yml (branch ids and note order) are rewritten to the new ids;
- each moved note records its old id under `aliases` in its YAML, so the website
  keeps a redirect page at the old address and progress marks follow the note.

Block ids (def-, thm-, rmk-, fig-, ...) never change, even when they contain the
old folder name. The script moves folders with the file system; it never runs
git. Run `make check` afterwards.
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

from model import META, NOTES, load

ID_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*(?:/[a-z0-9]+(?:-[a-z0-9]+)*)*")


def sec(nid: str) -> str:
    return "sec-" + nid.replace("/", "-")


def replace_ids(text: str, mapping: dict[str, str]) -> str:
    """Replace whole note ids inside YAML lists ([a, b] or '- a')."""
    for old, new in mapping.items():
        text = re.sub(r"(?<=[\[\s,])" + re.escape(old) + r"(?=[\],\s]|$)", new, text, flags=re.M)
    return text


def main(argv: list[str]) -> int:
    dry = "--dry-run" in argv
    args = [a for a in argv if not a.startswith("--")]
    if len(args) != 2:
        print(__doc__)
        return 2
    old, new = (a.strip("/") for a in args)
    if not ID_RE.fullmatch(new):
        print(f"error: '{new}' is not a valid id (lowercase words joined by hyphens, separated by /)")
        return 1
    repo = load()
    moved = {nid: new + nid[len(old):] for nid in repo.notes if nid == old or nid.startswith(old + "/")}
    if not moved:
        print(f"error: no note at or under '{old}'")
        return 1
    clash = [n for n in moved.values() if (NOTES / n).exists() or n in repo.notes]
    if clash:
        print(f"error: target already exists: {', '.join(clash)}")
        return 1
    aliases = {a for n in repo.notes.values() for a in n.aliases}
    clash = [n for n in moved.values() if n in aliases]
    if clash:
        print(f"error: target is an old id kept as an alias: {', '.join(clash)}")
        return 1

    changes: dict[Path, str] = {}

    def edit(path: Path, text: str) -> None:
        before = changes.get(path, path.read_text(encoding="utf-8"))
        if text != before:
            changes[path] = text

    # 1. references and requires in every note file
    for n in repo.all_notes:
        for f in n.files.values():
            text = changes.get(f.path, f.raw)
            for o, w in moved.items():
                text = re.sub(r"@" + re.escape(sec(o)) + r"(?![A-Za-z0-9-])", "@" + sec(w), text)
            if f.name == "note.md":
                m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
                if m:
                    head = re.sub(r"^(requires:.*)$", lambda r: replace_ids(r.group(1), moved),
                                  m.group(1), flags=re.M)
                    text = "---\n" + head + "\n---\n" + text[m.end():]
            edit(f.path, text)

    # 2. aliases in the moved notes
    for o, w in moved.items():
        path = NOTES / o / "note.md"
        text = changes.get(path, path.read_text(encoding="utf-8"))
        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        head = m.group(1)
        am = re.search(r"^aliases:\s*\[(.*?)\]\s*(#.*)?$", head, re.M)
        if am:
            items = [x.strip() for x in am.group(1).split(",") if x.strip()]
            note = "   " + am.group(2) if am.group(2) else ""
            head = head[:am.start()] + f"aliases: [{', '.join(items + [o])}]{note}" + head[am.end():]
        else:
            head = re.sub(r"^(requires:.*)$", lambda r: r.group(1) + f"\naliases: [{o}]   # old ids (moved)",
                          head, count=1, flags=re.M)
        edit(path, "---\n" + head + "\n---\n" + text[m.end():])

    # 3. course files
    for c in repo.courses:
        edit(c.path, replace_ids(c.path.read_text(encoding="utf-8"), moved))

    # 4. taxonomy: branch ids, and note order lists
    tax_path = META / "taxonomy.yml"
    tax = changes.get(tax_path, tax_path.read_text(encoding="utf-8"))
    branches = set(repo.branch_order)
    for b in sorted(branches, key=len, reverse=True):          # whole branches that move
        if b == old or b.startswith(old + "/"):
            tax = re.sub(r"^(\s*- id: )" + re.escape(b) + r"\s*$", lambda r: r.group(1) + new + b[len(old):],
                         tax, flags=re.M)
    for o, w in moved.items():
        ob, os_ = o.rsplit("/", 1)
        nb, ns = w.rsplit("/", 1)
        if ob in branches and (ob == old or ob.startswith(old + "/")):
            continue                                            # moved with its whole branch: same slug
        if nb == ob:                                            # renamed inside its branch
            tax = rename_in_branch(tax, ob, os_, ns)
        else:                                                   # to another, existing branch
            if nb not in branches:
                print(f"error: branch '{nb}' is not in meta/taxonomy.yml; add it there first")
                return 1
            tax = remove_from_branch(tax, ob, os_)
            tax = append_to_branch(tax, nb, ns)
    edit(tax_path, tax)

    # report, then write and move
    for path in sorted(changes):
        print(("would update " if dry else "update ") + str(path.relative_to(NOTES.parent)))
    for o, w in moved.items():
        print(("would move " if dry else "move ") + f"notes/{o} -> notes/{w}")
    if dry:
        return 0
    for path, text in changes.items():
        path.write_text(text, encoding="utf-8")
    src, dst = NOTES / old, NOTES / new
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(dst))
    # remove folders left empty by the move
    p = src.parent
    while p != NOTES and p.exists() and not any(p.iterdir()):
        p.rmdir()
        p = p.parent
    print(f"moved {len(moved)} note(s). Now run: make check")
    return 0


def branch_span(tax: str, bid: str) -> tuple[int, int]:
    """Start and end of the `notes:` list of branch bid in taxonomy.yml."""
    m = re.search(r"^\s*- id: " + re.escape(bid) + r"\s*$", tax, re.M)
    if not m:
        raise SystemExit(f"error: branch '{bid}' not found in meta/taxonomy.yml")
    nm = re.compile(r"^        notes:.*\n((?:          - .*\n)*)", re.M).search(tax, m.end())
    nxt = re.compile(r"^\s*- (id|title): ", re.M).search(tax, m.end())
    if not nm or (nxt and nm.start() > nxt.start()):
        raise SystemExit(f"error: branch '{bid}' has no notes: list in meta/taxonomy.yml")
    return nm.start(1), nm.end(1)


def rename_in_branch(tax: str, bid: str, old: str, new: str) -> str:
    a, b = branch_span(tax, bid)
    return tax[:a] + re.sub(r"^(          - )" + re.escape(old) + r"$", r"\g<1>" + new, tax[a:b], count=1,
                            flags=re.M) + tax[b:]


def remove_from_branch(tax: str, bid: str, slug: str) -> str:
    a, b = branch_span(tax, bid)
    return tax[:a] + re.sub(r"^          - " + re.escape(slug) + r"\n", "", tax[a:b], count=1, flags=re.M) + tax[b:]


def append_to_branch(tax: str, bid: str, slug: str) -> str:
    a, b = branch_span(tax, bid)
    return tax[:b] + f"          - {slug}\n" + tax[b:]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
