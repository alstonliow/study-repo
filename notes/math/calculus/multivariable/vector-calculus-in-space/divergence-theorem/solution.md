<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802f07-11-q2" status="draft"}
a) $z\to-z$ exchanges $P_1$ and $P_2$ and fixes $P_0,P_3$, so it exchanges the faces $P_0P_1P_3$ and $P_0P_2P_3$ (and maps each of $P_0P_1P_2$, $P_1P_2P_3$ to itself).

b) The tetrahedron lies in $y\ge0$ and $x\le1$.
- $P_0P_1P_2$ lies in the plane $y=0$: outward normal $-\hat\jmath$.
- $P_1P_2P_3$ lies in the plane $x=1$: outward normal $\hat\imath$.
- $P_0P_1P_3$: $\overrightarrow{P_0P_1}\times\overrightarrow{P_0P_3}=\langle1,0,1\rangle\times\langle1,1,0\rangle=\langle-1,1,1\rangle$; the plane is $-x+y+z=0$, and $P_2$ gives $-2<0$, so this normal points away from the tetrahedron.
- $P_0P_2P_3$: by symmetry, $\langle-1,1,-1\rangle$.

c) Parametrise a face $P_0+s\mathbf{U}+t\mathbf{V}$ ($s,t\ge0$, $s+t\le1$, area $\frac12$ in the $st$-plane), with $\hat{\mathbf{n}}\,dS=(\mathbf{U}\times\mathbf{V})\,ds\,dt$ (@prp-normal-and-surface-element).
- $P_0P_1P_2$: $y=0$, so $\vec F=\mathbf 0$: flux $0$.
- $P_1P_2P_3$: $\vec F\cdot\hat\imath=y$; in the plane $x=1$ the face is the triangle with $(y,z)$-vertices $(0,1),(0,-1),(1,0)$, of area $1$ and centroid $y=\frac13$: flux $\frac13$.
- $P_0P_1P_3$: $\mathbf{r}=s\langle1,0,1\rangle+t\langle1,1,0\rangle$, $y=t$, $\vec F\cdot\langle-1,1,1\rangle=-t$: flux $=-\iint t\,ds\,dt=-\frac16$.
- $P_0P_2P_3$: by symmetry, $-\frac16$.

d) Total flux $=0+\frac13-\frac16-\frac16=0$, and $\operatorname{div}\vec F=0$ gives $\iiint0\,dV=0$. The two sides agree.
:::

::: {.solution for="prob-mit1802f07-11-q3" status="draft"}
a) $f_x=-x(x^2+y^2+z^2)^{-3/2}$ and similarly, so $\vec F=-\dfrac{\langle x,y,z\rangle}{\rho^3}$: at each point it points towards the origin, with length $1/\rho^2$ (like the gravitational field of a point mass at the origin).

b) On the sphere, with outward $\hat{\mathbf{n}}=\langle x,y,z\rangle/a$: $\vec F\cdot\hat{\mathbf{n}}=-\frac{a^2}{a^4}=-\frac1{a^2}$, so the flux is $-\frac1{a^2}\cdot4\pi a^2=-4\pi$.

c) $\frac{\partial}{\partial x}\big(-x\rho^{-3}\big)=-\rho^{-3}+3x^2\rho^{-5}$; adding the three terms, $\operatorname{div}\vec F=-3\rho^{-3}+3(x^2+y^2+z^2)\rho^{-5}=0$ for $\rho\ne0$. No contradiction: $\vec F$ is not defined at the origin, which lies inside the sphere, so the divergence theorem does not apply to the ball.
:::

::: {.solution for="prob-mit1802f07-11-q4" status="draft"}
a) $\operatorname{div}(\nabla f)=(f_x)_x+(f_y)_y+(f_z)_z=\nabla^2f$; apply the divergence theorem (@thm-divergence-theorem) to $\nabla f$.

