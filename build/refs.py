"""Reference targets (meta/SPEC.md §7.4): what an @-reference points to.

`Resolver.find("thm-x")` / `find("sec-math-...")` returns a Target: the kind of
block (or a whole note), the note or review folder that owns it, and its name.
Renderers decide how to show it: the website as a link, PDFs as a LaTeX
cross-reference or plain text. Both describe targets with `describe()`, so a
reference reads the same everywhere.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

import kinds

if TYPE_CHECKING:
    from model import Note, Repo


@dataclass
class Target:
    ref: str
    note: "Note"                 # the Note (or review folder) that holds it
    kind: kinds.Kind | None      # None for a whole note (@sec-...)
    name: str = ""

    @property
    def is_note(self) -> bool:
        return self.kind is None


class Resolver:
    def __init__(self, repo: "Repo"):
        self.repo = repo
        self.sec = {n.sec_label: n for n in repo.notes.values()}
        self.holder = {bid: n for n in list(repo.notes.values()) + list(repo.reviews.values()) for bid in n.blocks}

    def find(self, ref: str) -> Target | None:
        if ref.startswith("sec-"):
            n = self.sec.get(ref)
            return Target(ref, n, None, "") if n else None
        n = self.holder.get(ref)
        if n is None:
            return None
        return Target(ref, n, kinds.of(ref), n.blocks.get(ref, ""))

    def resource_of(self, ref: str):
        """(Resource, ref) when ref is a resource or a resource node, else None."""
        e = self.repo.entities.get(ref)
        if e is None or e.type not in ("resource", "resource-node"):
            return None
        return self.repo.resources[e.holder], ref

    def resource_label(self, ref: str) -> str | None:
        """'FIT1058 CN 5.5 Quantifiers' for a node, the title for a resource."""
        rr = self.resource_of(ref)
        return rr[0].label(ref) if rr else None

    def describe(self, t: Target) -> str:
        """Plain words for a target: '8.1 Divisibility', 'Theorem (Euclid)',
        'Theorem in 8.1 Divisibility'."""
        if t.is_note:
            return t.note.display_title
        word = t.kind.word if t.kind else ""
        from model import REF
        name = REF.sub(lambda m: self.title(m.group(1)), t.name)   # a name may cite: keep it plain text
        return f"{word} ({name})" if name else f"{word} in {t.note.display_title}"

    def title(self, ref: str) -> str:
        """Bare title, safe inside maths (no braces or backslashes)."""
        t = self.find(ref)
        text = t.note.title if t else (self.resource_label(ref) or ref)
        return text.replace("\\", "").replace("{", "").replace("}", "")
