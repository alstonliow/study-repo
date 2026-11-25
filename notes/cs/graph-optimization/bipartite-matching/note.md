---
title: "Maximum Bipartite Matching"
sources: [mit6046-14, mit6046r-7]
requires: [cs/graph-optimization/ford-fulkerson, math/discrete/graph/bipartite-graphs]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 14 and Recitation 7, in our own wording; example our own (checked by computation); proofs written out in steps. Split from cs/graph-optimization/flow-applications on 2026-11-25 (one algorithm per note, SPEC §8.6). -->

A maximum matching in a bipartite graph is a maximum flow in a network built from it, by integrality (@cor-integral-flow).

::: {#thm-matching-by-flow .theorem name="Maximum bipartite matching"}

Let $G$ be bipartite with parts $L$ and $R$ (@def-bipartite). Direct every edge from $L$ to $R$ with capacity $1$, add a source $s$ with an edge of capacity $1$ to each vertex of $L$, and a sink $t$ with an edge of capacity $1$ from each vertex of $R$. Then the maximum flow value equals the size of a maximum matching (@def-matching), and an integral maximum flow gives one.

:::

::: {.proof}

1. A matching $M$ gives a flow of value $|M|$: send one unit along $s\to u\to v\to t$ for each edge $\{u,v\}\in M$. Capacities hold because matched vertices are distinct.

2. Conversely, take an integral flow. Every $u\in L$ receives at most $1$ unit, so it sends a unit along at most one edge; every $v\in R$ forwards at most $1$ unit to $t$, so it receives along at most one edge. The edges carrying flow form a matching whose size is the flow value.

3. So the two maxima are equal, and the max-flow algorithm finds a maximum matching in $O(|V||E|)$ time (each augmentation adds $1$, and the value is at most $|V|$).

:::

```{=latex}
\begin{algorithm}
\caption{Maximum bipartite matching by flow}
\begin{algorithmic}
\INPUT Bipartite graph $G$ with parts $L$ and $R$
\OUTPUT A maximum matching $M$
\STATE build a network: edges $s\to u$ ($u\in L$), $u\to v$ ($\{u,v\}\in E$, $u\in L$), $v\to t$ ($v\in R$), all of capacity $1$
\STATE $f\gets$ an integral maximum flow (Ford–Fulkerson)
\RETURN $M=\{\{u,v\}:u\in L,\ v\in R,\ f(u,v)=1\}$
\end{algorithmic}
\end{algorithm}
```

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
