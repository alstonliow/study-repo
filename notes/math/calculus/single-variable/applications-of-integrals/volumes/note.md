---
title: "Volumes by Slices, Disks and Shells"
sources: [mit1801-21, mit1801-22]
requires: [math/calculus/single-variable/applications-of-integrals/area-between-curves]
aliases: [math/calculus/applications-of-integrals/volumes]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lectures 21 (volume by slices) and 22, in our own wording. Numbers checked in Python. -->

::: {#prp-volume-by-slices .proposition name="Volume by slices"}

If the cross-section of a solid at height $x$ (or position $x$) has area $A(x)$ for $a\le x\le b$, its volume is
$$V=\int_a^bA(x)\,dx .$$

:::

::: {#def-disks-and-shells .definition name="Disks and shells"}

For the solid swept out by rotating the region under $y=f(x)\ge0$, $a\le x\le b$:

- around the $x$-axis, each slice is a disk of radius $f(x)$: $\displaystyle V=\int_a^b\pi f(x)^2\,dx$ (disks);
- around the $y$-axis ($0\le a$), each vertical strip sweeps a thin cylindrical shell of radius $x$, height $f(x)$ and thickness $dx$: $\displaystyle V=\int_a^b2\pi x\,f(x)\,dx$ (shells).

:::

::: {#exm-volume-ball .example name="Volume of a ball"}

Rotating $y=\sqrt{a^2-x^2}$, $-a\le x\le a$, around the $x$-axis: $V=\int_{-a}^a\pi(a^2-x^2)\,dx=\pi\big(2a^3-\tfrac23a^3\big)=\tfrac43\pi a^3$.

:::

::: {#exm-paraboloid-two-ways .example name="A bowl, two ways"}

Rotate the region $x^2\le y\le a$ around the $y$-axis (a paraboloid bowl filled to height $a$).

- Disks (horizontal slices): the slice at height $y$ has radius $\sqrt y$, so $V=\int_0^a\pi y\,dy=\tfrac{\pi a^2}2$.
- Shells: the strip at $x$, $0\le x\le\sqrt a$, has height $a-x^2$, so $V=\int_0^{\sqrt a}2\pi x(a-x^2)\,dx=\pi a^2-\tfrac{\pi a^2}2=\tfrac{\pi a^2}2$.

:::

::: {#exm-pipe-flow .example name="Flow through a pipe"}

In a pipe of radius $R$ the fluid speed at distance $r$ from the axis is $v(r)=c(R^2-r^2)$. The ring between $r$ and $r+dr$ has area $2\pi r\,dr$, so the flow rate is $\int_0^R2\pi r\,c(R^2-r^2)\,dr=\tfrac{\pi cR^4}2$: the shell idea applied to a flux instead of a volume.

:::
