---
title: "Minimum Spanning Trees"
sources: [mit6046-12]
requires: [math/discrete/graph/forests-and-spanning-trees]
aliases: [cs/graph-optimization/minimum-spanning-trees]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 12, in our own wording; proofs written out in steps. The definition is @def-minimum-spanning-tree. On 2026-11-25 the algorithms moved to their own notes (one algorithm per note, SPEC §8.6); this note is their overview. -->

Let $G=(V,E)$ be a connected undirected graph with edge weights $w$. A *minimum spanning tree* (MST) is a spanning tree (@def-spanning-tree) of least total weight (@def-minimum-spanning-tree). Both classical algorithms are greedy, and both are justified by one property of cuts.

::: {#def-cut-respect .definition name="Cut, crossing edge"}

A *cut* $(S,V\setminus S)$ is a split of the vertices into two non-empty parts. An edge *crosses* the cut if it has one end in each part. A cut *respects* a set $A$ of edges if no edge of $A$ crosses it.

:::

::: {#thm-cut-property .theorem name="Cut property"}

Let $A$ be a set of edges contained in some MST, let $(S,V\setminus S)$ be a cut that respects $A$, and let $e$ be a lightest edge crossing the cut. Then $A\cup\{e\}$ is contained in some MST.

:::

::: {.proof}

1. Let $T$ be an MST containing $A$. If $e\in T$ we are done; otherwise add $e=\{u,v\}$ to $T$, which creates exactly one cycle (@sec-math-discrete-graph-trees).

2. The cycle crosses the cut at $e$, and since it returns to its start it crosses the cut again at some other edge $e'$ of $T$. As the cut respects $A$, $e'\notin A$.

3. $T'=T-e'+e$ is again a spanning tree (removing $e'$ breaks the only cycle), it contains $A\cup\{e\}$, and $w(T')=w(T)-w(e')+w(e)\le w(T)$ because $e$ is a lightest crossing edge.

4. So $T'$ is an MST containing $A\cup\{e\}$.

:::

## The algorithms

Kruskal's algorithm (@sec-cs-graph-algorithms-kruskal) and Prim's algorithm (@sec-cs-graph-algorithms-prim) have their own notes.

| algorithm | grows | data structure | time $O(\cdot)$ |
|---|---|---|---|
| Kruskal (@thm-kruskal) | a forest, lightest edge between two trees | union-find | $\lvert E\rvert\log\lvert V\rvert$ |
| Prim (@thm-prim) | one tree, lightest edge leaving it | binary heap | $\lvert E\rvert\log\lvert V\rvert$ |
| Prim (@thm-prim) | one tree, lightest edge leaving it | Fibonacci heap | $\lvert E\rvert+\lvert V\rvert\log\lvert V\rvert$ |

::: {#rmk-minimum-spanning-trees-greedy .remark name="Greedy choice and optimal substructure"}

The cut property is the "greedy choice" property, and contracting the chosen edge leaves a smaller MST problem ("optimal substructure"). The same structure, a *matroid*, is what makes greedy algorithms work in general. With negative weights nothing changes: only the order of the weights matters.

:::
