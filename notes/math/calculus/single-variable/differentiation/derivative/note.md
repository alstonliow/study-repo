---
title: "The Derivative"
sources: [mit1801-1, mit1801-2]
requires: [math/calculus/single-variable/limits/continuity]
aliases: [math/calculus/differentiation/derivative]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lectures 1 and 2, in our own wording; proofs written out in steps. Numbers checked in Python. -->

## Slope of the tangent line

A secant line through $(x_0,f(x_0))$ and $(x_0+\Delta x,f(x_0+\Delta x))$ has slope $\Delta f/\Delta x$. As $\Delta x\to0$ the secant turns into the tangent line.

::: {#def-derivative .definition name="Derivative"}

The derivative of $f$ at $x_0$ is
$$f'(x_0)=\lim_{\Delta x\to0}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x},$$
when the limit exists; $f$ is then differentiable at $x_0$. The tangent line at $x_0$ is $y=f(x_0)+f'(x_0)(x-x_0)$.

:::

::: {#fig-derivative-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.3,0) -- (3.2,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.3) -- (0,3.4) node[lab, above] {$y$};
\draw[emph, domain=-0.2:2.6, samples=50] plot (\x,{\x*\x/2});
\draw[faint, dashed] (1.0,0.5) -- (2.4,0.5) node[lab, midway, below] {$\Delta x$} -- (2.4,2.88) node[lab, midway, left] {$\Delta f$};
\draw[faint] (0.4,-0.52) -- (2.8,3.56) node[lab, right] {secant};
\draw[hl] (0.10,-0.4) -- (2.5,2.0) node[lab, below right] {tangent};
\fill (1.0,0.5) circle (1.5pt) node[lab, above left] {$P$};
\fill (2.4,2.88) circle (1.5pt) node[lab, left] {$Q$};
\end{tikzpicture}
\end{center}
```

As $Q$ approaches $P$ ($\Delta x\to0$), the secant $PQ$ turns into the tangent at $P$; its slope $\Delta f/\Delta x$ tends to $f'(x_0)$. Here $f(x)=x^2/2$ at $x_0=1$.

:::

Other notations, with $y=f(x)$: $f'=\dfrac{dy}{dx}=\dfrac{df}{dx}=\dfrac{d}{dx}f=Df$.

::: {#exm-derivative-reciprocal .example name="Tangent lines to $y=1/x$"}

$$\frac{\Delta f}{\Delta x}=\frac{1}{\Delta x}\Big(\frac1{x_0+\Delta x}-\frac1{x_0}\Big)=\frac{-1}{x_0(x_0+\Delta x)}\to-\frac1{x_0^2}.$$
The tangent at $x_0$ is $y=\frac1{x_0}-\frac1{x_0^2}(x-x_0)$. It meets the axes at $x=2x_0$ and $y=2/x_0$, so the triangle it cuts from the first quadrant always has area $\frac12\cdot2x_0\cdot\frac2{x_0}=2$.

:::

::: {#thm-power-rule-integer .theorem name="Power rule for positive integers"}

For $n=1,2,3,\dots$,
$$\frac{d}{dx}x^n=nx^{n-1}.$$

:::

::: {.proof}

1. By the binomial theorem, $(x+\Delta x)^n=x^n+nx^{n-1}\Delta x+(\Delta x)^2\cdot(\text{polynomial in }x,\Delta x)$.

2. Hence $\dfrac{(x+\Delta x)^n-x^n}{\Delta x}=nx^{n-1}+\Delta x\cdot(\text{polynomial})$.

3. The last term tends to $0$ as $\Delta x\to0$, leaving $nx^{n-1}$.

:::

## Rate of change

If $s(t)$ is position at time $t$, then $\Delta s/\Delta t$ is the average velocity over $[t,t+\Delta t]$ and $s'(t)$ is the instantaneous velocity. In general $f'(x)$ is the rate of change of $f$ with respect to $x$: temperature gradient, marginal cost, sensitivity of a measurement.

::: {#exm-falling-object .example name="A falling object"}

An object dropped from height $80$ m has height $h(t)=80-5t^2$ (with $g\approx10$ m/s²). It lands when $t=4$; its average speed over the fall is $80/4=20$ m/s, but its speed on landing is $\lvert h'(4)\rvert=10\cdot4=40$ m/s.

:::

## Differentiable implies continuous

::: {#thm-differentiable-continuous .theorem name="Differentiable implies continuous"}

If $f$ is differentiable at $x_0$, then $f$ is continuous at $x_0$.

:::

::: {.proof}

1. For $x\neq x_0$, $f(x)-f(x_0)=\dfrac{f(x)-f(x_0)}{x-x_0}\,(x-x_0)$.

2. As $x\to x_0$ the first factor tends to $f'(x_0)$ and the second to $0$, so the product tends to $f'(x_0)\cdot0=0$.

3. Thus $\lim_{x\to x_0}f(x)=f(x_0)$.

:::

The converse is false: $\lvert x\rvert$ is continuous at $0$ but its difference quotient is $+1$ to the right and $-1$ to the left, so it has no derivative there.
