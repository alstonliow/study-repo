---
title: "Euler tours and Hamiltonian cycles"
sources: [fit1058-cn-11.11]
requires: [math/discrete/graph/degree, math/discrete/graph/walks-paths-cycles]
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

::: {.remark name="Königsberg"}

The four land masses of Königsberg are vertices and its seven bridges are edges. Every vertex has odd degree, so by the theorem there is no walk crossing every bridge exactly once and returning home, settling the old puzzle.

:::

```{=latex}
\begin{center}
\begin{tikzpicture}[every node/.style={circle,draw,fill=white,inner sep=1.5pt,minimum size=7mm}]
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

::: {.remark name="Multigraphs"}

The theorem also holds for multigraphs, and for graphs with loops if each loop counts $2$ towards the degree of its vertex.

:::

::: {#thm-route-inspection-chinese-postman-extra .theorem name="Route inspection / Chinese postman (extra)"}

If $G$ is connected with $2k$ vertices of odd degree ($k\ge1$; this number is even by @cor-odd-degree), then pairing them up and adding $k$ new edges, one per pair (parallel edges allowed), makes every degree even. The new graph therefore has an Euler tour.

:::

::: {.remark name="Re-using the fewest edges"}

In practice the added edges stand for streets walked twice. Choosing the pairing so that the total re-walked length is as small as possible is the *route inspection problem*. Unlike TSP (@sec-math-discrete-graph-walks-paths-cycles), it can be solved efficiently.

:::

::: {#def-hamiltonian .definition name="Hamiltonian cycle"}

A cycle is *Hamiltonian* if it contains every vertex of the graph.

:::

::: {#exm-euler-and-hamilton-2 .example}

$C_n$ and $K_n$ ($n\ge3$) have Hamiltonian cycles. A path graph has none, since it has no cycle at all. $K_{2,3}$ has none: a cycle alternates between the two sides, so it uses equally many vertices from each, but $2\ne3$.

:::

::: {#thm-dirac-extra .theorem name="Dirac (extra)"}

If $G$ is simple with $n\ge3$ vertices, and $\deg(v)\ge n/2$ for every $v$, then $G$ has a Hamiltonian cycle.

:::

::: {.remark name="Sufficient, not necessary"}

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

::: {.remark name="Why TSP is hard"}

Checking every Hamiltonian cycle of $K_n$ means checking $(n-1)!/2$ cycles, which grows faster than any exponential. No efficient algorithm for TSP is known.

:::
