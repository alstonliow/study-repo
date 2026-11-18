---
title: "Double Integrals and Iterated Integrals"
sources: [mit1802-16, mit1802n-I]
requires: [math/calculus/multivariable/differentiation/functions-of-several-variables, math/calculus/single-variable/applications-of-integrals/volumes]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lecture 16 and Supplementary Notes I.1, in our own wording. Numbers checked in Python (sympy). -->

::: {#def-double-integral .definition name="Double integral"}

Let $R$ be a bounded region of the plane and $f$ a function on $R$. Cut $R$ into small pieces of areas $\Delta A_i$ and pick a point $(x_i,y_i)$ in each. The **double integral** is the limit of the sums
$$\iint_Rf(x,y)\,dA=\lim\sum_if(x_i,y_i)\,\Delta A_i$$
as the pieces shrink to points. For $f\ge0$ it is the volume of the solid under the graph $z=f(x,y)$ and above $R$.

:::

::: {#thm-iterated-integral .theorem name="Computing by iterated integrals"}

If $R$ is the region $a\le x\le b$, $y_1(x)\le y\le y_2(x)$ and $f$ is continuous, then
$$\iint_Rf\,dA=\int_a^b\left(\int_{y_1(x)}^{y_2(x)}f(x,y)\,dy\right)dx .$$
In the inner integral $x$ is a constant; its limits may depend on $x$, the outer limits are constants. The same holds with the roles of $x$ and $y$ exchanged.

:::

::: {.proof}

1. (Sketch, for $f\ge0$.) Slice the solid under the graph by the plane perpendicular to the $x$-axis at $x$. The slice has area $S(x)=\int_{y_1(x)}^{y_2(x)}f(x,y)\,dy$.

2. The volume is the integral of the areas of the slices (@prp-volume-by-slices): $\int_a^bS(x)\,dx$.

:::

::: {#prp-setting-up-limits .proposition name="Setting up the limits"}

To integrate $dy\,dx$ over $R$:

1. Draw $R$.
2. Fix $x$ and move along the vertical line through $x$ in the direction of increasing $y$: it enters $R$ at $y_1(x)$ and leaves at $y_2(x)$. These are the inner limits.
3. The outer limits are the smallest and largest $x$ for which the vertical line meets $R$.

If a vertical line meets $R$ in several segments, cut $R$ into pieces.

:::

::: {#exm-double-integral-square .example name="Under a paraboloid, over a square"}

$\displaystyle\int_0^1\!\!\int_0^1(1-x^2-y^2)\,dy\,dx$. Inner: $\big[(1-x^2)y-\frac{y^3}3\big]_0^1=\frac23-x^2$. Outer: $\int_0^1(\frac23-x^2)\,dx=\frac23-\frac13=\frac13$.

:::

::: {#exm-double-integral-quarter-disk .example name="Over a quarter disk"}

Over the quarter of the unit disk in the first quadrant, a vertical line at $x$ runs from $y=0$ to $y=\sqrt{1-x^2}$, and $0\le x\le1$:
$$\int_0^1\!\!\int_0^{\sqrt{1-x^2}}(1-x^2-y^2)\,dy\,dx=\int_0^1\tfrac23(1-x^2)^{3/2}\,dx=\frac\pi8 .$$
The last integral needs the substitution $x=\sin\theta$; polar coordinates (@exm-polar-quarter-disk) make it easy.

:::

::: {#exm-exchange-order .example name="Exchanging the order of integration"}

$\displaystyle\int_0^1\!\!\int_x^{\sqrt x}\frac{e^y}y\,dy\,dx$ cannot be done as written: $e^y/y$ has no elementary antiderivative. The region is $x\le y\le\sqrt x$, $0\le x\le1$, i.e. between the line $y=x$ and the parabola $x=y^2$. For fixed $y$, $x$ runs from $y^2$ to $y$, and $0\le y\le1$:
$$\int_0^1\!\!\int_{y^2}^y\frac{e^y}y\,dx\,dy=\int_0^1(1-y)e^y\,dy=\big[(2-y)e^y\big]_0^1=e-2 .$$

:::

::: {#fig-double-integrals-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=3]
\draw[->, faint] (-0.1,0) -- (1.35,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.1) -- (0,1.3) node[lab, above] {$y$};
\fill[tintA] (0,0) -- plot[domain=0:1, samples=40] (\x,{sqrt(\x)}) -- (1,1) -- cycle;
\draw[emph] (0,0) -- (1.1,1.1) node[lab, below right] {$y=x$};
\draw[emph, domain=0:1, samples=40] plot (\x,{sqrt(\x)});
\node[lab, above left] at (0.62,0.8) {$y=\sqrt x$};
\draw[hl] (0.3,0.3) -- (0.3,0.5477);
\draw[hl, dashed] (0.36,0.6) -- (0.6,0.6);
\node[lab, below] at (0.3,0) {$x$}; \node[lab, left] at (0,0.6) {$y$};
\end{tikzpicture}
\end{center}
```

The region $x\le y\le\sqrt x$. A vertical slice (solid) runs from $y=x$ to $y=\sqrt x$; a horizontal slice (dashed) runs from $x=y^2$ to $x=y$.

:::

::: {#rmk-double-integrals-1 .remark name="Rectangles"}

Over a rectangle $a\le x\le b$, $c\le y\le d$ the limits are constants in both orders, and the order can be swapped freely. For a product $f(x)g(y)$ the integral is $\int_a^bf\,dx\cdot\int_c^dg\,dy$.

:::
