<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802f07-2-q2" status="draft"}
a) Let $Q_1,Q_2$ be the pegs. The large gear turns clockwise by $t$; at $t=0$ its peg is straight above the centre, so $\overrightarrow{OQ_1}=\langle0,-2\rangle+2\langle\sin t,\cos t\rangle$. No slipping means equal arcs at the contact point: the small gear turns by $2t$ (counterclockwise), and its peg starts straight below its centre, so $\overrightarrow{OQ_2}=\langle0,1\rangle+\langle\sin2t,-\cos2t\rangle$. (Check: at the origin both rims move to the right with speed $2$.) The midpoint is $\overrightarrow{OP}=\frac12(\overrightarrow{OQ_1}+\overrightarrow{OQ_2})$:
$$x(t)=\sin t+\tfrac12\sin2t,\qquad y(t)=-\tfrac12+\cos t-\tfrac12\cos2t .$$

b) $\mathbf{v}(t)=\langle\cos t+\cos2t,\ -\sin t+\sin2t\rangle$ and $\mathbf{a}(t)=\langle-\sin t-2\sin2t,\ -\cos t+2\cos2t\rangle$. At $t=0$: $\mathbf{v}=\langle2,0\rangle$ and $\mathbf{a}=\langle0,1\rangle$.
:::

::: {.solution for="prob-mit1802n-1i-q1" status="draft"}
The velocity is $v\cdot\dfrac{a\mathbf{i}+b\mathbf{j}}{\sqrt{a^2+b^2}}$, so
$$\mathbf{r}(t)=\Big(x_0+\frac{avt}{\sqrt{a^2+b^2}}\Big)\mathbf{i}+\Big(y_0+\frac{bvt}{\sqrt{a^2+b^2}}\Big)\mathbf{j}.$$
:::

::: {.solution for="prob-mit1802n-1i-q3" status="draft"}
a) $\frac x2+y=\cos^2t+\sin^2t=1$: the line $x+2y=2$. Since $0\le x\le2$, $P$ traces only the segment from $(2,0)$ to $(0,1)$, moving back and forth along it forever (period $\pi$).

b) $x=\cos2t=2\cos^2t-1=2y^2-1$: the parabola $x=2y^2-1$. Since $-1\le y\le1$, $P$ traces the arc from $(1,1)$ through $(-1,0)$ to $(1,-1)$, back and forth (period $2\pi$).

d) $y^2-x^2=\sec^2t-\tan^2t=1$: a hyperbola. On each interval $(-\frac\pi2+k\pi,\frac\pi2+k\pi)$, $x=\tan t$ runs from $-\infty$ to $\infty$; for even $k$, $y=\sec t\ge1$ (the upper branch), for odd $k$, $y\le-1$ (the lower branch). So $P$ runs alternately along the whole upper and the whole lower branch, from left to right each time, coming in from infinity ($t$ is undefined at the odd multiples of $\frac\pi2$).
:::

::: {.solution for="prob-mit1802n-1i-q5" status="draft"}
Starting from $P=(a,0)$ the string lies along the circle in the clockwise direction. When an arc of angle $\theta$ has been unwound, the string leaves the circle at $T=(a\cos\theta,-a\sin\theta)$, and the straight part $TP$ has length $a\theta$ and is tangent to the circle at $T$, pointing in the counterclockwise direction there, i.e. along $\langle\sin\theta,\cos\theta\rangle$. So
$$OP=OT+TP=\langle a\cos\theta,-a\sin\theta\rangle+a\theta\langle\sin\theta,\cos\theta\rangle,$$
$$x=a(\cos\theta+\theta\sin\theta),\qquad y=a(-\sin\theta+\theta\cos\theta)\qquad(\theta\ge0).$$
:::

::: {.solution for="prob-mit1802n-1j-q1" status="draft"}
a) $\mathbf{v}=e^t\mathbf{i}-e^{-t}\mathbf{j}$, speed $\sqrt{e^{2t}+e^{-2t}}$, $\mathbf{T}=\mathbf{v}/\sqrt{e^{2t}+e^{-2t}}$, $\mathbf{a}=e^t\mathbf{i}+e^{-t}\mathbf{j}$.

