---
title: "Trigonometric Substitution"
sources: [mit1801-26, mit1801-28]
requires: [math/calculus/single-variable/integration-techniques/trigonometric-integrals]
aliases: [math/calculus/integration-techniques/trigonometric-substitution]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lectures 26 and 28 (inverse substitution, completing the square), in our own wording. Results checked with sympy. -->

::: {#def-trigonometric-substitution .definition name="Trigonometric substitutions"}

An inverse substitution writes $x$ as a function of a new variable. For square roots of quadratics ($a>0$):
$$\begin{aligned}
\sqrt{a^2-x^2}:&\quad x=a\sin\theta, & dx&=a\cos\theta\,d\theta, & \sqrt{a^2-x^2}&=a\cos\theta;\\
\sqrt{a^2+x^2}:&\quad x=a\tan\theta, & dx&=a\sec^2\theta\,d\theta, & \sqrt{a^2+x^2}&=a\sec\theta;\\
\sqrt{x^2-a^2}:&\quad x=a\sec\theta, & dx&=a\sec\theta\tan\theta\,d\theta, & \sqrt{x^2-a^2}&=a\tan\theta .
\end{aligned}$$
After integrating in $\theta$, return to $x$ using a right triangle with the matching sides.

:::

::: {#exm-trig-sub-sine .example name="A sine substitution"}

$\int\frac{dx}{x^2\sqrt{1-x^2}}$: with $x=\sin\theta$ this is $\int\frac{\cos\theta\,d\theta}{\sin^2\theta\cos\theta}=\int\csc^2\theta\,d\theta=-\cot\theta+c=-\frac{\sqrt{1-x^2}}{x}+c$.

:::

::: {#exm-trig-sub-area-circle .example name="Area of a circle"}

$\int_{-a}^a\sqrt{a^2-x^2}\,dx$ with $x=a\sin\theta$, $\theta\in[-\pi/2,\pi/2]$, is $a^2\int_{-\pi/2}^{\pi/2}\cos^2\theta\,d\theta=\frac{\pi a^2}2$, half the area of the disc.

:::

::: {#exm-trig-sub-tangent .example name="A tangent substitution"}

$\int\frac{dx}{\sqrt{1+x^2}}$ with $x=\tan\theta$ is $\int\sec\theta\,d\theta=\ln\lvert\sec\theta+\tan\theta\rvert+c=\ln\big(x+\sqrt{1+x^2}\big)+c$ by @prp-tan-sec-integrals.

:::

::: {#prp-completing-the-square .proposition name="Completing the square"}

A general quadratic reduces to one of the three forms above by
$$x^2+bx+c=\Big(x+\frac b2\Big)^2+\Big(c-\frac{b^2}4\Big)$$
and the shift $u=x+b/2$.

:::

::: {#exm-completing-the-square .example name="A shifted root"}

$\int\frac{dx}{\sqrt{x^2+4x}}$: $x^2+4x=(x+2)^2-4$, so with $x+2=2\sec\theta$ the integral is $\int\sec\theta\,d\theta=\ln\Big\lvert\frac{x+2}2+\frac{\sqrt{x^2+4x}}2\Big\rvert+c$, or $\ln\big\lvert x+2+\sqrt{x^2+4x}\big\rvert+c'$.

:::
