---
title: "Average Value, Probability and Work"
sources: [mit1801-23, mit1801n-AV]
requires: [math/calculus/applications-of-integrals/volumes]
relations:
  related: [math/probability/continuous/continuous-random-variables]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lecture 23 and Supplementary Notes AV, in our own wording. Numbers checked in Python. -->

::: {#def-average-value .definition name="Average value"}

The average value of $f$ on $[a,b]$ is
$$\operatorname{Ave}(f)=\frac1{b-a}\int_a^bf(x)\,dx ,$$
the limit of the averages $\frac1n\sum f(x_i)$ of $n$ equally spaced samples. A weighted average with weight $w\ge0$ is $\dfrac{\int_a^bf\,w\,dx}{\int_a^bw\,dx}$.

:::

::: {#thm-mean-value-integrals .theorem name="Mean value theorem for integrals"}

If $f$ is continuous on $[a,b]$, then $\operatorname{Ave}(f)=f(c)$ for some $c\in[a,b]$.

:::

::: {.proof}

1. With $m\le f\le M$ (smallest and largest values, @thm-extreme-value), @prp-integral-properties gives $m\le\operatorname{Ave}(f)\le M$.

2. By @thm-intermediate-value, $f$ takes the value $\operatorname{Ave}(f)$ somewhere.

:::

::: {#exm-average-semicircle .example name="Average height of a semicircle"}

Over $-1\le x\le1$, the average of $\sqrt{1-x^2}$ is $\frac12\cdot\frac\pi2=\frac\pi4\approx0.785$. Averaged instead over the angle $\theta\in[0,\pi]$ (equally spaced along the arc), the average of $\sin\theta$ is $\frac1\pi\int_0^\pi\sin\theta\,d\theta=\frac2\pi\approx0.637$: the answer depends on what is spread evenly.

:::

## Probability

If a point is chosen in a region "uniformly", the probability of landing in a part is $\dfrac{\text{area of the part}}{\text{area of the whole}}$; with a non-uniform weight $w$ it is $\int_{\text{part}}w/\int_{\text{whole}}w$. This is the continuous probability of @def-probability-density.

::: {#exm-dart-board .example name="A dart board"}

If darts land with density proportional to $e^{-r^2}$ in the plane ($r$ the distance from the centre), the chance of landing within distance $1$ is $\dfrac{\int_0^1e^{-r^2}2\pi r\,dr}{\int_0^\infty e^{-r^2}2\pi r\,dr}=1-e^{-1}\approx0.632$, using rings as in @exm-pipe-flow.

:::

## Work

::: {#def-work .definition name="Work"}

The work done by a force $F(x)$ moving an object along $a\le x\le b$ is $W=\int_a^bF(x)\,dx$.

:::

::: {#exm-work-spring .example name="Stretching a spring"}

A spring obeying $F(x)=kx$ needs work $\int_0^Lkx\,dx=\tfrac12kL^2$ to stretch by $L$.

:::
