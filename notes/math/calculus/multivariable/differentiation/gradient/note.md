---
title: "The Gradient and Directional Derivatives"
sources: [mit1802-12]
requires: [math/calculus/multivariable/differentiation/differentials-and-chain-rule]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lecture 12, in our own wording. Numbers checked in Python. -->

::: {#def-gradient .definition name="Gradient"}

The **gradient** of $w=f(x,y,z)$ is the vector of its partial derivatives,
$$\nabla w=\langle w_x,w_y,w_z\rangle .$$
It depends on the point where it is evaluated (it is a vector field). With it the chain rule (@thm-multivariable-chain-rule) reads
$$\frac{dw}{dt}=\nabla w\cdot\frac{d\mathbf{r}}{dt}.$$

:::

::: {#thm-gradient-normal-to-level-surface .theorem name="The gradient is normal to level surfaces"}

At a point $P$ of the level surface $w=c$, the gradient $\nabla w(P)$ is perpendicular to the surface: it is perpendicular to the velocity of every curve through $P$ inside the surface.

:::

::: {.proof}

1. Let $\mathbf{r}(t)$ be a curve contained in the level surface with $\mathbf{r}(t_0)=P$. Then $w(\mathbf{r}(t))=c$ for all $t$.

2. Differentiate with the chain rule: $0=\dfrac{dw}{dt}=\nabla w\cdot\dfrac{d\mathbf{r}}{dt}$.

3. So $\nabla w(P)$ is perpendicular to the velocity $\mathbf{v}(t_0)$. Every tangent vector to the surface at $P$ is such a velocity, so $\nabla w(P)$ is perpendicular to the tangent plane.

:::

For $w=ax+by+cz$ the level surfaces are parallel planes and $\nabla w=\langle a,b,c\rangle$ is their normal; for $w=x^2+y^2$ the level curves are circles and $\nabla w=\langle2x,2y\rangle$ points radially outwards.

::: {#exm-tangent-plane-level-surface .example name="Tangent plane to a level surface"}

The surface $x^2+y^2-z^2=4$ at $(2,1,1)$: $\nabla w=\langle2x,2y,-2z\rangle=\langle4,2,-2\rangle$, so the tangent plane is $4(x-2)+2(y-1)-2(z-1)=0$, i.e. $4x+2y-2z=8$. The same plane comes from the approximation $\Delta w\approx4\Delta x+2\Delta y-2\Delta z$ with $\Delta w=0$.

:::

::: {#def-directional-derivative .definition name="Directional derivative"}

For a unit vector $\hat{\mathbf{u}}$, the **directional derivative** of $w$ at $P$ in the direction $\hat{\mathbf{u}}$ is the rate of change of $w$ along the straight line through $P$ with unit velocity $\hat{\mathbf{u}}$, $\mathbf{r}(s)=P+s\hat{\mathbf{u}}$:
$$\frac{dw}{ds}\Big\vert_{\hat{\mathbf{u}}}=\frac{d}{ds}\,w\big(P+s\hat{\mathbf{u}}\big)\Big\vert_{s=0}.$$

:::

For a function of two variables it is the slope of the slice of the graph by the vertical plane through $P$ in the direction $\hat{\mathbf{u}}$; $w_x$ and $w_y$ are the cases $\hat{\mathbf{u}}=\mathbf{i}$ and $\hat{\mathbf{u}}=\mathbf{j}$.

::: {#thm-directional-derivative-gradient .theorem name="Directional derivative from the gradient"}

$$\frac{dw}{ds}\Big\vert_{\hat{\mathbf{u}}}=\nabla w\cdot\hat{\mathbf{u}}=\lvert\nabla w\rvert\cos\theta,$$
where $\theta$ is the angle between $\nabla w$ and $\hat{\mathbf{u}}$. Hence $\nabla w$ points in the direction in which $w$ increases fastest, $\lvert\nabla w\rvert$ is that fastest rate, and the rate is $0$ in the directions tangent to the level surface.

:::

::: {.proof}

1. By the chain rule along $\mathbf{r}(s)=P+s\hat{\mathbf{u}}$: $\dfrac{dw}{ds}=\nabla w\cdot\dfrac{d\mathbf{r}}{ds}=\nabla w\cdot\hat{\mathbf{u}}$.

2. As $\lvert\hat{\mathbf{u}}\rvert=1$, this equals $\lvert\nabla w\rvert\cos\theta$, which is largest, equal to $\lvert\nabla w\rvert$, when $\theta=0$, and zero when $\hat{\mathbf{u}}\perp\nabla w$.

:::

::: {#exm-directional-derivative .example name="A directional derivative"}

$w=x^2+y^2+1$ at $(1,1)$: $\nabla w=\langle2,2\rangle$. In the direction $\hat{\mathbf{u}}=\langle\frac35,\frac45\rangle$ the rate is $\frac65+\frac85=\frac{14}5$; the largest rate is $\lvert\nabla w\rvert=2\sqrt2\approx2.83$, in the direction $\langle1,1\rangle/\sqrt2$.

:::
