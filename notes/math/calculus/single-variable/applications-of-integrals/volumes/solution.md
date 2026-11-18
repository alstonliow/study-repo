<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

::: {.solution for="prob-mit1801f06-5-q3" status="draft"}
The region is non-empty only where $z^2/2<z$, i.e. $0<z<2$. At height $z$ the cross-section is the part of the first quadrant between the lines $x+y=z^2/2$ and $x+y=z$; the triangle $x,y>0$, $x+y<s$ has area $s^2/2$, so the cross-section has area
$$A(z)=\frac{z^2}2-\frac{(z^2/2)^2}2=\frac{z^2}2-\frac{z^4}8 .$$
By @prp-volume-by-slices, $V=\int_0^2\Big(\frac{z^2}2-\frac{z^4}8\Big)dz=\frac86-\frac{32}{40}=\frac43-\frac45=\frac8{15}$.
:::

::: {.solution for="prob-mit1801f06-7-q2" status="draft"}
The vertical strip at $x\in[b-a,b+a]$ has height $2\sqrt{a^2-(x-b)^2}$ and sweeps a shell of radius $x$ (@def-disks-and-shells):
$$V=\int_{b-a}^{b+a}2\pi x\cdot2\sqrt{a^2-(x-b)^2}\,dx .$$
Put $u=x-b$: $V=4\pi\int_{-a}^a(u+b)\sqrt{a^2-u^2}\,du$. The term $u\sqrt{a^2-u^2}$ is odd and integrates to $0$; $\int_{-a}^a\sqrt{a^2-u^2}\,du=\frac{\pi a^2}2$ (@exm-trig-sub-area-circle). So
$$V=4\pi b\cdot\frac{\pi a^2}2=2\pi^2a^2b=(\pi a^2)(2\pi b),$$
the area of the disk times the distance travelled by its centre.
:::

::: {.solution for="prob-mit1801n-4b-q1" status="draft"}
By disks (@def-disks-and-shells):

d) $\int_0^a\pi x^2dx=\frac{\pi a^3}3$ (a cone of radius and height $a$).

e) The region is $0\le x\le2$: $\int_0^2\pi(2x-x^2)^2dx=\pi\int_0^2(4x^2-4x^3+x^4)\,dx=\pi\Big(\frac{32}3-16+\frac{32}5\Big)=\frac{16\pi}{15}$.
:::

::: {.solution for="prob-mit1801n-4b-q2" status="draft"}
By shells:

e) $\int_0^22\pi x(2x-x^2)\,dx=2\pi\Big(\frac{16}3-4\Big)=\frac{8\pi}3$.

g) $\int_0^a2\pi x\sqrt{ax}\,dx=2\pi\sqrt a\cdot\frac25a^{5/2}=\frac{4\pi a^3}5$.
:::

::: {.solution for="prob-mit1801n-4b-q5" status="draft"}
The solid is two cones joined at their bases. Each has height $\frac a2$ (half the side) and base radius equal to the triangle's height $\frac{\sqrt3}2a$. So
$$V=2\cdot\frac13\pi\Big(\frac{\sqrt3}2a\Big)^2\frac a2=\frac{\pi a^3}4 .$$
:::

::: {.solution for="prob-mit1801n-4b-q6" status="draft"}
At $x$ the hypotenuse is the chord of length $c=2\sqrt{a^2-x^2}$. An isosceles right triangle with hypotenuse $c$ has legs $c/\sqrt2$ and area $c^2/4=a^2-x^2$. By @prp-volume-by-slices,
$$V=\int_{-a}^a(a^2-x^2)\,dx=\frac{4a^3}3 .$$
:::

::: {.solution for="prob-mit1801n-4b-q7" status="draft"}
At height $y$ ($0\le y\le1$) the profile runs from $x=-1+\sqrt y$ (on $y=(x+1)^2$) to $x=1-\sqrt y$ (on $y=(x-1)^2$), so the square cross-section has side $2-2\sqrt y$ and area $4(1-\sqrt y)^2$. Then
$$V=\int_0^14\big(1-2\sqrt y+y\big)\,dy=4\Big(1-\frac43+\frac12\Big)=\frac23 .$$
:::

::: {.solution for="prob-mit1801n-4c-q1" status="draft"}
By shells, the strip at $x\in[b-a,b+a]$ has height $2\sqrt{a^2-(x-b)^2}$:
$$V=\int_{b-a}^{b+a}2\pi x\cdot2\sqrt{a^2-(x-b)^2}\,dx .$$
(Its value is $2\pi^2a^2b$, computed in @prob-mit1801f06-7-q2.)
:::

::: {.solution for="prob-mit1801n-4c-q2" status="draft"}
By shells: $\int_0^12\pi x\cdot x^2\,dx=\frac{\pi}2$.
:::

::: {.solution for="prob-mit1801n-4c-q3" status="draft"}
The region lies between $x=0$ and $x=y^2$ for $0\le y\le1$.

- Shells: $\int_0^12\pi x(1-\sqrt x)\,dx=2\pi\Big(\frac12-\frac25\Big)=\frac\pi5$.
- Disks: the slice at height $y$ is a disk of radius $y^2$: $\int_0^1\pi y^4\,dy=\frac\pi5$.
:::
