---
title: "Related Rates"
sources: [mit1801-12]
requires: [math/calculus/differentiation/implicit-differentiation]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lecture 12, in our own wording. Numbers checked in Python. -->

::: {#def-related-rates .definition name="Related rates"}

If quantities $x(t),y(t),\dots$ satisfy an equation for all $t$, differentiating the equation with respect to $t$ (implicit differentiation, @thm-derivative-chain-rule) gives an equation between their rates $x'(t),y'(t),\dots$. Substitute the values at the moment of interest only **after** differentiating.

:::

::: {#exm-police-radar .example name="Police radar"}

A police car is parked $30$ ft from a straight road. A car on the road is $50$ ft from the radar and the distance is decreasing at $80$ ft/s. Let $x$ be the car's distance along the road from the point nearest the police and $D$ its distance from them, so $x^2+30^2=D^2$. Differentiating, $2xx'=2DD'$. At this moment $D=50$, $x=40$ and $D'=-80$, so $x'=\dfrac{50\cdot(-80)}{40}=-100$ ft/s: the car's speed is $100$ ft/s (about $68$ mph).

:::

::: {#exm-conical-tank .example name="Filling a conical tank"}

A cone, vertex down, has top radius $4$ ft and height $10$ ft; water flows in at $2$ ft³/min. With water depth $h$ the surface radius is $r=\tfrac25h$, so the water volume is $V=\tfrac13\pi r^2h=\tfrac{4\pi}{75}h^3$. Then $V'=\tfrac{4\pi}{25}h^2h'$. At $h=5$: $2=4\pi h'$, so $h'=\tfrac1{2\pi}\approx0.159$ ft/min.

:::

::: {#rmk-related-rates-1 .remark name="Why substitute late"}

At the moment of interest $D=50$ is a value, not a constant: $D$ is changing. Substituting it before differentiating would make $D'=0$ and give a wrong answer.

:::
