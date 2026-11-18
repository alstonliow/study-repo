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

::: {#exm-lagrange-pyramid .example name="The pyramid of least surface area"}

A pyramid has a given triangle (sides $a_1,a_2,a_3$, area $A$) as base and a given volume, hence a given height $h$. Where should the top vertex be to make the lateral area smallest?

Use as variables the distances $u_1,u_2,u_3$ from the foot of the height to the three sides of the base. The face over side $a_i$ is a triangle of height $\sqrt{u_i^2+h^2}$, so we minimise
$$f=\tfrac12\big(a_1\sqrt{u_1^2+h^2}+a_2\sqrt{u_2^2+h^2}+a_3\sqrt{u_3^2+h^2}\big)$$
subject to $g=\tfrac12(a_1u_1+a_2u_2+a_3u_3)=A$ (cutting the base into three triangles with heights $u_i$). The equations $f_{u_i}=\lambda g_{u_i}$ read $\dfrac{a_iu_i}{2\sqrt{u_i^2+h^2}}=\lambda\dfrac{a_i}2$, so $\dfrac{u_i}{\sqrt{u_i^2+h^2}}=\lambda$ for $i=1,2,3$. The function $u\mapsto u/\sqrt{u^2+h^2}$ is increasing, so $u_1=u_2=u_3$: the top lies above the centre of the inscribed circle of the base.

:::
