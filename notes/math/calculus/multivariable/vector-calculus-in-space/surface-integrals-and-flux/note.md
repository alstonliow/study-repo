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
