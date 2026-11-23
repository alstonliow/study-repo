---
title: "Geometric Programs"
sources: [ee364a-4]
requires: [math/optimization/convex-problems/equivalent-problems]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on convex optimization problems, in our own wording; proofs written out in steps. Numbers checked in Python. -->

Geometric programs look nonconvex, being built from monomials and posynomials of positive variables, but a logarithmic change of variables turns them into convex problems with log-sum-exp constraints.

::: {#def-monomial-posynomial .definition name="Monomial, posynomial"}

For $x\in\mathbb{R}^n_{++}$, a *monomial* is $f(x)=c\,x_1^{a_1}x_2^{a_2}\cdots x_n^{a_n}$ with $c>0$ and real exponents $a_i$. A *posynomial* is a sum of monomials, $f(x)=\sum_{k=1}^Kc_kx_1^{a_{1k}}\cdots x_n^{a_{nk}}$.

:::

::: {#def-geometric-program .definition name="Geometric program"}

A *geometric program* (GP) is
$$\begin{array}{ll}\text{minimize}&f_0(x)\\ \text{subject to}&f_i(x)\le1,\quad i=1,\dots,m,\\ &h_i(x)=1,\quad i=1,\dots,p,\end{array}$$
with $f_0,\dots,f_m$ posynomials, $h_1,\dots,h_p$ monomials, and implicit constraint $x\succ0$.

:::

::: {#fig-geometric-programs-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (2.6,0) node[lab, right] {$x_1$};
\draw[->, faint] (0,-0.2) -- (0,2.6) node[lab, above] {$x_2$};
\fill[tintA] (0,0) -- (0,2.25) -- (0.03,1.77) -- (0.06,1.59) -- (0.09,1.46) -- (0.11,1.35) -- (0.14,1.26) -- (0.17,1.18) -- (0.2,1.11) -- (0.23,1.05) -- (0.26,0.99) -- (0.28,0.93) -- (0.31,0.88) -- (0.34,0.84) -- (0.37,0.79) -- (0.4,0.75) -- (0.43,0.72) -- (0.46,0.68) -- (0.48,0.65) -- (0.51,0.61) -- (0.54,0.58) -- (0.57,0.56) -- (0.6,0.53) -- (0.63,0.5) -- (0.66,0.48) -- (0.68,0.45) -- (0.71,0.43) -- (0.74,0.41) -- (0.77,0.39) -- (0.8,0.37) -- (0.83,0.35) -- (0.85,0.33) -- (0.88,0.31) -- (0.91,0.3) -- (0.94,0.28) -- (0.97,0.27) -- (1,0.25) -- (1.03,0.24) -- (1.05,0.22) -- (1.08,0.21) -- (1.11,0.2) -- (1.14,0.19) -- (1.17,0.18) -- (1.2,0.17) -- (1.22,0.15) -- (1.25,0.14) -- (1.28,0.14) -- (1.31,0.13) -- (1.34,0.12) -- (1.37,0.11) -- (1.4,0.1) -- (1.42,0.09) -- (1.45,0.09) -- (1.48,0.08) -- (1.51,0.07) -- (1.54,0.07) -- (1.57,0.06) -- (1.59,0.06) -- (1.62,0.05) -- (1.65,0.05) -- (1.68,0.04) -- (1.71,0.04) -- (1.74,0.03) -- (1.77,0.03) -- (1.79,0.03) -- (1.82,0.02) -- (1.85,0.02) -- (1.88,0.02) -- (1.91,0.01) -- (1.94,0.01) -- (1.97,0.01) -- (1.99,0.01) -- (2.02,0.01) -- (2.05,0) -- (2.08,0) -- (2.11,0) -- (2.14,0) -- (2.16,0) -- (2.19,0) -- (2.22,0) -- (2.25,0) -- cycle;
\draw[hl] (0,2.25) -- (0.03,1.77) -- (0.06,1.59) -- (0.09,1.46) -- (0.11,1.35) -- (0.14,1.26) -- (0.17,1.18) -- (0.2,1.11) -- (0.23,1.05) -- (0.26,0.99) -- (0.28,0.93) -- (0.31,0.88) -- (0.34,0.84) -- (0.37,0.79) -- (0.4,0.75) -- (0.43,0.72) -- (0.46,0.68) -- (0.48,0.65) -- (0.51,0.61) -- (0.54,0.58) -- (0.57,0.56) -- (0.6,0.53) -- (0.63,0.5) -- (0.66,0.48) -- (0.68,0.45) -- (0.71,0.43) -- (0.74,0.41) -- (0.77,0.39) -- (0.8,0.37) -- (0.83,0.35) -- (0.85,0.33) -- (0.88,0.31) -- (0.91,0.3) -- (0.94,0.28) -- (0.97,0.27) -- (1,0.25) -- (1.03,0.24) -- (1.05,0.22) -- (1.08,0.21) -- (1.11,0.2) -- (1.14,0.19) -- (1.17,0.18) -- (1.2,0.17) -- (1.22,0.15) -- (1.25,0.14) -- (1.28,0.14) -- (1.31,0.13) -- (1.34,0.12) -- (1.37,0.11) -- (1.4,0.1) -- (1.42,0.09) -- (1.45,0.09) -- (1.48,0.08) -- (1.51,0.07) -- (1.54,0.07) -- (1.57,0.06) -- (1.59,0.06) -- (1.62,0.05) -- (1.65,0.05) -- (1.68,0.04) -- (1.71,0.04) -- (1.74,0.03) -- (1.77,0.03) -- (1.79,0.03) -- (1.82,0.02) -- (1.85,0.02) -- (1.88,0.02) -- (1.91,0.01) -- (1.94,0.01) -- (1.97,0.01) -- (1.99,0.01) -- (2.02,0.01) -- (2.05,0) -- (2.08,0) -- (2.11,0) -- (2.14,0) -- (2.16,0) -- (2.19,0) -- (2.22,0) -- (2.25,0);
\node[lab] at (0.5,0.45) {feasible};
\end{tikzpicture}
\hspace{1.2em}
\begin{tikzpicture}
\draw[->, faint] (-3.2,0) -- (1.4,0) node[lab, right] {$u_1$};
\draw[->, faint] (0,-3.2) -- (0,1.4) node[lab, above] {$u_2$};
\fill[tintA] (-3,0.49) -- (-2.95,0.48) -- (-2.9,0.47) -- (-2.86,0.46) -- (-2.81,0.45) -- (-2.76,0.44) -- (-2.71,0.43) -- (-2.66,0.42) -- (-2.62,0.41) -- (-2.57,0.4) -- (-2.52,0.39) -- (-2.47,0.38) -- (-2.42,0.37) -- (-2.38,0.36) -- (-2.33,0.34) -- (-2.28,0.33) -- (-2.23,0.32) -- (-2.18,0.3) -- (-2.14,0.29) -- (-2.09,0.28) -- (-2.04,0.26) -- (-1.99,0.25) -- (-1.94,0.23) -- (-1.9,0.21) -- (-1.85,0.2) -- (-1.8,0.18) -- (-1.75,0.16) -- (-1.7,0.14) -- (-1.66,0.12) -- (-1.61,0.1) -- (-1.56,0.08) -- (-1.51,0.06) -- (-1.46,0.04) -- (-1.42,0.01) -- (-1.37,-0.01) -- (-1.32,-0.03) -- (-1.27,-0.06) -- (-1.22,-0.09) -- (-1.18,-0.11) -- (-1.13,-0.14) -- (-1.08,-0.17) -- (-1.03,-0.2) -- (-0.98,-0.24) -- (-0.94,-0.27) -- (-0.89,-0.3) -- (-0.84,-0.34) -- (-0.79,-0.38) -- (-0.74,-0.42) -- (-0.7,-0.46) -- (-0.65,-0.5) -- (-0.6,-0.55) -- (-0.55,-0.6) -- (-0.5,-0.65) -- (-0.46,-0.7) -- (-0.41,-0.76) -- (-0.36,-0.82) -- (-0.31,-0.88) -- (-0.26,-0.94) -- (-0.22,-1.01) -- (-0.17,-1.09) -- (-0.12,-1.16) -- (-0.07,-1.25) -- (-0.02,-1.34) -- (0.02,-1.43) -- (0.07,-1.54) -- (0.12,-1.65) -- (0.17,-1.77) -- (0.22,-1.9) -- (0.26,-2.05) -- (0.31,-2.21) -- (0.36,-2.39) -- (0.41,-2.59) -- (0.46,-2.82) -- (0.46,-3) -- (-3,-3) -- cycle;
\draw[hl] (-3,0.49) -- (-2.95,0.48) -- (-2.9,0.47) -- (-2.86,0.46) -- (-2.81,0.45) -- (-2.76,0.44) -- (-2.71,0.43) -- (-2.66,0.42) -- (-2.62,0.41) -- (-2.57,0.4) -- (-2.52,0.39) -- (-2.47,0.38) -- (-2.42,0.37) -- (-2.38,0.36) -- (-2.33,0.34) -- (-2.28,0.33) -- (-2.23,0.32) -- (-2.18,0.3) -- (-2.14,0.29) -- (-2.09,0.28) -- (-2.04,0.26) -- (-1.99,0.25) -- (-1.94,0.23) -- (-1.9,0.21) -- (-1.85,0.2) -- (-1.8,0.18) -- (-1.75,0.16) -- (-1.7,0.14) -- (-1.66,0.12) -- (-1.61,0.1) -- (-1.56,0.08) -- (-1.51,0.06) -- (-1.46,0.04) -- (-1.42,0.01) -- (-1.37,-0.01) -- (-1.32,-0.03) -- (-1.27,-0.06) -- (-1.22,-0.09) -- (-1.18,-0.11) -- (-1.13,-0.14) -- (-1.08,-0.17) -- (-1.03,-0.2) -- (-0.98,-0.24) -- (-0.94,-0.27) -- (-0.89,-0.3) -- (-0.84,-0.34) -- (-0.79,-0.38) -- (-0.74,-0.42) -- (-0.7,-0.46) -- (-0.65,-0.5) -- (-0.6,-0.55) -- (-0.55,-0.6) -- (-0.5,-0.65) -- (-0.46,-0.7) -- (-0.41,-0.76) -- (-0.36,-0.82) -- (-0.31,-0.88) -- (-0.26,-0.94) -- (-0.22,-1.01) -- (-0.17,-1.09) -- (-0.12,-1.16) -- (-0.07,-1.25) -- (-0.02,-1.34) -- (0.02,-1.43) -- (0.07,-1.54) -- (0.12,-1.65) -- (0.17,-1.77) -- (0.22,-1.9) -- (0.26,-2.05) -- (0.31,-2.21) -- (0.36,-2.39) -- (0.41,-2.59) -- (0.46,-2.82);
\node[lab] at (-1.8,-1.8) {feasible};
\end{tikzpicture}
\end{center}
```

The posynomial constraint $x_1^{1/2}+x_2^{1/2}\le1.5$. Left, in $x$: the feasible set is not convex (its boundary bows inward). Right, in $u=\log x$: the set $e^{u_1/2}+e^{u_2/2}\le1.5$ is convex.

:::

::: {#thm-gp-convex-form .theorem name="Geometric programs in convex form"}

With $y_i=\log x_i$, the GP of @def-geometric-program is equivalent to the convex problem
$$\begin{array}{ll}\text{minimize}&\log\sum_ke^{a_{0k}^{\mathsf T}y+b_{0k}}\\ \text{subject to}&\log\sum_ke^{a_{ik}^{\mathsf T}y+b_{ik}}\le0,\quad i=1,\dots,m,\\ &Gy+d=0,\end{array}$$
where $b_{ik}=\log c_{ik}$ and each monomial $h_i$ becomes the affine equation $g_i^{\mathsf T}y+d_i=0$.

:::

::: {.proof}

1. A monomial becomes $c\,e^{a^{\mathsf T}y}=e^{a^{\mathsf T}y+\log c}$, so $\log$ of a monomial is affine in $y$ and $h_i(x)=1$ iff that affine function is $0$.

2. A posynomial becomes $\sum_ke^{a_k^{\mathsf T}y+b_k}$; since $\log$ is increasing and $\log1=0$, $f_i(x)\le1$ iff $\log\sum_ke^{a_k^{\mathsf T}y+b_k}\le0$, and minimizing $f_0$ is the same as minimizing $\log f_0$.

3. Log-sum-exp is convex (@exm-convex-by-hessian) and composing it with an affine map keeps it convex (@prp-nonnegative-sum-affine-composition). The map $x\mapsto y$ is a bijection from $\mathbb{R}^n_{++}$ to $\mathbb{R}^n$.

:::

::: {#fig-geometric-programs-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-2.4,0) -- (2.4,0) node[lab, right] {$y=\log x$};
\draw[->, faint] (0,-1.4) -- (0,2.6) node[lab, above] {$\log f$};
\draw[emph] (-2.2,-0.41) -- (-2.13,-0.37) -- (-2.05,-0.33) -- (-1.98,-0.3) -- (-1.91,-0.26) -- (-1.83,-0.22) -- (-1.76,-0.19) -- (-1.69,-0.15) -- (-1.61,-0.11) -- (-1.54,-0.08) -- (-1.47,-0.04) -- (-1.39,-0) -- (-1.32,0.03) -- (-1.25,0.07) -- (-1.17,0.11) -- (-1.1,0.14) -- (-1.03,0.18) -- (-0.95,0.22) -- (-0.88,0.25) -- (-0.81,0.29) -- (-0.73,0.33) -- (-0.66,0.36) -- (-0.59,0.4) -- (-0.51,0.44) -- (-0.44,0.47) -- (-0.37,0.51) -- (-0.29,0.55) -- (-0.22,0.58) -- (-0.15,0.62) -- (-0.07,0.66) -- (0,0.69) -- (0.07,0.73) -- (0.15,0.77) -- (0.22,0.8) -- (0.29,0.84) -- (0.37,0.88) -- (0.44,0.91) -- (0.51,0.95) -- (0.59,0.99) -- (0.66,1.02) -- (0.73,1.06) -- (0.81,1.1) -- (0.88,1.13) -- (0.95,1.17) -- (1.03,1.21) -- (1.1,1.24) -- (1.17,1.28) -- (1.25,1.32) -- (1.32,1.35) -- (1.39,1.39) -- (1.47,1.43) -- (1.54,1.46) -- (1.61,1.5) -- (1.69,1.54) -- (1.76,1.57) -- (1.83,1.61) -- (1.91,1.65) -- (1.98,1.68) -- (2.05,1.72) -- (2.13,1.76) -- (2.2,1.79);
\draw[hl] (-2.2,2.24) -- (-2.13,2.17) -- (-2.05,2.1) -- (-1.98,2.03) -- (-1.91,1.96) -- (-1.83,1.9) -- (-1.76,1.83) -- (-1.69,1.76) -- (-1.61,1.7) -- (-1.54,1.63) -- (-1.47,1.57) -- (-1.39,1.51) -- (-1.32,1.45) -- (-1.25,1.39) -- (-1.17,1.33) -- (-1.1,1.28) -- (-1.03,1.22) -- (-0.95,1.17) -- (-0.88,1.12) -- (-0.81,1.07) -- (-0.73,1.02) -- (-0.66,0.98) -- (-0.59,0.93) -- (-0.51,0.89) -- (-0.44,0.86) -- (-0.37,0.82) -- (-0.29,0.79) -- (-0.22,0.76) -- (-0.15,0.74) -- (-0.07,0.71) -- (0,0.69) -- (0.07,0.68) -- (0.15,0.66) -- (0.22,0.65) -- (0.29,0.64) -- (0.37,0.64) -- (0.44,0.64) -- (0.51,0.64) -- (0.59,0.64) -- (0.66,0.65) -- (0.73,0.65) -- (0.81,0.66) -- (0.88,0.68) -- (0.95,0.69) -- (1.03,0.71) -- (1.1,0.73) -- (1.17,0.75) -- (1.25,0.77) -- (1.32,0.79) -- (1.39,0.81) -- (1.47,0.84) -- (1.54,0.86) -- (1.61,0.89) -- (1.69,0.92) -- (1.76,0.95) -- (1.83,0.98) -- (1.91,1.01) -- (1.98,1.04) -- (2.05,1.07) -- (2.13,1.1) -- (2.2,1.14);
\node[lab, right] at (2.3,1.79) {$2x^{0.5}$};
\node[lab, right] at (-2.2,2.3) {$x^{-1}+x^{0.5}$};
\end{tikzpicture}
\end{center}
```

In log–log coordinates a monomial becomes affine (the line $\log2+0.5y$) and a posynomial becomes convex ($\log(e^{-y}+e^{0.5y})$, a log-sum-exp). This change of variables is what turns a geometric program into a convex problem.

:::

::: {#exm-box-design-gp .example name="Designing a box"}

Maximize the volume $hwd$ of a box with wall area $2(hw+hd)\le A_{\rm wall}$ and floor area $wd\le A_{\rm flr}$. As a GP: minimize $h^{-1}w^{-1}d^{-1}$ subject to $\frac{2}{A_{\rm wall}}hw+\frac{2}{A_{\rm wall}}hd\le1$ and $\frac{1}{A_{\rm flr}}wd\le1$. For $A_{\rm wall}=100$ and $A_{\rm flr}=10$ the optimum can be found by hand: the wall constraint gives $h\le50/(w+d)$, so the volume is at most $50\,wd/(w+d)\le50\sqrt{wd}/2\le25\sqrt{10}\approx79.06$ (using $w+d\ge2\sqrt{wd}$ and $wd\le10$), attained at $w=d=\sqrt{10}$, $h=25/\sqrt{10}\approx7.91$.

:::

::: {#exm-spectral-radius-gp .example name="Spectral radius of a positive matrix"}

For an elementwise positive matrix $A(x)$ whose entries are posynomials in $x$, the Perron–Frobenius eigenvalue satisfies $\lambda_{\rm pf}(A(x))\le\lambda$ iff $A(x)v\preceq\lambda v$ for some $v\succ0$, that is, $\sum_jA(x)_{ij}v_j/(\lambda v_i)\le1$ for all $i$, a set of posynomial constraints in $(x,v,\lambda)$. So minimizing the spectral radius is a GP.

:::

::: {#rmk-geometric-programs-1 .remark name="What is and is not a GP"}

Posynomials are closed under sums, products and multiplication by positive constants, and a posynomial divided by a monomial is a posynomial. A ratio of two posynomials is in general not a posynomial, and a constraint $f(x)\ge1$ with $f$ a posynomial is not allowed.

:::
