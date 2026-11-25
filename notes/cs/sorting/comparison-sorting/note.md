---
title: "Sorting by Comparisons"
sources: [mit6006-3, mit6006r-3]
requires: [cs/data-structures/interfaces]
aliases: [cs/data-structures/comparison-sorting]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 3 and Recitation 3, in our own wording; proofs written out in steps. Algorithms are described in words, not copied code. On 2026-11-25 the algorithms moved to their own notes (one algorithm per note, SPEC §8.6); this note is their overview. -->

## The sorting problem

::: {#def-sorting-problem .definition name="Sorting"}

*Sorting*: given an array $A$ of $n$ items with keys, output a permutation $B$ of $A$ with $B[i-1].\mathrm{key}\le B[i].\mathrm{key}$ for $1\le i<n$. A sorting algorithm is

1. *destructive* if it overwrites $A$ instead of producing a new array,
2. *in place* if it uses only $O(1)$ extra space (so it is destructive), and
3. *stable* if items with equal keys appear in $B$ in the same relative order as in $A$.

:::

Trying all $n!$ permutations and checking each in $\Theta(n)$ time ("permutation sort") is correct by exhaustion but takes $\Omega(n!\cdot n)$ time. The following algorithms do much better.

## The algorithms

Each comparison sort has its own note: selection and insertion sort (@sec-cs-sorting-elementary-sorts), merge sort (@sec-cs-sorting-merge-sort) and heap sort (@sec-cs-sorting-heap-sort). A sorted array can then be searched by binary search (@sec-cs-sorting-binary-search). No comparison sort beats $\Omega(n\log n)$ comparisons in the worst case (@thm-comparison-sort-lower-bound).

| algorithm | worst-case time | in place | stable |
|---|---|---|---|
| selection sort (@def-selection-sort) | $\Theta(n^2)$ | yes | no |
| insertion sort (@def-insertion-sort) | $\Theta(n^2)$ | yes | yes |
| merge sort (@def-merge-sort) | $\Theta(n\log n)$ | no | yes |
| heap sort (@def-heap-sort) | $O(n\log n)$ | yes | no |
