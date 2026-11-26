---
title: "Bridges and Articulation Points"
sources: []
requires: [cs/graph-algorithms/depth-first-search]
status: draft
---

<!-- Added 2026-11-26 for the CSES graph problems, in our own wording. TODO: add a source. -->

Let $G$ be a connected undirected graph. An edge or vertex is *critical* if deleting it disconnects $G$. A depth-first search finds all critical edges and vertices in $O(|V|+|E|)$ time.

::: {#def-bridge .definition name="Bridge, articulation point"}

A *bridge* is an edge whose deletion disconnects the graph. An *articulation point* (cut vertex) is a vertex whose deletion, with its edges, disconnects the graph.

:::

::: {#def-low-link .definition name="Discovery time and low-link"}

Fix a depth-first search tree and let $\operatorname{tin}(v)$ be the order in which $v$ is discovered. The low-link of $v$ is

$$
\operatorname{low}(v)=\min\bigl(\{\operatorname{tin}(v)\}\cup\{\operatorname{tin}(w): vw\text{ is a back edge}\}\cup\{\operatorname{low}(c): c\text{ a child of }v\}\bigr),
$$

the earliest discovery time reachable from the subtree of $v$ by tree edges downward and at most one back edge.

:::

::: {#thm-bridges .theorem name="Bridges and articulation points by low-links"}

For a DFS tree with root $r$:

1. a tree edge $vc$ ($c$ a child of $v$) is a bridge if and only if $\operatorname{low}(c)>\operatorname{tin}(v)$;
2. a non-root vertex $v$ is an articulation point if and only if some child $c$ has $\operatorname{low}(c)\ge\operatorname{tin}(v)$;
3. the root is an articulation point if and only if it has at least two children.

Back edges are never bridges. All of this is computed in $O(|V|+|E|)$ time.

:::

::: {.proof}

1. *Non-tree edges.* In an undirected DFS every non-tree edge joins a vertex to an ancestor, so it lies on a cycle with tree edges and is not a bridge.

2. *Bridges.* Removing a tree edge $vc$ separates the subtree $T_c$ from the rest unless a back edge leaves $T_c$ to a proper ancestor of $c$, that is, to a vertex discovered no later than $v$. Such an edge exists iff $\operatorname{low}(c)\le\operatorname{tin}(v)$. (An edge to $v$ itself is a back edge only if it is not the tree edge $vc$ — parallel edges need care, so skip the parent edge by edge id, not by endpoint.) Hence $vc$ is a bridge iff $\operatorname{low}(c)>\operatorname{tin}(v)$.

3. *Non-root points.* Removing $v$ separates $T_c$ from the rest iff no back edge leaves $T_c$ to a proper ancestor of $v$, iff $\operatorname{low}(c)\ge\operatorname{tin}(v)$ (the back edge to $v$ itself does not help since $v$ is removed). If every child fails this, each $T_c$ stays connected to the part above $v$.

4. *Root.* The subtrees of different children of $r$ are joined only through $r$ (no edge joins them, since non-tree edges join ancestor and descendant). So removing $r$ leaves as many pieces as $r$ has children.

5. *Time.* Computing $\operatorname{tin}$ and $\operatorname{low}$ is one DFS in which each edge is looked at twice.

:::

::: {#exm-bridges-1 .example name="A bridge between two triangles"}

Take the triangles $\{1,2,3\}$ and $\{4,5,6\}$ joined by the edge $34$. A DFS from $1$ visits $1,2,3,4,5,6$ with discovery times $1,\dots,6$. Then $\operatorname{low}(4)=4>\operatorname{tin}(3)=3$, so $34$ is a bridge, and $3$ and $4$ are articulation points, while the other vertices are not.

:::

::: {#fig-bridges-and-articulation-points-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[graph, x=1.3cm, y=1cm]
\node (1) at (0,0.8) {1}; \node (2) at (0,-0.8) {2}; \node (3) at (1.2,0) {3};
\node (4) at (3,0) {4}; \node (5) at (4.2,0.8) {5}; \node (6) at (4.2,-0.8) {6};
\draw (1)--(2) (2)--(3) (3)--(1) (4)--(5) (5)--(6) (6)--(4);
\draw[hl] (3)--(4);
\end{tikzpicture}
\end{center}
```

@exm-bridges-1: the highlighted edge is the only bridge.

:::
