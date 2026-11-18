<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802f07-4-q3" status="draft"}
a) By @thm-chain-rule-several-parameters, $w_r=w_xx_r+w_yy_r=\cos\theta\,w_x+\sin\theta\,w_y$ and $w_\theta=w_xx_\theta+w_yy_\theta=-r\sin\theta\,w_x+r\cos\theta\,w_y$:
$$A=\begin{pmatrix}\cos\theta&\sin\theta\\-r\sin\theta&r\cos\theta\end{pmatrix}.$$

b) $r_x=\frac x{\sqrt{x^2+y^2}}$, $r_y=\frac y{\sqrt{x^2+y^2}}$, $\theta_x=\frac{-y}{x^2+y^2}$, $\theta_y=\frac{x}{x^2+y^2}$, and $w_x=w_rr_x+w_\theta\theta_x$, $w_y=w_rr_y+w_\theta\theta_y$:
$$B=\begin{pmatrix}\dfrac x{\sqrt{x^2+y^2}}&\dfrac{-y}{x^2+y^2}\\[2mm]\dfrac y{\sqrt{x^2+y^2}}&\dfrac x{x^2+y^2}\end{pmatrix}.$$

c) In polar coordinates $B=\begin{pmatrix}\cos\theta&-\sin\theta/r\\\sin\theta&\cos\theta/r\end{pmatrix}$, and
$$AB=\begin{pmatrix}\cos^2\theta+\sin^2\theta&(-\cos\theta\sin\theta+\sin\theta\cos\theta)/r\\-r\sin\theta\cos\theta+r\cos\theta\sin\theta&\sin^2\theta+\cos^2\theta\end{pmatrix}=I .$$

d) At $r=5$, $\theta=\pi/2$ (the point $(0,5)$): $w_x=\cos\theta\,w_r-\frac{\sin\theta}r\,w_\theta=-\frac{10}5=-2$ and $w_y=\sin\theta\,w_r+\frac{\cos\theta}r\,w_\theta=2$.
:::

::: {.solution for="prob-mit1802n-2c-q1" status="draft"}
a) $w=\ln x+\ln y+\ln z$: $dw=\dfrac{dx}x+\dfrac{dy}y+\dfrac{dz}z$.

b) $dw=3x^2y^2z\,dx+2x^3yz\,dy+x^3y^2\,dz=x^2y\,(3yz\,dx+2xz\,dy+xy\,dz)$.

c) $dz=\dfrac{2(y\,dx-x\,dy)}{(x+y)^2}$.

d) $dw=\dfrac{d(u/t)}{\sqrt{1-u^2/t^2}}=\dfrac{t\,du-u\,dt}{t^2}\cdot\dfrac{|t|}{\sqrt{t^2-u^2}}=\dfrac{t\,du-u\,dt}{t\sqrt{t^2-u^2}}$ (for $t>0$).
:::

::: {.solution for="prob-mit1802n-2c-q2" status="draft"}
$V=xyz$, $dV=yz\,dx+xz\,dy+xy\,dz$. With $(x,y,z)=(5,10,20)$ and $|dx|,|dy|,|dz|\le0.1$: $|dV|\le(200+100+50)(0.1)=35$ cm$^3$ (the volume is $1000$ cm$^3$).
:::

::: {.solution for="prob-mit1802n-2c-q3" status="draft"}
a) $A=\frac12ab\sin\theta$: $dA=\frac12\big(b\sin\theta\,da+a\sin\theta\,db+ab\cos\theta\,d\theta\big)$.

b) $A_a=\frac12$, $A_b=\frac14$, $A_\theta=\frac{\sqrt3}2\approx0.87$: most sensitive to $\theta$, least to $b$.

c) $|dA|\le(0.5+0.25+0.866)(0.02)\approx0.03$.
:::

::: {.solution for="prob-mit1802n-2c-q5" status="draft"}
a) $-\dfrac{dw}{w^2}=-\dfrac{dt}{t^2}-\dfrac{du}{u^2}-\dfrac{dv}{v^2}$, so $dw=w^2\Big(\dfrac{dt}{t^2}+\dfrac{du}{u^2}+\dfrac{dv}{v^2}\Big)$.

b) $2u\,du+4v\,dv+6w\,dw=0$, so $dw=-\dfrac{u\,du+2v\,dv}{3w}$.
:::

::: {.solution for="prob-mit1802n-2e-q1" status="draft"}
a) (i) $yz\cdot1+xz\cdot2t+xy\cdot3t^2=t^5+2t^5+3t^5=6t^5$. (ii) $w=t^6$, $w'=6t^5$.

b) (i) $2x(-\sin t)-2y\cos t=-4\sin t\cos t=-2\sin2t$. (ii) $w=\cos^2t-\sin^2t=\cos2t$, $w'=-2\sin2t$.

c) (Here $v=2\sin t$.) (i) $\dfrac{2u}{u^2+v^2}(-2\sin t)+\dfrac{2v}{u^2+v^2}(2\cos t)=\dfrac{-8\cos t\sin t+8\sin t\cos t}4=0$. (ii) $w=\ln4$, $w'=0$.
:::

::: {.solution for="prob-mit1802n-2e-q2" status="draft"}
b) $\dfrac{dw}{dt}=\nabla w\cdot\dfrac{d\mathbf{r}}{dt}=y(-\sin t)+x\cos t=\cos^2t-\sin^2t=\cos2t$, zero for $t=\frac\pi4+\frac{n\pi}2$.

c) $\dfrac{d\mathbf{r}}{dt}=\langle1,2t,3t^2\rangle=\langle1,2,3\rangle$ at $t=1$, where the point is $(1,1,1)$: $\dfrac{df}{dt}=1-2+6=5$.
:::

::: {.solution for="prob-mit1802n-2e-q5" status="draft"}
a) By @exm-chain-rule-polar, $w_r=w_x\cos\theta+w_y\sin\theta$ and $\frac1rw_\theta=-w_x\sin\theta+w_y\cos\theta$. Squaring and adding, the cross terms cancel and $\cos^2\theta+\sin^2\theta=1$ gives $w_x^2+w_y^2$.

b) At $r=\sqrt2$, $\theta=\pi/4$ (the point $(1,1)$): $w_r=\frac{2-1}{\sqrt2}=\frac1{\sqrt2}$ and $w_\theta=r(-w_x\sin\theta+w_y\cos\theta)=\sqrt2\cdot\frac{-2-1}{\sqrt2}=-3$. Check: $w_r^2+\frac1{r^2}w_\theta^2=\frac12+\frac92=5=2^2+(-1)^2$.
:::

::: {.solution for="prob-mit1802n-2e-q7" status="draft"}
The left side is the gradient of the composite function with respect to $u,v$: $\langle f_u\ f_v\rangle$. By @thm-chain-rule-several-parameters, $f_u=f_xx_u+f_yy_u$ and $f_v=f_xx_v+f_yy_v$, which are the two entries of $\langle f_x\ f_y\rangle\begin{pmatrix}x_u&x_v\\y_u&y_v\end{pmatrix}$.
:::

::: {.solution for="prob-mit1802n-2e-q8" status="draft"}
a) $w_x=f'(u)\cdot\left(-\dfrac y{x^2}\right)$ and $w_y=f'(u)\cdot\dfrac1x$, so $xw_x+yw_y=-\dfrac yxf'+\dfrac yxf'=0$.

b) $w_x=2xf'$ and $w_y=-2yf'$, so $yw_x+xw_y=2xyf'-2xyf'=0$.
:::
