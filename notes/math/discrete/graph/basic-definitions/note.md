---
title: "Graphs: Basic Definitions"
sources: [fit1058-cn-11.1, fit1058-cn-11.2, fit1058-cn-11.5]
requires: [math/discrete/graph/connectivity]
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/10-graph-theory.tex: Basic definitions; Types of graphs; Subgraphs. -->

## Basic definitions

::: {#def-graph .definition name="Graph"}

A *graph* $G=(V,E)$ consists of a set $V$ of *vertices* and a set $E$ of *edges*, each edge being an unordered pair $\{v,w\}$ of vertices.

:::

::: {#def-adjacent-neighbour-incident .definition name="Adjacent, neighbour, incident"}

$v$ and $w$ are *adjacent*, written $v\sim w$, if $\{v,w\}\in E$; otherwise $v\not\sim w$. Then each is a *neighbour* of the other, and both are *incident* with the edge $\{v,w\}$ (they are its *endpoints*). The *neighbourhood* $N(v)$ is the set of all neighbours of $v$.

:::

::: {#def-isolated-vertex-leaf .definition name="Isolated vertex, leaf"}

$v$ is *isolated* if $N(v)=\emptyset$, and a *leaf* if $|N(v)|=1$.

:::

::: {#exm-basic-definitions-1 .example}

Let $V=\{a,b,c,d,e,f,g\}$ and $E=\{\{a,b\},\{a,c\},\{b,c\},\{c,d\},\{f,g\}\}$: seven vertices and five edges. Here $a\sim b$, $a\sim c$, $b\sim c$, $c\sim d$, $f\sim g$, and every other pair is non-adjacent, e.g. $d\not\sim f$. Also $N(c)=\{a,b,d\}$.

:::

```{=latex}
\begin{center}
\begin{tikzpicture}[every node/.style={circle,draw,fill=white,inner sep=1.5pt,minimum size=6mm}]
\node (a) at (0,1.5) {$a$};
\node (b) at (0,0) {$b$};
\node (c) at (1.3,0.75) {$c$};
\node (d) at (2.6,0.75) {$d$};
\node (e) at (4.5,0.75) {$e$};
\node (f) at (6,1.5) {$f$};
\node (g) at (6,0) {$g$};
\draw (a)--(b) (a)--(c) (b)--(c) (c)--(d) (f)--(g);
\end{tikzpicture}
\end{center}
```

$e$ is isolated; $d,f,g$ are leaves; $\{a,b,c,d\}$, $\{e\}$, $\{f,g\}$ are the three components (@sec-math-discrete-graph-connectivity)

::: {.remark name="A graph is not its drawing"}

The graph is just the pair $(V,E)$. Positions of dots, lengths of lines and crossings in a picture carry no information; many different drawings show the same graph.

:::

## Types of graphs

::: {#def-simple-graph .definition name="Simple graph"}

$G$ is *simple* if it has no loops (edges $\{v,v\}$) and no multiple edges.

:::

::: {.remark name="Relaxations"}

A *multigraph* allows multiple edges; a *pseudograph* also allows loops. In a *directed graph* the edges are ordered pairs $(v,w)$ (*arcs*), e.g. for one-way streets. In a *weighted graph* each edge carries a number, such as a distance or cost.

:::

```{=latex}
\begin{center}
\begin{tikzpicture}[every node/.style={circle,draw,fill=white,inner sep=1.5pt,minimum size=6mm}, >={Stealth[length=2mm]}]
\node (v1) at (0,0) {$v_1$};
\node (v2) at (2,0.8) {$v_2$};
\node (v3) at (2,-0.8) {$v_3$};
\node (v4) at (4,0) {$v_4$};
\draw[->] (v1)--(v2);
\draw[->] (v1)--(v3);
\draw[->] (v2)--(v4);
\draw[->] (v3)--(v4);
\draw[->] (v2) to[bend left] (v3);
\draw[->] (v4) to[out=150,in=210,looseness=8] (v4);
\end{tikzpicture}
```

```{=latex}
\begin{tikzpicture}[every node/.style={circle,draw,fill=white,inner sep=1.5pt,minimum size=6mm}]
\node (w1) at (0,0) {$1$};
\node (w2) at (2,0.8) {$2$};
\node (w3) at (2,-0.8) {$3$};
\node (w4) at (4,0) {$4$};
\draw (w1)--(w2) node[midway,above left,font=\scriptsize] {$5$};
\draw (w1)--(w3) node[midway,below left,font=\scriptsize] {$2$};
\draw (w2)--(w4) node[midway,above right,font=\scriptsize] {$3$};
\draw (w3)--(w4) node[midway,below right,font=\scriptsize] {$7$};
\end{tikzpicture}
\end{center}
```

Directed graph (left, with a self-loop at $v_4$) and weighted graph (right)

::: {#def-complement .definition name="Complement"}

For a simple graph $G=(V,E)$, the *complement* is $\overline G=(V,\overline E)$, where $\overline E=\{\{v,w\}: v\neq w,\ \{v,w\}\notin E\}$.

:::

::: {#prp-basic-definitions-1 .proposition}

For a simple graph $G$ on $n$ vertices,  $|E(\overline G)| = \binom n2 - |E(G)|$.

:::

::: {.proof}

Each of the $\binom n2$ pairs of distinct vertices is an edge of exactly one of $G$ and $\overline G$.

:::

::: {#def-wheel-graph .definition name="Wheel graph"}

$W_n$ is the cycle $C_n$ (the *rim*) together with one extra vertex (the *hub*) adjacent to all $n$ rim vertices.

:::

## Subgraphs

::: {#def-subgraph .definition name="Subgraph"}

$H=(V_H,E_H)$ is a *subgraph* of $G=(V,E)$, written $H\le G$, if $V_H\subseteq V$ and $E_H\subseteq E$ (every edge of $H$ having both endpoints in $V_H$). It is a *proper* subgraph, $H<G$, if also $H\ne G$.

:::

::: {#exm-basic-definitions-1-2 .example}

For the graph $G$ of @sec-math-discrete-graph-basic-definitions, let $F=(U,D)$ with $U=\{a,b,c,e,g\}$ and $D=\{\{a,b\},\{a,c\}\}$. Then $F\le G$, and in fact $F<G$. Note that $\{b,c\}$ is left out even though $b,c\in U$.

:::

::: {#def-induced-subgraph .definition name="Induced subgraph"}

The subgraph *induced* by $S\subseteq V$, written $G[S]$, has vertex set $S$ and *all* edges of $G$ with both endpoints in $S$.

:::

```{=latex}
\begin{center}
\begin{tikzpicture}[every node/.style={circle,draw,fill=white,inner sep=1.5pt,minimum size=6mm}]
\node (p) at (0,1) {$p$};
\node (q) at (1.3,1.6) {$q$};
\node (r) at (1.3,0.4) {$r$};
\node (s) at (2.6,1) {$s$};
\draw[thick] (p)--(q) (p)--(r) (q)--(r) (q)--(s) (r)--(s);
\begin{scope}[on background layer]
\filldraw[fill=blue!10,draw=blue,rounded corners] (-0.5,0.2) rectangle (2,2.1);
\end{scope}
\end{tikzpicture}
\end{center}
```

The subgraph induced by $\{p,q,r\}$ (shaded): it includes *every* edge among them, $\{p,q\},\{p,r\},\{q,r\}$

::: {.remark name="Induced vs.\ ordinary subgraph"}

Every induced subgraph is a subgraph, but not conversely. For a subgraph $H$ we only know $E_H\subseteq E(G[V_H])$, while $H$ is induced exactly when equality holds, $H=G[V_H]$. The graph $F$ above is not induced, since it omits $\{b,c\}$.

:::
