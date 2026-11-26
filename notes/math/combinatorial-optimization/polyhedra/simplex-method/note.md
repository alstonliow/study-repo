---
title: "The Simplex Method"
sources: [mit6854-10, mit6854-11]
requires: [math/combinatorial-optimization/polyhedra/vertices-of-polyhedra]
status: draft
---

<!-- Added 2026-11-26 from MIT 6.854J (Fall 2008, Goemans), Lecture 10 (Section 3, a sketch of the simplex method) and Lecture 11 (Section 1), in our own wording; the pivot step with reduced costs is standard material written out to make the sketch concrete; example our own (checked by computation); proofs written out in steps. -->

Throughout, $Q=\{x\in\mathbb R^n:Ax=b,\ x\ge0\}$ with $A\in\mathbb R^{m\times n}$ of rank $m$, and we minimise $c^{\mathsf T}x$ over $Q$. By @prp-vertices-are-bfs the vertices of $Q$ are its basic feasible solutions.

::: {#thm-optimal-vertex .theorem name="Some vertex is optimal"}

If $\min\{c^{\mathsf T}x:x\in Q\}$ is finite, then for every $x\in Q$ there is a vertex $x'$ of $Q$ with $c^{\mathsf T}x'\le c^{\mathsf T}x$. In particular the minimum is attained at a vertex.

:::

::: {.proof}

1. Induct on the number of positive coordinates of $x$. If the columns $A_J$, $J=\{j:x_j>0\}$, are independent, $x$ is a bfs, hence a vertex.

2. Otherwise some $y\ne0$ with $y_j=0$ for $j\notin J$ has $Ay=0$, so $A(x+\alpha y)=b$ for all $\alpha$. Replacing $y$ by $-y$ if needed, assume $c^{\mathsf T}y\le0$, and if $c^{\mathsf T}y=0$ assume some $y_j<0$.

3. If $y\ge0$ then $c^{\mathsf T}y<0$ and $x+\alpha y\in Q$ for all $\alpha\ge0$, with cost tending to $-\infty$; this contradicts finiteness. So some $y_j<0$.

4. Take $\alpha=\min_{j:y_j<0}x_j/(-y_j)>0$. Then $x+\alpha y\in Q$, its cost is at most $c^{\mathsf T}x$, and it has fewer positive coordinates. Apply induction.

5. $Q$ has finitely many vertices, so the best of them is a minimum.

:::

The simplex method walks from vertex to vertex. A basis $B$ gives $x_B=A_B^{-1}b-A_B^{-1}A_Nx_N$, so on $Ax=b$
$$c^{\mathsf T}x=c_B^{\mathsf T}A_B^{-1}b+\bar c_N^{\mathsf T}x_N,\qquad \bar c^{\mathsf T}=c^{\mathsf T}-c_B^{\mathsf T}A_B^{-1}A,$$
the *reduced costs* $\bar c$ (zero on $B$).

::: {#def-simplex-method .definition name="Simplex method"}

1. Start from a basic feasible solution $x$ with basis $B$.
2. If $\bar c\ge0$, stop: $x$ is optimal.
3. Otherwise pick an *entering* index $k\in N$ with $\bar c_k<0$ and let $d=-A_B^{-1}A_k$ (the change of $x_B$ per unit of $x_k$).
4. If $d\ge0$, stop: the program is unbounded.
5. Otherwise increase $x_k$ to $\theta=\min_{i\in B:d_i<0}x_i/(-d_i)$, let a *leaving* index $j$ attain the minimum, and set $B\gets B\setminus\{j\}\cup\{k\}$ (a *pivot*). Go to 2.

:::

```{=latex}
\begin{algorithm}
\caption{Simplex method}
\begin{algorithmic}
\INPUT $A$ of rank $m$, $b$, $c$, a feasible basis $B$
\OUTPUT an optimal basis, or ``unbounded''
\LOOP
\STATE $x_B\gets A_B^{-1}b$; $y^{\mathsf T}\gets c_B^{\mathsf T}A_B^{-1}$; $\bar c^{\mathsf T}\gets c^{\mathsf T}-y^{\mathsf T}A$
\IF{$\bar c\ge0$}
\RETURN $B$
\ENDIF
\STATE choose $k$ with $\bar c_k<0$ \COMMENT{pivoting rule}
\STATE $d\gets-A_B^{-1}A_k$
\IF{$d\ge0$}
\RETURN unbounded
\ENDIF
\STATE choose $j\in\arg\min_{i:d_i<0}x_i/(-d_i)$
\STATE $B\gets B\setminus\{j\}\cup\{k\}$
\ENDLOOP
\end{algorithmic}
\end{algorithm}
```

::: {#prp-simplex-correct .proposition name="Correctness of the stopping rules"}

If $\bar c\ge0$, the basic feasible solution $x$ is optimal and $y^{\mathsf T}=c_B^{\mathsf T}A_B^{-1}$ is an optimal solution of the dual $\max\{b^{\mathsf T}y:A^{\mathsf T}y\le c\}$. If $\bar c_k<0$ and $d\ge0$, the program is unbounded. Otherwise the pivot gives a new basic feasible solution of cost $c^{\mathsf T}x+\theta\bar c_k\le c^{\mathsf T}x$.

:::

::: {.proof}

1. $\bar c\ge0$ says $A^{\mathsf T}y\le c$, so $y$ is dual feasible, and $b^{\mathsf T}y=c_B^{\mathsf T}A_B^{-1}b=c^{\mathsf T}x$. By weak duality (@thm-weak-duality) both are optimal.

2. Moving to $x(t)$ with $x_k=t$, $x_B=A_B^{-1}b+td$ and the other non-basic coordinates $0$ keeps $Ax=b$, and changes the cost by $t\bar c_k$. If $d\ge0$, every $t\ge0$ is feasible and the cost tends to $-\infty$.

3. Otherwise $t=\theta$ is the largest feasible step, and $x_j$ becomes $0$. The column $A_k$ has a non-zero coefficient $d_j$ on $A_j$ in the basis $B$, so exchanging $j$ for $k$ keeps the columns independent, and $x(\theta)$ is the basic solution of the new basis, with cost $c^{\mathsf T}x+\theta\bar c_k$.

:::

::: {#exm-simplex-small .example name="Two pivots"}

Minimise $-x_1-x_2$ subject to $x_1+2x_2+x_3=4$, $3x_1+x_2+x_4=6$, $x\ge0$ ($x_3,x_4$ are slacks). Start from $B=\{3,4\}$, $x=(0,0,4,6)$, $\bar c=(-1,-1,0,0)$.

1. Let $x_1$ enter: $d=(-1,-3)$ on $(x_3,x_4)$, ratios $4$ and $2$, so $x_4$ leaves. Now $x=(2,0,2,0)$, cost $-2$, and $\bar c=(0,-\tfrac23,0,\tfrac13)$.
2. Let $x_2$ enter: $x_3$ leaves. Now $x=(\tfrac85,\tfrac65,0,0)$, cost $-\tfrac{14}5$, and $\bar c=(0,0,\tfrac25,\tfrac15)\ge0$: optimal, with dual solution $y=(-\tfrac25,-\tfrac15)$.

:::

::: {#fig-simplex-method-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.3]
\draw[->, faint] (-0.2,0)--(3,0) node[lab, right] {$x_1$};
\draw[->, faint] (0,-0.2)--(0,2.6) node[lab, above] {$x_2$};
\fill[tintA] (0,0)--(2,0)--(1.6,1.2)--(0,2)--cycle;
\draw[emph] (0,0)--(2,0)--(1.6,1.2)--(0,2)--cycle;
\draw[faint, dashed] (0,2)--(2.8,0.6);
\draw[faint, dashed] (2,0)--(1.2,2.4);
\draw[->, hl] (0,0)--(1.95,0);
\draw[->, hl] (2,0)--(1.62,1.15);
\node[dot] at (0,0) {};
\node[dot] at (2,0) {};
\node[hl dot] at (1.6,1.2) {};
\node[lab, below left] at (0,0) {$(0,0)$};
\node[lab, below] at (2,0) {$(2,0)$};
\node[lab, above right] at (1.6,1.2) {$(\tfrac85,\tfrac65)$};
\draw[->, emph] (0.6,0.6)--(0.95,0.95) node[lab, above] {$-c$};
\end{tikzpicture}
\end{center}
```

The example in the $(x_1,x_2)$ plane (the slacks are the distances to the two dashed lines). The two pivots walk along edges from $(0,0)$ to $(2,0)$ to the optimal vertex $(\tfrac85,\tfrac65)$.

:::

::: {#rmk-simplex-method-1 .remark name="Pivoting rules, cycling and the Hirsch conjecture"}

The rule that picks $k$ and $j$ is a *pivoting rule*. If $\theta=0$ (a *degenerate* pivot) the basis changes but the vertex does not, and some rules can then cycle forever; *anticycling* rules such as Bland's (smallest eligible index for both $k$ and $j$) never repeat a basis, so the method terminates. Every known rule takes exponentially many pivots on some instances (Klee and Minty for Dantzig's rule), although few pivots are needed in practice, which smoothed analysis (Spielman and Teng) partly explains. Any vertex-walking method needs at least the edge-distance from the start to an optimum, so the diameter of polytopes matters: Hirsch conjectured in 1957 that a $d$-dimensional polytope with $k$ facets has diameter at most $k-d$. Santos disproved it in 2010; the best general bound, $k^{O(\log d)}$ (Kalai and Kleitman), is not polynomial.

:::
