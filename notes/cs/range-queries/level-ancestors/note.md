---
title: "Level Ancestors"
sources: [mit6851-15]
requires: [cs/range-queries/lowest-common-ancestor]
aliases: [cs/advanced-data-structures/level-ancestors]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-26 from MIT 6.851 (Spring 2012), Lecture 15, in our own wording; proofs written out in steps. The tree of the example and the figure are our own. -->

The level-ancestor problem asks for the $k$-th ancestor of a vertex. Binary lifting (@thm-binary-lifting) answers it in $O(\log n)$; a second structure, the ladder decomposition of long paths, combines with it to give $O(1)$ queries.

::: {#def-level-ancestor .definition name="Level ancestor query"}

For a rooted tree $T$, a vertex $v$ and $0\le k\le d(v)$ (the depth of $v$), $\operatorname{la}(v,k)$ is the ancestor of $v$ that is $k$ edges above it. Preprocessing costs $g(n)$ and a query $f(n)$; we write the pair as $\langle g,f\rangle$.

:::

Three simple structures, each stored in $O(n)$ or more words, give $\langle n^2,1\rangle$ (a table of all answers, filled level by level), $\langle n\log n,\log n\rangle$ (jump pointers $=$ binary lifting) and the ladders below.

::: {#def-long-path-decomposition .definition name="Long-path decomposition and ladders"}

Let $h(v)$ be the number of vertices on a longest downward path from $v$ (a leaf has $h=1$). The *long-path decomposition* splits the tree into vertex-disjoint downward paths: from each path top, continue to a child $c$ with the largest $h(c)$ until a leaf; every other child starts a new path. A path with $\ell$ vertices ($\ell=h$ of its top) is stored in an array together with up to $\ell$ further ancestors of its top (fewer if the root comes first); this array is its *ladder*. Each vertex stores a pointer to the position of the vertex in its path's ladder.

:::

::: {#fig-level-ancestors-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[level distance=0.95cm, every node/.style={small vertex},
  level 1/.style={sibling distance=2.6cm}, level 2/.style={sibling distance=1.3cm}]
\node (r) {$1$}
  child {node[fill=accentLight] (a) {$2$}
    child {node[fill=accentLight] (b) {$4$} child {node[fill=accentLight] (c) {$6$} child {node[fill=accentLight] (d) {$7$}}}}
    child {node (e) {$5$}}}
  child {node (f) {$3$} child {node (g) {$8$}}};
\draw[hl] (r)--(a); \draw[hl] (a)--(b); \draw[hl] (b)--(c); \draw[hl] (c)--(d);
\draw[hl] (f)--(g);
\end{tikzpicture}
\end{center}
```

Long-path decomposition of an eight-vertex tree: the path $1,2,4,6,7$ (five vertices; shaded), the path $3,8$ and the single vertex $5$. The ladder of $3,8$ adds $1$ above $3$; the ladder of $\{5\}$ adds $2$.

:::

::: {#prp-ladder-size .proposition name="Ladders are small"}

The ladders together hold at most $2n$ vertices, and they can be built in $O(n)$ time.

:::

::: {.proof}

1. A path with $\ell$ vertices has a ladder with at most $2\ell$ vertices.

2. The paths are disjoint and cover the $n$ vertices, so $\sum\ell=n$ and the ladders hold at most $2n$ vertices.

3. Compute $h$ bottom-up in one pass, choose each vertex's heavy child by $h$, and write each path and its upward extension into an array: $O(n)$ in total.

:::

::: {#prp-ladder-climb .proposition name="A ladder climbs at least the height"}

Let $u$ lie on a long path $P$ with top $t$. Then the ladder of $P$ contains the ancestors of $u$ up to at least $h(u)$ levels above $u$, or up to the root.

:::

::: {.proof}

1. On $P$ the height decreases by one per step, so $h(t)=h(u)+(d(u)-d(t))\ge h(u)$, and $\ell=h(t)$.

2. The ladder reaches $\ell$ vertices above $t$, so it contains the ancestors of $u$ up to $(d(u)-d(t))+\ell\ge h(u)$ levels above $u$ (or up to the root, where the extension stops).

:::

::: {#thm-level-ancestor .theorem name="Jump pointer plus ladder"}

Store, for every vertex, jump pointers to its ancestors at distance $2^j$ (@def-binary-lifting) and the ladders of @def-long-path-decomposition. Then $\operatorname{la}(v,k)$ is answered in $O(1)$ time after $O(n\log n)$ preprocessing, in $O(n\log n)$ space.

:::

::: {.proof}

1. For $k=0$ return $v$. Otherwise let $2^j\le k<2^{j+1}$ and let $u$ be the ancestor of $v$ at distance $2^j$, read from the jump pointer of $v$.

2. $u$ has the descendant $v$ at distance $2^j$, so $h(u)\ge2^j+1>2^j$.

3. The target is $k-2^j<2^j<h(u)$ levels above $u$, so by @prp-ladder-climb it lies in the ladder of the path containing $u$, at a known offset from $u$'s position. One array read finishes the query.

4. Space and time are those of the jump pointers, $O(n\log n)$; the ladders add $O(n)$ by @prp-ladder-size.

:::

::: {#rmk-level-ancestors-1 .remark name="Linear space"}

Ladders alone (without jump pointers) give $\langle n,\log n\rangle$: from $v$ one climbs a ladder, and each ladder step at least doubles the height, so $O(\log n)$ ladders suffice. Dietz, and Bender and Farach-Colton, reach $\langle n,1\rangle$ by keeping jump pointers only at the leaves of a macro tree with $O(n/\log n)$ leaves, below which micro trees of size $\tfrac14\log n$ are handled by lookup tables, as in @thm-rmq-linear. The problem is not harder in practice than LCA, but the known $O(1)$ methods are different from the RMQ ones.

:::
