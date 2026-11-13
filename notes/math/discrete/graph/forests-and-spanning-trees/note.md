---
title: "Forests and Spanning Trees"
sources: [fit1058-cn-12.3, fit1058-cn-12.4]
requires: [math/discrete/graph/walks-paths-cycles]
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/10-graph-theory.tex: Forests; Spanning trees. -->

## Forests

::: {#def-forest .definition name="Forest"}

A *forest* is a graph with no cycles (not necessarily connected).

:::

::: {.remark name="A forest is a union of trees"}

Each component of a forest is connected and has no cycles, so it is a tree.

:::

::: {#thm-cn-thm-69 .theorem name="CN Thm 69"}

For every $n\in\mathbb{N}$, every forest with $n$ vertices and $k$ components has $n-k$ edges.

:::

::: {.proof}

Let the components be $F_1,\dots,F_k$, with $n_i$ vertices and $m_i$ edges. Each $F_i$ is a tree, so $m_i=n_i-1$ by CN Thm 68. Hence the number of edges is $\sum_i m_i = \sum_i (n_i-1) = n-k$.

:::

```{=latex}
\begin{center}
\begin{tikzpicture}[every node/.style={circle,draw,fill=white,inner sep=1.5pt,minimum size=6mm}]
\node (a) at (0,1) {}; \node (b) at (0,0) {}; \node (c) at (1,0.5) {};
\draw (a)--(c) (b)--(c);
\node (e) at (2.7,0.5) {};
\node (f) at (4,1) {}; \node (g) at (4,0) {};
\draw (f)--(g);
\end{tikzpicture}
\end{center}
```

A forest with $k=3$ components: $n=6$ vertices and $3=n-k$ edges

## Spanning trees

::: {#def-spanning-tree .definition name="Spanning tree"}

A *spanning tree* of a connected graph $G$ is a subgraph of $G$ that is a tree and contains every vertex of $G$.

:::

::: {#prp-existence .proposition name="Existence"}

Every connected graph has a spanning tree.

:::

::: {.proof}

Delete edges one at a time, each time choosing an edge whose deletion leaves the graph connected, until no such edge remains. The result is connected, contains every vertex, and is minimal connected, so it is a tree by CN Thm 66.

:::

::: {#exm-forests-and-spanning-trees-1 .example}

The graph below (the graph of @sec-math-discrete-graph-walks-paths-cycles) has $6$ vertices and $8$ edges, so a spanning tree is obtained by deleting $3$ edges. Deleting $\{a,b\}$, $\{b,c\}$, $\{b,e\}$, each time keeping the graph connected, leaves the spanning tree drawn thick. Deleting $\{a,b\}$, $\{c,d\}$, $\{b,e\}$ instead gives a different spanning tree. Every spanning tree has $6-1=5$ edges.

:::

```{=latex}
\begin{center}
\begin{tikzpicture}[every node/.style={circle,draw,fill=white,inner sep=1.5pt,minimum size=6mm}]
\node (a) at (0,1) {$a$};
\node (b) at (1.3,1.6) {$b$};
\node (c) at (0,-0.3) {$c$};
\node (d) at (1.3,-0.9) {$d$};
\node (e) at (2.8,0.5) {$e$};
\node (f) at (4.3,0.5) {$f$};
\draw[very thin, gray] (a)--(b) (b)--(c) (b)--(e);
\draw[very thick] (a)--(c) (c)--(d) (b)--(d) (d)--(e) (e)--(f);
\end{tikzpicture}
\end{center}
```

A spanning tree (thick edges)

::: {.remark name="Building up instead"}

Equivalently, start with no edges and repeatedly add any edge that does not create a cycle, until no more can be added:

:::

```{=latex}
\begin{algorithm}[H]
\SetAlgoLined
\KwIn{Connected graph $G=(V,E)$}
\KwOut{Spanning tree $F=(V,X)$}
$X\gets\emptyset$\;
\While{$\exists e\in E\setminus X$ such that $X\cup\{e\}$ has no cycle}{
    pick such an $e$\;
    $X\gets X\cup\{e\}$\;
}
\caption{Spanning tree by adding edges}
\end{algorithm}
```

::: {.proof name="Correctness"}

$F$ has no cycle by construction. If $F$ were not connected, then since $G$ is connected some edge of $G$ would join two different components of $F$; adding it creates no cycle, so the algorithm would not have stopped. Hence $F$ is a connected graph with no cycles containing every vertex, i.e. a spanning tree.

:::

::: {#def-minimum-spanning-tree .definition name="Minimum spanning tree"}

In a connected graph with a weight (cost) $w(e)$ on each edge, a *minimum spanning tree* is a spanning tree whose total weight $\sum_{e\in X}w(e)$ is as small as possible.

:::

```{=latex}
\begin{algorithm}[H]
\SetAlgoLined
\KwIn{Connected weighted graph $G=(V,E,w)$}
\KwOut{Minimum spanning tree $F=(V,X)$}
$X\gets\emptyset$\;
\While{$\exists e\in E\setminus X$ such that $X\cup\{e\}$ has no cycle}{
    $e\gets$ such an edge of minimum weight\;
    $X\gets X\cup\{e\}$\;
}
\caption{Kruskal's Greedy Algorithm}
\end{algorithm}
```

::: {#thm-cn-thm-70 .theorem name="CN Thm 70"}

For every weighted graph $G$, Kruskal’s Greedy Algorithm finds a minimum weight spanning tree of $G$.

:::

::: {.remark name="Proof idea: the exchange argument"}

CN does not prove this. The idea: suppose Kruskal’s tree $T$ is not minimum, and let $T^*$ be a minimum spanning tree sharing as many edges with $T$ as possible. Let $e$ be the first edge chosen by Kruskal that is not in $T^*$. Adding $e$ to $T^*$ creates a cycle, which contains an edge $f\notin T$. When Kruskal chose $e$, the edge $f$ was also available (adding it would not have created a cycle), so $w(e)\le w(f)$. Then $T^*-f+e$ is a spanning tree of weight at most $w(T^*)$, so it is also minimum, and it shares more edges with $T$, a contradiction.

:::

::: {.remark name="Greedy is usually not optimal"}

Repeatedly taking the biggest immediate benefit seldom gives the best overall result. For example, greedily following the shortest available edge does not, in general, find a shortest path between two vertices, and may not find a path at all. Minimum spanning trees are a striking exception.

:::
