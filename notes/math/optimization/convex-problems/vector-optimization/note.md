---
title: "Vector and Multicriterion Optimization"
sources: [ee364a-4]
requires: [math/optimization/convex-problems/optimization-problems, math/optimization/convex-sets/dual-cones]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on convex optimization problems, in our own wording; proofs written out in steps. -->

When the objective is a vector, there is usually no single best point. One seeks Pareto optimal points instead, and scalarization finds them by minimizing weighted sums.

::: {#def-vector-optimization .definition name="Vector optimization problem"}

A *vector optimization problem* is
$$\begin{array}{ll}\text{minimize (w.r.t. }K)&f_0(x)\\ \text{subject to}&f_i(x)\le0,\quad h_i(x)=0,\end{array}$$
with $f_0:\mathbb{R}^n\to\mathbb{R}^q$ and a proper cone $K\subseteq\mathbb{R}^q$. It is *convex* if $f_0$ is $K$-convex, the $f_i$ are convex and the $h_i$ affine. Let $\mathcal O=\{f_0(x)\mid x\text{ feasible}\}$ be the set of achievable objective values. A feasible $x$ is *optimal* if $f_0(x)$ is the minimum element of $\mathcal O$, and *Pareto optimal* if $f_0(x)$ is a minimal element (@def-minimum-minimal-element). For $K=\mathbb{R}^q_+$ this is *multicriterion* optimization.

:::

::: {#thm-scalarization .theorem name="Scalarization"}

If $\lambda\succ_{K^*}0$ and $x$ minimizes $\lambda^{\mathsf T}f_0(x)$ over the feasible set, then $x$ is Pareto optimal. For a convex vector problem, every Pareto optimal point minimizes $\lambda^{\mathsf T}f_0$ for some nonzero $\lambda\succeq_{K^*}0$.

:::

::: {.proof}

1. The first claim is @thm-minimal-via-dual applied to $\mathcal O$.

2. For the second, $\mathcal O$ need not be convex, but $\mathcal A=\mathcal O+K$ is convex for a convex problem: if $f_0(x_1)+k_1,f_0(x_2)+k_2\in\mathcal A$, then $f_0(\theta x_1+(1-\theta)x_2)\preceq_K\theta f_0(x_1)+(1-\theta)f_0(x_2)$, so the combination is $f_0$ of a feasible point plus an element of $K$.

3. A minimal point of $\mathcal O$ is minimal in $\mathcal A$ (a point of $\mathcal A$ below it is below some point of $\mathcal O$). Part 3 of @thm-minimal-via-dual applied to the convex set $\mathcal A$ gives $\lambda\ne0$, $\lambda\succeq_{K^*}0$, with $f_0(x)$ minimizing $\lambda^{\mathsf T}z$ over $\mathcal A\supseteq\mathcal O$.

:::

::: {#exm-regularized-least-squares-tradeoff .example name="Regularized least squares"}

Minimize $(\lVert Ax-b\rVert_2^2,\lVert x\rVert_2^2)$ with respect to $\mathbb{R}^2_+$. Scalarizing with $\lambda=(1,\gamma)$, $\gamma>0$, gives $x(\gamma)=(A^{\mathsf T}A+\gamma I)^{-1}A^{\mathsf T}b$; as $\gamma$ runs over $(0,\infty)$ these trace the Pareto optimal trade-off curve between fit and size.

:::

::: {#exm-risk-return .example name="Risk and return"}

For a portfolio $x$ with $\mathbf 1^{\mathsf T}x=1$, $x\succeq0$, minimize $(-\bar p^{\mathsf T}x,\ x^{\mathsf T}\Sigma x)$: maximize mean return and minimize variance. Scalarizing gives the QPs minimize $-\bar p^{\mathsf T}x+\gamma x^{\mathsf T}\Sigma x$ over the simplex, whose solutions form the efficient frontier.

:::

::: {#rmk-vector-optimization-1 .remark name="Optimal points are rare"}

An optimal point exists only when one point beats all others in every objective at once. In multicriterion problems that is the exception; the useful output is the set of Pareto optimal values, the trade-off surface.

:::