b) $\mathbf{v}=2t\mathbf{i}+3t^2\mathbf{j}$, speed $|t|\sqrt{4+9t^2}$, $\mathbf{T}=\pm\dfrac{2\mathbf{i}+3t\mathbf{j}}{\sqrt{4+9t^2}}$ ($+$ for $t>0$, $-$ for $t<0$; undefined at $t=0$), $\mathbf{a}=2\mathbf{i}+6t\mathbf{j}$.

c) $\mathbf{v}=t(-4\mathbf{i}+2\mathbf{j}+4\mathbf{k})$, speed $6|t|$, $\mathbf{T}=\pm\frac13(-2\mathbf{i}+\mathbf{j}+2\mathbf{k})$ (same sign convention), $\mathbf{a}=-4\mathbf{i}+2\mathbf{j}+4\mathbf{k}$. (The motion is along a straight line.)
:::

::: {.solution for="prob-mit1802n-1j-q2" status="draft"}
a) $\mathbf{v}=\dfrac{-2t\,\mathbf{i}+(1-t^2)\,\mathbf{j}}{(1+t^2)^2}$. Since $|{-2t\,\mathbf{i}+(1-t^2)\mathbf{j}}|=\sqrt{4t^2+(1-t^2)^2}=1+t^2$, the speed is $\dfrac1{1+t^2}$ and $\mathbf{T}=\dfrac{-2t\,\mathbf{i}+(1-t^2)\mathbf{j}}{1+t^2}$.

b) Greatest at $t=0$, the point $(1,0)$, speed $1$. There is no smallest: the speed tends to $0$ as $t\to\pm\infty$, when $P$ approaches the origin.

c) $x^2+y^2=\dfrac{1+t^2}{(1+t^2)^2}=x$, i.e. $(x-\frac12)^2+y^2=\frac14$: the circle of radius $\frac12$ centred at $(\frac12,0)$, traversed once counterclockwise, the origin excluded.
:::

::: {.solution for="prob-mit1802n-1j-q3" status="draft"}
$\dfrac{d}{dt}(x_1x_2+y_1y_2)=x_1'x_2+x_1x_2'+y_1'y_2+y_1y_2'=(x_1'x_2+y_1'y_2)+(x_1x_2'+y_1y_2')=\mathbf{r}'\cdot\mathbf{s}+\mathbf{r}\cdot\mathbf{s}'$.
:::

::: {.solution for="prob-mit1802n-1j-q4" status="draft"}
a) $x^2+y^2+z^2=a^2$; differentiating, $2xx'+2yy'+2zz'=0$, i.e. $\mathbf{r}\cdot\mathbf{v}=0$.

b) $\mathbf{r}\cdot\mathbf{r}=a^2$ is constant, so $0=\frac{d}{dt}(\mathbf{r}\cdot\mathbf{r})=2\,\mathbf{r}\cdot\mathbf{v}$ (@cor-constant-length).

c) If $\mathbf{r}\cdot\mathbf{v}=0$ then $\frac{d}{dt}|\mathbf{r}|^2=2\mathbf{r}\cdot\mathbf{v}=0$, so $|\mathbf{r}|$ is constant: $P$ stays on a sphere centred at the origin.
:::

::: {.solution for="prob-mit1802n-1j-q5" status="draft"}
a) $\mathbf{v}\cdot\mathbf{v}=|\mathbf{v}|^2$ is constant, so $0=\frac{d}{dt}(\mathbf{v}\cdot\mathbf{v})=2\,\mathbf{v}\cdot\mathbf{a}$.

b) If $\mathbf{v}\cdot\mathbf{a}=0$ then $\frac{d}{dt}|\mathbf{v}|^2=2\mathbf{v}\cdot\mathbf{a}=0$, so the speed is constant.
:::

