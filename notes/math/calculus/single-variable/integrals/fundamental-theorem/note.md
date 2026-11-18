---
title: "The Fundamental Theorems of Calculus"
sources: [mit1801-19, mit1801-20, mit1801-21, mit1801n-FT]
requires: [math/calculus/single-variable/integrals/definite-integral, math/calculus/single-variable/integrals/antiderivatives]
aliases: [math/calculus/integrals/fundamental-theorem]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lectures 19, 20 and the logarithm part of 21, and Supplementary Notes FT, in our own wording; proofs written out in steps. Numbers checked in Python. -->

::: {#thm-ftc-1 .theorem name="First fundamental theorem"}

If $f$ is continuous on $[a,b]$ and $F'=f$, then
$$\int_a^bf(x)\,dx=F(b)-F(a)=F(x)\Big|_a^b .$$

:::

::: {.proof}

1. Split $[a,b]$ at $x_0<x_1<\dots<x_n$ and telescope: $F(b)-F(a)=\sum_{i=1}^n\big(F(x_i)-F(x_{i-1})\big)$.

2. By @thm-mean-value, $F(x_i)-F(x_{i-1})=f(c_i)\Delta x$ for some $c_i\in(x_{i-1},x_i)$.

3. So $F(b)-F(a)$ equals a Riemann sum for $f$, for every $n$. Letting $n\to\infty$, it equals $\int_a^bf$.

:::

::: {#exm-ftc-1 .example name="Using the first theorem"}

- $\int_0^\pi\sin x\,dx=-\cos x\big|_0^\pi=2$: one hump of the sine has area $2$.
- $\int_0^{2\pi}\sin x\,dx=0$: the area below the axis cancels the area above.
- $\int_1^2\frac{dx}x=\ln2$.

:::

The theorem also reads: if $F'=f$ then $\Delta F=\int f$. Positive $f$ means $F$ increases; bounds on $f$ give bounds on $F$. For instance, from $e^t\ge1$ on $[0,x]$ ($x\ge0$), integrating gives $e^x-1\ge x$; integrating again gives $e^x\ge1+x+x^2/2$.

::: {#thm-substitution-definite .theorem name="Substitution in definite integrals"}

If $u'$ is continuous on $[a,b]$ and $f$ is continuous on the range of $u$, then
$$\int_a^bf(u(x))\,u'(x)\,dx=\int_{u(a)}^{u(b)}f(u)\,du .$$

:::

::: {.proof}

1. Let $F'=f$. By @thm-substitution-indefinite and @thm-ftc-1 both sides equal $F(u(b))-F(u(a))$.

:::

::: {#thm-ftc-2 .theorem name="Second fundamental theorem"}

If $f$ is continuous on an interval containing $a$, then $G(x)=\int_a^xf(t)\,dt$ is differentiable and
$$G'(x)=f(x).$$

:::

::: {.proof}

1. $G(x+\Delta x)-G(x)=\int_x^{x+\Delta x}f(t)\,dt$ by @prp-integral-properties.

2. If $m$ and $M$ are the smallest and largest values of $f$ between $x$ and $x+\Delta x$, the integral lies between $m\Delta x$ and $M\Delta x$ (for $\Delta x>0$; the other case is the same).

3. So $\dfrac{G(x+\Delta x)-G(x)}{\Delta x}$ lies between $m$ and $M$. As $\Delta x\to0$, both tend to $f(x)$ by continuity.

:::

So every continuous function has an antiderivative, even when no formula exists: $\int_0^xe^{-t^2}dt$ and $\int_0^x\cos(t^2)\,dt$ are new functions defined by integrals. Combined with the chain rule, $\frac{d}{dx}\int_a^{u(x)}f(t)\,dt=f(u(x))\,u'(x)$.

::: {#def-logarithm-as-integral .definition name="The logarithm as an integral"}

$$\ln x=\int_1^x\frac{dt}{t}\qquad(x>0).$$

:::

By @thm-ftc-2, $(\ln x)'=1/x$, $\ln1=0$, $\ln$ is increasing and (since $(\ln x)''=-1/x^2<0$) concave down. Its properties, such as $\ln(ab)=\ln a+\ln b$, follow: both sides have the same derivative in $a$ and agree at $a=1$. This definition gives a second, self-contained route to $\ln$ and $e^x$.
