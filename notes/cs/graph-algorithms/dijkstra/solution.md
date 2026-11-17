<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6006s20-6-q1" status="draft"}
(a) *DAG relaxation.* A topological order, breaking ties alphabetically, is $a,d,b,e,f,c$ ($b$ must follow $d$ because of the edge $(d,b)$). Relaxing the out-edges of each vertex in this order gives
$$(a,b),(a,d),(d,b),(d,e),(b,c),(b,e),(b,f),(e,f),(f,c).$$
*Dijkstra.* Vertices leave the queue in the order $a\,(0)$, $b\,(2)$, $c\,(3)$, $f\,(4)$, $e\,(5)$, $d\,(6)$, so the edges are relaxed in the order
$$(a,b),(a,d),(b,c),(b,e),(b,f),(f,c),(e,f),(d,b),(d,e).$$

(b) $\delta(a,a)=0$, $\delta(a,b)=2$, $\delta(a,c)=3$, $\delta(a,d)=6$, $\delta(a,e)=5$, $\delta(a,f)=4$.
:::

::: {.solution for="prob-mit6006s20-6-q5" status="draft"}
*State graph.* A state is a pair $(x,\gamma)$: an intersection and an amount of gas $\gamma\in\{1,\dots,g\}$ (always positive). Its edges are:

1. for each road between $x_i$ and $x_j$ of time $t$, and each $\gamma$ with $\gamma'=\gamma-\max(0,e_j-e_i)\ge1$: an edge $(x_i,\gamma)\to(x_j,\gamma')$ of weight $t$ (and the same in the other direction);
2. at each gas station $x$, for $\gamma<g$: an edge $(x,\gamma)\to(x,\gamma+1)$ of weight $t_G$ (buying one unit; buying several is a sequence of these).

Routes that keep gas positive correspond exactly to paths from $(s,g)$, with the same total time.

*Size.* There are $ng\le n^2$ states. The average degree is below $5$, so $r<5n/2$, and there are at most $2rg+ng=O(n^2)$ edges.

*Algorithm.* All weights are positive, so run Dijkstra from $(s,g)$ with a binary heap (@prp-dijkstra-time), in $O(n^2\log(n^2))=O(n^2\log n)$ time, take the state $(t,\gamma)$ with the smallest distance, and follow parent pointers to recover the route (or report that none exists if all are $\infty$).
:::
