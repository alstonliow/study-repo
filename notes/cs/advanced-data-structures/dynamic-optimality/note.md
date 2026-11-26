---
title: "Dynamic Optimality and the Geometry of Binary Search Trees"
sources: [mit6851-5, mit6851-6]
requires: [cs/advanced-data-structures/splay-trees]
status: draft
---

<!-- Added 2026-11-26 from MIT 6.851 (Spring 2012), Lectures 5 and 6, in our own wording; proofs written out in steps. Brief version (owner scope): the lower-bound method of independent rectangles, signed greedy and the proof of the converse direction of the geometric theorem are only stated. The example was checked by computation; the figure is our own. -->

Is there a binary search tree that is within a constant factor of the best tree on *every* access sequence? This is the dynamic optimality conjecture; splay trees (@thm-access-lemma) are the main candidate. A geometric view turns the question into one about point sets.

::: {#def-bst-model .definition name="The BST model"}

Keys $1,\dots,n$ are stored in a binary search tree. In one unit of time a search pointer, which starts at the root for each access, moves to the left child, the right child or the parent, or rotates the node it is on. An algorithm serves an access sequence $x_1,\dots,x_m$ of existing keys (no insertions or deletions here): during step $t$ the pointer must visit $x_t$. The cost is the number of nodes *touched* (visited), summed over the steps, which is within a constant factor of the running time.

:::

::: {#def-access-properties .definition name="Properties of an access sequence algorithm"}

For an algorithm on a sequence $x_1,\dots,x_m$, with $x_j$ accessed after $x_i$ and $t_{i,j}$ distinct keys accessed in between, the algorithm has the

* *sequential access property* if the sequence $1,2,\dots,n$ costs $O(1)$ amortised per access;
* *dynamic finger property* if access $x_k$ costs $O(1+\log|x_k-x_{k-1}|)$ amortised;
* *static optimality* if, when key $k$ is accessed with frequency $p_k$, the cost per access is $O\bigl(\sum_kp_k\log\tfrac1{p_k}\bigr)$;
* *working-set property* if an access whose key has $t$ distinct keys accessed since its last access costs $O(\log(t+2))$ amortised;
* *unified property* if access $x_j$ costs $O\bigl(\log\min_{i<j}(|x_i-x_j|+t_{i,j}+2)\bigr)$ amortised.

The unified property implies the dynamic-finger and working-set properties, and the working-set property implies static optimality.

:::

Splay trees have the working-set property and static optimality (@thm-splay-static-optimality) and, by a long proof of Cole et al., the dynamic finger property. Whether they satisfy the unified property, or are dynamically optimal, is open.

::: {#def-dynamic-optimality .definition name="Dynamic optimality"}

Let $\mathrm{OPT}(X)$ be the cost of the cheapest BST execution on $X$, with full knowledge of $X$ in advance (offline). An *online* BST algorithm is *dynamically optimal* if its cost on every $X$ is $O(\mathrm{OPT}(X))$. It is not known whether one exists; the best known online algorithm is $O(\log\log n)$-competitive (Tango trees).

:::

::: {#def-arborally-satisfied .definition name="Arborally satisfied point set"}

Represent an access sequence by the points $(x_t,t)$ (key, time) of a grid and an execution by the set of all touched points $(y,t)$ (node $y$ touched at time $t$). A point set is *arborally satisfied* if for every two points not on a common horizontal or vertical line, the rectangle they span contains a third point of the set (inside or on its boundary).

:::

::: {#exm-dynamic-optimality-1 .example name="Accessing 3, 1, 4, 2"}

Keep the static tree with root $3$, children $1$ and $4$, and $2$ as the right child of $1$. The searches touch $\{3\}$, $\{3,1\}$, $\{3,4\}$, $\{3,1,2\}$ in turn, which gives the eight points of the figure. They form an arborally satisfied set (checked by computer).

:::

::: {#fig-dynamic-optimality-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex, fill=accentLight] at (2.7,-0.8) {};
\node[small vertex] at (2.7,-1.6) {};
\node[small vertex, fill=accentLight] at (0.9,-1.6) {};
\node[small vertex] at (2.7,-2.4) {};
\node[small vertex, fill=accentLight] at (3.6,-2.4) {};
\node[small vertex] at (2.7,-3.2) {};
\node[small vertex] at (0.9,-3.2) {};
\node[small vertex, fill=accentLight] at (1.8,-3.2) {};
\node[lab,tick] at (0.9,-0.1) {1};
\node[lab,tick] at (1.8,-0.1) {2};
\node[lab,tick] at (2.7,-0.1) {3};
\node[lab,tick] at (3.6,-0.1) {4};
\node[lab,tick] at (0.2,-0.8) {1};
\node[lab,tick] at (0.2,-1.6) {2};
\node[lab,tick] at (0.2,-2.4) {3};
\node[lab,tick] at (0.2,-3.2) {4};
\end{tikzpicture}
\end{center}
```

The touched points of @exm-dynamic-optimality-1: time runs downward and keys left to right; the accessed points are shaded. Every pair of points in general position spans a rectangle with another point in it.

:::

::: {#thm-bst-arborally .theorem name="Executions are arborally satisfied sets"}

The set of touched points of every BST execution on $x_1,\dots,x_m$ is arborally satisfied and contains the points $(x_t,t)$. Conversely every arborally satisfied superset of these points is the touched set of some BST execution. Hence $\mathrm{OPT}(X)$ is, up to a constant factor, the size of the smallest arborally satisfied superset of $\{(x_t,t)\}$.

:::

::: {.proof}

We prove the first statement.

1. Take two touched points $(x,i)$ and $(y,j)$ with $x<y$ and $i<j$ (the other orientations are symmetric). The set touched at any step is a connected subtree containing the root, and every key visited at step $t$ is touched at time $t$.

2. Let $z$ be the lowest common ancestor of $x$ and $y$ just before step $i$. It is an ancestor of $x$, so it was touched at time $i$, and $x\le z\le y$. If $z\ne x$, the point $(z,i)$ lies in the rectangle and is not a corner.

3. Let $w$ be the lowest common ancestor of $x$ and $y$ just before step $j$; it is touched at time $j$ and $x\le w\le y$. If $w\ne y$, the point $(w,j)$ is in the rectangle and not a corner (it may be $(x,j)$).

4. Remaining case $z=x$ and $w=y$: before step $i$ the key $x$ is an ancestor of $y$, before step $j$ the key $y$ is an ancestor of $x$. So at some step $k$ with $i\le k<j$ a rotation made $y$ an ancestor of $x$. A rotation changes the ancestor relation of two keys only when one is the parent of the other, so both were visited at step $k$; then $(y,k)$ is in the rectangle and is not a corner.

:::

The converse is shown by organising the tree after each step as a treap ordered by the next time a key will be touched; the touched keys always form a connected top part that can be rearranged freely. We do not prove it here.

::: {#def-greedy-future .definition name="Greedy"}

Process the rows (times) in order. In row $t$ put the point $(x_t,t)$, then add the fewest further points in this row so that all points of rows $1,\dots,t$ form an arborally satisfied set. This is an offline algorithm; it can be simulated online as a BST algorithm with constant-factor slowdown. It is conjectured to cost $O(\mathrm{OPT})$, which would settle dynamic optimality.

:::

::: {#rmk-dynamic-optimality-1 .remark name="Lower bounds and Tango trees"}

*Independent rectangles* give lower bounds: two rectangles spanned by input points are independent if neither is arborally satisfied and no corner of one lies strictly inside the other, and $\mathrm{OPT}\ge|X|+\tfrac12\cdot$(the largest independent set of rectangles). Wilber's two bounds are of this type: the first counts, for a fixed balanced tree $P$ on the keys, the alternations of an access sequence between the left and right subtree at each node; the second counts alternations seen from each point. On the bit-reversal sequence $0,4,2,6,1,5,3,7$ (and its extension) Wilber's first bound is $\Theta(n\log n)$, so every BST needs $\Omega(n\log n)$. Tango trees store the preferred paths of $P$ (preferred child = side of the last access) in auxiliary balanced trees of size $O(\log n)$ and cost the first Wilber bound times $O(\log\log n)$, hence are $O(\log\log n)$-competitive. Whether $\mathrm{OPT}=\Theta(\text{Wilber})$ is open.

:::