b) $\operatorname{div}(f\nabla f)=(ff_x)_x+(ff_y)_y+(ff_z)_z=f_x^2+f_y^2+f_z^2+f(f_{xx}+f_{yy}+f_{zz})=\lvert\nabla f\rvert^2+f\nabla^2f$; apply the divergence theorem to $f\nabla f$.

c) The left side of (b) is $0$ because $f=0$ on $S$, and $f\nabla^2f=0$ in $D$. So $\iiint_D\lvert\nabla f\rvert^2\,dV=0$. The integrand is continuous and $\ge0$, so it is $0$ everywhere: $\nabla f=\mathbf 0$ in $D$. Hence $f$ is constant (on each connected piece of $D$, along any path $f$ does not change by @thm-ftc-line-integrals), and the constant is its boundary value $0$.

d) $h=f-g$ is harmonic in $D$ (the Laplacian is linear) and zero on $S$, so $h=0$ by (c).
:::

::: {.solution for="prob-mit1802n-6c-q1" status="draft"}
a) $\operatorname{div}\mathbf{F}=2xy+x+x=2xy+2x$.
:::

::: {.solution for="prob-mit1802n-6c-q2" status="draft"}
$\frac{\partial}{\partial x}(\rho^nx)=\rho^n+n\rho^{n-1}\frac x\rho x=\rho^n+n\rho^{n-2}x^2$; adding the three terms, $\operatorname{div}\mathbf{F}=3\rho^n+n\rho^{n-2}\rho^2=(n+3)\rho^n$. It is $0$ exactly for $n=-3$ (away from the origin).
:::

::: {.solution for="prob-mit1802n-6c-q3" status="draft"}
Volume side: $\operatorname{div}\mathbf{F}=3$, half-ball volume $\frac23\pi a^3$: $2\pi a^3$. Surface side: on the hemisphere $\mathbf{F}\cdot\mathbf{n}=a$, area $2\pi a^2$, flux $2\pi a^3$; on the disc $\mathbf{n}=-\mathbf{k}$ and $\mathbf{F}\cdot\mathbf{n}=-z=0$, flux $0$. Both sides are $2\pi a^3$.
:::

::: {.solution for="prob-mit1802n-6c-q5" status="draft"}
$\operatorname{div}\mathbf{F}=1$, so the outward flux is the volume of the tetrahedron, $\frac16$.
:::

::: {.solution for="prob-mit1802n-6c-q6" status="draft"}
$\mathbf{F}=z\mathbf{k}$ has $\operatorname{div}\mathbf{F}=1$, so the outward flux is the volume of the cone of height $1$ and base radius $1$: $\frac\pi3$.
:::

::: {.solution for="prob-mit1802n-6c-q7" status="draft"}
Volume side: $\operatorname{div}\mathbf{F}=2x+x=3x$, and $\iiint3x\,dV=0$ by symmetry. Surface side: $\mathbf{F}$ has no $\mathbf{k}$-component, so top and bottom give $0$; on the side $\mathbf{n}=\langle x,y,0\rangle$, $\mathbf{F}\cdot\mathbf{n}=x^3+xy^2=x=\cos\theta$, $dS=dz\,d\theta$, and $\int_0^1\!\int_0^{2\pi}\cos\theta\,d\theta\,dz=0$. Both sides are $0$.
:::

::: {.solution for="prob-mit1802n-6c-q8" status="draft"}
a) The whole sphere with outward normal is $S_1$ together with $S_2$ reversed (the outward normal of the lower hemisphere points down). By the divergence theorem $\iint_{S_1}-\iint_{S_2}=\iiint\operatorname{div}\mathbf{F}\,dV=0$. Physically: there are no sources or sinks inside, so whatever flows in through the bottom hemisphere flows out through the top one.

b) If $\operatorname{div}\mathbf{F}=0$ in the solid bounded by $S$, and a closed curve $C$ on $S$ cuts it into two pieces $S_1,S_2$, oriented so that both normals point "the same way" across the solid (one outward, the other inward), then $\mathbf{F}$ has the same flux through $S_1$ and $S_2$. Equivalently, the outward flux through any closed surface is $0$.
:::
