#!/usr/bin/env python3
"""Render the website in parallel shards and merge them (CI speed-up).

Rendering every page in one `quarto render` takes most of the publish time, one
page after another. The generated site/ is split into units (a notes area, a
course, the library, each top-level page), the units are spread over N shards
by page count, and each shard renders its units with `quarto render <unit>` in
its own copy of site/. Quarto knows every page in each copy, so links and the
sidebar are the same as in a full render; each shard writes only its own pages
and their entries in search.json and sitemap.xml. `merge` joins the shards.

    python3 build/site_shards.py plan   [--site site] --of N
    python3 build/site_shards.py render [--site site] --shard I --of N
    python3 build/site_shards.py merge  [--site site] --of N OUT SHARD_SITE...

`plan` prints the units of each shard; `render` renders shard I (0-based) into
<site>/_site; `merge` joins the _site folders of every shard into OUT. Each
SHARD_SITE is that shard's _site folder, given in shard order. Pages are taken
from the shard that rendered them, so stubs Quarto writes for pages it did not
render (a redirecting index.html) never win.

Standard library only (the render jobs install nothing but Quarto). Reads only
the generated site/; never runs git. `make site` still renders in one go.
"""

from __future__ import annotations

import argparse
import filecmp
import json
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = {"_site", ".quarto", "_assets"}     # never pages
SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"


def pages(site: Path) -> list[str]:
    """Every page Quarto renders: the .qmd files of the generated site, relative."""
    out = []
    for p in site.rglob("*.qmd"):
        rel = p.relative_to(site)
        if rel.parts[0] not in SKIP:
            out.append(rel.as_posix())
    return sorted(out)


def folder_of(page: str) -> str:
    """The folder a page is rendered with: notes/<field>/<area>, else the first
    folder level (courses/<id>, library); "" for a top-level page."""
    parts = page.split("/")[:-1]
    return "/".join(parts[:3] if parts[:1] == ["notes"] else parts[:2])


def units(all_pages: list[str]) -> dict[str, str]:
    """Page -> its render unit. Units never overlap, because `quarto render <folder>`
    renders everything below it: a page whose folder holds another unit's folder
    (courses/cs70.qmd next to courses/cs70/) is a unit of its own, and so is a
    top-level page."""
    folders = {folder_of(p) for p in all_pages} - {""}
    nested = {f for f in folders if any(g.startswith(f + "/") for g in folders)}
    return {p: p if folder_of(p) in nested | {""} else folder_of(p) for p in all_pages}


def plan(site: Path, n: int) -> list[list[str]]:
    """Units per shard: largest first, each to the shard with the fewest pages."""
    size: dict[str, int] = {}
    for u in units(pages(site)).values():
        size[u] = size.get(u, 0) + 1
    shards: list[list[str]] = [[] for _ in range(n)]
    load = [0] * n
    for u in sorted(size, key=lambda u: (-size[u], u)):
        k = load.index(min(load))
        shards[k].append(u)
        load[k] += size[u]
    return [sorted(s) for s in shards]


def owner(site: Path, n: int) -> dict[str, int]:
    """Output page (.html) -> the shard that renders it."""
    shard_of = {u: k for k, s in enumerate(plan(site, n)) for u in s}
    return {p[:-4] + ".html": shard_of[u] for p, u in units(pages(site)).items()}


def render(site: Path, shard: int, n: int) -> int:
    todo = plan(site, n)[shard]
    print(f"shard {shard + 1}/{n}: {len(todo)} unit(s)", flush=True)
    for u in todo:
        print(f"quarto render {u}", flush=True)
        r = subprocess.run(["quarto", "render", u], cwd=site)
        if r.returncode:
            print(f"error: quarto render {u} failed ({r.returncode})")
            return r.returncode
    return 0


def merge_search(files: list[Path], own: dict[str, int]) -> list[dict]:
    """Join search.json files; an entry comes from the shard that owns its page."""
    seen: dict[str, dict] = {}
    for k, f in enumerate(files):
        if not f.exists():
            continue
        for e in json.loads(f.read_text(encoding="utf-8")):
            page = e["href"].split("#", 1)[0]
            if own.get(page, k) == k or e["objectID"] not in seen:
                seen[e["objectID"]] = e
    return sorted(seen.values(), key=lambda e: e["objectID"])


def merge_sitemap(files: list[Path]) -> str:
    """Join sitemap.xml files: one <url> per <loc>, sorted."""
    ET.register_namespace("", SITEMAP_NS)
    urls: dict[str, ET.Element] = {}
    for f in files:
        if f.exists():
            for u in ET.parse(f).getroot():
                loc = u.findtext(f"{{{SITEMAP_NS}}}loc") or ""
                urls.setdefault(loc, u)
    root = ET.Element(f"{{{SITEMAP_NS}}}urlset")
    root.extend(urls[k] for k in sorted(urls))
    ET.indent(root)
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(root, encoding="unicode") + "\n"


def merge(site: Path, n: int, out: Path, shard_sites: list[Path]) -> int:
    if len(shard_sites) != n:
        print(f"error: {n} shards expected, {len(shard_sites)} given")
        return 2
    own = owner(site, n)
    missing = [p for p, k in own.items() if not (shard_sites[k] / p).exists()]
    if missing:
        print(f"error: {len(missing)} page(s) not rendered, e.g. {missing[0]}")
        return 1
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    special = {"search.json", "sitemap.xml"}
    conflicts = 0
    for k, s in enumerate(shard_sites):
        for f in sorted(s.rglob("*")):
            if not f.is_file():
                continue
            rel = f.relative_to(s).as_posix()
            if rel in special:
                continue
            dest = out / rel
            if rel in own:
                if own[rel] != k:
                    continue   # a stub or a stale copy; the owner's page wins
            elif dest.exists():
                if not filecmp.cmp(f, dest, shallow=False):
                    conflicts += 1
                    print(f"warning: {rel} differs between shards; kept the first")
                continue
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, dest)
    search = merge_search([s / "search.json" for s in shard_sites], own)
    (out / "search.json").write_text(json.dumps(search, ensure_ascii=False), encoding="utf-8")
    (out / "sitemap.xml").write_text(merge_sitemap([s / "sitemap.xml" for s in shard_sites]), encoding="utf-8")
    print(f"merged {n} shards: {len(own)} pages, {len(search)} search entries, {conflicts} conflict(s)")
    return 0


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Render the website in shards and merge them.")
    ap.add_argument("command", choices=["plan", "render", "merge"])
    ap.add_argument("paths", nargs="*", type=Path, help="merge: OUT then each shard's _site, in order")
    ap.add_argument("--site", type=Path, default=ROOT / "site", help="the generated site folder")
    ap.add_argument("--of", type=int, required=True, help="number of shards")
    ap.add_argument("--shard", type=int, help="render: shard index, 0-based")
    a = ap.parse_args(argv)
    if a.of < 1:
        ap.error("--of must be at least 1")
    site = a.site.resolve()
    if a.command == "plan":
        own = owner(site, a.of)
        for k, units in enumerate(plan(site, a.of)):
            count = sum(1 for v in own.values() if v == k)
            print(f"shard {k}: {count} pages: {' '.join(units)}")
        return 0
    if a.command == "render":
        if a.shard is None or not 0 <= a.shard < a.of:
            ap.error("render needs --shard between 0 and --of minus 1")
        return render(site, a.shard, a.of)
    if len(a.paths) < 2:
        ap.error("merge needs OUT and the shard _site folders")
    return merge(site, a.of, a.paths[0], a.paths[1:])


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
