<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802f07-9-q1" status="draft"}
a) Green's theorem with $M=0$, $N=x$ gives $\oint_Cx\,dy=\iint_R1\,dA$; with $M=-y$, $N=0$ it gives $\oint_C-y\,dx=\iint_R1\,dA$ (@cor-area-by-line-integral).

b) The boundary, counterclockwise, is the $x$-axis from $0$ to $2\pi a$ followed by the arch traversed backwards (from $t=2\pi$ to $t=0$). On the $x$-axis $y=0$, so only the arch contributes to $\oint-y\,dx$:
$$\text{Area}=\int_{2\pi}^0-a(1-\cos t)\,a(1-\cos t)\,dt=a^2\int_0^{2\pi}(1-2\cos t+\cos^2t)\,dt=a^2(2\pi+\pi)=3\pi a^2 .$$
:::

::: {.solution for="prob-mit1802f07-9-q2" status="draft"}
a) With $M=x^2y+y^3-y$ and $N=3x+2y^2x+e^y$: $N_x-M_y=(3+2y^2)-(x^2+3y^2-1)=4-x^2-y^2$. By Green's theorem the integral is $\iint_R(4-x^2-y^2)\,dA$. It is largest when $R$ contains exactly the points where the integrand is positive: $R$ is the disk $x^2+y^2\le4$, and $C$ is the circle of radius $2$ about the origin, counterclockwise.

b) $\displaystyle\int_0^{2\pi}\!\!\int_0^2(4-r^2)\,r\,dr\,d\theta=2\pi\Big[2r^2-\frac{r^4}4\Big]_0^2=2\pi\cdot4=8\pi .$
:::

::: {.solution for="prob-mit1802n-4d-q1" status="draft"}
a) Directly, $x=\cos t$, $y=\sin t$: $\int_0^{2\pi}(-2\sin^2t+\cos^2t)\,dt=-2\pi+\pi=-\pi$. Green: $N_x-M_y=1-2=-1$, so $\iint-1\,dA=-\pi$.

b) Directly: bottom ($y=0$, $x:0\to2$) $\int_0^2x^2\,dx=\frac83$; right ($x=2$, $y:0\to1$) $\int_0^14\,dy=4$; top ($x:2\to0$) $-\frac83$; left ($x=0$) $0$. Total $4$. Green: $N_x-M_y=2x$, $\int_0^1\!\int_0^22x\,dx\,dy=4$.

c) Directly: along $y=x^2$ from $(0,0)$ to $(1,1)$, $\int_0^1(x^3+2x^5)\,dx=\frac14+\frac13=\frac7{12}$; back along $y=x$, $\int_1^02x^2\,dx=-\frac23$. Total $-\frac1{12}$. Green: $N_x-M_y=-x$, $\int_0^1\!\int_{x^2}^x-x\,dy\,dx=-\big(\frac13-\frac14\big)=-\frac1{12}$.
:::

::: {.solution for="prob-mit1802n-4d-q2" status="draft"}
$N_x=4x^3=M_y$ everywhere, and the field is continuously differentiable in the whole plane, so by Green's theorem the integral around any closed curve is $\iint0\,dA=0$. (Indeed $4x^3y\,dx+x^4\,dy=d(x^4y)$ is exact.)
:::

::: {.solution for="prob-mit1802n-4d-q3" status="draft"}
Use $\text{area}=\frac12\oint x\,dy-y\,dx$ (@cor-area-by-line-integral), with $0\le\theta\le2\pi$ (counterclockwise):
$$x\,dy-y\,dx=\cos^3\theta\cdot3\sin^2\theta\cos\theta\,d\theta+\sin^3\theta\cdot3\cos^2\theta\sin\theta\,d\theta=3\sin^2\theta\cos^2\theta\,d\theta=\tfrac34\sin^22\theta\,d\theta .$$
So area $=\frac12\cdot\frac34\cdot\pi=\frac{3\pi}8$.
:::

::: {.solution for="prob-mit1802n-4d-q4" status="draft"}
By Green's theorem it equals $\iint_R(3x^2+3y^2)\,dA$, where $R$ is the region inside $C$. The integrand is positive except at one point, so the integral is positive.
:::

::: {.solution for="prob-mit1802n-4d-q5" status="draft"}
$N_x-M_y=(2xy+2)-2xy=2$, so by Green's theorem the integral (counterclockwise) is $2\cdot\text{area}=2s^2$ for a square of side $s$, wherever it is.
:::
