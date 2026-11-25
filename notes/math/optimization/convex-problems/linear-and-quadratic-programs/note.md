---
title: "Linear and Quadratic Programs"
sources: [ee364a-4]
requires: [math/optimization/convex-problems/optimization-problems]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on convex optimization problems, in our own wording; proofs written out in steps. Linear programs as an algorithmic topic are in @sec-cs-algorithm-topics-linear-programming; this note places them among convex problems. -->

Linear programs (@def-linear-program) have affine objective and constraints; quadratic programs allow a convex quadratic objective; QCQPs allow convex quadratic constraints too. Each class contains the previous one.

::: {#def-lp-general-form .definition name="Linear program in general form" related="def-linear-program"}

A *linear program* (LP) is
$$\begin{array}{ll}\text{minimize}&c^{\mathsf T}x+d\\ \text{subject to}&Gx\preceq h,\\ &Ax=b.\end{array}$$
Its feasible set is a polyhedron (@def-polyhedron). In *standard form* the only inequalities are $x\succeq0$; any LP can be put in standard form with slack variables and by writing $x=x^+-x^-$, $x^\pm\succeq0$.

:::

::: {#fig-linear-and-quadratic-programs-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0,0) -- (2.4,-0.3) -- (3.2,1) -- (2.3,2.3) -- (0.3,1.9) -- cycle;
\draw[emph] (0,0) -- (2.4,-0.3) -- (3.2,1) -- (2.3,2.3) -- (0.3,1.9) -- cycle;
\draw[faint] (-0.6,1.3) -- (1.5,0.25) -- (3.6,-0.8);
\draw[faint] (-0.6,2.3) -- (1.5,1.25) -- (3.6,0.2);
\draw[faint] (-0.6,3.1) -- (1.5,2.05) -- (3.6,1);
\draw[emph, dashed] (-0.6,3.75) -- (1.5,2.7) -- (3.6,1.65);
\fill[accent] (2.3,2.3) circle[pt] node[lab, above right] {$x^\star$};
\draw[->, hl] (1.4,0.8) -- (1.85,1.7) node[lab, right] {$-c$};
\node[lab] at (1.1,0.5) {$\mathcal P$};
\end{tikzpicture}
\end{center}
```

An LP in the plane: the level lines of $c^{\mathsf T}x$ are parallel, and pushing them in the direction $-c$ until they leave the polyhedron $\mathcal P$ stops at a vertex $x^\star$.

:::

::: {#exm-chebyshev-center .example name="Chebyshev centre of a polyhedron"}

The largest ball $\{x_c+u\mid\lVert u\rVert_2\le r\}$ inside $\mathcal P=\{x\mid a_i^{\mathsf T}x\le b_i\}$ solves an LP. The ball lies in the halfspace $a_i^{\mathsf T}x\le b_i$ iff $\sup_{\lVert u\rVert_2\le r}a_i^{\mathsf T}(x_c+u)=a_i^{\mathsf T}x_c+r\lVert a_i\rVert_2\le b_i$. So maximize $r$ subject to $a_i^{\mathsf T}x_c+r\lVert a_i\rVert_2\le b_i$, linear in $(x_c,r)$. For the triangle $x_1\ge0$, $x_2\ge0$, $x_1+x_2\le1$ the answer is $r=1/(2+\sqrt2)\approx0.293$ at $x_c=(r,r)$.

:::

::: {#fig-linear-and-quadratic-programs-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0,0) -- (2.4,-0.3) -- (3.2,1) -- (2.3,2.3) -- (0.3,1.9) -- cycle;
\draw[emph] (0,0) -- (2.4,-0.3) -- (3.2,1) -- (2.3,2.3) -- (0.3,1.9) -- cycle;
\draw[hl] (1.77,0.98) circle (1.19);
\fill[ink] (1.77,0.98) circle[pt] node[lab, below] {$x_c$};
\draw[->] (1.77,0.98) -- (2.72,1.69) node[lab, above] {$r$};
\end{tikzpicture}
\end{center}
```

The Chebyshev centre $x_c$ of a polygon, computed by the LP: the centre of the largest disc inside it. The disc touches three of the five sides.

:::

::: {#def-linear-fractional-program .definition name="Linear-fractional program"}

Minimize $f_0(x)=\dfrac{c^{\mathsf T}x+d}{e^{\mathsf T}x+f}$ on $e^{\mathsf T}x+f>0$ subject to $Gx\preceq h$, $Ax=b$. It is quasiconvex, and when the feasible set is nonempty it is equivalent to the LP
$$\text{minimize }c^{\mathsf T}y+dz\quad\text{s.t. }Gy\preceq hz,\ Ay=bz,\ e^{\mathsf T}y+fz=1,\ z\ge0,$$
through $y=x/(e^{\mathsf T}x+f)$, $z=1/(e^{\mathsf T}x+f)$.

:::

::: {#def-qp-qcqp .definition name="Quadratic program, QCQP"}

A *quadratic program* (QP) is
$$\begin{array}{ll}\text{minimize}&\tfrac12x^{\mathsf T}Px+q^{\mathsf T}x+r\\ \text{subject to}&Gx\preceq h,\quad Ax=b,\end{array}$$
with $P\in\mathbb S^n_+$. A *quadratically constrained quadratic program* (QCQP) also has constraints $\tfrac12x^{\mathsf T}P_ix+q_i^{\mathsf T}x+r_i\le0$ with $P_i\in\mathbb S^n_+$; its feasible set is an intersection of ellipsoids (when $P_i\succ0$) and an affine set.

:::

::: {#fig-linear-and-quadratic-programs-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0,0) -- (2.4,-0.3) -- (3.2,1) -- (2.3,2.3) -- (0.3,1.9) -- cycle;
\draw[emph] (0,0) -- (2.4,-0.3) -- (3.2,1) -- (2.3,2.3) -- (0.3,1.9) -- cycle;
\begin{scope}\clip (-0.5,-0.6) rectangle (4.6,3.8); \draw[emph] (5.01,0.36) -- (5.11,0.43) -- (5.2,0.51) -- (5.28,0.62) -- (5.34,0.74) -- (5.39,0.88) -- (5.43,1.03) -- (5.45,1.2) -- (5.46,1.38) -- (5.45,1.58) -- (5.44,1.78) -- (5.4,1.99) -- (5.36,2.21) -- (5.3,2.44) -- (5.22,2.66) -- (5.14,2.89) -- (5.04,3.12) -- (4.93,3.35) -- (4.81,3.57) -- (4.69,3.79) -- (4.55,4) -- (4.41,4.21) -- (4.26,4.4) -- (4.1,4.58) -- (3.95,4.75) -- (3.79,4.91) -- (3.62,5.05) -- (3.46,5.17) -- (3.3,5.28) -- (3.14,5.37) -- (2.99,5.44) -- (2.84,5.49) -- (2.69,5.52) -- (2.55,5.53) -- (2.42,5.52) -- (2.3,5.49) -- (2.19,5.44) -- (2.09,5.37) -- (2,5.29) -- (1.92,5.18) -- (1.86,5.06) -- (1.81,4.92) -- (1.77,4.77) -- (1.75,4.6) -- (1.74,4.42) -- (1.75,4.22) -- (1.76,4.02) -- (1.8,3.81) -- (1.84,3.59) -- (1.9,3.36) -- (1.98,3.14) -- (2.06,2.91) -- (2.16,2.68) -- (2.27,2.45) -- (2.39,2.23) -- (2.51,2.01) -- (2.65,1.8) -- (2.79,1.59) -- (2.94,1.4) -- (3.1,1.22) -- (3.25,1.05) -- (3.41,0.89) -- (3.58,0.75) -- (3.74,0.63) -- (3.9,0.52) -- (4.06,0.43) -- (4.21,0.36) -- (4.36,0.31) -- (4.51,0.28) -- (4.65,0.27) -- (4.78,0.28) -- (4.9,0.31) -- (5.01,0.36) -- cycle; \end{scope}
\begin{scope}\clip (-0.5,-0.6) rectangle (4.6,3.8); \draw[faint] (5.59,-0.7) -- (5.73,-0.6) -- (5.86,-0.48) -- (5.97,-0.33) -- (6.06,-0.15) -- (6.13,0.04) -- (6.18,0.26) -- (6.22,0.5) -- (6.23,0.76) -- (6.22,1.03) -- (6.2,1.32) -- (6.15,1.62) -- (6.08,1.93) -- (6,2.24) -- (5.89,2.56) -- (5.77,2.89) -- (5.64,3.21) -- (5.48,3.53) -- (5.32,3.85) -- (5.14,4.16) -- (4.94,4.46) -- (4.74,4.75) -- (4.53,5.02) -- (4.31,5.28) -- (4.09,5.52) -- (3.86,5.74) -- (3.63,5.94) -- (3.4,6.12) -- (3.18,6.27) -- (2.95,6.39) -- (2.73,6.49) -- (2.52,6.56) -- (2.31,6.6) -- (2.12,6.62) -- (1.94,6.61) -- (1.76,6.56) -- (1.61,6.5) -- (1.47,6.4) -- (1.34,6.28) -- (1.23,6.13) -- (1.14,5.95) -- (1.07,5.76) -- (1.02,5.54) -- (0.98,5.3) -- (0.97,5.04) -- (0.98,4.77) -- (1,4.48) -- (1.05,4.18) -- (1.12,3.87) -- (1.2,3.56) -- (1.31,3.24) -- (1.43,2.91) -- (1.56,2.59) -- (1.72,2.27) -- (1.88,1.95) -- (2.06,1.64) -- (2.26,1.34) -- (2.46,1.05) -- (2.67,0.78) -- (2.89,0.52) -- (3.11,0.28) -- (3.34,0.06) -- (3.57,-0.14) -- (3.8,-0.32) -- (4.02,-0.47) -- (4.25,-0.59) -- (4.47,-0.69) -- (4.68,-0.76) -- (4.89,-0.8) -- (5.08,-0.82) -- (5.26,-0.81) -- (5.44,-0.76) -- (5.59,-0.7) -- cycle; \end{scope}
\begin{scope}\clip (-0.5,-0.6) rectangle (4.6,3.8); \draw[faint] (6.12,-1.65) -- (6.3,-1.53) -- (6.46,-1.37) -- (6.6,-1.18) -- (6.71,-0.96) -- (6.8,-0.71) -- (6.87,-0.44) -- (6.91,-0.14) -- (6.93,0.19) -- (6.92,0.53) -- (6.88,0.9) -- (6.82,1.28) -- (6.74,1.67) -- (6.63,2.07) -- (6.5,2.48) -- (6.35,2.88) -- (6.18,3.3) -- (5.98,3.7) -- (5.77,4.1) -- (5.54,4.49) -- (5.3,4.87) -- (5.04,5.24) -- (4.78,5.59) -- (4.5,5.91) -- (4.22,6.22) -- (3.93,6.49) -- (3.64,6.75) -- (3.35,6.97) -- (3.06,7.16) -- (2.78,7.32) -- (2.5,7.44) -- (2.23,7.53) -- (1.97,7.59) -- (1.73,7.6) -- (1.49,7.59) -- (1.28,7.54) -- (1.08,7.45) -- (0.9,7.33) -- (0.74,7.17) -- (0.6,6.98) -- (0.49,6.76) -- (0.4,6.51) -- (0.33,6.24) -- (0.29,5.94) -- (0.27,5.61) -- (0.28,5.27) -- (0.32,4.9) -- (0.38,4.52) -- (0.46,4.13) -- (0.57,3.73) -- (0.7,3.32) -- (0.85,2.92) -- (1.02,2.5) -- (1.22,2.1) -- (1.43,1.7) -- (1.66,1.31) -- (1.9,0.93) -- (2.16,0.56) -- (2.42,0.21) -- (2.7,-0.11) -- (2.98,-0.42) -- (3.27,-0.69) -- (3.56,-0.95) -- (3.85,-1.17) -- (4.14,-1.36) -- (4.42,-1.52) -- (4.7,-1.64) -- (4.97,-1.73) -- (5.23,-1.79) -- (5.47,-1.8) -- (5.71,-1.79) -- (5.92,-1.74) -- (6.12,-1.65) -- cycle; \end{scope}
\fill[ink] (3.6,2.9) circle[pt];
\node[lab] at (3.7,3.15) {unconstrained min};
\fill[accent] (2.7,1.72) circle[pt] node[lab, below left] {$x^\star$};
\end{tikzpicture}
\end{center}
```

A QP: the level curves of a convex quadratic are ellipses. Its unconstrained minimizer lies outside the polyhedron, so the optimum $x^\star$ is where the smallest level ellipse touching $\mathcal P$ meets it, here on an edge rather than at a vertex.

:::

::: {#exm-qp-examples .example name="Least squares and portfolio choice"}

1. Least squares $\lVert Ax-b\rVert_2^2$ (@def-least-squares-solution) is an unconstrained QP; adding bounds $l\preceq x\preceq u$ keeps it a QP.

2. *Markowitz portfolio*: with mean return $\bar p$ and covariance $\Sigma$ of asset returns, minimize the variance $x^{\mathsf T}\Sigma x$ of a portfolio $x$ subject to $\bar p^{\mathsf T}x\ge r_{\min}$, $\mathbf 1^{\mathsf T}x=1$, $x\succeq0$.

:::

::: {#rmk-linear-and-quadratic-programs-1 .remark name="The hierarchy"}

LP $\subset$ QP $\subset$ QCQP $\subset$ SOCP (@sec-math-optimization-convex-problems-second-order-cone-programs) $\subset$ SDP (@sec-math-optimization-convex-problems-semidefinite-programs). Each inclusion is by rewriting, not by identity of form.

:::
