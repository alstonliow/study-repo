<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802f07-7-q3" status="draft"}
1. The distance from $(x,y)$ to the line $x=\bar x$ is $\lvert x-\bar x\rvert$, so $\bar I=\iint_R(x-\bar x)^2\delta\,dA$.

2. Expand: $\bar I=\iint_Rx^2\delta\,dA-2\bar x\iint_Rx\,\delta\,dA+\bar x^2\iint_R\delta\,dA$.

3. By @def-mass-centroid-moment, $\iint_Rx\,\delta\,dA=M\bar x$ and $\iint_R\delta\,dA=M$. So $\bar I=I-2M\bar x^2+M\bar x^2=I-M\bar x^2$, i.e. $I=\bar I+M\bar x^2$.
:::

::: {.solution for="prob-mit1802n-3c-q1" status="draft"}
Put the legs on the axes: $R$ is $x,y\ge0$, $x+y\le a$.

a) $I_x=\displaystyle\int_0^a\!\!\int_0^{a-x}y^2\,dy\,dx=\int_0^a\frac{(a-x)^3}3\,dx=\frac{a^4}{12}$.

b) $I_0=I_x+I_y=\frac{a^4}{12}+\frac{a^4}{12}=\frac{a^4}6$ (by symmetry $I_y=I_x$).

c) The altitude from the right angle cuts $R$ into two right isosceles triangles with legs $a/\sqrt2$, each having a leg on the hypotenuse. By (a) each contributes $\frac{(a/\sqrt2)^4}{12}=\frac{a^4}{48}$, so the moment about the hypotenuse is $\frac{a^4}{24}$.
:::

::: {.solution for="prob-mit1802n-3c-q2" status="draft"}
a) $M=\int_0^\pi\sin x\,dx=2$. By symmetry $\bar x=\frac\pi2$. $\iint y\,dA=\int_0^\pi\frac{\sin^2x}2\,dx=\frac\pi4$, so $\bar y=\frac\pi8$.
:::

::: {.solution for="prob-mit1802n-3c-q4" status="draft"}
Put the vertex at the origin and the sector symmetric about the $x$-axis: $0\le r\le a$, $-\alpha\le\theta\le\alpha$. Its area is $a^2\alpha$, $\bar y=0$ by symmetry, and
$$\iint x\,dA=\int_{-\alpha}^\alpha\!\!\int_0^ar\cos\theta\cdot r\,dr\,d\theta=\frac{a^3}3\cdot2\sin\alpha,$$
so $\bar x=\dfrac{2a\sin\alpha}{3\alpha}$. (For $\alpha=\frac\pi2$, the half disc, this is $\frac{4a}{3\pi}$, as in @exm-centroid-half-disk.)
:::
