<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802f07-4-q2" status="draft"}
a) With $P_0=(1,0)$, $P_1=(\cos\theta_1,\sin\theta_1)$, $P_2=(\cos\theta_2,\sin\theta_2)$ counterclockwise, $A=\frac12\det(\overrightarrow{P_0P_1},\overrightarrow{P_0P_2})$ (@thm-plane-determinant-area), which simplifies to
$$A=\tfrac12\big(\sin\theta_1+\sin(\theta_2-\theta_1)-\sin\theta_2\big).$$
(Each term is the signed area of a triangle with a vertex at the centre.) The region is $0\le\theta_1\le\theta_2\le2\pi$.

b) $A_{\theta_1}=\frac12\big(\cos\theta_1-\cos(\theta_2-\theta_1)\big)$ and $A_{\theta_2}=\frac12\big(\cos(\theta_2-\theta_1)-\cos\theta_2\big)$. Both vanish when $\cos\theta_1=\cos(\theta_2-\theta_1)=\cos\theta_2$. Inside the region, $\cos\theta_1=\cos\theta_2$ with $\theta_1<\theta_2$ forces $\theta_2=2\pi-\theta_1$; then $\cos2\theta_1=\cos\theta_1$, i.e. $2\cos^2\theta_1-\cos\theta_1-1=0$, so $\cos\theta_1=-\frac12$ ($\cos\theta_1=1$ is on the boundary). The only critical point is $(\theta_1,\theta_2)=(\frac{2\pi}3,\frac{4\pi}3)$, where $A=\frac{3\sqrt3}4$.

c) On the boundary ($\theta_1=0$, $\theta_1=\theta_2$ or $\theta_2=2\pi$) two vertices coincide and $A=0$. $A$ is continuous on the closed triangle of possible values, so its maximum and minimum exist; they are among $\frac{3\sqrt3}4$ and $0$. Maximum $\frac{3\sqrt3}4\approx1.30$: the equilateral triangle. Minimum $0$: a degenerate triangle (two vertices coincide).

d) $A_{\theta_1\theta_1}=\frac12\big(-\sin\theta_1-\sin(\theta_2-\theta_1)\big)$, $A_{\theta_1\theta_2}=\frac12\sin(\theta_2-\theta_1)$, $A_{\theta_2\theta_2}=\frac12\big(-\sin(\theta_2-\theta_1)+\sin\theta_2\big)$. At the critical point these are $-\frac{\sqrt3}2$, $\frac{\sqrt3}4$, $-\frac{\sqrt3}2$, so $AC-B^2=\frac34-\frac3{16}=\frac9{16}>0$ with $A<0$: a local maximum.
:::

::: {.solution for="prob-mit1802n-2f-q1" status="draft"}
a) On the surface $z^2=\frac1{xy}$ (with $xy>0$), so we minimise $f=x^2+y^2+\frac1{xy}$. $f_x=2x-\frac1{x^2y}=0$ and $f_y=2y-\frac1{xy^2}=0$ give $2x^2y=1=2xy^2$, so $x=y$ and $2x^3=1$: $x=y=2^{-1/3}$ (or both negative, $x=y=-2^{-1/3}$), and $z^2=2^{2/3}$, $z=\pm2^{1/3}$. These four points have distance$^2$ $2^{1/3}+2^{2/3}$. Since $f\to\infty$ at the edges of the region ($x,y\to0$ or $\infty$), they are the closest points.

b) On the surface $x^2=1+yz$, so distance$^2=1+y^2+yz+z^2$. Since $y^2+yz+z^2=(y+\frac z2)^2+\frac34z^2\ge0$, with equality only at $y=z=0$, the closest points are $(\pm1,0,0)$, at distance $1$.
:::

