---
title: "Augmented Search Trees: Order Statistics and Range Trees"
sources: [mit6046-9]
requires: [cs/data-structures/two-three-trees]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 9, in our own wording; proofs written out in steps. Builds on @def-subtree-augmentation. On 2026-11-25 order-statistic trees and range trees moved to their own notes (SPEC §8.6); this note is their overview. -->

Augmentation (@def-subtree-augmentation) stores at every node a value computed from its subtree. If the value of a node is computed in $O(1)$ time from the node and its children, it can be maintained through rotations in AVL trees and splits and merges in 2-3 trees, at the cost of updating the $O(\log n)$ ancestors of each change.

Two augmented trees have their own notes: order-statistic trees (@sec-cs-data-structures-order-statistic-trees), augmented with subtree sizes, and range trees (@sec-cs-range-queries-range-trees), which answer range queries.

::: {#rmk-augmented-search-trees-finger .remark name="Finger search"}

Linking the nodes of each level of a 2-3 tree to their neighbours, and storing in each node the smallest and largest key of its subtree, allows a search that starts from a known key $y$ and finds $x$ in $O(\log|{\rm rank}(x)-{\rm rank}(y)|)$ time: walk up and sideways from $y$ until a node's key range contains $x$, then down. Searches near a recent position are then cheap.

:::
