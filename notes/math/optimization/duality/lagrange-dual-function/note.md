---
title: "The Lagrange Dual Function"
sources: [ee364a-5]
requires: [math/optimization/convex-problems/optimization-problems, math/optimization/convex-functions/conjugate-function]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on duality, in our own wording; proofs written out in steps. Lagrange multipliers for equality constraints in calculus are in @sec-math-calculus-multivariable-differentiation-lagrange-multipliers. -->

Adding the constraints to the objective with weights gives the Lagrangian. Minimizing it over $x$ gives a concave function of the weights whose every value is a lower bound on the optimal value, for any problem, convex or not.

::: {#def-lagrangian .definition name="Lagrangian, dual function" related="thm-lagrange-multipliers"}

For the problem of @def-optimization-problem with domain $\mathcal D$, the *Lagrangian* $L:\mathbb{R}^n\times\mathbb{R}^m\times\mathbb{R}^p\to\mathbb{R}$ is
$$L(x,\lambda,\nu)=f_0(x)+\sum_{i=1}^m\lambda_if_i(x)+\sum_{i=1}^p\nu_ih_i(x),$$
with *Lagrange multipliers* (dual variables) $\lambda_i$ and $\nu_i$. The *Lagrange dual function* is
$$g(\lambda,\nu)=\inf_{x\in\mathcal D}L(x,\lambda,\nu).$$
It is concave, as a pointwise infimum of affine functions of $(\lambda,\nu)$, and may take the value $-\infty$.

:::

::: {#fig-lagrange-dual-function-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-1.2,0) -- (3,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.4) -- (0,3.2) node[lab, above] {$y$};
\fill[tintA] (1,0) rectangle (2.8,3);
\draw[emph] (-1,1) -- (-0.95,0.91) -- (-0.91,0.83) -- (-0.86,0.74) -- (-0.82,0.67) -- (-0.77,0.59) -- (-0.72,0.53) -- (-0.68,0.46) -- (-0.63,0.4) -- (-0.59,0.35) -- (-0.54,0.29) -- (-0.5,0.25) -- (-0.45,0.2) -- (-0.4,0.16) -- (-0.36,0.13) -- (-0.31,0.1) -- (-0.27,0.07) -- (-0.22,0.05) -- (-0.18,0.03) -- (-0.13,0.02) -- (-0.08,0.01) -- (-0.04,0) -- (0.01,0) -- (0.05,0) -- (0.1,0.01) -- (0.15,0.02) -- (0.19,0.04) -- (0.24,0.06) -- (0.28,0.08) -- (0.33,0.11) -- (0.38,0.14) -- (0.42,0.18) -- (0.47,0.22) -- (0.51,0.26) -- (0.56,0.31) -- (0.6,0.37) -- (0.65,0.42) -- (0.7,0.48) -- (0.74,0.55) -- (0.79,0.62) -- (0.83,0.69) -- (0.88,0.77) -- (0.93,0.86) -- (0.97,0.94) -- (1.02,1.03) -- (1.06,1.13) -- (1.11,1.23) -- (1.15,1.33) -- (1.2,1.44) -- (1.25,1.55) -- (1.29,1.67) -- (1.34,1.79) -- (1.38,1.91) -- (1.43,2.04) -- (1.48,2.18) -- (1.52,2.31) -- (1.57,2.45) -- (1.61,2.6) -- (1.66,2.75) -- (1.7,2.9) -- (1.75,3.06);
\draw[faint, dashed] (-1,1) -- (2.8,1) node[lab, right] {$p^\star$};
\draw[faint] (-1,3) -- (-0.94,2.82) -- (-0.88,2.65) -- (-0.82,2.49) -- (-0.76,2.34) -- (-0.7,2.19) -- (-0.64,2.05) -- (-0.58,1.92) -- (-0.52,1.79) -- (-0.46,1.67) -- (-0.4,1.56) -- (-0.34,1.46) -- (-0.28,1.36) -- (-0.22,1.27) -- (-0.16,1.19) -- (-0.1,1.11) -- (-0.04,1.04) -- (0.02,0.98) -- (0.08,0.93) -- (0.14,0.88) -- (0.2,0.84) -- (0.26,0.81) -- (0.32,0.78) -- (0.38,0.76) -- (0.44,0.75) -- (0.5,0.75) -- (0.56,0.75) -- (0.62,0.76) -- (0.68,0.78) -- (0.74,0.81) -- (0.8,0.84) -- (0.86,0.88) -- (0.92,0.93) -- (0.98,0.98) -- (1.04,1.04) -- (1.1,1.11) -- (1.16,1.19) -- (1.22,1.27) -- (1.28,1.36) -- (1.34,1.46) -- (1.4,1.56) -- (1.46,1.67) -- (1.52,1.79) -- (1.58,1.92) -- (1.64,2.05) -- (1.7,2.19) -- (1.76,2.34) -- (1.82,2.49) -- (1.88,2.65) -- (1.94,2.82) -- (2,3);
\fill[accent] (0.5,0.75) circle[pt];
\draw[faint] (-0.4,2.96) -- (-0.34,2.8) -- (-0.28,2.64) -- (-0.22,2.49) -- (-0.16,2.35) -- (-0.1,2.21) -- (-0.04,2.08) -- (0.02,1.96) -- (0.08,1.85) -- (0.14,1.74) -- (0.2,1.64) -- (0.26,1.55) -- (0.32,1.46) -- (0.38,1.38) -- (0.44,1.31) -- (0.5,1.25) -- (0.56,1.19) -- (0.62,1.14) -- (0.68,1.1) -- (0.74,1.07) -- (0.8,1.04) -- (0.86,1.02) -- (0.92,1.01) -- (0.98,1) -- (1.04,1) -- (1.1,1.01) -- (1.16,1.03) -- (1.22,1.05) -- (1.28,1.08) -- (1.34,1.12) -- (1.4,1.16) -- (1.46,1.21) -- (1.52,1.27) -- (1.58,1.34) -- (1.64,1.41) -- (1.7,1.49) -- (1.76,1.58) -- (1.82,1.67) -- (1.88,1.77) -- (1.94,1.88) -- (2,2) -- (2.06,2.12) -- (2.12,2.25) -- (2.18,2.39) -- (2.24,2.54) -- (2.3,2.69) -- (2.36,2.85);
\fill[accent] (1,1) circle[pt];
\draw[faint] (0.02,2.94) -- (0.08,2.77) -- (0.14,2.6) -- (0.2,2.44) -- (0.26,2.29) -- (0.32,2.14) -- (0.38,2) -- (0.44,1.87) -- (0.5,1.75) -- (0.56,1.63) -- (0.62,1.52) -- (0.68,1.42) -- (0.74,1.33) -- (0.8,1.24) -- (0.86,1.16) -- (0.92,1.09) -- (0.98,1.02) -- (1.04,0.96) -- (1.1,0.91) -- (1.16,0.87) -- (1.22,0.83) -- (1.28,0.8) -- (1.34,0.78) -- (1.4,0.76) -- (1.46,0.75) -- (1.52,0.75) -- (1.58,0.76) -- (1.64,0.77) -- (1.7,0.79) -- (1.76,0.82) -- (1.82,0.85) -- (1.88,0.89) -- (1.94,0.94) -- (2,1) -- (2.06,1.06) -- (2.12,1.13) -- (2.18,1.21) -- (2.24,1.3) -- (2.3,1.39) -- (2.36,1.49) -- (2.42,1.6) -- (2.48,1.71) -- (2.54,1.83) -- (2.6,1.96);
\fill[accent] (1.5,0.75) circle[pt];
\node[lab] at (2,2.4) {feasible};
\node[lab, left] at (-0.95,1.5) {$f_0$};
\end{tikzpicture}
\end{center}
```

Minimize $f_0(x)=x^2$ subject to $1-x\le0$ (feasible set shaded, $p^\star=1$). Thin curves: the Lagrangian $L(x,\lambda)=x^2+\lambda(1-x)$ for $\lambda=1,2,3$. Each one's minimum (dot) is $g(\lambda)$; none lies above $p^\star$.

:::

::: {#thm-dual-lower-bound .theorem name="Lower bound property"}

If $\lambda\succeq0$, then $g(\lambda,\nu)\le p^\star$.

:::

::: {.proof}

1. Let $\tilde x$ be feasible. Then $f_i(\tilde x)\le0$, $\lambda_i\ge0$ and $h_i(\tilde x)=0$, so $\sum_i\lambda_if_i(\tilde x)+\sum_i\nu_ih_i(\tilde x)\le0$.

2. Hence $g(\lambda,\nu)\le L(\tilde x,\lambda,\nu)\le f_0(\tilde x)$.

3. Taking the infimum over feasible $\tilde x$ gives $g(\lambda,\nu)\le p^\star$.

:::

::: {#fig-lagrange-dual-function-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.3,0) -- (4.6,0) node[lab, right] {$\lambda$};
\draw[->, faint] (0,-0.6) -- (0,1.6) node[lab, above] {};
\draw[hl] (0,0) -- (0.07,0.07) -- (0.15,0.14) -- (0.22,0.21) -- (0.29,0.27) -- (0.37,0.33) -- (0.44,0.39) -- (0.51,0.45) -- (0.59,0.5) -- (0.66,0.55) -- (0.73,0.6) -- (0.81,0.64) -- (0.88,0.69) -- (0.95,0.73) -- (1.03,0.76) -- (1.1,0.8) -- (1.17,0.83) -- (1.25,0.86) -- (1.32,0.88) -- (1.39,0.91) -- (1.47,0.93) -- (1.54,0.95) -- (1.61,0.96) -- (1.69,0.98) -- (1.76,0.99) -- (1.83,0.99) -- (1.91,1) -- (1.98,1) -- (2.05,1) -- (2.13,1) -- (2.2,0.99) -- (2.27,0.98) -- (2.35,0.97) -- (2.42,0.96) -- (2.49,0.94) -- (2.57,0.92) -- (2.64,0.9) -- (2.71,0.87) -- (2.79,0.85) -- (2.86,0.82) -- (2.93,0.78) -- (3.01,0.75) -- (3.08,0.71) -- (3.15,0.67) -- (3.23,0.62) -- (3.3,0.58) -- (3.37,0.53) -- (3.45,0.48) -- (3.52,0.42) -- (3.59,0.37) -- (3.67,0.31) -- (3.74,0.24) -- (3.81,0.18) -- (3.89,0.11) -- (3.96,0.04) -- (4.03,-0.03) -- (4.11,-0.11) -- (4.18,-0.19) -- (4.25,-0.27) -- (4.33,-0.35) -- (4.4,-0.44);
\draw[faint, dashed] (0,1) -- (4.4,1) node[lab, right] {$p^\star=1$};
\fill[accent] (2,1) circle[pt] node[lab, above] {$\lambda^\star=2$};
\node[lab] at (3.7,0.3) {$g(\lambda)$};
\end{tikzpicture}
\end{center}
```

The dual function of the same problem, $g(\lambda)=\lambda-\lambda^2/4$: concave, and below $p^\star$ for every $\lambda\ge0$. Here the best bound equals $p^\star$ at $\lambda=2$.

:::

::: {#exm-dual-least-norm .example name="Least-norm solution of linear equations"}

Minimize $x^{\mathsf T}x$ subject to $Ax=b$. The Lagrangian $x^{\mathsf T}x+\nu^{\mathsf T}(Ax-b)$ is minimized at $x=-\frac12A^{\mathsf T}\nu$, so
$$g(\nu)=-\tfrac14\nu^{\mathsf T}AA^{\mathsf T}\nu-b^{\mathsf T}\nu,$$
a concave quadratic, and $p^\star\ge-\frac14\nu^{\mathsf T}AA^{\mathsf T}\nu-b^{\mathsf T}\nu$ for every $\nu$.

:::

::: {#exm-dual-standard-lp .example name="Standard form LP"}

Minimize $c^{\mathsf T}x$ subject to $Ax=b$, $x\succeq0$. The Lagrangian $c^{\mathsf T}x+\nu^{\mathsf T}(Ax-b)-\lambda^{\mathsf T}x=-b^{\mathsf T}\nu+(c+A^{\mathsf T}\nu-\lambda)^{\mathsf T}x$ is affine in $x$, so it is bounded below only when its slope vanishes:
$$g(\lambda,\nu)=\begin{cases}-b^{\mathsf T}\nu&\text{if }A^{\mathsf T}\nu-\lambda+c=0,\\-\infty&\text{otherwise.}\end{cases}$$

:::

::: {#exm-two-way-partitioning-dual .example name="Two-way partitioning"}

Minimize $x^{\mathsf T}Wx$ subject to $x_i^2=1$, $i=1,\dots,n$, with $W\in\mathbb S^n$: split $\{1,\dots,n\}$ into two groups ($x_i=\pm1$), with $W_{ij}$ the cost of putting $i,j$ in the same group and $-W_{ij}$ in different ones. This problem is not convex and has $2^n$ feasible points. The Lagrangian $x^{\mathsf T}(W+\operatorname{diag}\nu)x-\mathbf 1^{\mathsf T}\nu$ gives
$$g(\nu)=\begin{cases}-\mathbf 1^{\mathsf T}\nu&\text{if }W+\operatorname{diag}\nu\succeq0,\\-\infty&\text{otherwise.}\end{cases}$$
With $\nu=-\lambda_{\min}(W)\mathbf 1$ this gives the bound $p^\star\ge n\,\lambda_{\min}(W)$.

:::

::: {#prp-dual-via-conjugate .proposition name="Dual function through the conjugate"}

For the problem minimize $f_0(x)$ subject to $Ax\preceq b$, $Cx=d$,
$$g(\lambda,\nu)=-b^{\mathsf T}\lambda-d^{\mathsf T}\nu-f_0^*(-A^{\mathsf T}\lambda-C^{\mathsf T}\nu),$$
with $f_0^*$ the conjugate (@def-conjugate-function).

:::

::: {.proof}

1. $g(\lambda,\nu)=\inf_x\big(f_0(x)+(A^{\mathsf T}\lambda+C^{\mathsf T}\nu)^{\mathsf T}x\big)-b^{\mathsf T}\lambda-d^{\mathsf T}\nu$.

2. $\inf_x(f_0(x)+y^{\mathsf T}x)=-\sup_x\big((-y)^{\mathsf T}x-f_0(x)\big)=-f_0^*(-y)$ with $y=A^{\mathsf T}\lambda+C^{\mathsf T}\nu$.

:::

::: {#exm-dual-norm-minimization .example name="Equality constrained norm minimization"}

Minimize $\lVert x\rVert$ subject to $Ax=b$. The conjugate of a norm is the indicator of the dual-norm unit ball (@exm-conjugates), so
$$g(\nu)=-b^{\mathsf T}\nu-f_0^*(-A^{\mathsf T}\nu)=\begin{cases}-b^{\mathsf T}\nu&\text{if }\lVert A^{\mathsf T}\nu\rVert_*\le1,\\-\infty&\text{otherwise.}\end{cases}$$

:::

::: {#rmk-lagrange-dual-function-1 .remark name="Linear penalties"}

The Lagrangian replaces the hard constraints $f_i(x)\le0$ by linear penalties $\lambda_if_i(x)$, which reward slack. A hard constraint is an infinitely steep penalty, which always lies above a linear one with $\lambda_i\ge0$; this is the lower bound property in words.

:::

::: {#fig-lagrange-dual-function-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-2.2,0) -- (1.6,0) node[lab, right] {$u$};
\draw[->, faint] (0,-1.6) -- (0,2.4) node[lab, above] {};
\draw[emph] (-2,0) -- (0,0) -- (0,2.2);
\node[lab, right] at (0.1,1.9) {$I_-(u)$};
\draw[hl] (-2,-0.8) -- (-0.3,-0.12) -- (1.4,0.56);
\draw[hl] (-2,-1.6) -- (-0.3,-0.24) -- (1.4,1.12);
\node[lab, right] at (1.4,0.56) {$\lambda u$};
\end{tikzpicture}
\end{center}
```

The Lagrangian replaces the hard penalty $I_-(u)$ ($0$ for $u\le0$, $+\infty$ for $u>0$) by the linear penalty $\lambda u$. For $\lambda\ge0$ each line lies below $I_-$, which is why $g(\lambda)\le p^\star$.

:::
