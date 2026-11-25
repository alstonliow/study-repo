---
title: "Dynamic Programming on Intervals"
sources: [mit6046-10, mit6046-1, mit6046r-1, mit6046r-5]
requires: [cs/algorithm-design/subproblem-design]
aliases: [cs/dynamic-programming/interval-subproblems]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lectures 1 and 10 and Recitations 1 and 5, in our own wording; examples our own (checked by computation); proofs written out in steps. The alternating coin game of Lecture 10 is @exm-coin-game. On 2026-11-25 weighted interval scheduling, the longest palindromic subsequence, optimal binary search trees and stacking blocks (in @sec-cs-algorithm-design-lis) moved to their own notes (one problem per note, SPEC §8.6); this note is their overview. -->

Many problems on sequences use *substring* subproblems $x(i,j)$, one for each contiguous piece, and guess where the piece splits. There are $O(n^2)$ of them, so the running time is $O(n^2)$ times the work per subproblem.

## The problems

| problem | subproblems | guess | time |
|---|---|---|---|
| alternating coin game (@sec-cs-algorithm-design-coin-game) | substrings | the coin taken | $\Theta(n^2)$ |
| arithmetic parenthesization (@sec-cs-algorithm-design-arithmetic-parenthesization) | substrings, min or max | the last operation | $O(n^3)$ |
| longest palindromic subsequence (@sec-cs-algorithm-design-longest-palindromic-subsequence) | substrings | whether the two ends match | $O(n^2)$ |
| optimal binary search tree (@sec-cs-algorithm-design-optimal-bst) | intervals of keys | the root | $O(n^3)$ |

Weighted interval scheduling (@sec-cs-algorithm-design-weighted-interval-scheduling) and stacking blocks (@exm-stacking-blocks) were taught alongside these, but use suffix subproblems.
