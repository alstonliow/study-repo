---
title: "Dual Cones"
sources: [ee364a-2]
requires: [math/optimization/convex-sets/generalized-inequalities, math/optimization/convex-sets/separating-hyperplanes]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on convex sets, in our own wording; proofs written out in steps. -->

The dual cone of $K$ collects the linear functions that are nonnegative on $K$. It describes generalized inequalities by ordinary ones and characterizes minimum and minimal elements by minimizing linear functions.

::: {#def-dual-cone .definition name="Dual cone"}

The *dual cone* of a cone $K$ is
$$K^*=\{y\mid y^{\mathsf T}x\ge0\ \text{for all}\ x\in K\}.$$
For $K\subseteq\mathbb S^n$ the inner product is $\operatorname{tr}(XY)$.

:::

::: {#fig-dual-cones-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0,0) -- (1.91,1.1) -- (1.87,1.16) -- (1.83,1.21) -- (1.8,1.27) -- (1.76,1.32) -- (1.72,1.38) -- (1.67,1.43) -- (1.63,1.48) -- (1.58,1.53) -- (1.54,1.58) -- (1.49,1.62) -- (1.44,1.67) -- (1.38,1.71) -- (1.33,1.75) -- (1.28,1.79) -- (1.22,1.83) -- (1.17,1.87) -- (1.11,1.9) -- (1.05,1.93) -- (0.99,1.96) -- (0.93,1.99) -- cycle;
\draw[emph] (1.91,1.1) -- (0,0) -- (0.93,1.99);
\node[lab] at (1.07,1.19) {$K$};
\draw[faint, dashed] (2.18,1.01) -- (-1.45,-0.68);
\draw[->, hl] (0,0) -- (-0.59,1.27) node[lab, left] {$y$};
\node[lab] at (-1.65,0.95) {$y^{\mathsf T}x\ge0$};
\end{tikzpicture}
\end{center}
```

A vector $y$ lies in $K^*$ exactly when $K$ sits in the halfspace $\{x\mid y^{\mathsf T}x\ge0\}$, whose boundary (dashed) is the line through the origin perpendicular to $y$.

:::

::: {#exm-dual-cones .example name="Self-dual cones and the dual norm cone"}

1. $(\mathbb{R}^n_+)^*=\mathbb{R}^n_+$: if $y\succeq0$ then $y^{\mathsf T}x\ge0$ for $x\succeq0$; conversely $y^{\mathsf T}e_i=y_i\ge0$.

2. $(\mathbb S^n_+)^*=\mathbb S^n_+$: for $Y\succeq0$ and $X=\sum_i\lambda_iq_iq_i^{\mathsf T}\succeq0$, $\operatorname{tr}(XY)=\sum_i\lambda_iq_i^{\mathsf T}Yq_i\ge0$; conversely $\operatorname{tr}(Y\,zz^{\mathsf T})=z^{\mathsf T}Yz\ge0$ for all $z$.

3. For $K=\{(x,t)\mid\lVert x\rVert\le t\}$, $K^*=\{(u,v)\mid\lVert u\rVert_*\le v\}$, with the *dual norm* $\lVert u\rVert_*=\sup\{u^{\mathsf T}x\mid\lVert x\rVert\le1\}$.

4. Enlarging $K$ shrinks $K^*$: in $\mathbb{R}^2$ the dual of the halfplane $\{x\mid x_2\ge0\}$ is the ray $\{(0,v)\mid v\ge0\}$, and the dual of all of $\mathbb{R}^2$ is $\{0\}$.

:::

::: {#fig-dual-cones-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintB] (0,0) -- (1.99,-0.93) -- (2.1,-0.67) -- (2.16,-0.4) -- (2.2,-0.12) -- (2.19,0.15) -- (2.16,0.43) -- (2.09,0.7) -- (1.98,0.96) -- (1.85,1.2) -- (1.68,1.42) -- (1.49,1.62) -- (1.27,1.8) -- (1.03,1.94) -- (0.78,2.06) -- (0.51,2.14) -- (0.24,2.19) -- (-0.04,2.2) -- (-0.32,2.18) -- (-0.59,2.12) -- (-0.85,2.03) -- (-1.1,1.91) -- cycle;
\fill[tintA] (0,0) -- (1.91,1.1) -- (1.87,1.16) -- (1.83,1.21) -- (1.8,1.27) -- (1.76,1.32) -- (1.72,1.38) -- (1.67,1.43) -- (1.63,1.48) -- (1.58,1.53) -- (1.54,1.58) -- (1.49,1.62) -- (1.44,1.67) -- (1.38,1.71) -- (1.33,1.75) -- (1.28,1.79) -- (1.22,1.83) -- (1.17,1.87) -- (1.11,1.9) -- (1.05,1.93) -- (0.99,1.96) -- (0.93,1.99) -- cycle;
\draw[emph] (1.91,1.1) -- (0,0) -- (0.93,1.99);
\draw[hl] (1.99,-0.93) -- (0,0) -- (-1.1,1.91);
\node[lab] at (1,1.11) {$K$};
\node[lab] at (1.6,0) {$K^*$};
\node[lab] at (-0.28,1.58) {$K^*$};
\draw[faint] (0.39,0.22) arc[start angle=30, end angle=120, radius=0.45];
\end{tikzpicture}
\end{center}
```

In the plane the dual of a wedge $K$ with edges at angles $\alpha<\beta$ is the wider wedge $K^*$ with edges at $\beta-90^\circ$ and $\alpha+90^\circ$ (thick): a narrow cone has a wide dual, and enlarging $K$ shrinks $K^*$.

:::

::: {#prp-dual-cone-properties .proposition name="Properties of dual cones"}

For any cone $K$: $K^*$ is closed and convex; $K_1\subseteq K_2$ implies $K_2^*\subseteq K_1^*$; if $K$ has nonempty interior then $K^*$ contains no line; if $K$ is convex and its closure contains no line then $K^*$ has nonempty interior; $K^{**}$ is the closure of the convex hull of $K$. In particular, if $K$ is proper then so is $K^*$, and $K^{**}=K$.

:::

::: {.proof}

1. $K^*$ is an intersection of the closed halfspaces $\{y\mid y^{\mathsf T}x\ge0\}$, $x\in K$, so it is closed and convex. A larger $K$ gives more halfspaces and a smaller intersection.

2. Contains no line: if $y,-y\in K^*$ then $y^{\mathsf T}x=0$ on $K$; a set with interior is not inside a hyperplane, so $y=0$.

3. $K^{**}\supseteq K$ by definition, and $K^{**}$ is closed and convex, so it contains $\overline{\operatorname{conv}K}$. Conversely let $z\notin\overline{\operatorname{conv}K}$. Strict separation of the point $z$ from this closed convex cone (@def-strict-separation) gives $y$ with $y^{\mathsf T}z<b\le y^{\mathsf T}x$ for $x$ in the cone; as the cone contains $0$ and all positive multiples, $b\le0$ and $y^{\mathsf T}x\ge0$ there, so $y\in K^*$ and $y^{\mathsf T}z<0$, that is, $z\notin K^{**}$.

4. Nonempty interior of $K^*$: if $\operatorname{int}K^*=\emptyset$, $K^*$ lies in a hyperplane $\{y\mid c^{\mathsf T}y=0\}$ with $c\ne0$; then $\pm c\in K^{**}=\overline{\operatorname{conv}K}$, a line in the closure of $K$ (convex, since $K$ is).

:::

::: {#prp-dual-generalized-inequality .proposition name="Generalized inequalities through the dual cone"}

For a proper cone $K$,
$$x\preceq_Ky\iff\lambda^{\mathsf T}x\le\lambda^{\mathsf T}y\ \text{for all}\ \lambda\succeq_{K^*}0,$$
$$x\prec_Ky\iff\lambda^{\mathsf T}x<\lambda^{\mathsf T}y\ \text{for all}\ \lambda\succeq_{K^*}0,\ \lambda\ne0.$$

:::

::: {.proof}

1. The first line is $K=K^{**}$ applied to $y-x$.

2. If $y-x\in\operatorname{int}K$ and $\lambda\in K^*\setminus\{0\}$, then $y-x-\epsilon\lambda\in K$ for small $\epsilon>0$, so $\lambda^{\mathsf T}(y-x)\ge\epsilon\lVert\lambda\rVert_2^2>0$.

3. If $y-x\notin K$, step 1 gives $\lambda\in K^*$ with $\lambda^{\mathsf T}(y-x)<0$. If $y-x\in K\setminus\operatorname{int}K$, it is a boundary point of $K$, and a supporting hyperplane (@thm-supporting-hyperplane) gives $\mu\ne0$ with $\mu^{\mathsf T}u\le\mu^{\mathsf T}(y-x)$ for all $u\in K$.

4. Since $K$ is a cone containing $0$ and $2(y-x)$, this forces $\mu^{\mathsf T}(y-x)=0$ and $\mu^{\mathsf T}u\le0$ on $K$. So $\lambda=-\mu$ is a nonzero element of $K^*$ with $\lambda^{\mathsf T}(y-x)=0$, and the strict inequality fails.

:::

::: {#thm-minimal-via-dual .theorem name="Minimum and minimal elements by linear functions"}

Let $K$ be proper and $S\subseteq\mathbb{R}^n$.

1. $x$ is the minimum element of $S$ if and only if, for every $\lambda\succ_{K^*}0$, $x$ is the unique minimizer of $\lambda^{\mathsf T}z$ over $z\in S$.

2. If $x$ minimizes $\lambda^{\mathsf T}z$ over $S$ for some $\lambda\succ_{K^*}0$, then $x$ is minimal.

3. If $S$ is convex and $x$ is minimal, then $x$ minimizes $\lambda^{\mathsf T}z$ over $S$ for some nonzero $\lambda\succeq_{K^*}0$.

:::

::: {.proof}

1. If $x$ is the minimum, $z-x\in K$ for all $z\in S$, so $\lambda^{\mathsf T}z\ge\lambda^{\mathsf T}x$, with equality only for $z=x$: if $\lambda\in\operatorname{int}K^*$ and $u\in K$, $u\ne0$, then $\lambda-\epsilon u\in K^*$ for small $\epsilon>0$, so $\lambda^{\mathsf T}u\ge\epsilon\lVert u\rVert_2^2>0$.

2. Conversely, if $x$ is the unique minimizer for every $\lambda\succ_{K^*}0$, then by continuity $\lambda^{\mathsf T}(z-x)\ge0$ for every $\lambda\in K^*$, so $z-x\in K^{**}=K$.

3. Statement 2: if some $y\in S$, $y\ne x$, had $y\preceq_Kx$, then $x-y\in K\setminus\{0\}$ and $\lambda^{\mathsf T}(x-y)>0$, so $y$ would give a smaller value.

4. Statement 3: the convex sets $S$ and $x-\operatorname{int}K$ are disjoint, since a point $y\in S$ with $x-y\in\operatorname{int}K$ would be below $x$ and different from it. Separating them (@thm-separating-hyperplane) gives $\lambda\ne0$ with $\lambda^{\mathsf T}z\ge\lambda^{\mathsf T}(x-k)$ for $z\in S$, $k\in\operatorname{int}K$. Letting $k\to0$ gives $\lambda^{\mathsf T}z\ge\lambda^{\mathsf T}x$; letting $k$ grow shows $\lambda^{\mathsf T}k\ge0$ on $K$, so $\lambda\in K^*$.

:::

::: {#fig-dual-cones-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (4.6,0) node[lab, right] {$x_1$};
\draw[->, faint] (0,-0.2) -- (0,3.6) node[lab, above] {$x_2$};
\fill[tintA] (3.76,2.43) -- (3.75,2.46) -- (3.74,2.48) -- (3.73,2.5) -- (3.71,2.52) -- (3.7,2.53) -- (3.68,2.55) -- (3.67,2.57) -- (3.65,2.59) -- (3.63,2.61) -- (3.61,2.62) -- (3.6,2.64) -- (3.58,2.65) -- (3.55,2.67) -- (3.53,2.68) -- (3.51,2.7) -- (3.49,2.71) -- (3.46,2.72) -- (3.44,2.74) -- (3.41,2.75) -- (3.39,2.76) -- (3.36,2.77) -- (3.33,2.78) -- (3.3,2.78) -- (3.28,2.79) -- (3.25,2.8) -- (3.22,2.81) -- (3.19,2.81) -- (3.16,2.82) -- (3.12,2.82) -- (3.09,2.83) -- (3.06,2.83) -- (3.03,2.83) -- (2.99,2.83) -- (2.96,2.83) -- (2.93,2.83) -- (2.89,2.83) -- (2.86,2.83) -- (2.82,2.83) -- (2.79,2.83) -- (2.75,2.82) -- (2.71,2.82) -- (2.68,2.81) -- (2.64,2.81) -- (2.61,2.8) -- (2.57,2.8) -- (2.53,2.79) -- (2.5,2.78) -- (2.46,2.77) -- (2.42,2.76) -- (2.38,2.75) -- (2.35,2.74) -- (2.31,2.73) -- (2.27,2.72) -- (2.24,2.7) -- (2.2,2.69) -- (2.16,2.68) -- (2.13,2.66) -- (2.09,2.65) -- (2.06,2.63) -- (2.02,2.62) -- (1.98,2.6) -- (1.95,2.58) -- (1.91,2.56) -- (1.88,2.54) -- (1.85,2.53) -- (1.81,2.51) -- (1.78,2.49) -- (1.75,2.47) -- (1.71,2.45) -- (1.68,2.42) -- (1.65,2.4) -- (1.62,2.38) -- (1.59,2.36) -- (1.56,2.33) -- (1.53,2.31) -- (1.5,2.29) -- (1.47,2.26) -- (1.44,2.24) -- (1.42,2.21) -- (1.39,2.19) -- (1.37,2.16) -- (1.34,2.14) -- (1.32,2.11) -- (1.29,2.09) -- (1.27,2.06) -- (1.25,2.03) -- (1.23,2.01) -- (1.21,1.98) -- (1.19,1.96) -- (1.17,1.93) -- (1.15,1.9) -- (1.14,1.87) -- (1.12,1.85) -- (1.1,1.82) -- (1.09,1.79) -- (1.08,1.77) -- (1.06,1.74) -- (1.05,1.71) -- (1.04,1.69) -- (1.03,1.66) -- (1.02,1.63) -- (1.02,1.61) -- (1.01,1.58) -- (1,1.55) -- (1,1.53) -- (0.99,1.5) -- (0.99,1.47) -- (0.99,1.45) -- (0.99,1.42) -- (0.99,1.4) -- (0.99,1.37) -- (0.99,1.35) -- (0.99,1.33) -- (1,1.3) -- (1,1.28) -- (1.01,1.25) -- (1.01,1.23) -- (1.02,1.21) -- (1.03,1.19) -- (1.04,1.17) -- (1.05,1.14) -- (1.06,1.12) -- (1.07,1.1) -- (1.09,1.08) -- (1.1,1.07) -- (1.12,1.05) -- (1.13,1.03) -- (1.15,1.01) -- (1.17,0.99) -- (1.19,0.98) -- (1.2,0.96) -- (1.22,0.95) -- (1.25,0.93) -- (1.27,0.92) -- (1.29,0.9) -- (1.31,0.89) -- (1.34,0.88) -- (1.36,0.86) -- (1.39,0.85) -- (1.41,0.84) -- (1.44,0.83) -- (1.47,0.82) -- (1.5,0.82) -- (1.52,0.81) -- (1.55,0.8) -- (1.58,0.79) -- (1.61,0.79) -- (1.64,0.78) -- (1.68,0.78) -- (1.71,0.77) -- (1.74,0.77) -- (1.77,0.77) -- (1.81,0.77) -- (1.84,0.77) -- (1.87,0.77) -- (1.91,0.77) -- (1.94,0.77) -- (1.98,0.77) -- (2.01,0.77) -- (2.05,0.78) -- (2.09,0.78) -- (2.12,0.79) -- (2.16,0.79) -- (2.19,0.8) -- (2.23,0.8) -- (2.27,0.81) -- (2.3,0.82) -- (2.34,0.83) -- (2.38,0.84) -- (2.42,0.85) -- (2.45,0.86) -- (2.49,0.87) -- (2.53,0.88) -- (2.56,0.9) -- (2.6,0.91) -- (2.64,0.92) -- (2.67,0.94) -- (2.71,0.95) -- (2.74,0.97) -- (2.78,0.98) -- (2.82,1) -- (2.85,1.02) -- (2.89,1.04) -- (2.92,1.06) -- (2.95,1.07) -- (2.99,1.09) -- (3.02,1.11) -- (3.05,1.13) -- (3.09,1.15) -- (3.12,1.18) -- (3.15,1.2) -- (3.18,1.22) -- (3.21,1.24) -- (3.24,1.27) -- (3.27,1.29) -- (3.3,1.31) -- (3.33,1.34) -- (3.36,1.36) -- (3.38,1.39) -- (3.41,1.41) -- (3.43,1.44) -- (3.46,1.46) -- (3.48,1.49) -- (3.51,1.51) -- (3.53,1.54) -- (3.55,1.57) -- (3.57,1.59) -- (3.59,1.62) -- (3.61,1.64) -- (3.63,1.67) -- (3.65,1.7) -- (3.66,1.73) -- (3.68,1.75) -- (3.7,1.78) -- (3.71,1.81) -- (3.72,1.83) -- (3.74,1.86) -- (3.75,1.89) -- (3.76,1.91) -- (3.77,1.94) -- (3.78,1.97) -- (3.78,1.99) -- (3.79,2.02) -- (3.8,2.05) -- (3.8,2.07) -- (3.81,2.1) -- (3.81,2.13) -- (3.81,2.15) -- (3.81,2.18) -- (3.81,2.2) -- (3.81,2.23) -- (3.81,2.25) -- (3.81,2.27) -- (3.8,2.3) -- (3.8,2.32) -- (3.79,2.35) -- (3.79,2.37) -- (3.78,2.39) -- (3.77,2.41) -- cycle;
\draw[emph] (3.76,2.43) -- (3.75,2.46) -- (3.74,2.48) -- (3.73,2.5) -- (3.71,2.52) -- (3.7,2.53) -- (3.68,2.55) -- (3.67,2.57) -- (3.65,2.59) -- (3.63,2.61) -- (3.61,2.62) -- (3.6,2.64) -- (3.58,2.65) -- (3.55,2.67) -- (3.53,2.68) -- (3.51,2.7) -- (3.49,2.71) -- (3.46,2.72) -- (3.44,2.74) -- (3.41,2.75) -- (3.39,2.76) -- (3.36,2.77) -- (3.33,2.78) -- (3.3,2.78) -- (3.28,2.79) -- (3.25,2.8) -- (3.22,2.81) -- (3.19,2.81) -- (3.16,2.82) -- (3.12,2.82) -- (3.09,2.83) -- (3.06,2.83) -- (3.03,2.83) -- (2.99,2.83) -- (2.96,2.83) -- (2.93,2.83) -- (2.89,2.83) -- (2.86,2.83) -- (2.82,2.83) -- (2.79,2.83) -- (2.75,2.82) -- (2.71,2.82) -- (2.68,2.81) -- (2.64,2.81) -- (2.61,2.8) -- (2.57,2.8) -- (2.53,2.79) -- (2.5,2.78) -- (2.46,2.77) -- (2.42,2.76) -- (2.38,2.75) -- (2.35,2.74) -- (2.31,2.73) -- (2.27,2.72) -- (2.24,2.7) -- (2.2,2.69) -- (2.16,2.68) -- (2.13,2.66) -- (2.09,2.65) -- (2.06,2.63) -- (2.02,2.62) -- (1.98,2.6) -- (1.95,2.58) -- (1.91,2.56) -- (1.88,2.54) -- (1.85,2.53) -- (1.81,2.51) -- (1.78,2.49) -- (1.75,2.47) -- (1.71,2.45) -- (1.68,2.42) -- (1.65,2.4) -- (1.62,2.38) -- (1.59,2.36) -- (1.56,2.33) -- (1.53,2.31) -- (1.5,2.29) -- (1.47,2.26) -- (1.44,2.24) -- (1.42,2.21) -- (1.39,2.19) -- (1.37,2.16) -- (1.34,2.14) -- (1.32,2.11) -- (1.29,2.09) -- (1.27,2.06) -- (1.25,2.03) -- (1.23,2.01) -- (1.21,1.98) -- (1.19,1.96) -- (1.17,1.93) -- (1.15,1.9) -- (1.14,1.87) -- (1.12,1.85) -- (1.1,1.82) -- (1.09,1.79) -- (1.08,1.77) -- (1.06,1.74) -- (1.05,1.71) -- (1.04,1.69) -- (1.03,1.66) -- (1.02,1.63) -- (1.02,1.61) -- (1.01,1.58) -- (1,1.55) -- (1,1.53) -- (0.99,1.5) -- (0.99,1.47) -- (0.99,1.45) -- (0.99,1.42) -- (0.99,1.4) -- (0.99,1.37) -- (0.99,1.35) -- (0.99,1.33) -- (1,1.3) -- (1,1.28) -- (1.01,1.25) -- (1.01,1.23) -- (1.02,1.21) -- (1.03,1.19) -- (1.04,1.17) -- (1.05,1.14) -- (1.06,1.12) -- (1.07,1.1) -- (1.09,1.08) -- (1.1,1.07) -- (1.12,1.05) -- (1.13,1.03) -- (1.15,1.01) -- (1.17,0.99) -- (1.19,0.98) -- (1.2,0.96) -- (1.22,0.95) -- (1.25,0.93) -- (1.27,0.92) -- (1.29,0.9) -- (1.31,0.89) -- (1.34,0.88) -- (1.36,0.86) -- (1.39,0.85) -- (1.41,0.84) -- (1.44,0.83) -- (1.47,0.82) -- (1.5,0.82) -- (1.52,0.81) -- (1.55,0.8) -- (1.58,0.79) -- (1.61,0.79) -- (1.64,0.78) -- (1.68,0.78) -- (1.71,0.77) -- (1.74,0.77) -- (1.77,0.77) -- (1.81,0.77) -- (1.84,0.77) -- (1.87,0.77) -- (1.91,0.77) -- (1.94,0.77) -- (1.98,0.77) -- (2.01,0.77) -- (2.05,0.78) -- (2.09,0.78) -- (2.12,0.79) -- (2.16,0.79) -- (2.19,0.8) -- (2.23,0.8) -- (2.27,0.81) -- (2.3,0.82) -- (2.34,0.83) -- (2.38,0.84) -- (2.42,0.85) -- (2.45,0.86) -- (2.49,0.87) -- (2.53,0.88) -- (2.56,0.9) -- (2.6,0.91) -- (2.64,0.92) -- (2.67,0.94) -- (2.71,0.95) -- (2.74,0.97) -- (2.78,0.98) -- (2.82,1) -- (2.85,1.02) -- (2.89,1.04) -- (2.92,1.06) -- (2.95,1.07) -- (2.99,1.09) -- (3.02,1.11) -- (3.05,1.13) -- (3.09,1.15) -- (3.12,1.18) -- (3.15,1.2) -- (3.18,1.22) -- (3.21,1.24) -- (3.24,1.27) -- (3.27,1.29) -- (3.3,1.31) -- (3.33,1.34) -- (3.36,1.36) -- (3.38,1.39) -- (3.41,1.41) -- (3.43,1.44) -- (3.46,1.46) -- (3.48,1.49) -- (3.51,1.51) -- (3.53,1.54) -- (3.55,1.57) -- (3.57,1.59) -- (3.59,1.62) -- (3.61,1.64) -- (3.63,1.67) -- (3.65,1.7) -- (3.66,1.73) -- (3.68,1.75) -- (3.7,1.78) -- (3.71,1.81) -- (3.72,1.83) -- (3.74,1.86) -- (3.75,1.89) -- (3.76,1.91) -- (3.77,1.94) -- (3.78,1.97) -- (3.78,1.99) -- (3.79,2.02) -- (3.8,2.05) -- (3.8,2.07) -- (3.81,2.1) -- (3.81,2.13) -- (3.81,2.15) -- (3.81,2.18) -- (3.81,2.2) -- (3.81,2.23) -- (3.81,2.25) -- (3.81,2.27) -- (3.8,2.3) -- (3.8,2.32) -- (3.79,2.35) -- (3.79,2.37) -- (3.78,2.39) -- (3.77,2.41) -- cycle;
\draw[hl] (0.99,1.4) -- (0.99,1.37) -- (0.99,1.35) -- (0.99,1.33) -- (1,1.3) -- (1,1.28) -- (1.01,1.25) -- (1.01,1.23) -- (1.02,1.21) -- (1.03,1.19) -- (1.04,1.17) -- (1.05,1.14) -- (1.06,1.12) -- (1.07,1.1) -- (1.09,1.08) -- (1.1,1.07) -- (1.12,1.05) -- (1.13,1.03) -- (1.15,1.01) -- (1.17,0.99) -- (1.19,0.98) -- (1.2,0.96) -- (1.22,0.95) -- (1.25,0.93) -- (1.27,0.92) -- (1.29,0.9) -- (1.31,0.89) -- (1.34,0.88) -- (1.36,0.86) -- (1.39,0.85) -- (1.41,0.84) -- (1.44,0.83) -- (1.47,0.82) -- (1.5,0.82) -- (1.52,0.81) -- (1.55,0.8) -- (1.58,0.79) -- (1.61,0.79) -- (1.64,0.78) -- (1.68,0.78) -- (1.71,0.77) -- (1.74,0.77) -- (1.77,0.77) -- (1.81,0.77) -- (1.84,0.77);
\draw[faint, dashed] (-0.06,1.58) -- (2.74,0.18);
\fill[accent] (1.34,0.88) circle[pt] node[lab, below left] {$x$};
\draw[->] (1.34,0.88) -- (1.69,1.58) node[lab, right] {$\lambda$};
\node[lab] at (2.6,1.9) {$S$};
\end{tikzpicture}
\end{center}
```

With $K=\mathbb{R}^2_+$ and $\lambda=(1,2)\succ_{K^*}0$, the point $x$ minimizing $\lambda^{\mathsf T}z$ over $S$ is where the line $\lambda^{\mathsf T}z=\text{const}$ (dashed) touches $S$; it is minimal. The thick arc is the set of all minimal points, each reached by some $\lambda\succeq0$.

:::

::: {#exm-production-frontier .example name="Efficient production methods"}

A product can be made by several methods; method $x\in P\subseteq\mathbb{R}^n$ uses $x_i$ units of resource $i$. A method is *efficient* if it is minimal in $P$ for $\mathbb{R}^n_+$: no other method uses at most as much of every resource and less of one. By @thm-minimal-via-dual, every minimizer of a positive price vector $\lambda\succ0$ applied to resource use, $\lambda^{\mathsf T}x$, is efficient, and when $P$ is convex every efficient method arises this way with some $\lambda\succeq0$, $\lambda\ne0$.

:::
