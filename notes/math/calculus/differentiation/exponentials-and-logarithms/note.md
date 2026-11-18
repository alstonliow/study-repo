---
title: "Exponentials, Logarithms and Hyperbolic Functions"
sources: [mit1801-6, mit1801-7]
requires: [math/calculus/differentiation/implicit-differentiation]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lectures 6 and 7, in our own wording; proofs written out in steps. Numbers checked in Python. -->

## The number $e$

For a base $a>1$,
$$\frac{a^{x+\Delta x}-a^x}{\Delta x}=a^x\,\frac{a^{\Delta x}-1}{\Delta x},$$
so $\frac{d}{dx}a^x=M(a)\,a^x$ with $M(a)=\lim_{h\to0}\frac{a^h-1}{h}$, the slope of $a^x$ at $x=0$. For $a=2$, $M\approx0.693$; for $a=3$, $M\approx1.099$.

::: {#def-number-e .definition name="The number $e$ and the natural logarithm"}

$e$ is the base for which $M(e)=1$, that is
$$\lim_{h\to0}\frac{e^h-1}{h}=1,\qquad e=2.71828\ldots$$
The natural logarithm $\ln x$ is the inverse of $e^x$: $\ln x=y\iff e^y=x$ for $x>0$.

:::

::: {#thm-derivative-exp-log .theorem name="Derivatives of $e^x$, $\ln x$ and $a^x$"}

$$\frac{d}{dx}e^x=e^x,\qquad \frac{d}{dx}\ln x=\frac1x\ (x>0),\qquad \frac{d}{dx}a^x=(\ln a)\,a^x .$$

:::

::: {.proof}

1. The first is the definition of $e$ together with the computation above.

2. If $y=\ln x$ then $e^y=x$; differentiating, $e^yy'=1$, so $y'=1/e^y=1/x$.

3. $a^x=e^{x\ln a}$, so by @thm-derivative-chain-rule its derivative is $(\ln a)e^{x\ln a}=(\ln a)a^x$. In particular $M(a)=\ln a$.

:::

::: {#prp-logarithmic-differentiation .proposition name="Logarithmic differentiation"}

Where $u>0$, $\dfrac{u'}{u}=(\ln u)'$. Hence $u'=u\,(\ln u)'$, which turns products and powers into sums.

:::

::: {#exm-logarithmic-differentiation .example name="Variable exponents"}

For $y=x^x$ ($x>0$): $\ln y=x\ln x$, so $y'/y=\ln x+1$ and $y'=x^x(1+\ln x)$. The same method gives $\frac{d}{dx}x^r=rx^{r-1}$ for every real $r$: $\ln y=r\ln x$, $y'/y=r/x$.

:::

::: {#exm-limit-for-e .example name="$e$ as a limit"}

$\ln\big((1+\tfrac1n)^n\big)=n\ln(1+\tfrac1n)=\dfrac{\ln(1+1/n)-\ln1}{1/n}\to(\ln)'(1)=1$, so $(1+\tfrac1n)^n\to e$. For $n=1000$ the value is $2.7169\ldots$

:::

## Hyperbolic functions

::: {#def-hyperbolic-functions .definition name="Hyperbolic functions"}

$$\cosh x=\frac{e^x+e^{-x}}2,\qquad \sinh x=\frac{e^x-e^{-x}}2 .$$

:::

::: {#prp-hyperbolic-identities .proposition name="Hyperbolic identities"}

$$\frac{d}{dx}\sinh x=\cosh x,\qquad\frac{d}{dx}\cosh x=\sinh x,\qquad \cosh^2x-\sinh^2x=1 .$$

:::

::: {.proof}

1. Differentiating $e^{\pm x}$ gives $\pm e^{\pm x}$, which swaps the two definitions.

2. $\cosh^2x-\sinh^2x=\tfrac14\big[(e^{2x}+2+e^{-2x})-(e^{2x}-2+e^{-2x})\big]=1$.

:::

So $(\cosh t,\sinh t)$ lies on the hyperbola $x^2-y^2=1$, as $(\cos t,\sin t)$ lies on the circle.
