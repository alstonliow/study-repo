---
title: "Linear and Nonlinear Discrimination"
sources: [ee364a-8]
requires: [math/optimization/duality/lagrange-dual-problem, math/optimization/convex-problems/second-order-cone-programs]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on geometric problems, in our own wording; proofs written out in steps. Linear classifiers trained by gradient methods are in @sec-ai-machine-learning-linear-classification. -->

Separating two finite point sets by a hyperplane is a linear feasibility problem. Asking for the widest gap gives a QP whose dual is a distance between convex hulls; allowing violations gives the support vector classifier.

::: {#def-linear-discrimination .definition name="Linear discrimination"}

Point sets $\{x_1,\dots,x_N\}$ and $\{y_1,\dots,y_M\}$ are *linearly separable* if there are $a,b$ with
$$a^{\mathsf T}x_i+b>0,\qquad a^{\mathsf T}y_i+b<0.$$
By scaling $(a,b)$, this is equivalent to the LP feasibility problem $a^{\mathsf T}x_i+b\ge1$, $a^{\mathsf T}y_i+b\le-1$.

:::

::: {#def-max-margin-separation .definition name="Robust (maximum margin) separation"}

The gap between the hyperplanes $a^{\mathsf T}z+b=\pm1$ is $2/\lVert a\rVert_2$. The *maximum margin* separator solves the convex problem
$$\text{minimize }\tfrac12\lVert a\rVert_2\quad\text{s.t. }a^{\mathsf T}x_i+b\ge1,\ a^{\mathsf T}y_i+b\le-1.$$

:::

::: {#thm-max-margin-dual .theorem name="Dual of maximum margin separation"}

The Lagrange dual of @def-max-margin-separation is
$$\text{maximize }\mathbf 1^{\mathsf T}\lambda+\mathbf 1^{\mathsf T}\mu\quad\text{s.t. }\Big\lVert\sum_i\lambda_ix_i-\sum_i\mu_iy_i\Big\rVert_2\le\tfrac12,\ \mathbf 1^{\mathsf T}\lambda=\mathbf 1^{\mathsf T}\mu,\ \lambda,\mu\succeq0.$$
Its optimal value is $1/D$, where $D=\operatorname{dist}(\operatorname{conv}\{x_i\},\operatorname{conv}\{y_i\})$, and the maximum margin $2/\lVert a^\star\rVert_2$ equals $D$.

:::

::: {.proof}

1. The Lagrangian is $\frac12\lVert a\rVert_2+\sum_i\lambda_i(1-a^{\mathsf T}x_i-b)+\sum_i\mu_i(1+a^{\mathsf T}y_i+b)$.

2. Minimizing over $b$ is $-\infty$ unless $\mathbf 1^{\mathsf T}\lambda=\mathbf 1^{\mathsf T}\mu$. Minimizing $\frac12\lVert a\rVert_2-a^{\mathsf T}w$, with $w=\sum_i\lambda_ix_i-\sum_i\mu_iy_i$, over $a$ is $0$ if $\lVert w\rVert_2\le\frac12$ and $-\infty$ otherwise.

3. Write $\lambda=t\theta$, $\mu=t\gamma$ with $t=\mathbf 1^{\mathsf T}\lambda\ge0$ and $\theta,\gamma$ in probability simplices. The dual becomes maximize $2t$ subject to $t\lVert\sum_i\theta_ix_i-\sum_i\gamma_iy_i\rVert_2\le\frac12$. The best choice of $\theta,\gamma$ makes the norm $D$, so $t=1/(2D)$ and $d^\star=1/D$.

4. The constraints are affine and feasible (the sets are separable), so strong duality holds (@thm-slater) and $\frac12\lVert a^\star\rVert_2=1/D$. Hence the margin $2/\lVert a^\star\rVert_2=D$.

:::

::: {#def-support-vector-classifier .definition name="Support vector classifier"}

When the sets are not separable, allow violations $u_i,v_i\ge0$ and trade them off against the margin:
$$\text{minimize }\lVert a\rVert_2+\gamma(\mathbf 1^{\mathsf T}u+\mathbf 1^{\mathsf T}v)\quad\text{s.t. }a^{\mathsf T}x_i+b\ge1-u_i,\ a^{\mathsf T}y_i+b\le-1+v_i,\ u,v\succeq0.$$

:::

::: {#exm-separation-in-line .example name="Two points on a line"}

For $x_1=1$ and $y_1=-1$ in $\mathbb{R}$, the constraints $a+b\ge1$, $-a+b\le-1$ give $a\ge1$, so the maximum margin separator is $a=1$, $b=0$, margin $2/\lvert a\rvert=2$, the distance between the points.

:::

::: {#rmk-linear-discrimination-1 .remark name="Nonlinear discrimination and placement"}

Replacing $a^{\mathsf T}z+b$ by $\theta^{\mathsf T}F(z)$ for fixed basis functions $F$ (for example quadratics $z^{\mathsf T}Pz+q^{\mathsf T}z+r$, or polynomials) keeps the problem linear in $\theta$, so nonlinear separation is still an LP or QP. Placement and facility location problems, which choose positions to minimize a convex function of distances between linked points, are similar convex geometric problems.

:::
