---
title: "Flux and the Normal Form of Green's Theorem"
sources: [mit1802-23, mit1802n-V3, mit1802n-V4]
requires: [math/calculus/multivariable/line-integrals/greens-theorem]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lecture 23 and Supplementary Notes V3, V4, in our own wording. Numbers checked in Python (sympy). -->

::: {#def-flux-plane .definition name="Flux across a plane curve"}

Let $C$ be a curve with unit tangent $\hat{\mathbf{T}}$ (in its direction of travel), and let $\hat{\mathbf{n}}$ be $\hat{\mathbf{T}}$ turned $90^\circ$ clockwise, i.e. pointing to the right of the direction of travel. The **flux** of $\mathbf{F}$ across $C$ is
$$\int_C\mathbf{F}\cdot\hat{\mathbf{n}}\,ds .$$

:::

Work adds up the component of $\mathbf{F}$ along $C$; flux adds up the component across $C$.

::: {#rmk-flux-and-normal-form-of-greens-theorem-1 .remark name="Flux as flow"}

Let $\mathbf{F}$ be the velocity field of a fluid in the plane. In unit time, the fluid that crosses a short piece of $C$ of length $\Delta s$ fills a parallelogram with sides $\Delta s$ (along $C$) and $\mathbf{F}$, whose area is $\Delta s$ times the height $\mathbf{F}\cdot\hat{\mathbf{n}}$. So the flux is the amount of fluid crossing $C$ per unit time, counted positively from left to right as seen travelling along $C$.

:::

::: {#prp-flux-components .proposition name="Flux in components"}

If $\mathbf{F}=P\,\mathbf{i}+Q\,\mathbf{j}$, then
$$\int_C\mathbf{F}\cdot\hat{\mathbf{n}}\,ds=\int_C-Q\,dx+P\,dy .$$

:::

::: {.proof}

1. $\hat{\mathbf{T}}\,ds=d\mathbf{r}=\langle dx,dy\rangle$; turning by $90^\circ$ clockwise sends $\langle a,b\rangle$ to $\langle b,-a\rangle$, so $\hat{\mathbf{n}}\,ds=\langle dy,-dx\rangle$.

2. Hence $\mathbf{F}\cdot\hat{\mathbf{n}}\,ds=P\,dy-Q\,dx$.

:::

::: {#exm-flux-circle .example name="Flux across a circle"}

$C$ the circle of radius $a$ about the origin, counterclockwise, so $\hat{\mathbf{n}}$ points outwards.

- $\mathbf{F}=x\,\mathbf{i}+y\,\mathbf{j}$ is parallel to $\hat{\mathbf{n}}$ with length $a$: flux $=a\cdot2\pi a=2\pi a^2$.
- $\mathbf{F}=-y\,\mathbf{i}+x\,\mathbf{j}$ is tangent to $C$: flux $0$.

:::

::: {#def-divergence-plane .definition name="Divergence in the plane"}

The **divergence** of $\mathbf{F}=P\,\mathbf{i}+Q\,\mathbf{j}$ is $\operatorname{div}\mathbf{F}=P_x+Q_y$.

:::

::: {#thm-greens-theorem-normal-form .theorem name="Green's theorem for flux"}

If $C$ is a positively oriented closed curve bounding $R$ (so $\hat{\mathbf{n}}$ points out of $R$) and $\mathbf{F}=P\,\mathbf{i}+Q\,\mathbf{j}$ has continuous partial derivatives on $R$, then
$$\oint_C\mathbf{F}\cdot\hat{\mathbf{n}}\,ds=\iint_R\operatorname{div}\mathbf{F}\,dA .$$

:::

::: {.proof}

1. By @prp-flux-components the left side is $\oint_CM\,dx+N\,dy$ with $M=-Q$ and $N=P$.

2. By Green's theorem (@thm-greens-theorem) it equals $\iint_R(N_x-M_y)\,dA=\iint_R(P_x+Q_y)\,dA$.

:::

In @exm-flux-circle, $\operatorname{div}(x\,\mathbf{i}+y\,\mathbf{j})=2$ and the flux is $2\cdot\pi a^2$, as found. The flux of this field out of any circle of radius $a$, centred anywhere, is therefore also $2\pi a^2$, although direct computation would be harder.

::: {#rmk-flux-and-normal-form-of-greens-theorem-2 .remark name="What divergence measures"}

For the flow of an incompressible fluid, the flux out of $R$ is the fluid created inside $R$ per unit time. Dividing by the area and shrinking $R$ to a point shows that $\operatorname{div}\mathbf{F}$ is the **source rate**: fluid added per unit area per unit time (negative at a sink).

:::
