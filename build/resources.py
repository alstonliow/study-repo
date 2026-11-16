"""Resources (meta/SPEC.md §17.12): resource files, their node hierarchy,
editions and locators, and the resolver for legacy source keys.

A resource file is `resources/<slug>.yml` (public). The private store
(`private/resources/`) comes in a later round. A resource's nodes form a tree;
each node has a stable id and, per edition, a locator (`at`). A legacy source
key such as `fit1058-cn-5.4-q3` resolves deterministically:

    prefix -> resource + fixed edition;  pattern -> locator "5.4" and question 3;
    locator -> the one node whose `at` has "5.4" for that edition.

Locators are matched exactly ("1" is never "1.1"). A key that matches no node
is an error, never a guess. Model code reads resources through `load()`; the
labels of source keys come from `Sources` (build/sources.py), built on this.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ID = re.compile(r"res-[a-z0-9]+(?:-[a-z0-9]+)*")


@dataclass
class Node:
    id: str
    kind: str                         # chapter | section | exercises | ...
    title: str
    at: dict[str, str]                # edition id -> locator in that edition
    parent: str                       # parent node id, or the resource id
    children: list[str] = field(default_factory=list)
    extra: dict = field(default_factory=dict)          # other fields, e.g. relationships (covers: [...])


@dataclass
class LegacyKeys:
    prefix: str
    edition: str
    pattern: re.Pattern
    label: str
    problem_label: str


@dataclass
class Resolution:
    """What a legacy key means: resource, edition, node, locator, question."""
    resource: str
    edition: str
    node: str
    locator: str
    question: int | None


@dataclass
class Resource:
    id: str
    path: Path
    kind: str
    title: str
    status: str
    editions: list[str]
    legacy: LegacyKeys | None
    nodes: dict[str, Node]            # in file order
    roots: list[str]
    visibility: str = "public"
    problems: list[str] = field(default_factory=list)   # found while loading
    meta: dict = field(default_factory=dict)            # the other fields (courses, authors, url, ...)
    current_marks: list[str] = field(default_factory=list)   # editions marked current: true

    @property
    def slug(self) -> str:
        return self.id[len("res-"):]

    @property
    def current(self) -> str:
        """The current edition (the one marked current, else the first)."""
        return self._current

    def locator(self, node_id: str) -> str:
        """The node's locator in the current edition ('' if it has none there)."""
        n = self.nodes.get(node_id)
        return n.at.get(self.current, "") if n else ""

    def short(self, locator: str) -> str:
        """'FIT1058 CN 5.5': the legacy label when there is one, else title and locator."""
        if self.legacy:
            return self.legacy.label.format(section=locator)
        return f"{self.title} {locator}".strip()

    def label(self, eid: str) -> str:
        """How a resource or one of its nodes is named in links:
        'FIT1058 Course Notes' or 'FIT1058 CN 5.5 Quantifiers'."""
        if eid == self.id:
            return self.title
        n = self.nodes[eid]
        loc = self.locator(eid)
        return f"{self.short(loc)} {n.title}" if loc else n.title

    def node_at(self, edition: str, locator: str) -> Node | None:
        """The node at an exact locator in one edition."""
        return self._at.get((edition, locator))

    def resolve(self, key: str) -> Resolution | str:
        """A legacy key -> Resolution, or the reason it does not resolve."""
        lk = self.legacy
        if lk is None or not key.startswith(lk.prefix):
            return f"source key '{key}' is not a key of {self.id}"
        m = lk.pattern.match(key)
        if not m:
            return f"source key '{key}' does not have the form of {lk.prefix}… keys"
        loc = m.group("section")
        node = self.node_at(lk.edition, loc)
        if node is None:
            return f"source key '{key}': no node of {self.id} is at {loc} in edition {lk.edition}"
        q = m.groupdict().get("n")
        return Resolution(self.id, lk.edition, node.id, loc, int(q) if q else None)

    def key_label(self, key: str) -> str | None:
        r = self.resolve(key)
        if isinstance(r, str) or self.legacy is None:
            return None
        fmt = self.legacy.problem_label if r.question is not None else self.legacy.label
        return fmt.format(section=r.locator, n=r.question)

    def __post_init__(self):
        self._current = next((e for e in self.editions if e in self.current_marks), self.editions[0] if self.editions else "")
        self._at: dict[tuple[str, str], Node] = {}
        for n in self.nodes.values():
            for ed, loc in n.at.items():
                if (ed, loc) in self._at:
                    self.problems.append(f"{n.id}: locator {loc} of edition {ed} is also "
                                         f"{self._at[(ed, loc)].id}")
                else:
                    self._at[(ed, loc)] = n


def parse(path: Path) -> Resource:
    d = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    problems: list[str] = []
    rid = str(d.get("id", ""))
    if not ID.fullmatch(rid):
        problems.append(f"id '{rid}' must be res-<lowercase words joined by hyphens>")
    elif rid != "res-" + path.stem:
        problems.append(f"id '{rid}' must match the file name (res-{path.stem})")
    editions = [str(e["id"]) for e in d.get("editions") or []]
    nodes: dict[str, Node] = {}
    roots: list[str] = []

    def walk(items, parent: str) -> list[str]:
        ids = []
        for item in items or []:
            nid = str(item.get("id", ""))
            if not ID.fullmatch(nid) or not nid.startswith(rid + "-"):
                problems.append(f"node id '{nid}' must start with '{rid}-' (lowercase words joined by hyphens)")
            if nid in nodes:
                problems.append(f"node id '{nid}' is used twice")
            at = {str(k): str(v) for k, v in (item.get("at") or {}).items()}
            for ed in at:
                if ed not in editions:
                    problems.append(f"{nid}: edition '{ed}' is not listed under editions")
            nodes[nid] = Node(nid, str(item.get("kind", "")), str(item.get("title", "")), at, parent,
                              extra={k: v for k, v in item.items() if k not in ("id", "kind", "title", "at", "nodes")})
            nodes[nid].children = walk(item.get("nodes"), nid)
            ids.append(nid)
        return ids
    roots = walk(d.get("nodes"), rid)
    lk = None
    if d.get("legacy_keys"):
        k = d["legacy_keys"]
        lk = LegacyKeys(str(k["prefix"]), str(k["edition"]), re.compile(k["pattern"]),
                        str(k.get("label", "{section}")), str(k.get("problem_label", k.get("label", "{section}"))))
        if lk.edition not in editions:
            problems.append(f"legacy_keys: edition '{lk.edition}' is not listed under editions")
        if "section" not in lk.pattern.groupindex:
            problems.append("legacy_keys: pattern needs a (?P<section>...) group")
    for key in ("authors", "url"):
        if key in d and not d[key]:
            problems.append(f"'{key}' is empty; leave it out instead")
    known = {"id", "kind", "title", "status", "editions", "legacy_keys", "nodes"}
    return Resource(rid, path, str(d.get("kind", "")), str(d.get("title", "")), str(d.get("status", "draft")),
                    editions, lk, nodes, roots, problems=problems,
                    meta={k: v for k, v in d.items() if k not in known},
                    current_marks=[str(e["id"]) for e in d.get("editions") or [] if e.get("current")])


def load(root: Path) -> dict[str, Resource]:
    """All public resources: resources/*.yml under root."""
    folder = root / "resources"
    out = {}
    for p in sorted(folder.glob("*.yml")) if folder.exists() else []:
        r = parse(p)
        out[r.id or p.stem] = r
    return out
