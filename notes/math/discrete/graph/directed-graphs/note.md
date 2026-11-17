---
title: "Directed Graphs and Scheduling"
sources: [mcs-9.1, mcs-9.2, mcs-9.3, mcs-9.4, mcs-9.5]
requires: [math/discrete/graph/walks-paths-cycles, math/discrete/relations/partial-orders]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.042J, Mathematics for Computer Science (2015), Sections 9.1-9.5, in our own wording; proofs written out in steps. -->

## Directed graphs

::: {#def-digraph .definition name="Directed graph" related="def-directed-graph-of-a-relation"}

A *directed graph* (digraph) $G=(V,E)$ is a set $V$ of vertices and a set $E\subseteq V\times V$ of *directed edges*; the edge $(u,v)$, written $u\to v$, goes from its *tail* $u$ to its *head* $v$. The *out-degree* of $v$ is the number of edges with tail $v$, and the *in-degree* the number with head $v$. A *walk* is a sequence $v_0\to v_1\to\cdots\to v_k$ of edges; it is a *path* if its vertices are distinct, and *closed* if $v_k=v_0$. A closed walk of positive length whose only repeated vertex is $v_0=v_k$ is a *cycle*.

:::

A digraph is the same thing as a binary relation on $V$ (@def-binary-relation, @def-directed-graph-of-a-relation): the edges are the related pairs.

::: {#prp-digraph-degree-sum .proposition name="Degree sum in a digraph"}

In a finite digraph, $\sum_v\mathrm{indeg}(v)=\sum_v\mathrm{outdeg}(v)=|E|$.

:::

::: {.proof}

Each edge has exactly one tail and one head, so it is counted once in the sum of out-degrees and once in the sum of in-degrees.

:::

::: {#rmk-directed-graphs-walk-relation .remark name="Walk relations and matrix powers"}

Write $u\to^*v$ if there is a walk from $u$ to $v$ (of any length, including $0$), and $u\to^+v$ if there is one of positive length. As relations, $\to^+$ is the transitive closure of the edge relation and $\to^*$ is its reflexive transitive closure (@def-transitive-closure). With the adjacency matrix $A$ of the digraph ($A_{uv}=1$ if $u\to v$), the entry $(A^k)_{uv}$ counts the walks of length $k$ from $u$ to $v$; the proof of @thm-walks works unchanged for directed edges.

:::

## Directed acyclic graphs

::: {#def-dag .definition name="Directed acyclic graph"}

A digraph is *acyclic* (a DAG) if it has no cycle. In a DAG, a vertex with in-degree $0$ is a *source* (minimal), and one with out-degree $0$ is a *sink* (maximal).

:::

::: {#prp-dag-partial-order .proposition name="DAGs and strict partial orders"}

A digraph is acyclic if and only if its positive walk relation $\to^+$ is a strict partial order. In particular, a strict partial order, viewed as a digraph, is a DAG.

:::

::: {.proof}

1. $\to^+$ is always transitive: two walks of positive length can be joined.

2. If $G$ has a cycle through $u$, then $u\to^+u$, so $\to^+$ is not asymmetric (take $a=b=u$). Conversely, if $u\to^+v$ and $v\to^+u$, joining the walks gives a closed walk of positive length through $u$; a shortest closed walk of positive length is a cycle (it cannot repeat a vertex, or a shorter one could be cut out). So $G$ is acyclic exactly when $\to^+$ is asymmetric.

:::

::: {#thm-topological-sort .theorem name="Topological sort"}

Every finite DAG has a source, and its vertices can be listed $v_1,\dots,v_n$ so that every edge goes from an earlier to a later vertex (a *topological sort*).

:::

::: {.proof}

1. *A source exists.* Start anywhere and repeatedly step backwards along an edge into the current vertex. If this went on for $n$ steps, some vertex would repeat, giving a cycle. So it stops at a vertex with in-degree $0$.

2. *Sorting*, by induction on $n$. For $n=1$ there is nothing to do. For $n>1$, let $v_1$ be a source. Removing it leaves a DAG on $n-1$ vertices, which has a topological sort $v_2,\dots,v_n$ by the hypothesis. Every edge at $v_1$ goes out of $v_1$, so $v_1,v_2,\dots,v_n$ is a topological sort of $G$.

:::

## Scheduling

Think of the vertices of a finite DAG as tasks of unit duration and of an edge $u\to v$ as "$u$ must finish before $v$ starts". With unlimited processors, a *parallel schedule* assigns each task a time step so that $u\to v$ implies that $u$ is done in an earlier step.

::: {#thm-parallel-schedule .theorem name="Minimum parallel time"}

The minimum number of steps of a parallel schedule equals the maximum number of vertices on a path (a *critical path*) of the DAG.

:::

::: {.proof}

1. *Lower bound.* The tasks of a path $v_1\to\cdots\to v_k$ must run in $k$ strictly increasing steps, so every schedule takes at least $k$ steps.

2. *A schedule achieving it.* Give each task $v$ the step $h(v)$ = the maximum number of vertices on a path ending at $v$. If $u\to v$, then a longest path ending at $u$ extended by $v$ is a path ending at $v$ (it cannot revisit $v$ in a DAG), so $h(v)\ge h(u)+1$. So this is a valid schedule, and it uses $\max_vh(v)$ steps, the maximum number of vertices on a path.

:::

The tasks scheduled in the same step form an antichain (no edge between them, and indeed no path), and the tasks on a path form a chain of the partial order $\to^*$.

::: {#thm-dilworth-lemma .theorem name="Long chain or wide antichain"}

For every $t\ge1$, a partial order on $n$ elements has a chain of more than $t$ elements or an antichain of at least $n/t$ elements.

:::

::: {.proof}

1. Use the levels $h(v)$ of the proof of @thm-parallel-schedule, for the DAG of the strict order. Suppose there is no chain of more than $t$ elements. Then every path has at most $t$ vertices, so there are at most $t$ levels.

2. The $n$ elements are split among at most $t$ levels, so by the pigeonhole principle (@thm-pigeonhole) some level has at least $n/t$ elements.

3. Two elements in the same level are incomparable: if $u\prec v$, then $h(v)\ge h(u)+1$. So that level is an antichain of at least $n/t$ elements.

:::

For example, any $26$ distinct numbers contain an increasing or a decreasing subsequence of length $6$: order the positions by "$i\prec j$ if $i<j$ and $x_i<x_j$", with $t=5$.

::: {#rmk-directed-graphs-processors .remark name="Limited processors"}

With only $p$ processors, every schedule needs at least $\max(\lceil n/p\rceil,\,k)$ steps, where $k$ is the length of a critical path; greedy scheduling (run any $p$ available tasks) never needs more than $n/p+k$ steps.

:::
