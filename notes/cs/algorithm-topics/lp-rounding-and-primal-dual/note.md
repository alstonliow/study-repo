---
title: "LP Relaxation, Rounding and the Primal–Dual Method"
sources: [mit6854-16]
requires: [cs/algorithm-topics/approximation-algorithms, math/combinatorial-optimization/polyhedra/lp-duality]
status: draft
---

<!-- Added 2026-11-26 from MIT 6.854J (Fall 2008, Goemans), Lecture 16 (Sections 3-4), in our own wording; the example is our own (checked by computation); proofs written out in steps. -->

Most approximation guarantees compare the algorithm's solution not with the unknown optimum but with a *lower bound* on it (for minimisation), usually the value of a relaxation. A linear programming relaxation can be used in two ways: solve it and round the fractional solution, or never solve it and only build a dual solution alongside the primal one. Weighted vertex cover shows both.

## Relaxations and the integrality gap

::: {#def-lp-relaxation .definition name="Relaxation, integrality gap"}

A *relaxation* of $\min\{f(x):x\in S\}$ is a problem $\min\{g(x):x\in P\}$ with $P\supseteq S$ and $g\le f$ on $S$; its value is a lower bound on the optimum. For an integer program $\min\{c^{\mathsf T}x:Ax\ge b,\ x\in\{0,1\}^n\}$ the *LP relaxation* replaces $x\in\{0,1\}^n$ by $0\le x\le1$. Over a class of instances $I$, the *integrality gap* is
$$\sup_I\frac{\mathrm{OPT}(I)}{\mathrm{LP}(I)}.$$

:::

If an algorithm always returns a solution of cost at most $\alpha\cdot\mathrm{LP}$, it is an $\alpha$-approximation. Conversely, no such proof can give $\alpha$ below the integrality gap, since $\mathrm{OPT}\le\alpha\,\mathrm{LP}$ must hold on every instance.

The *weighted vertex cover* problem asks, for a graph $G=(V,E)$ with costs $c_v\ge0$, for a set $C$ meeting every edge with least cost $c(C)$. Its LP relaxation is
$$\mathrm{LP}=\min\Big\{\sum_vc_vx_v:x_u+x_v\ge1\ \ \forall uv\in E,\ x\ge0\Big\}$$
(the bounds $x_v\le1$ can be dropped: lowering a value above $1$ to $1$ keeps feasibility and lowers the cost).

::: {#prp-vertex-cover-gap .proposition name="Integrality gap of vertex cover"}

The integrality gap of this relaxation is $2$ over all graphs.

:::

::: {.proof}

1. *At least $2$.* In the complete graph $K_n$ with unit costs, a cover must contain all but one vertex, $\mathrm{OPT}=n-1$, while $x\equiv\tfrac12$ is feasible with value $n/2$. The ratio $2(n-1)/n$ tends to $2$.

2. *At most $2$.* @thm-vertex-cover-lp-rounding below finds a cover of cost at most $2\,\mathrm{LP}$.

:::

::: {#fig-lp-rounding-and-primal-dual-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (r1) at (0,1.4) {$\tfrac12$};
\node[small vertex] (r2) at (-1,0) {$\tfrac12$};
\node[small vertex] (r3) at (1,0) {$\tfrac12$};
\draw[emph] (r1)--(r2)--(r3)--(r1);
\node[lab] at (0,-0.6) {$\mathrm{LP}=\tfrac32$, $\mathrm{OPT}=2$};
\end{tikzpicture}
\end{center}
```

On a triangle with unit costs the LP puts $\tfrac12$ on every vertex (value $\tfrac32$), while every cover needs two vertices: the ratio $\tfrac43$; on $K_n$ it approaches $2$.

:::

## Rounding

::: {#thm-vertex-cover-lp-rounding .theorem name="Rounding the vertex cover LP" related="thm-vertex-cover-2-approx"}

Let $x^*$ be an optimal solution of the relaxation and $C=\{v:x^*_v\ge\tfrac12\}$. Then $C$ is a vertex cover with $c(C)\le2\,\mathrm{LP}\le2\,\mathrm{OPT}$.

:::

::: {.proof}

1. For an edge $uv$, $x^*_u+x^*_v\ge1$, so one of them is at least $\tfrac12$ and lies in $C$.

2. $c(C)=\sum_{v\in C}c_v\le\sum_{v\in C}2c_vx^*_v\le2\sum_vc_vx^*_v=2\,\mathrm{LP}$.

:::

## The primal–dual method

The dual of the relaxation puts a variable $y_e\ge0$ on every edge:
$$\max\Big\{\sum_ey_e:\sum_{e\ni v}y_e\le c_v\ \ \forall v\in V,\ y\ge0\Big\}.$$
By weak duality (@thm-lp-weak-duality) every feasible $y$ has $\sum_ey_e\le\mathrm{LP}\le\mathrm{OPT}$. The primal–dual method keeps a feasible dual solution and an infeasible integral primal one, raises dual variables until some dual constraint becomes tight, and adds the corresponding primal element; it stops when the primal is feasible.

::: {#def-vertex-cover-primal-dual .definition name="Primal–dual vertex cover"}

Start with $y=0$, $C=\varnothing$. While some edge $uv$ is not covered by $C$, raise $y_{uv}$ until $\sum_{e\ni u}y_e=c_u$ or $\sum_{e\ni v}y_e=c_v$, and add the vertex (or vertices) that became tight to $C$.

:::

```{=latex}
\begin{algorithm}
\caption{Primal--dual vertex cover}
\begin{algorithmic}
\INPUT graph $G=(V,E)$, costs $c_v\ge0$
\OUTPUT vertex cover $C$ with $c(C)\le2\,\mathrm{OPT}$
\STATE $y_e\gets0$ for all $e$; $C\gets\varnothing$
\FORALL{edges $uv$ (in any order)}
\IF{$u\notin C$ and $v\notin C$}
\STATE $\delta\gets\min\big(c_u-\sum_{e\ni u}y_e,\ c_v-\sum_{e\ni v}y_e\big)$
\STATE $y_{uv}\gets y_{uv}+\delta$
\STATE add to $C$ every endpoint whose constraint is now tight
\ENDIF
\ENDFOR
\RETURN $C$
\end{algorithmic}
\end{algorithm}
```

::: {#thm-vertex-cover-primal-dual .theorem name="Primal–dual vertex cover is a 2-approximation"}

The algorithm returns a vertex cover $C$ with $c(C)\le2\sum_ey_e\le2\,\mathrm{OPT}$, in time $O(|V|+|E|)$.

:::

::: {.proof}

1. $y$ stays feasible: a variable is raised only until a constraint at its ends becomes tight, and an edge with a tight end is covered and never raised again.

2. Every edge is covered at the end, since an uncovered edge would still be processed.

3. Every $v\in C$ is tight: $c_v=\sum_{e\ni v}y_e$. So $c(C)=\sum_{v\in C}\sum_{e\ni v}y_e\le2\sum_ey_e$, because each edge has two ends.

4. By weak duality $\sum_ey_e\le\mathrm{OPT}$.

:::

::: {#exm-vertex-cover-primal-dual .example name="A path with costs"}

On the path $a-b-c-d$ with costs $c_a=3$, $c_b=4$, $c_c=2$, $c_d=4$, process the edges from left to right. Edge $ab$: raise $y_{ab}$ to $3$, $a$ becomes tight. Edge $bc$: $b$ has slack $4$, $c$ has $2$; raise $y_{bc}$ to $2$, $c$ becomes tight. Edge $cd$ is covered. So $C=\{a,c\}$ with cost $5$ and dual value $5$; here primal and dual are equal, so $C$ is optimal (the other minimal covers, $\{b,c\}$ and $\{b,d\}$, cost $6$ and $8$).

:::

::: {#fig-lp-rounding-and-primal-dual-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex, fill=accentLight, draw=accent] (va) at (0.0,0) {$a$};
\node[lab, tick] at (0.0,-0.55) {$c=3$};
\node[small vertex] (vb) at (1.8,0) {$b$};
\node[lab, tick] at (1.8,-0.55) {$c=4$};
\node[small vertex, fill=accentLight, draw=accent] (vc) at (3.6,0) {$c$};
\node[lab, tick] at (3.6,-0.55) {$c=2$};
\node[small vertex] (vd) at (5.4,0) {$d$};
\node[lab, tick] at (5.4,-0.55) {$c=4$};
\draw[emph] (va) -- node[edge label] {$y=3$} (vb);
\draw[emph] (vb) -- node[edge label] {$y=2$} (vc);
\draw[emph] (vc) -- node[edge label] {$y=0$} (vd);
\end{tikzpicture}
\end{center}
```

Primal–dual on the path: raising $y_{ab}$ to $3$ makes $a$ tight, raising $y_{bc}$ to $2$ makes $c$ tight; the cover $\{a,c\}$ (highlighted) costs $5=\sum y$.

:::

The primal–dual method never solves an LP, so it is usually faster and combinatorial; the LP only appears in the analysis. The same pattern gives the $3$-approximation for facility location in @def-facility-location-primal-dual.
