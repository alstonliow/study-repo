"""Filters: which blocks and problems a page or PDF shows (meta/SPEC.md §15).

One Filter combines the reader's choices: kinds of block (groups from
kinds.GROUPS), exercise levels, and a course whose scope must be kept. Chapter
summaries and PDFs use it; the Export page applies the same rules in the browser
from site-data.json.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

import kinds

if TYPE_CHECKING:
    from model import Course, Repo

ALL_GROUPS = frozenset(g for g, _ in kinds.GROUPS)
ALL_LEVELS = frozenset(("easy", "medium", "hard", "unrated"))


@dataclass
class Filter:
    repo: "Repo"
    groups: frozenset = ALL_GROUPS
    levels: frozenset = ALL_LEVELS
    course: "Course | None" = None
    omit_extra: bool = False          # keep only the course's scope
    unknown: set = field(default_factory=set)

    def __post_init__(self):
        self.unknown = set(self.groups) - ALL_GROUPS
        if self.omit_extra and self.course is None:
            raise ValueError("omitting extra content needs a course")

    def shows(self, group: str | None) -> bool:
        """Is this group of blocks shown? Blocks without a group always are."""
        return group is None or group in self.groups

    def in_scope(self, note, block_id: str | None) -> bool:
        if not self.omit_extra or block_id is None:
            return True
        assert self.course is not None
        return self.repo.in_scope(self.course, note.id, block_id)

    def block(self, note, block_id: str | None) -> bool:
        """Scope and group of a block (by id)."""
        return self.in_scope(note, block_id) and self.shows(kinds.group(block_id))

    def problem(self, note, pid: str, level: str) -> bool:
        if (level or "unrated") not in self.levels:
            return False
        if not self.omit_extra or self.course is None:
            return True
        if note.id in self.repo.notes:
            return self.repo.in_scope(self.course, note.id, pid)
        return self.course.id in self.repo.review_courses(note.branch, pid)
