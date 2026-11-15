---
title: "Euler tours and Hamiltonian cycles"
sources: [fit1058-cn-11.11]
requires: [math/discrete/graph/connectivity, math/discrete/graph/degree]
status: draft
---

<!-- Migrated from 1058note notes/chapters/10-graph-theory.tex: Euler tours and Hamiltonian cycles. -->

::: {#def-euler-tour .definition name="Euler tour"}

An *Euler tour* of $G$ is a closed trail that uses every edge of $G$ exactly once. A graph with an Euler tour is *Eulerian*.

:::

::: {#exm-euler-and-hamilton-1 .example}

A postal worker who wants to walk along every street exactly once and finish where they started is looking for an Euler tour of the street graph.

:::

::: {#thm-euler-1736 .theorem name="Euler, 1736"}

A connected graph $G$ has an Euler tour if and only if every vertex has even degree.

:::

::: {.proof}

($\Rightarrow$) Follow the tour. Each time it passes through a vertex it uses two of that vertex’s edges, one to arrive and one to leave; the first and last edges at the starting vertex also pair up in this way. Every edge is used exactly once, so each degree is a sum of $2$’s, hence even.

($\Leftarrow$) Start at any vertex and keep walking along unused edges. Whenever we arrive at a vertex other than the start, we have used an odd number of its edges, and its degree is even, so an unused edge remains to leave by. Hence we can only get stuck at the start, and we obtain a closed trail $T$.

If $T$ uses every edge, we are done. Otherwise, because $G$ is connected, some vertex $u$ on $T$ has an unused edge. (Take a path from a vertex of $T$ to an endpoint of any unused edge; the first edge on it that is not in $T$ starts at a vertex of $T$.) Since $T$ uses an even number of edges at each vertex, every vertex still has an even number of unused edges. So the same walking argument, starting at $u$ and using only unused edges, gives a closed trail $U$. Splicing $U$ into $T$ at $u$ gives a longer closed trail. Repeating this, the trail grows until it uses every edge.

:::

::: {#rmk-euler-and-hamilton-1 .remark name="Königsberg"}

The four land masses of Königsberg are vertices and its seven bridges are edges. Every vertex has odd degree, so by the theorem there is no walk crossing every bridge exactly once and returning home, settling the old puzzle.

:::

::: {#fig-euler-and-hamilton-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[graph]
\node (A) at (0,1.8) {$A$};
\node (B) at (0,-1.8) {$B$};
\node (C) at (0,0) {$C$};
\node (D) at (2.8,0) {$D$};
\draw (A) to[bend left=40] (C);
\draw (A) to[bend right=40] (C);
\draw (B) to[bend left=40] (C);
\draw (B) to[bend right=40] (C);
\draw (C)--(D);
\draw (A) to[bend left=15] (D);
\draw (B) to[bend right=15] (D);
\end{tikzpicture}
\end{center}
```

Königsberg: the island $C$ has degree $5$, and $A$, $B$, $D$ have degree $3$, so no Euler tour exists

:::

::: {#rmk-euler-and-hamilton-2 .remark name="Multigraphs"}

The theorem also holds for multigraphs, and for graphs with loops if each loop counts $2$ towards the degree of its vertex.

:::

<!-- Added 2026-11-15 from CN §11.11 (own wording; the CN states it without proof). -->

::: {#thm-partition-into-trails .theorem name="Partitioning the edges into trails"}

Let $G$ be a connected graph with at least one edge, and let $k\in\mathbb{N}$. The edges of $G$ can be partitioned into at most $k$ trails (@def-trail-path-cycle) if and only if $G$ has at most $2k$ vertices of odd degree. In a partition using the fewest trails, every open trail starts and ends at vertices of odd degree.

:::

::: {.proof}

1. ($\Rightarrow$) Take a partition into at most $k$ trails. Each time a trail passes *through* a vertex it uses two of its edges, and a closed trail also pairs its first and last edges. So the only unpaired edge-ends are at the two ends of each open trail.

2. Hence a vertex has odd degree only if it is an end of some open trail. There are at most $k$ trails, with at most $2$ ends each, so at most $2k$ vertices have odd degree.

3. ($\Leftarrow$) The number of odd-degree vertices is even (@cor-odd-degree); say it is $2j \le 2k$. If $j = 0$, $G$ has an Euler tour (@thm-euler-1736), which is one trail.

4. If $j \ge 1$, pair up the odd-degree vertices and add one new edge joining each pair (parallel edges allowed). Now every degree is even and the graph is still connected, so it has an Euler tour (see the remark on multigraphs above).

5. Delete the $j$ new edges from this closed tour. The new edges have no endpoint in common, so no two of them are consecutive on the tour, and the tour falls apart into exactly $j$ nonempty trails of $G$. Together they use every edge of $G$ once, and $j \le k$.

6. Each of these trails starts and ends at an endpoint of a deleted edge, that is, at a vertex of odd degree. With $2j$ odd vertices, step 2 shows at least $j$ trails are needed, so this partition uses the fewest.

:::

::: {#thm-route-inspection-chinese-postman-extra .theorem name="Route inspection / Chinese postman (extra)"}

If $G$ is connected with $2k$ vertices of odd degree ($k\ge1$; this number is even by @cor-odd-degree), then pairing them up and adding $k$ new edges, one per pair (parallel edges allowed), makes every degree even. The new graph therefore has an Euler tour.

:::

::: {#rmk-euler-and-hamilton-3 .remark name="Re-using the fewest edges"}

In practice the added edges stand for streets walked twice. Choosing the pairing so that the total re-walked length is as small as possible is the *route inspection problem*. Unlike TSP (@sec-math-discrete-graph-walks-paths-cycles), it can be solved efficiently.

:::

::: {#def-hamiltonian .definition name="Hamiltonian cycle"}

A cycle is *Hamiltonian* if it contains every vertex of the graph.

:::

::: {#fig-euler-and-hamilton-2}

```{=latex}
\begin{tikzpicture}[dotgraph, x=1.15cm, y=1.15cm]
  \node[label={[lab, tick]below left:000}] (000) at (0,0) {};
  \node[label={[lab, tick]below right:100}] (100) at (2,0) {};
  \node[label={[lab, tick]above left:010}] (010) at (0,2) {};
  \node[label={[lab, tick]below right:110}] (110) at (2,2) {};
  \node[label={[lab, tick]above left:001}] (001) at (0.8,0.8) {};
  \node[label={[lab, tick]below right:101}] (101) at (2.8,0.8) {};
  \node[label={[lab, tick]above left:011}] (011) at (0.8,2.8) {};
  \node[label={[lab, tick]above right:111}] (111) at (2.8,2.8) {};
  \draw (000)--(100) (000)--(010) (000)--(001) (100)--(110) (100)--(101) (010)--(110)
        (010)--(011) (001)--(101) (001)--(011) (110)--(111) (101)--(111) (011)--(111);
  \draw[hl] (000)--(001)--(011)--(010)--(110)--(111)--(101)--(100)--cycle;
\end{tikzpicture}
```

A Hamiltonian cycle (highlighted) in the cube graph $Q_3$: $000,001,011,010,110,111,101,100$, then back to $000$

:::

::: {#exm-euler-and-hamilton-2 .example}

$C_n$ and $K_n$ ($n\ge3$) have Hamiltonian cycles. A path graph has none, since it has no cycle at all. $K_{2,3}$ has none: a cycle alternates between the two sides, so it uses equally many vertices from each, but $2\ne3$.

:::

::: {#thm-dirac-extra .theorem name="Dirac (extra)"}

If $G$ is simple with $n\ge3$ vertices, and $\deg(v)\ge n/2$ for every $v$, then $G$ has a Hamiltonian cycle.

:::

::: {#rmk-euler-and-hamilton-4 .remark name="Sufficient, not necessary"}

Many Hamiltonian graphs fail Dirac’s condition, e.g. $C_n$ for $n\ge5$, where every degree is $2$. The proof is beyond this unit.

:::

::: {#def-travelling-salesman-problem .definition name="Travelling Salesman Problem"}

Given a weighted graph, find a Hamiltonian cycle of minimum total weight. (E.g. visit every city in a region exactly once and return home, as cheaply as possible.)

:::

::: {#prp-euler-and-hamilton-1 .proposition}

For $n\ge3$, $K_n$ has exactly $\dfrac{(n-1)!}{2}$ Hamiltonian cycles.

:::

::: {.proof}

Fix a starting vertex. A Hamiltonian cycle is determined by the order in which the other $n-1$ vertices are visited, giving $(n-1)!$ orders. But each cycle is counted twice, once in each direction (and the two directions differ as $n\ge3$), so there are $(n-1)!/2$ cycles.

:::

::: {#rmk-euler-and-hamilton-5 .remark name="Why TSP is hard"}

Checking every Hamiltonian cycle of $K_n$ means checking $(n-1)!/2$ cycles, which grows faster than any exponential. No efficient algorithm for TSP is known.

:::
