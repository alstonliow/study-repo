---
title: "Generalized Inequalities"
sources: [ee364a-2]
requires: [math/optimization/convex-sets/examples-of-convex-sets]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on convex sets, in our own wording; proofs written out in steps. -->

A proper cone turns $\mathbb{R}^n$ (or $\mathbb S^n$) into a partially ordered space. Componentwise inequality of vectors and the semidefinite order of symmetric matrices are the two orders used most.

::: {#def-proper-cone .definition name="Proper cone, generalized inequality"}

A convex cone $K\subseteq\mathbb{R}^n$ is *proper* if it is closed, has nonempty interior (is solid) and contains no line ($x\in K$, $-x\in K$ imply $x=0$). A proper cone defines the *generalized inequalities*
$$x\preceq_Ky\iff y-x\in K,\qquad x\prec_Ky\iff y-x\in\operatorname{int}K.$$

:::

::: {#exm-proper-cones .example name="Standard proper cones"}

1. $K=\mathbb{R}^n_+$: $x\preceq_Ky$ means $x_i\le y_i$ for all $i$, written $x\preceq y$.

2. $K=\mathbb S^n_+$: $X\preceq_KY$ means $Y-X$ is positive semidefinite, written $X\preceq Y$.

3. The cone of polynomials $c_1+c_2t+\cdots+c_nt^{n-1}$ nonnegative on $[0,1]$, $K=\{c\in\mathbb{R}^n\mid c_1+c_2t+\cdots+c_nt^{n-1}\ge0\ \text{for}\ t\in[0,1]\}$.

:::

::: {#prp-generalized-inequality-properties .proposition name="Properties of generalized inequalities"}

For a proper cone $K$, $\preceq_K$ is a partial order compatible with addition and nonnegative scaling:
$$x\preceq_Ky,\ u\preceq_Kv\Rightarrow x+u\preceq_Ky+v;\qquad x\preceq_Ky,\ \alpha\ge0\Rightarrow\alpha x\preceq_K\alpha y.$$
It is not in general a total order: two vectors need not be comparable.

:::

::: {.proof}

1. Reflexive: $x-x=0\in K$ since $K$ is a closed cone. Antisymmetric: $y-x\in K$ and $x-y\in K$ force $y-x=0$ as $K$ contains no line. Transitive: $z-x=(z-y)+(y-x)\in K$ as $K$ is a convex cone.

2. Addition: $(y+v)-(x+u)=(y-x)+(v-u)\in K$. Scaling: $\alpha(y-x)\in K$.

3. In $\mathbb{R}^2_+$, neither $(1,0)\preceq(0,1)$ nor $(0,1)\preceq(1,0)$.

:::

::: {#def-minimum-minimal-element .definition name="Minimum and minimal elements"}

Let $S$ be a set and $K$ a proper cone. A point $x\in S$ is the *minimum element* of $S$ (with respect to $\preceq_K$) if $x\preceq_Ky$ for every $y\in S$, that is, $S\subseteq x+K$. It is a *minimal element* if no other point of $S$ is below it: $y\in S$, $y\preceq_Kx$ imply $y=x$, that is, $(x-K)\cap S=\{x\}$.

:::

::: {#exm-minimum-vs-minimal .example name="Minimal but not minimum"}

With $K=\mathbb{R}^2_+$, the segment $S$ from $(0,1)$ to $(1,0)$ has every point minimal (moving down-left leaves $S$) but no minimum element. The square $[0,1]^2$ has minimum element $(0,0)$.

:::

::: {#rmk-generalized-inequalities-1 .remark name="Minimum is unique"}

A minimum element, when it exists, is unique and is also the only minimal element: two minima $x,x'$ satisfy $x\preceq_Kx'$ and $x'\preceq_Kx$, so $x=x'$ by antisymmetry.

:::
