---
title: "Vertex Covers and König's Theorem"
sources: [mit18433-1]
requires: [math/combinatorial-optimization/matching/augmenting-paths]
status: draft
---

<!-- Added 2026-11-26 from MIT 18.433 (Spring 2015), lecture notes on bipartite matching (Sections 1.1 and 1.1.1), in our own wording; example our own (checked by computation); proofs written out in steps. Hall's theorem is kept once, as @cor-cn-cor-22 with the graph form in @rmk-bipartite-graphs-hall; its derivation from König's theorem is an exercise here. -->

To prove that a matching is maximum without referring to an algorithm, we want an upper bound on the size of every matching that is attained. This is the first instance of the duality that runs through combinatorial optimisation.

::: {#def-vertex-cover-graph .definition name="Vertex cover"}

A *vertex cover* of a graph $G=(V,E)$ is a set $C\subseteq V$ such that every edge has at least one end in $C$.

:::

::: {#prp-matching-cover-weak-duality .proposition name="Weak duality for matchings"}

In any graph, $|M|\le|C|$ for every matching $M$ and every vertex cover $C$.

:::

::: {.proof}

$C$ contains an end of each edge of $M$, and these ends are distinct because the edges of $M$ are disjoint.

:::

::: {#thm-konig .theorem name="König's theorem (1931)"}

In a bipartite graph, the maximum size of a matching equals the minimum size of a vertex cover:
$$\max_M|M|=\min_C|C| .$$

:::

The proof is algorithmic: when the augmenting path algorithm (@def-bipartite-augmenting-algorithm) stops, its last search also yields a vertex cover of the same size.

::: {.proof}

1. Let $M$ be the matching at termination, with sides $A$, $B$ and the oriented graph $D$ of @prp-augmenting-path-search. Let $L$ be the set of vertices reachable in $D$ from an exposed vertex of $A$, and put
$$C=(A\setminus L)\cup(B\cap L).$$

2. *$C$ is a cover.* Otherwise some edge $ab$ has $a\in A\cap L$ and $b\in B\setminus L$. If $ab\in M$, it is directed $b\to a$; but $a$ is not exposed, so $a$ can only be reached through its matching edge, that is from $b$, forcing $b\in L$. If $ab\notin M$, it is directed $a\to b$, and again $b\in L$. Both contradict $b\notin L$.

3. *Every vertex of $C$ is matched.* A vertex of $A\setminus L$ is not exposed, because exposed vertices of $A$ are in $L$. A vertex of $B\cap L$ is not exposed, because otherwise $D$ would contain a path from an exposed vertex of $A$ to it, an augmenting path, and the algorithm would not have stopped.

4. *No matching edge joins two vertices of $C$.* If $ab\in M$ with $a\in A\setminus L$ and $b\in B\cap L$, then the arc $b\to a$ would put $a$ in $L$.

5. So the matching edges at the vertices of $C$ are distinct, and $|C|\le|M|$. With @prp-matching-cover-weak-duality, $|C|=|M|$, which proves the theorem.

:::

::: {#exm-konig-cover .example name="A matching and a cover of the same size"}

Let $A=\{1,2,3\}$, $B=\{4,5,6\}$ and $E=\{14,24,34,35,36\}$, with $M=\{14,35\}$. The only exposed vertex of $A$ is $2$. In $D$: $2\to4$ (not in $M$), $4\to1$ (in $M$), and $1$ has no other edge, so $L=\{2,4,1\}$. Then $C=(A\setminus L)\cup(B\cap L)=\{3,4\}$ covers all five edges and $|C|=|M|=2$, so $M$ is maximum.

:::

::: {#fig-konig-theorem-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (na1) at (0,1.2) {$1$};
\node[small vertex] (na2) at (0,0.6) {$2$};
\node[small vertex, fill=accentLight, draw=accent] (na3) at (0,0) {$3$};
\node[small vertex, fill=accentLight, draw=accent] (na4) at (1.6,1.2) {$4$};
\node[small vertex] (na5) at (1.6,0.6) {$5$};
\node[small vertex] (na6) at (1.6,0) {$6$};
\draw[bold] (na1) -- (na4);
\draw[faint] (na2) -- (na4);
\draw[faint] (na3) -- (na4);
\draw[bold] (na3) -- (na5);
\draw[faint] (na3) -- (na6);
\end{tikzpicture}
\end{center}
```

The example: the matching $\{14,35\}$ (thick) and the vertex cover $\{3,4\}$ (highlighted) have the same size, so both are optimal.

:::

König's theorem fails for general graphs: in a triangle a maximum matching has one edge but every vertex cover has two vertices. The right min-max relation for general graphs is the Tutte–Berge formula (@sec-math-combinatorial-optimization-matching-tutte-berge-formula).

::: {#rmk-konig-theorem-hall .remark name="Hall's theorem from König's theorem"}

Hall's theorem (@cor-cn-cor-22, in graph form in @sec-math-discrete-graph-bipartite-graphs) says that a bipartite graph has a matching covering $A$ if and only if $|N(S)|\ge|S|$ for every $S\subseteq A$. Necessity is clear; sufficiency follows from König's theorem: a vertex cover $C$ must contain $N(A\setminus C)$, which gives $|C|\ge|A\setminus C|+|A\cap C|=|A|$ under Hall's condition (an exercise below). König's theorem also follows from max-flow min-cut (@thm-max-flow-min-cut) applied to the network of @thm-matching-by-flow, and from total unimodularity (@thm-bipartite-incidence-tu).

:::
