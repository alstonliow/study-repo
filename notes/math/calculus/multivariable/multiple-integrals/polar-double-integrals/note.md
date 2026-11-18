---
title: "Double Integrals in Polar Coordinates"
sources: [mit1802-17, mit1802n-I]
requires: [math/calculus/multivariable/multiple-integrals/double-integrals, math/calculus/single-variable/applications-of-integrals/polar-coordinates]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lecture 17 and Supplementary Notes I.2, in our own wording. Numbers checked in Python (sympy). -->

Polar coordinates $x=r\cos\theta$, $y=r\sin\theta$ (@def-polar-coordinates) help when the region or the integrand is simpler in $r$ and $\theta$, typically when it involves $x^2+y^2=r^2$.

::: {#thm-polar-area-element .theorem name="Area element in polar coordinates"}

$$dA=r\,dr\,d\theta,\qquad\text{so}\qquad\iint_Rf\,dA=\iint_Rf(r\cos\theta,r\sin\theta)\,r\,dr\,d\theta .$$

:::

::: {.proof}

1. The small region $r\le r'\le r+\Delta r$, $\theta\le\theta'\le\theta+\Delta\theta$ is nearly a rectangle with sides $\Delta r$ (radial) and $r\Delta\theta$ (an arc of the circle of radius $r$).

2. So $\Delta A\approx r\,\Delta r\,\Delta\theta$, and the sums defining the integral become sums of $f\,r\,\Delta r\,\Delta\theta$. (Exactly: the region is the difference of two sectors, of area $\frac12\big((r+\Delta r)^2-r^2\big)\Delta\theta=(r+\frac12\Delta r)\Delta r\Delta\theta$.)

:::

To set up the limits for $dr\,d\theta$: fix $\theta$ and follow the ray from the origin at angle $\theta$; it enters $R$ at $r_1(\theta)$ and leaves at $r_2(\theta)$. Then let $\theta$ run over the angles of the rays that meet $R$.

::: {#exm-polar-quarter-disk .example name="The quarter disk again"}

For @exm-double-integral-quarter-disk: $0\le r\le1$, $0\le\theta\le\pi/2$, and
$$\int_0^{\pi/2}\!\!\int_0^1(1-r^2)\,r\,dr\,d\theta=\int_0^{\pi/2}\Big[\frac{r^2}2-\frac{r^4}4\Big]_0^1d\theta=\frac\pi2\cdot\frac14=\frac\pi8 .$$

:::

::: {#exm-gaussian-integral .example name="The bell-curve integral"}

Let $I=\int_{-\infty}^\infty e^{-x^2}dx$. Then
$$I^2=\iint_{\mathbb{R}^2}e^{-x^2-y^2}\,dA=\int_0^{2\pi}\!\!\int_0^\infty e^{-r^2}r\,dr\,d\theta=2\pi\cdot\frac12=\pi,$$
so $I=\sqrt\pi$. (The improper double integral is the limit over larger and larger disks.)

:::
