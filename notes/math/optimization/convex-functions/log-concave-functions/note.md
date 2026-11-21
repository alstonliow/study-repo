---
title: "Log-Concave and Log-Convex Functions"
sources: [ee364a-3]
requires: [math/optimization/convex-functions/operations-preserving-convex-functions]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on convex functions, in our own wording; proofs written out in steps; the integration property is stated without proof. -->

Many probability densities are log-concave, and log-concavity survives multiplication, marginalization and convolution. This makes probabilities of convex events behave well in optimization.

::: {#def-log-concave .definition name="Log-concave function"}

A positive function $f$ with convex domain is *log-concave* if $\log f$ is concave, equivalently
$$f(\theta x+(1-\theta)y)\ge f(x)^\theta f(y)^{1-\theta}\qquad\text{for }0\le\theta\le1.$$
It is *log-convex* if $\log f$ is convex.

:::

::: {#exm-log-concave .example name="Log-concave functions"}

1. $x^a$ on $x>0$ is log-concave for $a\ge0$ and log-convex for $a\le0$; $e^{ax}$ is both.

2. The normal density $\frac{1}{\sqrt{(2\pi)^n\det\Sigma}}e^{-\frac12(x-\bar x)^{\mathsf T}\Sigma^{-1}(x-\bar x)}$ is log-concave, as is the indicator of a convex set (with $\log0=-\infty$).

3. The Gaussian cumulative distribution $\Phi(x)=\frac1{\sqrt{2\pi}}\int_{-\infty}^xe^{-u^2/2}\,du$ is log-concave (from the integration property below).

:::

::: {#prp-log-concave-second-order .proposition name="Second-order condition"}

A twice differentiable positive $f$ with convex domain is log-concave if and only if
$$f(x)\nabla^2f(x)\preceq\nabla f(x)\nabla f(x)^{\mathsf T}\qquad\text{for all }x\in\operatorname{dom}f.$$

:::

::: {.proof}

1. $\nabla^2\log f=\frac{1}{f}\nabla^2f-\frac1{f^2}\nabla f\nabla f^{\mathsf T}$.

2. Multiplying by $f^2>0$, $\nabla^2\log f\preceq0$ is the stated inequality; apply the second-order test (@prp-convex-second-derivative) to $-\log f$.

:::

::: {#prp-log-concave-operations .proposition name="Products, marginals and convolutions"}

1. A product of log-concave functions is log-concave.

2. A sum of log-concave functions need not be log-concave.

3. (Integration) If $f(x,y)$ is log-concave in $(x,y)$, then $g(x)=\int f(x,y)\,dy$ is log-concave.

4. Consequently the convolution $(f*g)(x)=\int f(x-y)g(y)\,dy$ of log-concave functions is log-concave.

:::

::: {.proof}

1. $\log(fg)=\log f+\log g$ is a sum of concave functions.

2. $h(x)=e^{-x^2/2}+e^{-(x-4)^2/2}$ is a sum of log-concave functions, but $h(2)=2e^{-2}\approx0.271$ is less than $\sqrt{h(0)h(4)}=1+e^{-8}\approx1.0003$, violating the defining inequality with $\theta=\frac12$.

3. The integration property is the Prékopa–Leindler theorem; we state it without proof.

4. $f(x-y)g(y)$ is log-concave in $(x,y)$ by part 1 (each factor is a log-concave function composed with a linear map), so part 3 applies.

:::

::: {#exm-yield-function .example name="Manufacturing yield"}

A part is made to target dimensions $x$, but the actual dimensions are $x+w$ with random $w$ of log-concave density $p$. If acceptable parts form a convex set $S$, the yield $Y(x)=\operatorname{P}(x+w\in S)=\int I_S(x+w)p(w)\,dw$ is log-concave in $x$ by @prp-log-concave-operations. So the set of targets with yield at least $\alpha$, $\{x\mid Y(x)\ge\alpha\}$, is convex.

:::

::: {#def-k-convex .definition name="Convexity with respect to a generalized inequality"}

For a proper cone $K$, $f:\mathbb{R}^n\to\mathbb{R}^m$ is *$K$-convex* if
$$f(\theta x+(1-\theta)y)\preceq_K\theta f(x)+(1-\theta)f(y)\qquad\text{for }0\le\theta\le1.$$
 With $K=\mathbb S^m_+$ the map $X\mapsto X^2$ is matrix convex: for any $z$, $z^{\mathsf T}X^2z=\lVert Xz\rVert_2^2$ is a convex function of $X$.

:::
