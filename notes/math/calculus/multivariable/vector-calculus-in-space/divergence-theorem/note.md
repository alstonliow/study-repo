---
title: "The Divergence Theorem"
sources: [mit1802-28, mit1802-29, mit1802-30, mit1802n-V10]
requires: [math/calculus/multivariable/vector-calculus-in-space/surface-integrals-and-flux, math/calculus/multivariable/differentiation/partial-differential-equations]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lectures 28-30 and Supplementary Notes V10, in our own wording. Numbers checked in Python (sympy). -->

::: {#def-divergence-space .definition name="Divergence and the del operator"}

The **del operator** is the symbolic vector $\nabla=\Big\langle\dfrac{\partial}{\partial x},\dfrac{\partial}{\partial y},\dfrac{\partial}{\partial z}\Big\rangle$. Applied to a function it gives the gradient $\nabla f$; dotted with $\mathbf{F}=\langle P,Q,R\rangle$ it gives the **divergence**
$$\operatorname{div}\mathbf{F}=\nabla\cdot\mathbf{F}=P_x+Q_y+R_z .$$

:::

::: {#thm-divergence-theorem .theorem name="Divergence theorem (Gauss–Green)"}

Let $S$ be a closed surface bounding the solid $D$, with outward normal, and let $\mathbf{F}$ have continuous partial derivatives on all of $D$. Then
$$\iint_S\mathbf{F}\cdot\hat{\mathbf{n}}\,dS=\iiint_D\operatorname{div}\mathbf{F}\,dV .$$

:::

::: {.proof}

1. Both sides split into three terms, one for each of $P\mathbf{i}$, $Q\mathbf{j}$, $R\mathbf{k}$. We prove $\iint_SR\,\mathbf{k}\cdot d\mathbf{S}=\iiint_DR_z\,dV$; the other two are the same with the axes exchanged.

2. **Vertically simple solids.** Let $D$ be $z_1(x,y)\le z\le z_2(x,y)$ over a region $U$ of the $xy$-plane. Then
$$\iiint_DR_z\,dV=\iint_U\int_{z_1}^{z_2}R_z\,dz\,dx\,dy=\iint_U\big(R(x,y,z_2)-R(x,y,z_1)\big)dx\,dy .$$

3. On the top surface $z=z_2(x,y)$ the outward normal points up: $d\mathbf{S}=\langle-z_{2,x},-z_{2,y},1\rangle\,dx\,dy$ (@prp-normal-and-surface-element), so $R\,\mathbf{k}\cdot d\mathbf{S}=R(x,y,z_2)\,dx\,dy$. On the bottom it points down: $R\,\mathbf{k}\cdot d\mathbf{S}=-R(x,y,z_1)\,dx\,dy$. On vertical sides $\hat{\mathbf{n}}$ is horizontal and $R\,\mathbf{k}\cdot\hat{\mathbf{n}}=0$. The flux equals the expression in step 2.

4. **General solids.** Cut $D$ into vertically simple pieces. Volume integrals add up. On an internal cut the two adjacent pieces have opposite outward normals, so their fluxes cancel, and the fluxes add up to the flux through $S$.

:::

::: {#exm-divergence-sphere .example name="Checking on the sphere"}

$\mathbf{F}=z\,\mathbf{k}$ has $\operatorname{div}\mathbf{F}=1$, so the flux out of the sphere of radius $a$ is the volume $\frac43\pi a^3$, as computed in @exm-flux-sphere. For $\langle x,y,z\rangle$, $\operatorname{div}=3$ and the flux is $3\cdot\frac43\pi a^3=4\pi a^3$.

:::

::: {#rmk-divergence-theorem-1 .remark name="Divergence as source rate"}

For an incompressible fluid with velocity $\mathbf{F}$, the flux out of $D$ is the net amount leaving $D$ per unit time, which must equal the amount produced inside. Dividing by the volume of $D$ and shrinking $D$ to a point, $\operatorname{div}\mathbf{F}$ is the source rate: the flux generated per unit volume.

:::

::: {#thm-diffusion-equation .theorem name="The diffusion equation"}

Let $u(x,y,z,t)$ be the concentration of a substance (or the temperature) and $\mathbf{F}$ its flow. If $\mathbf{F}=-k\nabla u$ with a constant $k>0$ (flow from high to low concentration, faster where $u$ changes faster) and the substance is neither created nor destroyed, then
$$\frac{\partial u}{\partial t}=k\nabla^2u=k\big(u_{xx}+u_{yy}+u_{zz}\big).$$

:::

::: {.proof}

1. For any solid $D$ with boundary $S$, the flux out of $D$ is the rate at which the amount inside decreases: $\iint_S\mathbf{F}\cdot\hat{\mathbf{n}}\,dS=-\dfrac{d}{dt}\iiint_Du\,dV=-\iiint_D\dfrac{\partial u}{\partial t}dV$ (differentiating under the integral sign, i.e. summing the derivatives of the terms $u\,\Delta V$).

2. By the divergence theorem the left side is $\iiint_D\operatorname{div}\mathbf{F}\,dV$. So $\operatorname{div}\mathbf{F}$ and $-\partial u/\partial t$ have the same average over every solid; shrinking $D$ to a point, $\dfrac{\partial u}{\partial t}=-\operatorname{div}\mathbf{F}$.

3. With $\mathbf{F}=-k\nabla u$: $\dfrac{\partial u}{\partial t}=k\operatorname{div}(\nabla u)=k(u_{xx}+u_{yy}+u_{zz})$, the heat equation of @def-classical-pdes.

:::
