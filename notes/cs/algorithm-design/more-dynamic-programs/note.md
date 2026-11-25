---
title: "More Dynamic Programs"
sources: [mit6006-17, mit6006r-17]
requires: [cs/algorithm-design/subproblem-design]
aliases: [cs/dynamic-programming/more-dynamic-programs]   # old ids (moved)
status: draft
---

When the natural subproblems do not carry enough information, *expanding* them with an extra parameter often helps (@sec-cs-algorithm-design-subproblem-design). Three more examples show the kinds of expansion.

## The problems

| problem | subproblems | expansion | time |
|---|---|---|---|
| single-source shortest paths (@exm-bellman-ford-dp) | vertices | number of edges, factor $\lvert V\rvert$ | $O(\lvert V\rvert(\lvert V\rvert+\lvert E\rvert))$ |
| all-pairs shortest paths, Floyd–Warshall (@sec-cs-algorithm-design-floyd-warshall) | pairs of vertices | allowed intermediate vertices | $\Theta(\lvert V\rvert^3)$ |
| arithmetic parenthesization (@sec-cs-algorithm-design-arithmetic-parenthesization) | substrings | minimum or maximum | $O(n^3)$ |
| piano fingering (@sec-cs-algorithm-design-piano-fingering) | suffixes | finger of the first note | $O(nF^2)$ |
