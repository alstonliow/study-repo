---
title: "Sum, Product and Quotient Rules"
sources: [mit1801-3]
requires: [math/calculus/single-variable/differentiation/derivative]
aliases: [math/calculus/differentiation/differentiation-rules]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lecture 3, in our own wording; proofs written out in steps. -->

Derivative formulas come in two kinds: formulas for particular functions ($x^n$, $\sin x$, $e^x$) and rules for combining functions. This note covers the combining rules; with them every polynomial and rational function can be differentiated.

::: {#thm-linearity-of-derivative .theorem name="Linearity"}

If $u,v$ are differentiable and $c$ is a constant, then
$$(u+v)'=u'+v',\qquad (cu)'=cu'.$$

:::

::: {.proof}

1. $\dfrac{\Delta(u+v)}{\Delta x}=\dfrac{\Delta u}{\Delta x}+\dfrac{\Delta v}{\Delta x}$ and $\dfrac{\Delta(cu)}{\Delta x}=c\dfrac{\Delta u}{\Delta x}$.

2. Take $\Delta x\to0$ and use the limit laws.

:::

::: {#thm-derivative-product-rule .theorem name="Product rule"}

$$(uv)'=u'v+uv'.$$

:::

::: {.proof}

1. Write $\Delta u=u(x+\Delta x)-u(x)$ and similarly $\Delta v$. Then
$$u(x+\Delta x)v(x+\Delta x)-u(x)v(x)=\Delta u\,v(x+\Delta x)+u(x)\,\Delta v .$$

2. Divide by $\Delta x$: $\dfrac{\Delta(uv)}{\Delta x}=\dfrac{\Delta u}{\Delta x}\,v(x+\Delta x)+u(x)\,\dfrac{\Delta v}{\Delta x}$.

3. As $\Delta x\to0$, $v(x+\Delta x)\to v(x)$ because $v$ is continuous (@thm-differentiable-continuous). The limit is $u'v+uv'$.

:::

::: {#thm-quotient-rule .theorem name="Quotient rule"}

Where $v\neq0$,
$$\Big(\frac uv\Big)'=\frac{u'v-uv'}{v^2}.$$

:::

::: {.proof}

1. $\dfrac{u+\Delta u}{v+\Delta v}-\dfrac uv=\dfrac{(u+\Delta u)v-u(v+\Delta v)}{v(v+\Delta v)}=\dfrac{\Delta u\,v-u\,\Delta v}{v(v+\Delta v)}$.

2. Divide by $\Delta x$ and let $\Delta x\to0$; $\Delta v\to0$ by continuity of $v$, giving $\dfrac{u'v-uv'}{v^2}$.

:::

::: {#cor-power-rule-negative .corollary name="Power rule for negative integers"}

For $n=1,2,\dots$ and $x\neq0$, $\dfrac{d}{dx}x^{-n}=-nx^{-n-1}$.

:::

::: {.proof}

1. Apply @thm-quotient-rule with $u=1$, $v=x^n$: $\dfrac{0\cdot x^n-1\cdot nx^{n-1}}{x^{2n}}=-nx^{-n-1}$.

:::

::: {#exm-product-rule-three .example name="A product of three factors"}

Applying the product rule twice, $(uvw)'=u'vw+uv'w+uvw'$: differentiate one factor at a time and add.

:::

::: {#exm-quotient-rule .example name="A rational function"}

$$\frac{d}{dx}\frac{x}{x^2+1}=\frac{(x^2+1)-x\cdot2x}{(x^2+1)^2}=\frac{1-x^2}{(x^2+1)^2}.$$

:::
