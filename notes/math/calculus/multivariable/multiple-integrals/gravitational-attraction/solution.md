<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802n-5c-q5" status="draft"}
Put the pole at the origin and the hemisphere above it: the ball $\rho\le2a\cos\phi$ (centre $(0,0,a)$) cut by its equatorial plane $z=a$, keeping $z\le a$, i.e. $\rho\le a\sec\phi$. By symmetry the force is vertical, and by @prp-attraction-of-solid
$$F_z=G\iiint\cos\phi\sin\phi\,d\rho\,d\phi\,d\theta .$$
A ray at angle $\phi$ leaves the solid at $\min(a\sec\phi,\ 2a\cos\phi)$; $a\sec\phi\le2a\cos\phi$ exactly when $\cos^2\phi\ge\frac12$, i.e. $\phi\le\frac\pi4$. So
$$F_z=2\pi G\Big[\int_0^{\pi/4}a\sec\phi\cos\phi\sin\phi\,d\phi+\int_{\pi/4}^{\pi/2}2a\cos^2\phi\sin\phi\,d\phi\Big]=2\pi Ga\Big[\Big(1-\frac1{\sqrt2}\Big)+\frac23\cdot\frac1{2\sqrt2}\Big]=2\pi Ga\Big(1-\frac{\sqrt2}3\Big),$$
directed from the pole into the hemisphere.
:::

::: {.solution for="prob-mit1802n-5c-q2" status="draft"}
The cone $z=2r$ is $\tan\phi=\frac12$; call this angle $\alpha$, with $\cos\alpha=\frac2{\sqrt5}$. The plane is $\rho=2\sec\phi$. By @prp-attraction-of-solid,
$$F_z=G\int_0^{2\pi}\!\!\int_0^\alpha\!\!\int_0^{2\sec\phi}\cos\phi\sin\phi\,d\rho\,d\phi\,d\theta=4\pi G\int_0^\alpha\sin\phi\,d\phi=4\pi G\Big(1-\frac2{\sqrt5}\Big),$$
directed upwards.
:::

::: {.solution for="prob-mit1802n-5c-q3" status="draft"}
Put $Q$ at the origin and the centre at $(0,0,1)$; the ball is $\rho\le2\cos\phi$, $0\le\phi\le\frac\pi2$, and $\delta=\rho^{-1/2}$. By symmetry the force is along the $z$-axis:
$$F_z=G\int_0^{2\pi}\!\!\int_0^{\pi/2}\!\!\int_0^{2\cos\phi}\rho^{-1/2}\cos\phi\sin\phi\,d\rho\,d\phi\,d\theta=2\pi G\int_0^{\pi/2}2\sqrt{2\cos\phi}\cos\phi\sin\phi\,d\phi=4\sqrt2\pi G\cdot\frac25=\frac{8\sqrt2\pi G}5,$$
towards the centre of the sphere.
:::

::: {.solution for="prob-mit1802n-5c-q4" status="draft"}
The second sphere is $\rho=2\cos\phi$. The region is $\rho\le\min(1,2\cos\phi)$, $0\le\phi\le\frac\pi2$; $2\cos\phi\ge1$ for $\phi\le\frac\pi3$.
$$F_z=2\pi G\Big[\int_0^{\pi/3}\cos\phi\sin\phi\,d\phi+\int_{\pi/3}^{\pi/2}2\cos^2\phi\sin\phi\,d\phi\Big]=2\pi G\Big[\frac38+\frac1{12}\Big]=\frac{11\pi G}{12},$$
directed upwards.
:::
