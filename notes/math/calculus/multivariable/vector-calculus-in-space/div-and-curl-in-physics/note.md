---
title: "Div and Curl in Physics: Maxwell's Equations"
sources: [mit1802-33, mit1802n-V15]
requires: [math/calculus/multivariable/vector-calculus-in-space/stokes-theorem]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lecture 33 and Supplementary Notes V15, in our own wording. -->

::: {#prp-curl-of-force .proposition name="Curl of a force field"}

Suppose a force field acts on a solid body with force $\mathbf{F}\,\Delta m$ on each small mass $\Delta m$. Just as $\text{force}/\text{mass}$ is the rate of change of velocity, $\text{torque}/\text{moment of inertia}$ is the rate of change of angular velocity, and
$$\operatorname{curl}\Big(\frac{\text{force}}{\text{mass}}\Big)=2\,\frac{\text{torque}}{\text{moment of inertia}} .$$
In particular a gradient field, whose curl is $\mathbf{0}$, exerts no torque on a small body: by itself, gravity does not change the rotation of the Earth.

:::

This combines @exm-curl-rotation (curl is twice angular velocity) with the torque $\mathbf{r}\times\mathbf{F}$ of the force about the origin; we do not prove it here. (The Earth is not rigid, and tidal friction does affect rotations; this is why the Moon always shows the same face.)

::: {#def-maxwell-equations .definition name="Maxwell's equations"}

For the electric field $\mathbf{E}$, the magnetic field $\mathbf{B}$, the charge density $\rho$ and the current density $\mathbf{J}$, with physical constants $\varepsilon_0,\mu_0$:
$$\nabla\cdot\mathbf{E}=\frac{\rho}{\varepsilon_0},\qquad\nabla\times\mathbf{E}=-\frac{\partial\mathbf{B}}{\partial t},\qquad\nabla\cdot\mathbf{B}=0,\qquad\nabla\times\mathbf{B}=\mu_0\mathbf{J}+\varepsilon_0\mu_0\frac{\partial\mathbf{E}}{\partial t}.$$
(Here $\rho$ is a density, not the spherical coordinate.)

:::

::: {#prp-gauss-law .proposition name="Gauss's law"}

For a closed surface $S$ enclosing the solid $D$, the flux of $\mathbf{E}$ out of $S$ is $Q/\varepsilon_0$, where $Q=\iiint_D\rho\,dV$ is the total charge inside.

:::

::: {.proof}

1. By the divergence theorem (@thm-divergence-theorem), $\iint_S\mathbf{E}\cdot\hat{\mathbf{n}}\,dS=\iiint_D\nabla\cdot\mathbf{E}\,dV=\iiint_D\frac{\rho}{\varepsilon_0}dV=\frac Q{\varepsilon_0}$.

:::

::: {#fig-div-and-curl-in-physics-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.1]
\fill[tintA] plot[smooth cycle] coordinates {(-2,0) (-1.2,1.3) (0.6,1.5) (2.1,0.6) (1.7,-1.1) (-0.3,-1.4)};
\draw[emph, primary] plot[smooth cycle] coordinates {(-2,0) (-1.2,1.3) (0.6,1.5) (2.1,0.6) (1.7,-1.1) (-0.3,-1.4)};
\foreach \a in {0,45,...,315} \draw[->, accent] (\a:0.25) -- (\a:1.05);
\node[hl dot] at (0,0) {};
\node[lab] at (0.42,-0.18) {$q$};
\draw[->, emph] (2.07,0.62) -- (2.75,0.95) node[lab, right] {$\hat{\mathbf n}$};
\draw[->, emph] (-1.2,1.3) -- (-1.65,1.85) node[lab, above] {$\hat{\mathbf n}$};
\node[lab, primary] at (1.6,-1.5) {$S$};
\node[lab, accent] at (0.75,0.3) {$\mathbf E$};
\end{tikzpicture}
\end{center}
```

Gauss's law (@prp-gauss-law): the flux of the electric field $\mathbf E$ out of a closed surface $S$ depends only on the charge enclosed by $S$, not on the shape of $S$.

:::

::: {#prp-faraday-law .proposition name="Faraday's law of induction"}

For a closed curve $C$ bounding a surface $S$, compatibly oriented,
$$\oint_C\mathbf{E}\cdot d\mathbf{r}=-\frac{d}{dt}\iint_S\mathbf{B}\cdot\hat{\mathbf{n}}\,dS .$$

:::

::: {.proof}

1. By Stokes' theorem (@thm-stokes), $\oint_C\mathbf{E}\cdot d\mathbf{r}=\iint_S(\nabla\times\mathbf{E})\cdot\hat{\mathbf{n}}\,dS=-\iint_S\frac{\partial\mathbf{B}}{\partial t}\cdot\hat{\mathbf{n}}\,dS$.

2. For a fixed surface the time derivative can be taken outside the integral.

:::

So a changing magnetic field makes $\mathbf{E}$ non-conservative: a voltage appears around a closed loop of wire. Transformers work this way: an alternating current in one coil makes an alternating magnetic field, whose changing flux through a second coil produces the output voltage.
