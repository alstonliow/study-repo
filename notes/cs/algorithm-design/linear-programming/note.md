---
title: "Linear Programming"
sources: [mit6046-15]
requires: [cs/algorithm-design/randomized-algorithms, cs/graph-algorithms/maximum-flow]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 15, in our own wording; example our own (checked by computation); proofs written out in steps. -->

::: {#def-linear-program .definition name="Linear program"}

A *linear program* (LP) asks to maximise or minimise a linear function of real variables $x_1,\dots,x_n$ subject to linear constraints (equalities or non-strict inequalities). In *standard form* it reads: maximise $c^{\mathsf T}x$ subject to $Ax\le b$ and $x\ge0$, for given $c\in\mathbb R^n$, $A\in\mathbb R^{m\times n}$ and $b\in\mathbb R^m$. A point satisfying the constraints is *feasible*; the feasible points form a convex polyhedron.

:::

Every LP can be put in standard form: minimising $c^{\mathsf T}x$ is maximising $-c^{\mathsf T}x$; an equality is two inequalities; $\ge$ becomes $\le$ after multiplying by $-1$; and a variable without a sign constraint is written as $x'-x''$ with $x',x''\ge0$.

::: {#exm-lp-campaign .example name="Spending on campaigns"}

A campaign can spend on two kinds of advertising. Each unit of the first kind wins $2$ votes in a city and $1$ in the country; each unit of the second wins $1$ and $3$. At least $8$ votes are needed in each region. Minimise the total spending $x_1+x_2$ subject to
$$2x_1+x_2\ge8,\qquad x_1+3x_2\ge8,\qquad x_1,x_2\ge0.$$
The optimum is at the corner where both constraints are tight: $x_1=\frac{16}5$, $x_2=\frac85$, with cost $\frac{24}5$. Each corner of the feasible region is the intersection of two tight constraints, and a linear objective is optimised at a corner.

:::

::: {#fig-linear-programming-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.5cm,y=0.5cm]
\draw[->] (0,0) -- (8.6,0) node[lab, anchor=west] {$x_1$};
\draw[->] (0,0) -- (0,8.6) node[lab, anchor=south] {$x_2$};
\fill[tintA] (0,8.4) -- (0,8) -- (3.2,1.6) -- (8,0) -- (8.4,0) -- (8.4,8.4) -- cycle;
\draw[faint] (0,8) -- (4.2,-0.4); \draw[faint] (0,2.67) -- (8.4,-0.13);
\draw[emph] (0,8) -- (3.2,1.6) -- (8,0);
\draw[faint, dashed] (0,4.8) -- (4.8,0);
\fill (3.2,1.6) circle[pt]; \node[lab,tick, anchor=west] at (3.35,1.75) {$(\frac{16}5,\frac85)$};
\node[lab,tick] at (5.6,5.6) {feasible};
\node[lab,tick, anchor=west] at (4.85,0.35) {$x_1+x_2=\frac{24}5$};
\end{tikzpicture}
\end{center}
```

The feasible region of the campaign example (shaded, unbounded upwards). The objective $x_1+x_2$ is smallest at the corner $(\frac{16}5,\frac85)$ where both constraints are tight; the dashed line is the level set $x_1+x_2=\frac{24}5$, which touches the region only there.

:::

## Duality

::: {#def-dual-lp .definition name="Dual program"}

The *dual* of the standard-form LP (the *primal*) "maximise $c^{\mathsf T}x$ subject to $Ax\le b$, $x\ge0$" is "minimise $b^{\mathsf T}y$ subject to $A^{\mathsf T}y\ge c$, $y\ge0$", with one variable $y_i$ per primal constraint.

:::

::: {#thm-weak-duality .theorem name="Weak duality"}

If $x$ is feasible for the primal and $y$ for the dual, then $c^{\mathsf T}x\le b^{\mathsf T}y$.

:::

::: {.proof}

$c^{\mathsf T}x\le(A^{\mathsf T}y)^{\mathsf T}x=y^{\mathsf T}Ax\le y^{\mathsf T}b$. The first step uses $c\le A^{\mathsf T}y$ and $x\ge0$; the second uses $Ax\le b$ and $y\ge0$.

:::

So any dual feasible $y$ *certifies* an upper bound on the primal optimum. The strong form, which we state without proof, says that the bounds meet.

::: {#thm-strong-duality .theorem name="Strong duality"}

If the primal has an optimal solution, so does the dual, and the two optimal values are equal.

:::

Max-flow min-cut (@thm-max-flow-min-cut) is an instance: the maximum flow is an LP whose dual is (a relaxation of) the minimum cut. In the example above, multiplying the constraints by $y_1=\frac25$ and $y_2=\frac15$ and adding gives $x_1+x_2\ge\frac{24}5$, which proves that $\frac{24}5$ is optimal.

## Solving linear programs

::: {#rmk-linear-programming-algorithms .remark name="Algorithms for LP"}

1. The *simplex method* (Dantzig, 1947) walks from corner to corner of the feasible region, each step improving the objective, until no neighbouring corner is better. Each step is a *pivot* that exchanges one tight constraint for another. It is fast in practice but takes exponentially many steps on some inputs.
2. The *ellipsoid method* (Khachiyan, 1979) was the first polynomial-time algorithm, but it is slow in practice.
3. *Interior-point methods* (Karmarkar, 1984) move through the inside of the region; they are polynomial and practical.

If the variables must be *integers*, the problem (integer linear programming) is NP-hard (@sec-cs-theory-np-complete-reductions).

:::

Many problems are LPs: shortest paths (maximise $d(t)$ subject to $d(v)\le d(u)+w(u,v)$ and $d(s)=0$), maximum flow, and diet, production and transport planning. Formulating a problem as an LP and calling a solver is often the quickest correct solution.
