::: {.problem #prob-mit1802f07-4-q3 origin="external" source="mit1802f07-4-q3"}
(see also 2E/5)

a) Let $w=f(x,y)$, and suppose we change from rectangular to polar coordinates: $x=r\cos\theta$, $y=r\sin\theta$. Using the chain rule, derive the change of variables formula in matrix form:
$$\begin{pmatrix}w_r\\w_\theta\end{pmatrix}=A\begin{pmatrix}w_x\\w_y\end{pmatrix},$$
writing the entries of the $2\times2$ matrix $A$ as functions of $r$ and $\theta$.

b) Use the formulas $r=\sqrt{x^2+y^2}$, $\theta=\tan^{-1}y/x$ to similarly derive the converse formula:
$$\begin{pmatrix}w_x\\w_y\end{pmatrix}=B\begin{pmatrix}w_r\\w_\theta\end{pmatrix},$$
writing the entries of the $2\times2$ matrix $B$ as functions of $x$ and $y$.

c) Check that $B=A^{-1}$ by computing the product $AB$ and changing variables.

d) If $w_r=2$ and $w_\theta=10$ at the point of polar coordinates $r=5$, $\theta=\pi/2$, compute $w_x$ and $w_y$ at the same point.
:::

::: {.problem #prob-mit1802n-2c-q1 origin="external" source="mit1802n-2c-q1"}
Find the differential ($dw$ or $dz$). Make the answer look as neat as possible.

a) $w=\ln(xyz)$  b) $w=x^3y^2z$  c) $z=\dfrac{x-y}{x+y}$  d) $w=\sin^{-1}\dfrac ut$ (use $\sqrt{t^2-u^2}$)
:::

::: {.problem #prob-mit1802n-2c-q2 origin="external" source="mit1802n-2c-q2"}
The dimensions of a rectangular box are 5, 10, and 20 cm., with a possible measurement error in each side of $\pm.1$ cm. Use differentials to find what possible error should be attached to its volume.
:::

::: {.problem #prob-mit1802n-2c-q3 origin="external" source="mit1802n-2c-q3"}
Two sides of a triangle have lengths respectively $a$ and $b$, with $\theta$ the included angle. Let $A$ be the area of the triangle.

a) Express $dA$ in terms of the variables and their differentials.

b) If $a=1$, $b=2$, $\theta=\pi/6$, to which variable is $A$ most sensitive? least sensitive?

c) Using the values in (b), if the possible error in each value is .02, what is the possible error in $A$, to two decimal places?
:::

::: {.problem #prob-mit1802n-2c-q5 origin="external" source="mit1802n-2c-q5"}
The following equations define $w$ implicitly as a function of the other variables. Find $dw$ in terms of all the variables by taking the differential of both sides and solving algebraically for $dw$.

a) $\dfrac1w=\dfrac1t+\dfrac1u+\dfrac1v$  b) $u^2+2v^2+3w^2=10$
:::

::: {.problem #prob-mit1802n-2e-q1 origin="external" source="mit1802n-2e-q1"}
In the following, find $\dfrac{df}{dt}$ for the composite function $f(x(t),y(t),z(t))$ in two distinct ways:

(i) use the chain rule, then express your answer in terms of $t$ by using $x=x(t)$, etc.;

(ii) express the composite function $f$ in terms of $t$, and differentiate.

a) $w=xyz$, $x=t$, $y=t^2$, $z=t^3$  b) $w=x^2-y^2$, $x=\cos t$, $y=\sin t$  c) $w=\ln(u^2+v^2)$, $u=2\cos t$, $y=2\sin t$
:::

::: {.problem #prob-mit1802n-2e-q2 origin="external" source="mit1802n-2e-q2"}
In each of these, information about the gradient of an unknown function $f(x,y)$ is given; $x$ and $y$ are in turn functions of $t$. Use the chain rule to find out additional information about the composite function $w=f(x(t),y(t))$, without trying to determine $f$ explicitly.

a) $\nabla w=2\mathbf{i}+3\mathbf{j}$ at $P:(1,0)$; $x=\cos t$, $y=\sin t$. Find the value of $\dfrac{dw}{dt}$ at $t=0$.

b) $\nabla w=y\mathbf{i}+x\mathbf{j}$; $x=\cos t$, $y=\sin t$. Find $\dfrac{dw}{dt}$ and tell for what $t$-values it is zero.

c) $\nabla f=\langle1,-1,2\rangle$ at $(1,1,1)$. Let $x=t$, $y=t^2$, $z=t^3$; find $\dfrac{df}{dt}$ at $t=1$.

d) $\nabla f=\langle3x^2y,\ x^3+z,\ y\rangle$; $x=t$, $y=t^2$, $z=t^3$. Find $\dfrac{df}{dt}$.

*Note (these notes):* Parts (b) and (c) were assigned.
:::

::: {.problem #prob-mit1802n-2e-q5 origin="external" source="mit1802n-2e-q5"}
Let $w=f(x,y)$, and suppose we change from rectangular to polar coordinates: $x=r\cos\theta$, $y=r\sin\theta$.

a) Show that $(w_x)^2+(w_y)^2=(w_r)^2+\dfrac1{r^2}(w_\theta)^2$.

b) Suppose $\nabla w=2\mathbf{i}-\mathbf{j}$ at the point $x=1$, $y=1$. Find $\dfrac{\partial w}{\partial r}$ and $\dfrac{\partial w}{\partial\theta}$ when $r=\sqrt2$, $\theta=\pi/4$, and verify the relation in part (a), at the point.
:::

::: {.problem #prob-mit1802n-2e-q7 origin="external" source="mit1802n-2e-q7"}
The Jacobian matrix for the change of variables $x=x(u,v)$, $y=y(u,v)$ is defined to be $J=\begin{pmatrix}x_u&x_v\\y_u&y_v\end{pmatrix}$. Let $\nabla f(x,y)$ be represented as the row vector $\langle f_x\ f_y\rangle$. Show that
$$\nabla f\big(x(u,v),y(u,v)\big)=\nabla f(x,y)\cdot J\qquad\text{(matrix multiplication).}$$
:::

::: {.problem #prob-mit1802n-2e-q8 origin="external" source="mit1802n-2e-q8"}
a) Let $w=f(y/x)$; i.e., $w$ is the composite of the functions $w=f(u)$, $u=y/x$. Show that $w$ satisfies the PDE (partial differential equation) $x\dfrac{\partial w}{\partial x}+y\dfrac{\partial w}{\partial y}=0$.

b) Let $w=f(x^2-y^2)$; show that $w$ satisfies the PDE $y\dfrac{\partial w}{\partial x}+x\dfrac{\partial w}{\partial y}=0$.

*Note (these notes):* Parts (a) and (b) were assigned.
:::
