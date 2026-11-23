---
title: "Norm and Penalty Function Approximation"
sources: [ee364a-6]
requires: [math/optimization/convex-problems/second-order-cone-programs, math/optimization/duality/kkt-conditions]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on approximation and fitting, in our own wording; proofs written out in steps. -->

Fitting $Ax\approx b$ means choosing how to measure the residual $r=Ax-b$. Different norms and penalty functions give different residual distributions; all lead to convex problems.

::: {#def-norm-approximation .definition name="Norm approximation"}

Given $A\in\mathbb{R}^{m\times n}$ with $m\ge n$ and $b\in\mathbb{R}^m$, the *norm approximation problem* is
$$\text{minimize }\lVert Ax-b\rVert.$$
Least squares uses $\lVert\cdot\rVert_2$; Chebyshev (minimax) approximation uses $\lVert\cdot\rVert_\infty$ and is an LP: minimize $t$ subject to $-t\mathbf 1\preceq Ax-b\preceq t\mathbf 1$; sum of absolute residuals uses $\lVert\cdot\rVert_1$ and is an LP: minimize $\mathbf 1^{\mathsf T}y$ subject to $-y\preceq Ax-b\preceq y$.

:::

::: {#def-penalty-function-approximation .definition name="Penalty function approximation"}

For a convex *penalty function* $\phi:\mathbb{R}\to\mathbb{R}$, minimize
$$\phi(r_1)+\cdots+\phi(r_m)\quad\text{subject to }r=Ax-b.$$
Examples: quadratic $\phi(u)=u^2$; dead zone linear $\phi(u)=\max\{0,\lvert u\rvert-a\}$; log barrier $\phi(u)=-a^2\log(1-(u/a)^2)$ for $\lvert u\rvert<a$; and the *Huber* penalty
$$\phi_M(u)=\begin{cases}u^2&\lvert u\rvert\le M,\\M(2\lvert u\rvert-M)&\lvert u\rvert>M,\end{cases}$$
quadratic for small residuals and linear for large ones, so robust to outliers.

:::

::: {#fig-norm-approximation-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-1.8,0) -- (1.9,0) node[lab, right] {$u$};
\draw[->, faint] (0,-0.2) -- (0,2.2) node[lab, above] {$\phi(u)$};
\draw[emph] (-1.4,1.96) -- (-1.35,1.83) -- (-1.3,1.7) -- (-1.26,1.58) -- (-1.21,1.46) -- (-1.16,1.35) -- (-1.11,1.24) -- (-1.06,1.13) -- (-1.02,1.03) -- (-0.97,0.93) -- (-0.92,0.84) -- (-0.87,0.76) -- (-0.82,0.68) -- (-0.77,0.6) -- (-0.72,0.53) -- (-0.68,0.46) -- (-0.63,0.39) -- (-0.58,0.34) -- (-0.53,0.28) -- (-0.48,0.23) -- (-0.44,0.19) -- (-0.39,0.15) -- (-0.34,0.11) -- (-0.29,0.08) -- (-0.24,0.06) -- (-0.19,0.04) -- (-0.15,0.02) -- (-0.1,0.01) -- (-0.05,0) -- (0,0) -- (0.05,0) -- (0.1,0.01) -- (0.15,0.02) -- (0.19,0.04) -- (0.24,0.06) -- (0.29,0.08) -- (0.34,0.11) -- (0.39,0.15) -- (0.44,0.19) -- (0.48,0.23) -- (0.53,0.28) -- (0.58,0.34) -- (0.63,0.39) -- (0.68,0.46) -- (0.72,0.53) -- (0.77,0.6) -- (0.82,0.68) -- (0.87,0.76) -- (0.92,0.84) -- (0.97,0.93) -- (1.02,1.03) -- (1.06,1.13) -- (1.11,1.24) -- (1.16,1.35) -- (1.21,1.46) -- (1.26,1.58) -- (1.3,1.7) -- (1.35,1.83) -- (1.4,1.96);
\draw[faint] (-1.7,1.2) -- (-0.5,0) -- (0.5,0) -- (1.7,1.2);
\draw[hl] (-0.59,1.23) -- (-0.58,0.98) -- (-0.57,0.84) -- (-0.56,0.74) -- (-0.55,0.66) -- (-0.54,0.6) -- (-0.53,0.55) -- (-0.52,0.51) -- (-0.51,0.47) -- (-0.5,0.43) -- (-0.49,0.4) -- (-0.48,0.37) -- (-0.47,0.35) -- (-0.46,0.32) -- (-0.45,0.3) -- (-0.44,0.28) -- (-0.43,0.26) -- (-0.42,0.25) -- (-0.41,0.23) -- (-0.4,0.22) -- (-0.39,0.2) -- (-0.38,0.19) -- (-0.37,0.18) -- (-0.36,0.17) -- (-0.35,0.15) -- (-0.34,0.14) -- (-0.33,0.13) -- (-0.32,0.12) -- (-0.31,0.12) -- (-0.3,0.11) -- (-0.29,0.1) -- (-0.29,0.09) -- (-0.28,0.09) -- (-0.27,0.08) -- (-0.26,0.07) -- (-0.25,0.07) -- (-0.24,0.06) -- (-0.23,0.06) -- (-0.22,0.05) -- (-0.21,0.05) -- (-0.2,0.04) -- (-0.19,0.04) -- (-0.18,0.03) -- (-0.17,0.03) -- (-0.16,0.03) -- (-0.15,0.02) -- (-0.14,0.02) -- (-0.13,0.02) -- (-0.12,0.01) -- (-0.11,0.01) -- (-0.1,0.01) -- (-0.09,0.01) -- (-0.08,0.01) -- (-0.07,0) -- (-0.06,0) -- (-0.05,0) -- (-0.04,0) -- (-0.03,0) -- (-0.02,0) -- (-0.01,0) -- (0,0) -- (0.01,0) -- (0.02,0) -- (0.03,0) -- (0.04,0) -- (0.05,0) -- (0.06,0) -- (0.07,0) -- (0.08,0.01) -- (0.09,0.01) -- (0.1,0.01) -- (0.11,0.01) -- (0.12,0.01) -- (0.13,0.02) -- (0.14,0.02) -- (0.15,0.02) -- (0.16,0.03) -- (0.17,0.03) -- (0.18,0.03) -- (0.19,0.04) -- (0.2,0.04) -- (0.21,0.05) -- (0.22,0.05) -- (0.23,0.06) -- (0.24,0.06) -- (0.25,0.07) -- (0.26,0.07) -- (0.27,0.08) -- (0.28,0.09) -- (0.29,0.09) -- (0.29,0.1) -- (0.3,0.11) -- (0.31,0.12) -- (0.32,0.12) -- (0.33,0.13) -- (0.34,0.14) -- (0.35,0.15) -- (0.36,0.17) -- (0.37,0.18) -- (0.38,0.19) -- (0.39,0.2) -- (0.4,0.22) -- (0.41,0.23) -- (0.42,0.25) -- (0.43,0.26) -- (0.44,0.28) -- (0.45,0.3) -- (0.46,0.32) -- (0.47,0.35) -- (0.48,0.37) -- (0.49,0.4) -- (0.5,0.43) -- (0.51,0.47) -- (0.52,0.51) -- (0.53,0.55) -- (0.54,0.6) -- (0.55,0.66) -- (0.56,0.74) -- (0.57,0.84) -- (0.58,0.98) -- (0.59,1.23);
\node[lab, right] at (1.45,2.1) {$u^2$};
\node[lab, right] at (1.7,1.2) {dead zone};
\node[lab, left] at (-0.6,1.6) {log barrier};
\end{tikzpicture}
\end{center}
```

Three penalty functions: quadratic $u^2$, dead zone linear with $a=0.5$ (no cost for $\lvert u\rvert\le a$), and log barrier with $a=0.6$ (infinite cost for $\lvert u\rvert\ge a$).

:::

::: {#prp-penalty-shapes .proposition name="Optimality condition for penalty approximation"}

If $\phi$ is convex and differentiable, $x$ solves @def-penalty-function-approximation if and only if
$$\sum_{i=1}^m\phi'(r_i)\,a_i=0,\qquad r=Ax-b,$$
where $a_i^{\mathsf T}$ are the rows of $A$.

:::

::: {.proof}

1. The objective $F(x)=\sum_i\phi(a_i^{\mathsf T}x-b_i)$ is convex (@prp-nonnegative-sum-affine-composition) and differentiable with $\nabla F(x)=\sum_i\phi'(r_i)a_i$ by the chain rule.

2. A differentiable convex function is minimized exactly where its gradient vanishes (@cor-convex-stationary-global and @thm-convex-optimality-criterion).

:::

::: {#rmk-norm-approximation-2 .remark name="How the penalty shapes the residuals"}

Each residual pulls on the balance with weight $\phi'(r_i)$. A penalty that grows fast (quadratic, log barrier) makes large residuals very costly, so it avoids them. A penalty that grows only linearly (Huber, $\ell_1$) gives a large residual bounded pull, so a few outliers are tolerated. A penalty with a corner at $0$ ($\ell_1$, dead zone at its edges) lets many residuals sit exactly there.

:::

::: {#fig-norm-approximation-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-2.08,0) -- (2.08,0);
\fill[bar] (-2,0) rectangle (-1.8,0.06);
\fill[bar] (-1.8,0) rectangle (-1.6,0.06);
\fill[bar] (-1.4,0) rectangle (-1.2,0.12);
\fill[bar] (-1.2,0) rectangle (-1,0.24);
\fill[bar] (-1,0) rectangle (-0.8,0.12);
\fill[bar] (-0.8,0) rectangle (-0.6,0.42);
\fill[bar] (-0.6,0) rectangle (-0.4,0.66);
\fill[bar] (-0.4,0) rectangle (-0.2,0.48);
\fill[bar] (-0.2,0) rectangle (0,0.42);
\fill[bar] (0,0) rectangle (0.2,0.72);
\fill[bar] (0.2,0) rectangle (0.4,0.78);
\fill[bar] (0.4,0) rectangle (0.6,0.6);
\fill[bar] (0.6,0) rectangle (0.8,0.48);
\fill[bar] (0.8,0) rectangle (1,0.18);
\fill[bar] (1,0) rectangle (1.2,0.36);
\fill[bar] (1.2,0) rectangle (1.4,0.12);
\fill[bar] (1.4,0) rectangle (1.6,0.12);
\fill[bar] (1.6,0) rectangle (1.8,0.06);
\node[lab] at (0,-0.3) {$\ell_2$ residuals};
\node[lab, tick] at (-1.6,-0.15) {$-2$};
\node[lab, tick] at (1.6,-0.15) {$2$};
\end{tikzpicture}
\hspace{1.2em}
\begin{tikzpicture}
\draw[faint] (-2.08,0) -- (2.08,0);
\fill[bar] (-2,0) rectangle (-1.8,0.06);
\fill[bar] (-1.6,0) rectangle (-1.4,0.12);
\fill[bar] (-1.2,0) rectangle (-1,0.42);
\fill[bar] (-1,0) rectangle (-0.8,0.18);
\fill[bar] (-0.8,0) rectangle (-0.6,0.06);
\fill[bar] (-0.6,0) rectangle (-0.4,0.36);
\fill[bar] (-0.4,0) rectangle (-0.2,0.54);
\fill[bar] (-0.2,0) rectangle (0,0.96);
\fill[bar] (0,0) rectangle (0.2,1.5);
\fill[bar] (0.2,0) rectangle (0.4,0.3);
\fill[bar] (0.4,0) rectangle (0.6,0.18);
\fill[bar] (0.6,0) rectangle (0.8,0.36);
\fill[bar] (0.8,0) rectangle (1,0.3);
\fill[bar] (1,0) rectangle (1.2,0.12);
\fill[bar] (1.2,0) rectangle (1.4,0.12);
\fill[bar] (1.4,0) rectangle (1.6,0.24);
\fill[bar] (1.6,0) rectangle (1.8,0.06);
\node[lab] at (0,-0.3) {$\ell_1$ residuals};
\node[lab, tick] at (-1.6,-0.15) {$-2$};
\node[lab, tick] at (1.6,-0.15) {$2$};
\end{tikzpicture}
\end{center}
```

Residual histograms for a random $100\times30$ problem. The $\ell_2$ fit spreads residuals in a bell shape; the $\ell_1$ fit makes many residuals exactly zero (30 of 100, the tall middle bar) and tolerates a few larger ones.

:::

::: {#exm-huber-line-fit .example name="Line fitting with an outlier"}

Fit $y\approx\alpha+\beta t$ to the seven points $(t,t)$, $t=0,\dots,5$, and the outlier $(6,-6)$. Least squares gives $\alpha=15/7\approx2.14$, $\beta=-2/7\approx-0.29$: the outlier reverses the slope. The Huber fit with $M=1$ gives $\alpha=1/3$, $\beta=0.8$, and the $\ell_1$ fit recovers $\alpha=0$, $\beta=1$ exactly (values computed numerically).

:::

::: {#fig-norm-approximation-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[y=0.45cm]
\draw[->, faint] (-0.4,0) -- (6.8,0) node[lab, right] {$t$};
\draw[->, faint] (0,-6.6) -- (0,5.6) node[lab, above] {$y$};
\fill[ink] (0,0) circle[pt];
\fill[ink] (1,1) circle[pt];
\fill[ink] (2,2) circle[pt];
\fill[ink] (3,3) circle[pt];
\fill[ink] (4,4) circle[pt];
\fill[ink] (5,5) circle[pt];
\fill[accent] (6,-6) circle[pt];
\draw[faint] (-0.2,2.2) -- (3.2,1.23) -- (6.6,0.26);
\draw[hl] (-0.2,0.17) -- (3.2,2.89) -- (6.6,5.61);
\node[lab, right] at (6.6,0.26) {least squares};
\node[lab, right] at (6.6,5.61) {Huber};
\node[lab, left] at (6,-6) {outlier};
\end{tikzpicture}
\end{center}
```

Line fitting with one outlier: least squares ($\alpha=15/7$, $\beta=-2/7$) is pulled so far that the slope turns negative; the Huber fit ($M=1$, $\alpha=1/3$, $\beta=0.8$) charges the outlier only linearly and stays close to the other six points.

:::

::: {#def-least-norm .definition name="Least-norm problems"}

For $A\in\mathbb{R}^{m\times n}$ with $m\le n$ and $Ax=b$ solvable, the *least-norm problem* is minimize $\lVert x\rVert$ subject to $Ax=b$. With $\lVert\cdot\rVert_2$ the solution is $x=A^{\mathsf T}(AA^{\mathsf T})^{-1}b$ (when $A$ has full row rank); with $\lVert\cdot\rVert_1$ it is an LP whose solutions tend to be sparse.

:::

::: {.proof}

1. Least Euclidean norm: the KKT conditions (@thm-kkt) for minimizing $x^{\mathsf T}x$ subject to $Ax=b$ are $2x+A^{\mathsf T}\nu=0$, $Ax=b$.

2. So $x=-\frac12A^{\mathsf T}\nu$ and $-\frac12AA^{\mathsf T}\nu=b$, giving $\nu=-2(AA^{\mathsf T})^{-1}b$ and $x=A^{\mathsf T}(AA^{\mathsf T})^{-1}b$.

:::

::: {#fig-norm-approximation-4}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.5]
\draw[->, faint] (-1,0) -- (2.8,0) node[lab, right] {$x_1$};
\draw[->, faint] (0,-0.6) -- (0,1.8) node[lab, above] {$x_2$};
\draw[emph] (-0.6,1.3) -- (1,0.5) -- (2.6,-0.3);
\node[lab, right] at (2.6,-0.3) {$Ax=b$};
\draw[faint] (0,0) circle (0.89);
\fill[accent] (0.4,0.8) circle[pt] node[lab, above right] {$\ell_2$};
\draw[faint] (1,0) -- (0,1) -- (-1,0) -- (0,-1) -- cycle;
\fill[accent] (0,1) circle[pt] node[lab, above left] {$\ell_1$};
\end{tikzpicture}
\end{center}
```

Least-norm solutions of one equation $x_1+2x_2=2$: the smallest $\ell_2$ ball touching the line does so at the projection $(0.4,0.8)$; the smallest $\ell_1$ ball touches at a corner, $(0,1)$, giving a sparse solution.

:::

::: {#rmk-norm-approximation-1 .remark name="Interpretations"}

Norm approximation can be read as estimation ($b=Ax+v$ with $v$ a measurement error, @sec-math-optimization-applications-statistical-estimation), as geometry (the point of $\operatorname{range}A$ nearest $b$), or as design ($x$ are design variables, $Ax$ the result, $b$ the target).

:::
