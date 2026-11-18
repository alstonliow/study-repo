---
title: "Continuity"
sources: [mit1801-2, mit1801n-C]
requires: [math/calculus/limits/limits-of-functions]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lecture 2 and Supplementary Notes C, in our own wording; proofs written out in steps. -->

::: {#def-continuity .definition name="Continuity"}

$f$ is continuous at $a$ if
$$\lim_{x\to a}f(x)=f(a).$$
$f$ is continuous on an interval if it is continuous at every point of it (using one-sided limits at endpoints).

:::

The definition asks for three things: $f(a)$ is defined, the limit exists, and the two agree. Each way of failing gives a kind of discontinuity.

::: {#def-kinds-of-discontinuity .definition name="Kinds of discontinuity"}

At a point $a$ where $f$ is not continuous:

- a **removable** discontinuity: $\lim_{x\to a}f(x)$ exists but is not $f(a)$ (or $f(a)$ is undefined);
- a **jump** discontinuity: both one-sided limits exist but differ;
- an **infinite** discontinuity: $f(x)\to\pm\infty$ from at least one side;
- otherwise (for example $\sin(1/x)$ at $0$, which oscillates) the discontinuity is called **essential** or oscillating.

:::

::: {#exm-discontinuities .example name="Four discontinuities at $0$"}

$\frac{\sin x}{x}$ (undefined at $0$, limit $1$) is removable; $x/\lvert x\rvert$ is a jump; $1/x^2$ is infinite; $\sin(1/x)$ takes every value in $[-1,1]$ on every interval $(0,\delta)$, so it has no one-sided limit.

:::

::: {#prp-continuity-algebra .proposition name="Combining continuous functions"}

Sums, products and quotients (where the denominator is not $0$) of functions continuous at $a$ are continuous at $a$. If $g$ is continuous at $a$ and $f$ is continuous at $g(a)$, then $f\circ g$ is continuous at $a$.

:::

::: {.proof}

1. The first part is @prp-limit-laws-functions with $L=f(a)$, $M=g(a)$.

2. For the composition, let $\varepsilon>0$. Continuity of $f$ at $b=g(a)$ gives $\eta>0$ with $\lvert y-b\rvert<\eta\Rightarrow\lvert f(y)-f(b)\rvert<\varepsilon$.

3. Continuity of $g$ at $a$ gives $\delta>0$ with $\lvert x-a\rvert<\delta\Rightarrow\lvert g(x)-b\rvert<\eta$. Chaining the two, $\lvert f(g(x))-f(g(a))\rvert<\varepsilon$.

:::

::: {#thm-intermediate-value .theorem name="Intermediate value theorem"}

If $f$ is continuous on $[a,b]$ and $y$ lies between $f(a)$ and $f(b)$, then $f(c)=y$ for some $c\in[a,b]$.

:::

::: {#thm-extreme-value .theorem name="Extreme value theorem"}

A function continuous on a closed bounded interval $[a,b]$ attains a largest and a smallest value there.

:::

Both theorems depend on the completeness of $\mathbb R$; we use them without proof. Both fail without continuity ($1/x$ on $[-1,1]$) or, for the second, on open intervals ($x$ on $(0,1)$ has no maximum).

::: {#exm-ivt-root .example name="Locating a root"}

$p(x)=x^3-x-1$ has $p(1)=-1<0<5=p(2)$, so by @thm-intermediate-value it has a root in $(1,2)$; halving the interval repeatedly (bisection) pins it down to $1.3247\ldots$.

:::
