<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802f07-5-q1" status="draft"}
$f_x=3x^2-y^2-8x+3+2xy$ and $f_y=x^2-2xy$, so at $(\frac12,1)$: $\nabla f=\langle-\frac14,-\frac34\rangle$, $\lvert\nabla f\rvert=\frac{\sqrt{10}}4\approx0.791$.

a) By @thm-directional-derivative-gradient, $\frac{df}{ds}\big|_{\hat{\mathbf{u}}}=\nabla f\cdot\hat{\mathbf{u}}$ ranges from $-\frac{\sqrt{10}}4$ to $\frac{\sqrt{10}}4$.

b) The maximum is in the direction of the gradient, $\hat{\mathbf{u}}=\frac1{\sqrt{10}}\langle-1,-3\rangle$ ($\theta\approx251.6^\circ$); the minimum in the opposite direction $\frac1{\sqrt{10}}\langle1,3\rangle$ ($\theta\approx71.6^\circ$).

c) $\hat{\mathbf{u}}\perp\nabla f$: $\hat{\mathbf{u}}=\pm\frac1{\sqrt{10}}\langle3,-1\rangle$ ($\theta\approx341.6^\circ$ or $161.6^\circ$).

d) The applet should show values close to these. At the maximum (minimum) the direction $\hat{\mathbf{u}}$ points along (against) the gradient vector, which is perpendicular to the contour line; where $df/ds=0$, $\hat{\mathbf{u}}$ is tangent to the contour line.
:::

::: {.solution for="prob-mit1802f07-5-q2" status="draft"}
a) $\nabla g=\langle2x,z,y\rangle=\langle4,1,-1\rangle$ at $(2,-1,1)$; $g$ decreases fastest in the direction $-\nabla g$, i.e. $\hat{\mathbf{u}}=\frac1{\sqrt{18}}\langle-4,-1,1\rangle$.

b) $g(2,-1,1)=3$; we need $\Delta g=-1$. Along $(2,-1,1)+s\langle-4,-1,1\rangle$, $\Delta g\approx\nabla g\cdot s\langle-4,-1,1\rangle=-18s$, so $s=\frac1{18}$ and the estimate is
$$\Big(\frac{16}9,\ -\frac{19}{18},\ \frac{19}{18}\Big).$$
There $g=\frac{256}{81}-\frac{361}{324}=\frac{663}{324}\approx2.046$.
:::

::: {.solution for="prob-mit1802n-2d-q1" status="draft"}
a) $\nabla f=\langle3x^2,6y^2\rangle=\langle3,6\rangle$; $\mathbf{u}=\frac1{\sqrt2}\langle1,-1\rangle$; $\frac{df}{ds}=\frac{3-6}{\sqrt2}=-\frac3{\sqrt2}$.

b) $\nabla w=\langle y/z,\ x/z,\ -xy/z^2\rangle=\langle-1,2,2\rangle$; $\mathbf{u}=\frac13\langle1,2,-2\rangle$; $\frac{dw}{ds}=\frac{-1+4-4}3=-\frac13$.

e) $\nabla f=2(u+2v+3w)\langle1,2,3\rangle=\langle4,8,12\rangle$ (here $u+2v+3w=2$); $\mathbf{u}=\frac13\langle-2,2,-1\rangle$; $\frac{df}{ds}=\frac{-8+16-12}3=-\frac43$.
:::

::: {.solution for="prob-mit1802n-2d-q2" status="draft"}
b) $\nabla w=\langle y+z,\ x+z,\ x+y\rangle=\langle1,3,0\rangle$, $|\nabla w|=\sqrt{10}$.

(i) Maximum $\sqrt{10}$, minimum $-\sqrt{10}$.

(ii) Maximum in the direction $\frac1{\sqrt{10}}\langle1,3,0\rangle$, minimum in the direction $-\frac1{\sqrt{10}}\langle1,3,0\rangle$.

(iii) All unit vectors perpendicular to $\langle1,3,0\rangle$: $\mathbf{u}=\langle-3b,\ b,\ c\rangle$ with $10b^2+c^2=1$ (a circle of directions).
:::

::: {.solution for="prob-mit1802n-2d-q3" status="draft"}
a) $\nabla f=\langle y^2z^3,\ 2xyz^3,\ 3xy^2z^2\rangle=\langle4,12,36\rangle$, parallel to $\langle1,3,9\rangle$: $(x-3)+3(y-2)+9(z-1)=0$, i.e. $x+3y+9z=18$.

c) $\nabla f=2\langle x_0,y_0,-z_0\rangle$: $x_0(x-x_0)+y_0(y-y_0)-z_0(z-z_0)=0$. Since $x_0^2+y_0^2-z_0^2=0$ on the cone, this simplifies to $x_0x+y_0y-z_0z=0$ (for $(x_0,y_0,z_0)\ne\mathbf0$): every tangent plane of the cone passes through its vertex.
:::

::: {.solution for="prob-mit1802n-2d-q8" status="draft"}
At the origin $P=32$ and $\nabla P=\langle(y+2)e^z,(x+1)e^z,(x+1)(y+2)e^z\rangle=\langle2,1,2\rangle$. The closest point with $\Delta P=-0.9$ lies (to first order) in the direction of $-\nabla P$: with $\Delta\mathbf{r}=s\nabla P$, $\Delta P\approx|\nabla P|^2s=9s=-0.9$, so $s=-0.1$ and the point is approximately $(-0.2,-0.1,-0.2)$.
:::

::: {.solution for="prob-mit1802n-2d-q9" status="draft"}
(The picture shows nested closed level curves $w=1,\dots,5$, the values increasing inwards; numerical answers can only be read off the picture, so we describe how.)

a) At $A$ the gradient is perpendicular to the level curve $w=1$, points inwards (towards higher values), and has length about $1/d$, where $d$ is the distance from $A$ to the curve $w=2$ measured along the normal.

b) $\partial w/\partial x=0$ where the level curve $w=3$ has a horizontal tangent: its highest or lowest point.

c) $\partial w/\partial y=0$ where $w=3$ has a vertical tangent: its leftmost or rightmost point.

d) $\partial w/\partial x\approx\Delta w/\Delta x$ along the horizontal line through $P$, i.e. the change of level ($1$) divided by the horizontal distance to the next curve, with the sign of the change; likewise $\partial w/\partial y$ along the vertical line.

e), f) $dw/ds$ is the change of level divided by the distance from $Q$ to the next curve along the line through $Q$ in the given direction; it is near $0$ in the direction tangent to the level curve through $Q$.

g) At the top of the hill, inside the innermost curve $w=5$.
:::
