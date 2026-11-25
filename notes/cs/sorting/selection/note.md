---
title: "Selection"
sources: [mit6046-2, mit6046-6]
requires: [cs/sorting/comparison-sorting]
status: draft
---

<!-- Added 2026-11-25 as the overview of the selection algorithms (one algorithm per note, SPEC §8.6); @def-select moved here from cs/algorithms/divide-and-conquer (MIT 6.046 Spring 2015, Lecture 2), in our own wording. -->

::: {#def-select .definition name="Selection"}

`select(S, i)` returns the element of rank $i$ in a set $S$ of $n$ distinct numbers (the median is rank $\lceil n/2\rceil$). Sorting gives $O(n\log n)$; we want $O(n)$.

:::

## The algorithms

Both algorithms partition $S$ around a pivot $x$ and recurse into the one side that holds rank $i$; they differ in how the pivot is chosen. Randomized selection (@sec-cs-sorting-randomized-selection) picks it at random; median of medians (@sec-cs-sorting-median-of-medians) computes a pivot that is guaranteed to be near the middle.

| algorithm | pivot | time |
|---|---|---|
| sort, then index (@thm-merge-sort) | none | $O(n\log n)$ worst case |
| randomized selection (@thm-randomized-select) | uniformly random | $O(n)$ expected |
| median of medians (@thm-median-of-medians) | median of the group medians | $O(n)$ worst case |
