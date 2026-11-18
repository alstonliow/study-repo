---
title: "Integration by Parts"
sources: [mit1801-30]
requires: [math/calculus/integration-techniques/trigonometric-integrals]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lecture 30, in our own wording; proofs written out in steps. Results checked with sympy. -->

::: {#thm-integration-by-parts .theorem name="Integration by parts"}

For continuously differentiable $u,v$,
$$\int uv'\,dx=uv-\int u'v\,dx,\qquad \int_a^buv'\,dx=uv\Big|_a^b-\int_a^bu'v\,dx .$$

:::

::: {.proof}

1. By @thm-derivative-product-rule, $(uv)'=u'v+uv'$.

2. Integrate both sides and rearrange; for the definite form use @thm-ftc-1.

:::

Choose $u$ to become simpler when differentiated ($\ln x$, $\tan^{-1}x$, powers of $x$) and $v'$ to be easy to integrate.

::: {#exm-by-parts .example name="Integrating by parts"}

- $\int\tan^{-1}x\,dx$ with $u=\tan^{-1}x$, $v=x$: $x\tan^{-1}x-\int\frac{x}{1+x^2}dx=x\tan^{-1}x-\frac12\ln(1+x^2)+c$.
- $\int\ln x\,dx=x\ln x-\int x\cdot\frac1x\,dx=x\ln x-x+c$.
- $\int xe^x\,dx=xe^x-\int e^xdx=(x-1)e^x+c$.

:::

::: {#prp-reduction-formulas .proposition name="Reduction formulas"}

For $n\ge1$,
$$\int x^ne^x\,dx=x^ne^x-n\int x^{n-1}e^x\,dx,\qquad \int(\ln x)^n\,dx=x(\ln x)^n-n\int(\ln x)^{n-1}dx .$$

:::

::: {.proof}

1. First: $u=x^n$, $v=e^x$.

2. Second: $u=(\ln x)^n$, $v=x$, so $u'v=n(\ln x)^{n-1}$.

:::

Applying a reduction formula repeatedly lowers $n$ to $0$; for example $\int x^2e^x\,dx=(x^2-2x+2)e^x+c$.

::: {#exm-secant-cubed .example name="$\int\sec^3x\,dx$"}

With $u=\sec x$, $v=\tan x$: $\int\sec^3x\,dx=\sec x\tan x-\int\sec x\tan^2x\,dx=\sec x\tan x-\int\sec^3x\,dx+\int\sec x\,dx$. The unknown integral appears on both sides, so
$$\int\sec^3x\,dx=\tfrac12\big(\sec x\tan x+\ln\lvert\sec x+\tan x\rvert\big)+c .$$

:::
