<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802n-5a-q1" status="draft"}
a) Inner: $\frac12+y+z$. Middle: $\int_{-1}^1(\frac12+y+z)\,dy=1+2z$. Outer: $\int_0^2(1+2z)\,dz=6$.

b) Inner: $xy^2(xy)^2=x^3y^4$. Middle: $\int_0^{\sqrt y}x^3y^4\,dx=\frac{y^6}4$. Outer: $\int_0^2\frac{y^6}4\,dy=\frac{2^7}{28}=\frac{32}7$.
:::

::: {.solution for="prob-mit1802n-5a-q2" status="draft"}
a) The prism is $0\le x\le1$, $y,z\ge0$, $y+z\le1$.
(i) $\displaystyle\int_0^1\!\!\int_0^1\!\!\int_0^{1-y}dz\,dy\,dx$  (ii) $\displaystyle\int_0^1\!\!\int_0^{1-y}\!\!\int_0^1dx\,dz\,dy$  (iii) $\displaystyle\int_0^1\!\!\int_0^1\!\!\int_0^{1-z}dy\,dx\,dz$.

b) The slanted face is $x+\frac y2+\frac z2=1$, i.e. $z=2-2x-y$: $\displaystyle\int_0^1\!\!\int_0^{2-2x}\!\!\int_0^{2-2x-y}dz\,dy\,dx$.

c) Polar coordinates in the $xz$-plane, $x=r\cos\theta$, $z=r\sin\theta$, and $y$: $\displaystyle\int_0^{\pi/2}\!\!\int_0^1\!\!\int_0^2dy\,r\,dr\,d\theta$.

d) The cone (upper half) is $z=r$ and the sphere $z=\sqrt{2-r^2}$; they meet at $r=1$: $\displaystyle\int_0^{2\pi}\!\!\int_0^1\!\!\int_r^{\sqrt{2-r^2}}dz\,r\,dr\,d\theta$.
:::

::: {.solution for="prob-mit1802n-5a-q3" status="draft"}
The volume is $\frac16$. $\iiint z\,dV=\int_0^1z\cdot\frac{(1-z)^2}2\,dz=\frac1{24}$ (the slice at height $z$ is a triangle of area $\frac12(1-z)^2$), so $\bar z=\frac{1/24}{1/6}=\frac14$, and by symmetry $(\bar x,\bar y,\bar z)=(\frac14,\frac14,\frac14)$.
:::

::: {.solution for="prob-mit1802n-5a-q4" status="draft"}
Put the vertex at the origin, axis up: $r\le z\le h$ (the half-angle is $45^\circ$), $\delta=r$.

a) $M=\displaystyle\int_0^{2\pi}\!\!\int_0^h\!\!\int_0^zr\cdot r\,dr\,dz\,d\theta=2\pi\int_0^h\frac{z^3}3\,dz=\frac{\pi h^4}6$.

b) $\bar x=\bar y=0$ by symmetry; $\iiint z\,\delta\,dV=2\pi\int_0^hz\frac{z^3}3\,dz=\frac{2\pi h^5}{15}$, so $\bar z=\frac{2\pi h^5/15}{\pi h^4/6}=\frac45h$ (measured from the vertex).
:::

::: {.solution for="prob-mit1802n-5a-q5" status="draft"}
Put the base vertices at $(\pm1,0,0)$, $(0,\pm1,0)$, so that $D$ lies along the $x$-axis, and the apex at $(0,0,2)$. The cross-section at height $z$ is the square $|x|+|y|\le1-\frac z2$. The distance to the $x$-axis is $\sqrt{y^2+z^2}$, and by symmetry in $x$ and $y$
$$I_D=\iiint_S(y^2+z^2)\,dV=4\int_0^2\!\!\int_0^{1-z/2}\!\!\int_0^{1-z/2-x}(y^2+z^2)\,dy\,dx\,dz .$$
:::

::: {.solution for="prob-mit1802n-5a-q6" status="draft"}
$I_z=\displaystyle\int_0^{2\pi}\!\!\int_0^a\!\!\int_0^{\sqrt{a^2-r^2}}r^2\,dz\,r\,dr\,d\theta=2\pi\int_0^ar^3\sqrt{a^2-r^2}\,dr$. With $u=a^2-r^2$: $\int_0^ar^3\sqrt{a^2-r^2}\,dr=\frac12\int_0^{a^2}(a^2-u)\sqrt u\,du=\frac12\Big(\frac23-\frac25\Big)a^5=\frac{2a^5}{15}$. So $I_z=\dfrac{4\pi a^5}{15}$.
:::

::: {.solution for="prob-mit1802n-5a-q7" status="draft"}
In cylindrical coordinates $D$ is $r^2\le z\le2r\cos\theta$, which requires $r\le2\cos\theta$, $-\frac\pi2\le\theta\le\frac\pi2$.
$$I_z=\int_{-\pi/2}^{\pi/2}\!\!\int_0^{2\cos\theta}r^2(2r\cos\theta-r^2)\,r\,dr\,d\theta=\int_{-\pi/2}^{\pi/2}\Big(\frac{64}5-\frac{64}6\Big)\cos^6\theta\,d\theta=\frac{32}{15}\cdot\frac{5\pi}{16}=\frac{2\pi}3 .$$
:::
