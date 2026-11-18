---
title: "Partial Derivatives with Non-Independent Variables"
sources: [mit1802-14, mit1802-15, mit1802n-N]
requires: [math/calculus/multivariable/differentiation/differentials-and-chain-rule]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lectures 14-15 and Supplementary Notes N, in our own wording. Numbers checked in Python (sympy). -->

Often the variables are tied by an equation, like pressure, volume and temperature in $PV=nRT$. Then "the partial derivative with respect to $x$" is ambiguous until we say which other variables are held fixed.

::: {#prp-implicit-partial-derivatives .proposition name="Implicit partial derivatives"}

If $g(x,y,z)=c$ defines $z$ as a function of $x$ and $y$ near a point where $g_z\ne0$, then
$$\frac{\partial z}{\partial x}=-\frac{g_x}{g_z},\qquad\frac{\partial z}{\partial y}=-\frac{g_y}{g_z}.$$

:::

::: {.proof}

1. Along the surface $g=c$ the differential vanishes: $g_x\,dx+g_y\,dy+g_z\,dz=0$.

2. Solve for $dz$: $dz=-\dfrac{g_x}{g_z}dx-\dfrac{g_y}{g_z}dy$. The coefficients of $dx$ and $dy$ are the partial derivatives. (Equivalently: hold $y$ fixed, i.e. put $dy=0$.)

:::

::: {#exm-implicit-partial-derivatives .example name="A surface through $(2,3,1)$"}

$x^2+yz+z^3=8$ at $(2,3,1)$: $2x\,dx+z\,dy+(y+3z^2)\,dz=0$ becomes $4\,dx+dy+6\,dz=0$, so $\dfrac{\partial z}{\partial x}=-\dfrac23$ and $\dfrac{\partial z}{\partial y}=-\dfrac16$.

:::

::: {#def-partial-derivative-held-fixed .definition name="Which variable is held fixed"}

$\left(\dfrac{\partial f}{\partial x}\right)_{y}$ is the rate of change of $f$ when $x$ varies and $y$ is held fixed, the remaining variables changing as the constraints require. Without a subscript, $\partial f/\partial x$ means that the other variables of the original list are held fixed.

:::

::: {#exm-held-fixed-matters .example name="Same variable, different derivatives"}

$f=x+y$ has $\left(\frac{\partial f}{\partial x}\right)_y=1$. Change variables to $u=x$, $v=y-x$: then $f=2u+v$ and $\left(\frac{\partial f}{\partial u}\right)_v=2$, although $u=x$. The second derivative moves $x$ while keeping $y-x$ fixed: it is $\left(\frac{\partial f}{\partial x}\right)_v$, not $\left(\frac{\partial f}{\partial x}\right)_y$.

:::

::: {#prp-constrained-partial-methods .proposition name="Computing a constrained partial derivative"}

Let $w=f(x,y,z)$ with the constraint $g(x,y,z)=c$. To find $\left(\frac{\partial w}{\partial z}\right)_y$:

1. **Differentials.** Write $dw=f_x\,dx+f_y\,dy+f_z\,dz$ and $0=g_x\,dx+g_y\,dy+g_z\,dz$. Put $dy=0$ and eliminate $dx$; the coefficient of $dz$ is the answer:
$$\left(\frac{\partial w}{\partial z}\right)_y=f_z-\frac{f_xg_z}{g_x}.$$
2. **Chain rule.** $\left(\frac{\partial w}{\partial z}\right)_y=f_x\left(\frac{\partial x}{\partial z}\right)_y+f_z$, and differentiating the constraint, $0=g_x\left(\frac{\partial x}{\partial z}\right)_y+g_z$, gives $\left(\frac{\partial x}{\partial z}\right)_y=-g_z/g_x$.

Both methods compute the same quantities (assume $g_x\ne0$).

:::

::: {#exm-right-triangle-area .example name="Area of a right triangle"}

A triangle with sides $a,b$ enclosing the angle $\theta$ has area $A=\frac12ab\sin\theta$. Make it a right triangle with hypotenuse $b$: constraint $a=b\cos\theta$.

- $\dfrac{\partial A}{\partial\theta}=\frac12ab\cos\theta$, with $a,b$ fixed (the triangle stops being right-angled).
- $\left(\dfrac{\partial A}{\partial\theta}\right)_a$: substitute $b=a\sec\theta$, $A=\frac12a^2\tan\theta$, so $\left(\frac{\partial A}{\partial\theta}\right)_a=\frac12a^2\sec^2\theta$.
- By differentials: $da=0$ and $da=\cos\theta\,db-b\sin\theta\,d\theta$ give $db=b\tan\theta\,d\theta$; then $dA=\frac12ab\cos\theta\,d\theta+\frac12a\sin\theta\,db=\big(\frac12ab\cos\theta+\frac12ab\sin\theta\tan\theta\big)d\theta=\frac12ab\sec\theta\,d\theta$. With $b=a\sec\theta$ this is $\frac12a^2\sec^2\theta$ again.

:::
