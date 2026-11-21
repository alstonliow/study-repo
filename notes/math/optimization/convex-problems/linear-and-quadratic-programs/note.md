---
title: "Linear and Quadratic Programs"
sources: [ee364a-4]
requires: [math/optimization/convex-problems/optimization-problems]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on convex optimization problems, in our own wording; proofs written out in steps. Linear programs as an algorithmic topic are in @sec-cs-algorithm-design-linear-programming; this note places them among convex problems. -->

Linear programs (@def-linear-program) have affine objective and constraints; quadratic programs allow a convex quadratic objective; QCQPs allow convex quadratic constraints too. Each class contains the previous one.

::: {#def-lp-general-form .definition name="Linear program in general form" related="def-linear-program"}

A *linear program* (LP) is
$$\begin{array}{ll}\text{minimize}&c^{\mathsf T}x+d\\ \text{subject to}&Gx\preceq h,\\ &Ax=b.\end{array}$$
Its feasible set is a polyhedron (@def-polyhedron). In *standard form* the only inequalities are $x\succeq0$; any LP can be put in standard form with slack variables and by writing $x=x^+-x^-$, $x^\pm\succeq0$.

:::

::: {#exm-chebyshev-center .example name="Chebyshev centre of a polyhedron"}

The largest ball $\{x_c+u\mid\lVert u\rVert_2\le r\}$ inside $\mathcal P=\{x\mid a_i^{\mathsf T}x\le b_i\}$ solves an LP. The ball lies in the halfspace $a_i^{\mathsf T}x\le b_i$ iff $\sup_{\lVert u\rVert_2\le r}a_i^{\mathsf T}(x_c+u)=a_i^{\mathsf T}x_c+r\lVert a_i\rVert_2\le b_i$. So maximize $r$ subject to $a_i^{\mathsf T}x_c+r\lVert a_i\rVert_2\le b_i$, linear in $(x_c,r)$. For the triangle $x_1\ge0$, $x_2\ge0$, $x_1+x_2\le1$ the answer is $r=1/(2+\sqrt2)\approx0.293$ at $x_c=(r,r)$.

:::

::: {#def-linear-fractional-program .definition name="Linear-fractional program"}

Minimize $f_0(x)=\dfrac{c^{\mathsf T}x+d}{e^{\mathsf T}x+f}$ on $e^{\mathsf T}x+f>0$ subject to $Gx\preceq h$, $Ax=b$. It is quasiconvex, and when the feasible set is nonempty it is equivalent to the LP
$$\text{minimize }c^{\mathsf T}y+dz\quad\text{s.t. }Gy\preceq hz,\ Ay=bz,\ e^{\mathsf T}y+fz=1,\ z\ge0,$$
through $y=x/(e^{\mathsf T}x+f)$, $z=1/(e^{\mathsf T}x+f)$.

:::

::: {#def-qp-qcqp .definition name="Quadratic program, QCQP"}

A *quadratic program* (QP) is
$$\begin{array}{ll}\text{minimize}&\tfrac12x^{\mathsf T}Px+q^{\mathsf T}x+r\\ \text{subject to}&Gx\preceq h,\quad Ax=b,\end{array}$$
with $P\in\mathbb S^n_+$. A *quadratically constrained quadratic program* (QCQP) also has constraints $\tfrac12x^{\mathsf T}P_ix+q_i^{\mathsf T}x+r_i\le0$ with $P_i\in\mathbb S^n_+$; its feasible set is an intersection of ellipsoids (when $P_i\succ0$) and an affine set.

:::

::: {#exm-qp-examples .example name="Least squares and portfolio choice"}

1. Least squares $\lVert Ax-b\rVert_2^2$ (@def-least-squares-solution) is an unconstrained QP; adding bounds $l\preceq x\preceq u$ keeps it a QP.

2. *Markowitz portfolio*: with mean return $\bar p$ and covariance $\Sigma$ of asset returns, minimize the variance $x^{\mathsf T}\Sigma x$ of a portfolio $x$ subject to $\bar p^{\mathsf T}x\ge r_{\min}$, $\mathbf 1^{\mathsf T}x=1$, $x\succeq0$.

:::

::: {#rmk-linear-and-quadratic-programs-1 .remark name="The hierarchy"}

LP $\subset$ QP $\subset$ QCQP $\subset$ SOCP (@sec-math-optimization-convex-problems-second-order-cone-programs) $\subset$ SDP (@sec-math-optimization-convex-problems-semidefinite-programs). Each inclusion is by rewriting, not by identity of form.

:::
