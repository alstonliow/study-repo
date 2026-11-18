<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802f07-12-q1" status="draft"}
a) The order $ABC$ is compatible with the normal $\overrightarrow{AB}\times\overrightarrow{AC}$ (right-hand rule). Using the outward normals of PS 11 Problem 2: $P_0P_1P_3$ (normal $\langle-1,1,1\rangle=\overrightarrow{P_0P_1}\times\overrightarrow{P_0P_3}$), $P_0P_3P_2$ (since $\overrightarrow{P_0P_2}\times\overrightarrow{P_0P_3}=\langle1,-1,1\rangle$ points inwards), $P_0P_2P_1$ (since $\overrightarrow{P_0P_1}\times\overrightarrow{P_0P_2}=\langle0,2,0\rangle$ points inwards) and $P_1P_2P_3$ ($\overrightarrow{P_1P_2}\times\overrightarrow{P_1P_3}=\langle2,0,0\rangle$, outwards).

b) $\vec F\cdot d\vec r=yz\,dy-y^2\,dz$. On $P_0P_1$, $y=0$: $0$. On $P_1P_3$: $(1,t,1-t)$, $dy=dt$, $dz=-dt$: $\int_0^1\big(t(1-t)+t^2\big)dt=\int_0^1t\,dt=\frac12$. On $P_3P_0$: $z=0$ and $dz=0$: $0$. Work $=\frac12$.

c) $\operatorname{curl}\vec F=\langle R_y-Q_z,\ P_z-R_x,\ Q_x-P_y\rangle=\langle-2y-y,0,0\rangle=-3y\,\hat\imath$, which is $-3$ times the field of PS 11 Problem 2. So the fluxes of the curl, i.e. by Stokes the works around the faces, are $-3$ times those fluxes: $P_0P_2P_1$: $0$; $P_1P_2P_3$: $-1$; $P_0P_1P_3$: $\frac12$ (agreeing with (b)); $P_0P_3P_2$: $\frac12$.

d) $0-1+\frac12+\frac12=0$.
(i) Each edge of the tetrahedron belongs to two faces, and the compatible orientations traverse it in opposite directions; so the twelve edge integrals cancel in pairs.
(ii) The sum is the flux of $\operatorname{curl}\vec F$ out of the closed surface, which by the divergence theorem is $\iiint\operatorname{div}(\operatorname{curl}\vec F)\,dV=0$ (@thm-div-curl-zero).
:::

::: {.solution for="prob-mit1802n-6f-q1" status="draft"}
$C$ is the unit circle in the $xy$-plane, counterclockwise (compatible with the outward normal), $x=\cos t$, $y=\sin t$, $z=0$.

a) $\operatorname{curl}\mathbf{F}=\mathbf0$, so the flux side is $0$; and $\oint x\,dx+y\,dy+z\,dz=\int_0^{2\pi}(-\cos t\sin t+\sin t\cos t)\,dt=0$.

b) $\operatorname{curl}\mathbf{F}=\langle-1,-1,-1\rangle$ and $\mathbf{n}=\langle x,y,z\rangle$: flux $=-\iint(x+y+z)\,dS=-\iint z\,dS=-\int_0^{2\pi}\!\int_0^{\pi/2}\cos\phi\sin\phi\,d\phi\,d\theta=-\pi$ (the $x$, $y$ terms vanish by symmetry). Line integral: $\oint y\,dx+z\,dy+x\,dz=\int_0^{2\pi}-\sin^2t\,dt=-\pi$.
:::

::: {.solution for="prob-mit1802n-6f-q2" status="draft"}
Take the upward normal $\mathbf{n}=\frac1{\sqrt3}\langle1,1,1\rangle$ and $C$ counterclockwise seen from above.

Flux: $\operatorname{curl}\mathbf{F}=\langle-1,-1,-1\rangle$, $\operatorname{curl}\mathbf{F}\cdot\mathbf{n}=-\sqrt3$. By @prp-normal-and-surface-element, $dS=\frac{|\mathbf{N}|}{\mathbf{N}\cdot\mathbf{k}}dx\,dy=\sqrt3\,dx\,dy$, so the area of $S$ is $\sqrt3\pi$ and the flux is $-\sqrt3\cdot\sqrt3\pi=-3\pi$.

Line integral: $x=\cos t$, $y=\sin t$, $z=-\cos t-\sin t$, $dz=(\sin t-\cos t)\,dt$:
$$y\,dx+z\,dy+x\,dz=\big(-\sin^2t-\cos^2t-\sin t\cos t+\cos t\sin t-\cos^2t\big)dt=-(1+\cos^2t)\,dt,$$
and $\int_0^{2\pi}-(1+\cos^2t)\,dt=-3\pi$.
:::

::: {.solution for="prob-mit1802n-6f-q3" status="draft"}
$\mathbf{F}=\nabla(xyz)$, so $\operatorname{curl}\mathbf{F}=\mathbf0$ and the flux side is $0$. The work around the closed boundary of the rectangle is also $0$, by the fundamental theorem for line integrals. (Directly: on the edges $z=0$ and $z=1$ with $x=y=t$, $\mathbf{F}\cdot d\mathbf{r}=2tz\,dt$, giving $0$ and $\pm1$; on the vertical edges $x=y=0$ gives $0$ and $x=y=1$ gives $\int dz=\pm1$; with the boundary traversed once, the $+1$ and $-1$ cancel.)
:::

::: {.solution for="prob-mit1802n-6f-q5" status="draft"}
$\nabla\times\mathbf{F}=\langle0,\ -2x,\ 2\rangle$.

(a) Top disc ($\mathbf{n}=\mathbf{k}$): $\iint2\,dA=2\pi a^2$. Side ($\mathbf{n}=\frac1a\langle x,y,0\rangle$, $dS=a\,dz\,d\theta$): $(\nabla\times\mathbf{F})\cdot\mathbf{n}\,dS=-2xy\,dz\,d\theta=-2a^2\cos\theta\sin\theta\,dz\,d\theta$, which integrates to $0$. Total $2\pi a^2$.

(b) The boundary is the circle $x^2+y^2=a^2$, $z=0$, traversed counterclockwise seen from above (the same flux as through the bottom disc with upward normal). $\oint-y\,dx+x\,dy+x^2\,dz=\int_0^{2\pi}a^2\,dt=2\pi a^2$.
:::

::: {.solution for="prob-mit1802n-6g-q1" status="draft"}
(@def-simply-connected-space.)

a) Yes. b) No: a loop going once around the ring of the torus (through its hole and back around the outside of the tube) bounds no surface avoiding the torus. c) Yes: any loop in a spherical shell bounds a surface in the shell. d) i) No (a loop around the line). ii) Yes. iii) No (a loop linking the circle). iv) Yes: the letter H has no loops, so a loop around it can be slipped off. v) No: the R contains a closed loop (its bowl), and a curve passing through that loop cannot bound a surface avoiding the R.
:::
