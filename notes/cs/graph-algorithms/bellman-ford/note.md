---
title: "Bellman–Ford: Shortest Paths with Negative Weights"
sources: [mit6006-12, mit6006r-12]
requires: [cs/graph-algorithms/weighted-shortest-paths]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 12 and Recitation 12, in our own wording; proofs written out in steps. -->

Goal: in a directed graph with arbitrary integer weights, compute $\delta(s,v)$ for every $v$, including $-\infty$ for vertices reached through a negative-weight cycle, in $O(|V|\cdot|E|)$ time.

## Bounded-length shortest paths

::: {#lem-simple-shortest-paths .lemma name="Finite shortest paths can be taken simple"}

If $\delta(s,v)$ is finite, some shortest path from $s$ to $v$ repeats no vertex, and so has at most $|V|-1$ edges.

:::

::: {.proof}

1. Since $\delta(s,v)$ is finite, no walk from $s$ to $v$ passes through a vertex of a negative-weight cycle (going round it would make the weight arbitrarily small). So every closed walk contained in a walk from $s$ to $v$ has weight $\ge0$.

2. If a walk from $s$ to $v$ repeats a vertex, it contains a closed walk $C$ between the two occurrences. Cutting $C$ out gives a walk from $s$ to $v$ with fewer edges and weight at most the original, by step 1. Repeating this turns every walk from $s$ to $v$ into a path (no repeated vertex) that is no heavier.

3. So $\delta(s,v)$, the infimum over all walks, equals the minimum over the finitely many paths from $s$ to $v$, and a lightest path attains it. A path has at most $|V|$ vertices, so at most $|V|-1$ edges.

:::

::: {#def-k-edge-distance .definition name="$k$-edge distance, witness"}

The *$k$-edge distance* $\delta_k(s,v)$ is the least weight of a walk from $s$ to $v$ with at most $k$ edges ($\infty$ if there is none). A vertex $v$ with $\delta_{|V|}(s,v)<\delta_{|V|-1}(s,v)$ is a *(negative cycle) witness*.

:::

By @lem-simple-shortest-paths, $\delta(s,v)=\delta_{|V|-1}(s,v)$ whenever $\delta(s,v)>-\infty$. A witness has a walk with $|V|$ edges lighter than every walk with fewer edges, which (as shown below) is impossible unless $\delta(s,v)=-\infty$.

::: {#lem-witnesses .lemma name="Witnesses find all $-\infty$ vertices"}

1. Every witness $v$ has $\delta(s,v)=-\infty$.
2. If $\delta(s,v)=-\infty$, then $v$ is reachable from a witness.

:::

::: {.proof}

1. If $\delta(s,v)$ were finite, then $\delta_{|V|}(s,v)\ge\delta(s,v)=\delta_{|V|-1}(s,v)$, so $v$ would not be a witness. And $\delta_{|V|}(s,v)<\infty$ means $v$ is reachable, so $\delta(s,v)\ne\infty$.

2. If $\delta(s,v)=-\infty$, some walk from $s$ to $v$ passes through a negative-weight cycle $C$ reachable from $s$. It suffices to show that $C$ contains a witness. For each $x$ on $C$, let $x'$ be its predecessor on $C$, so $\sum_{x\in C}w(x',x)=w(C)<0$. Each $x$ on $C$ is reachable, so $\delta_{|V|-1}(s,x)$ is finite (a reachable vertex has a path with at most $|V|-1$ edges).

3. A walk with at most $|V|-1$ edges to $x'$, followed by the edge $(x',x)$, has at most $|V|$ edges, so $\delta_{|V|}(s,x)\le\delta_{|V|-1}(s,x')+w(x',x)$. Summing over $x\in C$ (each vertex of $C$ appears once as $x$ and once as $x'$):
   $$\sum_{x\in C}\delta_{|V|}(s,x)\le\sum_{x\in C}\delta_{|V|-1}(s,x)+w(C)<\sum_{x\in C}\delta_{|V|-1}(s,x).$$

4. So $\delta_{|V|}(s,x)<\delta_{|V|-1}(s,x)$ for at least one $x$ on $C$: a witness.

:::

## The algorithm

::: {#def-bellman-ford .definition name="Bellman–Ford by graph duplication"}

Build a DAG $G'$ with $|V|+1$ *levels*: a copy $v_k$ of every vertex $v$ for $k=0,\dots,|V|$, and for $k=1,\dots,|V|$ the edges $(v_{k-1},v_k)$ of weight $0$ for every vertex $v$ and $(u_{k-1},v_k)$ of weight $w(u,v)$ for every edge $(u,v)\in E$. Run DAG relaxation (@def-dag-relaxation) from $s_0$. Set $d(v)=\delta'(s_0,v_{|V|-1})$; then, for every witness $u$ (a vertex with $\delta'(s_0,u_{|V|})<\delta'(s_0,u_{|V|-1})$), set $d(v)=-\infty$ for every $v$ reachable from $u$ in $G$.

:::

::: {#thm-bellman-ford .theorem name="Bellman–Ford"}

1. $\delta'(s_0,v_k)=\delta_k(s,v)$ for all $v$ and $k$.
2. Bellman–Ford computes $d(v)=\delta(s,v)$ for every vertex $v$, in $O(|V|\cdot|E|)$ time.

:::

::: {.proof}

1. Every edge of $G'$ goes up one level, so $G'$ is a DAG, and a walk from $s_0$ to $v_k$ corresponds to a walk from $s$ to $v$ in $G$ with at most $k$ edges (the weight-$0$ edges are "waiting" steps), of the same weight. Conversely, every such walk in $G$ lifts to $G'$ by waiting at $s$ first. So $\delta'(s_0,v_k)=\delta_k(s,v)$.

2. By part 1, DAG relaxation (@thm-dag-relaxation) gives $\delta_{|V|-1}$ and $\delta_{|V|}$ exactly. If $\delta(s,v)>-\infty$ then $d(v)=\delta_{|V|-1}(s,v)=\delta(s,v)$ by @lem-simple-shortest-paths, and $v$ is not reachable from a witness by @lem-witnesses part 1 (a vertex reachable from a vertex with weight $-\infty$ also has weight $-\infty$). If $\delta(s,v)=-\infty$, $v$ is reachable from a witness by @lem-witnesses part 2 and is set to $-\infty$.

3. *Time.* First discard the vertices not reachable from $s$ (their $\delta$ is $\infty$), using BFS in $O(|V|+|E|)$; what remains is connected from $s$, so $|V|=O(|E|+1)$. $G'$ has $O(|V|^2)$ vertices and $O(|V|(|V|+|E|))=O(|V|\cdot|E|)$ edges, and DAG relaxation is linear in its size. Marking everything reachable from the witnesses takes one search from an extra vertex joined to all witnesses, $O(|V|+|E|)$.

:::

::: {#rmk-bellman-ford-practice .remark name="The usual implementation"}

Only two levels of $G'$ are needed at a time, so $O(|V|)$ space suffices. The traditional form keeps one estimate per vertex and relaxes every edge of $G$ in each of $|V|-1$ rounds; a further round that still lowers some estimate reveals a negative-weight cycle. Its estimates are no longer exactly the $k$-edge distances, so its proof is less direct, but it has the same $O(|V|\cdot|E|)$ time. A shortest walk from $s_0$ to $v_{|V|}$ for a witness $v$ has $|V|+1$ vertices, so it repeats a vertex of $G$, and the repeated part is a negative-weight cycle that can be returned.

:::
