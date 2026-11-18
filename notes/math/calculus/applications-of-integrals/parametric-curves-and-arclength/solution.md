<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit1801f06-8a-q1" status="draft"}
a) $(x/a)^{2/k}=\cos^2t$ and $(y/a)^{2/k}=\sin^2t$, so
$$\Big(\frac xa\Big)^{2/k}+\Big(\frac ya\Big)^{2/k}=1\qquad(x,y\ge0).$$
For $0\le t\le\pi/2$ each curve runs from $(a,0)$ to $(0,a)$: $k=1$ is the quarter circle $x^2+y^2=a^2$; $k=2$ is the segment $x+y=a$; $k=3$ is the quarter astroid $x^{2/3}+y^{2/3}=a^{2/3}$, curving in towards the origin with cusps at the two ends.

b) $k=1$: a quarter of a circle of radius $a$, length $\frac{\pi a}2$. $k=2$: the segment from $(a,0)$ to $(0,a)$, length $\sqrt2\,a$.

c) $x'=-ak\cos^{k-1}t\sin t$ and $y'=ak\sin^{k-1}t\cos t$, so (@prp-arclength), for $0<t<\pi/2$,
$$s=\int_0^{\pi/2}ak\sin t\cos t\sqrt{\cos^{2k-4}t+\sin^{2k-4}t}\;dt .$$
- $k=1$: $\sqrt{\cos^{-2}t+\sin^{-2}t}=\frac1{\sin t\cos t}$, so $s=\int_0^{\pi/2}a\,dt=\frac{\pi a}2$.
- $k=2$: $s=2\sqrt2\,a\int_0^{\pi/2}\sin t\cos t\,dt=2\sqrt2\,a\cdot\frac12=\sqrt2\,a$.
- $k=3$: $\sqrt{\cos^2t+\sin^2t}=1$, so $s=3a\int_0^{\pi/2}\sin t\cos t\,dt=\frac{3a}2$.
:::

::: {.solution for="prob-mit1801f06-8a-q2" status="draft"}
a) (i) and (ii) are @prp-hyperbolic-identities. (iii) $\cosh2x=\frac{e^{2x}+e^{-2x}}2$, while $\cosh^2x=\frac{e^{2x}+2+e^{-2x}}4=\frac{1+\cosh2x}2$.

b) By (ii), $x^2-y^2=1$, and $x=\cosh t\ge1$: the right branch of the hyperbola $x^2-y^2=1$ (traced upwards as $t$ increases).

c) (i) $y=\cosh x$ is even, with minimum $(0,1)$, concave up ($y''=\cosh x>0$), growing like $\frac12e^{\lvert x\rvert}$; it looks like a parabola near $0$ ($\cosh x\approx1+\frac{x^2}2$) but rises much faster.
(ii) $ds=\sqrt{1+\sinh^2x}\,dx=\cosh x\,dx$, so the length from $(0,1)$ to $(x_1,\cosh x_1)$ is $\int_0^{x_1}\cosh x\,dx=\sinh x_1$.

d) By @prp-surface-of-revolution with $y=\cosh x$, $ds=\cosh x\,dx$:
$$A=\int_0^{x_1}2\pi\cosh^2x\,dx=\pi\int_0^{x_1}(1+\cosh2x)\,dx=\pi\Big(x_1+\frac{\sinh2x_1}2\Big)=\pi(x_1+\sinh x_1\cosh x_1).$$
For the whole catenoid between the circles at $x=\pm x_1$ the area is twice this, $2\pi(x_1+\sinh x_1\cosh x_1)$.
:::

::: {.solution for="prob-mit1801f06-8b-q2" status="draft"}
a) Picture: the ball $x^2+y^2+z^2\le r^2$ cut by the plane at height $r-h$; the solid is the top piece. Rotating the region under $x=\sqrt{r^2-y^2}$, $r-h\le y\le r$, about the $y$-axis, horizontal slices are disks of radius $\sqrt{r^2-y^2}$ (@prp-volume-by-slices):
$$V=\int_{r-h}^r\pi(r^2-y^2)\,dy=\pi\Big[r^2h-\frac{r^3-(r-h)^3}3\Big]=\pi\Big[r^2h-\frac{3r^2h-3rh^2+h^3}3\Big]=\pi\Big(rh^2-\frac{h^3}3\Big).$$
Checks: $h=0$ gives $0$; $h=r$ gives $\frac23\pi r^3$, half a ball; $h=2r$ gives $\pi(4r^3-\frac83r^3)=\frac43\pi r^3$. We need $0\le h\le2r$ because the cap cannot be higher than the diameter of the sphere.

b) By @exm-surface-of-sphere, every band of a sphere of radius $r$ of height $h$ has area $2\pi rh$; so the cap has area $S=2\pi rh$. Checks: $0$; $2\pi r^2$ (hemisphere); $4\pi r^2$ (sphere).

c) Fix $V$. From (a), $r=\frac{V}{\pi h^2}+\frac h3$, so
$$S(h)=2\pi rh=\frac{2V}h+\frac{2\pi h^2}3 .$$
$S'(h)=-\frac{2V}{h^2}+\frac{4\pi h}3=0$ gives $V=\frac{2\pi h^3}3$. Substituting into (a): $\pi(rh^2-\frac{h^3}3)=\frac{2\pi h^3}3$, so $rh^2=h^3$ and $h=r$. Since $S\to\infty$ as $h\to0^+$ and $S''=\frac{4V}{h^3}+\frac{4\pi}3>0$, this is the minimum; it also satisfies $h\le2r$. So $h/r=1$: the bubble is a **hemisphere**, meeting the table at a right angle.
:::
