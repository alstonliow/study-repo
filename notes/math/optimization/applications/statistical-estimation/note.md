---
title: "Statistical Estimation and Detection"
sources: [ee364a-7]
requires: [math/optimization/applications/norm-approximation, math/optimization/convex-functions/log-concave-functions]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on statistical estimation, in our own wording; proofs written out in steps. Logistic regression as a learning method is in @sec-ai-machine-learning-logistic-regression. -->

Maximum likelihood estimation is a convex problem whenever the log-likelihood is concave in the parameters, which happens for linear measurements with log-concave noise and for logistic models. Choosing a detector that trades off error probabilities is also convex.

::: {#def-maximum-likelihood-estimation .definition name="Maximum likelihood estimation" related="def-estimator-properties"}

For a family of densities $p_x(y)$ indexed by $x\in C$, the *maximum likelihood* (ML) estimate from an observation $y$ is
$$\hat x_{\rm ml}=\operatorname*{argmax}_{x\in C}\ \ell(x),\qquad\ell(x)=\log p_x(y).$$
This is a convex problem when $\ell$ is concave in $x$ for each $y$ and $C$ is convex.

:::

::: {#prp-ml-linear-measurements .proposition name="Linear measurements with IID noise"}

Let $y_i=a_i^{\mathsf T}x+v_i$, $i=1,\dots,m$, with independent noise of density $p$. Then
$$\ell(x)=\sum_{i=1}^m\log p(y_i-a_i^{\mathsf T}x),$$
which is concave in $x$ when $p$ is log-concave. Gaussian noise gives least squares, Laplacian noise ($p(z)\propto e^{-\lvert z\rvert/a}$) gives $\ell_1$-norm approximation, and uniform noise on $[-a,a]$ gives any $x$ with $\lVert Ax-y\rVert_\infty\le a$.

:::

::: {.proof}

1. Independence makes the joint density the product $\prod_ip(y_i-a_i^{\mathsf T}x)$; its logarithm is the stated sum.

2. Each term is a concave function ($\log p$) of an affine function of $x$, so the sum is concave (@prp-nonnegative-sum-affine-composition).

3. Gaussian: $\log p(z)=-z^2/(2\sigma^2)+\text{const}$, so maximizing $\ell$ is minimizing $\sum_ir_i^2$. Laplacian: $-\lvert z\rvert/a+\text{const}$ gives $\sum_i\lvert r_i\rvert$. Uniform: $\ell$ is a constant on $\{\lvert r_i\rvert\le a\}$ and $-\infty$ elsewhere.

:::

::: {#exm-logistic-ml .example name="Logistic regression as ML"}

A binary $y\in\{0,1\}$ has $\operatorname{P}(y=1)=\frac{e^{a^{\mathsf T}u+b}}{1+e^{a^{\mathsf T}u+b}}$ for explanatory variable $u$. With data $(u_i,y_i)$ ordered so that $y_1=\dots=y_k=1$ and $y_{k+1}=\dots=y_m=0$,
$$\ell(a,b)=\sum_{i=1}^k(a^{\mathsf T}u_i+b)-\sum_{i=1}^m\log\big(1+e^{a^{\mathsf T}u_i+b}\big),$$
concave in $(a,b)$ since $\log(1+e^z)$ is convex (log-sum-exp of $0$ and $z$).

:::

::: {#def-hypothesis-testing-randomized .definition name="Randomized detector"}

A random variable $X\in\{1,\dots,n\}$ has distribution $p$ or $q$ (hypotheses $1$ and $2$), the columns of $P=[p\ q]\in\mathbb{R}^{n\times2}$. A *randomized detector* is a matrix $T\in\mathbb{R}^{2\times n}$ with nonnegative entries and columns summing to $1$; on observing $X=k$ it guesses hypothesis $i$ with probability $t_{ik}$. The *detection probability matrix* $D=TP$ has the error probabilities $P_{\rm fp}=D_{21}$ and $P_{\rm fn}=D_{12}$ off the diagonal.

:::

::: {#thm-optimal-detector-lp .theorem name="Optimal detectors by LP"}

Minimizing $P_{\rm fp}+\lambda P_{\rm fn}$ over randomized detectors, $\lambda>0$, is an LP whose solution is deterministic: guess hypothesis $1$ when $p_k\ge\lambda q_k$ and hypothesis $2$ otherwise (a likelihood ratio test).

:::

::: {.proof}

1. $P_{\rm fp}+\lambda P_{\rm fn}=\sum_k(t_{2k}p_k+\lambda t_{1k}q_k)$ is linear in $T$, and the constraints $t_{1k}+t_{2k}=1$, $t_{ik}\ge0$ are linear, so the problem is an LP.

2. The objective separates over $k$: for each $k$ choose $(t_{1k},t_{2k})$ on the segment $t_{1k}+t_{2k}=1$ to minimize $t_{2k}p_k+t_{1k}\lambda q_k$.

3. A linear function on a segment is minimized at an endpoint: $t_{1k}=1$ if $\lambda q_k\le p_k$, and $t_{2k}=1$ otherwise.

:::

::: {#rmk-statistical-estimation-1 .remark name="MAP estimation"}

With a prior density $p_{\rm prior}(x)$, the maximum a posteriori estimate maximizes $\log p_x(y)+\log p_{\rm prior}(x)$. A log-concave prior keeps the problem convex; a Gaussian prior adds a Tikhonov term (@def-regularized-approximation).

:::
