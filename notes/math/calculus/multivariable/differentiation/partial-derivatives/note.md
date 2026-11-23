---
title: "Partial Derivatives and the Tangent Plane"
sources: [mit1802-8, mit1802-9, mit1802n-TA]
requires: [math/calculus/multivariable/differentiation/functions-of-several-variables, math/calculus/single-variable/applications-of-derivatives/linear-and-quadratic-approximation]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lectures 8-9 and Supplementary Notes TA, in our own wording. Numbers checked in Python. -->

::: {#def-partial-derivative .definition name="Partial derivatives"}

For $w=f(x,y)$ at $(x_0,y_0)$,
$$f_x(x_0,y_0)=\frac{\partial f}{\partial x}(x_0,y_0)=\lim_{\Delta x\to0}\frac{f(x_0+\Delta x,y_0)-f(x_0,y_0)}{\Delta x},$$
and similarly $f_y$, varying $y$ with $x=x_0$ fixed. Functions of more variables have one partial derivative per variable.

:::

To compute $f_x$, treat every variable except $x$ as a constant and differentiate as in one variable. For $f=x^3y+y^2$: $f_x=3x^2y$, $f_y=x^3+2y$.

Geometrically, the slice of the graph by the plane $y=y_0$ is the curve $z=f(x,y_0)$; $f_x(x_0,y_0)$ is the slope of its tangent line. Likewise $f_y$ is the slope of the slice $x=x_0$.

::: {#fig-partial-derivatives-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.3,0) -- (4,0) node[lab, right] {$x$}; \draw[->, faint] (0,-0.3) -- (0,2.5) node[lab, above] {$y$};
\draw[emph, domain=0.2:3.6, samples=40] plot (\x,{0.25*\x*\x-0.3*\x+0.6});
\fill[ink] (2,1) circle[pt] node[lab, above left] {$(x_0,f(x_0,y_0))$};
\draw[hl] (1,0.3) -- (3.2,1.84) node[lab, right] {slope $f_x(x_0,y_0)$};
\end{tikzpicture}
\end{center}
```

The slice $y=y_0$ of the graph $z=f(x,y)$ is a curve $z=f(x,y_0)$; its slope at $x_0$ is $f_x(x_0,y_0)$. The slice $x=x_0$ gives $f_y$ the same way.

:::

::: {#def-tangent-plane-graph .definition name="Tangent plane to a graph"}

The tangent plane to the graph $z=f(x,y)$ at $(x_0,y_0,z_0)$, $z_0=f(x_0,y_0)$, is
$$z=z_0+f_x(x_0,y_0)(x-x_0)+f_y(x_0,y_0)(y-y_0).$$
It is the plane containing the tangent lines of the two slices $y=y_0$ and $x=x_0$.

:::

::: {#fig-partial-derivatives-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (0,0) -- (-1.1,-0.7) node[lab, below left] {$x$};
\draw[->, faint] (0,0) -- (2.2,0) node[lab, right] {$y$};
\draw[->, faint] (0,0) -- (0,2.4) node[lab, above] {$z$};
\draw[faint] (0,1.8) -- (0.09,1.8) -- (0.19,1.79) -- (0.28,1.78) -- (0.38,1.76) -- (0.47,1.74) -- (0.57,1.72) -- (0.66,1.69) -- (0.76,1.66) -- (0.85,1.62) -- (0.95,1.58) -- (1.04,1.53) -- (1.14,1.48) -- (1.23,1.42) -- (1.33,1.36) -- (1.42,1.3) -- (1.52,1.23) -- (1.61,1.15) -- (1.71,1.07) -- (1.8,0.99);
\draw[faint] (-0.23,1.61) -- (-0.13,1.6) -- (-0.04,1.6) -- (0.06,1.59) -- (0.15,1.57) -- (0.25,1.55) -- (0.34,1.52) -- (0.44,1.5) -- (0.53,1.46) -- (0.63,1.42) -- (0.72,1.38) -- (0.82,1.33) -- (0.91,1.28) -- (1.01,1.23) -- (1.1,1.17) -- (1.2,1.1) -- (1.29,1.03) -- (1.39,0.96) -- (1.48,0.88) -- (1.57,0.8);
\draw[faint] (-0.45,1.31) -- (-0.36,1.31) -- (-0.26,1.3) -- (-0.17,1.29) -- (-0.07,1.27) -- (0.02,1.25) -- (0.12,1.23) -- (0.21,1.2) -- (0.31,1.17) -- (0.4,1.13) -- (0.5,1.09) -- (0.59,1.04) -- (0.69,0.99) -- (0.78,0.93) -- (0.88,0.87) -- (0.97,0.8) -- (1.07,0.74) -- (1.16,0.66) -- (1.26,0.58) -- (1.35,0.5);
\draw[faint] (-0.68,0.91) -- (-0.58,0.91) -- (-0.49,0.9) -- (-0.39,0.89) -- (-0.3,0.88) -- (-0.2,0.86) -- (-0.11,0.83) -- (-0.01,0.8) -- (0.08,0.77) -- (0.18,0.73) -- (0.27,0.69) -- (0.37,0.64) -- (0.46,0.59) -- (0.56,0.53) -- (0.65,0.47) -- (0.75,0.41) -- (0.84,0.34) -- (0.94,0.26) -- (1.03,0.19) -- (1.12,0.1);
\draw[faint] (-0.9,0.41) -- (-0.81,0.41) -- (-0.71,0.41) -- (-0.62,0.39) -- (-0.52,0.38) -- (-0.43,0.36) -- (-0.33,0.33) -- (-0.24,0.3) -- (-0.14,0.27) -- (-0.05,0.23) -- (0.05,0.19) -- (0.14,0.14) -- (0.24,0.09) -- (0.33,0.03) -- (0.43,-0.03) -- (0.52,-0.09) -- (0.62,-0.16) -- (0.71,-0.23) -- (0.81,-0.31) -- (0.9,-0.4);
\draw[faint] (0,1.8) -- (-0.05,1.77) -- (-0.09,1.73) -- (-0.14,1.69) -- (-0.19,1.64) -- (-0.24,1.59) -- (-0.28,1.54) -- (-0.33,1.48) -- (-0.38,1.41) -- (-0.43,1.35) -- (-0.47,1.27) -- (-0.52,1.2) -- (-0.57,1.11) -- (-0.62,1.03) -- (-0.66,0.94) -- (-0.71,0.84) -- (-0.76,0.74) -- (-0.81,0.64) -- (-0.85,0.53) -- (-0.9,0.41);
\draw[faint] (0.45,1.75) -- (0.4,1.72) -- (0.36,1.68) -- (0.31,1.64) -- (0.26,1.59) -- (0.21,1.54) -- (0.17,1.49) -- (0.12,1.43) -- (0.07,1.36) -- (0.02,1.29) -- (-0.02,1.22) -- (-0.07,1.14) -- (-0.12,1.06) -- (-0.17,0.98) -- (-0.21,0.89) -- (-0.26,0.79) -- (-0.31,0.69) -- (-0.36,0.59) -- (-0.4,0.48) -- (-0.45,0.36);
\draw[faint] (0.9,1.6) -- (0.85,1.56) -- (0.81,1.53) -- (0.76,1.49) -- (0.71,1.44) -- (0.66,1.39) -- (0.62,1.33) -- (0.57,1.28) -- (0.52,1.21) -- (0.47,1.14) -- (0.43,1.07) -- (0.38,0.99) -- (0.33,0.91) -- (0.28,0.82) -- (0.24,0.73) -- (0.19,0.64) -- (0.14,0.54) -- (0.09,0.43) -- (0.05,0.32) -- (0,0.21);
\draw[faint] (1.35,1.34) -- (1.3,1.31) -- (1.26,1.27) -- (1.21,1.23) -- (1.16,1.19) -- (1.11,1.14) -- (1.07,1.08) -- (1.02,1.02) -- (0.97,0.96) -- (0.92,0.89) -- (0.88,0.82) -- (0.83,0.74) -- (0.78,0.66) -- (0.73,0.57) -- (0.69,0.48) -- (0.64,0.38) -- (0.59,0.28) -- (0.54,0.18) -- (0.5,0.07) -- (0.45,-0.04);
\draw[faint] (1.8,0.99) -- (1.75,0.96) -- (1.71,0.92) -- (1.66,0.88) -- (1.61,0.83) -- (1.56,0.78) -- (1.52,0.73) -- (1.47,0.67) -- (1.42,0.6) -- (1.37,0.54) -- (1.33,0.46) -- (1.28,0.39) -- (1.23,0.3) -- (1.18,0.22) -- (1.14,0.13) -- (1.09,0.03) -- (1.04,-0.07) -- (0.99,-0.17) -- (0.95,-0.28) -- (0.9,-0.4);
\fill[tintB] (0.15,1.84) -- (-0.45,0.92) -- (0.75,0.38) -- (1.35,1.3) -- cycle;
\draw[hl] (0.15,1.84) -- (-0.45,0.92) -- (0.75,0.38) -- (1.35,1.3) -- cycle;
\fill[accent] (0.45,1.11) circle[pt];
\end{tikzpicture}
\end{center}
```

The tangent plane $z-z_0=f_x(x-x_0)+f_y(y-y_0)$ (shaded) to the graph of $z=1.8-\tfrac14(x^2+y^2)$ (grid of slices) at the marked point. It contains the tangent lines of both slices through the point.

:::

<!-- Merged 2026-11-20 (owner): the block thm-linear-approximation-two-variables (statement and two-step mean value proof) was removed in favour of thm-continuous-partials-differentiable in math/analysis/differentiation/derivative-of-maps, which proves the same for any number of variables. -->

**Linear approximation.** If $f_x$ and $f_y$ exist near $(x_0,y_0)$ and are continuous there, then
$$\Delta f\approx f_x(x_0,y_0)\,\Delta x+f_y(x_0,y_0)\,\Delta y,$$
in the sense that the error divided by $\sqrt{\Delta x^2+\Delta y^2}$ tends to $0$: near the point, the graph is close to its tangent plane. This is @thm-continuous-partials-differentiable for two variables, proved there by moving along the axes and using the mean value theorem on each step.

::: {#exm-linear-approximation-two-variables .example name="Estimating a change"}

For $w=x^2y$ at $(1,2)$: $w_x=2xy=4$, $w_y=x^2=1$, so $\Delta w\approx4\Delta x+\Delta y$. Moving to $(1.1,1.9)$ gives the estimate $w\approx2+0.4-0.1=2.3$; the true value is $1.21\cdot1.9=2.299$. The tangent plane at $(1,2,2)$ is $z=2+4(x-1)+(y-2)$.

:::

::: {#fig-partial-derivatives-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (3.2,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.2) -- (0,3) node[lab, above] {$y$};
\draw[faint] ;
\draw[faint] (0,1) -- (1.5,0.25);
\draw[faint] (0,1.5) -- (1.5,0.75) -- (3,0);
\draw[faint] (0,2) -- (1.5,1.25) -- (3,0.5);
\draw[faint] (0,2.5) -- (1.5,1.75) -- (3,1);
\draw[faint] (1.5,2.25) -- (3,1.5);
\fill[ink] (1,1) circle[pt] node[lab, below left] {$P$};
\draw[->, hl] (1,1) -- (2,1);
\draw[->, hl] (1,1) -- (1,2);
\node[lab, below] at (1.5,0.75) {crosses $\tfrac12$ unit};
\node[lab, right] at (1.05,1.5) {crosses $1$ unit};
\end{tikzpicture}
\end{center}
```

Reading partial derivatives off a contour plot: level lines of $f=\tfrac12x+y$ at spacing $\tfrac12$. A unit step in $x$ from $P$ crosses one gap ($f_x=\tfrac12$), a unit step in $y$ crosses two ($f_y=1$); the linear approximation $\Delta f\approx f_x\Delta x+f_y\Delta y$ adds them.

:::

::: {#def-higher-partial-derivatives .definition name="Second partial derivatives"}

$$f_{xx}=\frac{\partial^2f}{\partial x^2},\qquad f_{xy}=(f_x)_y=\frac{\partial^2f}{\partial y\,\partial x},\qquad f_{yx}=(f_y)_x,\qquad f_{yy}=\frac{\partial^2f}{\partial y^2}.$$

:::

<!-- Merged 2026-11-20 (owner): the block thm-mixed-partials was removed in favour of thm-symmetry-mixed-partials in math/analysis/differentiation/second-derivatives (same second-difference proof, weaker hypothesis: continuity at the point). -->

**Equality of mixed partials.** If $f_{xy}$ and $f_{yx}$ exist near a point and are continuous at it, then $f_{xy}=f_{yx}$ there (@thm-symmetry-mixed-partials). Without continuity they can differ (@exm-mixed-partials-differ).

For example $f=x^3y+y^2$ has $f_{xy}=3x^2=f_{yx}$.
