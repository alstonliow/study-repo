---
title: "Triple Integrals and Cylindrical Coordinates"
sources: [mit1802-25, mit1802n-I]
requires: [math/calculus/multivariable/multiple-integrals/mass-and-moments, math/calculus/multivariable/multiple-integrals/change-of-variables]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lecture 25 and Supplementary Notes I.3, in our own wording. Numbers checked in Python (sympy). -->

::: {#def-triple-integral .definition name="Triple integral"}

For a solid region $D$ and a function $f(x,y,z)$, the **triple integral** $\iiint_Df\,dV$ is the limit of the sums $\sum f(x_i,y_i,z_i)\,\Delta V_i$ over small pieces of $D$ of volumes $\Delta V_i$. $\iiint_D1\,dV$ is the volume of $D$.

:::

::: {#prp-triple-integral-limits .proposition name="Limits for $dz\,dy\,dx$"}

If $D$ lies between a lower surface $z=z_1(x,y)$ and an upper surface $z=z_2(x,y)$ over a plane region $R$ (the **shadow** of $D$ on the $xy$-plane), then
$$\iiint_Df\,dV=\iint_R\left(\int_{z_1(x,y)}^{z_2(x,y)}f\,dz\right)dA,$$
and the double integral over $R$ is set up as in @prp-setting-up-limits. The shadow is the set of $(x,y)$ where the upper surface is above the lower one.

:::

::: {#exm-between-paraboloids .example name="Between two paraboloids"}

The solid between $z=x^2+y^2$ and $z=4-x^2-y^2$. The upper surface is above the lower one when $4-x^2-y^2>x^2+y^2$, i.e. $x^2+y^2<2$: the shadow is the disk of radius $\sqrt2$. In rectangular coordinates
$$V=\int_{-\sqrt2}^{\sqrt2}\int_{-\sqrt{2-x^2}}^{\sqrt{2-x^2}}\int_{x^2+y^2}^{4-x^2-y^2}dz\,dy\,dx,$$
but polar coordinates in the shadow are easier: $V=\int_0^{2\pi}\!\int_0^{\sqrt2}(4-2r^2)\,r\,dr\,d\theta=2\pi\cdot2=4\pi$.

:::

::: {#fig-triple-integrals-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[y=0.6cm]
\draw[->, faint] (0,-0.3) -- (0,4.5) node[lab, above] {$z$};
\draw[->, faint] (-2.2,0) -- (2.4,0) node[lab, right] {$x$};
\fill[tintA] (-1.41,2) -- (-1.34,1.8) -- (-1.27,1.61) -- (-1.2,1.43) -- (-1.12,1.26) -- (-1.05,1.11) -- (-0.98,0.96) -- (-0.91,0.82) -- (-0.83,0.7) -- (-0.76,0.58) -- (-0.69,0.47) -- (-0.62,0.38) -- (-0.54,0.3) -- (-0.47,0.22) -- (-0.4,0.16) -- (-0.33,0.11) -- (-0.25,0.06) -- (-0.18,0.03) -- (-0.11,0.01) -- (-0.04,0) -- (0.04,0) -- (0.11,0.01) -- (0.18,0.03) -- (0.25,0.06) -- (0.33,0.11) -- (0.4,0.16) -- (0.47,0.22) -- (0.54,0.3) -- (0.62,0.38) -- (0.69,0.47) -- (0.76,0.58) -- (0.83,0.7) -- (0.91,0.82) -- (0.98,0.96) -- (1.05,1.11) -- (1.12,1.26) -- (1.2,1.43) -- (1.27,1.61) -- (1.34,1.8) -- (1.41,2) -- (1.41,2) -- (1.34,2.2) -- (1.27,2.39) -- (1.2,2.57) -- (1.12,2.74) -- (1.05,2.89) -- (0.98,3.04) -- (0.91,3.18) -- (0.83,3.3) -- (0.76,3.42) -- (0.69,3.53) -- (0.62,3.62) -- (0.54,3.7) -- (0.47,3.78) -- (0.4,3.84) -- (0.33,3.89) -- (0.25,3.94) -- (0.18,3.97) -- (0.11,3.99) -- (0.04,4) -- (-0.04,4) -- (-0.11,3.99) -- (-0.18,3.97) -- (-0.25,3.94) -- (-0.33,3.89) -- (-0.4,3.84) -- (-0.47,3.78) -- (-0.54,3.7) -- (-0.62,3.62) -- (-0.69,3.53) -- (-0.76,3.42) -- (-0.83,3.3) -- (-0.91,3.18) -- (-0.98,3.04) -- (-1.05,2.89) -- (-1.12,2.74) -- (-1.2,2.57) -- (-1.27,2.39) -- (-1.34,2.2) -- (-1.41,2) -- cycle;
\draw[emph] (-1.9,3.61) -- (-1.84,3.37) -- (-1.77,3.14) -- (-1.71,2.92) -- (-1.65,2.71) -- (-1.58,2.51) -- (-1.52,2.31) -- (-1.46,2.12) -- (-1.39,1.94) -- (-1.33,1.77) -- (-1.27,1.6) -- (-1.2,1.45) -- (-1.14,1.3) -- (-1.08,1.16) -- (-1.01,1.03) -- (-0.95,0.9) -- (-0.89,0.79) -- (-0.82,0.68) -- (-0.76,0.58) -- (-0.7,0.49) -- (-0.63,0.4) -- (-0.57,0.32) -- (-0.51,0.26) -- (-0.44,0.2) -- (-0.38,0.14) -- (-0.32,0.1) -- (-0.25,0.06) -- (-0.19,0.04) -- (-0.13,0.02) -- (-0.06,0) -- (0,0) -- (0.06,0) -- (0.13,0.02) -- (0.19,0.04) -- (0.25,0.06) -- (0.32,0.1) -- (0.38,0.14) -- (0.44,0.2) -- (0.51,0.26) -- (0.57,0.32) -- (0.63,0.4) -- (0.7,0.49) -- (0.76,0.58) -- (0.82,0.68) -- (0.89,0.79) -- (0.95,0.9) -- (1.01,1.03) -- (1.08,1.16) -- (1.14,1.3) -- (1.2,1.45) -- (1.27,1.6) -- (1.33,1.77) -- (1.39,1.94) -- (1.46,2.12) -- (1.52,2.31) -- (1.58,2.51) -- (1.65,2.71) -- (1.71,2.92) -- (1.77,3.14) -- (1.84,3.37) -- (1.9,3.61);
\draw[emph] (-1.9,0.39) -- (-1.84,0.63) -- (-1.77,0.86) -- (-1.71,1.08) -- (-1.65,1.29) -- (-1.58,1.49) -- (-1.52,1.69) -- (-1.46,1.88) -- (-1.39,2.06) -- (-1.33,2.23) -- (-1.27,2.4) -- (-1.2,2.55) -- (-1.14,2.7) -- (-1.08,2.84) -- (-1.01,2.97) -- (-0.95,3.1) -- (-0.89,3.21) -- (-0.82,3.32) -- (-0.76,3.42) -- (-0.7,3.51) -- (-0.63,3.6) -- (-0.57,3.68) -- (-0.51,3.74) -- (-0.44,3.8) -- (-0.38,3.86) -- (-0.32,3.9) -- (-0.25,3.94) -- (-0.19,3.96) -- (-0.13,3.98) -- (-0.06,4) -- (0,4) -- (0.06,4) -- (0.13,3.98) -- (0.19,3.96) -- (0.25,3.94) -- (0.32,3.9) -- (0.38,3.86) -- (0.44,3.8) -- (0.51,3.74) -- (0.57,3.68) -- (0.63,3.6) -- (0.7,3.51) -- (0.76,3.42) -- (0.82,3.32) -- (0.89,3.21) -- (0.95,3.1) -- (1.01,2.97) -- (1.08,2.84) -- (1.14,2.7) -- (1.2,2.55) -- (1.27,2.4) -- (1.33,2.23) -- (1.39,2.06) -- (1.46,1.88) -- (1.52,1.69) -- (1.58,1.49) -- (1.65,1.29) -- (1.71,1.08) -- (1.77,0.86) -- (1.84,0.63) -- (1.9,0.39);
\draw[hl] (-1.41,0) -- (1.41,0);
\draw[faint, dashed] (-1.41,0) -- (-1.41,2) (1.41,0) -- (1.41,2);
\node[lab, right] at (1.9,3.61) {$z=x^2+y^2$};
\node[lab, right] at (1.9,0.39) {$z=4-x^2-y^2$};
\node[lab, below] at (0,-0.3) {shadow $r\le\sqrt2$};
\end{tikzpicture}
\end{center}
```

Cross-section $y=0$ of the solid between $z=x^2+y^2$ and $z=4-x^2-y^2$ (shaded). The surfaces meet where $x^2+y^2=2$, so the shadow in the $xy$-plane is the disk of radius $\sqrt2$ (thick).

:::

::: {#def-cylindrical-coordinates .definition name="Cylindrical coordinates"}

**Cylindrical coordinates** $(r,\theta,z)$ are polar coordinates in the $xy$-plane together with $z$: $x=r\cos\theta$, $y=r\sin\theta$. $r=a$ is the cylinder of radius $a$ about the $z$-axis; $\theta=\theta_0$ is a vertical half-plane. The volume element is
$$dV=r\,dr\,d\theta\,dz,$$
since a small box with base area $\Delta A=r\,\Delta r\,\Delta\theta$ and height $\Delta z$ has volume $\Delta A\,\Delta z$.

:::

::: {#fig-triple-integrals-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x={(-0.45cm,-0.35cm)}, y={(1cm,0cm)}, z={(0cm,1cm)}, scale=1.2]
\draw[->] (0,0,0) -- (2.6,0,0) node[lab, below left] {$x$};
\draw[->] (0,0,0) -- (0,3,0) node[lab, right] {$y$};
\draw[->] (0,0,0) -- (0,0,2.6) node[lab, above] {$z$};
\draw[faint, dashed] plot[domain=-20:110, samples=50] ({2.4*cos(\x)},{2.4*sin(\x)},0);
\draw[emph, primary] (0,0,0) -- node[lab, below right] {$r$} (1.377,1.966,0);
\draw[dashed] (1.377,1.966,0) -- node[lab, right] {$z$} (1.377,1.966,1.8);
\draw[faint] (0,0,1.8) -- (1.377,1.966,1.8);
\draw plot[domain=0:55, samples=20] ({0.7*cos(\x)},{0.7*sin(\x)},0);
\node[lab] at (1.0,0.5,0) {$\theta$};
\node[hl dot] at (1.377,1.966,1.8) {};
\node[lab, above right] at (1.377,1.966,1.8) {$(r,\theta,z)$};
\end{tikzpicture}
\end{center}
```

Cylindrical coordinates: polar coordinates $(r,\theta)$ of the point's shadow in the $xy$-plane, together with its height $z$.

:::

::: {#exm-cone-moment .example name="Moment of inertia of a cone"}

The solid cone between $z=ar$ and $z=b$ ($a,b>0$, $\delta=1$). For fixed $z$ the slice is the disk $r\le z/a$, and $0\le z\le b$:
$$I_z=\iiint r^2\,dV=\int_0^b\!\!\int_0^{2\pi}\!\!\int_0^{z/a}r^3\,dr\,d\theta\,dz=\int_0^b\frac{2\pi}4\frac{z^4}{a^4}dz=\frac{\pi b^5}{10a^4}.$$

:::

::: {#exm-sphere-cut-by-plane .example name="A ball cut by a slanted plane"}

The part of the unit ball above the plane $z=1-y$. For fixed $(x,y)$, $z$ runs from $1-y$ up to $\sqrt{1-x^2-y^2}$. The shadow is where $1-y<\sqrt{1-x^2-y^2}$, i.e. $x^2<2y-2y^2$ (which forces $0<y<1$):
$$V=\int_0^1\int_{-\sqrt{2y-2y^2}}^{\sqrt{2y-2y^2}}\int_{1-y}^{\sqrt{1-x^2-y^2}}dz\,dx\,dy .$$
This is hard to evaluate as it stands; @exm-ball-cap-spherical computes it after a rotation.

:::

::: {#fig-triple-integrals-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.8]
\draw[->, faint] (0,-1.2) -- (0,1.5) node[lab, above] {$z$};
\draw[->, faint] (-1.3,0) -- (1.5,0) node[lab, right] {$y$};
\draw[emph] (0,0) circle (1);
\fill[tintB] (0,1) -- (0,1) -- (0.05,1) -- (0.11,0.99) -- (0.16,0.99) -- (0.21,0.98) -- (0.27,0.96) -- (0.32,0.95) -- (0.37,0.93) -- (0.42,0.91) -- (0.47,0.88) -- (0.52,0.86) -- (0.56,0.83) -- (0.61,0.8) -- (0.65,0.76) -- (0.69,0.73) -- (0.73,0.69) -- (0.76,0.65) -- (0.8,0.61) -- (0.83,0.56) -- (0.86,0.52) -- (0.88,0.47) -- (0.91,0.42) -- (0.93,0.37) -- (0.95,0.32) -- (0.96,0.27) -- (0.98,0.21) -- (0.99,0.16) -- (0.99,0.11) -- (1,0.05) -- (1,0) -- cycle;
\draw[hl] (-0.3,1.3) -- (1.3,-0.3);
\node[lab, right] at (1.25,-0.25) {$z=1-y$};
\draw[faint, dashed] (0,0) -- (0.5,0.5);
\node[lab, right] at (0.25,0.32) {$\tfrac1{\sqrt2}$};
\end{tikzpicture}
\end{center}
```

The plane $z=1-y$ cuts off a cap of the unit ball (cross-section $x=0$, shaded). The plane is at distance $1/\sqrt2$ from the centre, which is why rotating it to a horizontal position gives the cap of @exm-ball-cap-spherical.

:::

::: {#rmk-triple-integrals-1 .remark name="Symmetry"}

Mass, centre of mass and moments of inertia of solids are defined as for plates (@def-mass-centroid-moment) with $dV$ in place of $dA$. Symmetry often gives some coordinates of the centre of mass at once: in @exm-between-paraboloids, $\bar x=\bar y=0$.

:::
