---
title: "Stokes' Theorem"
sources: [mit1802-31, mit1802-32, mit1802n-V13, mit1802n-V14]
requires: [math/calculus/multivariable/vector-calculus-in-space/line-integrals-in-space, math/calculus/multivariable/line-integrals/simply-connected-regions]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lectures 31-32 and Supplementary Notes V13, V14, in our own wording. Numbers checked in Python (sympy). -->

Stokes' theorem is the analogue in space of Green's theorem for work, as the divergence theorem is the analogue of Green's theorem for flux.

::: {#fig-stokes-theorem-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (-2,0) arc (180:360:2 and 0.6) .. controls (2,2) and (-2,2) .. (-2,0);
\draw[emph] (-2,0) .. controls (-2,2) and (2,2) .. (2,0);
\draw[emph] (0,0) ellipse (2 and 0.6); \draw[->, emph] (-0.1,-0.6) -- (0.1,-0.6);
\draw[->, hl] (0,1.5) -- (0,2.4) node[lab, above] {$\hat{\mathbf n}$};
\node[lab] at (0.6,1) {$S$}; \node[lab] at (2.2,-0.4) {$C$};
\end{tikzpicture}
\end{center}
```

Compatible orientation: with $\hat{\mathbf n}$ pointing up, walking along $C$ in the arrow direction keeps $S$ on the left (right-hand rule).

:::

::: {#def-compatible-orientation .definition name="Compatible orientations"}

Let $S$ be a two-sided surface with boundary curve $C$. An orientation of $C$ and a unit normal $\hat{\mathbf{n}}$ of $S$ are **compatible** if, walking along $C$ in its direction with the body along $\hat{\mathbf{n}}$, the surface $S$ is on the left. (Right-hand rule: thumb along $C$, index finger pointing into $S$, then the middle finger points along $\hat{\mathbf{n}}$.)

:::

::: {#thm-stokes .theorem name="Stokes' theorem"}

If $C$ is a closed curve, $S$ any two-sided surface with boundary $C$, compatibly oriented, and $\mathbf{F}$ has continuous partial derivatives on $S$, then
$$\oint_C\mathbf{F}\cdot d\mathbf{r}=\iint_S(\nabla\times\mathbf{F})\cdot\hat{\mathbf{n}}\,dS .$$

:::

::: {.proof}

1. (Sketch.) If $S$ is a region of the $xy$-plane with $\hat{\mathbf{n}}=\mathbf{k}$, then $(\nabla\times\mathbf{F})\cdot\mathbf{k}=Q_x-P_y$ and $dz=0$ on $C$, so the statement is Green's theorem (@thm-greens-theorem).

2. If $S$ lies in any plane, choose coordinates $u,v,w$ adapted to the plane ($w$ along the normal). Work, flux and curl can be defined geometrically, without coordinates, so their formulas are the same in the new coordinates, and step 1 applies.

3. A general $S$ is cut into small pieces, each nearly flat. For each piece the circulation around its boundary nearly equals the flux of the curl through it. Adding up, the line integrals over the internal edges cancel (each is traversed twice in opposite directions), leaving $\oint_C$; the fluxes add up to the flux through $S$.

:::

The surface is any surface with boundary $C$: for a circle, a disk, a hemisphere or a cone all give the same flux of the curl.

::: {#exm-stokes-paraboloid .example name="Checking on a paraboloid"}

$\mathbf{F}=\langle z,x,y\rangle$, $C$ the unit circle in the $xy$-plane counterclockwise, $S$ the part of $z=1-x^2-y^2$ above it, normal up.

- Directly: on $C$, $z=0$ and $dz=0$, so $\oint_Cx\,dy=\int_0^{2\pi}\cos^2\theta\,d\theta=\pi$.
- By Stokes: $\nabla\times\mathbf{F}=\langle1,1,1\rangle$ and $\hat{\mathbf{n}}\,dS=\langle2x,2y,1\rangle\,dx\,dy$, so the flux is $\iint_{x^2+y^2\le1}(2x+2y+1)\,dx\,dy=\pi$ (the $x$ and $y$ terms vanish by symmetry).

:::

::: {#def-simply-connected-space .definition name="Simply connected region in space"}

A region $D$ of space is **simply connected** if every closed curve in $D$ is the boundary of some two-sided surface lying in $D$.

:::

All of space and space without one point are simply connected; space without the $z$-axis is not (a loop around the axis bounds no surface avoiding it). The sphere is simply connected and the torus is not; this is how topology proves they are different surfaces.

::: {#thm-curl-free-conservative .theorem name="Curl-free fields are conservative"}

If $\nabla\times\mathbf{F}=\mathbf{0}$ in a simply connected region $D$, then $\mathbf{F}$ is conservative in $D$, hence a gradient field there.

:::

::: {.proof}

1. Let $C_1,C_2$ be curves in $D$ with the same endpoints. The closed curve $C=C_1-C_2$ bounds a surface $S$ in $D$, because $D$ is simply connected.

2. By Stokes' theorem $\int_{C_1}\mathbf{F}\cdot d\mathbf{r}-\int_{C_2}\mathbf{F}\cdot d\mathbf{r}=\oint_C\mathbf{F}\cdot d\mathbf{r}=\iint_S\mathbf{0}\cdot\hat{\mathbf{n}}\,dS=0$.

3. So $\mathbf{F}$ is path independent, and by the argument of @thm-conservative-equivalences it has a potential.

:::

::: {#thm-div-curl-zero .theorem name="The divergence of a curl is zero"}

If $\mathbf{F}$ has continuous second partial derivatives, then $\nabla\cdot(\nabla\times\mathbf{F})=0$.

:::

::: {.proof}

1. $\nabla\cdot\langle R_y-Q_z,P_z-R_x,Q_x-P_y\rangle=R_{yx}-Q_{zx}+P_{zy}-R_{xy}+Q_{xz}-P_{yz}$.

2. By @thm-mixed-partials the terms cancel in pairs. (Symbolically: $\nabla\cdot(\nabla\times\mathbf{F})=0$ like $\mathbf{u}\cdot(\mathbf{u}\times\mathbf{v})=0$.)

:::

::: {#rmk-stokes-theorem-1 .remark name="Two surfaces with the same boundary"}

If $S_1$ and $S_2$ both have boundary $C$, Stokes gives them the same flux of $\nabla\times\mathbf{F}$. This can be seen directly: with $S_2$ reversed, $S_1$ and $S_2$ together form a closed surface bounding a solid $D$, and the divergence theorem gives the difference of the fluxes as $\iiint_D\nabla\cdot(\nabla\times\mathbf{F})\,dV=0$. Stokes' theorem needs a two-sided surface: a Möbius strip has only one side, and no flux can be defined through it.

:::
