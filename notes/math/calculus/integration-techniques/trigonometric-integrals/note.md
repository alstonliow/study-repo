---
title: "Trigonometric Integrals"
sources: [mit1801-26]
requires: [math/calculus/integrals/fundamental-theorem]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lecture 26, in our own wording. Results checked with sympy. -->

::: {#prp-sine-cosine-powers-odd .proposition name="$\int\sin^mx\cos^nx\,dx$ with an odd power"}

If $n$ is odd, write $\cos^nx=\cos^{n-1}x\cos x$, express $\cos^{n-1}x=(1-\sin^2x)^{(n-1)/2}$, and substitute $u=\sin x$, $du=\cos x\,dx$; the integral becomes a polynomial in $u$. If $m$ is odd, do the same with $u=\cos x$.

:::

::: {#exm-odd-power .example name="An odd power"}

$\int\sin^3x\cos^2x\,dx=\int(1-\cos^2x)\cos^2x\sin x\,dx$. With $u=\cos x$, $du=-\sin x\,dx$: $-\int(u^2-u^4)du=-\frac{\cos^3x}3+\frac{\cos^5x}5+c$.

:::

::: {#prp-sine-cosine-powers-even .proposition name="Even powers: half-angle formulas"}

If $m$ and $n$ are both even, lower the powers with
$$\cos^2x=\frac{1+\cos2x}2,\qquad\sin^2x=\frac{1-\cos2x}2,\qquad\sin x\cos x=\frac{\sin2x}2 .$$

:::

::: {#exm-even-powers .example name="Even powers"}

- $\int\cos^2x\,dx=\frac x2+\frac{\sin2x}4+c$.
- $\int\sin^2x\cos^2x\,dx=\frac14\int\sin^22x\,dx=\frac18\int(1-\cos4x)\,dx=\frac x8-\frac{\sin4x}{32}+c$.

:::

::: {#prp-tan-sec-integrals .proposition name="Tangent and secant"}

$$\int\tan x\,dx=-\ln\lvert\cos x\rvert+c,\qquad\int\sec x\,dx=\ln\lvert\sec x+\tan x\rvert+c .$$

:::

::: {.proof}

1. $\int\frac{\sin x}{\cos x}dx$ with $u=\cos x$ is $-\int\frac{du}u=-\ln\lvert u\rvert+c$.

2. $\frac{d}{dx}\ln(\sec x+\tan x)=\frac{\sec x\tan x+\sec^2x}{\sec x+\tan x}=\sec x$.

:::

Powers of $\sec x$ and $\tan x$: for $\int\sec^nx\tan^mx\,dx$ with $n$ even, substitute $u=\tan x$ and keep one $\sec^2x\,dx=du$, using $\sec^2x=1+\tan^2x$; for example $\int\sec^4x\,dx=\int(1+u^2)du=\tan x+\frac{\tan^3x}3+c$. Odd powers of $\sec x$ alone need integration by parts (see the note on that method).
