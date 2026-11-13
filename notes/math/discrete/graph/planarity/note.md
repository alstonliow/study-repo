---
title: "Planarity"
sources: [fit1058-cn-12.5]
requires: []
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/10-graph-theory.tex: Planarity. -->

::: {#def-planar-graph .definition name="Planar graph"}

A graph is *planar* if it can be drawn in the plane with no crossings: vertices are distinct points, and edges are curves that meet only at shared endpoints. Such a drawing is a *plane graph*.

:::

::: {.remark name="Why planarity matters"}

Electrical circuits are laid out on flat circuit boards, and wires that cross can cause short circuits; maps and diagrams are easier to read without crossings.

:::

::: {#def-face .definition name="Face"}

A plane graph divides the plane into regions called *faces*: each face is a maximal set of points any two of which can be joined by a curve avoiding all vertices and edges. The unbounded region is the *outer face*, and it must be counted too.

:::

::: {.remark name="Sides of an edge"}

Walking around the boundary of every face, each edge is met exactly twice: once from each side. The two sides usually belong to different faces, but may belong to the same face (e.g. for an edge to a leaf).

:::

```{=latex}
\begin{center}
\begin{tikzpicture}[every node/.style={circle,draw,fill=white,inner sep=1.5pt,minimum size=6mm}]
\node (a) at (0,0.75) {$a$};
\node (b) at (1.3,0.3) {$b$};
\node (c) at (1.3,1.5) {$c$};
\node (d) at (1.3,-1) {$d$};
\node (e) at (2.6,0.75) {$e$};
\node (f) at (4,0.75) {$f$};
\node (g) at (5.3,1.5) {$g$};
\node (h) at (5.3,-0.3) {$h$};
\draw (a)--(c) (a)--(d) (c)--(e) (b)--(d) (b)--(e) (e)--(c) (e)--(f) (f)--(g) (f)--(h) (g)--(h);
\node[draw=none,fill=none] at (0.9,0.75) {\small $F_1$};
\node[draw=none,fill=none] at (2.9,1.1) {\small $F_2$};
\node[draw=none,fill=none] at (4.6,0.75) {\small $F_3$};
\node[draw=none,fill=none] at (2.7,-1.3) {\small $F_4$ (outer)};
\end{tikzpicture}
\end{center}
```

A plane graph with $n=8$, $m=10$, $f=4$; indeed $n-m+f=8-10+4=2$

::: {#thm-euler-s-theorem-cn-thm .theorem name="Euler's Theorem, CN Thm 71"}

Let $G$ be a connected plane graph with $n$ vertices, $m$ edges and $f$ faces. Then $n-m+f = 2$.

:::

::: {.proof}

Fix $n$; we use induction on $m$. Since $G$ is connected, $m\ge n-1$.

**Base case** ($m=n-1$): $G$ is a connected graph with $n-1$ edges, so it is a tree. A tree has no cycle to enclose a region, so $f=1$, and $n-(n-1)+1=2$.

**Inductive step**: Let $m\ge n-1$ and assume the formula for connected plane graphs with $n$ vertices and $m$ edges. Let $G$ have $n$ vertices, $m+1$ edges and $f$ faces. Since $m+1>n-1$, $G$ is not a tree, so it has a cycle; let $e$ be an edge on it. The cycle separates the plane, so the two sides of $e$ lie in different faces. Deleting $e$ keeps the graph connected and merges those two faces into one, giving $H$ with $n$ vertices, $m$ edges and $f-1$ faces. By the inductive hypothesis $n-m+(f-1)=2$, that is, $n-(m+1)+f=2$.

By the Principle of Mathematical Induction, the formula holds for all $m\ge n-1$.

:::

::: {#cor-cn-cor-72 .corollary name="CN Cor 72"}

For any simple planar graph with $n\ge3$ vertices and $m$ edges,  $m \le 3n-6$.

:::

::: {.proof}

We may assume $G$ is connected, since adding edges between components keeps it planar and only increases $m$. Take a plane drawing with $f$ faces. Since $G$ is simple with $n\ge3$, every face has at least $3$ sides, and every edge has exactly $2$ sides, so $3f\le2m$. By Euler’s Theorem, $2=n-m+f\le n-m+\frac23m=n-\frac13m$, which rearranges to $m\le3n-6$.

:::

::: {#cor-cn-cor-73 .corollary name="CN Cor 73"}

$K_5$ is nonplanar.

:::

::: {.proof}

$K_5$ has $n=5$ and $m=10$, but $3n-6=9<10$, contradicting CN Cor 72.

:::

::: {#cor-cn-cor-74 .corollary name="CN Cor 74"}

For any triangle-free simple planar graph with $n\ge3$ vertices and $m$ edges,  $m\le2n-4$.

:::

::: {.proof}

As for CN Cor 72, but now every face has at least $4$ sides, so $4f\le2m$. Then $2=n-m+f\le n-m+\frac12m$, giving $m\le2n-4$.

:::

::: {#cor-cn-cor-75 .corollary name="CN Cor 75"}

$K_{3,3}$ is nonplanar.

:::

::: {.proof}

$K_{3,3}$ is bipartite, so it has no odd cycles and in particular no triangles. It has $n=6$ and $m=9$, but $2n-4=8<9$, contradicting CN Cor 74.

:::

::: {.remark name="A crossing drawing does not prove nonplanarity"}

A graph may have drawings with crossings and still be planar. $K_4$ is planar, as the second drawing below shows; to prove a graph *non*planar, use a counting argument like the ones above.

:::

```{=latex}
\begin{center}
\begin{tikzpicture}[every node/.style={circle,draw,fill=white,inner sep=1.5pt,minimum size=6mm}]
\node (a) at (0,1.5) {};
\node (b) at (1.5,1.5) {};
\node (c) at (0,0) {};
\node (d) at (1.5,0) {};
\draw (a)--(b) (a)--(c) (a)--(d) (b)--(c) (b)--(d) (c)--(d);
\end{tikzpicture}
\qquad
\begin{tikzpicture}[every node/.style={circle,draw,fill=white,inner sep=1.5pt,minimum size=6mm}]
\node (a) at (0.75,2) {};
\node (b) at (0,0.5) {};
\node (c) at (1.5,0.5) {};
\node (d) at (0.75,1) {};
\draw (a)--(b) (a)--(c) (a)--(d) (b)--(c) (b)--(d) (c)--(d);
\end{tikzpicture}
\end{center}
```

$K_4$: a drawing with a crossing (left) and a plane drawing (right) of the same graph

::: {#thm-four-colour-theorem-extra .theorem name="Four colour theorem (extra)"}

The vertices of every planar graph can be coloured with $4$ colours so that adjacent vertices get different colours.

:::

::: {.remark name="History"}

Conjectured in 1852 and proved in 1976 by Appel and Haken. It was the first major theorem whose proof essentially needed a computer (to check about $1900$ configurations), which was controversial because no person could check it by hand.

:::
