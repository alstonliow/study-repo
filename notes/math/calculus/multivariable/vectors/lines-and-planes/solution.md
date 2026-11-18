<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802f07-2-q1" status="draft"}
a) $\overrightarrow{AB}=\langle1,-3,1\rangle$, $\overrightarrow{CD}=\langle-1,4,-2\rangle$, and $\mathbf{N}=\overrightarrow{AB}\times\overrightarrow{CD}=\langle2,1,1\rangle$ is perpendicular to both lines. The planes with normal $\mathbf{N}$ through $A$ and through $C$ are $2x+y+z=8$ and $2x+y+z=6$. Moving from one to the other along the unit normal $\mathbf{N}/\sqrt6$ changes $2x+y+z$ at the rate $\sqrt6$ per unit length, so their distance is $\dfrac{8-6}{\sqrt6}=\dfrac{\sqrt6}3\approx0.816$.

b) $P_1(t_1)=(2+t_1,\ 4-3t_1,\ t_1)$ and $P_2(t_2)=(1-t_2,\ 1+4t_2,\ 3-2t_2)$. With $\mathbf{w}=\overrightarrow{P_1P_2}=\langle-1-t_1-t_2,\ -3+3t_1+4t_2,\ 3-t_1-2t_2\rangle$, the conditions $\mathbf{w}\cdot\overrightarrow{AB}=0$ and $\mathbf{w}\cdot\overrightarrow{CD}=0$ are
$$11t_1+15t_2=11,\qquad 15t_1+21t_2=17,$$
so $t_1=-4$, $t_2=\frac{11}3$. Then $P_1=(-2,16,-4)$, $P_2=(-\frac83,\frac{47}3,-\frac{13}3)$, $\mathbf{w}=\langle-\frac23,-\frac13,-\frac13\rangle$ and the distance is $\lvert\mathbf{w}\rvert=\frac{\sqrt6}3$, as in (a).
:::

::: {.solution for="prob-mit1802f07-3-q1" status="draft"}
a) The line from $E$ to $P$ is $E+s\,\overrightarrow{EP}=(2+s(x_0-2),\ sy_0,\ sz_0)$; it meets $x=0$ at $s=\frac2{2-x_0}$, so
$$Q=\Big(\frac{2y_0}{2-x_0},\ \frac{2z_0}{2-x_0}\Big).$$
The assumption $x_0<2$ means the object is on the same side of the eye as the screen, the only points one can see through the screen; for $x_0\ge2$ the segment from $P$ to the eye does not meet the screen.

b) A segment: the segment and $E$ lie in one plane (unless the line passes through $E$, when the image is a single point), and the lines from $E$ to its points sweep out a triangle in that plane, which meets the screen in a segment.

c) $P_0\mapsto(-2,\frac23)$ (factor $\frac23$) and $P_1\mapsto(2,3)$ (factor $\frac12$): the segment from $(-2,\frac23)$ to $(2,3)$.

d) The bird is at $P(t)=P_0+t\overrightarrow{P_0P_1}=(-1-t,\ -3+7t,\ 1+5t)$, so its image is
$$y(t)=\frac{2(7t-3)}{t+3},\qquad z(t)=\frac{2(5t+1)}{t+3}.$$
This moves along the straight line through $(-2,\frac23)$ and $(2,3)$ (by (b)), and as $t\to\infty$ it tends to the vanishing point $(14,10)$, without reaching it. So the image is the segment from $(-2,\frac23)$ to $(14,10)$, the endpoint excluded.

e) The fence top is the line $x=1$, $z=1$. The plane through $E$ and this line is $z=2-x$. A point with $x<1$ is hidden when the segment from it to $E$ crosses $x=1$ below the top, i.e. when it lies below that plane: $z<2-x$. For the bird, $1+5t<3+t$, i.e. $t<\frac12$. So the bird is hidden from $P_0$ until $t=\frac12$, at $(-\frac32,\frac12,\frac72)$; on the screen, the part from $(-2,\frac23)$ to $(\frac27,2)$ is hidden (the top of the fence appears as the line $z=2$).
:::

::: {.solution for="prob-mit1802n-1e-q1" status="draft"}
a) $(x-2)+2y-2(z+1)=0$, i.e. $x+2y-2z=4$.

b) $\mathbf{N}=\langle1,1,0\rangle\times\langle2,-1,3\rangle=\langle3,-3,-3\rangle$: $x-y-z=0$.

c) $\langle1,-1,1\rangle\times\langle-2,3,1\rangle=\langle-4,-3,1\rangle$: $4x+3y-z=3$.

