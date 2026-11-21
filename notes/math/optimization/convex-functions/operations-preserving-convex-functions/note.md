---
title: "Operations that Preserve Convexity of Functions"
sources: [ee364a-3]
requires: [math/optimization/convex-functions/convex-functions]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on convex functions, in our own wording; proofs written out in steps. -->

As for sets (@sec-math-optimization-convex-sets-operations-preserving-convex-sets), convexity of a function is usually shown by building it from known convex functions with operations that preserve convexity.

::: {#prp-nonnegative-sum-affine-composition .proposition name="Nonnegative sums and affine composition"}

If $f_1,\dots,f_m$ are convex and $w_i\ge0$, then $\sum_iw_if_i$ is convex. If $f$ is convex then $g(x)=f(Ax+b)$ is convex. Example: $\lVert Ax+b\rVert$ and $-\sum_{i=1}^m\log(b_i-a_i^{\mathsf T}x)$ (on $\{x\mid a_i^{\mathsf T}x<b_i\}$) are convex.

:::

::: {.proof}

1. Sum: add the inequalities $w_if_i(\theta x+(1-\theta)y)\le w_i\theta f_i(x)+w_i(1-\theta)f_i(y)$.

2. Affine composition: $A(\theta x+(1-\theta)y)+b=\theta(Ax+b)+(1-\theta)(Ay+b)$, so the inequality for $f$ at the images is the inequality for $g$; the domain $\{x\mid Ax+b\in\operatorname{dom}f\}$ is convex by @prp-affine-image-convex.

:::

::: {#prp-pointwise-supremum .proposition name="Pointwise maximum and supremum"}

If $f(x,y)$ is convex in $x$ for each $y\in\mathcal A$, then $g(x)=\sup_{y\in\mathcal A}f(x,y)$ is convex. Examples: the piecewise-linear function $\max_i(a_i^{\mathsf T}x+b_i)$; the sum of the $r$ largest components of $x$; the support function $S_C(x)=\sup_{y\in C}y^{\mathsf T}x$; the largest eigenvalue $\lambda_{\max}(X)=\sup_{\lVert y\rVert_2=1}y^{\mathsf T}Xy$.

:::

::: {.proof}

1. $\operatorname{epi}g=\bigcap_{y\in\mathcal A}\operatorname{epi}f(\cdot,y)$, since $g(x)\le t$ iff $f(x,y)\le t$ for all $y$.

2. An intersection of convex sets is convex (@prp-intersection-convex), so $g$ is convex by @prp-epigraph-convex.

3. The sum of the $r$ largest components is the maximum of $x_{i_1}+\cdots+x_{i_r}$ over all index sets of size $r$, a maximum of linear functions.

:::

::: {#prp-scalar-composition-rules .proposition name="Composition with a scalar function"}

Let $f(x)=h(g(x))$ with $g:\mathbb{R}^n\to\mathbb{R}$ and $h:\mathbb{R}\to\mathbb{R}$, and let $\tilde h$ be the extended-value extension of $h$. Then $f$ is convex if

- $g$ is convex, $h$ is convex and $\tilde h$ is nondecreasing; or
- $g$ is concave, $h$ is convex and $\tilde h$ is nonincreasing.

Examples: $e^{g(x)}$ is convex if $g$ is convex; $1/g(x)$ is convex if $g$ is concave and positive.

:::

::: {.proof}

1. For differentiable $g,h$ and $n=1$: $f''=h''(g)\,g'^2+h'(g)\,g''$. In the first case $h''\ge0$, $h'\ge0$, $g''\ge0$; in the second $h''\ge0$, $h'\le0$, $g''\le0$. Either way $f''\ge0$.

2. In general, first case: for $x,y\in\operatorname{dom}f$, convexity of $g$ gives $g(\theta x+(1-\theta)y)\le\theta g(x)+(1-\theta)g(y)$. As $\tilde h$ is nondecreasing, $f(\theta x+(1-\theta)y)\le\tilde h(\theta g(x)+(1-\theta)g(y))$, and convexity of $h$ bounds this by $\theta f(x)+(1-\theta)f(y)$. The point $\theta g(x)+(1-\theta)g(y)$ lies in $\operatorname{dom}h$ because $\operatorname{dom}h$ is an interval containing $g(x)$ and $g(y)$, so $\operatorname{dom}f$ is convex as well.

3. The second case is the same with the inequality for $g$ reversed and $\tilde h$ nonincreasing.

:::

::: {#rmk-operations-preserving-convex-functions-1 .remark name="Vector composition"}

The same rule holds for $f(x)=h(g_1(x),\dots,g_k(x))$ with $h:\mathbb{R}^k\to\mathbb{R}$ convex: $f$ is convex if, for each $i$, either $g_i$ is convex and $\tilde h$ is nondecreasing in argument $i$, or $g_i$ is concave and $\tilde h$ is nonincreasing in argument $i$ (or $g_i$ is affine). For instance $\log\sum_ie^{g_i(x)}$ is convex when every $g_i$ is convex.

:::

::: {#prp-partial-minimization .proposition name="Minimization over some variables"}

If $f(x,y)$ is jointly convex in $(x,y)$ and $C$ is a nonempty convex set, then $g(x)=\inf_{y\in C}f(x,y)$ is convex, provided $g(x)>-\infty$ for some $x$. Example: the distance $\operatorname{dist}(x,S)=\inf_{y\in S}\lVert x-y\rVert$ to a convex set $S$ is convex.

:::

::: {.proof}

1. Take $x_1,x_2\in\operatorname{dom}g$ and $\epsilon>0$. Choose $y_i\in C$ with $f(x_i,y_i)\le g(x_i)+\epsilon$.

2. Then $\theta y_1+(1-\theta)y_2\in C$ and
$$g(\theta x_1+(1-\theta)x_2)\le f\big(\theta(x_1,y_1)+(1-\theta)(x_2,y_2)\big)\le\theta f(x_1,y_1)+(1-\theta)f(x_2,y_2)\le\theta g(x_1)+(1-\theta)g(x_2)+\epsilon.$$

3. Let $\epsilon\to0$.

:::

::: {#exm-schur-complement-convex .example name="Schur complement"}

Let $f(x,y)=x^{\mathsf T}Ax+2x^{\mathsf T}By+y^{\mathsf T}Cy$ with $\begin{bmatrix}A&B\\B^{\mathsf T}&C\end{bmatrix}\succeq0$ and $C\succ0$. Minimizing over $y$ (set the gradient $2B^{\mathsf T}x+2Cy$ to zero, $y=-C^{-1}B^{\mathsf T}x$) gives $g(x)=x^{\mathsf T}(A-BC^{-1}B^{\mathsf T})x$. As $f$ is jointly convex, $g$ is convex, so the Schur complement $A-BC^{-1}B^{\mathsf T}$ is positive semidefinite.

:::

::: {#def-perspective-of-function .definition name="Perspective of a function"}

The *perspective* of $f:\mathbb{R}^n\to\mathbb{R}$ is
$$g(x,t)=t\,f(x/t),\qquad\operatorname{dom}g=\{(x,t)\mid x/t\in\operatorname{dom}f,\ t>0\}.$$
If $f$ is convex then $g$ is convex: $(x,t,s)\in\operatorname{epi}g$ iff $(x/t,s/t)\in\operatorname{epi}f$, so $\operatorname{epi}g$ is the preimage of $\operatorname{epi}f$ under a perspective map (@prp-perspective-preserves-convexity). Examples: $x^{\mathsf T}x/t$ and the relative entropy $t\log t-t\log x$ on $x,t>0$.

:::
