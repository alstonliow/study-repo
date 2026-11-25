---
title: "Designing Subproblems"
sources: [mit6006-16, mit6006r-16]
requires: [cs/algorithm-design/recursive-algorithms]
aliases: [cs/dynamic-programming/subproblem-design]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 16 and Recitation 16, in our own wording; examples our own (checked by computation); proofs written out in steps. On 2026-11-25 the longest common subsequence, the longest increasing subsequence and the alternating coin game moved to their own notes (one problem per note, SPEC §8.6); this note is their overview. -->

The hard part of dynamic programming is choosing subproblems. Natural choices are prefixes, suffixes or substrings of a sequence, and pairs of these for several sequences. When the natural subproblems do not carry enough information, *constrain* or *expand* them.

## The problems

| problem | subproblems | technique | time |
|---|---|---|---|
| longest common subsequence (@sec-cs-algorithm-design-lcs) | pairs of suffixes $x(i,j)$ | two sequences at once | $O(\lvert A\rvert\cdot\lvert B\rvert)$ |
| longest increasing subsequence (@sec-cs-algorithm-design-lis) | suffixes starting with $A[i]$ | constraint | $O(\lvert A\rvert^2)$ |
| alternating coin game (@sec-cs-algorithm-design-coin-game) | substrings $x(i,j)$, and whose turn | expansion | $\Theta(n^2)$ |

::: {#rmk-subproblem-design-expansion .remark name="Constraint and expansion"}

If the relation lacks information to check a condition of the problem, or there is no natural smaller subproblem to recurse on, add a constraint (LIS: the subsequence starts here) or extra parameters (the coin game: whose turn). More subproblems give the relation more to work with; the usual trade-off is between the number of subproblems and the work per subproblem.

:::
