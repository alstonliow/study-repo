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

::: {#thm-linear-approximation-two-variables .theorem name="Linear approximation"}

If $f_x$ and $f_y$ exist near $(x_0,y_0)$ and are continuous there, then
$$\Delta f\approx f_x(x_0,y_0)\,\Delta x+f_y(x_0,y_0)\,\Delta y,$$
in the sense that the error divided by $\sqrt{\Delta x^2+\Delta y^2}$ tends to $0$. In words: near the point, the graph is close to its tangent plane.

:::

::: {.proof}

1. Go from $(x_0,y_0)$ to $(x_0+\Delta x,y_0+\Delta y)$ in two steps, first in $x$, then in $y$:
$$\Delta f=\big[f(x_0+\Delta x,y_0)-f(x_0,y_0)\big]+\big[f(x_0+\Delta x,y_0+\Delta y)-f(x_0+\Delta x,y_0)\big].$$

2. By the mean value theorem (@thm-mean-value) the first bracket is $f_x(\xi,y_0)\Delta x$ and the second is $f_y(x_0+\Delta x,\eta)\Delta y$, for some $\xi$ between $x_0$ and $x_0+\Delta x$ and $\eta$ between $y_0$ and $y_0+\Delta y$.

3. As $(\Delta x,\Delta y)\to(0,0)$, continuity gives $f_x(\xi,y_0)\to f_x(x_0,y_0)$ and $f_y(x_0+\Delta x,\eta)\to f_y(x_0,y_0)$.

4. So $\Delta f-f_x\Delta x-f_y\Delta y=\varepsilon_1\Delta x+\varepsilon_2\Delta y$ with $\varepsilon_1,\varepsilon_2\to0$, and $\lvert\varepsilon_1\Delta x+\varepsilon_2\Delta y\rvert\le(\lvert\varepsilon_1\rvert+\lvert\varepsilon_2\rvert)\sqrt{\Delta x^2+\Delta y^2}$.

:::

::: {#exm-linear-approximation-two-variables .example name="Estimating a change"}

For $w=x^2y$ at $(1,2)$: $w_x=2xy=4$, $w_y=x^2=1$, so $\Delta w\approx4\Delta x+\Delta y$. Moving to $(1.1,1.9)$ gives the estimate $w\approx2+0.4-0.1=2.3$; the true value is $1.21\cdot1.9=2.299$. The tangent plane at $(1,2,2)$ is $z=2+4(x-1)+(y-2)$.

:::

::: {#def-higher-partial-derivatives .definition name="Second partial derivatives"}

$$f_{xx}=\frac{\partial^2f}{\partial x^2},\qquad f_{xy}=(f_x)_y=\frac{\partial^2f}{\partial y\,\partial x},\qquad f_{yx}=(f_y)_x,\qquad f_{yy}=\frac{\partial^2f}{\partial y^2}.$$

:::

::: {#thm-mixed-partials .theorem name="Equality of mixed partials"}

If $f_{xy}$ and $f_{yx}$ exist and are continuous near a point, then $f_{xy}=f_{yx}$ there.

:::

::: {.proof}

1. Fix $h,k$ small and let $D=f(x+h,y+k)-f(x+h,y)-f(x,y+k)+f(x,y)$.

2. With $g(s)=f(s,y+k)-f(s,y)$ we have $D=g(x+h)-g(x)=h\,g'(\xi)=h\,[f_x(\xi,y+k)-f_x(\xi,y)]$ for some $\xi$ between $x$ and $x+h$, by the mean value theorem; applying it again in the second variable, $D=hk\,f_{xy}(\xi,\eta)$.

3. Grouping the four terms the other way, with $u(t)=f(x+h,t)-f(x,t)$, the same argument gives $D=hk\,f_{yx}(\xi',\eta')$.

4. So $f_{xy}(\xi,\eta)=f_{yx}(\xi',\eta')$. Let $h,k\to0$: both points tend to $(x,y)$ and continuity gives $f_{xy}(x,y)=f_{yx}(x,y)$.

:::

For example $f=x^3y+y^2$ has $f_{xy}=3x^2=f_{yx}$.
