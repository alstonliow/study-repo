---
title: "Change of Variables and the Jacobian"
sources: [mit1802-18, mit1802n-CV]
requires: [math/calculus/multivariable/multiple-integrals/polar-double-integrals]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lecture 18 and Supplementary Notes CV, in our own wording. Numbers checked in Python (sympy). -->

::: {#exm-ellipse-area-substitution .example name="Area of an ellipse"}

With $u=x/a$, $v=y/b$ we have $du=dx/a$, $dv=dy/b$, so $dx\,dy=ab\,du\,dv$ and
$$\iint_{(x/a)^2+(y/b)^2\le1}dx\,dy=ab\iint_{u^2+v^2\le1}du\,dv=\pi ab .$$

:::

In general we need the factor relating $du\,dv$ and $dx\,dy$.

::: {#def-jacobian .definition name="Jacobian"}

For a change of variables $u=u(x,y)$, $v=v(x,y)$, the **Jacobian** is the determinant
$$\frac{\partial(u,v)}{\partial(x,y)}=\begin{vmatrix}u_x&u_y\\v_x&v_y\end{vmatrix}.$$
For three variables it is the $3\times3$ determinant of the partial derivatives of $u,v,w$ with respect to $x,y,z$.

:::

::: {#thm-change-of-variables .theorem name="Change of variables in a double integral"}

If $(x,y)\mapsto(u,v)$ maps the region $R$ one-to-one onto the region $G$, with continuous partial derivatives and non-zero Jacobian, then
$$du\,dv=\left\lvert\frac{\partial(u,v)}{\partial(x,y)}\right\rvert dx\,dy,\qquad
\iint_Rf\,dx\,dy=\iint_Gf\,\left\lvert\frac{\partial(x,y)}{\partial(u,v)}\right\rvert du\,dv,$$
where $\frac{\partial(x,y)}{\partial(u,v)}=1\Big/\frac{\partial(u,v)}{\partial(x,y)}$ and $f$ is written in terms of $u,v$.

:::

::: {.proof}

1. (Sketch.) Take a small rectangle with sides $\Delta x,\Delta y$ at $(x,y)$. By linear approximation, $\Delta u\approx u_x\Delta x+u_y\Delta y$ and $\Delta v\approx v_x\Delta x+v_y\Delta y$: in the $uv$-plane the rectangle becomes nearly the parallelogram with sides $\langle u_x,v_x\rangle\Delta x$ and $\langle u_y,v_y\rangle\Delta y$.

2. Its area is $\lvert\det\rvert\,\Delta x\Delta y=\left\lvert\frac{\partial(u,v)}{\partial(x,y)}\right\rvert\Delta x\Delta y$ (@thm-plane-determinant-area). Absolute value, because an area is positive.

3. Summing $f\,\Delta A$ over the pieces in either plane and passing to the limit gives the formula. The two Jacobians are reciprocal because the matrices of partial derivatives of inverse changes of variables are inverse matrices (chain rule), and $\det(M^{-1})=1/\det M$.

:::

::: {#exm-linear-change-of-variables .example name="A linear change"}

$u=3x-2y$, $v=x+y$: $\dfrac{\partial(u,v)}{\partial(x,y)}=\begin{vmatrix}3&-2\\1&1\end{vmatrix}=5$, so $du\,dv=5\,dx\,dy$: the unit square goes to a parallelogram of area $5$.

:::

::: {#exm-polar-jacobian .example name="Polar coordinates"}

$x=r\cos\theta$, $y=r\sin\theta$: $\dfrac{\partial(x,y)}{\partial(r,\theta)}=\begin{vmatrix}\cos\theta&-r\sin\theta\\\sin\theta&r\cos\theta\end{vmatrix}=r$, so $dx\,dy=r\,dr\,d\theta$, as in @thm-polar-area-element.

:::

::: {#prp-change-of-variables-method .proposition name="Method"}

1. Compute the Jacobian and the area element ($dx\,dy$ in terms of $du\,dv$).
2. Express the integrand in $u,v$.
3. Find the limits by drawing the region in the $uv$-plane, or by describing the curves $u=\text{const}$ or $v=\text{const}$ in the $xy$-plane.

:::

::: {#exm-change-of-variables-hyperbolas .example name="Slicing a square by hyperbolas"}

$\int_0^1\!\int_0^1x^2y\,dx\,dy$ with $u=x$, $v=xy$. Jacobian $\begin{vmatrix}1&0\\y&x\end{vmatrix}=x$, so $dx\,dy=\frac1x\,du\,dv$ and $x^2y\,dx\,dy=xy\,du\,dv=v\,du\,dv$. The square $0\le x,y\le1$ becomes the triangle $0\le v\le u\le1$ (the edge $y=1$ becomes $u=v$, the edge $x=1$ becomes $u=1$):
$$\int_0^1\!\!\int_v^1v\,du\,dv=\int_0^1v(1-v)\,dv=\frac16,$$
which agrees with $\int_0^1x^2dx\int_0^1y\,dy=\frac13\cdot\frac12$.

:::
