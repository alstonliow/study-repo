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

<!-- Merged 2026-11-20 (owner): the block thm-linear-approximation-two-variables (statement and two-step mean value proof) was removed in favour of thm-continuous-partials-differentiable in math/analysis/differentiation/derivative-of-maps, which proves the same for any number of variables. -->

**Linear approximation.** If $f_x$ and $f_y$ exist near $(x_0,y_0)$ and are continuous there, then
$$\Delta f\approx f_x(x_0,y_0)\,\Delta x+f_y(x_0,y_0)\,\Delta y,$$
in the sense that the error divided by $\sqrt{\Delta x^2+\Delta y^2}$ tends to $0$: near the point, the graph is close to its tangent plane. This is @thm-continuous-partials-differentiable for two variables, proved there by moving along the axes and using the mean value theorem on each step.

::: {#exm-linear-approximation-two-variables .example name="Estimating a change"}

For $w=x^2y$ at $(1,2)$: $w_x=2xy=4$, $w_y=x^2=1$, so $\Delta w\approx4\Delta x+\Delta y$. Moving to $(1.1,1.9)$ gives the estimate $w\approx2+0.4-0.1=2.3$; the true value is $1.21\cdot1.9=2.299$. The tangent plane at $(1,2,2)$ is $z=2+4(x-1)+(y-2)$.

:::

::: {#def-higher-partial-derivatives .definition name="Second partial derivatives"}

$$f_{xx}=\frac{\partial^2f}{\partial x^2},\qquad f_{xy}=(f_x)_y=\frac{\partial^2f}{\partial y\,\partial x},\qquad f_{yx}=(f_y)_x,\qquad f_{yy}=\frac{\partial^2f}{\partial y^2}.$$

:::

<!-- Merged 2026-11-20 (owner): the block thm-mixed-partials was removed in favour of thm-symmetry-mixed-partials in math/analysis/differentiation/second-derivatives (same second-difference proof, weaker hypothesis: continuity at the point). -->

**Equality of mixed partials.** If $f_{xy}$ and $f_{yx}$ exist near a point and are continuous at it, then $f_{xy}=f_{yx}$ there (@thm-symmetry-mixed-partials). Without continuity they can differ (@exm-mixed-partials-differ).

For example $f=x^3y+y^2$ has $f_{xy}=3x^2=f_{yx}$.
