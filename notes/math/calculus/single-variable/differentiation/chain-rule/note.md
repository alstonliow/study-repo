---
title: "The Chain Rule and Higher Derivatives"
sources: [mit1801-4]
requires: [math/calculus/single-variable/differentiation/trigonometric-derivatives, math/discrete/functions/composition]
aliases: [math/calculus/differentiation/chain-rule]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lecture 4, in our own wording; proofs written out in steps. -->

::: {#thm-derivative-chain-rule .theorem name="Chain rule"}

If $x=g(t)$ is differentiable at $t$ and $y=f(x)$ is differentiable at $g(t)$, then $f\circ g$ is differentiable at $t$ and
$$\frac{dy}{dt}=\frac{dy}{dx}\frac{dx}{dt},\qquad\text{that is}\qquad (f\circ g)'(t)=f'(g(t))\,g'(t).$$

:::

::: {.proof}

1. Define $\phi(h)=\dfrac{f(g(t)+h)-f(g(t))}{h}$ for $h\neq0$ and $\phi(0)=f'(g(t))$. Then $\phi$ is continuous at $0$, and $f(g(t)+h)-f(g(t))=\phi(h)\,h$ for every $h$, including $h=0$.

2. Put $h=\Delta x=g(t+\Delta t)-g(t)$. Then
$$\frac{f(g(t+\Delta t))-f(g(t))}{\Delta t}=\phi(\Delta x)\,\frac{\Delta x}{\Delta t}.$$

3. As $\Delta t\to0$, $\Delta x\to0$ (since $g$ is continuous), so $\phi(\Delta x)\to f'(g(t))$ and $\Delta x/\Delta t\to g'(t)$.

:::

The function $\phi$ avoids dividing by $\Delta x$, which may be $0$ for some $\Delta t\neq0$.

::: {#exm-chain-rule .example name="Using the chain rule"}

- $\dfrac{d}{dt}\sin(t^2)=\cos(t^2)\cdot2t$.
- $\dfrac{d}{dx}\dfrac1{\cos x}=-\dfrac{1}{\cos^2x}\cdot(-\sin x)=\sec x\tan x$, agreeing with @cor-derivatives-of-tan-sec.
- $\dfrac{d}{dx}\sin(10x)=10\cos(10x)$: speeding up time by $10$ multiplies rates by $10$.

:::

## Higher derivatives

::: {#def-higher-derivatives .definition name="Higher derivatives"}

The second derivative is $f''=(f')'$, also written $\dfrac{d^2y}{dx^2}$; in general $f^{(n)}=\big(f^{(n-1)}\big)'=\dfrac{d^ny}{dx^n}$.

:::

If $s(t)$ is position, $s''(t)$ is acceleration.

::: {#prp-nth-derivative-power .proposition name="Repeated derivatives of $x^n$"}

For $n\ge0$, $\dfrac{d^n}{dx^n}x^n=n!$, and $\dfrac{d^{n+1}}{dx^{n+1}}x^n=0$.

:::

::: {.proof}

1. By induction on $k$, $\dfrac{d^k}{dx^k}x^n=n(n-1)\cdots(n-k+1)\,x^{n-k}$ for $0\le k\le n$: the case $k=0$ is trivial, and differentiating once more multiplies by $n-k$ and lowers the power by one (@thm-power-rule-integer).

2. With $k=n$ this is $n!$, a constant, whose derivative is $0$.

:::
