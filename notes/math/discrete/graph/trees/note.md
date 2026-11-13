---
title: "Trees"
sources: [fit1058-cn-12.1, fit1058-cn-12.2]
requires: []
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/10-graph-theory.tex: Trees; Properties of trees. -->

## Trees

::: {#def-tree .definition name="Tree"}

A *tree* is a connected graph with no cycles.

:::

```{=latex}
\begin{center}
\begin{tikzpicture}[every node/.style={circle,draw,fill=white,inner sep=1.5pt,minimum size=6mm}]
\node (r) at (2,3) {};
\node (a) at (0.5,1.8) {};
\node (b) at (2,1.8) {};
\node (c) at (3.5,1.8) {};
\node (d) at (0,0.5) {};
\node (e) at (1,0.5) {};
\node (f) at (3.5,0.5) {};
\draw (r)--(a) (r)--(b) (r)--(c) (a)--(d) (a)--(e) (c)--(f);
\end{tikzpicture}
\end{center}
```

A tree

::: {.remark name="Where trees appear"}

Trees model communication networks with the fewest possible links, hierarchies (directories, class inheritance, organisation charts), decision processes, and the structure of sentences in a grammar. Many of these have a special vertex called the *root*, such as `/` in a Unix directory tree.

:::

## Properties of trees

::: {#def-minimal-connected-graph .definition name="Minimal connected graph"}

A connected graph $G$ is *minimal connected* if deleting any one of its edges disconnects it.

:::

::: {#thm-cn-thm-66 .theorem name="CN Thm 66"}

A graph $G$ is a tree if and only if it is a minimal connected graph.

:::

::: {.proof}

($\Rightarrow$) Let $G$ be a tree, and suppose, for contradiction, that some edge $e=\{v,w\}$ can be deleted without disconnecting $G$. Then there is a path from $v$ to $w$ avoiding $e$, and adding $e$ to it gives a cycle, contradicting that $G$ has no cycles.

($\Leftarrow$) Let $G$ be minimal connected, and suppose, for contradiction, that $G$ has a cycle $C$; let $e$ be an edge of $C$. Any walk that uses $e$ can go the other way around $C$ instead, so deleting $e$ leaves the graph connected. This contradicts minimality.

:::

::: {.remark name="Unique paths"}

It follows that any two vertices of a tree are joined by exactly one path: two different paths would together contain a cycle.

:::

::: {.remark name="The two extreme trees"}

Among trees on $n$ vertices, the path $P_{n-1}$ has the longest possible path (length $n-1$) and the smallest possible maximum degree ($2$). The star $K_{1,n-1}$ has the shortest paths (length at most $2$) and the largest possible maximum degree ($n-1$).

:::

```{=latex}
\begin{center}
\begin{tikzpicture}[every node/.style={circle,draw,fill=white,inner sep=1.5pt,minimum size=6mm}]
\node (p1) at (0,0) {};
\node (p2) at (1,0) {};
\node (p3) at (2,0) {};
\node (p4) at (3,0) {};
\node (p5) at (4,0) {};
\draw (p1)--(p2)--(p3)--(p4)--(p5);
\end{tikzpicture}
\qquad
\begin{tikzpicture}[every node/.style={circle,draw,fill=white,inner sep=1.5pt,minimum size=6mm}]
\node (s0) at (0,0) {};
\node (s1) at (-1.3,1) {};
\node (s2) at (-0.6,1.3) {};
\node (s3) at (0.6,1.3) {};
\node (s4) at (1.3,1) {};
\draw (s0)--(s1) (s0)--(s2) (s0)--(s3) (s0)--(s4);
\end{tikzpicture}
\end{center}
```

$P_4$ (left) and $K_{1,4}$ (right): the two extreme trees on $5$ vertices

::: {#thm-cn-thm-67 .theorem name="CN Thm 67"}

Every tree with at least two vertices has a leaf.

:::

::: {.proof}

Take a longest path $v_0,\dots,v_k$ in the tree; $k\ge1$ since there is at least one edge. Any neighbour of $v_k$ other than $v_{k-1}$ is either on the path, giving a cycle, or off it, giving a longer path. Neither is possible, so $\deg(v_k)=1$.

:::

::: {#thm-cn-thm-68 .theorem name="CN Thm 68"}

For every $n\in\mathbb{N}$, every tree on $n$ vertices has $n-1$ edges.

:::

::: {.proof}

We use induction on $n$.

**Base case** ($n=1$): The only tree on one vertex has $0=1-1$ edges.

**Inductive step**: Let $k\ge1$ and assume every tree on $k$ vertices has $k-1$ edges. Let $T$ be a tree on $k+1$ vertices. By CN Thm 67, $T$ has a leaf $\ell$. Deleting $\ell$ and its one edge gives a graph $S$ that is still connected (no path between other vertices passes through a leaf) and still has no cycles, so $S$ is a tree on $k$ vertices. By the inductive hypothesis $S$ has $k-1$ edges, so $T$ has $(k-1)+1=k$ edges.

By the Principle of Mathematical Induction, the claim holds for all $n$.

:::

::: {.remark name="Using the edge count"}

So a connected graph on $n$ vertices has at least $n-1$ edges, and has exactly $n-1$ if and only if it is a tree.

:::
