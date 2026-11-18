---
title: "Implicit Differentiation and Inverse Functions"
sources: [mit1801-5]
requires: [math/calculus/single-variable/differentiation/chain-rule]
aliases: [math/calculus/differentiation/implicit-differentiation]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lecture 5, in our own wording; proofs written out in steps. -->

When $y$ is given by an equation $F(x,y)=0$ instead of a formula, differentiate both sides with respect to $x$, treating $y$ as a function of $x$ (so $\frac{d}{dx}y^2=2yy'$ by the chain rule), then solve for $y'$.

::: {#exm-implicit-circle .example name="The circle"}

From $x^2+y^2=1$: $2x+2yy'=0$, so $y'=-x/y$ wherever $y\neq0$. This one formula serves both halves $y=\pm\sqrt{1-x^2}$.

:::

::: {#exm-implicit-cubic .example name="A curve with no explicit formula"}

From $y^3+xy^2+1=0$: $3y^2y'+y^2+2xyy'=0$, so $y'=\dfrac{-y^2}{3y^2+2xy}$. At the point $(-2,1)$ on the curve, $y'=-1/(3-4)=1$.

:::

::: {#thm-power-rule-rational .theorem name="Power rule for rational exponents"}

For a rational number $a=m/n$ and $x>0$, $\dfrac{d}{dx}x^{a}=ax^{a-1}$.

:::

::: {.proof}

1. Let $y=x^{m/n}$, so $y^n=x^m$.

2. Differentiate implicitly: $ny^{n-1}y'=mx^{m-1}$.

3. Then $y'=\dfrac mn\,\dfrac{x^{m-1}}{y^{n-1}}=\dfrac mn\,\dfrac{x^{m-1}}{x^{m(n-1)/n}}=\dfrac mn\,x^{m/n-1}$.

:::

## Derivatives of inverse functions

::: {#thm-inverse-function-derivative .theorem name="Derivative of an inverse"}

If $y=f(x)$ has a differentiable inverse $x=g(y)$ and $f'(x)\neq0$, then
$$g'(y)=\frac1{f'(x)},\qquad\text{that is}\qquad \frac{dx}{dy}=\frac{1}{dy/dx}.$$

:::

::: {.proof}

1. Differentiate $f(g(y))=y$ with respect to $y$ using @thm-derivative-chain-rule: $f'(g(y))\,g'(y)=1$.

2. Divide by $f'(g(y))=f'(x)\neq0$.

:::

Geometrically, reflecting in $y=x$ (@prp-graph-of-inverse) turns a slope $m$ into $1/m$.

::: {#prp-inverse-trig-derivatives .proposition name="Inverse trigonometric derivatives"}

$$\frac{d}{dx}\sin^{-1}x=\frac1{\sqrt{1-x^2}},\qquad\frac{d}{dx}\cos^{-1}x=\frac{-1}{\sqrt{1-x^2}}\quad(-1<x<1),\qquad\frac{d}{dx}\tan^{-1}x=\frac1{1+x^2}.$$

:::

::: {.proof}

1. Let $y=\sin^{-1}x$ with $-\pi/2\le y\le\pi/2$. From $\sin y=x$, $\cos y\,y'=1$. On this range $\cos y\ge0$, so $\cos y=\sqrt{1-x^2}$ and $y'=1/\sqrt{1-x^2}$.

2. Let $y=\cos^{-1}x$ with $0\le y\le\pi$. From $\cos y=x$, $-\sin y\,y'=1$. Here $\sin y\ge0$, so $\sin y=\sqrt{1-x^2}$ and $y'=-1/\sqrt{1-x^2}$.

3. Let $y=\tan^{-1}x$ with $-\pi/2<y<\pi/2$. From $\tan y=x$, $\sec^2y\,y'=1$, and $\sec^2y=1+\tan^2y=1+x^2$.

:::
