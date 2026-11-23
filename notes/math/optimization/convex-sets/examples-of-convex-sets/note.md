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

::: {#fig-examples-of-convex-sets-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (-0.4,2.4) -- (2.4,-0.4) -- (3.2,0.4) -- (3.2,2.4) -- cycle;
\draw[emph] (-0.4,2.4) -- (2.4,-0.4);
\fill[ink] (1,1) circle[pt] node[lab, below left] {$x_0$};
\draw[->, hl] (1,1) -- (1.6,1.6) node[lab, above] {$a$};
\fill[ink] (0.4,1.6) circle[pt];
\draw[->, faint] (1,1) -- (0.4,1.6) node[lab, left] {$x-x_0$};
\node[lab] at (2.4,1.7) {$a^{\mathsf T}x\ge b$};
\node[lab] at (0.6,0.2) {$a^{\mathsf T}x\le b$};
\end{tikzpicture}
\end{center}
```

The hyperplane $a^{\mathsf T}x=b$ through $x_0$ is the set of $x$ with $x-x_0\perp a$. It cuts the plane into two halfspaces; $a$ points into $\{a^{\mathsf T}x\ge b\}$ (shaded).

:::

::: {#def-ball-ellipsoid .definition name="Euclidean ball, ellipsoid"}

The Euclidean ball with centre $x_c$ and radius $r>0$ is $B(x_c,r)=\{x\mid\lVert x-x_c\rVert_2\le r\}=\{x_c+ru\mid\lVert u\rVert_2\le1\}$. For $P\in\mathbb S^n_{++}$ the *ellipsoid*
$$\mathcal E=\{x\mid(x-x_c)^{\mathsf T}P^{-1}(x-x_c)\le1\}=\{x_c+Au\mid\lVert u\rVert_2\le1\},\qquad A=P^{1/2},$$
has semi-axis lengths $\sqrt{\lambda_i(P)}$ along the eigenvectors of $P$.

:::

::: {#fig-examples-of-convex-sets-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (1.56,0.9) -- (1.51,0.96) -- (1.46,1.02) -- (1.39,1.07) -- (1.31,1.11) -- (1.22,1.15) -- (1.13,1.17) -- (1.02,1.18) -- (0.9,1.19) -- (0.78,1.19) -- (0.66,1.18) -- (0.53,1.15) -- (0.39,1.12) -- (0.25,1.09) -- (0.11,1.04) -- (-0.03,0.99) -- (-0.17,0.92) -- (-0.31,0.85) -- (-0.45,0.78) -- (-0.58,0.7) -- (-0.71,0.61) -- (-0.84,0.52) -- (-0.96,0.42) -- (-1.07,0.33) -- (-1.17,0.23) -- (-1.26,0.12) -- (-1.35,0.02) -- (-1.42,-0.09) -- (-1.48,-0.19) -- (-1.54,-0.29) -- (-1.57,-0.39) -- (-1.6,-0.49) -- (-1.62,-0.58) -- (-1.62,-0.67) -- (-1.61,-0.75) -- (-1.59,-0.83) -- (-1.56,-0.9) -- (-1.51,-0.96) -- (-1.46,-1.02) -- (-1.39,-1.07) -- (-1.31,-1.11) -- (-1.22,-1.15) -- (-1.12,-1.17) -- (-1.02,-1.18) -- (-0.9,-1.19) -- (-0.78,-1.19) -- (-0.66,-1.18) -- (-0.53,-1.15) -- (-0.39,-1.13) -- (-0.25,-1.09) -- (-0.11,-1.04) -- (0.03,-0.99) -- (0.17,-0.92) -- (0.31,-0.85) -- (0.45,-0.78) -- (0.58,-0.7) -- (0.71,-0.61) -- (0.84,-0.52) -- (0.96,-0.42) -- (1.07,-0.33) -- (1.17,-0.23) -- (1.26,-0.12) -- (1.35,-0.02) -- (1.42,0.09) -- (1.48,0.19) -- (1.54,0.29) -- (1.58,0.39) -- (1.6,0.49) -- (1.62,0.58) -- (1.62,0.67) -- (1.61,0.75) -- (1.59,0.83) -- cycle;
\draw[emph] (1.56,0.9) -- (1.51,0.96) -- (1.46,1.02) -- (1.39,1.07) -- (1.31,1.11) -- (1.22,1.15) -- (1.13,1.17) -- (1.02,1.18) -- (0.9,1.19) -- (0.78,1.19) -- (0.66,1.18) -- (0.53,1.15) -- (0.39,1.12) -- (0.25,1.09) -- (0.11,1.04) -- (-0.03,0.99) -- (-0.17,0.92) -- (-0.31,0.85) -- (-0.45,0.78) -- (-0.58,0.7) -- (-0.71,0.61) -- (-0.84,0.52) -- (-0.96,0.42) -- (-1.07,0.33) -- (-1.17,0.23) -- (-1.26,0.12) -- (-1.35,0.02) -- (-1.42,-0.09) -- (-1.48,-0.19) -- (-1.54,-0.29) -- (-1.57,-0.39) -- (-1.6,-0.49) -- (-1.62,-0.58) -- (-1.62,-0.67) -- (-1.61,-0.75) -- (-1.59,-0.83) -- (-1.56,-0.9) -- (-1.51,-0.96) -- (-1.46,-1.02) -- (-1.39,-1.07) -- (-1.31,-1.11) -- (-1.22,-1.15) -- (-1.12,-1.17) -- (-1.02,-1.18) -- (-0.9,-1.19) -- (-0.78,-1.19) -- (-0.66,-1.18) -- (-0.53,-1.15) -- (-0.39,-1.13) -- (-0.25,-1.09) -- (-0.11,-1.04) -- (0.03,-0.99) -- (0.17,-0.92) -- (0.31,-0.85) -- (0.45,-0.78) -- (0.58,-0.7) -- (0.71,-0.61) -- (0.84,-0.52) -- (0.96,-0.42) -- (1.07,-0.33) -- (1.17,-0.23) -- (1.26,-0.12) -- (1.35,-0.02) -- (1.42,0.09) -- (1.48,0.19) -- (1.54,0.29) -- (1.58,0.39) -- (1.6,0.49) -- (1.62,0.58) -- (1.62,0.67) -- (1.61,0.75) -- (1.59,0.83) -- cycle;
\fill[ink] (0,0) circle[pt] node[lab, below] {$x_c$};
\draw[->, hl] (0,0) -- (1.56,0.9) node[lab, right] {$\sqrt{\lambda_1}\,q_1$};
\draw[->, hl] (0,0) -- (-0.45,0.78) node[lab, left] {$\sqrt{\lambda_2}\,q_2$};
\end{tikzpicture}
\end{center}
```

The ellipsoid $\{x\mid(x-x_c)^{\mathsf T}P^{-1}(x-x_c)\le1\}$ with $P=Q\Lambda Q^{\mathsf T}$: its semi-axes point along the eigenvectors $q_i$ of $P$ and have lengths $\sqrt{\lambda_i}$. The ball is the case $P=r^2I$.

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

::: {#fig-examples-of-convex-sets-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0,0) -- (2.2,-0.3) -- (3.1,1) -- (2.2,2.2) -- (0.3,1.8) -- cycle;
\draw[emph] (0,0) -- (2.2,-0.3) -- (3.1,1) -- (2.2,2.2) -- (0.3,1.8) -- cycle;
\draw[->, hl] (1.1,-0.15) -- (1.03,-0.69) node[lab, left] {$a_1$};
\draw[->, hl] (2.65,0.35) -- (3.1,0.04) node[lab, right] {$a_2$};
\draw[->, hl] (2.65,1.6) -- (3.09,1.93) node[lab, right] {$a_3$};
\draw[->, hl] (1.25,2) -- (1.14,2.54) node[lab, left] {$a_4$};
\draw[->, hl] (0.15,0.9) -- (-0.39,0.99) node[lab, left] {$a_5$};
\node[lab] at (1.5,0.9) {$\mathcal P$};
\end{tikzpicture}
\end{center}
```

A polyhedron $\mathcal P=\{x\mid a_i^{\mathsf T}x\le b_i\}$ in the plane: each inequality keeps the side of a line opposite its outward normal $a_i$, and $\mathcal P$ is the intersection of these five halfplanes.

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
