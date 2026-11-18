---
title: "Separable Differential Equations"
sources: [mit1801-16]
requires: [math/calculus/integrals/antiderivatives]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lecture 16, in our own wording. -->

::: {#def-separable-equation .definition name="Separable differential equation"}

A first-order equation of the form
$$\frac{dy}{dx}=f(x)\,g(y)$$
is separable. Where $g(y)\neq0$ it is solved by separating variables and integrating:
$$\int\frac{dy}{g(y)}=\int f(x)\,dx .$$
This gives $H(y)=F(x)+c$, an implicit formula for $y$; solve for $y$ if possible.

:::

Why it works: if $H'=1/g$ and $y=y(x)$ is a solution, then $\frac{d}{dx}H(y(x))=\frac{y'}{g(y)}=f(x)$, so $H(y(x))$ is an antiderivative of $f$. Points with $g(y_0)=0$ give constant solutions $y\equiv y_0$, which the division loses.

::: {#exm-exponential-growth .example name="Exponential growth"}

$y'=ky$: $\int\frac{dy}y=\int k\,dx$ gives $\ln\lvert y\rvert=kx+c$, so $y=Ae^{kx}$ with $A=\pm e^c$; $A=0$ is the lost constant solution. With $y(0)=y_0$, $y=y_0e^{kx}$.

:::

::: {#exm-separable-gaussian .example name="A bell curve"}

$y'+xy=0$, i.e. $y'=-xy$: $\ln\lvert y\rvert=-\tfrac12x^2+c$, so $y=Ae^{-x^2/2}$.

:::

::: {#exm-orthogonal-trajectories .example name="Curves crossing parabolas at right angles"}

The parabolas $y=ax^2$ satisfy $y'=2ax=2y/x$ (eliminating $a$). A curve meeting each of them at right angles has slope $-x/(2y)$, so $2y\,dy=-x\,dx$, $y^2=-\tfrac12x^2+c$, i.e. $\tfrac{x^2}2+y^2=c$: a family of ellipses.

:::