d) $\dfrac xa+\dfrac yb+\dfrac zc=1$ (each intercept satisfies it, and it is a plane).

e) The plane contains $\langle-1,1,0\rangle$ (from the first point to the second) and $\langle1,-1,2\rangle$; their cross product is $\langle2,2,0\rangle$. So $x+y=1$.
:::

::: {.solution for="prob-mit1802n-1e-q2" status="draft"}
The angle between the normals: $\cos\theta=\dfrac{\langle2,-1,1\rangle\cdot\langle1,1,2\rangle}{\sqrt6\sqrt6}=\dfrac36=\dfrac12$, so $\theta=60^\circ$ (the supplementary angle $120^\circ$ is the other dihedral angle).
:::

::: {.solution for="prob-mit1802n-1e-q3" status="draft"}
a) $x=1+2t$, $y=-t$, $z=-1+3t$.

b) Direction $\langle1,-1,2\rangle$: $x=2+t$, $y=-1-t$, $z=-1+2t$.

c) $(1,1,1)$ lies in the plane. A line through it lies in the plane exactly when its direction $\langle a,b,c\rangle$ is perpendicular to $\langle1,2,-1\rangle$, i.e. $c=a+2b$: $x=1+at$, $y=1+bt$, $z=1+(a+2b)t$, with $(a,b)\ne(0,0)$.
:::

::: {.solution for="prob-mit1802n-1e-q4" status="draft"}
The line is $(2t,\ 1-t,\ 2+t)$. Then $x+4y+z=2t+4-4t+2+t=6-t=4$ gives $t=2$: the point $(4,-1,4)$.
:::

::: {.solution for="prob-mit1802n-1e-q5" status="draft"}
The line is $(1+t,\ 1+2t,\ -1-t)$. Then $2x-y+z=2+2t-1-2t-1-t=-t=1$ gives $t=-1$: the point $(0,-1,0)$.
:::

::: {.solution for="prob-mit1802n-1e-q6" status="draft"}
The closest point of the plane to $O$ is the foot $F$ of the perpendicular from $O$; for any point $P$ of the plane, $OP=OF+FP$ with $FP\perp\mathbf{n}$, so the component $OP\cdot\mathbf{n}=OF\cdot\mathbf{n}=\pm D$. With $P=(x,y,z)$ on the plane and $\mathbf{n}=\langle a,b,c\rangle/\sqrt{a^2+b^2+c^2}$:
$$D=|OP\cdot\mathbf{n}|=\frac{|ax+by+cz|}{\sqrt{a^2+b^2+c^2}}=\frac{|d|}{\sqrt{a^2+b^2+c^2}} .$$
:::

::: {.solution for="prob-mit1802n-1h-q3" status="draft"}
a) By @thm-square-system-geometry there is a non-trivial solution exactly when the determinant is $0$: $\begin{vmatrix}1&-1&1\\2&1&1\\-1&c&2\end{vmatrix}=c+8=0$, so $c=-8$.

b) The system is $(2-c)x+y=0$, $(-1-c)y=0$, with determinant $(2-c)(-1-c)$: $c=2$ or $c=-1$.

c) For $c=-8$ we need $\mathbf{x}$ orthogonal to $\langle1,-1,1\rangle$, $\langle2,1,1\rangle$ and $\langle-1,-8,2\rangle$. The first two give $\langle1,-1,1\rangle\times\langle2,1,1\rangle=\langle-2,1,3\rangle$, and indeed $\langle-1,-8,2\rangle\cdot\langle-2,1,3\rangle=2-8+6=0$. So $\mathbf{x}=(-2,1,3)$ (or any multiple).
:::

::: {.solution for="prob-mit1802n-1h-q7" status="draft"}
a) The conditions are the linear system $a\cos x_1+b\sin x_1=y_1$, $a\cos x_2+b\sin x_2=y_2$, with determinant $\cos x_1\sin x_2-\sin x_1\cos x_2=\sin(x_2-x_1)$. It is non-zero exactly when $x_2-x_1$ is not a multiple of $\pi$, and then there is exactly one solution $(a,b)$.

b) If $x_2=x_1+n\pi$ then $\cos x_2=(-1)^n\cos x_1$ and $\sin x_2=(-1)^n\sin x_1$, so every such $f$ has $f(x_2)=(-1)^nf(x_1)$. Solutions exist exactly when $y_2=(-1)^ny_1$, and then there are infinitely many (one equation for two unknowns).
:::
