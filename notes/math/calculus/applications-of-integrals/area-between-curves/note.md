---
title: "Area Between Curves"
sources: [mit1801-21]
requires: [math/calculus/integrals/fundamental-theorem]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lecture 21, in our own wording. Numbers checked in Python. -->

::: {#prp-area-between-curves .proposition name="Area between two graphs"}

If $f(x)\ge g(x)$ on $[a,b]$, the area of the region between their graphs is
$$\int_a^b\big(f(x)-g(x)\big)\,dx .$$
If the region is bounded on the right by $x=f_2(y)$ and on the left by $x=f_1(y)$ for $c\le y\le d$, its area is $\int_c^d\big(f_2(y)-f_1(y)\big)\,dy$.

:::

The integrand is the length of a thin strip (top minus bottom, or right minus left); the integral adds up the strips (@def-riemann-sum).

::: {#exm-area-parabola-line .example name="A parabola and a line"}

The curves $x=y^2$ and $y=x-2$ meet where $y^2=y+2$, i.e. $y=-1$ and $y=2$. Using horizontal strips, the right boundary is $x=y+2$ and the left is $x=y^2$:
$$\int_{-1}^2(y+2-y^2)\,dy=\Big[\tfrac{y^2}2+2y-\tfrac{y^3}3\Big]_{-1}^2=\tfrac{10}3+\tfrac76=\tfrac92 .$$
Vertical strips would need two integrals, since the lower boundary changes at $x=1$.

:::

::: {#rmk-area-between-curves-1 .remark name="Choosing the strips"}

Choose the direction of the strips so that each strip runs between the same two curves throughout; otherwise split the region where the boundary changes.

:::
