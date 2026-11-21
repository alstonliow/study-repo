---
title: "Regularized and Robust Approximation"
sources: [ee364a-6]
requires: [math/optimization/applications/norm-approximation, math/optimization/convex-problems/vector-optimization]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on approximation and fitting, in our own wording; proofs written out in steps. -->

Regularization trades fit against the size or smoothness of $x$; robust approximation protects against uncertainty in $A$. Both keep the problem convex.

::: {#def-regularized-approximation .definition name="Regularized approximation"}

The bi-criterion problem minimize $(\lVert Ax-b\rVert,\lVert x\rVert)$ with respect to $\mathbb{R}^2_+$ is scalarized (@thm-scalarization) as
$$\text{minimize }\lVert Ax-b\rVert+\gamma\lVert x\rVert,\qquad\gamma>0.$$
*Tikhonov regularization* uses squared Euclidean norms: minimize $\lVert Ax-b\rVert_2^2+\delta\lVert x\rVert_2^2$, with solution $x=(A^{\mathsf T}A+\delta I)^{-1}A^{\mathsf T}b$.

:::

::: {.proof}

1. The Tikhonov objective is $x^{\mathsf T}(A^{\mathsf T}A+\delta I)x-2b^{\mathsf T}Ax+b^{\mathsf T}b$, a strictly convex quadratic for $\delta>0$.

2. Setting its gradient $2(A^{\mathsf T}A+\delta I)x-2A^{\mathsf T}b$ to zero gives the formula; $A^{\mathsf T}A+\delta I\succ0$ is invertible.

:::

::: {#def-signal-reconstruction .definition name="Signal reconstruction"}

Given a corrupted signal $x_{\rm cor}=x+v\in\mathbb{R}^n$, choose $\hat x$ to minimize $(\lVert\hat x-x_{\rm cor}\rVert_2,\ \phi(\hat x))$ with a convex *smoothing* function $\phi$. *Quadratic smoothing* uses $\phi(\hat x)=\sum_{i=1}^{n-1}(\hat x_{i+1}-\hat x_i)^2$; *total variation* uses $\phi(\hat x)=\sum_{i=1}^{n-1}\lvert\hat x_{i+1}-\hat x_i\rvert$.

:::

::: {#exm-tv-vs-quadratic .example name="Keeping jumps"}

Quadratic smoothing penalizes a jump of height $h$ in one step by $h^2$ but the same rise spread over $k$ steps by $h^2/k$, so it blurs edges. Total variation charges $h$ either way, so it removes small noise while keeping sharp jumps. For a step signal plus small noise, total variation reconstruction is nearly piecewise constant.

:::

::: {#def-robust-approximation .definition name="Robust approximation"}

When $A$ is uncertain, either

- *stochastic*: $A$ is random, minimize $\operatorname{E}\lVert Ax-b\rVert$; or
- *worst-case*: $A\in\mathcal A$, minimize $\sup_{A\in\mathcal A}\lVert Ax-b\rVert$.

Both objectives are convex in $x$ (an expectation, resp. a supremum, of convex functions).

:::

::: {#prp-stochastic-robust-ls .proposition name="Stochastic robust least squares"}

If $A=\bar A+U$ with $\operatorname{E}U=0$ and $\operatorname{E}U^{\mathsf T}U=P$, then
$$\operatorname{E}\lVert Ax-b\rVert_2^2=\lVert\bar Ax-b\rVert_2^2+x^{\mathsf T}Px.$$
So stochastic robust least squares is Tikhonov-type regularized least squares; with $P=\delta I$ it is exactly Tikhonov regularization.

:::

::: {.proof}

1. $\lVert(\bar A+U)x-b\rVert_2^2=\lVert\bar Ax-b\rVert_2^2+2(\bar Ax-b)^{\mathsf T}Ux+x^{\mathsf T}U^{\mathsf T}Ux$.

2. Take expectations: the middle term vanishes since $\operatorname{E}U=0$, and $\operatorname{E}x^{\mathsf T}U^{\mathsf T}Ux=x^{\mathsf T}Px$.

:::

::: {#prp-worst-case-robust-ls .proposition name="Worst-case robust least squares is an SOCP"}

For $\mathcal A=\{\bar A+u_1A_1+\cdots+u_pA_p\mid\lVert u\rVert_2\le1\}$,
$$\sup_{A\in\mathcal A}\lVert Ax-b\rVert_2^2=\sup_{\lVert u\rVert_2\le1}\lVert P(x)u+q(x)\rVert_2^2,\qquad P(x)=[A_1x\ \cdots\ A_px],\ q(x)=\bar Ax-b,$$
and minimizing it is equivalent to the SDP
$$\text{minimize }t+\lambda\quad\text{s.t. }\begin{bmatrix}I&P(x)&q(x)\\P(x)^{\mathsf T}&\lambda I&0\\q(x)^{\mathsf T}&0&t\end{bmatrix}\succeq0.$$

:::

::: {.proof}

1. The first equality is $Ax-b=\bar Ax-b+\sum_iu_iA_ix$.

2. By the S-procedure (strong duality for one quadratic constraint, @exm-nonconvex-strong-duality), $\sup_{\lVert u\rVert_2\le1}\lVert Pu+q\rVert_2^2\le t+\lambda$ for some feasible $t,\lambda\ge0$ iff $\begin{bmatrix}\lambda I-P^{\mathsf T}P&-P^{\mathsf T}q\\-q^{\mathsf T}P&t-q^{\mathsf T}q\end{bmatrix}\succeq0$, which by a Schur complement on the identity block is the stated LMI. We use the S-procedure without proof.

:::

::: {#rmk-regularized-and-robust-approximation-1 .remark name="Regularization as robustness"}

Regularization terms can be read three ways: as a second objective, as a prior (@sec-math-optimization-applications-statistical-estimation), or as protection against uncertainty in $A$ (@prp-stochastic-robust-ls).

:::
