<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

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

::: {.solution for="prob-mit1801n-4e-q2" status="draft"}
$x^2=t^2+2+\frac1{t^2}$ and $y^2=t^2-2+\frac1{t^2}$, so $x^2-y^2=4$: a hyperbola ($t>0$ gives the right branch, $t<0$ the left).
:::

::: {.solution for="prob-mit1801n-4e-q3" status="draft"}
$(x-1)^2+(y-4)^2=\sin^2t+\cos^2t=1$: the circle of radius $1$ centred at $(1,4)$.
:::

::: {.solution for="prob-mit1801n-4e-q8" status="draft"}
Put the origin at the centre, the $y$-axis towards 12 o'clock, and measure $t$ in hours from noon ($0\le t\le1$). The hour hand turns clockwise by $2\pi$ in $12$ hours, so its angle from the $y$-axis is $\frac{\pi t}6$, and the snail is at distance $t$ from the centre:
$$x=t\sin\frac{\pi t}6,\qquad y=t\cos\frac{\pi t}6 .$$
:::

::: {.solution for="prob-mit1801n-4f-q1" status="draft"}
$y'=x(2+x^2)^{1/2}$, so $1+y'^2=1+2x^2+x^4=(1+x^2)^2$ and $ds=(1+x^2)\,dx$ (@prp-arclength). The length is $\int_1^2(1+x^2)\,dx=1+\frac73=\frac{10}3$.
:::

::: {.solution for="prob-mit1801n-4f-q4" status="draft"}
As in @exm-arclength-semicubical, $ds=t\sqrt{4+9t^2}\,dt$, so $s=\frac1{27}(4+9t^2)^{3/2}\Big|_0^2=\frac{40^{3/2}-8}{27}=\frac{80\sqrt{10}-8}{27}\approx9.073$.
:::

::: {.solution for="prob-mit1801n-4f-q5" status="draft"}
$x'=1-\frac1{t^2}$ and $y'=1+\frac1{t^2}$, so $x'^2+y'^2=2+\frac2{t^4}$ and
$$s=\int_1^2\sqrt{2+\frac2{t^4}}\,dt=\sqrt2\int_1^2\frac{\sqrt{t^4+1}}{t^2}\,dt .$$
:::

::: {.solution for="prob-mit1801n-4f-q8" status="draft"}
$x'=e^t(\cos t-\sin t)$, $y'=e^t(\sin t+\cos t)$, so $x'^2+y'^2=2e^{2t}$ and $ds=\sqrt2\,e^tdt$. The length is $\sqrt2\,(e^{10}-1)$.
:::

::: {.solution for="prob-mit1801n-4g-q2" status="draft"}
The segment is $0\le x\le\frac12$, with $ds=\sqrt5\,dx$. By @prp-surface-of-revolution,
$$A=\int_0^{1/2}2\pi(1-2x)\sqrt5\,dx=2\pi\sqrt5\big[x-x^2\big]_0^{1/2}=\frac{\sqrt5\,\pi}2 ,$$
the lateral area of a cone of radius $1$ and slant height $\frac{\sqrt5}2$.
:::

::: {.solution for="prob-mit1801n-4g-q5" status="draft"}
Around the $y$-axis a piece $ds$ at distance $x$ from the axis sweeps $2\pi x\,ds$, with $ds=\sqrt{1+4x^2}\,dx$:
$$A=\int_0^42\pi x\sqrt{1+4x^2}\,dx=\frac\pi6(1+4x^2)^{3/2}\Big|_0^4=\frac\pi6\big(65^{3/2}-1\big)\approx273.9 .$$
:::
