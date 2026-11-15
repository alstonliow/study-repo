"""The source registry (meta/sources.yml): which source-key prefixes exist,
which edition they refer to, and how a key is shown ("FIT1058 CN 1.16 Q2")."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass(frozen=True)
class Source:
    prefix: str
    title: str
    course: str
    edition: str
    pattern: re.Pattern
    label: str
    problem_label: str

    def show(self, key: str) -> str | None:
        m = self.pattern.match(key)
        if not m:
            return None
        parts = {k: v for k, v in m.groupdict().items() if v is not None}
        return (self.problem_label if "n" in parts else self.label).format(**parts)


class Sources:
    def __init__(self, meta: Path):
        path = meta / "sources.yml"
        data = (yaml.safe_load(path.read_text(encoding="utf-8")) or {}) if path.exists() else {}
        self.all = [Source(s["prefix"], s.get("title", ""), s.get("course", ""), str(s.get("edition", "")),
                           re.compile(s["pattern"]), s.get("label", "{section}"),
                           s.get("problem_label", s.get("label", "{section}")))
                    for s in data.get("sources") or []]

    def find(self, key: str) -> Source | None:
        return next((s for s in self.all if key.startswith(s.prefix)), None)

    def label(self, key: str) -> str:
        """How a key is shown; the key itself when no source knows it."""
        s = self.find(key)
        return (s.show(key) if s else None) or key

    def problems(self, key: str) -> str | None:
        """Why a key is not valid, or None."""
        s = self.find(key)
        if s is None:
            return f"source key '{key}' has no entry in meta/sources.yml"
        if not s.pattern.match(key):
            return f"source key '{key}' does not have the form of {s.prefix}… keys"
        return None
