---
title: "Examples of Convex Sets"
sources: [ee364a-2]
requires: [math/optimization/convex-sets/affine-and-convex-sets, math/linear-algebra/matrix-methods/matrix-norms]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on convex sets, in our own wording; proofs written out in steps. -->

Most convex sets met in practice are built from a few standard ones: hyperplanes and halfspaces, balls and ellipsoids, norm balls and norm cones, polyhedra, and the cone of positive semidefinite matrices.

::: {#def-hyperplane-halfspace .definition name="Hyperplane, halfspace"}

For $a\in\mathbb{R}^n$, $a\ne0$, and $b\in\mathbb{R}$,
$$\{x\mid a^{\mathsf T}x=b\}\ \text{is a hyperplane},\qquad \{x\mid a^{\mathsf T}x\le b\}\ \text{is a (closed) halfspace}.$$
The vector $a$ is the *normal* vector. A hyperplane is affine and convex; a halfspace is convex but not affine.

:::

::: {#def-ball-ellipsoid .definition name="Euclidean ball, ellipsoid"}

The Euclidean ball with centre $x_c$ and radius $r>0$ is $B(x_c,r)=\{x\mid\lVert x-x_c\rVert_2\le r\}=\{x_c+ru\mid\lVert u\rVert_2\le1\}$. For $P\in\mathbb S^n_{++}$ the *ellipsoid*
$$\mathcal E=\{x\mid(x-x_c)^{\mathsf T}P^{-1}(x-x_c)\le1\}=\{x_c+Au\mid\lVert u\rVert_2\le1\},\qquad A=P^{1/2},$$
has semi-axis lengths $\sqrt{\lambda_i(P)}$ along the eigenvectors of $P$.

:::

::: {#def-norm-ball-norm-cone .definition name="Norm ball, norm cone"}

For any norm $\lVert\cdot\rVert$ on $\mathbb{R}^n$ (@def-norm), the *norm ball* $\{x\mid\lVert x-x_c\rVert\le r\}$ and the *norm cone*
$$\{(x,t)\in\mathbb{R}^{n}\times\mathbb{R}\mid\lVert x\rVert\le t\}$$
are convex. For the Euclidean norm the norm cone is the *second-order cone* (ice-cream cone).

:::

::: {#prp-norm-balls-convex .proposition name="Norm balls and norm cones are convex"}

The sets in @def-norm-ball-norm-cone are convex, and the norm cone is a convex cone.

:::

::: {.proof}

1. Let $\lVert x_1\rVert\le t_1$, $\lVert x_2\rVert\le t_2$ and $0\le\theta\le1$.

2. The triangle inequality and homogeneity give $\lVert\theta x_1+(1-\theta)x_2\rVert\le\theta\lVert x_1\rVert+(1-\theta)\lVert x_2\rVert\le\theta t_1+(1-\theta)t_2$, so the norm cone is convex.

3. For $\alpha\ge0$, $\lVert\alpha x_1\rVert=\alpha\lVert x_1\rVert\le\alpha t_1$, so it is a cone.

4. The ball $\{x\mid\lVert x-x_c\rVert\le r\}$ is the slice $t=r$ of the norm cone shifted by $x_c$; slices and translates of convex sets are convex.

:::

::: {#def-polyhedron .definition name="Polyhedron"}

A *polyhedron* is the solution set of finitely many linear inequalities and equalities,
$$\mathcal P=\{x\mid Ax\preceq b,\ Cx=d\},$$
that is, an intersection of finitely many halfspaces and hyperplanes. A bounded polyhedron is a *polytope*. The *probability simplex* $\{x\mid x\succeq0,\ \mathbf 1^{\mathsf T}x=1\}$ is an example.

:::

::: {#def-psd-cone .definition name="Positive semidefinite cone"}

$\mathbb S^n$ is the space of symmetric $n\times n$ matrices, $\mathbb S^n_+=\{X\in\mathbb S^n\mid X\succeq0\}$ the positive semidefinite matrices (@def-positive-definite) and $\mathbb S^n_{++}$ the positive definite ones. $\mathbb S^n_+$ is a convex cone, because
$$z^{\mathsf T}(\theta_1X_1+\theta_2X_2)z=\theta_1z^{\mathsf T}X_1z+\theta_2z^{\mathsf T}X_2z\ge0\quad\text{for }\theta_1,\theta_2\ge0.$$

:::

::: {#exm-psd-cone-two-by-two .example name="The cone $\mathbb S^2_+$"}

Identify $\begin{bmatrix}x&y\\y&z\end{bmatrix}$ with $(x,y,z)\in\mathbb{R}^3$. It is positive semidefinite exactly when $x\ge0$, $z\ge0$ and $xz\ge y^2$. The boundary $xz=y^2$ is a circular cone around the axis $x=z$, $y=0$: with $x=s+w$, $z=s-w$ the condition reads $s\ge\sqrt{w^2+y^2}$, a second-order cone in the coordinates $(w,y,s)$.

:::

::: {#rmk-examples-of-convex-sets-1 .remark name="Which descriptions to use"}

An ellipsoid has two descriptions, as a sublevel set of a quadratic form and as the image of the unit ball under an affine map; the second also covers degenerate (flat) ellipsoids when $A$ is singular. Both kinds of description, inequality form and image form, recur throughout the subject.

:::
