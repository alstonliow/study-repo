"""Numbers for everything that is numbered (meta/SPEC.md §16).

A Numbering is built from one outline (outline.topic or outline.course) and
meta/numbering.yml. It answers every "what is this called" question: a note's
section number, a block's number (Theorem 8.1.2), an exercise's number on its
page (3) or elsewhere (8.1.3), a synthesis problem's number (Review 8.1), and
the label of a reference, with the book's title added across books. The
website, summaries, PDFs and the page scripts all use it.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

import yaml

import kinds

if TYPE_CHECKING:
    from model import Note, Repo
    from outline import Outline


@dataclass
class Formats:
    block: str = "{section}.{n}"
    numbered: tuple[str, ...] = ("def", "thm", "prp", "lem", "cor", "exm", "fig")
    exercise_page: str = "{n}"
    exercise_ref: str = "{section}.{n}"
    review_word: str = "Review"
    review: str = "{chapter}.{n}"
    cross_book: str = "{label} ({book})"

    @classmethod
    def load(cls, meta: Path) -> "Formats":
        path = meta / "numbering.yml"
        data = (yaml.safe_load(path.read_text(encoding="utf-8")) or {}) if path.exists() else {}
        f = cls()
        for k, v in data.items():
            if hasattr(f, k):
                setattr(f, k, tuple(v) if k == "numbered" else str(v))
        return f


class Numbering:
    def __init__(self, repo: "Repo", outline: "Outline", topic: "Outline", formats: Formats):
        self.repo, self.formats = repo, formats
        self.section = outline.numbers()                         # note id -> "8.1"
        self.chapter_of_review = {rv.id: ch.num for ch in outline.chapters for rv in ch.reviews}
        self.book = {n.id: ch.book for ch in topic.chapters for n in ch.notes}   # books are topic parts
        for ch in topic.chapters:
            for rv in ch.reviews:
                self.book[rv.id] = ch.book
        self._blocks: dict[str, str] = {}
        for nid in self.section:
            self._number_blocks(repo.notes[nid])

    def _number_blocks(self, note: "Note") -> None:
        counters: dict[str, int] = {}
        for name in ("note.md", "example.md"):          # page order
            f = note.files.get(name)
            if not f:
                continue
            for d in f.divs:
                k = kinds.of(d.id)
                if d.id and k and k.prefix in self.formats.numbered and k.prefix != "prob":
                    counters[k.prefix] = counters.get(k.prefix, 0) + 1
                    self._blocks[d.id] = self.formats.block.format(
                        section=self.section[note.id], n=counters[k.prefix])

    # ---- numbers
    def block(self, block_id: str) -> str:
        """'8.1.2' for a numbered block, '' otherwise."""
        return self._blocks.get(block_id, "")

    def exercise(self, note: "Note", pid: str, on_page: bool) -> str:
        n = note.exercise_number(pid) or 0
        if note.id in self.chapter_of_review or note.id.endswith("/review"):
            return self.formats.review.format(chapter=self.chapter_of_review.get(note.id, "?"), n=n)
        fmt = self.formats.exercise_page if on_page else self.formats.exercise_ref
        return fmt.format(section=self.section.get(note.id, "?"), n=n)

    def exercise_word(self, note: "Note") -> str:
        return self.formats.review_word if note.id not in self.repo.notes else kinds.word("prob-")

    # ---- labels
    def label(self, block_id: str, holder: "Note", here=None, wrap=None) -> str:
        """'Theorem 8.1.2', 'Exercise 8.1.3', 'Review 8.1', with the book's title
        added when the target is in another book than `here`. wrap(number,
        note id) may mark the number up (the website does, for the course filter)."""
        wrap = wrap or (lambda num, nid: num)
        k = kinds.of(block_id)
        if k and k.prefix == "prob":
            num = self.exercise(holder, block_id, on_page=False)
            is_review = holder.id not in self.repo.notes
            text = f"{self.exercise_word(holder)} {num if is_review else wrap(num, holder.id)}"
        else:
            num = self.block(block_id)
            text = f"{k.word if k else ''} {wrap(num, holder.id)}".strip() if num else (k.word if k else "")
        return self.across(text, holder, here)

    def across(self, text: str, holder: "Note", here=None) -> str:
        """Add the target's book when `here` is in another collection: another
        book, or no book at all (SPEC §16.1). A target outside any book gets no
        name; a page whose place is unknown adds nothing."""
        hid = getattr(here, "id", None)
        b = self.book.get(holder.id)
        if b and hid in self.book and self.book[hid] != b:
            return self.formats.cross_book.format(label=text, book=b)
        return text

    def as_data(self) -> dict[str, str]:
        """note id -> section number, for the page scripts."""
        return dict(self.section)


def build(repo: "Repo", outline: "Outline | None" = None) -> Numbering:
    import outline as outlines
    from model import META
    topic = outlines.topic(repo)
    return Numbering(repo, outline or topic, topic, Formats.load(META))
