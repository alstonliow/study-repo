---
title: "Statistical Estimation and Detection"
sources: [ee364a-7]
requires: [math/optimization/applications/norm-approximation, math/optimization/convex-functions/log-concave-functions]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on statistical estimation, in our own wording; proofs written out in steps. Logistic regression as a learning method is in @sec-ai-machine-learning-logistic-regression. -->

Maximum likelihood estimation is a convex problem whenever the log-likelihood is concave in the parameters, which happens for linear measurements with log-concave noise and for logistic models. Choosing a detector that trades off error probabilities is also convex.

::: {#def-maximum-likelihood-estimation .definition name="Maximum likelihood estimation" related="def-estimator-properties"}

For a family of densities $p_x(y)$ indexed by $x\in C$, the *maximum likelihood* (ML) estimate from an observation $y$ is
$$\hat x_{\rm ml}=\operatorname*{argmax}_{x\in C}\ \ell(x),\qquad\ell(x)=\log p_x(y).$$
This is a convex problem when $\ell$ is concave in $x$ for each $y$ and $C$ is convex.

:::

::: {#prp-ml-linear-measurements .proposition name="Linear measurements with IID noise"}

Let $y_i=a_i^{\mathsf T}x+v_i$, $i=1,\dots,m$, with independent noise of density $p$. Then
$$\ell(x)=\sum_{i=1}^m\log p(y_i-a_i^{\mathsf T}x),$$
which is concave in $x$ when $p$ is log-concave. Gaussian noise gives least squares, Laplacian noise ($p(z)\propto e^{-\lvert z\rvert/a}$) gives $\ell_1$-norm approximation, and uniform noise on $[-a,a]$ gives any $x$ with $\lVert Ax-y\rVert_\infty\le a$.

:::

::: {.proof}

1. Independence makes the joint density the product $\prod_ip(y_i-a_i^{\mathsf T}x)$; its logarithm is the stated sum.

2. Each term is a concave function ($\log p$) of an affine function of $x$, so the sum is concave (@prp-nonnegative-sum-affine-composition).

3. Gaussian: $\log p(z)=-z^2/(2\sigma^2)+\text{const}$, so maximizing $\ell$ is minimizing $\sum_ir_i^2$. Laplacian: $-\lvert z\rvert/a+\text{const}$ gives $\sum_i\lvert r_i\rvert$. Uniform: $\ell$ is a constant on $\{\lvert r_i\rvert\le a\}$ and $-\infty$ elsewhere.

:::

::: {#fig-statistical-estimation-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-2.6,0) -- (2.8,0) node[lab, right] {$v$};
\draw[->, faint] (0,-0.1) -- (0,1.2) node[lab, above] {};
\draw[emph] (-2.5,0.04) -- (-2.42,0.05) -- (-2.33,0.06) -- (-2.25,0.07) -- (-2.17,0.09) -- (-2.08,0.1) -- (-2,0.12) -- (-1.92,0.14) -- (-1.83,0.17) -- (-1.75,0.19) -- (-1.67,0.22) -- (-1.58,0.26) -- (-1.5,0.29) -- (-1.42,0.33) -- (-1.33,0.37) -- (-1.25,0.41) -- (-1.17,0.46) -- (-1.08,0.5) -- (-1,0.55) -- (-0.92,0.59) -- (-0.83,0.64) -- (-0.75,0.68) -- (-0.67,0.72) -- (-0.58,0.76) -- (-0.5,0.79) -- (-0.42,0.83) -- (-0.33,0.85) -- (-0.25,0.87) -- (-0.17,0.89) -- (-0.08,0.9) -- (0,0.9) -- (0.08,0.9) -- (0.17,0.89) -- (0.25,0.87) -- (0.33,0.85) -- (0.42,0.83) -- (0.5,0.79) -- (0.58,0.76) -- (0.67,0.72) -- (0.75,0.68) -- (0.83,0.64) -- (0.92,0.59) -- (1,0.55) -- (1.08,0.5) -- (1.17,0.46) -- (1.25,0.41) -- (1.33,0.37) -- (1.42,0.33) -- (1.5,0.29) -- (1.58,0.26) -- (1.67,0.22) -- (1.75,0.19) -- (1.83,0.17) -- (1.92,0.14) -- (2,0.12) -- (2.08,0.1) -- (2.17,0.09) -- (2.25,0.07) -- (2.33,0.06) -- (2.42,0.05) -- (2.5,0.04);
\draw[hl] (-2.5,0.03) -- (-2.46,0.03) -- (-2.42,0.03) -- (-2.38,0.04) -- (-2.33,0.04) -- (-2.29,0.04) -- (-2.25,0.04) -- (-2.21,0.05) -- (-2.17,0.05) -- (-2.12,0.05) -- (-2.08,0.05) -- (-2.04,0.06) -- (-2,0.06) -- (-1.96,0.06) -- (-1.92,0.07) -- (-1.88,0.07) -- (-1.83,0.08) -- (-1.79,0.08) -- (-1.75,0.09) -- (-1.71,0.09) -- (-1.67,0.1) -- (-1.62,0.1) -- (-1.58,0.11) -- (-1.54,0.12) -- (-1.5,0.12) -- (-1.46,0.13) -- (-1.42,0.14) -- (-1.38,0.15) -- (-1.33,0.15) -- (-1.29,0.16) -- (-1.25,0.17) -- (-1.21,0.18) -- (-1.17,0.2) -- (-1.12,0.21) -- (-1.08,0.22) -- (-1.04,0.23) -- (-1,0.25) -- (-0.96,0.26) -- (-0.92,0.28) -- (-0.88,0.29) -- (-0.83,0.31) -- (-0.79,0.33) -- (-0.75,0.35) -- (-0.71,0.37) -- (-0.67,0.39) -- (-0.62,0.42) -- (-0.58,0.44) -- (-0.54,0.47) -- (-0.5,0.5) -- (-0.46,0.53) -- (-0.42,0.56) -- (-0.38,0.59) -- (-0.33,0.63) -- (-0.29,0.66) -- (-0.25,0.7) -- (-0.21,0.75) -- (-0.17,0.79) -- (-0.12,0.84) -- (-0.08,0.89) -- (-0.04,0.94) -- (0,1) -- (0.04,0.94) -- (0.08,0.89) -- (0.12,0.84) -- (0.17,0.79) -- (0.21,0.75) -- (0.25,0.7) -- (0.29,0.66) -- (0.33,0.63) -- (0.38,0.59) -- (0.42,0.56) -- (0.46,0.53) -- (0.5,0.5) -- (0.54,0.47) -- (0.58,0.44) -- (0.62,0.42) -- (0.67,0.39) -- (0.71,0.37) -- (0.75,0.35) -- (0.79,0.33) -- (0.83,0.31) -- (0.88,0.29) -- (0.92,0.28) -- (0.96,0.26) -- (1,0.25) -- (1.04,0.23) -- (1.08,0.22) -- (1.12,0.21) -- (1.17,0.2) -- (1.21,0.18) -- (1.25,0.17) -- (1.29,0.16) -- (1.33,0.15) -- (1.38,0.15) -- (1.42,0.14) -- (1.46,0.13) -- (1.5,0.12) -- (1.54,0.12) -- (1.58,0.11) -- (1.62,0.1) -- (1.67,0.1) -- (1.71,0.09) -- (1.75,0.09) -- (1.79,0.08) -- (1.83,0.08) -- (1.88,0.07) -- (1.92,0.07) -- (1.96,0.06) -- (2,0.06) -- (2.04,0.06) -- (2.08,0.05) -- (2.12,0.05) -- (2.17,0.05) -- (2.21,0.05) -- (2.25,0.04) -- (2.29,0.04) -- (2.33,0.04) -- (2.38,0.04) -- (2.42,0.03) -- (2.46,0.03) -- (2.5,0.03);
\draw[faint] (-2.5,0) -- (-1,0) -- (-1,0.5) -- (1,0.5) -- (1,0) -- (2.5,0);
\node[lab] at (0,-0.35) {densities};
\end{tikzpicture}
\hspace{1.2em}
\begin{tikzpicture}
\draw[->, faint] (-2.6,0) -- (2.8,0) node[lab, right] {$v$};
\draw[->, faint] (0,-0.2) -- (0,2.6) node[lab, above] {};
\draw[emph] (-2.2,2.42) -- (-2.13,2.26) -- (-2.05,2.11) -- (-1.98,1.96) -- (-1.91,1.82) -- (-1.83,1.68) -- (-1.76,1.55) -- (-1.69,1.42) -- (-1.61,1.3) -- (-1.54,1.19) -- (-1.47,1.08) -- (-1.39,0.97) -- (-1.32,0.87) -- (-1.25,0.78) -- (-1.17,0.69) -- (-1.1,0.61) -- (-1.03,0.53) -- (-0.95,0.45) -- (-0.88,0.39) -- (-0.81,0.33) -- (-0.73,0.27) -- (-0.66,0.22) -- (-0.59,0.17) -- (-0.51,0.13) -- (-0.44,0.1) -- (-0.37,0.07) -- (-0.29,0.04) -- (-0.22,0.02) -- (-0.15,0.01) -- (-0.07,0) -- (0,0) -- (0.07,0) -- (0.15,0.01) -- (0.22,0.02) -- (0.29,0.04) -- (0.37,0.07) -- (0.44,0.1) -- (0.51,0.13) -- (0.59,0.17) -- (0.66,0.22) -- (0.73,0.27) -- (0.81,0.33) -- (0.88,0.39) -- (0.95,0.45) -- (1.03,0.53) -- (1.1,0.61) -- (1.17,0.69) -- (1.25,0.78) -- (1.32,0.87) -- (1.39,0.97) -- (1.47,1.08) -- (1.54,1.19) -- (1.61,1.3) -- (1.69,1.42) -- (1.76,1.55) -- (1.83,1.68) -- (1.91,1.82) -- (1.98,1.96) -- (2.05,2.11) -- (2.13,2.26) -- (2.2,2.42);
\draw[hl] (-1.8,2.5) -- (0,0) -- (1.8,2.5);
\draw[faint] (-2.5,2.5) -- (-1,2.5) (-1,2.5) -- (-1,0) -- (1,0) -- (1,2.5);
\node[lab] at (0,-0.45) {penalties $-\log p$};
\end{tikzpicture}
\end{center}
```

Noise densities and the penalties $-\log p$ they induce in ML estimation: Gaussian noise gives the quadratic penalty (least squares), Laplacian noise (thick) the absolute value ($\ell_1$), and uniform noise on $[-1,1]$ (thin) a hard bound $\lvert v\rvert\le1$ with no cost inside.

:::

::: {#exm-logistic-ml .example name="Logistic regression as ML"}

A binary $y\in\{0,1\}$ has $\operatorname{P}(y=1)=\frac{e^{a^{\mathsf T}u+b}}{1+e^{a^{\mathsf T}u+b}}$ for explanatory variable $u$. With data $(u_i,y_i)$ ordered so that $y_1=\dots=y_k=1$ and $y_{k+1}=\dots=y_m=0$,
$$\ell(a,b)=\sum_{i=1}^k(a^{\mathsf T}u_i+b)-\sum_{i=1}^m\log\big(1+e^{a^{\mathsf T}u_i+b}\big),$$
concave in $(a,b)$ since $\log(1+e^z)$ is convex (log-sum-exp of $0$ and $z$).

:::

::: {#fig-statistical-estimation-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (4.4,0) node[lab, right] {$u$};
\draw[->, faint] (0,-0.2) -- (0,1.6) node[lab, above] {};
\fill[accent] (0.22,0) circle[pt];
\fill[accent] (0.37,0) circle[pt];
\fill[accent] (0.42,0) circle[pt];
\fill[accent] (0.43,0) circle[pt];
\fill[accent] (0.6,0) circle[pt];
\fill[accent] (0.75,0) circle[pt];
\fill[accent] (0.75,0) circle[pt];
\fill[accent] (0.81,0) circle[pt];
\fill[accent] (1.05,0) circle[pt];
\fill[accent] (1.1,1.2) circle[pt];
\fill[accent] (1.19,0) circle[pt];
\fill[accent] (1.27,0) circle[pt];
\fill[accent] (1.38,0) circle[pt];
\fill[accent] (1.57,0) circle[pt];
\fill[accent] (1.63,0) circle[pt];
\fill[accent] (1.69,0) circle[pt];
\fill[accent] (1.73,0) circle[pt];
\fill[accent] (1.75,0) circle[pt];
\fill[accent] (1.88,1.2) circle[pt];
\fill[accent] (2.04,1.2) circle[pt];
\fill[accent] (2.07,1.2) circle[pt];
\fill[accent] (2.25,1.2) circle[pt];
\fill[accent] (2.37,1.2) circle[pt];
\fill[accent] (2.4,1.2) circle[pt];
\fill[accent] (2.53,1.2) circle[pt];
\fill[accent] (2.58,1.2) circle[pt];
\fill[accent] (2.63,1.2) circle[pt];
\fill[accent] (2.68,1.2) circle[pt];
\fill[accent] (2.72,1.2) circle[pt];
\fill[accent] (2.73,1.2) circle[pt];
\fill[accent] (2.78,1.2) circle[pt];
\fill[accent] (2.91,1.2) circle[pt];
\fill[accent] (3.1,1.2) circle[pt];
\fill[accent] (3.26,1.2) circle[pt];
\fill[accent] (3.4,1.2) circle[pt];
\fill[accent] (3.45,1.2) circle[pt];
\fill[accent] (3.54,1.2) circle[pt];
\fill[accent] (3.56,1.2) circle[pt];
\fill[accent] (3.7,1.2) circle[pt];
\fill[accent] (3.87,1.2) circle[pt];
\draw[emph] (0,0) -- (0.04,0) -- (0.08,0) -- (0.12,0) -- (0.16,0) -- (0.2,0) -- (0.24,0) -- (0.28,0) -- (0.32,0) -- (0.36,0) -- (0.4,0) -- (0.44,0) -- (0.48,0) -- (0.52,0) -- (0.56,0) -- (0.6,0) -- (0.64,0) -- (0.68,0) -- (0.72,0.01) -- (0.76,0.01) -- (0.8,0.01) -- (0.84,0.01) -- (0.88,0.01) -- (0.92,0.01) -- (0.96,0.02) -- (1,0.02) -- (1.04,0.03) -- (1.08,0.03) -- (1.12,0.04) -- (1.16,0.05) -- (1.2,0.06) -- (1.24,0.07) -- (1.28,0.08) -- (1.32,0.1) -- (1.36,0.12) -- (1.4,0.15) -- (1.44,0.17) -- (1.48,0.21) -- (1.52,0.24) -- (1.56,0.28) -- (1.6,0.33) -- (1.64,0.38) -- (1.68,0.43) -- (1.72,0.49) -- (1.76,0.55) -- (1.8,0.61) -- (1.84,0.67) -- (1.88,0.73) -- (1.92,0.79) -- (1.96,0.84) -- (2,0.89) -- (2.04,0.93) -- (2.08,0.97) -- (2.12,1.01) -- (2.16,1.04) -- (2.2,1.06) -- (2.24,1.09) -- (2.28,1.1) -- (2.32,1.12) -- (2.36,1.13) -- (2.4,1.15) -- (2.44,1.16) -- (2.48,1.16) -- (2.52,1.17) -- (2.56,1.18) -- (2.6,1.18) -- (2.64,1.18) -- (2.68,1.19) -- (2.72,1.19) -- (2.76,1.19) -- (2.8,1.19) -- (2.84,1.19) -- (2.88,1.19) -- (2.92,1.2) -- (2.96,1.2) -- (3,1.2) -- (3.04,1.2) -- (3.08,1.2) -- (3.12,1.2) -- (3.16,1.2) -- (3.2,1.2) -- (3.24,1.2) -- (3.28,1.2) -- (3.32,1.2) -- (3.36,1.2) -- (3.4,1.2) -- (3.44,1.2) -- (3.48,1.2) -- (3.52,1.2) -- (3.56,1.2) -- (3.6,1.2) -- (3.64,1.2) -- (3.68,1.2) -- (3.72,1.2) -- (3.76,1.2) -- (3.8,1.2) -- (3.84,1.2) -- (3.88,1.2) -- (3.92,1.2) -- (3.96,1.2) -- (4,1.2);
\node[lab, tick, left] at (0,1.2) {$1$};
\node[lab, right] at (4,0.95) {$\mathrm P(y=1)$};
\end{tikzpicture}
\end{center}
```

Logistic regression: forty observations $(u_i,y_i)$ with $y_i\in\{0,1\}$ (dots) and the maximum-likelihood fit $\mathrm P(y=1)=e^{au+b}/(1+e^{au+b})$, here $a\approx2.01$, $b\approx-9.01$.

:::

::: {#def-hypothesis-testing-randomized .definition name="Randomized detector"}

A random variable $X\in\{1,\dots,n\}$ has distribution $p$ or $q$ (hypotheses $1$ and $2$), the columns of $P=[p\ q]\in\mathbb{R}^{n\times2}$. A *randomized detector* is a matrix $T\in\mathbb{R}^{2\times n}$ with nonnegative entries and columns summing to $1$; on observing $X=k$ it guesses hypothesis $i$ with probability $t_{ik}$. The *detection probability matrix* $D=TP$ has the error probabilities $P_{\rm fp}=D_{21}$ and $P_{\rm fn}=D_{12}$ off the diagonal.

:::

::: {#thm-optimal-detector-lp .theorem name="Optimal detectors by LP"}

Minimizing $P_{\rm fp}+\lambda P_{\rm fn}$ over randomized detectors, $\lambda>0$, is an LP whose solution is deterministic: guess hypothesis $1$ when $p_k\ge\lambda q_k$ and hypothesis $2$ otherwise (a likelihood ratio test).

:::

::: {.proof}

1. $P_{\rm fp}+\lambda P_{\rm fn}=\sum_k(t_{2k}p_k+\lambda t_{1k}q_k)$ is linear in $T$, and the constraints $t_{1k}+t_{2k}=1$, $t_{ik}\ge0$ are linear, so the problem is an LP.

2. The objective separates over $k$: for each $k$ choose $(t_{1k},t_{2k})$ on the segment $t_{1k}+t_{2k}=1$ to minimize $t_{2k}p_k+t_{1k}\lambda q_k$.

3. A linear function on a segment is minimized at an endpoint: $t_{1k}=1$ if $\lambda q_k\le p_k$, and $t_{2k}=1$ otherwise.

:::

::: {#fig-statistical-estimation-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.1,0) -- (2.9,0) node[lab, right] {$P_{\rm fp}$};
\draw[->, faint] (0,-0.1) -- (0,2.9) node[lab, above] {$P_{\rm fn}$};
\draw[hl] (0,2.6) -- (0.13,1.3) -- (0.52,0.52) -- (1.3,0.13) -- (2.6,0);
\fill[ink] (0,2.6) circle[pt];
\fill[ink] (0.13,1.3) circle[pt];
\fill[ink] (0.52,0.52) circle[pt];
\fill[ink] (1.3,0.13) circle[pt];
\fill[ink] (2.6,0) circle[pt];
\fill[tintA] (0,2.6) -- (0.13,1.3) -- (0.52,0.52) -- (1.3,0.13) -- (2.6,0) -- (2.6,2.6) -- cycle;
\node[lab] at (1.7,1.7) {randomized};
\node[lab, tick] at (2.6,-0.2) {1};
\node[lab, tick, left] at (0,2.6) {1};
\end{tikzpicture}
\end{center}
```

Error probabilities of detectors for two distributions on four outcomes. The dots are the deterministic likelihood ratio tests, the shaded region what randomized detectors can reach, and its lower-left boundary (thick) the optimal trade-off: minimizing $P_{\rm fp}+\lambda P_{\rm fn}$ picks a vertex, as the theorem says.

:::

::: {#rmk-statistical-estimation-1 .remark name="MAP estimation"}

With a prior density $p_{\rm prior}(x)$, the maximum a posteriori estimate maximizes $\log p_x(y)+\log p_{\rm prior}(x)$. A log-concave prior keeps the problem convex; a Gaussian prior adds a Tikhonov term (@def-regularized-approximation).

:::
