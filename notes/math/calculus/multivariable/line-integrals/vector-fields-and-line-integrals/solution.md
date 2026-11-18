<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802f07-8-q1" status="draft"}
1. Use $x$ as the parameter along $C$: $y=f(x)$, $x_1\le x\le x_2$. Since $\vec F$ has no $\hat\jmath$ component,
$$\int_C\vec F\cdot d\vec r=\int_C\big(x^2y+\tfrac13y^3\big)\,dx=\int_{x_1}^{x_2}\big(x^2f(x)+\tfrac13f(x)^3\big)\,dx .$$

2. The region is $x_1\le x\le x_2$, $0\le y\le f(x)$, so
$$I_0=\iint_R(x^2+y^2)\,dA=\int_{x_1}^{x_2}\Big[x^2y+\frac{y^3}3\Big]_0^{f(x)}dx=\int_{x_1}^{x_2}\big(x^2f(x)+\tfrac13f(x)^3\big)\,dx,$$
the same.
:::

::: {.solution for="prob-mit1802n-4a-q1" status="draft"}
b) Every vector points towards the origin, with length $r$ (the distance to the origin); continuously differentiable in the whole plane.

d) Unit vectors tangent to the circles centred at the origin, pointing clockwise ($\langle y,-x\rangle$ is $\langle x,y\rangle$ turned $90^\circ$ clockwise); continuously differentiable everywhere except the origin, where it is undefined.
:::

::: {.solution for="prob-mit1802n-4a-q2" status="draft"}
a) $a\mathbf{i}+b\mathbf{j}$.

b) $\ln r=\frac12\ln(x^2+y^2)$, so $\nabla w=\dfrac{x\mathbf{i}+y\mathbf{j}}{r^2}$.

c) $r_x=x/r$, $r_y=y/r$, so $\nabla w=f'(r)\,\dfrac{x\mathbf{i}+y\mathbf{j}}r$.
:::

::: {.solution for="prob-mit1802n-4a-q3" status="draft"}
a) $\mathbf{F}=\mathbf{i}+2\mathbf{j}$.

b) The unit vector towards the origin is $-(x\mathbf{i}+y\mathbf{j})/r$, so $\mathbf{F}=-r(x\mathbf{i}+y\mathbf{j})$.

c) $(y\mathbf{i}-x\mathbf{j})/r$ is the clockwise unit tangent, so $\mathbf{F}=\dfrac{y\mathbf{i}-x\mathbf{j}}{r^3}$.

d) $\mathbf{F}=g(x,y)(\mathbf{i}+\mathbf{j})$ for some function $g$.
:::

::: {.solution for="prob-mit1802n-4a-q4" status="draft"}
The right-hand rule gives the counterclockwise direction (seen from above), whose unit tangent is $(-y\mathbf{i}+x\mathbf{j})/r$. So $\mathbf{F}=\dfrac kr\cdot\dfrac{-y\mathbf{i}+x\mathbf{j}}r=k\,\dfrac{-y\mathbf{i}+x\mathbf{j}}{x^2+y^2}$.
:::

::: {.solution for="prob-mit1802n-4b-q1" status="draft"}
a) $\int(x^2-y)\,dx+2x\,dy$. On $C_1$ ($y=0$, $dy=0$): $\int_{-1}^1x^2\,dx=\frac23$. On $C_2$ ($y=1-x^2$, $dy=-2x\,dx$): $\int_{-1}^1\big[(2x^2-1)-4x^2\big]dx=\int_{-1}^1(-2x^2-1)\,dx=-\frac{10}3$.

b) $\int xy\,dx-x^2\,dy$ with $x=\sin t$, $y=\cos t$, $0\le t\le\frac\pi2$: $\int_0^{\pi/2}(\sin t\cos^2t+\sin^3t)\,dt=\int_0^{\pi/2}\sin t\,dt=1$.

c) $\oint y\,dx-x\,dy$ along $(0,0)\to(0,1)\to(1,0)\to(0,0)$. First side: $x=0$, $dx=0$: $0$. Second: $x=t$, $y=1-t$: $\int_0^1\big((1-t)+t\big)dt=1$. Third: $y=0$, $dy=0$: $0$. Total $1$.

d) $\int y\,dx=\int_0^{2\pi}\sin t(-2\sin t)\,dt=-2\pi$.
:::

::: {.solution for="prob-mit1802n-4b-q2" status="draft"}
Use $\int_C\mathbf{F}\cdot\hat{\mathbf{T}}\,ds$.

a) $\mathbf{F}$ is radial, perpendicular to $C$: $\mathbf{F}\cdot\hat{\mathbf{T}}=0$, the integral is $0$.

b) $\mathbf{F}$ is tangent to $C$, pointing clockwise, with length $a$: $\mathbf{F}\cdot\hat{\mathbf{T}}=-a$, the integral is $-a\cdot2\pi a=-2\pi a^2$.
:::
