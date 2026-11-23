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
It depends on the point where it is evaluated (it is a vector field). With it the chain rule (@thm-chain-rule-several-variables) reads
$$\frac{dw}{dt}=\nabla w\cdot\frac{d\mathbf{r}}{dt}.$$

:::

::: {#fig-gradient-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \r in {0.6,1.2,1.8} \draw[emph] (0,0) circle (\r);
\fill[ink] (1.06,0.85) circle[pt] node[lab, below left] {$P$};
\draw[->, hl] (1.06,0.85) -- (1.76,1.41) node[lab, above right] {$\nabla f$};
\draw[faint, dashed] (0.5,1.55) -- (1.62,0.15);
\end{tikzpicture}
\end{center}
```

Level curves of $f=x^2+y^2$. At each point the gradient is perpendicular to the level curve (dashed tangent line) and points towards larger values.

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

::: {#fig-gradient-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.4,0) -- (3.2,0) node[lab, right] {$x$};
\draw[->, faint] (0,-1.6) -- (0,2.2) node[lab, above] {$z$};
\draw[emph] (2.29,-1.5) -- (2.25,-1.44) -- (2.22,-1.39) -- (2.18,-1.33) -- (2.15,-1.27) -- (2.12,-1.22) -- (2.08,-1.16) -- (2.05,-1.1) -- (2.02,-1.05) -- (2,-0.99) -- (1.97,-0.93) -- (1.94,-0.88) -- (1.92,-0.82) -- (1.89,-0.76) -- (1.87,-0.71) -- (1.85,-0.65) -- (1.83,-0.59) -- (1.81,-0.54) -- (1.8,-0.48) -- (1.78,-0.42) -- (1.77,-0.37) -- (1.76,-0.31) -- (1.75,-0.25) -- (1.74,-0.2) -- (1.74,-0.14) -- (1.73,-0.08) -- (1.73,-0.03) -- (1.73,0.03) -- (1.73,0.09) -- (1.74,0.14) -- (1.74,0.2) -- (1.75,0.26) -- (1.76,0.31) -- (1.77,0.37) -- (1.78,0.43) -- (1.8,0.48) -- (1.81,0.54) -- (1.83,0.6) -- (1.85,0.65) -- (1.87,0.71) -- (1.89,0.77) -- (1.92,0.82) -- (1.94,0.88) -- (1.97,0.94) -- (2,0.99) -- (2.03,1.05) -- (2.06,1.11) -- (2.09,1.16) -- (2.12,1.22) -- (2.15,1.28) -- (2.19,1.33) -- (2.22,1.39) -- (2.26,1.45) -- (2.29,1.5) -- (2.33,1.56) -- (2.37,1.62) -- (2.41,1.67) -- (2.45,1.73) -- (2.49,1.79) -- (2.53,1.84) -- (2.57,1.9);
\fill[accent] (2,1) circle[pt] node[lab, right] {$(2,1,1)$};
\draw[hl] (1.3,-0.4) -- (2,1) -- (2.7,2.4);
\draw[->] (2,1) -- (2.8,0.6) node[lab, below right] {$\nabla w$};
\node[lab, right] at (1.4,-1.4) {slice $y=1$};
\end{tikzpicture}
\end{center}
```

The slice $y=1$ of the surface $x^2+y^2-z^2=4$ is the hyperbola $x^2-z^2=3$. At $(2,1,1)$ the gradient $\langle4,2,-2\rangle$ has $xz$-part $\langle4,-2\rangle$, normal to the slice, and the tangent plane $4x+2y-2z=8$ meets the slice in the tangent line $z=2x-3$ (thick).

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

::: {#fig-gradient-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[emph] (0.8,0) circle (0.8);
\draw[->, hl] (0,0) -- (1.6,0) node[lab, right] {$\nabla f$};
\fill[ink] (0,0) circle[pt] node[lab, left] {$P$};
\draw[->] (0,0) -- (0.92,0.77) node[lab, above] {$\hat{\mathbf u}$};
\fill[ink] (0.94,0.79) circle[pt];
\draw[->] (0,0) -- (-0.6,1.04);
\fill[ink] (0.4,-0.69) circle[pt];
\draw[faint] (0.35,0) arc[start angle=0, end angle=40, radius=0.35];
\node[lab, right] at (0.45,0.17) {$\theta$};
\end{tikzpicture}
\end{center}
```

$D_{\hat{\mathbf u}}f=\nabla f\cdot\hat{\mathbf u}=\lvert\nabla f\rvert\cos\theta$. Marking $D_{\hat{\mathbf u}}f$ along each direction traces the thick circle through $P$: largest ($\lvert\nabla f\rvert$) along $\nabla f$, zero perpendicular to it (along the level curve), negative in the backward half.

:::

::: {#exm-directional-derivative .example name="A directional derivative"}

$w=x^2+y^2+1$ at $(1,1)$: $\nabla w=\langle2,2\rangle$. In the direction $\hat{\mathbf{u}}=\langle\frac35,\frac45\rangle$ the rate is $\frac65+\frac85=\frac{14}5$; the largest rate is $\lvert\nabla w\rvert=2\sqrt2\approx2.83$, in the direction $\langle1,1\rangle/\sqrt2$.

:::
