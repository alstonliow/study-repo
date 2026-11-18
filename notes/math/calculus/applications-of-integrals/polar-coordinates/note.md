---
title: "Polar Coordinates and Area"
sources: [mit1801-32]
requires: [math/calculus/applications-of-integrals/parametric-curves-and-arclength]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lecture 32, in our own wording. Numbers checked in Python. -->

::: {#def-polar-coordinates .definition name="Polar coordinates"}

A point $(x,y)$ has polar coordinates $(r,\theta)$ with
$$x=r\cos\theta,\qquad y=r\sin\theta,\qquad r=\sqrt{x^2+y^2},\qquad \tan\theta=\frac yx .$$
$\theta$ is determined only up to multiples of $2\pi$; we also allow $r<0$, meaning the point $(\lvert r\rvert,\theta+\pi)$.

:::

::: {#exm-polar-point .example name="Converting a point"}

$(1,-1)$ has $r=\sqrt2$ and $\theta=-\pi/4$ (or $7\pi/4$). Note $\tan\theta=-1$ also holds for $\theta=3\pi/4$, which is the opposite point $(-1,1)$: choose the angle from the quadrant.

:::

::: {#exm-polar-circle .example name="A circle through the origin"}

The circle of radius $a$ centred at $(a,0)$ is $(x-a)^2+y^2=a^2$, i.e. $x^2+y^2=2ax$, i.e. $r^2=2ar\cos\theta$, i.e. $r=2a\cos\theta$ for $-\pi/2\le\theta\le\pi/2$.

:::

::: {#prp-polar-area .proposition name="Area in polar coordinates"}

The region $0\le r\le f(\theta)$, $\alpha\le\theta\le\beta$ has area
$$A=\int_\alpha^\beta\tfrac12f(\theta)^2\,d\theta .$$

:::

A thin sector of angle $\Delta\theta$ and radius $r$ is nearly a triangle of area $\tfrac12r^2\Delta\theta$; the integral adds the sectors.

::: {#exm-polar-area-circle .example name="Area of the circle again"}

For $r=2a\cos\theta$: $A=\int_{-\pi/2}^{\pi/2}\tfrac12\cdot4a^2\cos^2\theta\,d\theta=2a^2\cdot\tfrac\pi2=\pi a^2$, as it should be.

:::

::: {#exm-polar-to-cartesian .example name="Back to $x$ and $y$"}

$r=\dfrac1{2\cos\theta+3\sin\theta}$ means $2r\cos\theta+3r\sin\theta=1$, i.e. the line $2x+3y=1$.

:::
