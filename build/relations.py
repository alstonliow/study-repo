"""Typed relationships, references and backlinks (meta/SPEC.md §17.4–§17.6).

Relationship types come only from meta/relations.yml. A relationship is
written once, at its source: `requires` and `relations:` in a note's YAML, or
an attribute named after the type on a block's div (`uses="def-a def-b"`).
References are the `@` links in the text. Both are collected here from the
model (build/model.py parses the files), and both feed one backlink index:

    canonical records -> Graph.backward[target] -> rendered backlinks

Inverse names ("used by") are display names; they are never stored.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING

import yaml

from model import META, REF

if TYPE_CHECKING:
    from model import Note, Repo


@dataclass(frozen=True)
class RelType:
    name: str
    inverse: str
    symmetric: bool
    acyclic: bool
    between: frozenset[str]          # "notes", "blocks", "resources", "nodes"
    sources: frozenset[str] = frozenset()   # allowed at the source end (default: between)
    targets: frozenset[str] = frozenset()   # allowed at the target end (default: between)


def load_types(meta: Path = META) -> dict[str, RelType]:
    path = meta / "relations.yml"
    data = (yaml.safe_load(path.read_text(encoding="utf-8")) or {}) if path.exists() else {}
    out = {}
    for t in data.get("types") or []:
        between = frozenset(t.get("between") or ["notes", "blocks"])
        out[t["name"]] = RelType(t["name"], t.get("inverse", t["name"]), bool(t.get("symmetric")),
                                 bool(t.get("acyclic")), between,
                                 frozenset(t.get("from") or between), frozenset(t.get("to") or between))
    return out


@dataclass
class Relation:
    source: str
    type: str
    target: str
    where: str                        # file (and line) it is written in
    meta: dict = field(default_factory=dict)   # optional metadata ({to: id, note: ...}), SPEC §17.5.2


@dataclass
class Reference:
    source: str                       # block id, or the note id for text outside blocks
    holder: str                       # note (or review folder) the text is in
    target: str                       # block id or note id
    where: str


@dataclass
class Link:
    """One entry in the index: a relationship or a reference seen from one end."""
    kind: str                         # "relation" or "reference"
    name: str                         # relation type, or "references"
    other: str                        # the entity at the other end
    holder: str = ""                  # for references: the note the text is in


class Graph:
    def __init__(self, repo: "Repo"):
        self.repo = repo
        self.types = load_types()
        self.relations: list[Relation] = []
        self.references: list[Reference] = []
        self.problems: list[tuple[str, str]] = []           # (level, message), read by check.py
        self.cited_by: dict[str, list[Link]] = {}           # node id -> notes and problems citing it
        self._collect_relations()
        self._collect_resource_relations()
        self._collect_references()
        self._collect_citations()
        self.forward: dict[str, list[Link]] = {}
        self.backward: dict[str, list[Link]] = {}
        for r in self.relations:
            if r.target not in repo.entities or r.source == r.target:
                continue
            self.forward.setdefault(r.source, []).append(Link("relation", r.type, r.target))
            self.backward.setdefault(r.target, []).append(Link("relation", r.type, r.source))
        self.referenced_by: dict[str, list[Link]] = {}
        for ref in self.references:
            self.referenced_by.setdefault(ref.target, []).append(Link("reference", "references", ref.source, ref.holder))

    # ------------------------------------------------------------ relationships
    def _add(self, source: str, rtype: str, item, where: str) -> None:
        if isinstance(item, dict):
            target = str(item.get("to", ""))
            meta = {k: v for k, v in item.items() if k != "to"}
        else:
            target, meta = str(item), {}
        if not target:
            self.problems.append(("error", f"{where}: {rtype}: an entry without a target id"))
            return
        self.relations.append(Relation(source, rtype, target, where, meta))

    def _collect_relations(self) -> None:
        repo = self.repo
        for n in repo.notes.values():
            where = f"notes/{n.id}/note.md"
            for r in n.front.get("requires") or []:
                self.relations.append(Relation(n.id, "requires", str(r), where))
            rel = n.front.get("relations")
            if rel is None:
                pass
            elif not isinstance(rel, dict):
                self.problems.append(("error", f"{where}: relations must map a type to a list of ids"))
            else:
                for rtype, items in rel.items():
                    if rtype == "requires":
                        self.problems.append(("error", f"{where}: write requires as the top-level field, not under relations"))
                        continue
                    if rtype not in self.types:
                        self.problems.append(("error", f"{where}: unknown relationship type '{rtype}' "
                                                       "(see meta/relations.yml)"))
                        continue
                    for item in items if isinstance(items, list) else [items]:
                        self._add(n.id, str(rtype), item, where)
        for n in list(repo.notes.values()) + list(repo.reviews.values()):
            for f in n.files.values():
                if f.name == "solution.md":
                    continue
                for d in f.divs:
                    if not d.id:
                        continue
                    for key, value in d.attrs.items():
                        if key in self.types:
                            for target in str(value).split():
                                self._add(d.id, key, target, f"notes/{n.id}/{f.name}:{d.line}")

    def _collect_resource_relations(self) -> None:
        """Relationships written in resource files: on the resource or on a
        node, a field named after the type (covers: [...]), SPEC §17.12.4."""
        for res in self.repo.resources.values():
            where = str(res.path.relative_to(self.repo.root)) if res.path.is_relative_to(self.repo.root) else str(res.path)
            items = [(res.id, res.meta)] + [(n.id, n.extra) for n in res.nodes.values()]
            for source, fields in items:
                for key, value in fields.items():
                    if key in self.types:
                        for item in value if isinstance(value, list) else [value]:
                            self._add(source, key, item, f"{where} ({source})")

    def _collect_citations(self) -> None:
        """Citations (SPEC §17.12.5): source keys of notes and problems, resolved
        to resource nodes. Provenance, not relationships."""
        repo = self.repo
        for n in list(repo.notes.values()) + list(repo.reviews.values()):
            keys = [(n.id, str(k)) for k in n.front.get("sources") or []]
            keys += [(p.id, p.attrs.get("source", "")) for p in n.problems if p.id]
            for source, key in keys:
                res = repo.sources.resolve(key) if key else None
                if res:
                    self.cited_by.setdefault(res.node, []).append(Link("citation", "cites", source, n.id))

    def check(self) -> list[tuple[str, str]]:
        """Problems with relationships (SPEC §17.5.8). `requires` targets and
        cycles are checked by the model's own requires rules (SPEC §4)."""
        out = list(self.problems)
        ents, alias = self.repo.entities, self.repo.alias_of
        seen: set[tuple[str, str, str]] = set()
        for r in self.relations:
            t = self.types.get(r.type)
            if t is None:
                out.append(("error", f"{r.where}: unknown relationship type '{r.type}'"))
                continue
            in_yaml = r.type == "requires" and r.source in self.repo.notes
            if in_yaml:
                continue                  # the requires field: checked by the requires rules (SPEC §4)
            if r.target not in ents:
                if r.target in alias:
                    out.append(("error", f"{r.where}: {r.type} '{r.target}' is an old id; "
                                         f"use the current id '{alias[r.target]}'"))
                else:
                    out.append(("error", f"{r.where}: {r.type} unknown id '{r.target}'"))
                continue
            if r.source == r.target:
                out.append(("error", f"{r.where}: {r.source} {r.type} itself"))
                continue
            if r.source in ents and ents[r.source].level not in t.sources:
                out.append(("error", f"{r.where}: {r.type} is only from {' and '.join(sorted(t.sources))}, "
                                     f"not {ents[r.source].level} ('{r.source}')"))
            if ents[r.target].level not in t.targets:
                out.append(("error", f"{r.where}: {r.type} is only to {' and '.join(sorted(t.targets))}, "
                                     f"not {ents[r.target].level} ('{r.target}')"))
            key = (r.source, r.type, r.target)
            if key in seen:
                out.append(("warning", f"{r.where}: {r.source} {r.type} {r.target} is written twice"))
            elif t.symmetric and (r.target, r.type, r.source) in seen:
                out.append(("warning", f"{r.where}: {r.type} is symmetric; write it on one side only "
                                       f"({r.source}, {r.target})"))
            seen.add(key)
        for t in self.types.values():
            if t.acyclic and t.name != "requires":
                for cycle in self.cycles(t.name):
                    out.append(("error", f"{t.name} has a cycle: {' -> '.join(cycle + [cycle[0]])}"))
        return out

    def cycles(self, rtype: str) -> list[list[str]]:
        """Cycles in one type's graph over all notes and blocks, one per
        strongly connected group (SPEC §17.5.5)."""
        edges: dict[str, list[str]] = {}
        for r in self.relations:
            if r.type == rtype and r.target in self.repo.entities and r.source != r.target:
                edges.setdefault(r.source, []).append(r.target)

        def reach(a: str) -> set[str]:
            seen, stack = set(), list(edges.get(a, []))
            while stack:
                x = stack.pop()
                if x not in seen:
                    seen.add(x)
                    stack += edges.get(x, [])
            return seen
        reached = {a: reach(a) for a in edges}
        out, done = [], set()
        for a in sorted(edges):
            if a in done or a not in reached[a]:
                continue
            group = sorted(b for b in reached[a] if a in reached.get(b, set()))
            done.update(group)
            out.append(group)
        return out

    # ------------------------------------------------------------ references
    def _collect_references(self) -> None:
        repo = self.repo
        sec = {n.sec_label: n.id for n in repo.notes.values()}
        for n in list(repo.notes.values()) + list(repo.reviews.values()):
            for f in n.files.values():
                lines = f.masked.split("\n")
                owner_of_line: list[str] = [n.id] * len(lines)
                last: str | None = None
                for d in f.divs:
                    if d.depth:
                        continue
                    if f.name == "solution.md":
                        src = d.attrs.get("for") or n.id
                    elif d.has("proof") and not d.has("remark"):
                        src = last or n.id
                    else:
                        src = d.id or n.id
                        last = d.id
                    for i in range(d.line - 1, min(d.end, len(lines))):
                        owner_of_line[i] = src
                for i, line in enumerate(lines):
                    for m in REF.finditer(line):
                        ref = m.group(1)
                        target = sec.get(ref) if ref.startswith("sec-") else (ref if ref in repo.entities else None)
                        if target is None:
                            continue                              # check.py reports broken references
                        tholder = repo.entities[target].holder
                        if tholder == n.id:
                            continue                              # references within one page are not backlinks
                        self.references.append(Reference(owner_of_line[i], n.id, target, f"notes/{n.id}/{f.name}:{i + 1}"))

    # ------------------------------------------------------------ views
    def outgoing(self, eid: str) -> list[Link]:
        """Relationships written at eid, and symmetric ones written at the other end."""
        out = [l for l in self.forward.get(eid, [])]
        out += [l for l in self.backward.get(eid, []) if self.types[l.name].symmetric]
        return out

    def incoming(self, eid: str) -> list[Link]:
        """Relationships that point to eid (shown with the inverse name)."""
        return [l for l in self.backward.get(eid, []) if not self.types[l.name].symmetric]

    def word(self, link: Link, forward: bool) -> str:
        t = self.types[link.name]
        return t.name if forward or t.symmetric else t.inverse


def page_entities(note: "Note") -> list[str]:
    """The note and its blocks, in page order."""
    return [note.id] + list(note.blocks)
