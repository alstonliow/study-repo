---
title: "Trigonometric Limits and Derivatives"
sources: [mit1801-2, mit1801-3]
requires: [math/calculus/differentiation/differentiation-rules]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lectures 2 and 3, in our own wording; proofs written out in steps. Angles are in radians. -->

::: {#thm-two-trig-limits .theorem name="Two trigonometric limits"}

$$\lim_{\theta\to0}\frac{\sin\theta}{\theta}=1,\qquad \lim_{\theta\to0}\frac{1-\cos\theta}{\theta}=0 .$$

:::

::: {.proof}

1. Let $0<\theta<\pi/2$ and take the unit circle. The triangle with vertices $(0,0)$, $(1,0)$, $(\cos\theta,\sin\theta)$, the sector of angle $\theta$, and the right triangle with legs $1$ and $\tan\theta$ are nested, so their areas satisfy
$$\tfrac12\sin\theta\le\tfrac12\theta\le\tfrac12\tan\theta .$$

2. Dividing by $\tfrac12\sin\theta>0$ and inverting: $\cos\theta\le\dfrac{\sin\theta}{\theta}\le1$. Both sides are even in $\theta$, so this also holds for $-\pi/2<\theta<0$.

3. As $\theta\to0$, $\cos\theta\to1$; by @thm-squeeze-functions, $\sin\theta/\theta\to1$.

4. For the second limit, $\dfrac{1-\cos\theta}{\theta}=\dfrac{1-\cos^2\theta}{\theta(1+\cos\theta)}=\dfrac{\sin\theta}{\theta}\cdot\dfrac{\sin\theta}{1+\cos\theta}\to1\cdot\dfrac02=0$.

:::

::: {#thm-derivatives-of-sine-cosine .theorem name="Derivatives of sine and cosine"}

$$\frac{d}{dx}\sin x=\cos x,\qquad \frac{d}{dx}\cos x=-\sin x .$$

:::

::: {.proof}

1. By the addition formula, $\sin(x+\Delta x)-\sin x=\sin x(\cos\Delta x-1)+\cos x\sin\Delta x$.

2. Divide by $\Delta x$: $\dfrac{\Delta\sin}{\Delta x}=-\sin x\,\dfrac{1-\cos\Delta x}{\Delta x}+\cos x\,\dfrac{\sin\Delta x}{\Delta x}\to-\sin x\cdot0+\cos x\cdot1$ by @thm-two-trig-limits.

3. Similarly $\cos(x+\Delta x)-\cos x=\cos x(\cos\Delta x-1)-\sin x\sin\Delta x$, and the quotient tends to $-\sin x$.

:::

::: {#cor-derivatives-of-tan-sec .corollary name="Other trigonometric derivatives"}

$$\frac{d}{dx}\tan x=\sec^2x,\qquad \frac{d}{dx}\sec x=\sec x\tan x,\qquad \frac{d}{dx}\cot x=-\csc^2x,\qquad\frac{d}{dx}\csc x=-\csc x\cot x .$$

:::

::: {.proof}

1. $\tan x=\sin x/\cos x$, so by @thm-quotient-rule its derivative is $\dfrac{\cos^2x+\sin^2x}{\cos^2x}=\sec^2x$.

2. $\sec x=1/\cos x$ has derivative $\dfrac{\sin x}{\cos^2x}=\sec x\tan x$. The other two follow in the same way from $\cot x=\cos x/\sin x$ and $\csc x=1/\sin x$.

:::

::: {#exm-why-radians .example name="Why radians"}

In degrees, $\sin(x^\circ)=\sin(\pi x/180)$, and the limit becomes $\lim_{x\to0}\sin(x^\circ)/x=\pi/180$. Every derivative formula would carry this factor; radians are chosen to make it $1$.

:::
