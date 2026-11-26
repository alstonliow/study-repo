---
title: "Minimum-Cost Circulations and Cycle Cancelling"
sources: [mit6854-3, mit6854-4]
requires: [cs/graph-optimization/min-cost-flow]
status: draft
---

<!-- Added 2026-11-26 from MIT 6.854J (Fall 2008, Goemans), Lecture 3 (Section 3) and Lecture 4 (Sections 1-2.1), in our own wording; the example is our own (checked by computation); proofs written out in steps. Capacities are written c and costs a, as in the other flow notes (the course writes u and c). -->

A *circulation* is a flow without source or sink. Minimum-cost circulation contains maximum flow, min-cost flow (@def-min-cost-flow) and the assignment problem as special cases. Its optimality conditions are the model for the strongly polynomial algorithm of @def-goldberg-tarjan.

## The problem

::: {#def-min-cost-circulation .definition name="Circulation, minimum-cost circulation"}

Let $G=(V,E)$ be a directed graph with capacities $c(v,w)$ and costs $a(v,w)$, both skew-symmetric in the sense that an edge $(v,w)$ comes with its reverse $(w,v)$, $c(w,v)\ge0$ (often $0$) and $a(w,v)=-a(v,w)$. A *circulation* is a function $f$ on the edges with

1. *skew symmetry:* $f(v,w)=-f(w,v)$;
2. *conservation:* $\sum_wf(v,w)=0$ for every vertex $v$;
3. *capacity:* $f(v,w)\le c(v,w)$.

Its cost is $a(f)=\sum_{f(v,w)>0}a(v,w)f(v,w)$, half of $\sum_{(v,w)}a(v,w)f(v,w)$ over all ordered pairs. The *residual capacity* is $c_f(v,w)=c(v,w)-f(v,w)$, the residual network $G_f$ has the edges $E_f=\{(v,w):c_f(v,w)>0\}$, and the cost of a cycle $\Gamma$ is $a(\Gamma)=\sum_{(v,w)\in\Gamma}a(v,w)$.

:::

An $s$–$t$ flow becomes a circulation after adding an edge $(t,s)$ of infinite capacity. With cost $-1$ on this edge and $0$ elsewhere, a minimum-cost circulation is a maximum flow; with the costs of @def-min-cost-flow on the other edges and a very negative cost on $(t,s)$, it is a min-cost max-flow.

::: {#def-reduced-cost .definition name="Potential, reduced cost"}

A *potential* is any function $p:V\to\mathbb R$. The *reduced cost* of an edge is
$$a_p(v,w)=a(v,w)+p(v)-p(w).$$

:::

::: {#prp-reduced-cost .proposition name="Reduced costs change nothing that matters"}

$a_p$ is skew-symmetric, $a_p(\Gamma)=a(\Gamma)$ for every cycle $\Gamma$, and $a_p(f)=a(f)$ for every circulation $f$.

:::

::: {.proof}

1. $a_p(w,v)=-a(v,w)+p(w)-p(v)=-a_p(v,w)$.

2. Around a cycle every vertex is entered once and left once, so the potentials cancel.

3. For a circulation, $\sum_{(v,w)}\big(p(v)-p(w)\big)f(v,w)=\sum_vp(v)\sum_wf(v,w)-\sum_wp(w)\sum_vf(v,w)$, and both inner sums are $0$ by conservation and skew symmetry.

:::

## Optimality

::: {#thm-circulation-optimality .theorem name="Optimality conditions for circulations" generalizes="lem-min-cost-flow-optimality"}

For a circulation $f$ the following are equivalent:

1. $f$ has minimum cost;
2. $G_f$ has no cycle of negative cost;
3. there is a potential $p$ with $a_p(v,w)\ge0$ for every residual edge $(v,w)\in E_f$.

:::

::: {.proof}

1. *(1 ⇒ 2).* Suppose $\Gamma$ is a negative cycle in $G_f$ and let $\varepsilon=\min_{e\in\Gamma}c_f(e)>0$. Adding $\varepsilon$ on the edges of $\Gamma$ (and $-\varepsilon$ on their reverses) gives a circulation of cost $a(f)+\varepsilon a(\Gamma)<a(f)$.

2. *(2 ⇒ 3).* Add a vertex $s$ with edges of cost $0$ to every vertex and let $p(v)$ be the least cost of a path from $s$ to $v$ in $G_f$. Without negative cycles these are finite (@thm-bellman-ford) and satisfy $p(w)\le p(v)+a(v,w)$ for $(v,w)\in E_f$, which is $a_p(v,w)\ge0$.

3. *(3 ⇒ 1).* Let $f'$ be any circulation. The difference $g=f'-f$ is a circulation, and $g(v,w)>0$ only if $f(v,w)<f'(v,w)\le c(v,w)$, that is, on residual edges of $f$. By @prp-reduced-cost,
$$a(f')-a(f)=a(g)=a_p(g)=\sum_{g(v,w)>0}a_p(v,w)\,g(v,w)\ge0.$$

:::

The potentials in (3) are the dual variables of the linear program of the problem, and (3) is complementary slackness: an edge with $a_p(v,w)>0$ is not residual, so its reverse is saturated.

## Klein's algorithm

::: {#def-cycle-cancelling .definition name="Klein's cycle-cancelling algorithm"}

Start from any circulation, for example $f=0$. While $G_f$ has a negative cycle $\Gamma$, push $\min_{e\in\Gamma}c_f(e)$ units around $\Gamma$.

:::

```{=latex}
\begin{algorithm}
\caption{Cycle cancelling (Klein)}
\begin{algorithmic}
\INPUT graph with capacities $c$ and costs $a$
\OUTPUT a minimum-cost circulation $f$
\STATE $f\gets0$
\WHILE{$G_f$ has a cycle $\Gamma$ with $a(\Gamma)<0$}
\STATE $\varepsilon\gets\min_{e\in\Gamma}c_f(e)$
\STATE push $\varepsilon$ units around $\Gamma$
\ENDWHILE
\RETURN $f$
\end{algorithmic}
\end{algorithm}
```

When it stops, $f$ is optimal by @thm-circulation-optimality. With integer capacities and costs every step lowers the cost by at least $1$, and the cost is bounded below by $-\sum|a(e)|c(e)$, so the algorithm terminates. A negative cycle can be found by Bellman–Ford in $O(nm)$. As for augmenting paths, the choice of cycle decides the running time:

1. Ford–Fulkerson (@def-ford-fulkerson) is the special case above: zero costs and an edge $(t,s)$ of cost $-1$, every negative cycle being an augmenting path closed by $(t,s)$.
2. The *maximum improvement* cycle (Weintraub) needs polynomially many iterations for rational data, but finding it is NP-hard.
3. The *minimum mean cost* cycle (Goldberg and Tarjan) can be found in polynomial time and gives a strongly polynomial algorithm (@def-goldberg-tarjan).

::: {#exm-cycle-cancelling .example name="Cancelling two cycles"}

Vertices $s,x,y,t$, edges $s\to x$ (capacity $2$, cost $1$), $s\to y$ ($2$, $3$), $x\to y$ ($1$, $1$), $x\to t$ ($1$, $4$), $y\to t$ ($2$, $1$), and the return edge $t\to s$ (capacity $3$, cost $-10$). From $f=0$:

1. The cycle $s\,x\,t\,s$ has cost $1+4-10=-5$; pushing $1$ unit saturates $x\to t$. Cost $-5$.
2. The cycle $s\,y\,t\,s$ has cost $3+1-10=-6$; pushing $2$ units saturates $s\to y$ and $y\to t$. Cost $-17$.
3. Now $t\to s$ carries $3$ units and is saturated, but the cycle $s\,x\,y\,s$, closed by the backward residual edge $y\to s$ of cost $-3$, has cost $1+1-3=-1$; pushing $1$ unit gives cost $-18$, rerouting one unit from $s\to y$ to $s\to x\to y$.
4. No negative cycle remains: the potential $p(s)=0$, $p(x)=1$, $p(y)=3$, $p(t)=5$ has $a_p\ge0$ on every residual edge. The minimum cost is $-18$, that is, $3$ units from $s$ to $t$ at cost $12$.

:::

::: {#fig-min-cost-circulation-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (s) at (0,0) {$s$};
\node[small vertex] (x) at (2,1.2) {$x$};
\node[small vertex] (y) at (2,-1.2) {$y$};
\node[small vertex] (t) at (4,0) {$t$};
\draw[->, emph] (s) -- node[edge label] {$2/2, 1$} (x);
\draw[->, emph] (s) -- node[edge label] {$1/2, 3$} (y);
\draw[->, emph] (x) -- node[edge label] {$1/1, 1$} (y);
\draw[->, emph] (x) -- node[edge label] {$1/1, 4$} (t);
\draw[->, emph] (y) -- node[edge label] {$2/2, 1$} (t);
\draw[->, hl] (t) to[out=-110, in=-70, looseness=1.4] node[edge label] {$3/3,\,-10$} (s);
\end{tikzpicture}
\end{center}
```

The optimal circulation of the example (labels: flow/capacity, cost). Three units go around through the return edge $t\to s$; the potentials $p=(0,1,3,5)$ for $(s,x,y,t)$ certify optimality.

:::
