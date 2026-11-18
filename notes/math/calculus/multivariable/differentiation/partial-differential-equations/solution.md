<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802n-2k-q1" status="draft"}
$w=\frac12\ln(x^2+y^2)$, so $w_x=\dfrac x{x^2+y^2}$, $w_{xx}=\dfrac{y^2-x^2}{(x^2+y^2)^2}$, and by symmetry $w_{yy}=\dfrac{x^2-y^2}{(x^2+y^2)^2}$; the sum is $0$ (@exm-laplace-solutions). At $(0,0)$, $w$ is not defined ($\ln r\to-\infty$), so it cannot satisfy the equation there.
:::

::: {.solution for="prob-mit1802n-2k-q2" status="draft"}
Write $w=\rho^{2n}$ and put $m=2n$. $w_x=m\rho^{m-2}x$, $w_{xx}=m\rho^{m-2}+m(m-2)\rho^{m-4}x^2$; adding the three second derivatives, $\nabla^2w=3m\rho^{m-2}+m(m-2)\rho^{m-2}=m(m+1)\rho^{m-2}$. This is $0$ for $m=0$ (the constant $w=1$, $n=0$) or $m=-1$, i.e. $n=-\frac12$: $w=\dfrac1{\sqrt{x^2+y^2+z^2}}=\dfrac1\rho$ (away from the origin). It is the gravitational (or electrostatic) potential of a point mass (or charge) at the origin.
:::

::: {.solution for="prob-mit1802n-2k-q3" status="draft"}
a) $w_{xx}+w_{yy}=2a+2c=0$ exactly when $c=-a$. So the solutions are $w=a(x^2-y^2)+bxy$: combinations of $f_1=x^2-y^2$ and $f_2=xy$.

b) $w_{xx}=6ax+2by$ and $w_{yy}=2cx+6dy$; the sum $(6a+2c)x+(2b+6d)y$ vanishes identically exactly when $c=-3a$ and $b=-3d$. So the solutions are $w=a(x^3-3xy^2)+d(y^3-3x^2y)$: combinations of $x^3-3xy^2$ and $3x^2y-y^3$.
:::

::: {.solution for="prob-mit1802n-2k-q4" status="draft"}
The equation is $w_{xx}=\frac1{c^2}w_{tt}$; @prp-wave-equation-travelling shows that $w=f(x+ct)+g(x-ct)$ satisfies it. $f(x)$ is the shape of the wave at time $t=0$. At time $t$ the graph of $f(x+ct)$ is the graph of $f$ moved $ct$ units to the left: the same shape travelling to the left with speed $c$.
:::

::: {.solution for="prob-mit1802n-2k-q5" status="draft"}
The equation is $w_{xx}=\frac1{a^2}w_t$ ($a$ a constant of the material). For $w=\sin kx\,e^{rt}$: $w_{xx}=-k^2w$ and $w_t=rw$, so we need $r=-a^2k^2$. $w(0,t)=0$ holds automatically; $w(1,t)=0$ requires $\sin k=0$, i.e. $k=n\pi$. So
$$w=\sin(n\pi x)\,e^{-a^2n^2\pi^2t},\qquad n=1,2,3,\dots$$
These are temperatures in a rod $0\le x\le1$ whose ends are held at temperature $0$: a sinusoidal initial profile keeps its shape while dying away exponentially, faster for larger $n$. As $t\to\infty$ the temperature tends to $0$ everywhere.
:::
