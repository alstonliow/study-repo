---
title: "Velocity, Acceleration and Kepler's Second Law"
sources: [mit1802-5, mit1802-6, mit1802n-K]
requires: [math/calculus/multivariable/vectors/lines-and-planes, math/calculus/single-variable/applications-of-integrals/parametric-curves-and-arclength]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lectures 5-6 and Supplementary Notes K, in our own wording. Numbers checked in Python. -->

A moving point is described by its **position vector** $\mathbf{r}(t)=\langle x(t),y(t),z(t)\rangle$, a vector-valued function of time (@def-parametric-curve in the plane). A good way to find $\mathbf{r}(t)$ is to write it as a sum of simpler vectors whose lengths and directions are known.

::: {#exm-cycloid .example name="The cycloid"}

A wheel of radius $a$ rolls along the $x$-axis; $P$ is a point on the rim, at the origin at the start. Let $\theta$ be the angle the wheel has turned, $A$ the contact point and $B$ the centre. Rolling without slipping means $OA$ equals the arc $a\theta$, so
$$\overrightarrow{OP}=\overrightarrow{OA}+\overrightarrow{AB}+\overrightarrow{BP}
=\langle a\theta,0\rangle+\langle0,a\rangle+\langle-a\sin\theta,-a\cos\theta\rangle
=\langle a(\theta-\sin\theta),\ a(1-\cos\theta)\rangle .$$
Near $\theta=0$, Taylor's formula gives $x\approx a\theta^3/6$ and $y\approx a\theta^2/2$, so $y/x\approx3/\theta\to\infty$: the cycloid has a cusp with a vertical tangent where it touches the floor.

:::

::: {#fig-vector-valued-functions-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.75]
\draw[->, faint] (-0.3,0) -- (13.2,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.3) -- (0,2.6) node[lab, above] {$y$};
\draw[emph, domain=0:12.566, samples=120] plot ({\x-sin(\x r)},{1-cos(\x r)});
\draw[faint] (2.2,1) circle (1);
\draw[->, hl] (0,0) -- (2.2,0) node[lab, midway, below] {$a\theta$};
\draw[->, hl] (2.2,0) -- (2.2,1);
\draw[->, hl] (2.2,1) -- (1.39,1.59);
\fill (1.39,1.59) circle (1.5pt) node[lab, left] {$P$};
\node[lab, below right] at (2.2,0) {$A$};
\node[lab, right] at (2.2,1) {$B$};
\end{tikzpicture}
\end{center}
```

Two arches of the cycloid ($a=1$) and the wheel after turning $\theta=2.2$: $\overrightarrow{OP}=\overrightarrow{OA}+\overrightarrow{AB}+\overrightarrow{BP}$. The curve has cusps on the axis.

:::

::: {#def-velocity-acceleration .definition name="Velocity, speed, acceleration"}

For a moving point $\mathbf{r}(t)$:
$$\mathbf{v}=\frac{d\mathbf{r}}{dt}=\Big\langle\frac{dx}{dt},\frac{dy}{dt},\frac{dz}{dt}\Big\rangle,\qquad
\text{speed}=\lvert\mathbf{v}\rvert,\qquad \mathbf{a}=\frac{d\mathbf{v}}{dt}.$$
If $s$ is arclength along the path, $ds/dt=\lvert\mathbf{v}\rvert$, and the unit tangent vector is $\hat{\mathbf{T}}=\mathbf{v}/\lvert\mathbf{v}\rvert$, so
$$\mathbf{v}=\frac{d\mathbf{r}}{dt}=\hat{\mathbf{T}}\,\frac{ds}{dt}.$$

:::

::: {#fig-vector-valued-functions-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[emph] (0,0) circle (1.4);
\fill[ink] (0,0) circle[pt];
\fill[ink] (1.16,0.79) circle[pt];
\draw[->, hl] (1.16,0.79) -- (0.76,1.37);
\draw[->] (1.16,0.79) -- (0.64,0.43);
\fill[ink] (-0.93,1.04) circle[pt];
\draw[->, hl] (-0.93,1.04) -- (-1.45,0.58);
\draw[->] (-0.93,1.04) -- (-0.51,0.57);
\fill[ink] (-0.69,-1.22) circle[pt];
\draw[->, hl] (-0.69,-1.22) -- (-0.08,-1.56);
\draw[->] (-0.69,-1.22) -- (-0.38,-0.67);
\node[lab, above] at (0.56,1.54) {$\mathbf v$};
\node[lab] at (0.5,0.18) {$\mathbf a$};
\end{tikzpicture}
\end{center}
```

Uniform circular motion: the velocity $\mathbf v$ (thick) is tangent to the circle and the acceleration $\mathbf a$ points to the centre. Constant speed does not mean zero acceleration, because the direction of $\mathbf v$ changes.

:::

The speed is $\lvert d\mathbf{r}/dt\rvert$, which is not the same as $d\lvert\mathbf{r}\rvert/dt$: a point moving round a circle centred at the origin has $\lvert\mathbf{r}\rvert$ constant but non-zero speed.

::: {#exm-cycloid-velocity .example name="Velocity on the cycloid"}

With $a=1$ and $t=\theta$: $\mathbf{v}=\langle1-\cos t,\sin t\rangle$, speed $\sqrt{2-2\cos t}=2\lvert\sin(t/2)\rvert$, $\mathbf{a}=\langle\sin t,\cos t\rangle$. At $t=0$ the point is at rest ($\mathbf{v}=\mathbf{0}$) but $\mathbf{a}=\langle0,1\rangle$ points straight up; at $t=\pi$ the speed is largest, $\mathbf{v}=\langle2,0\rangle$. One arch has length $\int_0^{2\pi}2\sin(t/2)\,dt=8$.

:::

::: {#prp-vector-product-rules .proposition name="Product rules for vector functions"}

For differentiable vector functions $\mathbf{a}(t),\mathbf{b}(t)$ and scalar $f(t)$,
$$\frac{d}{dt}(f\mathbf{a})=f'\mathbf{a}+f\mathbf{a}',\qquad
\frac{d}{dt}(\mathbf{a}\cdot\mathbf{b})=\mathbf{a}'\cdot\mathbf{b}+\mathbf{a}\cdot\mathbf{b}',\qquad
\frac{d}{dt}(\mathbf{a}\times\mathbf{b})=\mathbf{a}'\times\mathbf{b}+\mathbf{a}\times\mathbf{b}' ,$$
keeping the order of the factors in the cross product.

:::

::: {.proof}

1. Each component of $\mathbf{a}\cdot\mathbf{b}$ or $\mathbf{a}\times\mathbf{b}$ is a sum of products $\pm a_ib_j$ of components.

2. Differentiate each product by the one-variable product rule (@thm-derivative-product-rule): $(a_ib_j)'=a_i'b_j+a_ib_j'$.

3. Collecting the terms with $a_i'$ gives $\mathbf{a}'\cdot\mathbf{b}$ (or $\mathbf{a}'\times\mathbf{b}$), and the terms with $b_j'$ give $\mathbf{a}\cdot\mathbf{b}'$ (or $\mathbf{a}\times\mathbf{b}'$).

:::

::: {#cor-constant-length .corollary name="Constant length"}

If $\lvert\mathbf{r}(t)\rvert$ is constant then $\mathbf{r}\cdot\mathbf{v}=0$: the velocity is perpendicular to the position vector.

:::

::: {.proof}

1. $\mathbf{r}\cdot\mathbf{r}=\lvert\mathbf{r}\rvert^2$ is constant, so its derivative $2\,\mathbf{r}\cdot\mathbf{r}'$ is $0$.

:::

::: {#thm-kepler-second-law .theorem name="Kepler's second law and central forces"}

Let a planet move with position $\mathbf{r}(t)$ relative to the sun. The line from the sun to the planet sweeps out area at a constant rate, in a fixed plane through the sun, if and only if $\mathbf{r}\times\mathbf{v}$ is constant, if and only if the acceleration (hence the force) is parallel to $\mathbf{r}$ (a **central** force).

:::

::: {.proof}

1. In a short time $\Delta t$ the swept region is nearly the triangle with sides $\mathbf{r}$ and $\Delta\mathbf{r}\approx\mathbf{v}\Delta t$, of area $\tfrac12\lvert\mathbf{r}\times\Delta\mathbf{r}\rvert$. Hence the rate of sweeping area is $\tfrac12\lvert\mathbf{r}\times\mathbf{v}\rvert$.

2. The vector $\mathbf{r}\times\mathbf{v}$ is perpendicular to the plane spanned by $\mathbf{r}$ and $\mathbf{v}$. Motion in a fixed plane with constant rate of area is therefore the statement that $\mathbf{r}\times\mathbf{v}$ has constant direction and constant length, i.e. is a constant vector.

3. By @prp-vector-product-rules, $\dfrac{d}{dt}(\mathbf{r}\times\mathbf{v})=\mathbf{v}\times\mathbf{v}+\mathbf{r}\times\mathbf{a}=\mathbf{r}\times\mathbf{a}$.

4. So $\mathbf{r}\times\mathbf{v}$ is constant exactly when $\mathbf{r}\times\mathbf{a}=\mathbf{0}$, i.e. when $\mathbf{a}$ is parallel to $\mathbf{r}$.

:::

::: {#fig-vector-valued-functions-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[emph] (2,0) -- (1.99,0.11) -- (1.97,0.23) -- (1.93,0.34) -- (1.88,0.44) -- (1.81,0.55) -- (1.73,0.65) -- (1.64,0.75) -- (1.53,0.84) -- (1.41,0.92) -- (1.29,1) -- (1.15,1.06) -- (1,1.13) -- (0.85,1.18) -- (0.68,1.22) -- (0.52,1.26) -- (0.35,1.28) -- (0.17,1.3) -- (0,1.3) -- (-0.17,1.3) -- (-0.35,1.28) -- (-0.52,1.26) -- (-0.68,1.22) -- (-0.85,1.18) -- (-1,1.13) -- (-1.15,1.06) -- (-1.29,1) -- (-1.41,0.92) -- (-1.53,0.84) -- (-1.64,0.75) -- (-1.73,0.65) -- (-1.81,0.55) -- (-1.88,0.44) -- (-1.93,0.34) -- (-1.97,0.23) -- (-1.99,0.11) -- (-2,0) -- (-1.99,-0.11) -- (-1.97,-0.23) -- (-1.93,-0.34) -- (-1.88,-0.44) -- (-1.81,-0.55) -- (-1.73,-0.65) -- (-1.64,-0.75) -- (-1.53,-0.84) -- (-1.41,-0.92) -- (-1.29,-1) -- (-1.15,-1.06) -- (-1,-1.13) -- (-0.85,-1.18) -- (-0.68,-1.22) -- (-0.52,-1.26) -- (-0.35,-1.28) -- (-0.17,-1.3) -- (0,-1.3) -- (0.17,-1.3) -- (0.35,-1.28) -- (0.52,-1.26) -- (0.68,-1.22) -- (0.85,-1.18) -- (1,-1.13) -- (1.15,-1.06) -- (1.29,-1) -- (1.41,-0.92) -- (1.53,-0.84) -- (1.64,-0.75) -- (1.73,-0.65) -- (1.81,-0.55) -- (1.88,-0.44) -- (1.93,-0.34) -- (1.97,-0.23) -- (1.99,-0.11) -- cycle;
\fill[ink] (1.52,0) circle[pt] node[lab, below] {sun};
\fill[tintB] (1.52,0) -- (1.41,-0.92) -- (1.48,-0.87) -- (1.56,-0.81) -- (1.64,-0.75) -- (1.71,-0.67) -- (1.79,-0.59) -- (1.85,-0.49) -- (1.91,-0.38) -- (1.96,-0.26) -- (1.99,-0.13) -- (2,0) -- (1.99,0.13) -- (1.96,0.26) -- (1.91,0.38) -- (1.85,0.49) -- (1.79,0.59) -- (1.71,0.67) -- (1.64,0.75) -- (1.56,0.81) -- (1.48,0.87) -- (1.41,0.92) -- cycle;
\draw[hl] (1.52,0) -- (1.41,-0.92) -- (1.48,-0.87) -- (1.56,-0.81) -- (1.64,-0.75) -- (1.71,-0.67) -- (1.79,-0.59) -- (1.85,-0.49) -- (1.91,-0.38) -- (1.96,-0.26) -- (1.99,-0.13) -- (2,0) -- (1.99,0.13) -- (1.96,0.26) -- (1.91,0.38) -- (1.85,0.49) -- (1.79,0.59) -- (1.71,0.67) -- (1.64,0.75) -- (1.56,0.81) -- (1.48,0.87) -- (1.41,0.92) -- cycle;
\fill[tintB] (1.52,0) -- (-1.98,0.18) -- (-1.98,0.17) -- (-1.99,0.15) -- (-1.99,0.13) -- (-1.99,0.11) -- (-1.99,0.09) -- (-2,0.07) -- (-2,0.06) -- (-2,0.04) -- (-2,0.02) -- (-2,0) -- (-2,-0.02) -- (-2,-0.04) -- (-2,-0.06) -- (-2,-0.07) -- (-1.99,-0.09) -- (-1.99,-0.11) -- (-1.99,-0.13) -- (-1.99,-0.15) -- (-1.98,-0.17) -- (-1.98,-0.18) -- cycle;
\draw[hl] (1.52,0) -- (-1.98,0.18) -- (-1.98,0.17) -- (-1.99,0.15) -- (-1.99,0.13) -- (-1.99,0.11) -- (-1.99,0.09) -- (-2,0.07) -- (-2,0.06) -- (-2,0.04) -- (-2,0.02) -- (-2,0) -- (-2,-0.02) -- (-2,-0.04) -- (-2,-0.06) -- (-2,-0.07) -- (-1.99,-0.09) -- (-1.99,-0.11) -- (-1.99,-0.13) -- (-1.99,-0.15) -- (-1.98,-0.17) -- (-1.98,-0.18) -- cycle;
\end{tikzpicture}
\end{center}
```

Kepler's second law: the line from the sun to the planet sweeps out equal areas in equal times. Both shaded sectors take the same time; near the sun the planet moves faster, so its sector is short and wide.

:::

::: {#rmk-vector-valued-functions-1 .remark name="Why this matters"}

Kepler found the law from observations; Newton explained it, since gravity pulls towards the sun. The proof shows the law holds for any central force, for example the attraction between two electric charges.

:::
