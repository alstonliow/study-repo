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

::: {#fig-double-integrals-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (2.6,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.2) -- (0,2.2) node[lab, above] {$y$};
\draw[cell frame] (0.2,0.2) rectangle (0.42,0.42);
\draw[cell frame] (0.2,0.42) rectangle (0.42,0.64);
\draw[cell frame] (0.2,0.64) rectangle (0.42,0.86);
\draw[cell frame] (0.2,0.86) rectangle (0.42,1.08);
\draw[cell frame] (0.2,1.08) rectangle (0.42,1.3);
\draw[cell frame] (0.42,0.2) rectangle (0.64,0.42);
\draw[cell frame] (0.42,0.42) rectangle (0.64,0.64);
\draw[cell frame] (0.42,0.64) rectangle (0.64,0.86);
\draw[cell frame] (0.42,0.86) rectangle (0.64,1.08);
\draw[cell frame] (0.42,1.08) rectangle (0.64,1.3);
\draw[cell frame] (0.42,1.3) rectangle (0.64,1.52);
\draw[cell frame] (0.64,0.2) rectangle (0.86,0.42);
\draw[cell frame] (0.64,0.42) rectangle (0.86,0.64);
\draw[cell frame] (0.64,0.64) rectangle (0.86,0.86);
\draw[cell frame] (0.64,0.86) rectangle (0.86,1.08);
\draw[cell frame] (0.64,1.08) rectangle (0.86,1.3);
\draw[cell frame] (0.64,1.3) rectangle (0.86,1.52);
\draw[cell frame] (0.64,1.52) rectangle (0.86,1.74);
\draw[cell frame] (0.86,0.2) rectangle (1.08,0.42);
\draw[cell frame] (0.86,0.42) rectangle (1.08,0.64);
\draw[cell frame] (0.86,0.64) rectangle (1.08,0.86);
\draw[cell frame] (0.86,0.86) rectangle (1.08,1.08);
\draw[cell frame] (0.86,1.08) rectangle (1.08,1.3);
\draw[cell frame] (0.86,1.3) rectangle (1.08,1.52);
\draw[cell frame] (0.86,1.52) rectangle (1.08,1.74);
\draw[cell frame] (1.08,0.2) rectangle (1.3,0.42);
\draw[cell frame] (1.08,0.42) rectangle (1.3,0.64);
\draw[cell frame] (1.08,0.64) rectangle (1.3,0.86);
\draw[cell frame] (1.08,0.86) rectangle (1.3,1.08);
\draw[cell frame] (1.08,1.08) rectangle (1.3,1.3);
\draw[cell frame] (1.08,1.3) rectangle (1.3,1.52);
\draw[cell frame] (1.08,1.52) rectangle (1.3,1.74);
\draw[cell frame] (1.3,0.2) rectangle (1.52,0.42);
\draw[cell frame] (1.3,0.42) rectangle (1.52,0.64);
\draw[cell frame] (1.3,0.64) rectangle (1.52,0.86);
\draw[cell frame] (1.3,0.86) rectangle (1.52,1.08);
\draw[cell frame] (1.3,1.08) rectangle (1.52,1.3);
\draw[cell frame] (1.3,1.3) rectangle (1.52,1.52);
\draw[cell frame] (1.3,1.52) rectangle (1.52,1.74);
\draw[cell frame] (1.52,0.2) rectangle (1.74,0.42);
\draw[cell frame] (1.52,0.42) rectangle (1.74,0.64);
\draw[cell frame] (1.52,0.64) rectangle (1.74,0.86);
\draw[cell frame] (1.52,0.86) rectangle (1.74,1.08);
\draw[cell frame] (1.52,1.08) rectangle (1.74,1.3);
\draw[cell frame] (1.52,1.3) rectangle (1.74,1.52);
\draw[cell frame] (1.52,1.52) rectangle (1.74,1.74);
\draw[cell frame] (1.74,0.2) rectangle (1.96,0.42);
\draw[cell frame] (1.74,0.42) rectangle (1.96,0.64);
\draw[cell frame] (1.74,0.64) rectangle (1.96,0.86);
\draw[cell frame] (1.74,0.86) rectangle (1.96,1.08);
\draw[cell frame] (1.74,1.08) rectangle (1.96,1.3);
\draw[cell frame] (1.74,1.3) rectangle (1.96,1.52);
\draw[cell frame] (1.74,1.52) rectangle (1.96,1.74);
\draw[cell frame] (1.96,0.2) rectangle (2.18,0.42);
\draw[cell frame] (1.96,0.42) rectangle (2.18,0.64);
\draw[cell frame] (1.96,0.64) rectangle (2.18,0.86);
\draw[cell frame] (1.96,0.86) rectangle (2.18,1.08);
\draw[cell frame] (1.96,1.08) rectangle (2.18,1.3);
\draw[cell frame] (1.96,1.3) rectangle (2.18,1.52);
\draw[hl cell] (1.08,0.64) rectangle (1.3,0.86);
\draw[emph] (0.2,1.37) -- (0.24,1.41) -- (0.27,1.44) -- (0.31,1.47) -- (0.35,1.5) -- (0.38,1.53) -- (0.42,1.55) -- (0.46,1.58) -- (0.49,1.61) -- (0.53,1.63) -- (0.57,1.66) -- (0.6,1.68) -- (0.64,1.71) -- (0.68,1.73) -- (0.71,1.75) -- (0.75,1.77) -- (0.79,1.79) -- (0.82,1.81) -- (0.86,1.83) -- (0.9,1.84) -- (0.93,1.86) -- (0.97,1.87) -- (1.01,1.88) -- (1.04,1.89) -- (1.08,1.9) -- (1.12,1.91) -- (1.15,1.91) -- (1.19,1.92) -- (1.23,1.92) -- (1.26,1.92) -- (1.3,1.93) -- (1.34,1.93) -- (1.37,1.92) -- (1.41,1.92) -- (1.45,1.92) -- (1.48,1.91) -- (1.52,1.9) -- (1.56,1.9) -- (1.59,1.89) -- (1.63,1.88) -- (1.67,1.86) -- (1.7,1.85) -- (1.74,1.84) -- (1.78,1.82) -- (1.81,1.81) -- (1.85,1.79) -- (1.89,1.77) -- (1.92,1.75) -- (1.96,1.73) -- (2,1.71) -- (2.03,1.69) -- (2.07,1.67) -- (2.11,1.65) -- (2.14,1.62) -- (2.18,1.6) -- (2.22,1.58) -- (2.25,1.55) -- (2.29,1.53) -- (2.33,1.5) -- (2.36,1.48) -- (2.4,1.45);
\draw[emph] (0.2,0.2) -- (2.4,0.2) -- (2.4,1.45) (0.2,0.2) -- (0.2,1.37);
\node[lab, right] at (1.6,0.75) {$\Delta A_i$};
\end{tikzpicture}
\end{center}
```

The double integral as a limit of sums: cut the region into small rectangles of area $\Delta A_i$, take $\sum f(x_i,y_i)\,\Delta A_i$ (volume of thin boxes under the graph), and let the rectangles shrink.

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

::: {#fig-double-integrals-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=2]
\draw[->, faint] (-0.2,0) -- (1.4,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.2) -- (0,1.3) node[lab, above] {$y$};
\fill[tintA] (0,0) -- (1,0) -- (1,0.05) -- (0.99,0.11) -- (0.99,0.16) -- (0.98,0.21) -- (0.96,0.27) -- (0.95,0.32) -- (0.93,0.37) -- (0.91,0.42) -- (0.88,0.47) -- (0.86,0.52) -- (0.83,0.56) -- (0.8,0.61) -- (0.76,0.65) -- (0.73,0.69) -- (0.69,0.73) -- (0.65,0.76) -- (0.61,0.8) -- (0.56,0.83) -- (0.52,0.86) -- (0.47,0.88) -- (0.42,0.91) -- (0.37,0.93) -- (0.32,0.95) -- (0.27,0.96) -- (0.21,0.98) -- (0.16,0.99) -- (0.11,0.99) -- (0.05,1) -- (0,1) -- cycle;
\draw[emph] (1,0) arc[start angle=0, end angle=90, radius=1];
\draw[hl] (0.55,0) -- (0.55,0.84);
\node[lab] at (0.55,-0.15) {$x$};
\node[lab, above right] at (0.57,0.84) {$y=\sqrt{1-x^2}$};
\node[lab, right] at (0.57,0.08) {$y=0$};
\end{tikzpicture}
\end{center}
```

Limits for the quarter disk: a vertical line at $x$ meets the region from $y=0$ up to the circle $y=\sqrt{1-x^2}$, and $x$ runs from $0$ to $1$.

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
