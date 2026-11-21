---
title: "Quasiconvex Functions"
sources: [ee364a-3]
requires: [math/optimization/convex-functions/convex-functions]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on convex functions, in our own wording; proofs written out in steps. -->

Quasiconvexity keeps only the part of convexity that matters for sublevel sets: every sublevel set is convex. Such functions can still be minimized by solving a sequence of convex feasibility problems (@sec-math-optimization-convex-problems-equivalent-problems).

::: {#def-quasiconvex .definition name="Quasiconvex function"}

$f:\mathbb{R}^n\to\mathbb{R}$ is *quasiconvex* if $\operatorname{dom}f$ is convex and every sublevel set
$$S_\alpha=\{x\in\operatorname{dom}f\mid f(x)\le\alpha\}$$
is convex. It is *quasiconcave* if $-f$ is quasiconvex, and *quasilinear* if it is both.

:::

::: {#exm-quasiconvex .example name="Quasiconvex functions"}

1. $\sqrt{\lvert x\rvert}$ on $\mathbb{R}$ is quasiconvex but not convex; $\log x$ on $x>0$ is quasilinear; $\lceil x\rceil$ is quasilinear.

2. $x_1x_2$ on $\mathbb{R}^2_{++}$ is quasiconcave: its superlevel sets $\{x_1x_2\ge\alpha\}$ are convex regions bounded by hyperbolas.

3. The linear-fractional $\frac{a^{\mathsf T}x+b}{c^{\mathsf T}x+d}$ on $c^{\mathsf T}x+d>0$ is quasilinear: its sublevel set $\{x\mid c^{\mathsf T}x+d>0,\ a^{\mathsf T}x+b\le\alpha(c^{\mathsf T}x+d)\}$ is an intersection of halfspaces, and so is each superlevel set.

4. The internal rate of return of a cash flow $x_0<0$, $x_1,\dots$ is quasiconcave: it is at least $R$ iff the present value $\sum_ix_i(1+r)^{-i}$ is positive for all $0\le r<R$, an intersection of halfspaces.

:::

::: {#prp-quasiconvex-jensen .proposition name="Modified Jensen inequality"}

$f$ with convex domain is quasiconvex if and only if
$$f(\theta x+(1-\theta)y)\le\max\{f(x),f(y)\}\qquad\text{for }0\le\theta\le1.$$

:::

::: {.proof}

1. If $f$ is quasiconvex, $x$ and $y$ lie in $S_\alpha$ for $\alpha=\max\{f(x),f(y)\}$, and so does the segment.

2. Conversely, if the inequality holds and $f(x),f(y)\le\alpha$, then every point between them has $f\le\alpha$, so $S_\alpha$ is convex.

:::

::: {#prp-quasiconvex-first-order .proposition name="First-order condition for quasiconvexity"}

Let $f$ be differentiable with convex domain. Then $f$ is quasiconvex if and only if
$$f(y)\le f(x)\ \Longrightarrow\ \nabla f(x)^{\mathsf T}(y-x)\le0.$$

:::

::: {.proof}

1. Suppose $f$ is quasiconvex and $f(y)\le f(x)$. For $0<t\le1$, $f(x+t(y-x))\le f(x)$ by @prp-quasiconvex-jensen, so the one-sided derivative $\nabla f(x)^{\mathsf T}(y-x)=\lim_{t\to0^+}\frac{f(x+t(y-x))-f(x)}{t}\le0$.

2. Conversely assume the condition, take $x,y\in\operatorname{dom}f$, put $g(t)=f(x+t(y-x))$, $M=\max\{g(0),g(1)\}$, and suppose the open set $U=\{t\in(0,1)\mid g(t)>M\}$ is nonempty.

3. For $t\in U$ let $z=x+t(y-x)$. Since $f(x)<f(z)$ and $f(y)<f(z)$, the condition at $z$ gives $\nabla f(z)^{\mathsf T}(x-z)\le0$ and $\nabla f(z)^{\mathsf T}(y-z)\le0$, that is, $-t\,g'(t)\le0$ and $(1-t)\,g'(t)\le0$. So $g'=0$ on $U$.

4. Let $(a,b)$ be a component of $U$. Then $g$ is constant, say $c>M$, on $(a,b)$, and $g(a)=c$ by continuity. But $a\notin U$, so either $a=0$ and $g(0)\le M$, or $a>0$ and $g(a)\le M$; both contradict $g(a)=c>M$. Hence $U$ is empty and @prp-quasiconvex-jensen holds.

:::

::: {#rmk-quasiconvex-functions-1 .remark name="Sums are not preserved"}

Unlike convex functions, a sum of quasiconvex functions need not be quasiconvex: $\sqrt{\lvert x\rvert}$ and $\sqrt{\lvert x-1\rvert}$ are quasiconvex, but their sum is $1$ at $x=0$ and $x=1$ and $\sqrt2>1$ at $x=\frac12$. Nonnegative weighted maxima and composition with nondecreasing functions are preserved.

:::
