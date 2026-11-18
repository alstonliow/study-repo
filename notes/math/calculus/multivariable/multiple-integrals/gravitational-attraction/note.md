---
title: "Gravitational Attraction"
sources: [mit1802-26, mit1802n-G]
requires: [math/calculus/multivariable/multiple-integrals/spherical-coordinates]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lecture 26 and Supplementary Notes G, in our own wording. Numbers checked in Python (sympy). -->

A mass $\Delta M$ at the point $(x,y,z)$, at distance $\rho$ from a mass $m$ at the origin, attracts it with a force of magnitude $G\,m\,\Delta M/\rho^2$ ($G$ the gravitational constant) directed towards $(x,y,z)$:
$$\mathbf{F}=\frac{G\,m\,\Delta M}{\rho^2}\cdot\frac{\langle x,y,z\rangle}{\rho}=\frac{G\,m\,\Delta M}{\rho^3}\langle x,y,z\rangle .$$

::: {#prp-attraction-of-solid .proposition name="Attraction of a solid"}

A solid $D$ of density $\delta$ attracts a mass $m$ at the origin with the force
$$\mathbf{F}=Gm\iiint_D\frac{\langle x,y,z\rangle}{\rho^3}\,\delta\,dV .$$
If $D$ is symmetric about the $z$-axis, then $\mathbf{F}=\langle0,0,F_z\rangle$ with
$$F_z=Gm\iiint_D\frac{z}{\rho^3}\,\delta\,dV=Gm\iiint_D\delta\cos\phi\sin\phi\,d\rho\,d\phi\,d\theta .$$

:::

::: {.proof}

1. Add up the forces of the small pieces $\Delta M=\delta\,\Delta V$ and pass to the limit.

2. With symmetry about the $z$-axis, the horizontal components of pieces placed symmetrically cancel.

3. In spherical coordinates $z/\rho^3=\cos\phi/\rho^2$, and $dV=\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$, so the $\rho^2$ cancels.

:::

The usual set-up: put the test mass at the origin and the axis of symmetry of the solid along the $z$-axis.

::: {#thm-newton-shell .theorem name="Newton's theorem"}

A uniform solid ball of mass $M$ and radius $a$ attracts a mass $m$ outside it as if all its mass were at its centre. For a mass on its surface, the force has magnitude $GMm/a^2$.

:::

::: {.proof}

1. We treat the case of a mass $m$ at the origin on the surface. Place the ball with centre $(0,0,a)$, so it is tangent to the $xy$-plane at the origin.

2. In the vertical plane through the $z$-axis at angle $\theta$, a ray from the origin at angle $\phi$ from the $z$-axis meets the sphere again at distance $\rho=2a\cos\phi$ (the triangle from the origin to the far pole to the point is right-angled at the point, with hypotenuse $2a$). The ray meets the ball for $0\le\phi\le\pi/2$.

3. By @prp-attraction-of-solid,
$$F_z=Gm\delta\int_0^{2\pi}\!\!\int_0^{\pi/2}\!\!\int_0^{2a\cos\phi}\cos\phi\sin\phi\,d\rho\,d\phi\,d\theta=Gm\delta\cdot2\pi\cdot2a\int_0^{\pi/2}\cos^2\phi\sin\phi\,d\phi=\frac43\pi a\,G\,m\,\delta .$$

4. With $M=\frac43\pi a^3\delta$ this is $GMm/a^2$, the attraction of a point mass $M$ at the centre, distance $a$ away. (The case of a mass at distance greater than $a$ is similar, with harder limits.)

:::
