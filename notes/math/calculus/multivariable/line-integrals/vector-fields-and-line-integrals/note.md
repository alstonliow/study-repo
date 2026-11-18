---
title: "Vector Fields and Line Integrals in the Plane"
sources: [mit1802-19, mit1802-20, mit1802n-V1]
requires: [math/calculus/multivariable/vectors/vector-valued-functions, math/calculus/multivariable/differentiation/gradient]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lectures 19-20 and Supplementary Notes V1, in our own wording. Numbers checked in Python (sympy). -->

::: {#def-vector-field-plane .definition name="Vector field in the plane"}

A **vector field** assigns to each point $(x,y)$ of a region a vector
$$\mathbf{F}=M(x,y)\,\mathbf{i}+N(x,y)\,\mathbf{j}=\langle M,N\rangle .$$
It is continuous, differentiable, etc. when $M$ and $N$ are.

:::

Velocity fields of a fluid (wind maps) and force fields (gravity) are examples; so is the gradient $\nabla f$ of any function.

::: {#exm-plane-vector-fields .example name="Four fields"}

- $\mathbf{F}=2\mathbf{i}+\mathbf{j}$: the same vector everywhere.
- $\mathbf{F}=x\,\mathbf{i}$: horizontal, pointing away from the $y$-axis, growing with $\lvert x\rvert$.
- $\mathbf{F}=x\,\mathbf{i}+y\,\mathbf{j}$: points radially outwards, of length $r$.
- $\mathbf{F}=-y\,\mathbf{i}+x\,\mathbf{j}$: $\langle x,y\rangle$ turned $90^\circ$ counterclockwise; it circles the origin counterclockwise, of length $r$.

:::

::: {#fig-vector-fields-and-line-integrals-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.9]
\draw[->, faint] (-2.4,0) -- (2.6,0) node[lab, right] {$x$};
\draw[->, faint] (0,-2.4) -- (0,2.6) node[lab, above] {$y$};
\draw[->, hl] (-1.9,-1.9) -- (-1.482,-2.318);
\draw[->, hl] (-1.9,-0.95) -- (-1.691,-1.368);
\draw[->, hl] (-1.9,0.0) -- (-1.900,-0.418);
\draw[->, hl] (-1.9,0.95) -- (-2.109,0.532);
\draw[->, hl] (-1.9,1.9) -- (-2.318,1.482);
\draw[->, hl] (-0.95,-1.9) -- (-0.532,-2.109);
\draw[->, hl] (-0.95,-0.95) -- (-0.741,-1.159);
\draw[->, hl] (-0.95,0.0) -- (-0.950,-0.209);
\draw[->, hl] (-0.95,0.95) -- (-1.159,0.741);
\draw[->, hl] (-0.95,1.9) -- (-1.368,1.691);
\draw[->, hl] (0.0,-1.9) -- (0.418,-1.900);
\draw[->, hl] (0.0,-0.95) -- (0.209,-0.950);
\draw[->, hl] (0.0,0.95) -- (-0.209,0.950);
\draw[->, hl] (0.0,1.9) -- (-0.418,1.900);
\draw[->, hl] (0.95,-1.9) -- (1.368,-1.691);
\draw[->, hl] (0.95,-0.95) -- (1.159,-0.741);
\draw[->, hl] (0.95,0.0) -- (0.950,0.209);
\draw[->, hl] (0.95,0.95) -- (0.741,1.159);
\draw[->, hl] (0.95,1.9) -- (0.532,2.109);
\draw[->, hl] (1.9,-1.9) -- (2.318,-1.482);
\draw[->, hl] (1.9,-0.95) -- (2.109,-0.532);
\draw[->, hl] (1.9,0.0) -- (1.900,0.418);
\draw[->, hl] (1.9,0.95) -- (1.691,1.368);
\draw[->, hl] (1.9,1.9) -- (1.482,2.318);
\draw[emph] (0,0) circle (1.9);
\end{tikzpicture}
\end{center}
```

The field $-y\,\mathbf{i}+x\,\mathbf{j}$ (arrows scaled down): it circles the origin counterclockwise, tangent to every circle centred there, with length $r$.

:::

::: {#def-line-integral-work .definition name="Line integral (work)"}

Let $C$ be a curve traversed from $P_0$ to $P_1$. The **work** of $\mathbf{F}$ along $C$ is the limit of the sums of $\mathbf{F}\cdot\Delta\mathbf{r}_i$ over small displacements along $C$:
$$W=\int_C\mathbf{F}\cdot d\mathbf{r}=\lim\sum_i\mathbf{F}\cdot\Delta\mathbf{r}_i .$$
If $\mathbf{r}(t)$, $t_0\le t\le t_1$, parametrises $C$ in this direction,
$$\int_C\mathbf{F}\cdot d\mathbf{r}=\int_{t_0}^{t_1}\mathbf{F}(\mathbf{r}(t))\cdot\frac{d\mathbf{r}}{dt}\,dt .$$

:::

::: {#prp-line-integral-forms .proposition name="Three ways to write the line integral"}

$$\int_C\mathbf{F}\cdot d\mathbf{r}=\int_CM\,dx+N\,dy=\int_C\mathbf{F}\cdot\hat{\mathbf{T}}\,ds .$$
The value does not depend on the parametrisation of $C$, only on its direction: reversing the direction changes the sign.

:::

::: {.proof}

1. $d\mathbf{r}=\langle dx,dy\rangle$, so $\mathbf{F}\cdot d\mathbf{r}=M\,dx+N\,dy$; with a parameter, $dx=x'(t)\,dt$ and $dy=y'(t)\,dt$.

2. $\dfrac{d\mathbf{r}}{dt}=\hat{\mathbf{T}}\dfrac{ds}{dt}$ (@def-velocity-acceleration), so $\mathbf{F}\cdot\dfrac{d\mathbf{r}}{dt}dt=\mathbf{F}\cdot\hat{\mathbf{T}}\,ds$.

3. If $t=t(u)$ is another parameter, increasing, then $\dfrac{d\mathbf{r}}{du}=\dfrac{d\mathbf{r}}{dt}\dfrac{dt}{du}$, and the substitution rule for one-variable integrals (@thm-substitution-definite) turns one integral into the other. If $t(u)$ is decreasing, the limits are exchanged and the sign changes.

:::

The notation $\int_CM\,dx+N\,dy$ is not a sum of an $x$-integral and a $y$-integral: to evaluate it, express $x$, $y$, $dx$, $dy$ in terms of one parameter along $C$.

::: {#exm-line-integral-parabola .example name="Along a parabola"}

$\mathbf{F}=-y\,\mathbf{i}+x\,\mathbf{j}$ on $C$: $x=t$, $y=t^2$, $0\le t\le1$. Then $dx=dt$, $dy=2t\,dt$ and
$$\int_C-y\,dx+x\,dy=\int_0^1(-t^2+2t^2)\,dt=\frac13 .$$
The parametrisation $x=\sin\theta$, $y=\sin^2\theta$, $0\le\theta\le\pi/2$ gives the same value.

:::

::: {#exm-line-integral-circle-geometric .example name="Around a circle, geometrically"}

$C$ the circle of radius $a$ about the origin, counterclockwise.

- $\mathbf{F}=x\,\mathbf{i}+y\,\mathbf{j}$ is perpendicular to $C$, so $\mathbf{F}\cdot\hat{\mathbf{T}}=0$ and the work is $0$.
- $\mathbf{F}=-y\,\mathbf{i}+x\,\mathbf{j}$ is tangent to $C$ with length $a$, so $\mathbf{F}\cdot\hat{\mathbf{T}}=a$ and the work is $a\cdot2\pi a=2\pi a^2$.

:::

::: {#exm-line-integral-sector .example name="Around a sector, piece by piece"}

$\oint_Cy\,dx+x\,dy$ around the boundary of the sector of the unit disk between angles $0$ and $\pi/4$, counterclockwise.

1. On the $x$-axis from $(0,0)$ to $(1,0)$: $y=0$, $dy=0$, contribution $0$.
2. On the arc $x=\cos\theta$, $y=\sin\theta$, $0\le\theta\le\pi/4$: $\int_0^{\pi/4}(-\sin^2\theta+\cos^2\theta)\,d\theta=\int_0^{\pi/4}\cos2\theta\,d\theta=\frac12$.
3. Back along $y=x$ to the origin: traverse it in the other direction, $x=y=t$, $0\le t\le\frac1{\sqrt2}$, which gives $\int2t\,dt=\frac12$, and change the sign: $-\frac12$.

Total: $0$. (The next note explains why.)

:::
