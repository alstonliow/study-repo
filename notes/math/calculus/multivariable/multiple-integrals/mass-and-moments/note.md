---
title: "Mass, Centre of Mass and Moment of Inertia"
sources: [mit1802-17, mit1802-25]
requires: [math/calculus/multivariable/multiple-integrals/polar-double-integrals, math/calculus/single-variable/applications-of-integrals/average-value-and-work]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lecture 17 (plane regions) and Lecture 25 (solids), in our own wording. Numbers checked in Python (sympy). -->

A flat plate occupying the region $R$ has **density** $\delta(x,y)=\lim\Delta m/\Delta A$ (mass per unit area; constant for a uniform material).

::: {#def-mass-centroid-moment .definition name="Mass, centre of mass, moment of inertia"}

For a plate $R$ with density $\delta$:
$$\text{area}=\iint_R1\,dA,\qquad M=\iint_R\delta\,dA,\qquad
\bar x=\frac1M\iint_Rx\,\delta\,dA,\qquad\bar y=\frac1M\iint_Ry\,\delta\,dA .$$
$(\bar x,\bar y)$ is the **centre of mass** (the **centroid** when $\delta$ is constant). The **moment of inertia** about an axis is
$$I=\iint_R(\text{distance to the axis})^2\,\delta\,dA;$$
in particular $I_x=\iint y^2\delta\,dA$, $I_y=\iint x^2\delta\,dA$, and about the origin (the axis perpendicular to the plane) $I_0=\iint(x^2+y^2)\delta\,dA$.

For a solid $D$ in space the same formulas hold with $dV$ and triple integrals (@sec-math-calculus-multivariable-multiple-integrals-triple-integrals); there $I_z=\iiint(x^2+y^2)\delta\,dV$, $I_x=\iiint(y^2+z^2)\delta\,dV$, $I_y=\iiint(x^2+z^2)\delta\,dV$.

:::

The average value of $f$ over $R$ is $\bar f=\frac1{\text{area}}\iint_Rf\,dA$; the centre of mass is the weighted average of the position, with weight $\delta$.

::: {#rmk-mass-and-moments-1 .remark name="Why moment of inertia"}

A mass $m$ turning at angular speed $\omega$ at distance $r$ from the axis has speed $r\omega$ and kinetic energy $\frac12mr^2\omega^2$. Summing over a body gives $\frac12I\omega^2$: the moment of inertia plays for rotation the part that mass plays for translation (how hard it is to set the body turning).

:::

::: {#exm-moment-disk-centre .example name="A disk about its centre"}

A uniform disk ($\delta=1$) of radius $a$: $I_0=\displaystyle\int_0^{2\pi}\!\!\int_0^ar^2\cdot r\,dr\,d\theta=2\pi\frac{a^4}4=\frac{\pi a^4}2$.

:::

::: {#exm-moment-disk-edge .example name="A disk about a point of its rim"}

Put the origin on the rim and the diameter along the $x$-axis; the circle is $r=2a\cos\theta$, $-\pi/2\le\theta\le\pi/2$ (@exm-polar-circle). Then
$$I_0=\int_{-\pi/2}^{\pi/2}\!\!\int_0^{2a\cos\theta}r^3\,dr\,d\theta=\int_{-\pi/2}^{\pi/2}4a^4\cos^4\theta\,d\theta=4a^4\cdot\frac{3\pi}8=\frac{3\pi a^4}2 .$$
This is $\frac{\pi a^4}2+\pi a^2\cdot a^2$: the moment about the centre plus mass times distance squared.

:::

::: {#exm-centroid-half-disk .example name="Centroid of a half disk"}

The upper half of the unit disk, $\delta=1$: $M=\frac\pi2$, $\bar x=0$ by symmetry, and $\iint y\,dA=\int_0^\pi\!\int_0^1r\sin\theta\cdot r\,dr\,d\theta=\frac13\cdot2=\frac23$, so $\bar y=\dfrac{2/3}{\pi/2}=\dfrac4{3\pi}\approx0.42$.

:::

::: {#fig-mass-and-moments-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.4]
\fill[tintA] (2,0) arc[start angle=0, end angle=180, radius=2] -- cycle;
\draw[emph, primary] (2,0) arc[start angle=0, end angle=180, radius=2] -- cycle;
\draw[->] (-2.4,0) -- (2.5,0) node[lab, right] {$x$};
\draw[->] (0,-0.2) -- (0,2.4) node[lab, above] {$y$};
\node[tick, below] at (2,0) {$1$}; \node[tick, below] at (-2,0) {$-1$};
\node[hl dot] at (0,0.849) {};
\node[lab, right] at (0.1,0.849) {$(\bar x,\bar y)=\big(0,\tfrac4{3\pi}\big)$};
\end{tikzpicture}
\end{center}
```

The centroid of the upper half disk (@exm-centroid-half-disk) lies on the axis of symmetry, at height $4/(3\pi)\approx0.42$: below the middle height $\frac12$, because more of the area lies near the diameter.

:::
