---
title: "Lagrange Multipliers"
sources: [mit1802-13]
requires: [math/calculus/multivariable/differentiation/gradient, math/calculus/multivariable/differentiation/critical-points]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lecture 13, in our own wording. Numbers checked in Python (sympy). -->

Problem: find the largest or smallest value of $f(x,y,z)$ when the variables are tied by a constraint $g(x,y,z)=c$.

::: {#thm-lagrange-multipliers .theorem name="Lagrange multipliers"}

Let $f$ and $g$ have continuous partial derivatives. If $f$, restricted to the level surface $g=c$, has a local maximum or minimum at $P$ and $\nabla g(P)\ne\mathbf{0}$, then there is a number $\lambda$ (the **multiplier**) with
$$\nabla f(P)=\lambda\,\nabla g(P),\qquad g(P)=c .$$
In two variables this is the system $f_x=\lambda g_x$, $f_y=\lambda g_y$, $g=c$: three equations for $x,y,\lambda$.

:::

::: {.proof}

1. Let $\hat{\mathbf{u}}$ be any unit vector tangent to the surface $g=c$ at $P$, and $\mathbf{r}(s)$ a curve in the surface through $P$ with velocity $\hat{\mathbf{u}}$ there.

2. Along the curve, $f(\mathbf{r}(s))$ has a local extremum at $P$, so its derivative is $0$: by the chain rule $\nabla f(P)\cdot\hat{\mathbf{u}}=0$.

3. So $\nabla f(P)$ is perpendicular to every tangent vector of the surface, i.e. normal to the tangent plane.

4. $\nabla g(P)$ is also normal to that plane (@thm-gradient-normal-to-level-surface) and is not $\mathbf{0}$, so the two vectors are parallel: $\nabla f(P)=\lambda\nabla g(P)$. (The existence of a curve with any given tangent direction, used in step 1, is part of the implicit function theorem and is assumed here.)

:::

::: {#fig-lagrange-multipliers-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-2.6,0) -- (2.8,0) node[lab, right] {$x$};
\draw[->, faint] (0,-1.6) -- (0,2) node[lab, above] {$y$};
\draw[emph] (2,0) -- (1.99,0.09) -- (1.97,0.17) -- (1.93,0.26) -- (1.88,0.34) -- (1.81,0.42) -- (1.73,0.5) -- (1.64,0.57) -- (1.53,0.64) -- (1.41,0.71) -- (1.29,0.77) -- (1.15,0.82) -- (1,0.87) -- (0.85,0.91) -- (0.68,0.94) -- (0.52,0.97) -- (0.35,0.98) -- (0.17,1) -- (0,1) -- (-0.17,1) -- (-0.35,0.98) -- (-0.52,0.97) -- (-0.68,0.94) -- (-0.85,0.91) -- (-1,0.87) -- (-1.15,0.82) -- (-1.29,0.77) -- (-1.41,0.71) -- (-1.53,0.64) -- (-1.64,0.57) -- (-1.73,0.5) -- (-1.81,0.42) -- (-1.88,0.34) -- (-1.93,0.26) -- (-1.97,0.17) -- (-1.99,0.09) -- (-2,0) -- (-1.99,-0.09) -- (-1.97,-0.17) -- (-1.93,-0.26) -- (-1.88,-0.34) -- (-1.81,-0.42) -- (-1.73,-0.5) -- (-1.64,-0.57) -- (-1.53,-0.64) -- (-1.41,-0.71) -- (-1.29,-0.77) -- (-1.15,-0.82) -- (-1,-0.87) -- (-0.85,-0.91) -- (-0.68,-0.94) -- (-0.52,-0.97) -- (-0.35,-0.98) -- (-0.17,-1) -- (0,-1) -- (0.17,-1) -- (0.35,-0.98) -- (0.52,-0.97) -- (0.68,-0.94) -- (0.85,-0.91) -- (1,-0.87) -- (1.15,-0.82) -- (1.29,-0.77) -- (1.41,-0.71) -- (1.53,-0.64) -- (1.64,-0.57) -- (1.73,-0.5) -- (1.81,-0.42) -- (1.88,-0.34) -- (1.93,-0.26) -- (1.97,-0.17) -- (1.99,-0.09) -- (2,0) -- cycle;
\draw[faint] ;
\draw[faint] (0.8,0.7) -- (2.8,-1.3);
\draw[faint] (0.8,1.2) -- (2.8,-0.8);
\draw[faint] (0.8,1.7) -- (2.8,-0.3);
\draw[hl] (0.6,1.64) -- (1.65,0.59) -- (2.7,-0.46);
\fill[accent] (1.79,0.45) circle[pt];
\draw[->] (1.79,0.45) -- (2.29,0.95) node[lab, above] {$\nabla f$};
\draw[->] (1.79,0.45) -- (2.29,0.95) node[lab, below right] {$\nabla g$};
\node[lab] at (-1.6,-1.2) {$g=1$};
\end{tikzpicture}
\end{center}
```

Maximizing $f=x+y$ on the ellipse $g=\tfrac14x^2+y^2=1$: the level lines of $f$ move up until the last one touching the ellipse (thick). There the two curves are tangent, so $\nabla f$ and $\nabla g$ are parallel: $\nabla f=\lambda\nabla g$. Here the point is $(4/\sqrt5,1/\sqrt5)$.

:::

In the picture: at a constrained extremum the level curve of $f$ through $P$ is tangent to the constraint curve $g=c$.

::: {#exm-lagrange-hyperbola .example name="Closest point of a hyperbola"}

Find the points of $xy=3$ closest to the origin: minimise $f=x^2+y^2$ subject to $g=xy=3$.
$$2x=\lambda y,\qquad 2y=\lambda x,\qquad xy=3 .$$
The first two equations form a linear system in $x,y$ with determinant $4-\lambda^2$. If it is non-zero, $x=y=0$, which violates $xy=3$. So $\lambda=\pm2$. For $\lambda=-2$, $y=-x$ and $xy=-x^2=3$ is impossible; for $\lambda=2$, $y=x$ and $x^2=3$. The candidates are $(\sqrt3,\sqrt3)$ and $(-\sqrt3,-\sqrt3)$, at distance $\sqrt6$.

:::

::: {#fig-lagrange-multipliers-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.8]
\draw[->, faint] (-0.2,0) -- (4.6,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.2) -- (0,4.6) node[lab, above] {$y$};
\draw[emph, domain=0.68:4.4, samples=60] plot (\x,{3/\x}) node[lab, right] {$xy=3$};
\draw[faint] (2.45,0) arc (0:90:2.45);
\draw[faint] (1.8,0) arc (0:90:1.8); \draw[faint] (3.1,0) arc (0:90:3.1);
\fill (1.73,1.73) circle (1.5pt) node[lab, below left] {$(\sqrt3,\sqrt3)$};
\draw[->, hl] (1.73,1.73) -- (2.33,2.33) node[lab, right] {$\nabla f\parallel\nabla g$};
\end{tikzpicture}
\end{center}
```

Level circles $x^2+y^2=c$ of $f$ and the constraint $xy=3$ (first quadrant). The smallest circle that meets the hyperbola, $x^2+y^2=6$, is tangent to it at $(\sqrt3,\sqrt3)$, where the two gradients are parallel.

:::

::: {#rmk-lagrange-multipliers-1 .remark name="Maximum or minimum?"}

The method finds candidates only. The second derivative test does not apply to constrained variables; decide by comparing values of $f$ or by a geometric argument. In @exm-lagrange-hyperbola, $f\to\infty$ along the hyperbola, so the candidates are minima and there is no maximum.

:::

::: {#fig-lagrange-multipliers-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[y=0.2cm]
\draw[->, faint] (-0.2,0) -- (4.2,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.4) -- (0,14) node[lab, above] {};
\draw[hl] (0.86,12.95) -- (0.89,12.26) -- (0.91,11.64) -- (0.94,11.08) -- (0.97,10.57) -- (0.99,10.1) -- (1.02,9.68) -- (1.05,9.29) -- (1.07,8.94) -- (1.1,8.62) -- (1.13,8.33) -- (1.16,8.07) -- (1.18,7.83) -- (1.21,7.61) -- (1.24,7.41) -- (1.26,7.23) -- (1.29,7.06) -- (1.32,6.91) -- (1.35,6.78) -- (1.37,6.66) -- (1.4,6.55) -- (1.43,6.46) -- (1.45,6.37) -- (1.48,6.3) -- (1.51,6.23) -- (1.54,6.18) -- (1.56,6.13) -- (1.59,6.09) -- (1.62,6.06) -- (1.64,6.03) -- (1.67,6.02) -- (1.7,6) -- (1.73,6) -- (1.75,6) -- (1.78,6.01) -- (1.81,6.02) -- (1.83,6.04) -- (1.86,6.06) -- (1.89,6.09) -- (1.91,6.12) -- (1.94,6.16) -- (1.97,6.2) -- (2,6.24) -- (2.02,6.29) -- (2.05,6.34) -- (2.08,6.4) -- (2.1,6.46) -- (2.13,6.52) -- (2.16,6.59) -- (2.19,6.66) -- (2.21,6.73) -- (2.24,6.81) -- (2.27,6.89) -- (2.29,6.97) -- (2.32,7.06) -- (2.35,7.15) -- (2.38,7.24) -- (2.4,7.33) -- (2.43,7.43) -- (2.46,7.52) -- (2.48,7.63) -- (2.51,7.73) -- (2.54,7.84) -- (2.56,7.95) -- (2.59,8.06) -- (2.62,8.17) -- (2.65,8.29) -- (2.67,8.4) -- (2.7,8.52) -- (2.73,8.65) -- (2.75,8.77) -- (2.78,8.9) -- (2.81,9.03) -- (2.84,9.16) -- (2.86,9.29) -- (2.89,9.43) -- (2.92,9.56) -- (2.94,9.7) -- (2.97,9.85) -- (3,9.99) -- (3.02,10.13) -- (3.05,10.28) -- (3.08,10.43) -- (3.11,10.58) -- (3.13,10.73) -- (3.16,10.89) -- (3.19,11.05) -- (3.21,11.2) -- (3.24,11.36) -- (3.27,11.53) -- (3.3,11.69) -- (3.32,11.86) -- (3.35,12.02) -- (3.38,12.19) -- (3.4,12.36) -- (3.43,12.54) -- (3.46,12.71) -- (3.49,12.89);
\fill[accent] (1.73,6) circle[pt] node[lab, below] {$(\sqrt3,6)$};
\draw[faint, dashed] (0,6) -- (4,6);
\node[lab, right] at (3.4,12) {$x^2+\dfrac9{x^2}$};
\end{tikzpicture}
\end{center}
```

To tell a maximum from a minimum, follow $f$ along the constraint. For $f=x^2+y^2$ on $xy=3$, $x>0$: $f=x^2+9/x^2$ tends to $\infty$ at both ends, so the critical point $x=\sqrt3$ found by Lagrange multipliers is the minimum, $f=6$.

:::

::: {#exm-lagrange-pyramid .example name="The pyramid of least surface area"}

A pyramid has a given triangle (sides $a_1,a_2,a_3$, area $A$) as base and a given volume, hence a given height $h$. Where should the top vertex be to make the lateral area smallest?

Use as variables the distances $u_1,u_2,u_3$ from the foot of the height to the three sides of the base. The face over side $a_i$ is a triangle of height $\sqrt{u_i^2+h^2}$, so we minimise
$$f=\tfrac12\big(a_1\sqrt{u_1^2+h^2}+a_2\sqrt{u_2^2+h^2}+a_3\sqrt{u_3^2+h^2}\big)$$
subject to $g=\tfrac12(a_1u_1+a_2u_2+a_3u_3)=A$ (cutting the base into three triangles with heights $u_i$). The equations $f_{u_i}=\lambda g_{u_i}$ read $\dfrac{a_iu_i}{2\sqrt{u_i^2+h^2}}=\lambda\dfrac{a_i}2$, so $\dfrac{u_i}{\sqrt{u_i^2+h^2}}=\lambda$ for $i=1,2,3$. The function $u\mapsto u/\sqrt{u^2+h^2}$ is increasing, so $u_1=u_2=u_3$: the top lies above the centre of the inscribed circle of the base.

:::
