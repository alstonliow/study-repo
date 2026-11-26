---
title: "Minimum-Cost Maximum Flow"
sources: [cs97si-8]
requires: [cs/graph-optimization/ford-fulkerson, cs/graph-algorithms/bellman-ford]
status: draft
---

<!-- Added 2026-11-26 from Stanford CS 97SI (Winter 2011-12), Lecture 8 (min-cost max-flow), in our own wording; proofs written out in steps. The example and figure are our own; values checked by computation. -->

When every edge also has a cost per unit of flow, one wants, among all maximum flows, one of least total cost. Ford–Fulkerson (@def-ford-fulkerson) still works if every augmenting path is a *cheapest* one.

::: {#def-min-cost-flow .definition name="Min-cost flow, residual costs"}

A flow network $(G,c,s,t)$ (@def-flow-network) with a cost $a(e)$ per unit on every edge $e$. The cost of a flow $f$ is $\sum_e a(e)f(e)$. In the residual network (@def-residual-network) a forward residual edge $u\to v$ costs $a(u,v)$ and a backward residual edge $v\to u$ costs $-a(u,v)$: sending flow back refunds its cost. A *min-cost max-flow* is a maximum flow of least cost.

:::

::: {#def-successive-shortest-paths .definition name="Successive shortest paths"}

Start with $f=0$. While the residual network has an $s$–$t$ path, find a cheapest one $P$ with respect to the residual costs (with Bellman–Ford, since backward edges have negative costs), push its bottleneck capacity along $P$, and repeat.

:::

```{=latex}
\begin{algorithm}
\caption{Min-cost max-flow by successive shortest paths}
\begin{algorithmic}
\INPUT Network $G$ with capacities $c$, costs $a\ge0$, source $s$, sink $t$
\OUTPUT A min-cost maximum flow $f$
\STATE $f\gets0$
\WHILE{$G_f$ has an $s$--$t$ path}
    \STATE $P\gets$ a cheapest $s$--$t$ path in $G_f$ \COMMENT{Bellman--Ford on residual costs}
    \STATE $b\gets\min_{e\in P}c_f(e)$
    \STATE push $b$ units along $P$
\ENDWHILE
\RETURN $f$
\end{algorithmic}
\end{algorithm}
```

::: {#lem-min-cost-flow-optimality .lemma name="Negative cycle optimality"}

A flow $f$ of value $v$ has least cost among the flows of value $v$ if and only if its residual network has no cycle of negative cost.

:::

::: {.proof}

1. *If there is a negative cycle*, push $\varepsilon>0$ units around it, with $\varepsilon$ at most its smallest residual capacity. Flow is conserved at every vertex, the value is unchanged, and the cost drops by $\varepsilon$ times the cycle's cost. So $f$ was not cheapest.

2. *If $f$ is not cheapest*, take a cheaper flow $f'$ of the same value. The difference $f'-f$, read as flow on residual edges (an increase on $u\to v$ uses the forward edge, a decrease uses the backward edge), is conserved at every vertex including $s$ and $t$, so it decomposes into cycles of the residual network. Its cost is $\operatorname{cost}(f')-\operatorname{cost}(f)<0$, so one of these cycles has negative cost.

:::

::: {#thm-successive-shortest-paths .theorem name="Successive shortest paths"}

If all costs $a(e)$ are non-negative and the capacities are integers, the method ends with a min-cost maximum flow. Each intermediate flow is cheapest among the flows of its value. With $F$ the maximum flow value, it takes at most $F$ rounds of Bellman–Ford, $O(F\,|V|\,|E|)$ time.

:::

::: {.proof}

1. *Start.* The zero flow has residual network $G$ itself, which has no negative cycle since $a\ge0$.

2. *Invariant: no negative residual cycle.* Suppose $G_f$ has none, and let $d$ be the cheapest-path distances from $s$ in $G_f$. For every residual edge $u\to v$, $d(v)\le d(u)+a_f(u,v)$, with equality on the edges of the cheapest path $P$. After pushing along $P$, the only new residual edges are reverses of edges of $P$, of cost $-a_f(u,v)=d(u)-d(v)$. So every residual edge of the new network satisfies $a_f(u,v)+d(u)-d(v)\ge0$, and around any cycle through vertices reachable from $s$ the terms $d(u)-d(v)$ cancel: such a cycle has non-negative cost. A cycle through a vertex not reachable from $s$ in $G_f$ has no reachable vertex at all, and the push did not touch it, so it keeps its non-negative cost.

3. *Each flow is cheapest for its value*, by @lem-min-cost-flow-optimality and step 2.

4. *Termination and maximality.* Each round raises the flow value by a positive integer, so there are at most $F$ rounds; the method stops when $G_f$ has no $s$–$t$ path, and then $f$ is a maximum flow by the max-flow min-cut theorem (@thm-max-flow-min-cut).

5. *Time.* Each round is one Bellman–Ford run, $O(|V||E|)$, plus $O(|V|)$ for the push.

:::

::: {#exm-min-cost-flow-1 .example name="Four vertices"}

Edges, written (capacity, cost): $s\to a\,(2,1)$, $s\to b\,(2,4)$, $a\to b\,(1,1)$, $a\to t\,(1,5)$, $b\to t\,(3,1)$. The method finds

1. $s\,a\,b\,t$ of cost $3$, pushing $1$;
2. $s\,b\,t$ of cost $5$, pushing $2$;
3. $s\,a\,t$ of cost $6$, pushing $1$.

The maximum flow has value $4$ and least cost $3+2\cdot5+6=19$.

:::

::: {#fig-min-cost-flow-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=2.1cm,y=1.3cm,>=Stealth]
\node[small vertex] (s) at (0,0) {$s$};
\node[small vertex] (a) at (1,1) {$a$};
\node[small vertex] (b) at (1,-1) {$b$};
\node[small vertex] (t) at (2,0) {$t$};
\draw[->,hl] (s) -- node[edge label] {$2/2,\ 1$} (a);
\draw[->,hl] (s) -- node[edge label] {$2/2,\ 4$} (b);
\draw[->,hl] (a) -- node[edge label] {$1/1,\ 1$} (b);
\draw[->,hl] (a) -- node[edge label] {$1/1,\ 5$} (t);
\draw[->,hl] (b) -- node[edge label] {$3/3,\ 1$} (t);
\end{tikzpicture}
\end{center}
```

The final flow of @exm-min-cost-flow-1; each edge shows flow/capacity and cost. Every edge is saturated, and the cost is $2+8+1+5+3=19$.

:::

::: {#rmk-min-cost-flow-1 .remark name="Faster versions and uses"}

Keeping the distances $d$ as *potentials* makes all reduced costs $a_f(u,v)+d(u)-d(v)$ non-negative (step 2 of the proof), so later rounds can use Dijkstra (@def-dijkstra) instead of Bellman–Ford. Typical contest uses: the assignment problem (bipartite matching of least total weight), choosing $k$ disjoint paths of least total length (send $k$ units), and transport problems.

:::
