---
title: "Maximum and Minimum Problems"
sources: [mit1801-11]
requires: [math/calculus/single-variable/applications-of-derivatives/curve-sketching]
aliases: [math/calculus/applications-of-derivatives/optimization]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lecture 11, in our own wording; proofs written out in steps. Numbers checked in Python. -->

::: {#thm-closed-interval-method .theorem name="Where extreme values occur"}

If $f$ is continuous on $[a,b]$, its largest and smallest values on $[a,b]$ occur at critical points, at points where $f'$ does not exist, or at the endpoints $a,b$.

:::

::: {.proof}

1. The extreme values exist by @thm-extreme-value.

2. Suppose the maximum occurs at an interior point $c$ where $f'(c)$ exists. For $h>0$ small, $f(c+h)-f(c)\le0$, so $\frac{f(c+h)-f(c)}h\le0$ and, letting $h\to0^+$, $f'(c)\le0$.

3. For $h<0$ the quotient is $\ge0$, so $f'(c)\ge0$. Hence $f'(c)=0$. The minimum is the same with signs reversed.

:::

So: list the candidates, evaluate $f$ at each, and compare. On an open or infinite interval, compare instead with the limits at the ends.

::: {#exm-open-can .example name="The open can"}

An open-topped cylindrical can has fixed volume $V=\pi r^2h$ and area $A=\pi r^2+2\pi rh$. Eliminating $h$, $A(r)=\pi r^2+2V/r$ for $r>0$. Then $A'(r)=2\pi r-2V/r^2=0$ gives $r^3=V/\pi$, and so $\pi r^3=V=\pi r^2h$, i.e. $h=r$. Since $A\to\infty$ as $r\to0^+$ and as $r\to\infty$, this critical point is the minimum: the best can is as tall as its radius.

:::

::: {#exm-wire-two-squares .example name="Cutting a wire into two squares"}

A wire of length $1$ is cut at $x$ and each piece bent into a square: total area $A(x)=\big(\tfrac x4\big)^2+\big(\tfrac{1-x}4\big)^2$ on $[0,1]$. $A'(x)=\tfrac{x-(1-x)}8=0$ at $x=\tfrac12$, where $A=\tfrac1{32}$; at the endpoints $A=\tfrac1{16}$. So the minimum is at the middle and the maximum is at the endpoints (do not cut at all).

:::

::: {#rmk-optimization-1 .remark name="Recipe"}

Draw a picture, name the variables, write the quantity to optimize, use the constraint to reduce it to one variable, find the candidates, and check endpoints or behaviour at the ends before deciding.

:::
