<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802f07-10-q3" status="draft"}
The ball is centred at $(0,0,a)$; the distance to the origin is $\rho=\sqrt{r^2+z^2}$, and $V=\frac43\pi a^3$.

Cylindrical: the ball is $(z-a)^2+r^2\le a^2$, i.e. $0\le r\le\sqrt{2az-z^2}$, $0\le z\le2a$:
$$\int_0^{2\pi}\!\!\int_0^{2a}\!\!\int_0^{\sqrt{2az-z^2}}\sqrt{r^2+z^2}\,r\,dr\,dz\,d\theta=2\pi\int_0^{2a}\frac{(2az)^{3/2}-z^3}3\,dz=\frac{2\pi}3(2a)^4\Big(\frac25-\frac14\Big)=\frac{8\pi a^4}5 .$$

Spherical: the sphere is $\rho=2a\cos\phi$ (as in @thm-newton-shell), $0\le\phi\le\frac\pi2$:
$$\int_0^{2\pi}\!\!\int_0^{\pi/2}\!\!\int_0^{2a\cos\phi}\rho\cdot\rho^2\sin\phi\,d\rho\,d\phi\,d\theta=2\pi\int_0^{\pi/2}4a^4\cos^4\phi\sin\phi\,d\phi=\frac{8\pi a^4}5 .$$

Average distance $=\dfrac{8\pi a^4/5}{4\pi a^3/3}=\dfrac65a$.
:::

::: {.solution for="prob-mit1802n-5b-q1" status="draft"}
a) The cone is $\phi=\frac\pi4$: $\displaystyle\int_0^{2\pi}\!\!\int_0^{\pi/4}\!\!\int_0^{\sqrt2}d\rho\,d\phi\,d\theta$.

b) $\displaystyle\int_0^{\pi/2}\!\!\int_0^{\pi/2}\!\!\int_0^\infty d\rho\,d\phi\,d\theta$.

c) The sphere is $\rho=2\cos\phi$ and the plane is $\rho=\sec\phi$; they meet where $2\cos^2\phi=1$, $\phi=\frac\pi4$: $\displaystyle\int_0^{2\pi}\!\!\int_0^{\pi/4}\!\!\int_{\sec\phi}^{2\cos\phi}d\rho\,d\phi\,d\theta$.
:::

::: {.solution for="prob-mit1802n-5b-q2" status="draft"}
Take $z\ge0$; $\bar x=\bar y=0$. $\iiint z\,dV=\int_0^{2\pi}\!\int_0^{\pi/2}\!\int_0^a\rho\cos\phi\,\rho^2\sin\phi\,d\rho\,d\phi\,d\theta=2\pi\cdot\frac{a^4}4\cdot\frac12=\frac{\pi a^4}4$, and the volume is $\frac23\pi a^3$, so $\bar z=\frac38a$.
:::

::: {.solution for="prob-mit1802n-5b-q3" status="draft"}
Vertex at the origin, axis along the $z$-axis: $D$ is $\rho\le a$, $\phi\le\frac\pi6$, and $\delta=z=\rho\cos\phi$. The distance to the axis is $\rho\sin\phi$:
$$I=\int_0^{2\pi}\!\!\int_0^{\pi/6}\!\!\int_0^a\rho^2\sin^2\phi\cdot\rho\cos\phi\cdot\rho^2\sin\phi\,d\rho\,d\phi\,d\theta=2\pi\cdot\frac{a^6}6\cdot\frac{\sin^4(\pi/6)}4=\frac{\pi a^6}{192}.$$
:::

::: {.solution for="prob-mit1802n-5b-q4" status="draft"}
Divide by the volume $V=\frac43\pi a^3$; put the centre at the origin and use $\int_0^a\rho^3\,d\rho=\frac{a^4}4$.

a) $\iiint\rho\,dV=2\pi\cdot2\cdot\frac{a^4}4=\pi a^4$; average $\frac34a$.

b) Distance to the $z$-axis: $\rho\sin\phi$. $\iiint\rho\sin\phi\,dV=2\pi\cdot\frac{a^4}4\int_0^\pi\sin^2\phi\,d\phi=\frac{\pi^2a^4}4$; average $\frac{3\pi}{16}a$.

c) Distance to the $xy$-plane: $|z|=\rho|\cos\phi|$. $\iiint|z|\,dV=2\pi\cdot\frac{a^4}4\int_0^\pi|\cos\phi|\sin\phi\,d\phi=\frac{\pi a^4}2$; average $\frac38a$.
:::
