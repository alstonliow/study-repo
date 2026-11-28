---
title: "Planar Point Location by Persistence"
sources: [mit6851-3]
requires: [cs/data-structure-models/persistent-data-structures, cs/computational-geometry/sweep-line]
status: draft
---

<!-- Added 2026-11-27 from MIT 6.851 (Spring 2012), Lecture 3, in our own wording; proofs written out in steps. -->

Given a planar subdivision (a map without crossings), *planar point location* asks, for a query point $(x,y)$, in which face it lies. It reduces to *vertical ray shooting*: which map segment lies directly above $(x,y)$? Precompute, for each segment, the face below it.

::: {#def-vertical-ray-shooting .definition name="Vertical ray shooting"}

Given $n$ non-crossing segments in the plane (they may touch at endpoints), preprocess them so that for a query point $q=(x,y)$ the first segment hit by the vertical ray upward from $q$ is returned.

:::

::: {#thm-ray-shooting-persistent .theorem name="Ray shooting by a persistent search tree"}

Vertical ray shooting among $n$ non-crossing segments can be answered in $O(\log n)$ time per query with $O(n)$ space and $O(n\log n)$ preprocessing time.

:::

::: {.proof}

1. *Sweep.* Sweep a vertical line from left to right. At any position it meets the segments in a total order from bottom to top. Because the segments do not cross, two segments never change their relative order while both are met; so the order changes only when a left endpoint inserts a segment or a right endpoint removes one.

2. *Tree.* Keep the current segments in a balanced search tree ordered from bottom to top (a comparison of two segments at the sweep position is an $O(1)$ test). A segment is inserted at its left endpoint and deleted at its right endpoint: $2n$ updates in $O(n\log n)$ time after sorting the endpoints.

3. *Persistence.* Make the tree partially persistent (@thm-partial-persistence): the update costs and space grow only by $O(1)$ amortised each, giving $O(n)$ extra space, and every version remains searchable. Keep the versions indexed by the $x$-coordinate of the event, in a sorted array.

4. *Query.* To shoot a ray from $(x,y)$, binary search for the version current at $x$, then search that version for the successor of $y$ among the segments (a comparison of $y$ with a segment at position $x$). Both searches take $O(\log n)$ time.

:::

::: {#rmk-planar-point-location-1 .remark name="Related facts"}

*Line sweep* reduces a $d$-dimensional problem to a $(d-1)$-dimensional one that changes over "time", so a persistent or retroactive structure for the lower dimension solves the higher one. The same sweep, with the extra event "two adjacent segments cross" and the earliest crossing of each segment with its successor maintained in the tree, reports all $k$ intersections of $n$ segments in $O(n\log n+k)$ time. For horizontal segments only, a fully retroactive successor structure gives *dynamic* ray shooting with $O(\log n)$ queries. Open in the lecture: $O(\log n)$ dynamic ray shooting for a general planar graph, and $O(\log n)$ static ray shooting for rays that are not vertical.

:::
