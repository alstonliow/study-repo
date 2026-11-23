---
title: "Extremal Ellipsoids and Centering"
sources: [ee364a-8]
requires: [math/optimization/convex-problems/semidefinite-programs, math/optimization/duality/kkt-conditions]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on geometric problems, in our own wording; proofs written out in steps. Numbers checked in Python. -->

Ellipsoids approximate convex sets: the smallest one containing a set and the largest one inside it both come from convex problems. Centers of a set, such as the analytic center of a system of inequalities, are found the same way.

::: {#def-lowner-john-ellipsoid .definition name="Minimum volume ellipsoid (Löwner–John)"}

The minimum volume ellipsoid containing a set $C$ is found by parametrizing $\mathcal E=\{v\mid\lVert Av+b\rVert_2\le1\}$ with $A\in\mathbb S^n_{++}$ (volume proportional to $\det A^{-1}$) and solving
$$\text{minimize }\log\det A^{-1}\quad\text{s.t. }\sup_{v\in C}\lVert Av+b\rVert_2\le1.$$
For a finite set $C=\{x_1,\dots,x_m\}$ the constraints are $\lVert Ax_i+b\rVert_2\le1$, a convex problem.

:::

::: {#fig-extremal-ellipsoids-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0.2,0.3) -- (2.6,0) -- (3,1.4) -- (1.8,2.2) -- (0.4,1.6) -- cycle;
\draw[faint] (0.2,0.3) -- (2.6,0) -- (3,1.4) -- (1.8,2.2) -- (0.4,1.6) -- cycle;
\draw[hl] (0.14,0.46) -- (0.18,0.36) -- (0.22,0.25) -- (0.28,0.15) -- (0.35,0.06) -- (0.43,-0.02) -- (0.51,-0.1) -- (0.61,-0.17) -- (0.71,-0.24) -- (0.82,-0.29) -- (0.94,-0.34) -- (1.05,-0.38) -- (1.18,-0.4) -- (1.3,-0.42) -- (1.43,-0.43) -- (1.56,-0.42) -- (1.69,-0.41) -- (1.82,-0.39) -- (1.95,-0.36) -- (2.07,-0.32) -- (2.2,-0.26) -- (2.31,-0.2) -- (2.42,-0.14) -- (2.53,-0.06) -- (2.62,0.02) -- (2.71,0.11) -- (2.79,0.21) -- (2.86,0.31) -- (2.93,0.41) -- (2.98,0.52) -- (3.02,0.63) -- (3.05,0.75) -- (3.07,0.86) -- (3.07,0.98) -- (3.07,1.09) -- (3.06,1.2) -- (3.03,1.31) -- (2.99,1.42) -- (2.94,1.52) -- (2.89,1.62) -- (2.82,1.71) -- (2.74,1.8) -- (2.65,1.88) -- (2.56,1.95) -- (2.46,2.01) -- (2.35,2.07) -- (2.23,2.11) -- (2.11,2.15) -- (1.99,2.18) -- (1.86,2.19) -- (1.73,2.2) -- (1.6,2.2) -- (1.47,2.19) -- (1.35,2.16) -- (1.22,2.13) -- (1.09,2.09) -- (0.97,2.04) -- (0.86,1.98) -- (0.75,1.91) -- (0.64,1.84) -- (0.54,1.75) -- (0.45,1.66) -- (0.37,1.57) -- (0.3,1.47) -- (0.24,1.36) -- (0.19,1.25) -- (0.15,1.14) -- (0.12,1.03) -- (0.1,0.91) -- (0.09,0.8) -- (0.1,0.68) -- (0.11,0.57) -- (0.14,0.46) -- cycle;
\fill[ink] (0.2,0.3) circle[pt];
\fill[ink] (2.6,0) circle[pt];
\fill[ink] (3,1.4) circle[pt];
\fill[ink] (1.8,2.2) circle[pt];
\fill[ink] (0.4,1.6) circle[pt];
\fill[ink] (1.2,0.9) circle[pt];
\fill[ink] (2,1) circle[pt];
\fill[ink] (1,1.8) circle[pt];
\end{tikzpicture}
\end{center}
```

The Löwner–John ellipsoid of eight points: the minimum-area ellipse containing them (equivalently, containing their convex hull, shaded). It touches only some of the hull's vertices.

:::

::: {#def-max-inscribed-ellipsoid .definition name="Maximum volume inscribed ellipsoid"}

The largest ellipsoid $\mathcal E=\{Bu+d\mid\lVert u\rVert_2\le1\}$, $B\in\mathbb S^n_{++}$, inside a convex set $C$ solves
$$\text{maximize }\log\det B\quad\text{s.t. }\sup_{\lVert u\rVert_2\le1}I_C(Bu+d)\le0.$$
For a polyhedron $\{x\mid a_i^{\mathsf T}x\le b_i\}$ the constraints are $\lVert Ba_i\rVert_2+a_i^{\mathsf T}d\le b_i$, a convex problem.

:::

::: {.proof}

1. $\mathcal E$ lies in the halfspace $a_i^{\mathsf T}x\le b_i$ iff $\sup_{\lVert u\rVert_2\le1}a_i^{\mathsf T}(Bu+d)\le b_i$.

2. The supremum is $\lVert Ba_i\rVert_2+a_i^{\mathsf T}d$ by Cauchy–Schwarz (using $B=B^{\mathsf T}$).

:::

::: {#fig-extremal-ellipsoids-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0,0) -- (2.4,-0.3) -- (3.2,1) -- (2.3,2.3) -- (0.3,1.9) -- cycle;
\draw[emph] (0,0) -- (2.4,-0.3) -- (3.2,1) -- (2.3,2.3) -- (0.3,1.9) -- cycle;
\draw[hl] (1.59,-0.19) -- (1.71,-0.18) -- (1.83,-0.17) -- (1.96,-0.15) -- (2.07,-0.12) -- (2.19,-0.08) -- (2.3,-0.03) -- (2.4,0.02) -- (2.5,0.08) -- (2.59,0.15) -- (2.68,0.23) -- (2.75,0.31) -- (2.82,0.39) -- (2.88,0.48) -- (2.93,0.57) -- (2.96,0.67) -- (2.99,0.77) -- (3.01,0.87) -- (3.01,0.97) -- (3.01,1.07) -- (2.99,1.17) -- (2.97,1.27) -- (2.93,1.36) -- (2.88,1.45) -- (2.82,1.54) -- (2.76,1.63) -- (2.68,1.71) -- (2.6,1.78) -- (2.51,1.85) -- (2.41,1.91) -- (2.3,1.97) -- (2.19,2.01) -- (2.08,2.05) -- (1.96,2.08) -- (1.84,2.11) -- (1.71,2.12) -- (1.59,2.12) -- (1.47,2.12) -- (1.34,2.11) -- (1.22,2.08) -- (1.1,2.05) -- (0.99,2.02) -- (0.88,1.97) -- (0.77,1.92) -- (0.67,1.85) -- (0.58,1.79) -- (0.5,1.71) -- (0.42,1.63) -- (0.36,1.55) -- (0.3,1.46) -- (0.25,1.37) -- (0.21,1.27) -- (0.19,1.17) -- (0.17,1.07) -- (0.16,0.97) -- (0.17,0.87) -- (0.19,0.77) -- (0.21,0.67) -- (0.25,0.58) -- (0.3,0.48) -- (0.35,0.39) -- (0.42,0.31) -- (0.5,0.23) -- (0.58,0.15) -- (0.67,0.09) -- (0.77,0.02) -- (0.88,-0.03) -- (0.99,-0.08) -- (1.1,-0.11) -- (1.22,-0.15) -- (1.34,-0.17) -- (1.46,-0.18) -- (1.59,-0.19) -- cycle;
\fill[ink] (1.59,0.97) circle[pt] node[lab, below] {$d$};
\end{tikzpicture}
\end{center}
```

The maximum-area ellipse $\{Bu+d\mid\lVert u\rVert_2\le1\}$ inside a pentagon, found from the constraints $\lVert Ba_i\rVert_2+a_i^{\mathsf T}d\le b_i$. Compare the largest disc, the Chebyshev centre: the ellipse can stretch along the long direction.

:::

::: {#thm-ellipsoid-efficiency .theorem name="Efficiency of ellipsoidal approximation"}

Let $C\subseteq\mathbb{R}^n$ be bounded and convex with nonempty interior.

1. The minimum volume ellipsoid containing $C$, shrunk by the factor $n$ about its centre, lies inside $C$.

2. The maximum volume ellipsoid inside $C$, expanded by the factor $n$ about its centre, contains $C$.

If $C$ is symmetric about a point, the factor $n$ improves to $\sqrt n$.

:::

::: {#rmk-extremal-ellipsoids-1 .remark name="About the efficiency theorem"}

We state @thm-ellipsoid-efficiency without proof. The factor $n$ is attained by a simplex.

:::

::: {#def-analytic-center .definition name="Analytic center"}

The *analytic center* of the inequalities $f_i(x)\le0$, $Fx=g$ (with $f_i$ convex and a strictly feasible point) is the solution of
$$\text{minimize }-\sum_{i=1}^m\log(-f_i(x))\quad\text{s.t. }Fx=g.$$
For linear inequalities $a_i^{\mathsf T}x\le b_i$ it maximizes $\prod_i(b_i-a_i^{\mathsf T}x)$, the product of the slacks.

:::

::: {#exm-analytic-center-interval .example name="Analytic center of an interval"}

For $0\le x\le1$ written as $-x\le0$, $x-1\le0$, the analytic center maximizes $x(1-x)$, at $x=\frac12$. Adding the redundant inequality $x\le2$ moves it: maximizing $x(1-x)(2-x)$ on $(0,1)$ gives $x=1-1/\sqrt3\approx0.423$. The analytic center depends on the description, not only on the set.

:::

::: {#prp-analytic-center-ellipsoids .proposition name="Inner and outer ellipsoids at the analytic center"}

Let $x_{\rm ac}$ be the analytic center of $a_i^{\mathsf T}x\le b_i$, $i=1,\dots,m$, and $H=\sum_i\frac{a_ia_i^{\mathsf T}}{(b_i-a_i^{\mathsf T}x_{\rm ac})^2}$ the Hessian of the log barrier there. Then
$$\{x\mid(x-x_{\rm ac})^{\mathsf T}H(x-x_{\rm ac})\le1\}\subseteq\mathcal P\subseteq\{x\mid(x-x_{\rm ac})^{\mathsf T}H(x-x_{\rm ac})\le m(m-1)\}.$$

:::

::: {.proof}

1. Inner: write $s_i=b_i-a_i^{\mathsf T}x_{\rm ac}>0$ and $d=x-x_{\rm ac}$. If $d^{\mathsf T}Hd=\sum_i(a_i^{\mathsf T}d)^2/s_i^2\le1$ then each $\lvert a_i^{\mathsf T}d\rvert\le s_i$, so $a_i^{\mathsf T}x\le b_i$.

2. Outer: optimality of $x_{\rm ac}$ gives $\sum_ia_i/s_i=0$. For $x\in\mathcal P$ put $t_i=a_i^{\mathsf T}d/s_i\le1$; then $\sum_it_i=0$.

3. Let $P=\sum_{t_i>0}t_i$. At most $m-1$ of the $t_i$ are positive (they sum to $0$ and are not all zero unless $d=0$), each at most $1$, so $P\le m-1$, and $\sum_{t_i>0}t_i^2\le P$. The negative entries sum to $-P$, so $\sum_{t_i<0}t_i^2\le P^2$.

4. Hence $d^{\mathsf T}Hd=\sum_it_i^2\le P+P^2\le(m-1)+(m-1)^2=m(m-1)$.

:::

::: {#fig-extremal-ellipsoids-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.6]
\begin{scope}\clip (-2.6,-2.6) rectangle (5.6,4.8);
\draw[faint] (-2.5,-0.03) -- (-2.42,-0.3) -- (-2.31,-0.57) -- (-2.17,-0.82) -- (-2.01,-1.06) -- (-1.82,-1.29) -- (-1.6,-1.5) -- (-1.37,-1.69) -- (-1.11,-1.87) -- (-0.83,-2.02) -- (-0.54,-2.15) -- (-0.23,-2.25) -- (0.09,-2.34) -- (0.42,-2.39) -- (0.75,-2.43) -- (1.09,-2.44) -- (1.44,-2.42) -- (1.78,-2.38) -- (2.12,-2.31) -- (2.46,-2.22) -- (2.78,-2.1) -- (3.1,-1.97) -- (3.4,-1.81) -- (3.69,-1.63) -- (3.95,-1.43) -- (4.2,-1.21) -- (4.43,-0.98) -- (4.64,-0.73) -- (4.82,-0.47) -- (4.97,-0.2) -- (5.1,0.07) -- (5.19,0.36) -- (5.26,0.64) -- (5.3,0.93) -- (5.31,1.22) -- (5.29,1.51) -- (5.24,1.79) -- (5.16,2.06) -- (5.05,2.33) -- (4.91,2.58) -- (4.75,2.83) -- (4.56,3.05) -- (4.35,3.26) -- (4.11,3.46) -- (3.85,3.63) -- (3.58,3.78) -- (3.28,3.91) -- (2.98,4.02) -- (2.66,4.1) -- (2.33,4.16) -- (1.99,4.19) -- (1.65,4.2) -- (1.3,4.18) -- (0.96,4.14) -- (0.62,4.07) -- (0.29,3.98) -- (-0.04,3.86) -- (-0.35,3.73) -- (-0.66,3.57) -- (-0.94,3.39) -- (-1.21,3.19) -- (-1.46,2.97) -- (-1.69,2.74) -- (-1.89,2.49) -- (-2.07,2.23) -- (-2.23,1.97) -- (-2.35,1.69) -- (-2.45,1.4) -- (-2.52,1.12) -- (-2.56,0.83) -- (-2.57,0.54) -- (-2.55,0.25) -- (-2.5,-0.03) -- cycle;
\end{scope}
\fill[tintA] (0,0) -- (2.4,-0.3) -- (3.2,1) -- (2.3,2.3) -- (0.3,1.9) -- cycle;
\draw[emph] (0,0) -- (2.4,-0.3) -- (3.2,1) -- (2.3,2.3) -- (0.3,1.9) -- cycle;
\draw[hl] (0.51,0.68) -- (0.52,0.62) -- (0.55,0.56) -- (0.58,0.5) -- (0.62,0.45) -- (0.66,0.39) -- (0.71,0.35) -- (0.76,0.3) -- (0.82,0.27) -- (0.88,0.23) -- (0.94,0.2) -- (1.01,0.18) -- (1.08,0.16) -- (1.16,0.15) -- (1.23,0.14) -- (1.31,0.14) -- (1.39,0.14) -- (1.46,0.15) -- (1.54,0.17) -- (1.61,0.19) -- (1.69,0.21) -- (1.76,0.24) -- (1.82,0.28) -- (1.89,0.32) -- (1.95,0.36) -- (2,0.41) -- (2.06,0.46) -- (2.1,0.52) -- (2.14,0.58) -- (2.18,0.64) -- (2.2,0.7) -- (2.23,0.76) -- (2.24,0.83) -- (2.25,0.89) -- (2.25,0.96) -- (2.25,1.02) -- (2.24,1.08) -- (2.22,1.15) -- (2.19,1.2) -- (2.16,1.26) -- (2.13,1.32) -- (2.08,1.37) -- (2.04,1.41) -- (1.98,1.46) -- (1.93,1.49) -- (1.86,1.53) -- (1.8,1.56) -- (1.73,1.58) -- (1.66,1.6) -- (1.58,1.61) -- (1.51,1.62) -- (1.43,1.62) -- (1.36,1.62) -- (1.28,1.61) -- (1.2,1.59) -- (1.13,1.57) -- (1.06,1.55) -- (0.99,1.52) -- (0.92,1.48) -- (0.85,1.44) -- (0.79,1.4) -- (0.74,1.35) -- (0.69,1.3) -- (0.64,1.24) -- (0.6,1.18) -- (0.57,1.12) -- (0.54,1.06) -- (0.52,1) -- (0.5,0.93) -- (0.49,0.87) -- (0.49,0.8) -- (0.49,0.74) -- (0.51,0.68) -- cycle;
\fill[ink] (1.37,0.88) circle[pt] node[lab, below] {$x_{\rm ac}$};
\end{tikzpicture}
\end{center}
```

At the analytic centre $x_{\rm ac}$ of a pentagon ($m=5$), the ellipse defined by the barrier Hessian $H$ (thick) lies inside, and the same ellipse scaled by $\sqrt{m(m-1)}=\sqrt{20}$ (thin, clipped) contains the pentagon. The inner one is the Dikin ellipsoid.

:::
