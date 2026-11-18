---
title: "Partial Fractions"
sources: [mit1801-29, mit1801n-F]
requires: [math/calculus/single-variable/integration-techniques/trigonometric-substitution, math/discrete/polynomials/polynomials-and-roots]
aliases: [math/calculus/integration-techniques/partial-fractions]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lecture 29 and Supplementary Notes F (cover-up method), in our own wording. Results checked with sympy. -->

::: {#thm-partial-fractions .theorem name="Partial fraction decomposition"}

Let $P/Q$ be a rational function with $\deg P<\deg Q$, and factor $Q$ into real linear and irreducible quadratic factors. Then $P/Q$ is a sum of terms
$$\frac{A}{(x-a)^k}\quad\text{for each factor }(x-a)^m,\ k=1,\dots,m,\qquad \frac{Bx+C}{(x^2+px+q)^k}\quad\text{for each factor }(x^2+px+q)^m,$$
with constants $A,B,C$ determined uniquely.

:::

We use the theorem without proof. If $\deg P\ge\deg Q$, first divide: $P/Q=(\text{polynomial})+R/Q$ with $\deg R<\deg Q$.

::: {#prp-cover-up .proposition name="Cover-up method"}

For a simple linear factor $(x-a)$ of $Q$, the coefficient of $\frac{A}{x-a}$ is
$$A=\Big[(x-a)\frac{P(x)}{Q(x)}\Big]_{x=a},$$
computed by covering the factor $x-a$ in $Q$ and substituting $x=a$ in what remains.

:::

::: {.proof}

1. Multiply the decomposition by $(x-a)$: $(x-a)\frac PQ=A+(x-a)\cdot(\text{the other terms})$.

2. The other terms have no factor $x-a$ in their denominators, so at $x=a$ the second part is $0$.

:::

::: {#exm-partial-fractions-simple .example name="Distinct linear factors"}

$\frac{x+3}{(x-1)(x+2)}=\frac{A}{x-1}+\frac{B}{x+2}$ with $A=\frac{4}{3}$ (cover $x-1$, put $x=1$) and $B=\frac{1}{-3}$ (cover $x+2$, put $x=-2$). So
$$\int\frac{x+3}{(x-1)(x+2)}dx=\tfrac43\ln\lvert x-1\rvert-\tfrac13\ln\lvert x+2\rvert+c .$$

:::

::: {#exm-partial-fractions-repeated .example name="A repeated factor"}

$\frac{x^2+2}{(x-1)^2(x+2)}=\frac{A}{x-1}+\frac{B}{(x-1)^2}+\frac{C}{x+2}$. Cover-up gives $B=\frac{3}{3}=1$ (cover $(x-1)^2$, $x=1$) and $C=\frac{6}{9}=\frac23$. Comparing $x^2$ coefficients after clearing denominators, $A+C=1$, so $A=\frac13$.

:::

::: {#exm-partial-fractions-quadratic .example name="A quadratic factor"}

$\frac{1}{x(x^2+1)}=\frac1x-\frac{x}{x^2+1}$, so $\int\frac{dx}{x(x^2+1)}=\ln\lvert x\rvert-\tfrac12\ln(x^2+1)+c$.

:::

Every rational function therefore has an elementary antiderivative made of rational functions, logarithms and arctangents.
