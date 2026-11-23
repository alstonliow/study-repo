---
title: "Vector Fields in Space, Surface Integrals and Flux"
sources: [mit1802-27, mit1802-28, mit1802n-V8, mit1802n-V9]
requires: [math/calculus/multivariable/multiple-integrals/spherical-coordinates, math/calculus/multivariable/line-integrals/flux-and-normal-form-of-greens-theorem]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lectures 27-28 and Supplementary Notes V8, V9, in our own wording. Numbers checked in Python (sympy). -->

A **vector field in space** is $\mathbf{F}=P\,\mathbf{i}+Q\,\mathbf{j}+R\,\mathbf{k}$ with $P,Q,R$ functions of $x,y,z$: force fields (gravity $-c\langle x,y,z\rangle/\rho^3$, electric and magnetic fields), velocity fields of fluids, gradient fields.

::: {#fig-surface-integrals-and-flux-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[emph] (0,0) circle (1.6); \draw[faint, dashed] (0,0) ellipse (1.6 and 0.45);
\foreach \a in {30,90,150,250,320} \draw[->, hl] (\a:1.6) -- (\a:2.4);
\node[lab] at (45:2.6) {$\hat{\mathbf n}$}; \node[lab] at (0.3,0.9) {$S$};
\end{tikzpicture}
\end{center}
```

On the sphere of radius $a$ the outward unit normal is $\hat{\mathbf n}=\langle x,y,z\rangle/a$; flux adds up $\mathbf F\cdot\hat{\mathbf n}\,dS$ over $S$.

:::

::: {#def-flux-surface .definition name="Flux through a surface"}

Let $S$ be a surface with a chosen unit normal $\hat{\mathbf{n}}$ (one of the two sides counts as positive). The **flux** of $\mathbf{F}$ through $S$ is the surface integral
$$\iint_S\mathbf{F}\cdot\hat{\mathbf{n}}\,dS=\iint_S\mathbf{F}\cdot d\mathbf{S},\qquad d\mathbf{S}=\hat{\mathbf{n}}\,dS .$$
For a closed surface the outward normal is the usual choice.

:::

As in the plane, if $\mathbf{F}$ is the velocity of a fluid, the fluid crossing a small piece $\Delta S$ in unit time fills a slanted box with base $\Delta S$ and edge $\mathbf{F}$, of volume $(\mathbf{F}\cdot\hat{\mathbf{n}})\Delta S$; the flux is the flow through $S$ per unit time.

::: {#prp-normal-and-surface-element .proposition name="Formulas for $\hat{\mathbf{n}}\,dS$"}

1. Horizontal plane $z=a$: $\hat{\mathbf{n}}=\pm\mathbf{k}$, $dS=dx\,dy$ (similarly for planes parallel to the other coordinate planes).
2. Sphere of radius $a$ about the origin, parameters $\phi,\theta$: $\hat{\mathbf{n}}=\pm\frac1a\langle x,y,z\rangle$, $dS=a^2\sin\phi\,d\phi\,d\theta$.
3. Cylinder of radius $a$ about the $z$-axis, parameters $z,\theta$: $\hat{\mathbf{n}}=\pm\frac1a\langle x,y,0\rangle$, $dS=a\,dz\,d\theta$.
4. Graph $z=f(x,y)$, parameters $x,y$: $\hat{\mathbf{n}}\,dS=\pm\langle-f_x,-f_y,1\rangle\,dx\,dy$, so $dS=\sqrt{1+f_x^2+f_y^2}\,dx\,dy$.
5. Parametric surface $\mathbf{r}(u,v)$: $\hat{\mathbf{n}}\,dS=\pm\Big(\dfrac{\partial\mathbf{r}}{\partial u}\times\dfrac{\partial\mathbf{r}}{\partial v}\Big)du\,dv$.
6. Surface with a known normal vector $\mathbf{N}$ (for a level surface $g=c$, $\mathbf{N}=\nabla g$): $\hat{\mathbf{n}}\,dS=\pm\dfrac{\mathbf{N}}{\mathbf{N}\cdot\mathbf{k}}\,dx\,dy$ and $dS=\dfrac{\lvert\mathbf{N}\rvert}{\lvert\mathbf{N}\cdot\mathbf{k}\rvert}dx\,dy$, wherever $\mathbf{N}\cdot\mathbf{k}\ne0$.

:::

::: {.proof}

1. Case 5 contains the others. A small piece of the surface with parameter ranges $\Delta u$, $\Delta v$ is nearly the parallelogram with sides $\mathbf{r}(u+\Delta u,v)-\mathbf{r}(u,v)\approx\mathbf{r}_u\Delta u$ and $\mathbf{r}_v\Delta v$. By @thm-cross-product-geometry, $(\mathbf{r}_u\times\mathbf{r}_v)\Delta u\Delta v$ is normal to it and has length equal to its area.

2. For a graph, $\mathbf{r}=\langle x,y,f(x,y)\rangle$, $\mathbf{r}_x=\langle1,0,f_x\rangle$, $\mathbf{r}_y=\langle0,1,f_y\rangle$, and $\mathbf{r}_x\times\mathbf{r}_y=\langle-f_x,-f_y,1\rangle$.

3. For a sphere, $\mathbf{r}=a\langle\sin\phi\cos\theta,\sin\phi\sin\theta,\cos\phi\rangle$ and $\mathbf{r}_\phi\times\mathbf{r}_\theta=a\sin\phi\,\mathbf{r}$, of length $a^2\sin\phi$, pointing outwards. For a cylinder, $\mathbf{r}=\langle a\cos\theta,a\sin\theta,z\rangle$ and $\lvert\mathbf{r}_z\times\mathbf{r}_\theta\rvert=a$.

4. For case 6, a piece $\Delta S$ of the surface projects onto the $xy$-plane with area $\Delta A=\lvert\cos\alpha\rvert\Delta S$, where $\alpha$ is the angle between $\hat{\mathbf{n}}$ and $\mathbf{k}$, and $\cos\alpha=\mathbf{N}\cdot\mathbf{k}/\lvert\mathbf{N}\rvert$. For a graph, $\mathbf{N}=\langle-f_x,-f_y,1\rangle$ and $\mathbf{N}\cdot\mathbf{k}=1$, which gives case 4 again.

:::

::: {#fig-surface-integrals-and-flux-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.5]
\draw[->, faint] (-0.2,0) -- (2.4,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.2) -- (0,1.8) node[lab, above] {$z$};
\draw[emph] (0,0.3) -- (0.03,0.3) -- (0.07,0.3) -- (0.1,0.3) -- (0.13,0.31) -- (0.17,0.31) -- (0.2,0.31) -- (0.23,0.32) -- (0.27,0.32) -- (0.3,0.33) -- (0.33,0.34) -- (0.37,0.35) -- (0.4,0.36) -- (0.43,0.37) -- (0.47,0.38) -- (0.5,0.39) -- (0.53,0.4) -- (0.57,0.41) -- (0.6,0.43) -- (0.63,0.44) -- (0.67,0.46) -- (0.7,0.47) -- (0.73,0.49) -- (0.77,0.51) -- (0.8,0.52) -- (0.83,0.54) -- (0.87,0.56) -- (0.9,0.58) -- (0.93,0.6) -- (0.97,0.63) -- (1,0.65) -- (1.03,0.67) -- (1.07,0.7) -- (1.1,0.72) -- (1.13,0.75) -- (1.17,0.78) -- (1.2,0.8) -- (1.23,0.83) -- (1.27,0.86) -- (1.3,0.89) -- (1.33,0.92) -- (1.37,0.95) -- (1.4,0.99) -- (1.43,1.02) -- (1.47,1.05) -- (1.5,1.09) -- (1.53,1.12) -- (1.57,1.16) -- (1.6,1.2) -- (1.63,1.23) -- (1.67,1.27) -- (1.7,1.31) -- (1.73,1.35) -- (1.77,1.39) -- (1.8,1.43) -- (1.83,1.48) -- (1.87,1.52) -- (1.9,1.56) -- (1.93,1.61) -- (1.97,1.65) -- (2,1.7);
\draw[hl] (0.95,0.59) -- (1.45,1.01) node[lab, above left] {$dS$};
\draw[hl] (0.95,0) -- (1.45,0) node[lab, below] {$dA$};
\draw[faint, dashed] (0.95,0) -- (0.95,0.59) (1.45,0) -- (1.45,1.01);
\draw[->] (1.2,0.8) -- (0.88,1.19) node[lab, left] {$\langle-f_x,-f_y,1\rangle$};
\end{tikzpicture}
\end{center}
```

Cross-section of a graph $z=f(x,y)$: a piece of surface $dS$ lies over a piece $dA$ of its shadow and is tilted, so it is larger. The upward normal $\langle-f_x,-f_y,1\rangle$ records both the tilt and the size: $\hat{\mathbf n}\,dS=\langle-f_x,-f_y,1\rangle\,dA$.

:::

The vector $\langle-f_x,-f_y,1\rangle$ is not $\hat{\mathbf{n}}$, and $dx\,dy$ is not $dS$: only their product is $\hat{\mathbf{n}}\,dS$.

::: {#exm-flux-sphere .example name="Two fluxes out of a sphere"}

$S$ the sphere of radius $a$, outward normal $\hat{\mathbf{n}}=\frac1a\langle x,y,z\rangle$.

- $\mathbf{F}=\langle x,y,z\rangle$: $\mathbf{F}\cdot\hat{\mathbf{n}}=\frac1a(x^2+y^2+z^2)=a$, so the flux is $a\cdot4\pi a^2=4\pi a^3$.
- $\mathbf{H}=z\,\mathbf{k}$: $\mathbf{H}\cdot\hat{\mathbf{n}}=z^2/a=a\cos^2\phi$, so the flux is $\int_0^{2\pi}\!\int_0^\pi a\cos^2\phi\cdot a^2\sin\phi\,d\phi\,d\theta=2\pi a^3\cdot\frac23=\frac43\pi a^3$.

:::

::: {#exm-flux-paraboloid .example name="Through a paraboloid"}

$\mathbf{F}=z\,\mathbf{k}$ through the part of $z=x^2+y^2$ above the unit disk, normal pointing up. $\hat{\mathbf{n}}\,dS=\langle-2x,-2y,1\rangle\,dx\,dy$, so
$$\iint_S\mathbf{F}\cdot d\mathbf{S}=\iint_{x^2+y^2\le1}z\,dx\,dy=\iint(x^2+y^2)\,dx\,dy=\int_0^{2\pi}\!\!\int_0^1r^3\,dr\,d\theta=\frac\pi2 .$$

:::

::: {#fig-surface-integrals-and-flux-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.5]
\draw[->, faint] (0,0) -- (-0.8,-0.51) node[lab, below left] {$x$};
\draw[->, faint] (0,0) -- (1.6,0) node[lab, right] {$y$};
\draw[->, faint] (0,0) -- (0,1.6) node[lab, above] {$z$};
\draw[faint] (0.5,1.32) -- (0.47,1.16) -- (0.43,1.02) -- (0.4,0.88) -- (0.36,0.76) -- (0.33,0.64) -- (0.29,0.53) -- (0.26,0.43) -- (0.22,0.34) -- (0.19,0.27) -- (0.16,0.2) -- (0.12,0.14) -- (0.09,0.08) -- (0.05,0.04) -- (0.02,0.01) -- (-0.02,-0.01) -- (-0.05,-0.02) -- (-0.09,-0.03) -- (-0.12,-0.02) -- (-0.16,-0) -- (-0.19,0.02) -- (-0.22,0.06) -- (-0.26,0.1) -- (-0.29,0.16) -- (-0.33,0.22) -- (-0.36,0.29) -- (-0.4,0.38) -- (-0.43,0.47) -- (-0.47,0.57) -- (-0.5,0.68);
\draw[faint] (-0.35,1.23) -- (-0.33,1.08) -- (-0.3,0.94) -- (-0.28,0.81) -- (-0.26,0.69) -- (-0.23,0.58) -- (-0.21,0.48) -- (-0.18,0.38) -- (-0.16,0.3) -- (-0.13,0.23) -- (-0.11,0.17) -- (-0.09,0.11) -- (-0.06,0.07) -- (-0.04,0.03) -- (-0.01,0.01) -- (0.01,-0.01) -- (0.04,-0.01) -- (0.06,-0.01) -- (0.09,0) -- (0.11,0.03) -- (0.13,0.06) -- (0.16,0.1) -- (0.18,0.15) -- (0.21,0.21) -- (0.23,0.28) -- (0.26,0.36) -- (0.28,0.45) -- (0.3,0.55) -- (0.33,0.66) -- (0.35,0.77);
\draw[faint] (-1,1) -- (-0.93,0.87) -- (-0.86,0.74) -- (-0.79,0.63) -- (-0.72,0.52) -- (-0.66,0.43) -- (-0.59,0.34) -- (-0.52,0.27) -- (-0.45,0.2) -- (-0.38,0.14) -- (-0.31,0.1) -- (-0.24,0.06) -- (-0.17,0.03) -- (-0.1,0.01) -- (-0.03,0) -- (0.03,0) -- (0.1,0.01) -- (0.17,0.03) -- (0.24,0.06) -- (0.31,0.1) -- (0.38,0.14) -- (0.45,0.2) -- (0.52,0.27) -- (0.59,0.34) -- (0.66,0.43) -- (0.72,0.52) -- (0.79,0.63) -- (0.86,0.74) -- (0.93,0.87) -- (1,1);
\draw[faint] (-1.06,0.77) -- (-0.99,0.66) -- (-0.91,0.55) -- (-0.84,0.45) -- (-0.77,0.36) -- (-0.69,0.28) -- (-0.62,0.21) -- (-0.55,0.15) -- (-0.48,0.1) -- (-0.4,0.06) -- (-0.33,0.03) -- (-0.26,0) -- (-0.18,-0.01) -- (-0.11,-0.01) -- (-0.04,-0.01) -- (0.04,0.01) -- (0.11,0.03) -- (0.18,0.07) -- (0.26,0.11) -- (0.33,0.17) -- (0.4,0.23) -- (0.48,0.3) -- (0.55,0.38) -- (0.62,0.48) -- (0.69,0.58) -- (0.77,0.69) -- (0.84,0.81) -- (0.91,0.94) -- (0.99,1.08) -- (1.06,1.23);
\draw[faint] (-0.5,0.68) -- (-0.47,0.57) -- (-0.43,0.47) -- (-0.4,0.38) -- (-0.36,0.29) -- (-0.33,0.22) -- (-0.29,0.16) -- (-0.26,0.1) -- (-0.22,0.06) -- (-0.19,0.02) -- (-0.16,-0) -- (-0.12,-0.02) -- (-0.09,-0.03) -- (-0.05,-0.02) -- (-0.02,-0.01) -- (0.02,0.01) -- (0.05,0.04) -- (0.09,0.08) -- (0.12,0.14) -- (0.16,0.2) -- (0.19,0.27) -- (0.22,0.34) -- (0.26,0.43) -- (0.29,0.53) -- (0.33,0.64) -- (0.36,0.76) -- (0.4,0.88) -- (0.43,1.02) -- (0.47,1.16) -- (0.5,1.32);
\draw[emph] (-0.5,0.68) -- (-0.39,0.68) -- (-0.28,0.69) -- (-0.17,0.7) -- (-0.05,0.71) -- (0.07,0.72) -- (0.18,0.74) -- (0.3,0.76) -- (0.41,0.79) -- (0.52,0.81) -- (0.62,0.84) -- (0.71,0.87) -- (0.8,0.9) -- (0.87,0.93) -- (0.94,0.97) -- (1,1) -- (1.05,1.03) -- (1.08,1.07) -- (1.11,1.1) -- (1.12,1.13) -- (1.12,1.16) -- (1.1,1.19) -- (1.08,1.21) -- (1.04,1.24) -- (0.99,1.26) -- (0.93,1.28) -- (0.86,1.29) -- (0.78,1.3) -- (0.7,1.31) -- (0.6,1.32) -- (0.5,1.32) -- (0.39,1.32) -- (0.28,1.31) -- (0.17,1.3) -- (0.05,1.29) -- (-0.07,1.28) -- (-0.18,1.26) -- (-0.3,1.24) -- (-0.41,1.21) -- (-0.52,1.19) -- (-0.62,1.16) -- (-0.71,1.13) -- (-0.8,1.1) -- (-0.87,1.07) -- (-0.94,1.03) -- (-1,1) -- (-1.05,0.97) -- (-1.08,0.93) -- (-1.11,0.9) -- (-1.12,0.87) -- (-1.12,0.84) -- (-1.1,0.81) -- (-1.08,0.79) -- (-1.04,0.76) -- (-0.99,0.74) -- (-0.93,0.72) -- (-0.86,0.71) -- (-0.78,0.7) -- (-0.7,0.69) -- (-0.6,0.68) -- (-0.5,0.68);
\draw[->, hl] (-0.25,0.09) -- (-0.09,0.51);
\draw[->, hl] (0.6,0.36) -- (0.25,0.65);
\draw[->, hl] (0,0.64) -- (0,0.81);
\draw[->, hl] (-0.85,0.48) -- (-0.43,0.78);
\node[lab, right] at (1.05,1) {$z=x^2+y^2$};
\end{tikzpicture}
\end{center}
```

The paraboloid $z=x^2+y^2$ over the unit disk with upward normals $\propto\langle-2x,-2y,1\rangle$ (thick arrows). The flux of $z\,\mathbf k$ only sees the vertical part, which is why it reduces to $\iint(x^2+y^2)\,dx\,dy$.

:::
