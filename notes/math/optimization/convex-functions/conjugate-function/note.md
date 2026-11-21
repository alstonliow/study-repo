---
title: "The Conjugate Function"
sources: [ee364a-3]
requires: [math/optimization/convex-functions/operations-preserving-convex-functions]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on convex functions, in our own wording; proofs written out in steps. Examples checked with sympy. -->

The conjugate of $f$ records, for each slope $y$, how far the linear function $y^{\mathsf T}x$ can rise above $f$. It is always convex, and it is the bridge between a problem and its Lagrange dual (@sec-math-optimization-duality-lagrange-dual-function).

::: {#def-conjugate-function .definition name="Conjugate function"}

The *conjugate* of $f:\mathbb{R}^n\to\mathbb{R}$ is
$$f^*(y)=\sup_{x\in\operatorname{dom}f}\big(y^{\mathsf T}x-f(x)\big),$$
with $\operatorname{dom}f^*$ the set of $y$ where the supremum is finite. $f^*$ is convex whether or not $f$ is, being a supremum of affine functions of $y$ (@prp-pointwise-supremum).

:::

::: {#exm-conjugates .example name="Conjugates of standard functions"}

1. $f(x)=-\log x$ on $x>0$: $xy+\log x$ is unbounded above for $y\ge0$; for $y<0$ its maximum is at $x=-1/y$, giving $f^*(y)=-1-\log(-y)$ on $y<0$.

2. $f(x)=\frac12x^{\mathsf T}Qx$ with $Q\succ0$: the maximizer of $y^{\mathsf T}x-\frac12x^{\mathsf T}Qx$ is $x=Q^{-1}y$, so $f^*(y)=\frac12y^{\mathsf T}Q^{-1}y$.

3. $f(x)=e^x$: $f^*(y)=y\log y-y$ for $y>0$, $f^*(0)=0$, and $+\infty$ for $y<0$.

4. The indicator $I_C$ of a set ($0$ on $C$, $+\infty$ off it) has conjugate the support function $\sup_{x\in C}y^{\mathsf T}x$.

5. A norm $f(x)=\lVert x\rVert$ has $f^*=I_{\{y\mid\lVert y\rVert_*\le1\}}$, the indicator of the dual-norm unit ball (@exm-dual-cones).

:::

::: {#prp-fenchel-young .proposition name="Fenchel's inequality"}

For all $x\in\operatorname{dom}f$ and $y$,
$$f(x)+f^*(y)\ge x^{\mathsf T}y.$$
For example $\frac12x^{\mathsf T}Qx+\frac12y^{\mathsf T}Q^{-1}y\ge x^{\mathsf T}y$ for $Q\succ0$.

:::

::: {.proof}

1. By definition $f^*(y)\ge y^{\mathsf T}x-f(x)$ for each $x\in\operatorname{dom}f$.

:::

::: {#prp-conjugate-properties .proposition name="Rules for conjugates"}

1. If $g(x)=f(Ax+b)$ with $A$ invertible, then $g^*(y)=f^*(A^{-\mathsf T}y)-b^{\mathsf T}A^{-\mathsf T}y$.

2. If $f(u,v)=f_1(u)+f_2(v)$, then $f^*(w,z)=f_1^*(w)+f_2^*(z)$.

3. If $f$ is convex and closed (its epigraph is closed), then $f^{**}=f$.

:::

::: {.proof}

1. Substitute $u=Ax+b$: $g^*(y)=\sup_u\big(y^{\mathsf T}A^{-1}(u-b)-f(u)\big)=\sup_u\big((A^{-\mathsf T}y)^{\mathsf T}u-f(u)\big)-y^{\mathsf T}A^{-1}b$.

2. The supremum of $w^{\mathsf T}u+z^{\mathsf T}v-f_1(u)-f_2(v)$ over $(u,v)$ splits into two independent suprema.

3. $f^{**}\le f$ by Fenchel's inequality. For the reverse, a closed convex epigraph is the intersection of the closed halfspaces containing it (strict separation, @def-strict-separation); the nonvertical ones are epigraphs of affine minorants $y^{\mathsf T}x-c$ with $c\ge f^*(y)$, and their supremum is $f^{**}$. (This step is a sketch: showing that the nonvertical halfspaces suffice takes one more separation argument.)

:::

::: {#rmk-conjugate-function-1 .remark name="Geometric picture"}

For a fixed slope $y$, $-f^*(y)$ is the intercept of the highest line $x\mapsto y^{\mathsf T}x-c$ lying below the graph of $f$. When $f$ is differentiable and convex, the supremum is attained where $\nabla f(x)=y$, so $f^*(y)=x^{\mathsf T}\nabla f(x)-f(x)$ at that point (the Legendre transform).

:::
