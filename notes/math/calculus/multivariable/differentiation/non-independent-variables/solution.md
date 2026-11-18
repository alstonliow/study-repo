<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802f07-6-q1" status="draft"}
The constraint ties $x$ and $y$ together; $z$ is free. So there are two independent variables, $z$ and one of $x,y$.

i) No sense: $x$ cannot vary while $x$ is held fixed.

ii) No sense: holding $y$ fixed also fixes $x$ (by $g(x,y)=c$, where $g_x\ne0$), so $x$ cannot vary.

iii) Makes sense: hold $z$ fixed and let $y$ follow $x$ along the constraint. $dw=f_x\,dx+f_y\,dy+f_z\,dz$ with $dz=0$ and $g_x\,dx+g_y\,dy=0$, i.e. $dy=-\frac{g_x}{g_y}dx$:
$$\Big(\frac{\partial w}{\partial x}\Big)_z=f_x-\frac{f_yg_x}{g_y}.$$
:::

::: {.solution for="prob-mit1802f07-6-q2" status="draft"}
a) $dw=3x^2yt\,dx+x^3t\,dy+x^3y\,dt$ and $dt=\cos(x+y)(dx+dy)$. With $dx=0$: $dy=\frac{dt}{\cos(x+y)}$, so
$$\Big(\frac{\partial w}{\partial t}\Big)_x=\frac{x^3t}{\cos(x+y)}+x^3y=x^3\tan(x+y)+x^3y .$$

b) The differentials of the two equations are $5x^4\,dx+z\,dy+y\,dz=0$ and $(y^2+2xz)\,dx+(2xy+z^2)\,dy+(2yz+x^2)\,dz=0$. At $(1,1,2)$ (which satisfies both equations): $5\,dx+2\,dy+dz=0$ and $5\,dx+6\,dy+5\,dz=0$. The first gives $dz=-5\,dx-2\,dy$; then the second gives $-20\,dx-4\,dy=0$, so $\dfrac{dx}{dy}=-\dfrac15$.
:::

::: {.solution for="prob-mit1802n-2j-q1" status="draft"}
With $y,z$ independent, eliminate $x$: $x^2=z-y^2$, so $w=(z-y^2)+y^2+z^2=z+z^2$.

a) $\left(\frac{\partial w}{\partial y}\right)_z=0$.  b) $\left(\frac{\partial w}{\partial z}\right)_y=1+2z$.
:::

::: {.solution for="prob-mit1802n-2j-q2" status="draft"}
(i) With $y,z$ independent, $x$ depends on them. Differentiating $z=x^2+y^2$: $0=2x\left(\frac{\partial x}{\partial y}\right)_z+2y$ and $1=2x\left(\frac{\partial x}{\partial z}\right)_y$. Then
$$\Big(\frac{\partial w}{\partial y}\Big)_z=2x\Big(\frac{\partial x}{\partial y}\Big)_z+2y=-2y+2y=0,\qquad\Big(\frac{\partial w}{\partial z}\Big)_y=2x\Big(\frac{\partial x}{\partial z}\Big)_y+2z=1+2z .$$

(ii) $dw=2x\,dx+2y\,dy+2z\,dz$ and $dz=2x\,dx+2y\,dy$, so $2x\,dx=dz-2y\,dy$ and $dw=dz-2y\,dy+2y\,dy+2z\,dz=(1+2z)\,dz+0\,dy$. The coefficients give the same two derivatives.
:::

::: {.solution for="prob-mit1802n-2j-q3" status="draft"}
a) Independent $x,z,t$; then $y=zt/x$ and $\left(\frac{\partial y}{\partial t}\right)_{x,z}=\frac zx$:
$$\Big(\frac{\partial w}{\partial t}\Big)_{x,z}=w_y\frac zx+w_t=x^3\cdot\frac zx-z^2=x^2z-z^2 .$$

b) Independent $x,y,z$; then $t=xy/z$ and $\left(\frac{\partial t}{\partial z}\right)_{x,y}=-\frac{xy}{z^2}=-\frac tz$:
$$\Big(\frac{\partial w}{\partial z}\Big)_{x,y}=w_z+w_t\Big(-\frac tz\Big)=-2zt+z^2\frac tz=-zt .$$
:::

::: {.solution for="prob-mit1802n-2j-q4" status="draft"}
$dw=3x^2y\,dx+x^3\,dy-2zt\,dz-z^2\,dt$ and, from $xy=zt$, $y\,dx+x\,dy=t\,dz+z\,dt$.

a) $dx=dz=0$: $x\,dy=z\,dt$, so $dw=x^3\frac zx\,dt-z^2\,dt=(x^2z-z^2)\,dt$.

b) $dx=dy=0$: $0=t\,dz+z\,dt$, so $dt=-\frac tz\,dz$ and $dw=-2zt\,dz+z^2\frac tz\,dz=-zt\,dz$.
:::

::: {.solution for="prob-mit1802n-2j-q5" status="draft"}
a) With $v$ fixed, $T=\frac{pv}{nR}$ changes with $p$: $\left(\frac{\partial S}{\partial p}\right)_v=S_p+S_T\frac v{nR}$.
:::

::: {.solution for="prob-mit1802n-2j-q6" status="draft"}
The independent variables are $u$ and $x$; $v=u+x$ (and $y=u/x$ plays no part).

a) $w_u=3u^2-v^2$, $w_v=-2uv$, $\left(\frac{\partial v}{\partial u}\right)_x=1$, $\left(\frac{\partial v}{\partial x}\right)_u=1$:
$$\Big(\frac{\partial w}{\partial u}\Big)_x=3u^2-v^2-2uv,\qquad\Big(\frac{\partial w}{\partial x}\Big)_u=-2uv .$$

b) $dw=(3u^2-v^2)\,du-2uv\,dv$ with $dv=du+dx$: $dw=(3u^2-v^2-2uv)\,du-2uv\,dx$, giving the same two coefficients.
:::

::: {.solution for="prob-mit1802n-2j-q7" status="draft"}
From the constraint $y=z-x^2-1$ (which gives $y=-1$ at $x=z=1$, the point $P$), $y_x=-2x=-2$ and $y_z=1$. By the chain rule $g_x=f_x+f_yy_x=2+1\cdot(-2)=0$ and $g_z=f_yy_z+f_z=1-3=-2$. So $\nabla g=\langle0,-2\rangle$.
:::
