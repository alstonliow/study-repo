---
title: "The Lagrange Dual Function"
sources: [ee364a-5]
requires: [math/optimization/convex-problems/optimization-problems, math/optimization/convex-functions/conjugate-function]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on duality, in our own wording; proofs written out in steps. Lagrange multipliers for equality constraints in calculus are in @sec-math-calculus-multivariable-differentiation-lagrange-multipliers. -->

Adding the constraints to the objective with weights gives the Lagrangian. Minimizing it over $x$ gives a concave function of the weights whose every value is a lower bound on the optimal value, for any problem, convex or not.

::: {#def-lagrangian .definition name="Lagrangian, dual function" related="thm-lagrange-multipliers"}

For the problem of @def-optimization-problem with domain $\mathcal D$, the *Lagrangian* $L:\mathbb{R}^n\times\mathbb{R}^m\times\mathbb{R}^p\to\mathbb{R}$ is
$$L(x,\lambda,\nu)=f_0(x)+\sum_{i=1}^m\lambda_if_i(x)+\sum_{i=1}^p\nu_ih_i(x),$$
with *Lagrange multipliers* (dual variables) $\lambda_i$ and $\nu_i$. The *Lagrange dual function* is
$$g(\lambda,\nu)=\inf_{x\in\mathcal D}L(x,\lambda,\nu).$$
It is concave, as a pointwise infimum of affine functions of $(\lambda,\nu)$, and may take the value $-\infty$.

:::

::: {#thm-dual-lower-bound .theorem name="Lower bound property"}

If $\lambda\succeq0$, then $g(\lambda,\nu)\le p^\star$.

:::

::: {.proof}

1. Let $\tilde x$ be feasible. Then $f_i(\tilde x)\le0$, $\lambda_i\ge0$ and $h_i(\tilde x)=0$, so $\sum_i\lambda_if_i(\tilde x)+\sum_i\nu_ih_i(\tilde x)\le0$.

2. Hence $g(\lambda,\nu)\le L(\tilde x,\lambda,\nu)\le f_0(\tilde x)$.

3. Taking the infimum over feasible $\tilde x$ gives $g(\lambda,\nu)\le p^\star$.

:::

::: {#exm-dual-least-norm .example name="Least-norm solution of linear equations"}

Minimize $x^{\mathsf T}x$ subject to $Ax=b$. The Lagrangian $x^{\mathsf T}x+\nu^{\mathsf T}(Ax-b)$ is minimized at $x=-\frac12A^{\mathsf T}\nu$, so
$$g(\nu)=-\tfrac14\nu^{\mathsf T}AA^{\mathsf T}\nu-b^{\mathsf T}\nu,$$
a concave quadratic, and $p^\star\ge-\frac14\nu^{\mathsf T}AA^{\mathsf T}\nu-b^{\mathsf T}\nu$ for every $\nu$.

:::

::: {#exm-dual-standard-lp .example name="Standard form LP"}

Minimize $c^{\mathsf T}x$ subject to $Ax=b$, $x\succeq0$. The Lagrangian $c^{\mathsf T}x+\nu^{\mathsf T}(Ax-b)-\lambda^{\mathsf T}x=-b^{\mathsf T}\nu+(c+A^{\mathsf T}\nu-\lambda)^{\mathsf T}x$ is affine in $x$, so it is bounded below only when its slope vanishes:
$$g(\lambda,\nu)=\begin{cases}-b^{\mathsf T}\nu&\text{if }A^{\mathsf T}\nu-\lambda+c=0,\\-\infty&\text{otherwise.}\end{cases}$$

:::

::: {#exm-two-way-partitioning-dual .example name="Two-way partitioning"}

Minimize $x^{\mathsf T}Wx$ subject to $x_i^2=1$, $i=1,\dots,n$, with $W\in\mathbb S^n$: split $\{1,\dots,n\}$ into two groups ($x_i=\pm1$), with $W_{ij}$ the cost of putting $i,j$ in the same group and $-W_{ij}$ in different ones. This problem is not convex and has $2^n$ feasible points. The Lagrangian $x^{\mathsf T}(W+\operatorname{diag}\nu)x-\mathbf 1^{\mathsf T}\nu$ gives
$$g(\nu)=\begin{cases}-\mathbf 1^{\mathsf T}\nu&\text{if }W+\operatorname{diag}\nu\succeq0,\\-\infty&\text{otherwise.}\end{cases}$$
With $\nu=-\lambda_{\min}(W)\mathbf 1$ this gives the bound $p^\star\ge n\,\lambda_{\min}(W)$.

:::

::: {#prp-dual-via-conjugate .proposition name="Dual function through the conjugate"}

For the problem minimize $f_0(x)$ subject to $Ax\preceq b$, $Cx=d$,
$$g(\lambda,\nu)=-b^{\mathsf T}\lambda-d^{\mathsf T}\nu-f_0^*(-A^{\mathsf T}\lambda-C^{\mathsf T}\nu),$$
with $f_0^*$ the conjugate (@def-conjugate-function).

:::

::: {.proof}

1. $g(\lambda,\nu)=\inf_x\big(f_0(x)+(A^{\mathsf T}\lambda+C^{\mathsf T}\nu)^{\mathsf T}x\big)-b^{\mathsf T}\lambda-d^{\mathsf T}\nu$.

2. $\inf_x(f_0(x)+y^{\mathsf T}x)=-\sup_x\big((-y)^{\mathsf T}x-f_0(x)\big)=-f_0^*(-y)$ with $y=A^{\mathsf T}\lambda+C^{\mathsf T}\nu$.

:::

::: {#exm-dual-norm-minimization .example name="Equality constrained norm minimization"}

Minimize $\lVert x\rVert$ subject to $Ax=b$. The conjugate of a norm is the indicator of the dual-norm unit ball (@exm-conjugates), so
$$g(\nu)=-b^{\mathsf T}\nu-f_0^*(-A^{\mathsf T}\nu)=\begin{cases}-b^{\mathsf T}\nu&\text{if }\lVert A^{\mathsf T}\nu\rVert_*\le1,\\-\infty&\text{otherwise.}\end{cases}$$

:::

::: {#rmk-lagrange-dual-function-1 .remark name="Linear penalties"}

The Lagrangian replaces the hard constraints $f_i(x)\le0$ by linear penalties $\lambda_if_i(x)$, which reward slack. A hard constraint is an infinitely steep penalty, which always lies above a linear one with $\lambda_i\ge0$; this is the lower bound property in words.

:::
