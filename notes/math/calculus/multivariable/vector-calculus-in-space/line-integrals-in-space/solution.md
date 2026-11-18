<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802f07-11-q5" status="draft"}
a) $dx=-\sin t\,dt$, $dy=\cos t\,dt$, $dz=dt$:
$$W=\int_0^{2\pi}\Big[-(a\sin t+b\cos t\sin^2t)\sin t+2\cos^3t\sin t+\cos^2t-t^2\Big]dt=-a\pi-0+0+\pi-\frac{8\pi^3}3 .$$
So $W=(1-a)\pi-\dfrac{8\pi^3}3$ (it does not depend on $b$).

b) $\operatorname{curl}\vec F=\langle R_y-Q_z,\ P_z-R_x,\ Q_x-P_y\rangle=\langle0,\ (a-1)\cos z,\ (4-2b)xy\rangle$. It is $\mathbf0$ everywhere exactly when $a=1$, $b=2$; then $\vec F$ is conservative (@thm-gradient-field-criterion-space), and otherwise it is not.

c) $f_x=\sin z+2xy^2$ gives $f=x\sin z+x^2y^2+g(y,z)$; $f_y=2x^2y+g_y=2x^2y$ gives $g=h(z)$; $f_z=x\cos z+h'(z)=x\cos z-z^2$ gives $h=-\frac{z^3}3+c$. So $f=x\sin z+x^2y^2-\frac{z^3}3$. Then $W=f(1,0,2\pi)-f(1,0,0)=-\frac{8\pi^3}3$, which agrees with (a) for $a=1$.
:::

::: {.solution for="prob-mit1802n-6d-q1" status="draft"}
a) $\int y\,dx+z\,dy-x\,dz=\int_0^1(t^2+2t^4-3t^3)\,dt=\frac13+\frac25-\frac34=-\frac1{60}$.

b) $x=y=z=t$: $\int_0^1(t+t-t)\,dt=\frac12$.

c) First segment: $y=z=0$, $dy=dz=0$: $0$. Second: $z=0$, $dx=dz=0$: $0$. Third: $x=1$, $dx=dy=0$: $\int_0^1-1\,dz=-1$. Total $-1$. (Different answers for the same endpoints: $\mathbf{F}$ is not a gradient field.)

d) $\int_0^{2\pi}\big(-t\cos t\sin t+t\sin t\cos t+\cos t\big)\,dt=\int_0^{2\pi}\cos t\,dt=0$.
:::

::: {.solution for="prob-mit1802n-6d-q2" status="draft"}
$\mathbf{F}=\nabla f$ with $f=\frac12(x^2+y^2+z^2)$, which is constant ($\frac{a^2}2$) on the sphere. By the fundamental theorem the integral is $f(P_1)-f(P_0)=0$. (Or: $\mathbf{F}\cdot d\mathbf{r}=\mathbf{r}\cdot\mathbf{v}\,dt=0$ since $\mathbf{v}\perp\mathbf{r}$ on the sphere, @cor-constant-length.)
:::

::: {.solution for="prob-mit1802n-6d-q4" status="draft"}
a) $\mathbf{F}=2x\mathbf{i}+2y\mathbf{j}+2z\mathbf{k}$.

b) (i) $\int_0^{2n\pi}\big(-2\cos t\sin t+2\sin t\cos t+2t\big)\,dt=(2n\pi)^2=4n^2\pi^2$.

(ii) The vertical segment from $(1,0,0)$ to $(1,0,2n\pi)$: $\int_0^{2n\pi}2z\,dz=4n^2\pi^2$.

(iii) $f(1,0,2n\pi)-f(1,0,0)=1+4n^2\pi^2-1=4n^2\pi^2$.
:::

::: {.solution for="prob-mit1802n-6d-q5" status="draft"}
The integral is $f(P_1)-f(P_0)\le1-(-1)=2$. It equals $2$ for a path from a point with $xyz=-\frac\pi2$ to one with $xyz=\frac\pi2$, e.g. the segment from $(1,1,-\frac\pi2)$ to $(1,1,\frac\pi2)$.
:::

::: {.solution for="prob-mit1802n-6e-q1" status="draft"}
All three are exact: in each the curl of $\langle M,N,P\rangle$ is $\mathbf0$ (@thm-gradient-field-criterion-space).

a) $d\Big(\dfrac{x^3+y^3+z^3}3\Big)$.

b) $M_y=2yz=N_x$, $M_z=y^2=P_x$, $N_z=2xy=P_y$. $f_x=y^2z$ gives $f=xy^2z+g(y,z)$; $f_y=2xyz+g_y=2xyz$, so $g=h(z)$; $f_z=xy^2+h'=xy^2$, so $h=c$: $d(xy^2z)$.

c) $M_y=6x^2+z=N_x$, $M_z=y=P_x$, $N_z=x=P_y$. $f_x=6x^2y+yz$ gives $f=2x^3y+xyz+g(y,z)$, and comparing with $N$ and $P$ shows $g$ is constant: $d(2x^3y+xyz)$.
:::

::: {.solution for="prob-mit1802n-6e-q2" status="draft"}
$\operatorname{curl}\mathbf{F}=\langle R_y-Q_z,\ P_z-R_x,\ Q_x-P_y\rangle=\langle xz^2-y,\ -yz^2,\ -x^2\rangle$.
:::

::: {.solution for="prob-mit1802n-6e-q3" status="draft"}
a) $R_y-Q_z=0-0$, $P_z-R_x=1-1$, $Q_x-P_y=2x-2x$: all $0$.

b) Antiderivatives: $f_x=2xy+z$ gives $f=x^2y+xz+g(y,z)$; then $f_y=x^2+g_y=x^2$ and $f_z=x+g_z=x$, so $g$ is constant: $f=x^2y+xz+c$.

Line integral from the origin along segments parallel to the axes, to $(x_1,0,0)$, then $(x_1,y_1,0)$, then $(x_1,y_1,z_1)$: the first gives $\int_0^{x_1}0\,dx=0$ (there $P=0$), the second $\int_0^{y_1}x_1^2\,dy=x_1^2y_1$, the third $\int_0^{z_1}x_1\,dz=x_1z_1$. So $f=x_1^2y_1+x_1z_1$, the same.
:::

::: {.solution for="prob-mit1802n-6e-q5" status="draft"}
$P_y=z^2=Q_x$ always. $P_z=2yz$ and $R_x=byz$: $b=2$. $Q_z=2xz+ay$ and $R_y=bxz+2y$: with $b=2$, $a=2$. Then $f_x=yz^2$ gives $f=xyz^2+g(y,z)$; $f_y=xz^2+g_y=xz^2+2yz$ gives $g=y^2z+h(z)$; $f_z=2xyz+y^2+h'=2xyz+y^2$ gives $h=c$. So $f=xyz^2+y^2z+c$.
:::
