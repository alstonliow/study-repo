<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802f07-9-q3" status="draft"}
a) On the unit circle $\hat{\mathbf{n}}=\langle x,y\rangle$ (outwards), so $\vec F\cdot\hat{\mathbf{n}}=x^2y+y^3=y(x^2+y^2)=y$. The upper half ($y>0$) contributes positively, the lower half negatively.

b) With $x=\cos t$, $y=\sin t$, $ds=dt$: flux $=\int_0^{2\pi}\sin t\,dt=0$. The contributions of the two halves are equal and opposite, by the symmetry $y\to-y$.

c) $\operatorname{div}\vec F=y+2y=3y$, and $\iint_{x^2+y^2\le1}3y\,dA=0$ by symmetry (@thm-greens-theorem-normal-form).
:::

::: {.solution for="prob-mit1802n-4e-q1" status="draft"}
a) $\mathbf{F}$ is tangent to the circle, so $\mathbf{F}\cdot\mathbf{n}=0$ and the flux is $0$.

c) On the segment, $\mathbf{F}=x\mathbf{j}$ and $\mathbf{n}=-\mathbf{j}$ (to the right of the direction of travel), so $\mathbf{F}\cdot\mathbf{n}=-x$ and the flux is $\int_0^1-x\,dx=-\frac12$.
:::

::: {.solution for="prob-mit1802n-4e-q2" status="draft"}
The flux is $\mathbf{F}\cdot\mathbf{n}$ times the length $1$, where $\mathbf{n}$ is the direction of $C$ turned $90^\circ$ clockwise. The position does not matter, only the direction.

a) $\mathbf{n}=\frac{\mathbf{i}+\mathbf{j}}{\sqrt2}$: $C$ points in the direction $\frac{-\mathbf{i}+\mathbf{j}}{\sqrt2}$.

b) $C$ points in the direction $\frac{\mathbf{i}-\mathbf{j}}{\sqrt2}$.

c) $C$ is parallel to $\mathbf{i}+\mathbf{j}$ (either direction).

d) $\mathbf{n}\cdot(\mathbf{i}+\mathbf{j})=-1$ for $\mathbf{n}=-\mathbf{i}$ or $\mathbf{n}=-\mathbf{j}$: $C$ points in the direction $-\mathbf{j}$ or $\mathbf{i}$.

e) Maximum $\sqrt2$, minimum $-\sqrt2$.
:::

::: {.solution for="prob-mit1802n-4e-q3" status="draft"}
By @prp-flux-components the flux is $\int_C-N\,dx+M\,dy$ with $M=x^2$, $N=xy$. With $x=t+1$, $y=t^2$, $dx=dt$, $dy=2t\,dt$:
$$\int_0^1\big(-(t+1)t^2+(t+1)^2\,2t\big)dt=\int_0^1(t^3+3t^2+2t)\,dt=\frac14+1+1=\frac94 .$$
:::

::: {.solution for="prob-mit1802n-4e-q4" status="draft"}
Travelling clockwise, $\mathbf{n}$ (to the right) points into the square, so the flux is minus the outward flux. By Green's theorem for flux the outward flux is $\iint\operatorname{div}\mathbf{F}\,dA=\iint2\,dA=2$. So the flux is $-2$. (Directly: only the sides $x=1$ and $y=1$ contribute, each $-1$.)
:::

::: {.solution for="prob-mit1802n-4e-q5" status="draft"}
a) On the circle, $\mathbf{F}$ is along the outward normal $\mathbf{n}$ with length $a^m$, so the flux is $a^m\cdot2\pi a=2\pi a^{m+1}$.

b) Independent of $a$ exactly for $m=-1$ (flux $2\pi$).
:::

::: {.solution for="prob-mit1802n-4f-q3" status="draft"}
Double integral: $\operatorname{div}\mathbf{F}=2$, and the half disc has area $\frac\pi2$: $\iint2\,dA=\pi$.

Line integral (outward normal): on the semicircle $\mathbf{n}=\langle x,y\rangle$ and $\mathbf{F}\cdot\mathbf{n}=x^2+y^2=1$, giving its length $\pi$; on the segment $\mathbf{n}=-\mathbf{j}$ and $\mathbf{F}\cdot\mathbf{n}=-y=0$. Total $\pi$.
:::

::: {.solution for="prob-mit1802n-4f-q4" status="draft"}
Double integral: $\operatorname{div}\mathbf{F}=2x+x=3x$, $\int_0^1\!\int_0^13x\,dx\,dy=\frac32$.

Line integral (outward normals): right side $x=1$, $\mathbf{n}=\mathbf{i}$, $\mathbf{F}\cdot\mathbf{n}=1$: $1$. Top $y=1$, $\mathbf{n}=\mathbf{j}$, $\mathbf{F}\cdot\mathbf{n}=x$: $\frac12$. Left $x=0$: $\mathbf{F}\cdot(-\mathbf{i})=-x^2=0$. Bottom $y=0$: $\mathbf{F}\cdot(-\mathbf{j})=-xy=0$. Total $\frac32$.
:::
