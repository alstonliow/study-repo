---
title: "Linear and Quadratic Approximation"
sources: [mit1801-9, mit1801-15]
requires: [math/calculus/differentiation/exponentials-and-logarithms]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lecture 9 and the differentials part of Lecture 15, in our own wording. Numbers checked in Python. -->

::: {#def-linear-approximation .definition name="Linear approximation"}

Near a base point $x_0$,
$$f(x)\approx f(x_0)+f'(x_0)(x-x_0).$$
The right side is the tangent line; it is the best straight-line fit to $f$ at $x_0$.

:::

The same statement in increments: $\Delta f\approx f'(x_0)\,\Delta x$, i.e. $\Delta f/\Delta x\approx f'(x_0)$, which is the definition of the derivative read backwards. In differential notation, $dy=f'(x)\,dx$.

::: {#prp-standard-linear-approximations .proposition name="Standard approximations near $0$"}

For $x$ near $0$ and any real $r$:
$$\sin x\approx x,\quad \cos x\approx1,\quad e^x\approx1+x,\quad \ln(1+x)\approx x,\quad (1+x)^r\approx1+rx .$$

:::

::: {.proof}

1. Each follows from @def-linear-approximation with $x_0=0$, using $f(0)$ and $f'(0)$: for example $f(x)=(1+x)^r$ has $f(0)=1$ and $f'(0)=r$; $f(x)=\ln(1+x)$ has $f(0)=0$ and $f'(0)=1$.

:::

::: {#exm-linear-approximation-combined .example name="Combining approximations"}

For small $x$, $\dfrac{e^{-3x}}{\sqrt{1+x}}\approx(1-3x)(1-\tfrac12x)\approx1-\tfrac72x$, dropping the $x^2$ term. At $x=0.01$: exact $0.96563\ldots$, approximation $0.965$.

:::

::: {#def-quadratic-approximation .definition name="Quadratic approximation"}

$$f(x)\approx f(x_0)+f'(x_0)(x-x_0)+\frac{f''(x_0)}{2}(x-x_0)^2 .$$

:::

The coefficient $\frac12 f''(x_0)$ is chosen so that the right side has the same value, first and second derivative as $f$ at $x_0$.

::: {#prp-standard-quadratic-approximations .proposition name="Quadratic approximations near $0$"}

$$\sin x\approx x,\quad \cos x\approx1-\tfrac{x^2}2,\quad e^x\approx1+x+\tfrac{x^2}2,\quad \ln(1+x)\approx x-\tfrac{x^2}2,\quad (1+x)^r\approx1+rx+\tfrac{r(r-1)}2x^2 .$$

:::

::: {#exm-quadratic-approximation .example name="Square roots"}

$\sqrt{1.1}=1.04881\ldots$; the linear approximation gives $1.05$ and the quadratic one $1+0.05-0.00125=1.04875$. The error drops from about $10^{-3}$ to about $6\times10^{-5}$: it is roughly proportional to $(\Delta x)^2$ and $(\Delta x)^3$ respectively.

:::

::: {#exm-cube-root-differential .example name="Using differentials"}

To estimate $65^{1/3}$, use $f(x)=x^{1/3}$ at $x_0=64$: $dy=\tfrac13x_0^{-2/3}dx=\tfrac1{48}$, so $65^{1/3}\approx4+\tfrac1{48}=4.0208$ (exact $4.0207\ldots$).

:::
