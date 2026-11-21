---
title: "Optimization Problems and Convex Problems"
sources: [ee364a-4]
requires: [math/optimization/convex-functions/convex-functions]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on the introduction and on convex optimization problems, in our own wording; proofs written out in steps. -->

An optimization problem asks for the least value of an objective over the points that satisfy some constraints. When the objective and the inequality constraints are convex and the equality constraints affine, every local solution is global and optimality has a simple first-order description.

::: {#def-optimization-problem .definition name="Optimization problem in standard form"}

An optimization problem in standard form is
$$\begin{array}{ll}\text{minimize}&f_0(x)\\ \text{subject to}&f_i(x)\le0,\quad i=1,\dots,m,\\ &h_i(x)=0,\quad i=1,\dots,p,\end{array}$$
with variable $x\in\mathbb{R}^n$, objective $f_0$, inequality constraints $f_i$ and equality constraints $h_i$. Its *domain* is $\mathcal D=\bigcap_i\operatorname{dom}f_i\cap\bigcap_i\operatorname{dom}h_i$; a point of $\mathcal D$ satisfying all constraints is *feasible*. The *optimal value* is
$$p^\star=\inf\{f_0(x)\mid x\text{ feasible}\},$$
with $p^\star=+\infty$ if no point is feasible and $p^\star=-\infty$ if the problem is *unbounded below*. A feasible $x$ with $f_0(x)=p^\star$ is *optimal*; $x$ is *locally optimal* if it is optimal for the problem with the extra constraint $\lVert z-x\rVert_2\le R$ for some $R>0$.

:::

::: {#exm-optimal-values .example name="Optimal values on the line"}

1. $f_0(x)=1/x$ on $x>0$: $p^\star=0$, not attained.

2. $f_0(x)=-\log x$ on $x>0$: $p^\star=-\infty$.

3. $f_0(x)=x\log x$ on $x>0$: $p^\star=-1/e$, attained at $x=1/e$.

4. $f_0(x)=x^3-3x$: $p^\star=-\infty$; $x=1$ is locally optimal.

:::

::: {#def-convex-optimization-problem .definition name="Convex optimization problem"}

A *convex optimization problem* is a problem in standard form whose objective $f_0$ and inequality constraint functions $f_1,\dots,f_m$ are convex and whose equality constraints are affine:
$$\begin{array}{ll}\text{minimize}&f_0(x)\\ \text{subject to}&f_i(x)\le0,\quad i=1,\dots,m,\\ &Ax=b.\end{array}$$
Its feasible set is convex, as an intersection of sublevel sets of convex functions and an affine set. A *feasibility problem* is the special case $f_0=0$, where $p^\star$ is $0$ or $+\infty$.

:::

::: {#rmk-optimization-problems-1 .remark name="Convexity depends on the description"}

The problem of minimizing $x_1^2+x_2^2$ subject to $x_1/(1+x_2^2)\le0$ and $(x_1+x_2)^2=0$ is not a convex problem as written, although its feasible set $\{x\mid x_1=-x_2\le0\}$ is convex. Replacing the constraints by $x_1\le0$ and $x_1+x_2=0$ gives an equivalent convex problem.

:::

::: {#thm-convex-local-global .theorem name="Local optima of convex problems are global"}

For a convex optimization problem, every locally optimal point is optimal.

:::

::: {.proof}

1. Let $x$ be locally optimal with radius $R$ and suppose a feasible $y$ has $f_0(y)<f_0(x)$. Then $\lVert y-x\rVert_2>R$.

2. Put $z=(1-\theta)x+\theta y$ with $\theta=\frac{R}{2\lVert y-x\rVert_2}\in(0,\tfrac12)$. Then $z$ is feasible (the feasible set is convex) and $\lVert z-x\rVert_2=R/2$.

3. Convexity of $f_0$ gives $f_0(z)\le(1-\theta)f_0(x)+\theta f_0(y)<f_0(x)$, contradicting local optimality.

:::

::: {#thm-convex-optimality-criterion .theorem name="Optimality criterion for differentiable objectives"}

Let $f_0$ be differentiable in a convex problem with feasible set $X$. Then $x\in X$ is optimal if and only if
$$\nabla f_0(x)^{\mathsf T}(y-x)\ge0\qquad\text{for all }y\in X.$$
Special cases: unconstrained, $\nabla f_0(x)=0$; with only $Ax=b$, there is $\nu$ with $\nabla f_0(x)+A^{\mathsf T}\nu=0$; on $x\succeq0$, $\nabla f_0(x)\succeq0$ and $x_i(\nabla f_0(x))_i=0$ for each $i$.

:::

::: {.proof}

1. If the condition holds, the first-order condition (@thm-first-order-convexity) gives $f_0(y)\ge f_0(x)+\nabla f_0(x)^{\mathsf T}(y-x)\ge f_0(x)$ for $y\in X$.

2. Conversely, if $\nabla f_0(x)^{\mathsf T}(y-x)<0$ for some $y\in X$, the points $z(t)=x+t(y-x)$, $0<t\le1$, are feasible and $\frac{d}{dt}f_0(z(t))\big|_{t=0}<0$, so $f_0(z(t))<f_0(x)$ for small $t$.

3. Unconstrained: take $y=x-t\nabla f_0(x)$ to get $-t\lVert\nabla f_0(x)\rVert_2^2\ge0$.

4. Equality constraints: $y-x$ ranges over $\operatorname{null}A$, a subspace, so $\nabla f_0(x)^{\mathsf T}v\ge0$ for $\pm v$ forces $\nabla f_0(x)\perp\operatorname{null}A$, that is, $\nabla f_0(x)\in\operatorname{range}A^{\mathsf T}$.

5. Nonnegative orthant: $\nabla f_0(x)^{\mathsf T}y\ge\nabla f_0(x)^{\mathsf T}x$ for all $y\succeq0$ forces $\nabla f_0(x)\succeq0$ (else let one $y_i\to\infty$) and then, with $y=0$, $\nabla f_0(x)^{\mathsf T}x\le0$, a sum of nonnegative terms, so each term is $0$.

:::

::: {#exm-optimality-criterion-box .example name="A one-variable check"}

Minimize $(x-2)^2$ over $X=[0,1]$. At $x=1$, $f_0'(1)=-2$ and $f_0'(1)(y-1)=-2(y-1)\ge0$ for every $y\le1$, so $x=1$ is optimal. At $x=0.5$ the choice $y=1$ gives $-3\cdot0.5<0$, so it is not.

:::
