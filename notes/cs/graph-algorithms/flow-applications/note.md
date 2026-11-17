---
title: "Applications of Maximum Flow: Matching and Elimination"
sources: [mit6046-14, mit6046r-7]
requires: [cs/graph-algorithms/maximum-flow, math/discrete/graph/bipartite-graphs]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 14 and Recitation 7, in our own wording; example our own (checked by computation); proofs written out in steps. -->

Many problems reduce to maximum flow: build a network whose integral flows correspond to the objects wanted, and use integrality (@cor-integral-flow).

## Bipartite matching

::: {#thm-matching-by-flow .theorem name="Maximum bipartite matching"}

Let $G$ be bipartite with parts $L$ and $R$ (@def-bipartite). Direct every edge from $L$ to $R$ with capacity $1$, add a source $s$ with an edge of capacity $1$ to each vertex of $L$, and a sink $t$ with an edge of capacity $1$ from each vertex of $R$. Then the maximum flow value equals the size of a maximum matching (@def-matching), and an integral maximum flow gives one.

:::

::: {.proof}

1. A matching $M$ gives a flow of value $|M|$: send one unit along $s\to u\to v\to t$ for each edge $\{u,v\}\in M$. Capacities hold because matched vertices are distinct.

2. Conversely, take an integral flow. Every $u\in L$ receives at most $1$ unit, so it sends a unit along at most one edge; every $v\in R$ forwards at most $1$ unit to $t$, so it receives along at most one edge. The edges carrying flow form a matching whose size is the flow value.

3. So the two maxima are equal, and the max-flow algorithm finds a maximum matching in $O(|V||E|)$ time (each augmentation adds $1$, and the value is at most $|V|$).

:::

::: {#fig-flow-applications-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (s) at (0,0) {$s$};
\node[small vertex] (t) at (6,0) {$t$};
\node[small vertex] (l0) at (2,1.2) {$u_1$};
\node[small vertex] (l1) at (2,0.0) {$u_2$};
\node[small vertex] (l2) at (2,-1.2) {$u_3$};
\node[small vertex] (r0) at (4,1.2) {$v_1$};
\node[small vertex] (r1) at (4,0.0) {$v_2$};
\node[small vertex] (r2) at (4,-1.2) {$v_3$};
\draw[->, emph] (s) -- (l0);
\draw[->, emph] (r0) -- (t);
\draw[->, emph] (s) -- (l1);
\draw[->, emph] (r1) -- (t);
\draw[->, emph] (s) -- (l2);
\draw[->, emph] (r2) -- (t);
\draw[->, faint] (l0) -- (r0);
\draw[->, hl] (l0) -- (r1);
\draw[->, hl] (l1) -- (r0);
\draw[->, faint] (l2) -- (r1);
\draw[->, hl] (l2) -- (r2);
\end{tikzpicture}
\end{center}
```

Bipartite matching as a flow problem: every edge has capacity $1$. An integral maximum flow of value $3$ uses the highlighted middle edges, which form a perfect matching.

:::

Hall's theorem (@sec-math-discrete-graph-bipartite-graphs) also follows: a minimum cut that is smaller than $|L|$ exhibits a set of vertices of $L$ with too few neighbours.

## Baseball elimination

::: {#exm-baseball-elimination .example name="Is a team eliminated?"}

In a league, team $i$ has $w_i$ wins and $g_{ij}$ games left against team $j$. Team $x$ is *eliminated* if it cannot finish with the most wins (ties allowed) however the remaining games turn out.

Assume $x$ wins all its remaining games, reaching $W=w_x+\sum_jg_{xj}$. Build a network with a node for each pair $\{i,j\}$ of other teams and a node for each other team $i$: an edge $s\to\{i,j\}$ of capacity $g_{ij}$ (the games to be played), edges $\{i,j\}\to i$ and $\{i,j\}\to j$ of capacity $\infty$ (who wins them), and an edge $i\to t$ of capacity $W-w_i$ (how many more wins $i$ may get without passing $x$). If some $W-w_i<0$, $x$ is eliminated at once.

Then $x$ is *not* eliminated exactly when the maximum flow saturates every edge out of $s$, that is, has value $\sum_{\{i,j\}}g_{ij}$. Indeed, an integral flow assigns the winner of every remaining game so that no team passes $W$. If the flow is smaller, the minimum cut names a set $R$ of teams whose wins plus games among themselves force some team of $R$ above $W$: $\frac{\sum_{i\in R}w_i+\sum_{i,j\in R}g_{ij}}{|R|}>W$.

For example, with three other teams on $70,69,68$ wins and $2$ games left between each pair of them, a team with $68$ wins and $4$ games left reaches $W=72$; the three others must share $6$ more wins among $207$, an average of $71$, so they can all stay at or below $72$ and the team is not eliminated. With $W=70$ it would be, because $\frac{207+6}{3}=71>70$.

:::

## Other uses

Edge-disjoint paths from $s$ to $t$ (all capacities $1$; the maximum number equals the minimum number of edges whose removal separates $t$ from $s$, which is Menger's theorem), assigning people to tasks with capacities, and image segmentation by minimum cuts all follow the same pattern.