::: {.solution for="prob-mit1802n-2f-q2" status="draft"}
Let the box have length $x$, width $y$ (the ends are $y$ by $z$) and height $z$, with $xyz=1$. The cardboard used is $A=2xz+4yz+3xy$. Substituting $z=\frac1{xy}$: $A=\frac2y+\frac4x+3xy$, and
$$A_x=-\frac4{x^2}+3y=0,\qquad A_y=-\frac2{y^2}+3x=0$$
give $3x^2y=4$, $3xy^2=2$, hence $x=2y$, $y^3=\frac13$, and $z=\frac1{xy}=\frac32y$. So length : width : height $=2:1:\frac32=4:2:3$ (with $y=3^{-1/3}\approx0.69$ ft). $A\to\infty$ at the edges of the region, so this critical point is the minimum.
:::

::: {.solution for="prob-mit1802n-2h-q1" status="draft"}
a) $f_x=2x-y-3=0$, $f_y=-x-4y-3=0$ give $(1,-1)$. $A=2$, $B=-1$, $C=-4$: $AC-B^2=-9<0$, a saddle.

c) $f_x=8x^3-y=0$, $f_y=2y-x=0$: $y=\frac x2$ and $8x^3=\frac x2$, so $x=0$ or $x=\pm\frac14$. Critical points $(0,0)$, $(\frac14,\frac18)$, $(-\frac14,-\frac18)$. $f_{xx}=24x^2$, $f_{xy}=-1$, $f_{yy}=2$. At $(0,0)$: $AC-B^2=-1<0$, a saddle. At $(\pm\frac14,\pm\frac18)$: $A=\frac32$, $AC-B^2=3-1=2>0$, local minima.
:::

::: {.solution for="prob-mit1802n-2h-q3" status="draft"}
$R$ is $x+y\ge0$. The only critical point, $(-1,-2)$ (from $f_x=2x+2$, $f_y=2y+4$), is not in $R$. On the boundary $y=-x$: $f=2x^2-2x-1$, smallest at $x=\frac12$, where $f=-\frac32$. Since $f=(x+1)^2+(y+2)^2-6\to\infty$ at infinity, the minimum on $R$ is $-\frac32$, at $(\frac12,-\frac12)$, and there is no maximum.
:::

::: {.solution for="prob-mit1802n-2h-q4" status="draft"}
$f=(x-1)(y-1)+1$; the only critical point is $(1,1)$, where $f=1$.

a) On the $y$-axis $f=2-y\to-\infty$, and on the line $y=x$, $f=(x-1)^2+1\to\infty$: no maximum and no minimum. Near $(1,1)$, $f$ takes values above $1$ (where $x-1$ and $y-1$ have the same sign) and below $1$: a saddle.

b) With $|x-1|,|y-1|\le1$: the maximum $2$ is at $(0,0)$ and $(2,2)$, the minimum $0$ at $(2,0)$ and $(0,2)$; both are on the boundary, so the critical point is neither: a saddle.

c) $A=f_{xx}=0$, $B=f_{xy}=1$, $C=f_{yy}=0$: $AC-B^2=-1<0$, a saddle.
:::

::: {.solution for="prob-mit1802n-2h-q6" status="draft"}
a) $z=4-x-y$ and the total area is $A=xy+\frac14(4-x-y)^2$ on the triangle $x,y\ge0$, $x+y\le4$. $A_x=y-\frac12(4-x-y)=0$ and $A_y=x-\frac12(4-x-y)=0$ give $x=y=1$, $z=2$, $A=2$. On the boundary: if $z=0$, $A=xy$ with $x+y=4$ ranges from $0$ to $4$; if $x=0$ (or $y=0$), $A=\frac14z^2$ with $z\le4$ ranges from $0$ to $4$. So the largest total area is $4$: either a $2\times2$ square from the rectangle pieces ($x=y=2$, $z=0$), or only the square of side $2$ ($z=4$). The smallest is $0$ (e.g. $x=4$, $y=z=0$: a degenerate rectangle). The critical value $2$ is neither, so $(1,1)$ is a saddle point.

b) $A_{xx}=\frac12$, $A_{xy}=\frac32$, $A_{yy}=\frac12$: $AC-B^2=\frac14-\frac94=-2<0$, a saddle.
:::
