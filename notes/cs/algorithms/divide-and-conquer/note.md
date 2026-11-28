---
title: "Divide and Conquer"
sources: [mit6046-2, mit6046r-1]
requires: []
aliases: [cs/algorithm-design/divide-and-conquer]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 2 and Recitation 1, in our own wording; proofs written out in steps. On 2026-11-25 the algorithms moved to their own notes (one algorithm per note, SPEC §8.6); this note is their overview. -->

*Divide and conquer*: split a problem of size $n$ into $a$ subproblems of size $n/b$, solve them recursively, and combine the answers. The running time satisfies $T(n)=aT(n/b)+(\text{divide and combine time})$, solved by the master theorem (@thm-master-theorem).

## The algorithms

Each algorithm has its own note: the convex hull (@sec-cs-computational-geometry-convex-hull), selection in linear time by the median of medians (@sec-cs-sorting-median-of-medians) and Strassen's matrix multiplication (@sec-cs-algorithms-strassen). Merge sort (@sec-cs-sorting-merge-sort) is another example.

| algorithm | recurrence | time |
|---|---|---|
| convex hull (@def-hull-divide-conquer) | $T(n)=2T(n/2)+O(n)$ | $O(n\log n)$ |
| median of medians (@thm-median-of-medians) | $T(n)\le T(\lceil n/5\rceil)+T(\frac{7n}{10}+6)+O(n)$ | $O(n)$ |
| Strassen (@thm-strassen) | $T(n)=7T(n/2)+O(n^2)$ | $O(n^{\log_27})$ |
