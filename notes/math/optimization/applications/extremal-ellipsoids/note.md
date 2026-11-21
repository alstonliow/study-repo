---
title: "Extremal Ellipsoids and Centering"
sources: [ee364a-8]
requires: [math/optimization/convex-problems/semidefinite-programs, math/optimization/duality/kkt-conditions]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on geometric problems, in our own wording; proofs written out in steps. Numbers checked in Python. -->

Ellipsoids approximate convex sets: the smallest one containing a set and the largest one inside it both come from convex problems. Centers of a set, such as the analytic center of a system of inequalities, are found the same way.

::: {#def-lowner-john-ellipsoid .definition name="Minimum volume ellipsoid (Löwner–John)"}

The minimum volume ellipsoid containing a set $C$ is found by parametrizing $\mathcal E=\{v\mid\lVert Av+b\rVert_2\le1\}$ with $A\in\mathbb S^n_{++}$ (volume proportional to $\det A^{-1}$) and solving
$$\text{minimize }\log\det A^{-1}\quad\text{s.t. }\sup_{v\in C}\lVert Av+b\rVert_2\le1.$$
For a finite set $C=\{x_1,\dots,x_m\}$ the constraints are $\lVert Ax_i+b\rVert_2\le1$, a convex problem.

:::

::: {#def-max-inscribed-ellipsoid .definition name="Maximum volume inscribed ellipsoid"}

The largest ellipsoid $\mathcal E=\{Bu+d\mid\lVert u\rVert_2\le1\}$, $B\in\mathbb S^n_{++}$, inside a convex set $C$ solves
$$\text{maximize }\log\det B\quad\text{s.t. }\sup_{\lVert u\rVert_2\le1}I_C(Bu+d)\le0.$$
For a polyhedron $\{x\mid a_i^{\mathsf T}x\le b_i\}$ the constraints are $\lVert Ba_i\rVert_2+a_i^{\mathsf T}d\le b_i$, a convex problem.

:::

::: {.proof}

1. $\mathcal E$ lies in the halfspace $a_i^{\mathsf T}x\le b_i$ iff $\sup_{\lVert u\rVert_2\le1}a_i^{\mathsf T}(Bu+d)\le b_i$.

2. The supremum is $\lVert Ba_i\rVert_2+a_i^{\mathsf T}d$ by Cauchy–Schwarz (using $B=B^{\mathsf T}$).

:::

::: {#thm-ellipsoid-efficiency .theorem name="Efficiency of ellipsoidal approximation"}

Let $C\subseteq\mathbb{R}^n$ be bounded and convex with nonempty interior.

1. The minimum volume ellipsoid containing $C$, shrunk by the factor $n$ about its centre, lies inside $C$.

2. The maximum volume ellipsoid inside $C$, expanded by the factor $n$ about its centre, contains $C$.

If $C$ is symmetric about a point, the factor $n$ improves to $\sqrt n$.

:::

::: {#rmk-extremal-ellipsoids-1 .remark name="About the efficiency theorem"}

We state @thm-ellipsoid-efficiency without proof. The factor $n$ is attained by a simplex.

:::

::: {#def-analytic-center .definition name="Analytic center"}

The *analytic center* of the inequalities $f_i(x)\le0$, $Fx=g$ (with $f_i$ convex and a strictly feasible point) is the solution of
$$\text{minimize }-\sum_{i=1}^m\log(-f_i(x))\quad\text{s.t. }Fx=g.$$
For linear inequalities $a_i^{\mathsf T}x\le b_i$ it maximizes $\prod_i(b_i-a_i^{\mathsf T}x)$, the product of the slacks.

:::

::: {#exm-analytic-center-interval .example name="Analytic center of an interval"}

For $0\le x\le1$ written as $-x\le0$, $x-1\le0$, the analytic center maximizes $x(1-x)$, at $x=\frac12$. Adding the redundant inequality $x\le2$ moves it: maximizing $x(1-x)(2-x)$ on $(0,1)$ gives $x=1-1/\sqrt3\approx0.423$. The analytic center depends on the description, not only on the set.

:::

::: {#prp-analytic-center-ellipsoids .proposition name="Inner and outer ellipsoids at the analytic center"}

Let $x_{\rm ac}$ be the analytic center of $a_i^{\mathsf T}x\le b_i$, $i=1,\dots,m$, and $H=\sum_i\frac{a_ia_i^{\mathsf T}}{(b_i-a_i^{\mathsf T}x_{\rm ac})^2}$ the Hessian of the log barrier there. Then
$$\{x\mid(x-x_{\rm ac})^{\mathsf T}H(x-x_{\rm ac})\le1\}\subseteq\mathcal P\subseteq\{x\mid(x-x_{\rm ac})^{\mathsf T}H(x-x_{\rm ac})\le m(m-1)\}.$$

:::

::: {.proof}

1. Inner: write $s_i=b_i-a_i^{\mathsf T}x_{\rm ac}>0$ and $d=x-x_{\rm ac}$. If $d^{\mathsf T}Hd=\sum_i(a_i^{\mathsf T}d)^2/s_i^2\le1$ then each $\lvert a_i^{\mathsf T}d\rvert\le s_i$, so $a_i^{\mathsf T}x\le b_i$.

2. Outer: optimality of $x_{\rm ac}$ gives $\sum_ia_i/s_i=0$. For $x\in\mathcal P$ put $t_i=a_i^{\mathsf T}d/s_i\le1$; then $\sum_it_i=0$.

3. Let $P=\sum_{t_i>0}t_i$. At most $m-1$ of the $t_i$ are positive (they sum to $0$ and are not all zero unless $d=0$), each at most $1$, so $P\le m-1$, and $\sum_{t_i>0}t_i^2\le P$. The negative entries sum to $-P$, so $\sum_{t_i<0}t_i^2\le P^2$.

4. Hence $d^{\mathsf T}Hd=\sum_it_i^2\le P+P^2\le(m-1)+(m-1)^2=m(m-1)$.

:::
