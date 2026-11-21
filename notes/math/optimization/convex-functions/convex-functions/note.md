---
title: "Convex Functions"
sources: [ee364a-3]
requires: [math/optimization/convex-sets/operations-preserving-convex-sets, math/calculus/multivariable/differentiation/gradient]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on convex functions, in our own wording; proofs written out in steps. The basic definition and the second-order test are already in @sec-ai-machine-learning-convex-optimization; this note adds domains, the first-order condition, epigraphs and Jensen's inequality. -->

A convex function (@def-convex-function) lies below its chords. In optimization a function comes with its domain, convexity can be checked on lines, by the gradient or by the Hessian, and it is equivalent to convexity of the epigraph.

::: {#def-extended-value-extension .definition name="Domain, extended-value extension" related="def-convex-function"}

A function $f:\mathbb{R}^n\to\mathbb{R}$ is convex if $\operatorname{dom}f$ is convex and
$$f(\theta x+(1-\theta)y)\le\theta f(x)+(1-\theta)f(y)\qquad\text{for } x,y\in\operatorname{dom}f,\ 0\le\theta\le1.$$
It is *concave* if $-f$ is convex. Its *extended-value extension* is $\tilde f(x)=f(x)$ on $\operatorname{dom}f$ and $+\infty$ elsewhere; with the rule $\theta\cdot\infty=\infty$ the inequality above then holds for all $x,y\in\mathbb{R}^n$ exactly when $f$ is convex.

:::

::: {#exm-convex-functions-basic .example name="Basic convex and concave functions"}

On $\mathbb{R}$: $e^{ax}$; $x^a$ on $x>0$ for $a\ge1$ or $a\le0$ (concave for $0\le a\le1$); $\lvert x\rvert^p$ for $p\ge1$; $x\log x$ on $x>0$; $\log x$ is concave. On $\mathbb{R}^n$: every affine function is both convex and concave; every norm is convex. On $\mathbb{R}^{m\times n}$: $\operatorname{tr}(A^{\mathsf T}X)+b$ is affine; the spectral norm $\lVert X\rVert_2=\sigma_{\max}(X)$ is convex.

:::

::: {#prp-convex-restriction-to-line .proposition name="Restriction to a line"}

$f$ is convex if and only if, for every $x\in\operatorname{dom}f$ and $v$, the function $g(t)=f(x+tv)$ is convex on $\{t\mid x+tv\in\operatorname{dom}f\}$.

:::

::: {.proof}

1. The defining inequality involves only points of one segment, and a segment lies on a line; conversely every segment of $\operatorname{dom}f$ lies on a line through one of its points.

:::

::: {#exm-log-det-concave .example name="$\log\det$ is concave"}

Let $f(X)=\log\det X$ on $\mathbb S^n_{++}$, $X\succ0$ and $V\in\mathbb S^n$. With $X^{1/2}$ the positive square root and $\lambda_i$ the eigenvalues of $X^{-1/2}VX^{-1/2}$,
$$g(t)=\log\det(X+tV)=\log\det X+\log\det\big(I+tX^{-1/2}VX^{-1/2}\big)=\log\det X+\sum_i\log(1+t\lambda_i),$$
a sum of concave functions of $t$. By @prp-convex-restriction-to-line, $f$ is concave.

:::

::: {#thm-first-order-convexity .theorem name="First-order condition"}

Let $f$ be differentiable with open convex domain. Then $f$ is convex if and only if
$$f(y)\ge f(x)+\nabla f(x)^{\mathsf T}(y-x)\qquad\text{for all }x,y\in\operatorname{dom}f.$$
The first-order Taylor approximation is a global underestimator.

:::

::: {.proof}

1. One variable first. If $f$ is convex and $0<t\le1$, then $f(x+t(y-x))\le(1-t)f(x)+tf(y)$, so $f(y)\ge f(x)+\frac{f(x+t(y-x))-f(x)}{t}$. Let $t\to0$ to get $f(y)\ge f(x)+f'(x)(y-x)$.

2. Conversely, assume the inequality and let $z=\theta x+(1-\theta)y$. Apply it at $z$ twice: $f(x)\ge f(z)+f'(z)(x-z)$ and $f(y)\ge f(z)+f'(z)(y-z)$. Multiply by $\theta$ and $1-\theta$ and add; the derivative terms cancel because $\theta(x-z)+(1-\theta)(y-z)=0$. This gives $\theta f(x)+(1-\theta)f(y)\ge f(z)$.

3. Several variables. Put $g(t)=f(ty+(1-t)x)$, so $g'(t)=\nabla f(ty+(1-t)x)^{\mathsf T}(y-x)$. If $f$ is convex then $g$ is convex (@prp-convex-restriction-to-line), and step 1 with $g(1)\ge g(0)+g'(0)$ is the inequality.

4. Conversely, if the inequality holds for $f$, then for any two points on the line it holds for $g$, so $g$ is convex by step 2 for every line, and $f$ is convex.

:::

::: {#cor-convex-stationary-global .corollary name="Stationary points are global minima"}

If $f$ is convex and differentiable and $\nabla f(x)=0$, then $f(y)\ge f(x)$ for all $y\in\operatorname{dom}f$.

:::

::: {#rmk-convex-functions-1 .remark name="Second-order condition"}

For twice differentiable $f$ with open convex domain, $f$ is convex iff $\nabla^2f(x)\succeq0$ on $\operatorname{dom}f$ (@prp-convex-second-derivative). If $\nabla^2f(x)\succ0$ everywhere then $f$ is strictly convex, but not conversely: $x^4$ is strictly convex with $f''(0)=0$.

:::

::: {#exm-convex-by-hessian .example name="Quadratic-over-linear and log-sum-exp"}

1. $f(x,y)=x^2/y$ on $y>0$ has $\nabla^2f=\frac{2}{y^3}\begin{bmatrix}y\\-x\end{bmatrix}\begin{bmatrix}y\\-x\end{bmatrix}^{\mathsf T}\succeq0$, so it is convex.

2. $f(x)=\log\sum_{k}e^{x_k}$ has, with $z_k=e^{x_k}$, $\nabla^2f=\frac{1}{\mathbf 1^{\mathsf T}z}\operatorname{diag}(z)-\frac{1}{(\mathbf 1^{\mathsf T}z)^2}zz^{\mathsf T}$. For any $v$, $v^{\mathsf T}\nabla^2f\,v=\frac{(\sum_kz_kv_k^2)(\sum_kz_k)-(\sum_kv_kz_k)^2}{(\sum_kz_k)^2}\ge0$ by Cauchy–Schwarz applied to $(\sqrt{z_k}v_k)$ and $(\sqrt{z_k})$. So log-sum-exp is convex.

3. The geometric mean $(\prod_kx_k)^{1/n}$ is concave on $\mathbb{R}^n_{++}$ by a similar computation.

:::

::: {#def-epigraph-sublevel-set .definition name="Sublevel set, epigraph"}

The *$\alpha$-sublevel set* of $f$ is $C_\alpha=\{x\in\operatorname{dom}f\mid f(x)\le\alpha\}$, and the *epigraph* is
$$\operatorname{epi}f=\{(x,t)\in\mathbb{R}^{n+1}\mid x\in\operatorname{dom}f,\ f(x)\le t\}.$$

:::

::: {#prp-epigraph-convex .proposition name="Convexity and the epigraph"}

$f$ is convex if and only if $\operatorname{epi}f$ is a convex set. Sublevel sets of a convex function are convex; the converse fails ($-e^x$ has convex sublevel sets but is not convex).

:::

::: {.proof}

1. If $f$ is convex and $(x,s),(y,t)\in\operatorname{epi}f$, then $f(\theta x+(1-\theta)y)\le\theta f(x)+(1-\theta)f(y)\le\theta s+(1-\theta)t$.

2. If the epigraph is convex, apply this to the points $(x,f(x))$ and $(y,f(y))$; their combination lies in $\operatorname{epi}f$, which is the convexity inequality.

3. Sublevel sets: if $f(x),f(y)\le\alpha$ then $f(\theta x+(1-\theta)y)\le\alpha$.

:::

::: {#thm-jensen-inequality .theorem name="Jensen's inequality"}

If $f$ is convex, $x_1,\dots,x_k\in\operatorname{dom}f$ and $\theta_i\ge0$ with $\sum_i\theta_i=1$, then
$$f\Big(\sum_i\theta_ix_i\Big)\le\sum_i\theta_if(x_i).$$
More generally $f(\operatorname{E}z)\le\operatorname{E}f(z)$ for any random variable $z$ with values in $\operatorname{dom}f$ for which the expectations exist.

:::

::: {.proof}

1. The points $(x_i,f(x_i))$ lie in the convex set $\operatorname{epi}f$, so their convex combination $(\sum_i\theta_ix_i,\sum_i\theta_if(x_i))$ does too (@prp-convex-hull-smallest).

2. Membership in the epigraph is the inequality.

3. The expectation form for finitely many values is the same statement; the general case follows from the first-order condition at $x=\operatorname{E}z$ when $f$ is differentiable, $f(z)\ge f(\operatorname{E}z)+\nabla f(\operatorname{E}z)^{\mathsf T}(z-\operatorname{E}z)$, by taking expectations.

:::

::: {#exm-jensen-am-gm .example name="Arithmetic–geometric mean inequality"}

Jensen for the concave function $\log$ with weights $\theta,1-\theta$ gives $\log(\theta a+(1-\theta)b)\ge\theta\log a+(1-\theta)\log b$, that is,
$$a^\theta b^{1-\theta}\le\theta a+(1-\theta)b\qquad(a,b\ge0,\ 0\le\theta\le1).$$
With $\theta=\tfrac12$: $\sqrt{ab}\le\tfrac{a+b}{2}$.

:::
