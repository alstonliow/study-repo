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

::: {#rmk-triple-integrals-1 .remark name="Symmetry"}

Mass, centre of mass and moments of inertia of solids are defined as for plates (@def-mass-centroid-moment) with $dV$ in place of $dA$. Symmetry often gives some coordinates of the centre of mass at once: in @exm-between-paraboloids, $\bar x=\bar y=0$.

:::
