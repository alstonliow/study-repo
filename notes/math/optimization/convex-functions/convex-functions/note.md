---
title: "Convex Functions"
sources: [ee364a-3, mit18065-21]
requires: [math/optimization/convex-sets/operations-preserving-convex-sets, math/calculus/multivariable/differentiation/gradient]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on convex functions, in our own wording; proofs written out in steps. The second-order test is in @sec-ai-machine-learning-convex-optimization. -->
<!-- Merged 2026-11-21 (owner approval): def-convex-function moved here from @sec-ai-machine-learning-convex-optimization (MIT 18.065, Lecture 21) and combined with the EE364A definition (domain, extended-value extension), which replaces def-extended-value-extension; chord wording and strict convexity from 18.065, domain and extension from EE364A. -->

A convex function lies below its chords. In optimization a function comes with its domain, convexity can be checked on lines, by the gradient or by the Hessian, and it is equivalent to convexity of the epigraph.

::: {#def-convex-function .definition name="Convex function"}

A function $f:\mathbb{R}^n\to\mathbb{R}$ is *convex* if $\operatorname{dom}f$ is convex and
$$f(\theta x+(1-\theta)y)\le\theta f(x)+(1-\theta)f(y)\qquad\text{for } x,y\in\operatorname{dom}f,\ 0\le\theta\le1,$$
that is, the graph lies below every chord. It is *strictly convex* if the inequality is strict for $x\ne y$ and $0<\theta<1$, and *concave* if $-f$ is convex. Its *extended-value extension* is $\tilde f(x)=f(x)$ on $\operatorname{dom}f$ and $+\infty$ elsewhere; with the rule $\theta\cdot\infty=\infty$ the inequality above then holds for all $x,y\in\mathbb{R}^n$ exactly when $f$ is convex.

:::

::: {#fig-convex-functions-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-2.2,0) -- (3.2,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.3) -- (0,2.8) node[lab, above] {$y$};
\draw[emph] (-2,2.2) -- (-1.92,2.07) -- (-1.84,1.95) -- (-1.75,1.83) -- (-1.67,1.71) -- (-1.59,1.61) -- (-1.51,1.5) -- (-1.43,1.4) -- (-1.35,1.3) -- (-1.27,1.21) -- (-1.18,1.13) -- (-1.1,1.05) -- (-1.02,0.97) -- (-0.94,0.9) -- (-0.86,0.83) -- (-0.77,0.77) -- (-0.69,0.71) -- (-0.61,0.65) -- (-0.53,0.6) -- (-0.45,0.56) -- (-0.37,0.52) -- (-0.28,0.49) -- (-0.2,0.46) -- (-0.12,0.43) -- (-0.04,0.41) -- (0.04,0.39) -- (0.12,0.38) -- (0.21,0.37) -- (0.29,0.37) -- (0.37,0.37) -- (0.45,0.38) -- (0.53,0.39) -- (0.61,0.41) -- (0.7,0.43) -- (0.78,0.46) -- (0.86,0.49) -- (0.94,0.52) -- (1.02,0.56) -- (1.1,0.61) -- (1.19,0.65) -- (1.27,0.71) -- (1.35,0.77) -- (1.43,0.83) -- (1.51,0.9) -- (1.59,0.97) -- (1.68,1.05) -- (1.76,1.13) -- (1.84,1.22) -- (1.92,1.31) -- (2,1.4) -- (2.08,1.5) -- (2.17,1.61) -- (2.25,1.72) -- (2.33,1.83) -- (2.41,1.95) -- (2.49,2.07) -- (2.57,2.2) -- (2.66,2.34) -- (2.74,2.47) -- (2.82,2.62) -- (2.9,2.76);
\draw[hl] (-1.6,1.62) -- (2.4,1.94);
\fill[ink] (-1.6,1.62) circle[pt] node[lab, left] {$(x,f(x))$};
\fill[ink] (2.4,1.94) circle[pt] node[lab, right] {$(y,f(y))$};
\draw[faint, dashed] (0.8,0) -- (0.8,1.81);
\fill[ink] (0.8,0.46) circle[pt];
\fill[accent] (0.8,1.81) circle[pt];
\node[lab] at (0.8,-0.25) {$\theta x+(1-\theta)y$};
\end{tikzpicture}
\end{center}
```

Convexity: the chord between $(x,f(x))$ and $(y,f(y))$ lies on or above the graph, so at $\theta x+(1-\theta)y$ the function value is at most $\theta f(x)+(1-\theta)f(y)$.

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

::: {#fig-convex-functions-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-2.2,0) -- (3.2,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.6) -- (0,2.8) node[lab, above] {$y$};
\draw[emph] (-2,2.2) -- (-1.92,2.07) -- (-1.84,1.95) -- (-1.75,1.83) -- (-1.67,1.71) -- (-1.59,1.61) -- (-1.51,1.5) -- (-1.43,1.4) -- (-1.35,1.3) -- (-1.27,1.21) -- (-1.18,1.13) -- (-1.1,1.05) -- (-1.02,0.97) -- (-0.94,0.9) -- (-0.86,0.83) -- (-0.77,0.77) -- (-0.69,0.71) -- (-0.61,0.65) -- (-0.53,0.6) -- (-0.45,0.56) -- (-0.37,0.52) -- (-0.28,0.49) -- (-0.2,0.46) -- (-0.12,0.43) -- (-0.04,0.41) -- (0.04,0.39) -- (0.12,0.38) -- (0.21,0.37) -- (0.29,0.37) -- (0.37,0.37) -- (0.45,0.38) -- (0.53,0.39) -- (0.61,0.41) -- (0.7,0.43) -- (0.78,0.46) -- (0.86,0.49) -- (0.94,0.52) -- (1.02,0.56) -- (1.1,0.61) -- (1.19,0.65) -- (1.27,0.71) -- (1.35,0.77) -- (1.43,0.83) -- (1.51,0.9) -- (1.59,0.97) -- (1.68,1.05) -- (1.76,1.13) -- (1.84,1.22) -- (1.92,1.31) -- (2,1.4) -- (2.08,1.5) -- (2.17,1.61) -- (2.25,1.72) -- (2.33,1.83) -- (2.41,1.95) -- (2.49,2.07) -- (2.57,2.2) -- (2.66,2.34) -- (2.74,2.47) -- (2.82,2.62) -- (2.9,2.76);
\draw[hl] (-1.6,-0.75) -- (0.65,0.38) -- (2.9,1.5);
\fill[ink] (1,0.55) circle[pt] node[lab, above left] {$(x,f(x))$};
\node[lab, right] at (2.6,0.95) {$f(x)+\nabla f(x)^{\mathsf T}(y-x)$};
\end{tikzpicture}
\end{center}
```

First-order condition: the tangent at any point is a global underestimator of a differentiable convex function. Local slope information gives a bound valid everywhere.

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

::: {#fig-convex-functions-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-2.2,0) -- (3.2,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.3) -- (0,2.9) node[lab, above] {$y$};
\fill[tintA] (-2,2.2) -- (-1.92,2.07) -- (-1.84,1.95) -- (-1.75,1.83) -- (-1.67,1.71) -- (-1.59,1.61) -- (-1.51,1.5) -- (-1.43,1.4) -- (-1.35,1.3) -- (-1.27,1.21) -- (-1.18,1.13) -- (-1.1,1.05) -- (-1.02,0.97) -- (-0.94,0.9) -- (-0.86,0.83) -- (-0.77,0.77) -- (-0.69,0.71) -- (-0.61,0.65) -- (-0.53,0.6) -- (-0.45,0.56) -- (-0.37,0.52) -- (-0.28,0.49) -- (-0.2,0.46) -- (-0.12,0.43) -- (-0.04,0.41) -- (0.04,0.39) -- (0.12,0.38) -- (0.21,0.37) -- (0.29,0.37) -- (0.37,0.37) -- (0.45,0.38) -- (0.53,0.39) -- (0.61,0.41) -- (0.7,0.43) -- (0.78,0.46) -- (0.86,0.49) -- (0.94,0.52) -- (1.02,0.56) -- (1.1,0.61) -- (1.19,0.65) -- (1.27,0.71) -- (1.35,0.77) -- (1.43,0.83) -- (1.51,0.9) -- (1.59,0.97) -- (1.68,1.05) -- (1.76,1.13) -- (1.84,1.22) -- (1.92,1.31) -- (2,1.4) -- (2.08,1.5) -- (2.17,1.61) -- (2.25,1.72) -- (2.33,1.83) -- (2.41,1.95) -- (2.49,2.07) -- (2.57,2.2) -- (2.66,2.34) -- (2.74,2.47) -- (2.82,2.62) -- (2.82,2.7) -- (-2,2.7) -- cycle;
\draw[emph] (-2,2.2) -- (-1.92,2.07) -- (-1.84,1.95) -- (-1.75,1.83) -- (-1.67,1.71) -- (-1.59,1.61) -- (-1.51,1.5) -- (-1.43,1.4) -- (-1.35,1.3) -- (-1.27,1.21) -- (-1.18,1.13) -- (-1.1,1.05) -- (-1.02,0.97) -- (-0.94,0.9) -- (-0.86,0.83) -- (-0.77,0.77) -- (-0.69,0.71) -- (-0.61,0.65) -- (-0.53,0.6) -- (-0.45,0.56) -- (-0.37,0.52) -- (-0.28,0.49) -- (-0.2,0.46) -- (-0.12,0.43) -- (-0.04,0.41) -- (0.04,0.39) -- (0.12,0.38) -- (0.21,0.37) -- (0.29,0.37) -- (0.37,0.37) -- (0.45,0.38) -- (0.53,0.39) -- (0.61,0.41) -- (0.7,0.43) -- (0.78,0.46) -- (0.86,0.49) -- (0.94,0.52) -- (1.02,0.56) -- (1.1,0.61) -- (1.19,0.65) -- (1.27,0.71) -- (1.35,0.77) -- (1.43,0.83) -- (1.51,0.9) -- (1.59,0.97) -- (1.68,1.05) -- (1.76,1.13) -- (1.84,1.22) -- (1.92,1.31) -- (2,1.4) -- (2.08,1.5) -- (2.17,1.61) -- (2.25,1.72) -- (2.33,1.83) -- (2.41,1.95) -- (2.49,2.07) -- (2.57,2.2) -- (2.66,2.34) -- (2.74,2.47) -- (2.82,2.62);
\draw[faint, dashed] (-2,1.2) -- (2.9,1.2) node[lab, right] {$\alpha$};
\draw[hl] (-1.25,0) -- (1.82,0);
\draw[faint] (-1.25,0) -- (-1.25,1.2) (1.82,0) -- (1.82,1.2);
\node[lab] at (0.5,2.2) {$\operatorname{epi}f$};
\node[lab] at (0.29,-0.25) {$C_\alpha$};
\end{tikzpicture}
\end{center}
```

The epigraph is the region on and above the graph (shaded); $f$ is convex exactly when it is a convex set. The sublevel set $C_\alpha$ is the interval where the graph is at or below the level $\alpha$.

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
