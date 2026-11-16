"""Source keys (meta/SPEC.md §4, §6, §17.12.6): how a key such as
`fit1058-cn-1.16-q2` is checked and shown ("FIT1058 CN 1.16 Q2").

Source keys are citations. Each key belongs to the resource whose
`legacy_keys.prefix` it starts with, and resolves through that resource to an
explicit edition and node (build/resources.py). There is no other registry of
sources.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from resources import Resolution, Resource


class Sources:
    def __init__(self, resources: dict[str, "Resource"]):
        self.resources = [r for r in resources.values() if r.legacy is not None]

    def find(self, key: str) -> "Resource | None":
        return next((r for r in self.resources if r.legacy and key.startswith(r.legacy.prefix)), None)

    def resolve(self, key: str) -> "Resolution | None":
        r = self.find(key)
        res = r.resolve(key) if r else None
        return None if res is None or isinstance(res, str) else res

    def label(self, key: str) -> str:
        """How a key is shown; the key itself when no resource knows it."""
        r = self.find(key)
        return (r.key_label(key) if r else None) or key

    def problems(self, key: str) -> str | None:
        """Why a key is not valid, or None."""
        r = self.find(key)
        if r is None:
            return f"source key '{key}' belongs to no resource (no legacy_keys prefix matches)"
        res = r.resolve(key)
        return res if isinstance(res, str) else None
