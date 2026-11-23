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

::: {#fig-stokes-theorem-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (0,-1.5) -- (0,1.8) node[lab, above] {$z$};
\draw[hl] (0,-1.4) -- (0,1.6);
\draw[emph] (0,0.2) ellipse (1.2 and 0.4);
\draw[->, emph] (1.2,0.2) arc[start angle=0, end angle=-70, x radius=1.2, y radius=0.4];
\node[lab, right] at (1.25,0) {loop};
\node[lab, right] at (0.1,1.45) {removed};
\end{tikzpicture}
\end{center}
```

Space with the $z$-axis removed is not simply connected: a loop around the axis cannot be shrunk to a point without crossing it. There a curl-free field, such as the vortex field $\frac{-y\,\mathbf i+x\,\mathbf j}{x^2+y^2}$, can have nonzero work around the loop.

:::

::: {#thm-div-curl-zero .theorem name="The divergence of a curl is zero"}

If $\mathbf{F}$ has continuous second partial derivatives, then $\nabla\cdot(\nabla\times\mathbf{F})=0$.

:::

::: {.proof}

1. $\nabla\cdot\langle R_y-Q_z,P_z-R_x,Q_x-P_y\rangle=R_{yx}-Q_{zx}+P_{zy}-R_{xy}+Q_{xz}-P_{yz}$.

2. By @thm-symmetry-mixed-partials the terms cancel in pairs. (Symbolically: $\nabla\cdot(\nabla\times\mathbf{F})=0$ like $\mathbf{u}\cdot(\mathbf{u}\times\mathbf{v})=0$.)

:::

::: {#rmk-stokes-theorem-1 .remark name="Two surfaces with the same boundary"}

If $S_1$ and $S_2$ both have boundary $C$, Stokes gives them the same flux of $\nabla\times\mathbf{F}$. This can be seen directly: with $S_2$ reversed, $S_1$ and $S_2$ together form a closed surface bounding a solid $D$, and the divergence theorem gives the difference of the fluxes as $\iiint_D\nabla\cdot(\nabla\times\mathbf{F})\,dV=0$. Stokes' theorem needs a two-sided surface: a Möbius strip has only one side, and no flux can be defined through it.

:::

::: {#fig-stokes-theorem-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.5]
\draw[hl] (-0.5,-0.32) -- (-0.39,-0.32) -- (-0.28,-0.31) -- (-0.17,-0.3) -- (-0.05,-0.29) -- (0.07,-0.28) -- (0.18,-0.26) -- (0.3,-0.24) -- (0.41,-0.21) -- (0.52,-0.19) -- (0.62,-0.16) -- (0.71,-0.13) -- (0.8,-0.1) -- (0.87,-0.07) -- (0.94,-0.03) -- (1,0) -- (1.05,0.03) -- (1.08,0.07) -- (1.11,0.1) -- (1.12,0.13) -- (1.12,0.16) -- (1.1,0.19) -- (1.08,0.21) -- (1.04,0.24) -- (0.99,0.26) -- (0.93,0.28) -- (0.86,0.29) -- (0.78,0.3) -- (0.7,0.31) -- (0.6,0.32) -- (0.5,0.32) -- (0.39,0.32) -- (0.28,0.31) -- (0.17,0.3) -- (0.05,0.29) -- (-0.07,0.28) -- (-0.18,0.26) -- (-0.3,0.24) -- (-0.41,0.21) -- (-0.52,0.19) -- (-0.62,0.16) -- (-0.71,0.13) -- (-0.8,0.1) -- (-0.87,0.07) -- (-0.94,0.03) -- (-1,0) -- (-1.05,-0.03) -- (-1.08,-0.07) -- (-1.11,-0.1) -- (-1.12,-0.13) -- (-1.12,-0.16) -- (-1.1,-0.19) -- (-1.08,-0.21) -- (-1.04,-0.24) -- (-0.99,-0.26) -- (-0.93,-0.28) -- (-0.86,-0.29) -- (-0.78,-0.3) -- (-0.7,-0.31) -- (-0.6,-0.32) -- (-0.5,-0.32);
\draw[faint] (0.5,0.32) -- (0.47,0.43) -- (0.43,0.53) -- (0.4,0.62) -- (0.36,0.71) -- (0.33,0.78) -- (0.29,0.84) -- (0.26,0.9) -- (0.22,0.94) -- (0.19,0.98) -- (0.16,1) -- (0.12,1.02) -- (0.09,1.03) -- (0.05,1.02) -- (0.02,1.01) -- (-0.02,0.99) -- (-0.05,0.96) -- (-0.09,0.92) -- (-0.12,0.86) -- (-0.16,0.8) -- (-0.19,0.73) -- (-0.22,0.66) -- (-0.26,0.57) -- (-0.29,0.47) -- (-0.33,0.36) -- (-0.36,0.24) -- (-0.4,0.12) -- (-0.43,-0.02) -- (-0.47,-0.16) -- (-0.5,-0.32);
\draw[faint] (-0.35,0.23) -- (-0.33,0.34) -- (-0.3,0.45) -- (-0.28,0.55) -- (-0.26,0.64) -- (-0.23,0.72) -- (-0.21,0.79) -- (-0.18,0.85) -- (-0.16,0.9) -- (-0.13,0.94) -- (-0.11,0.97) -- (-0.09,1) -- (-0.06,1.01) -- (-0.04,1.01) -- (-0.01,1.01) -- (0.01,0.99) -- (0.04,0.97) -- (0.06,0.93) -- (0.09,0.89) -- (0.11,0.83) -- (0.13,0.77) -- (0.16,0.7) -- (0.18,0.62) -- (0.21,0.52) -- (0.23,0.42) -- (0.26,0.31) -- (0.28,0.19) -- (0.3,0.06) -- (0.33,-0.08) -- (0.35,-0.23);
\draw[faint] (-1,0) -- (-0.93,0.13) -- (-0.86,0.26) -- (-0.79,0.37) -- (-0.72,0.48) -- (-0.66,0.57) -- (-0.59,0.66) -- (-0.52,0.73) -- (-0.45,0.8) -- (-0.38,0.86) -- (-0.31,0.9) -- (-0.24,0.94) -- (-0.17,0.97) -- (-0.1,0.99) -- (-0.03,1) -- (0.03,1) -- (0.1,0.99) -- (0.17,0.97) -- (0.24,0.94) -- (0.31,0.9) -- (0.38,0.86) -- (0.45,0.8) -- (0.52,0.73) -- (0.59,0.66) -- (0.66,0.57) -- (0.72,0.48) -- (0.79,0.37) -- (0.86,0.26) -- (0.93,0.13) -- (1,0);
\draw[faint] (-1.06,-0.23) -- (-0.99,-0.08) -- (-0.91,0.06) -- (-0.84,0.19) -- (-0.77,0.31) -- (-0.69,0.42) -- (-0.62,0.52) -- (-0.55,0.62) -- (-0.48,0.7) -- (-0.4,0.77) -- (-0.33,0.83) -- (-0.26,0.89) -- (-0.18,0.93) -- (-0.11,0.97) -- (-0.04,0.99) -- (0.04,1.01) -- (0.11,1.01) -- (0.18,1.01) -- (0.26,1) -- (0.33,0.97) -- (0.4,0.94) -- (0.48,0.9) -- (0.55,0.85) -- (0.62,0.79) -- (0.69,0.72) -- (0.77,0.64) -- (0.84,0.55) -- (0.91,0.45) -- (0.99,0.34) -- (1.06,0.23);
\draw[faint] (-0.5,-0.32) -- (-0.47,-0.16) -- (-0.43,-0.02) -- (-0.4,0.12) -- (-0.36,0.24) -- (-0.33,0.36) -- (-0.29,0.47) -- (-0.26,0.57) -- (-0.22,0.66) -- (-0.19,0.73) -- (-0.16,0.8) -- (-0.12,0.86) -- (-0.09,0.92) -- (-0.05,0.96) -- (-0.02,0.99) -- (0.02,1.01) -- (0.05,1.02) -- (0.09,1.03) -- (0.12,1.02) -- (0.16,1) -- (0.19,0.98) -- (0.22,0.94) -- (0.26,0.9) -- (0.29,0.84) -- (0.33,0.78) -- (0.36,0.71) -- (0.4,0.62) -- (0.43,0.53) -- (0.47,0.43) -- (0.5,0.32);
\draw[faint] (-0.39,0.15) -- (-0.3,0.15) -- (-0.22,0.16) -- (-0.13,0.16) -- (-0.04,0.17) -- (0.05,0.19) -- (0.14,0.2) -- (0.23,0.22) -- (0.32,0.23) -- (0.4,0.25) -- (0.48,0.28) -- (0.55,0.3) -- (0.62,0.32) -- (0.68,0.35) -- (0.73,0.37) -- (0.77,0.4) -- (0.81,0.43) -- (0.84,0.45) -- (0.86,0.48) -- (0.87,0.5) -- (0.86,0.52) -- (0.85,0.55) -- (0.83,0.57) -- (0.81,0.58) -- (0.77,0.6) -- (0.72,0.61) -- (0.67,0.63) -- (0.61,0.64) -- (0.54,0.64) -- (0.47,0.65) -- (0.39,0.65) -- (0.3,0.65) -- (0.22,0.64) -- (0.13,0.64) -- (0.04,0.63) -- (-0.05,0.61) -- (-0.14,0.6) -- (-0.23,0.58) -- (-0.32,0.57) -- (-0.4,0.55) -- (-0.48,0.52) -- (-0.55,0.5) -- (-0.62,0.48) -- (-0.68,0.45) -- (-0.73,0.43) -- (-0.77,0.4) -- (-0.81,0.37) -- (-0.84,0.35) -- (-0.86,0.32) -- (-0.87,0.3) -- (-0.86,0.28) -- (-0.85,0.25) -- (-0.83,0.23) -- (-0.81,0.22) -- (-0.77,0.2) -- (-0.72,0.19) -- (-0.67,0.17) -- (-0.61,0.16) -- (-0.54,0.16) -- (-0.47,0.15) -- (-0.39,0.15);
\draw[faint] (-0.25,0.59) -- (-0.2,0.59) -- (-0.14,0.59) -- (-0.08,0.6) -- (-0.03,0.6) -- (0.03,0.61) -- (0.09,0.62) -- (0.15,0.63) -- (0.2,0.64) -- (0.26,0.66) -- (0.31,0.67) -- (0.36,0.68) -- (0.4,0.7) -- (0.44,0.72) -- (0.47,0.73) -- (0.5,0.75) -- (0.52,0.77) -- (0.54,0.78) -- (0.55,0.8) -- (0.56,0.82) -- (0.56,0.83) -- (0.55,0.84) -- (0.54,0.86) -- (0.52,0.87) -- (0.5,0.88) -- (0.47,0.89) -- (0.43,0.9) -- (0.39,0.9) -- (0.35,0.91) -- (0.3,0.91) -- (0.25,0.91) -- (0.2,0.91) -- (0.14,0.91) -- (0.08,0.9) -- (0.03,0.9) -- (-0.03,0.89) -- (-0.09,0.88) -- (-0.15,0.87) -- (-0.2,0.86) -- (-0.26,0.84) -- (-0.31,0.83) -- (-0.36,0.82) -- (-0.4,0.8) -- (-0.44,0.78) -- (-0.47,0.77) -- (-0.5,0.75) -- (-0.52,0.73) -- (-0.54,0.72) -- (-0.55,0.7) -- (-0.56,0.68) -- (-0.56,0.67) -- (-0.55,0.66) -- (-0.54,0.64) -- (-0.52,0.63) -- (-0.5,0.62) -- (-0.47,0.61) -- (-0.43,0.6) -- (-0.39,0.6) -- (-0.35,0.59) -- (-0.3,0.59) -- (-0.25,0.59);
\fill[tintA] (-0.5,-0.32) -- (-0.39,-0.32) -- (-0.28,-0.31) -- (-0.17,-0.3) -- (-0.05,-0.29) -- (0.07,-0.28) -- (0.18,-0.26) -- (0.3,-0.24) -- (0.41,-0.21) -- (0.52,-0.19) -- (0.62,-0.16) -- (0.71,-0.13) -- (0.8,-0.1) -- (0.87,-0.07) -- (0.94,-0.03) -- (1,0) -- (1.05,0.03) -- (1.08,0.07) -- (1.11,0.1) -- (1.12,0.13) -- (1.12,0.16) -- (1.1,0.19) -- (1.08,0.21) -- (1.04,0.24) -- (0.99,0.26) -- (0.93,0.28) -- (0.86,0.29) -- (0.78,0.3) -- (0.7,0.31) -- (0.6,0.32) -- (0.5,0.32) -- (0.39,0.32) -- (0.28,0.31) -- (0.17,0.3) -- (0.05,0.29) -- (-0.07,0.28) -- (-0.18,0.26) -- (-0.3,0.24) -- (-0.41,0.21) -- (-0.52,0.19) -- (-0.62,0.16) -- (-0.71,0.13) -- (-0.8,0.1) -- (-0.87,0.07) -- (-0.94,0.03) -- (-1,0) -- (-1.05,-0.03) -- (-1.08,-0.07) -- (-1.11,-0.1) -- (-1.12,-0.13) -- (-1.12,-0.16) -- (-1.1,-0.19) -- (-1.08,-0.21) -- (-1.04,-0.24) -- (-0.99,-0.26) -- (-0.93,-0.28) -- (-0.86,-0.29) -- (-0.78,-0.3) -- (-0.7,-0.31) -- (-0.6,-0.32) -- (-0.5,-0.32) -- cycle;
\draw[->, hl] (-0.45,-0.32) -- (-0.38,-0.32);
\node[lab, right] at (1.1,0) {$C$};
\node[lab, above] at (0,1.05) {$S$};
\end{tikzpicture}
\end{center}
```

Two surfaces with the same boundary circle $C$: the flat disk (shaded) and the paraboloid $z=1-x^2-y^2$ above it. By Stokes' theorem the flux of $\nabla\times\mathbf F$ is the same through both, $\oint_C\mathbf F\cdot d\mathbf r$.

:::
