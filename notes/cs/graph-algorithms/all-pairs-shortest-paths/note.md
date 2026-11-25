---
title: "All-Pairs Shortest Paths"
sources: [mit6006-14, mit6006r-14, mit6046-11]
requires: [cs/graph-algorithms/weighted-shortest-paths]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 14 and Recitation 14, in our own wording; proofs written out in steps. -->

::: {#def-apsp .definition name="All-pairs shortest paths"}

*All-pairs shortest paths* (APSP): given a weighted directed graph $G=(V,E)$, return $\delta(u,v)$ for all $u,v\in V$, or report that $G$ has a negative-weight cycle.

:::

The output has $|V|^2$ entries, so running a single-source algorithm from every vertex is a reasonable plan: $|V|$ runs of BFS or DAG relaxation take $O(|V|(|V|+|E|))$, $|V|$ runs of Dijkstra take $O(|V|^2\log|V|+|V|\cdot|E|)$ for non-negative weights, and $|V|$ runs of Bellman–Ford take $O(|V|^2|E|)$. Johnson's algorithm gets the Dijkstra bound for arbitrary weights, by first making all weights non-negative without changing which paths are shortest.

## The algorithms

Repeated squaring of the weight matrix (@sec-cs-graph-algorithms-shortest-paths-by-squaring) and Johnson's algorithm (@sec-cs-graph-algorithms-johnson) have their own notes; the Floyd–Warshall algorithm is a dynamic program (@thm-floyd-warshall).

| algorithm | weights | time $O(\cdot)$ |
|---|---|---|
| $\lvert V\rvert$ runs of BFS or DAG relaxation | unweighted, or a DAG | $\lvert V\rvert(\lvert V\rvert+\lvert E\rvert)$ |
| $\lvert V\rvert$ runs of Dijkstra (@thm-dijkstra) | non-negative | $\lvert V\rvert^2\log\lvert V\rvert+\lvert V\rvert\cdot\lvert E\rvert$ |
| $\lvert V\rvert$ runs of Bellman–Ford (@thm-bellman-ford) | any | $\lvert V\rvert^2\lvert E\rvert$ |
| repeated squaring (@prp-shortest-paths-by-squaring) | no negative-weight cycle | $\lvert V\rvert^3\log\lvert V\rvert$ |
| Floyd–Warshall (@thm-floyd-warshall) | no negative-weight cycle | $\lvert V\rvert^3$ |
| Johnson (@thm-johnson) | any | $\lvert V\rvert^2\log\lvert V\rvert+\lvert V\rvert\cdot\lvert E\rvert$ |
