<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802n-6b-q7" status="draft"}
On the cylinder $x^2+y^2=1$, $\hat{\mathbf{n}}=\langle x,y,0\rangle$ and $dS=dz\,d\theta$ (@prp-normal-and-surface-element), so $\mathbf{F}\cdot\hat{\mathbf{n}}=\dfrac{x^2+y^2}{1+z^2}=\dfrac1{1+z^2}$ and
$$\iint_S\mathbf{F}\cdot d\mathbf{S}=\int_0^{2\pi}\!\!\int_{-\infty}^\infty\frac{dz}{1+z^2}\,d\theta=2\pi\cdot\pi=2\pi^2 .$$
:::

::: {.solution for="prob-mit1802n-6a-q1" status="draft"}
a) Unit vectors pointing radially away from the origin (undefined at the origin).

b) Each vector is perpendicular to the $y$-axis and points towards it, with length equal to the distance $\sqrt{x^2+z^2}$ from the point to the $y$-axis.
:::

::: {.solution for="prob-mit1802n-6a-q2" status="draft"}
From $\mathbf{r}=\langle x,y,z\rangle$ to $\frac12\mathbf{r}$: $\mathbf{F}=-\frac12(x\mathbf{i}+y\mathbf{j}+z\mathbf{k})$.
:::

::: {.solution for="prob-mit1802n-6a-q3" status="draft"}
The velocity of a rotation with angular velocity vector $\omega\mathbf{i}$ is $\omega\mathbf{i}\times\mathbf{r}=\omega\mathbf{i}\times(x\mathbf{i}+y\mathbf{j}+z\mathbf{k})$: $\mathbf{F}=\omega(-z\mathbf{j}+y\mathbf{k})$. (At $(0,1,0)$ it points in the $+\mathbf{k}$ direction, as the right-hand rule requires.)
:::

::: {.solution for="prob-mit1802n-6a-q4" status="draft"}
$\mathbf{F}$ must be perpendicular to the normal $\langle3,-4,1\rangle$: $3M-4N+P=0$. So $\mathbf{F}=M\mathbf{i}+N\mathbf{j}+(4N-3M)\mathbf{k}$, with $M,N$ arbitrary functions of $x,y,z$.
:::

::: {.solution for="prob-mit1802n-6b-q1" status="draft"}
On the sphere $\mathbf{F}\cdot\mathbf{n}=a$, so the flux is $a\cdot4\pi a^2=4\pi a^3$.
:::

::: {.solution for="prob-mit1802n-6b-q2" status="draft"}
The outward normal of the cylinder is horizontal, so $\mathbf{k}\cdot\mathbf{n}=0$ and the flux is $0$.
:::

::: {.solution for="prob-mit1802n-6b-q3" status="draft"}
$\mathbf{n}=\frac1{\sqrt3}\langle1,1,1\rangle$, so $\mathbf{i}\cdot\mathbf{n}=\frac1{\sqrt3}$; the triangle is equilateral with side $\sqrt2$, area $\frac{\sqrt3}2$. Flux $=\frac12$ (the area of the projection of the triangle on the $yz$-plane).
:::

::: {.solution for="prob-mit1802n-6b-q4" status="draft"}
$\mathbf{F}\cdot\mathbf{n}=\frac{y^2}a$. Over the whole sphere, by symmetry $\iint y^2\,dS=\frac13\iint(x^2+y^2+z^2)\,dS=\frac13a^2\cdot4\pi a^2$; half of it is $\frac23\pi a^4$. So the flux is $\frac1a\cdot\frac23\pi a^4=\frac23\pi a^3$.
:::

::: {.solution for="prob-mit1802n-6b-q6" status="draft"}
$\mathbf{n}\,dS=\langle-2x,-2y,1\rangle\,dx\,dy$ (@prp-normal-and-surface-element), so $\mathbf{F}\cdot\mathbf{n}\,dS=(-2x^2-2y^2+z)\,dx\,dy=-(x^2+y^2)\,dx\,dy$ on $S$. Flux $=-\int_0^{2\pi}\!\int_0^1r^3\,dr\,d\theta=-\frac\pi2$. The position vector at a point of the bowl points away from the axis and up only slightly, so it crosses the surface from the inside of the bowl to the outside, i.e. against the upward normal.
:::

::: {.solution for="prob-mit1802n-6b-q8" status="draft"}
"To the right of the $xz$-plane" is $y\ge0$, i.e. $0\le\theta\le\pi$. $\mathbf{n}=\frac1a\langle x,y,0\rangle$, $dS=a\,dz\,d\theta$, $\mathbf{F}\cdot\mathbf{n}=\frac{y^2}a=a\sin^2\theta$:
$$\int_0^h\!\!\int_0^\pi a\sin^2\theta\cdot a\,d\theta\,dz=\frac{\pi a^2h}2 .$$
:::
