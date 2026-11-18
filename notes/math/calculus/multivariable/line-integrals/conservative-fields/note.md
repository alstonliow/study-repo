---
title: "Gradient Fields, Path Independence and Conservative Fields"
sources: [mit1802-20, mit1802n-V2]
requires: [math/calculus/multivariable/line-integrals/vector-fields-and-line-integrals]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lecture 20 and Supplementary Notes V2, in our own wording. -->

::: {#thm-ftc-line-integrals .theorem name="Fundamental theorem for line integrals"}

If $f$ has continuous partial derivatives and $C$ runs from $P_0$ to $P_1$, then
$$\int_C\nabla f\cdot d\mathbf{r}=\int_Cf_x\,dx+f_y\,dy=f(P_1)-f(P_0).$$
The function $f$ is called a **potential** of the field $\nabla f$.

:::

::: {.proof}

1. Parametrise $C$ by $\mathbf{r}(t)$, $t_0\le t\le t_1$. By the chain rule, $\nabla f\cdot\dfrac{d\mathbf{r}}{dt}=f_x\dfrac{dx}{dt}+f_y\dfrac{dy}{dt}=\dfrac{d}{dt}f(x(t),y(t))$.

2. By the fundamental theorem of calculus (@thm-ftc-1), $\displaystyle\int_{t_0}^{t_1}\frac{d}{dt}f(\mathbf{r}(t))\,dt=f(\mathbf{r}(t_1))-f(\mathbf{r}(t_0))=f(P_1)-f(P_0)$.

:::

In @exm-line-integral-sector the field $\langle y,x\rangle$ is $\nabla(xy)$, so each piece can be computed from the values of $xy$ at its ends, and the closed curve gives $0$.

::: {#def-conservative-field .definition name="Path independent and conservative"}

A field $\mathbf{F}$ on a region is **path independent** if $\int_C\mathbf{F}\cdot d\mathbf{r}$ depends only on the endpoints of $C$, and **conservative** if $\oint_C\mathbf{F}\cdot d\mathbf{r}=0$ for every closed curve $C$ in the region. The expression $M\,dx+N\,dy$ is an **exact differential** if it equals $df$ for some $f$.

:::

::: {#thm-conservative-equivalences .theorem name="Four equivalent properties"}

For a continuous field $\mathbf{F}=\langle M,N\rangle$ on a connected open region, the following are equivalent:

1. $\mathbf{F}$ is conservative;
2. $\int\mathbf{F}\cdot d\mathbf{r}$ is path independent;
3. $\mathbf{F}$ is a gradient field: $\mathbf{F}=\nabla f$ for some $f$;
4. $M\,dx+N\,dy$ is an exact differential.

:::

::: {.proof}

1. (1)$\Leftrightarrow$(2). If $C_1,C_2$ have the same endpoints, $C=C_1-C_2$ (first $C_1$, then $C_2$ backwards) is closed, and $\oint_C=\int_{C_1}-\int_{C_2}$. So the closed-curve integrals all vanish exactly when the integrals along curves with equal endpoints agree.

2. (3)$\Rightarrow$(2) is @thm-ftc-line-integrals.

3. (2)$\Rightarrow$(3). Fix $P_0$ and define $f(P)=\int_{P_0}^P\mathbf{F}\cdot d\mathbf{r}$ along any curve; by (2) this does not depend on the curve. To find $f_x$ at $(x,y)$, reach $(x+h,y)$ by going to $(x,y)$ and then along the horizontal segment: $f(x+h,y)-f(x,y)=\int_x^{x+h}M(t,y)\,dt$, so $f_x=M$ by @thm-ftc-2. In the same way $f_y=N$.

4. (3)$\Leftrightarrow$(4): $\mathbf{F}=\nabla f$ means $M=f_x$, $N=f_y$, i.e. $M\,dx+N\,dy=f_x\,dx+f_y\,dy=df$.

:::

::: {#exm-not-conservative .example name="A field that is not a gradient"}

$\mathbf{F}=-y\,\mathbf{i}+x\,\mathbf{j}$ has work $2\pi a^2\ne0$ around the circle of radius $a$ (@exm-line-integral-circle-geometric). So it is not conservative, hence not a gradient field.

:::

::: {#rmk-conservative-fields-1 .remark name="Physics"}

If a force field is the gradient of a potential, its work along a path is the change of potential: no energy can be gained by moving around a closed path. This is conservation of energy, since the work also equals the change in kinetic energy. Gravitational and electrostatic fields are of this kind (physicists write $\mathbf{F}=-\nabla f$, with the opposite sign).

:::
