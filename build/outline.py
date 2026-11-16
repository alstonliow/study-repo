"""Outlines: the ordered trees that organise and number the notes (meta/SPEC.md §16).

An outline is a list of chapters, each with its notes in order and the review
folders whose synthesis problems end the chapter. There are two sources with
the same shape:

- the topic outline, from meta/taxonomy.yml: books (parts) -> chapters
  (branches) -> notes; chapter numbers restart in each book;
- one outline per course, from meta/courses/<id>.yml: course chapters -> notes
  in course order.

Every number on the website and in PDFs comes from an outline; switching the
course filter on means using that course's outline.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Chapter:
    key: str                 # branch id, or "<course id>:<chapter number>"
    num: str                 # "8"
    title: str               # "Number Theory"
    book: str                # the book (part) for topic chapters; the course code for course chapters
    notes: list = field(default_factory=list)
    reviews: list = field(default_factory=list)

    @property
    def label(self) -> str:
        return f"{self.num} {self.title}"


@dataclass
class Outline:
    name: str                # "topic" or a course id
    chapters: list[Chapter]

    def numbers(self) -> dict[str, str]:
        """note id -> section number in this outline ("8.1")."""
        return {n.id: f"{ch.num}.{k}" for ch in self.chapters for k, n in enumerate(ch.notes, 1)}

    def chapter_of(self, nid: str) -> Chapter | None:
        return next((ch for ch in self.chapters if any(n.id == nid for n in ch.notes)), None)

    def apply(self) -> None:
        """Set note.num (shown in titles) to this outline's numbers."""
        nums = self.numbers()
        for ch in self.chapters:
            for n in ch.notes:
                n.num = nums[n.id]


def topic(repo) -> Outline:
    """Chapter numbers restart in each book. Parts marked `book: false` are no
    book (SPEC §17.7): their chapters share one sequence, and their book is ''."""
    chapters = []
    seq: dict[str | None, int] = {}
    for part, branches in repo.parts:
        book = None if part in repo.unbooked else part
        for bid, title in branches:
            members = repo.branch_members(bid)
            if not members:
                continue
            seq[book] = seq.get(book, 0) + 1
            chapters.append(Chapter(bid, str(seq[book]), title, book or "", members,
                                    [repo.reviews[bid]] if bid in repo.reviews else []))
    return Outline("topic", chapters)


def course(repo, c, only_in_scope: bool = False) -> Outline:
    """Course order. A branch's synthesis problems close the last course chapter
    that uses the branch."""
    last: dict[str, int] = {}
    for nid, p in c.order:
        last[repo.notes[nid].branch] = p.chapter
    chapters = []
    for ch in c.chapters:
        notes = [repo.notes[nid] for nid, p in c.order if p.chapter == ch["num"]]
        if only_in_scope:
            notes = [n for n in notes if repo.in_scope(c, n.id)]
        if not notes:
            continue
        reviews = [repo.reviews[b] for b, lc in last.items() if lc == ch["num"] and b in repo.reviews]
        chapters.append(Chapter(f"{c.id}:{ch['num']}", str(ch["num"]), ch["title"], c.code, notes, reviews))
    return Outline(c.id, chapters)
