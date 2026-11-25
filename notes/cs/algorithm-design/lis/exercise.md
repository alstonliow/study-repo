::: {.problem #prob-mit6046r-5-q1 origin="external" source="mit6046r-5-q1"}
**Rectangular blocks**

Given a set of $n$ rectangular three-dimensional blocks, where block $B_i$ has length $l_i$, width $w_i$, and height $h_i$, all real numbers, find the maximum height of a tower of blocks that is as tall as possible, using any subset of the blocks, such that the tower respects the following constraints:

1. Blocks cannot be rotated: the length always refers to the east-west direction, the width is always north-south, and the height is always up-down.
2. Block $B_i$ can be stacked on top of block $B_j$ only if $l_i\le l_j$ and $w_i\le w_j$, that is, the two dimensions of the base of block $B_i$ are no greater than those of block $B_j$.
:::

::: {.problem #prob-mit6006-16-q1 origin="external" source="mit6006-16-q1"}
Speed up to $O(|A|\log|A|)$ by doing only $O(\log|A|)$ work per subproblem, via AVL tree augmentation

*Note (these notes):* This refers to the longest increasing subsequence DP of @exm-lis, which spends $O(|A|)$ work per subproblem.
:::
