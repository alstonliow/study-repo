---
title: "Spherical Coordinates"
sources: [mit1802-26, mit1802n-I, mit1802n-CV]
requires: [math/calculus/multivariable/multiple-integrals/triple-integrals]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lecture 26 and Supplementary Notes I.4, CV.4, in our own wording. Numbers checked in Python (sympy). -->

::: {#def-spherical-coordinates .definition name="Spherical coordinates"}

**Spherical coordinates** $(\rho,\phi,\theta)$: $\rho\ge0$ is the distance to the origin, $\phi\in[0,\pi]$ the angle down from the positive $z$-axis, $\theta$ the same angle as in cylindrical coordinates. Then
$$z=\rho\cos\phi,\quad r=\rho\sin\phi,\qquad x=\rho\sin\phi\cos\theta,\quad y=\rho\sin\phi\sin\theta,\qquad \rho=\sqrt{x^2+y^2+z^2}.$$

:::

$\rho=a$ is the sphere of radius $a$ about the origin; on it, $\phi$ is like latitude measured from the north pole ($0$ at the north pole, $\pi/2$ on the equator) and $\theta$ like longitude. $\phi=\pi/4$ is the cone $z=r$, and $\phi=\pi/2$ is the $xy$-plane.

::: {#thm-spherical-volume-element .theorem name="Surface and volume elements"}

On the sphere $\rho=a$ the area element is $dS=a^2\sin\phi\,d\phi\,d\theta$, and in space
$$dV=\rho^2\sin\phi\,d\rho\,d\phi\,d\theta .$$

:::

::: {.proof}

1. On the sphere of radius $a$, the small region $\Delta\phi$ by $\Delta\theta$ is nearly a rectangle. One side is an arc of a great circle of radius $a$, of length $a\Delta\phi$; the other is an arc of the horizontal circle of radius $r=a\sin\phi$, of length $a\sin\phi\,\Delta\theta$. So $\Delta S\approx a^2\sin\phi\,\Delta\phi\Delta\theta$.

2. A small box between the spheres of radii $\rho$ and $\rho+\Delta\rho$ has volume $\Delta V\approx\Delta S\,\Delta\rho=\rho^2\sin\phi\,\Delta\rho\,\Delta\phi\,\Delta\theta$.

3. Check with the Jacobian (@def-jacobian): $\dfrac{\partial(x,y,z)}{\partial(\rho,\phi,\theta)}=\rho^2\sin\phi$.

:::

::: {#exm-ball-volume-spherical .example name="Volume of a ball"}

$\displaystyle\int_0^{2\pi}\!\!\int_0^\pi\!\!\int_0^a\rho^2\sin\phi\,d\rho\,d\phi\,d\theta=2\pi\cdot2\cdot\frac{a^3}3=\frac43\pi a^3$. The surface area of the sphere is $\int_0^{2\pi}\!\int_0^\pi a^2\sin\phi\,d\phi\,d\theta=4\pi a^2$.

:::

::: {#exm-ball-cap-spherical .example name="A cap of the unit ball"}

Rotating @exm-sphere-cut-by-plane about the $x$-axis, the plane becomes horizontal at distance $1/\sqrt2$ from the centre: we want the part of the unit ball above $z=1/\sqrt2$. For fixed $\phi,\theta$ the ray from the origin enters the region on the plane $\rho\cos\phi=1/\sqrt2$, i.e. $\rho=\frac1{\sqrt2}\sec\phi$, and leaves on the sphere $\rho=1$. The plane meets the sphere where $z=r=1/\sqrt2$, i.e. $\phi=\pi/4$. So
$$V=\int_0^{2\pi}\!\!\int_0^{\pi/4}\!\!\int_{\sec\phi/\sqrt2}^1\rho^2\sin\phi\,d\rho\,d\phi\,d\theta=\frac{2\pi}3-\frac{5\pi}{6\sqrt2}\approx0.243 ,$$
which agrees with the formula $\pi h^2(3-h)/3$ for a cap of height $h=1-1/\sqrt2$ of a unit ball.

:::
