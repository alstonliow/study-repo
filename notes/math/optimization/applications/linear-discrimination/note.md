---
title: "Linear and Nonlinear Discrimination"
sources: [ee364a-8]
requires: [math/optimization/duality/lagrange-dual-problem, math/optimization/convex-problems/second-order-cone-programs]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on geometric problems, in our own wording; proofs written out in steps. Linear classifiers trained by gradient methods are in @sec-ai-machine-learning-linear-classification. -->

Separating two finite point sets by a hyperplane is a linear feasibility problem. Asking for the widest gap gives a QP whose dual is a distance between convex hulls; allowing violations gives the support vector classifier.

::: {#def-linear-discrimination .definition name="Linear discrimination"}

Point sets $\{x_1,\dots,x_N\}$ and $\{y_1,\dots,y_M\}$ are *linearly separable* if there are $a,b$ with
$$a^{\mathsf T}x_i+b>0,\qquad a^{\mathsf T}y_i+b<0.$$
By scaling $(a,b)$, this is equivalent to the LP feasibility problem $a^{\mathsf T}x_i+b\ge1$, $a^{\mathsf T}y_i+b\le-1$.

:::

::: {#fig-linear-discrimination-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}\clip (-0.6,-0.6) rectangle (3.8,3.2);
\draw[faint] (-0.91,-0.4) -- (2.69,3.2);
\draw[emph] (-0.6,-0.16) -- (3.8,2.7);
\end{scope}
\fill[primary] (0.8,2.03) circle[pt];
\fill[primary] (0.68,1.5) circle[pt];
\fill[primary] (0.6,1.45) circle[pt];
\fill[primary] (0.83,2.5) circle[pt];
\fill[primary] (0.58,1.62) circle[pt];
\fill[primary] (1.02,2.06) circle[pt];
\fill[primary] (0.85,1.48) circle[pt];
\fill[primary] (0.79,2.21) circle[pt];
\fill[primary] (0.2,1.69) circle[pt];
\draw[emph] (1.48,-0.04) rectangle (1.6,0.08);
\draw[emph] (1.51,0.43) rectangle (1.63,0.55);
\draw[emph] (1.77,0.66) rectangle (1.89,0.78);
\draw[emph] (2.41,0.46) rectangle (2.53,0.58);
\draw[emph] (1.21,0.3) rectangle (1.33,0.42);
\draw[emph] (2.32,0.59) rectangle (2.44,0.71);
\draw[emph] (1.65,0.33) rectangle (1.77,0.45);
\draw[emph] (1.9,0.18) rectangle (2.02,0.3);
\draw[emph] (2.82,0.18) rectangle (2.94,0.3);
\end{tikzpicture}
\end{center}
```

Linear discrimination: find $a,b$ with $a^{\mathsf T}x_i+b>0$ on one set (dots) and $a^{\mathsf T}y_i+b<0$ on the other (squares). Usually many lines work (two shown), which motivates choosing one by margin.

:::

::: {#def-max-margin-separation .definition name="Robust (maximum margin) separation"}

The gap between the hyperplanes $a^{\mathsf T}z+b=\pm1$ is $2/\lVert a\rVert_2$. The *maximum margin* separator solves the convex problem
$$\text{minimize }\tfrac12\lVert a\rVert_2\quad\text{s.t. }a^{\mathsf T}x_i+b\ge1,\ a^{\mathsf T}y_i+b\le-1.$$

:::

::: {#fig-linear-discrimination-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}\clip (-0.6,-0.6) rectangle (3.8,3.2);
\draw[faint, dashed] (-0.6,0.54) -- (3.8,3.4);
\draw[faint, dashed] (-0.6,-0.85) -- (3.8,2);
\draw[hl] (-0.6,-0.16) -- (3.8,2.7);
\end{scope}
\fill[primary] (0.8,2.03) circle[pt];
\fill[primary] (0.68,1.5) circle[pt];
\fill[primary] (0.6,1.45) circle[pt];
\fill[primary] (0.83,2.5) circle[pt];
\fill[primary] (0.58,1.62) circle[pt];
\fill[primary] (1.02,2.06) circle[pt];
\fill[primary] (0.85,1.48) circle[pt];
\fill[primary] (0.79,2.21) circle[pt];
\fill[primary] (0.2,1.69) circle[pt];
\draw[emph] (1.48,-0.04) rectangle (1.6,0.08);
\draw[emph] (1.51,0.43) rectangle (1.63,0.55);
\draw[emph] (1.77,0.66) rectangle (1.89,0.78);
\draw[emph] (2.41,0.46) rectangle (2.53,0.58);
\draw[emph] (1.21,0.3) rectangle (1.33,0.42);
\draw[emph] (2.32,0.59) rectangle (2.44,0.71);
\draw[emph] (1.65,0.33) rectangle (1.77,0.45);
\draw[emph] (1.9,0.18) rectangle (2.02,0.3);
\draw[emph] (2.82,0.18) rectangle (2.94,0.3);
\draw[accent] (0.85,1.48) circle (0.14);
\draw[accent] (1.83,0.72) circle (0.14);
\draw[accent] (1.27,0.36) circle (0.14);
\end{tikzpicture}
\end{center}
```

The maximum-margin separator (thick) and the hyperplanes $a^{\mathsf T}z+b=\pm1$ (dashed), a slab of width $2/\lVert a\rVert_2$ with no points inside. The circled points lie on the slab's edges; they alone determine the solution.

:::

::: {#thm-max-margin-dual .theorem name="Dual of maximum margin separation"}

The Lagrange dual of @def-max-margin-separation is
$$\text{maximize }\mathbf 1^{\mathsf T}\lambda+\mathbf 1^{\mathsf T}\mu\quad\text{s.t. }\Big\lVert\sum_i\lambda_ix_i-\sum_i\mu_iy_i\Big\rVert_2\le\tfrac12,\ \mathbf 1^{\mathsf T}\lambda=\mathbf 1^{\mathsf T}\mu,\ \lambda,\mu\succeq0.$$
Its optimal value is $1/D$, where $D=\operatorname{dist}(\operatorname{conv}\{x_i\},\operatorname{conv}\{y_i\})$, and the maximum margin $2/\lVert a^\star\rVert_2$ equals $D$.

:::

::: {.proof}

1. The Lagrangian is $\frac12\lVert a\rVert_2+\sum_i\lambda_i(1-a^{\mathsf T}x_i-b)+\sum_i\mu_i(1+a^{\mathsf T}y_i+b)$.

2. Minimizing over $b$ is $-\infty$ unless $\mathbf 1^{\mathsf T}\lambda=\mathbf 1^{\mathsf T}\mu$. Minimizing $\frac12\lVert a\rVert_2-a^{\mathsf T}w$, with $w=\sum_i\lambda_ix_i-\sum_i\mu_iy_i$, over $a$ is $0$ if $\lVert w\rVert_2\le\frac12$ and $-\infty$ otherwise.

3. Write $\lambda=t\theta$, $\mu=t\gamma$ with $t=\mathbf 1^{\mathsf T}\lambda\ge0$ and $\theta,\gamma$ in probability simplices. The dual becomes maximize $2t$ subject to $t\lVert\sum_i\theta_ix_i-\sum_i\gamma_iy_i\rVert_2\le\frac12$. The best choice of $\theta,\gamma$ makes the norm $D$, so $t=1/(2D)$ and $d^\star=1/D$.

4. The constraints are affine and feasible (the sets are separable), so strong duality holds (@thm-slater) and $\frac12\lVert a^\star\rVert_2=1/D$. Hence the margin $2/\lVert a^\star\rVert_2=D$.

:::

::: {#def-support-vector-classifier .definition name="Support vector classifier"}

When the sets are not separable, allow violations $u_i,v_i\ge0$ and trade them off against the margin:
$$\text{minimize }\lVert a\rVert_2+\gamma(\mathbf 1^{\mathsf T}u+\mathbf 1^{\mathsf T}v)\quad\text{s.t. }a^{\mathsf T}x_i+b\ge1-u_i,\ a^{\mathsf T}y_i+b\le-1+v_i,\ u,v\succeq0.$$

:::

::: {#fig-linear-discrimination-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}\clip (-0.6,-0.6) rectangle (3.8,3.2);
\draw[faint, dashed] (-0.6,0.38) -- (3.8,2.79);
\draw[faint, dashed] (-0.6,-0.55) -- (3.8,1.86);
\draw[hl] (-0.6,-0.08) -- (3.8,2.33);
\end{scope}
\fill[primary] (1.4,1.43) circle[pt];
\fill[primary] (1.28,0.9) circle[pt];
\fill[primary] (1.2,0.85) circle[pt];
\fill[primary] (1.43,1.9) circle[pt];
\fill[primary] (1.18,1.02) circle[pt];
\fill[primary] (1.62,1.46) circle[pt];
\fill[primary] (1.45,0.88) circle[pt];
\fill[primary] (1.39,1.61) circle[pt];
\fill[primary] (0.8,1.09) circle[pt];
\draw[emph] (1.08,0.36) rectangle (1.2,0.48);
\draw[emph] (1.11,0.83) rectangle (1.23,0.95);
\draw[emph] (1.37,1.06) rectangle (1.49,1.18);
\draw[emph] (2.01,0.86) rectangle (2.13,0.98);
\draw[emph] (0.81,0.7) rectangle (0.93,0.82);
\draw[emph] (1.92,0.99) rectangle (2.04,1.11);
\draw[emph] (1.25,0.73) rectangle (1.37,0.85);
\draw[emph] (1.5,0.58) rectangle (1.62,0.7);
\draw[emph] (2.42,0.58) rectangle (2.54,0.7);
\draw[accent] (1.4,1.43) circle (0.14);
\draw[accent] (1.28,0.9) circle (0.14);
\draw[accent] (1.2,0.85) circle (0.14);
\draw[accent] (1.18,1.02) circle (0.14);
\draw[accent] (1.62,1.46) circle (0.14);
\draw[accent] (1.45,0.88) circle (0.14);
\draw[accent] (0.8,1.09) circle (0.14);
\draw[accent] (1.14,0.42) circle (0.14);
\draw[accent] (1.17,0.89) circle (0.14);
\draw[accent] (1.43,1.12) circle (0.14);
\draw[accent] (0.87,0.76) circle (0.14);
\draw[accent] (1.98,1.05) circle (0.14);
\draw[accent] (1.31,0.79) circle (0.14);
\end{tikzpicture}
\end{center}
```

A support vector classifier ($\gamma=0.5$) on data that cannot be separated. The circled points have positive slack $u_i$ or $v_i$: they sit inside the slab or on the wrong side, and each pays $\gamma$ times its violation.

:::

::: {#exm-separation-in-line .example name="Two points on a line"}

For $x_1=1$ and $y_1=-1$ in $\mathbb{R}$, the constraints $a+b\ge1$, $-a+b\le-1$ give $a\ge1$, so the maximum margin separator is $a=1$, $b=0$, margin $2/\lvert a\rvert=2$, the distance between the points.

:::

::: {#rmk-linear-discrimination-1 .remark name="Nonlinear discrimination and placement"}

Replacing $a^{\mathsf T}z+b$ by $\theta^{\mathsf T}F(z)$ for fixed basis functions $F$ (for example quadratics $z^{\mathsf T}Pz+q^{\mathsf T}z+r$, or polynomials) keeps the problem linear in $\theta$, so nonlinear separation is still an LP or QP. Placement and facility location problems, which choose positions to minimize a convex function of distances between linked points, are similar convex geometric problems.

:::
