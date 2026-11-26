---
title: "Centroid Decomposition"
sources: []
requires: [cs/graph-algorithms/depth-first-search]
status: draft
---

<!-- Added 2026-11-26 for the CSES tree problems, in our own wording. TODO: add a source. -->

Many questions about paths in a tree ("how many paths have length $k$?") are hard to answer directly, but easy for the paths through one fixed vertex. A *centroid* splits the tree into small pieces, so that recursing on the pieces covers all paths in $O(n\log n)$ total work.

::: {#def-centroid .definition name="Centroid"}

A *centroid* of a tree with $n$ vertices is a vertex $c$ such that every connected component of the tree minus $c$ has at most $n/2$ vertices.

:::

::: {#thm-centroid .theorem name="Existence and decomposition"}

Every tree has a centroid, and it is found in $O(n)$ time. The *centroid decomposition* (choose a centroid $c$, remove it, and recurse on each component) has depth at most $\lfloor\log_2 n\rfloor+1$, and every path of the tree passes through the centroid of the smallest recursion piece that contains the whole path.

:::

::: {.proof}

1. *Existence.* Root the tree anywhere and, starting at the root, move to a child whose subtree has more than $n/2$ vertices as long as there is one. The walk ends, since subtrees shrink, at a vertex $c$ all of whose child subtrees have at most $n/2$ vertices. The component above $c$ has $n-\text{size}(c)<n/2$ vertices, because $\text{size}(c)>n/2$ (or $c$ is the root). So $c$ is a centroid.

2. *Time.* One DFS computes the subtree sizes, and the walk follows one root-to-leaf path.

3. *Depth.* Each component has at most half as many vertices as its parent piece, so after $\lfloor\log_2 n\rfloor+1$ levels components are empty.

4. *Paths.* Take a path $P$ and the smallest piece that contains $P$. The centroid of this piece is on $P$: otherwise $P$ would lie inside one component of the piece minus its centroid, contradicting minimality.

5. *Cost.* The pieces at one level are disjoint, so a computation linear in the size of each piece costs $O(n)$ per level and $O(n\log n)$ in total.

:::

::: {#exm-centroid-decomposition-1 .example name="Paths of length $k$"}

To count the paths with exactly $k$ edges, process each centroid $c$: do a DFS from $c$ in the piece and let $\operatorname{cnt}[d]$ be the number of vertices at depth $d$ among the subtrees already seen. For each vertex $v$ at depth $d$ in a new subtree add $\operatorname{cnt}[k-d]$ (with $c$ itself counted at depth $0$), then add the depths of that subtree to $\operatorname{cnt}$. Paths through $c$ are counted exactly once, since the two endpoints lie in different subtrees of $c$. Replacing $\operatorname{cnt}[k-d]$ by a prefix sum of $\operatorname{cnt}$ over $d'\in[a-d,b-d]$ counts paths with length in $[a,b]$; the array has length at most the piece size, so the cost is still linear per piece.

:::

::: {#fig-centroid-decomposition-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[graph, x=1.1cm, y=1cm]
\node (1) at (0,1) {1}; \node (2) at (1.2,1) {2}; \node (3) at (2.4,1) {3};
\node (4) at (3.6,1) {4}; \node (5) at (4.8,1) {5};
\node (6) at (2.4,-0.3) {6}; \node (7) at (2.4,-1.6) {7};
\draw (1)--(2)--(3)--(4)--(5) (3)--(6)--(7);
\node[hl ball] at (3) {3};
\draw[hl] (1)--(2)--(3)--(6);
\end{tikzpicture}
\end{center}
```

@exm-centroid-decomposition-1: vertex $3$ is the centroid of this tree on $7$ vertices (components of sizes $2$, $2$ and $2$). The highlighted path $1\!-\!2\!-\!3\!-\!6$ passes through it.

:::

::: {#rmk-centroid-decomposition-1 .remark name="The centroid tree"}

The centroids, with each one attached to the centroid of the piece it was chosen in, form the *centroid tree* of height $O(\log n)$. Two vertices are joined in the original tree by a path through the lowest common ancestor of the two in the centroid tree. This is used for queries such as "nearest marked vertex" by storing, at each centroid, the best distance to a marked vertex in its piece.

:::
