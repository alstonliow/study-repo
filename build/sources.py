"""Source keys (meta/SPEC.md §4, §6, §17.12.6): how a key such as
`fit1058-cn-1.16-q2` is checked and shown ("FIT1058 CN 1.16 Q2").

Source keys are citations. Each key belongs to the resource whose
`legacy_keys.prefix` it starts with, and resolves through that resource to an
explicit edition and node (build/resources.py). There is no other registry of
sources.

A coding exercise cites its handout by the node id itself
(`source="res-stanford-cs221-hw-route"`, SPEC §6.4 item 3); such a key resolves
to that node in the current edition and is shown with the node's label.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from resources import Resolution, Resource


class Sources:
    def __init__(self, resources: dict[str, "Resource"]):
        self.resources = [r for r in resources.values() if r.legacy is not None]
        self.node_of = {nid: r for r in resources.values() for nid in r.nodes}   # node id -> resource

    def find(self, key: str) -> "Resource | None":
        return next((r for r in self.resources if r.legacy and key.startswith(r.legacy.prefix)), None)

    def resolve(self, key: str) -> "Resolution | None":
        if key in self.node_of:
            from resources import Resolution
            owner = self.node_of[key]
            return Resolution(owner.id, owner.current, key, owner.locator(key), None)
        r = self.find(key)
        res = r.resolve(key) if r else None
        return None if res is None or isinstance(res, str) else res

    def url(self, key: str) -> str:
        """The web address of a node cited by its id ('' when it has none)."""
        res = self.node_of.get(key)
        return str(res.nodes[key].extra.get("url") or "") if res else ""

    def label(self, key: str) -> str:
        """How a key is shown; the key itself when no resource knows it."""
        if key in self.node_of:
            return self.node_of[key].label(key)
        r = self.find(key)
        return (r.key_label(key) if r else None) or key

    def problems(self, key: str) -> str | None:
        """Why a key is not valid, or None."""
        if key in self.node_of:
            return None
        r = self.find(key)
        if r is None:
            return f"source key '{key}' belongs to no resource (no legacy_keys prefix matches)"
        res = r.resolve(key)
        return res if isinstance(res, str) else None
