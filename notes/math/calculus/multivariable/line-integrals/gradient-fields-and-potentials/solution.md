<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802f07-8-q2" status="draft"}
a) $\theta_x=\dfrac{-y/x^2}{1+y^2/x^2}=\dfrac{-y}{x^2+y^2}$ and $\theta_y=\dfrac{1/x}{1+y^2/x^2}=\dfrac{x}{x^2+y^2}$, so $\nabla\theta=\vec F$ for $x>0$.

b) By @thm-ftc-line-integrals, $\int_C\vec F\cdot d\vec r=\theta(B)-\theta(A)=\theta_2-\theta_1$, with the angles taken in $(-\frac\pi2,\frac\pi2)$. It does not depend on $r_1,r_2$.

c) On the unit circle $x=\cos t$, $y=\sin t$: $\vec F\cdot d\vec r=(-\sin t)(-\sin t)\,dt+\cos t\cos t\,dt=dt$. $C_1$ is $t$ from $0$ to $\pi$: $\int_{C_1}=\pi$. $C_2$ is $t$ from $0$ to $-\pi$: $\int_{C_2}=-\pi$.

d) $N_x=\dfrac{(x^2+y^2)-2x^2}{(x^2+y^2)^2}=\dfrac{y^2-x^2}{(x^2+y^2)^2}$ and $M_y=\dfrac{-(x^2+y^2)+2y^2}{(x^2+y^2)^2}=\dfrac{y^2-x^2}{(x^2+y^2)^2}$, so $\operatorname{curl}\vec F=N_x-M_y=0$ wherever $(x,y)\ne(0,0)$.

e) Not conservative on its whole domain (the plane minus the origin): $C_1$ and $C_2$ have the same endpoints but give $\pi\ne-\pi$; equivalently the closed curve $C_1-C_2$ (the unit circle counterclockwise) gives $2\pi\ne0$. Zero curl does not suffice because the domain has a hole (@sec-math-calculus-multivariable-line-integrals-simply-connected-regions). On the right half-plane it is conservative: there it is the gradient field $\nabla\theta$ (part (a)), and gradient fields are conservative (@thm-conservative-equivalences).
:::

::: {.solution for="prob-mit1802f07-8-q3" status="draft"}
a) $r_x=\frac xr$, $r_y=\frac yr$. With $M=r^nx$, $N=r^ny$: $N_x=nr^{n-1}\frac xr\,y$ and $M_y=nr^{n-1}\frac yr\,x$, so $\operatorname{curl}\vec F=N_x-M_y=0$ (away from the origin, or everywhere if $n\ge0$).

b) For $g=g(r)$, $\nabla g=g'(r)\langle r_x,r_y\rangle=\frac{g'(r)}r\langle x,y\rangle$. We need $g'(r)/r=r^n$, i.e. $g'(r)=r^{n+1}$:
$$g=\frac{r^{n+2}}{n+2}+c\quad(n\ne-2),\qquad g=\ln r+c\quad(n=-2).$$
:::

::: {.solution for="prob-mit1802n-4c-q5" status="draft"}
a) $M_y=2y$, $N_x=ay$: $a=2$. Then $f_x=y^2+2x$ gives $f=xy^2+x^2+g(y)$, and $f_y=2xy+g'(y)=2xy$ gives $g=c$: $f=xy^2+x^2+c$. (Check with method 1: along the $x$-axis $\int_0^{x_1}2x\,dx=x_1^2$, then up $\int_0^{y_1}2x_1y\,dy=x_1y_1^2$.)

b) $M_y=(x+a)e^{x+y}$, $N_x=(1+x)e^{x+y}$: $a=1$. Then $f_y=xe^{x+y}$ gives $f=xe^{x+y}+g(x)$, and $f_x=(1+x)e^{x+y}+g'(x)=(x+1)e^{x+y}$ gives $g=c$: $f=xe^{x+y}+c$.
:::

::: {.solution for="prob-mit1802n-4c-q6" status="draft"}
a) $M_y=1\ne-1=N_x$: not exact.

b) $M=2xy+y^2$, $N=2xy+x^2$: $M_y=2x+2y=N_x$, exact. $f_x=2xy+y^2$ gives $f=x^2y+xy^2+g(y)$, and $f_y=x^2+2xy+g'=N$ gives $g=c$. So the differential is $d(x^2y+xy^2)$.
:::