::: {.solution for="prob-mit1802n-1j-q6" status="draft"}
a) $\mathbf{v}=-a\sin t\,\mathbf{i}+a\cos t\,\mathbf{j}+b\,\mathbf{k}$, $|ds/dt|=\sqrt{a^2+b^2}$, $\mathbf{T}=\mathbf{v}/\sqrt{a^2+b^2}$, $\mathbf{a}=-a\cos t\,\mathbf{i}-a\sin t\,\mathbf{j}$.

b) $\mathbf{v}\cdot\mathbf{a}=a^2\sin t\cos t-a^2\sin t\cos t+0=0$. This agrees with 1J-5: the speed $\sqrt{a^2+b^2}$ is constant.
:::

::: {.solution for="prob-mit1802n-1j-q9" status="draft"}
a) $|\mathbf{r}|^2=9\cos^2t+25\sin^2t+16\cos^2t=25$: the sphere of radius $5$ about the origin.

b) $\mathbf{v}=-3\sin t\,\mathbf{i}+5\cos t\,\mathbf{j}-4\sin t\,\mathbf{k}$ and $|\mathbf{v}|^2=25\sin^2t+25\cos^2t=25$: speed $5$.

c) $\mathbf{a}=-3\cos t\,\mathbf{i}-5\sin t\,\mathbf{j}-4\cos t\,\mathbf{k}=-\mathbf{r}$, which points towards the origin.

d) $4x-3z=12\cos t-12\cos t=0$: $P$ stays in the plane $4x-3z=0$, which contains the origin.

e) The intersection of the sphere with a plane through its centre: a great circle of radius $5$, traversed at constant speed $5$, once every $2\pi$ units of time.
:::

::: {.solution for="prob-mit1802n-1j-q10" status="draft"}
a) (Take $a>0$.) $\mathbf{T}=\dfrac{-a\sin t\,\mathbf{i}+a\cos t\,\mathbf{j}+b\,\mathbf{k}}{\sqrt{a^2+b^2}}$, so $\dfrac{d\mathbf{T}}{dt}=\dfrac{-a\cos t\,\mathbf{i}-a\sin t\,\mathbf{j}}{\sqrt{a^2+b^2}}$, of length $\dfrac a{\sqrt{a^2+b^2}}$. By the chain rule $\dfrac{d\mathbf{T}}{dt}=\dfrac{d\mathbf{T}}{ds}\dfrac{ds}{dt}$ with $\dfrac{ds}{dt}=\sqrt{a^2+b^2}$, so
$$\kappa=\frac{a}{a^2+b^2},$$
a constant.

b) $b=0$: $\kappa=\frac1a$, the reciprocal of the radius.
:::

::: {.solution for="prob-mit1802n-1k-q3" status="draft"}
The statement is the converse of Kepler's law: if the force on the planet is central (directed along $\mathbf{r}$), then the motion lies in a plane and $\mathbf{r}$ sweeps out equal areas in equal times. (1K-2: if $d\mathbf{s}/dt=\mathbf{0}$ then $\mathbf{s}$ is constant.)

1. A central force gives $\mathbf{a}\parallel\mathbf{r}$, so $\mathbf{r}\times\mathbf{a}=\mathbf{0}$.

2. $\frac{d}{dt}(\mathbf{r}\times\mathbf{v})=\mathbf{v}\times\mathbf{v}+\mathbf{r}\times\mathbf{a}=\mathbf{0}$, so by 1K-2, $\mathbf{r}\times\mathbf{v}=\mathbf{K}$, a constant vector.

3. If $\mathbf{K}\ne\mathbf{0}$: $\mathbf{r}\cdot\mathbf{K}=\mathbf{r}\cdot(\mathbf{r}\times\mathbf{v})=0$, so $\mathbf{r}$ stays in the plane through the sun perpendicular to $\mathbf{K}$. (If $\mathbf{K}=\mathbf{0}$, $\mathbf{v}\parallel\mathbf{r}$ and the motion is along a line through the sun, sweeping no area.)

4. The area is swept at the rate $\frac12|\mathbf{r}\times\mathbf{v}|=\frac12|\mathbf{K}|$, a constant (@thm-kepler-second-law): equal areas in equal times.
:::
