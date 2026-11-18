---
title: "Antiderivatives and Substitution"
sources: [mit1801-15]
requires: [math/calculus/single-variable/applications-of-derivatives/mean-value-theorem]
aliases: [math/calculus/integrals/antiderivatives]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lecture 15, in our own wording; proofs written out in steps. -->

::: {#def-antiderivative .definition name="Antiderivative, indefinite integral"}

$G$ is an antiderivative of $g$ if $G'=g$. The indefinite integral
$$\int g(x)\,dx=G(x)+c$$
denotes all antiderivatives of $g$, where $c$ is an arbitrary constant.

:::

::: {#thm-antiderivatives-differ-by-constant .theorem name="Uniqueness up to a constant"}

On an interval, two antiderivatives of the same function differ by a constant.

:::

::: {.proof}

1. If $F'=G'=g$ on an interval, then $(F-G)'=0$ there.

2. By @cor-sign-of-derivative, $F-G$ is constant.

:::

On a domain made of several intervals the constant may differ on each piece: $\int\frac{dx}x=\ln\lvert x\rvert+c$, with independent constants for $x>0$ and $x<0$.

::: {#prp-basic-antiderivatives .proposition name="Basic antiderivatives"}

$$\begin{aligned}
\int x^a\,dx&=\frac{x^{a+1}}{a+1}+c\ (a\neq-1), &\int\frac{dx}{x}&=\ln\lvert x\rvert+c, &\int e^{ax}dx&=\frac{e^{ax}}a+c,\\
\int\sin x\,dx&=-\cos x+c, &\int\cos x\,dx&=\sin x+c, &\int\sec^2x\,dx&=\tan x+c,\\
\int\frac{dx}{\sqrt{1-x^2}}&=\sin^{-1}x+c, &\int\frac{dx}{1+x^2}&=\tan^{-1}x+c.
\end{aligned}$$

:::

Each is checked by differentiating the right side.

::: {#thm-substitution-indefinite .theorem name="Substitution"}

If $u=u(x)$ is differentiable and $F'=f$, then
$$\int f(u(x))\,u'(x)\,dx=F(u(x))+c,\qquad\text{written}\qquad \int f(u)\,du\ \text{ with } du=u'(x)\,dx .$$

:::

::: {.proof}

1. By @thm-derivative-chain-rule, $\dfrac{d}{dx}F(u(x))=f(u(x))\,u'(x)$.

:::

::: {#exm-substitution .example name="Substitutions"}

- $\int x^3(x^4+2)^5dx$: with $u=x^4+2$, $du=4x^3dx$, this is $\tfrac14\int u^5du=\tfrac1{24}(x^4+2)^6+c$.
- $\int\frac{x\,dx}{\sqrt{1+x^2}}$: with $u=1+x^2$, it is $\tfrac12\int u^{-1/2}du=\sqrt{1+x^2}+c$.
- $\int xe^{-x^2}dx=-\tfrac12e^{-x^2}+c$, with $u=-x^2$.
- $\int\frac{dx}{x\ln x}=\ln\lvert\ln x\rvert+c$, with $u=\ln x$.

:::
