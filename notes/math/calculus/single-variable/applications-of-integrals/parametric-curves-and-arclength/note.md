---
title: "Parametric Curves, Arclength and Surface Area"
sources: [mit1801-30, mit1801-31]
requires: [math/calculus/single-variable/applications-of-integrals/volumes, math/calculus/single-variable/integration-techniques/trigonometric-substitution]
aliases: [math/calculus/applications-of-integrals/parametric-curves-and-arclength]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lectures 30 (arclength) and 31, in our own wording. Numbers checked in Python. -->

::: {#def-parametric-curve .definition name="Parametric curve"}

A parametric curve is a pair of functions $x=x(t)$, $y=y(t)$ for $t$ in an interval; $t$ is the parameter (often time). Its velocity vector is $(x'(t),y'(t))$ and its speed is $\sqrt{x'^2+y'^2}$. The slope of the curve is $\dfrac{dy}{dx}=\dfrac{y'(t)}{x'(t)}$ where $x'(t)\neq0$.

:::

::: {#exm-parametric-circle .example name="Circles and ellipses"}

$x=a\cos t$, $y=a\sin t$, $0\le t\le2\pi$, traces the circle $x^2+y^2=a^2$ counter-clockwise with speed $a$. $x=a\cos t$, $y=b\sin t$ traces the ellipse $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$.

:::

::: {#prp-arclength .proposition name="Arclength"}

The length of the curve $(x(t),y(t))$, $a\le t\le b$, is
$$s=\int_a^b\sqrt{x'(t)^2+y'(t)^2}\,dt ;\qquad\text{for a graph } y=f(x):\ s=\int_a^b\sqrt{1+f'(x)^2}\,dx .$$

:::

Reason: a short piece has $(\Delta s)^2\approx(\Delta x)^2+(\Delta y)^2$, so $ds=\sqrt{dx^2+dy^2}$ and the length adds up the pieces.

::: {#exm-arclength-semicubical .example name="A curve with a cusp"}

For $x=t^2$, $y=t^3$, $0\le t\le1$: $ds=\sqrt{4t^2+9t^4}\,dt=t\sqrt{4+9t^2}\,dt$, and $s=\frac1{27}(4+9t^2)^{3/2}\Big|_0^1=\frac{13^{3/2}-8}{27}\approx1.440$.

:::

::: {#prp-surface-of-revolution .proposition name="Area of a surface of revolution"}

Rotating the curve around the $x$-axis (with $y\ge0$) sweeps a surface of area
$$A=\int2\pi y\,ds .$$

:::

Each piece of length $ds$ at height $y$ sweeps a thin band of circumference $2\pi y$.

::: {#exm-surface-of-sphere .example name="Area of a sphere"}

For $y=\sqrt{a^2-x^2}$: $ds=\frac{a}{\sqrt{a^2-x^2}}dx$, so $2\pi y\,ds=2\pi a\,dx$ and $A=\int_{-a}^a2\pi a\,dx=4\pi a^2$. The band between $x=x_1$ and $x=x_1+h$ always has area $2\pi ah$, whatever $x_1$ is.

:::
