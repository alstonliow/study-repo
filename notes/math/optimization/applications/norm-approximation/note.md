---
title: "Norm and Penalty Function Approximation"
sources: [ee364a-6]
requires: [math/optimization/convex-problems/second-order-cone-programs, math/optimization/duality/kkt-conditions]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on approximation and fitting, in our own wording; proofs written out in steps. -->

Fitting $Ax\approx b$ means choosing how to measure the residual $r=Ax-b$. Different norms and penalty functions give different residual distributions; all lead to convex problems.

::: {#def-norm-approximation .definition name="Norm approximation"}

Given $A\in\mathbb{R}^{m\times n}$ with $m\ge n$ and $b\in\mathbb{R}^m$, the *norm approximation problem* is
$$\text{minimize }\lVert Ax-b\rVert.$$
Least squares uses $\lVert\cdot\rVert_2$; Chebyshev (minimax) approximation uses $\lVert\cdot\rVert_\infty$ and is an LP: minimize $t$ subject to $-t\mathbf 1\preceq Ax-b\preceq t\mathbf 1$; sum of absolute residuals uses $\lVert\cdot\rVert_1$ and is an LP: minimize $\mathbf 1^{\mathsf T}y$ subject to $-y\preceq Ax-b\preceq y$.

:::

::: {#def-penalty-function-approximation .definition name="Penalty function approximation"}

For a convex *penalty function* $\phi:\mathbb{R}\to\mathbb{R}$, minimize
$$\phi(r_1)+\cdots+\phi(r_m)\quad\text{subject to }r=Ax-b.$$
Examples: quadratic $\phi(u)=u^2$; dead zone linear $\phi(u)=\max\{0,\lvert u\rvert-a\}$; log barrier $\phi(u)=-a^2\log(1-(u/a)^2)$ for $\lvert u\rvert<a$; and the *Huber* penalty
$$\phi_M(u)=\begin{cases}u^2&\lvert u\rvert\le M,\\M(2\lvert u\rvert-M)&\lvert u\rvert>M,\end{cases}$$
quadratic for small residuals and linear for large ones, so robust to outliers.

:::

::: {#prp-penalty-shapes .proposition name="Optimality condition for penalty approximation"}

If $\phi$ is convex and differentiable, $x$ solves @def-penalty-function-approximation if and only if
$$\sum_{i=1}^m\phi'(r_i)\,a_i=0,\qquad r=Ax-b,$$
where $a_i^{\mathsf T}$ are the rows of $A$.

:::

::: {.proof}

1. The objective $F(x)=\sum_i\phi(a_i^{\mathsf T}x-b_i)$ is convex (@prp-nonnegative-sum-affine-composition) and differentiable with $\nabla F(x)=\sum_i\phi'(r_i)a_i$ by the chain rule.

2. A differentiable convex function is minimized exactly where its gradient vanishes (@cor-convex-stationary-global and @thm-convex-optimality-criterion).

:::

::: {#rmk-norm-approximation-2 .remark name="How the penalty shapes the residuals"}

Each residual pulls on the balance with weight $\phi'(r_i)$. A penalty that grows fast (quadratic, log barrier) makes large residuals very costly, so it avoids them. A penalty that grows only linearly (Huber, $\ell_1$) gives a large residual bounded pull, so a few outliers are tolerated. A penalty with a corner at $0$ ($\ell_1$, dead zone at its edges) lets many residuals sit exactly there.

:::

::: {#exm-huber-line-fit .example name="Line fitting with an outlier"}

Fit $y\approx\alpha+\beta t$ to the seven points $(t,t)$, $t=0,\dots,5$, and the outlier $(6,-6)$. Least squares gives $\alpha=15/7\approx2.14$, $\beta=-2/7\approx-0.29$: the outlier reverses the slope. The Huber fit with $M=1$ gives $\alpha=1/3$, $\beta=0.8$, and the $\ell_1$ fit recovers $\alpha=0$, $\beta=1$ exactly (values computed numerically).

:::

::: {#def-least-norm .definition name="Least-norm problems"}

For $A\in\mathbb{R}^{m\times n}$ with $m\le n$ and $Ax=b$ solvable, the *least-norm problem* is minimize $\lVert x\rVert$ subject to $Ax=b$. With $\lVert\cdot\rVert_2$ the solution is $x=A^{\mathsf T}(AA^{\mathsf T})^{-1}b$ (when $A$ has full row rank); with $\lVert\cdot\rVert_1$ it is an LP whose solutions tend to be sparse.

:::

::: {.proof}

1. Least Euclidean norm: the KKT conditions (@thm-kkt) for minimizing $x^{\mathsf T}x$ subject to $Ax=b$ are $2x+A^{\mathsf T}\nu=0$, $Ax=b$.

2. So $x=-\frac12A^{\mathsf T}\nu$ and $-\frac12AA^{\mathsf T}\nu=b$, giving $\nu=-2(AA^{\mathsf T})^{-1}b$ and $x=A^{\mathsf T}(AA^{\mathsf T})^{-1}b$.

:::

::: {#rmk-norm-approximation-1 .remark name="Interpretations"}

Norm approximation can be read as estimation ($b=Ax+v$ with $v$ a measurement error, @sec-math-optimization-applications-statistical-estimation), as geometry (the point of $\operatorname{range}A$ nearest $b$), or as design ($x$ are design variables, $Ax$ the result, $b$ the target).

:::
