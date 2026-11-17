---
title: "Graph Colouring"
sources: [mcs-11.7, mcs-12.6]
requires: [math/discrete/graph/planarity, math/discrete/graph/bipartite-graphs]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.042J, Mathematics for Computer Science (2015), Sections 11.7 and 12.6, in our own wording; proofs written out in steps. -->

::: {#def-chromatic-number .definition name="Colouring, chromatic number"}

A *$k$-colouring* of a graph $G$ is a function $c:V\to\{1,\dots,k\}$ with $c(u)\ne c(v)$ for every edge $\{u,v\}$. The *chromatic number* $\chi(G)$ is the least $k$ for which a $k$-colouring exists.

:::

Colourings model conflicts: if vertices are exams and edges join exams taken by a common student, a $k$-colouring is a timetable with $k$ slots and no clashes.

::: {#exm-chromatic-numbers .example name="Some chromatic numbers"}

1. $\chi(K_n)=n$: all vertices are adjacent, so all colours must differ.

2. A graph with at least one edge has $\chi(G)=2$ exactly when it is bipartite (@def-colouring, @sec-math-discrete-graph-bipartite-graphs). So $\chi(C_n)=2$ for even $n$.

3. For odd $n\ge3$, $\chi(C_n)=3$: an odd cycle is not bipartite, and colouring the vertices $1,2,1,2,\dots,1,2,3$ around the cycle works.

:::

::: {#thm-greedy-colouring .theorem name="Greedy colouring"}

If every vertex of $G$ has degree at most $k$, then $\chi(G)\le k+1$.

:::

::: {.proof}

1. List the vertices $v_1,\dots,v_n$ in any order, and colour them one by one, giving $v_i$ the smallest colour in $\{1,\dots,k+1\}$ not used by its already coloured neighbours.

2. $v_i$ has at most $k$ neighbours, so at most $k$ colours are forbidden and one of the $k+1$ colours is free. Every edge joins a vertex to an earlier one with a different colour, so the result is a colouring.

:::

The bound is reached by complete graphs and odd cycles; Brooks' theorem says these are the only connected graphs that need $k+1$ colours.

## Colouring planar graphs

::: {#lem-planar-low-degree .lemma name="Planar graphs have a vertex of small degree"}

Every planar graph has a vertex of degree at most $5$.

:::

::: {.proof}

1. Graphs with at most $2$ vertices have all degrees at most $1$. Let $G$ have $v\ge3$ vertices and $e$ edges. By @cor-cn-cor-72, $e\le3v-6$.

2. By the handshaking lemma (@thm-handshake), the degrees sum to $2e\le6v-12<6v$, so the average degree is less than $6$, and some vertex has degree at most $5$.

:::

::: {#thm-six-colour .theorem name="Six colour theorem"}

Every planar graph has a $6$-colouring.

:::

::: {.proof}

Induction on the number $v$ of vertices. A graph with one vertex is $1$-colourable. For $v>1$, take a vertex $x$ of degree at most $5$ (@lem-planar-low-degree). Deleting $x$ leaves a planar graph, which has a $6$-colouring by the hypothesis. The at most $5$ neighbours of $x$ use at most $5$ colours, so a sixth is free for $x$.

:::

With more care (looking at two neighbours of a degree-$5$ vertex and swapping colours along a two-coloured path) the same induction gives five colours. That four colours always suffice is the four colour theorem (@thm-four-colour-theorem-extra), whose proof needs a computer check of many cases.
