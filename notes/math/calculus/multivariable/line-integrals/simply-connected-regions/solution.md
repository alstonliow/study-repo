<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802f07-10-q1" status="draft"}
Away from the origin, $\operatorname{div}\vec F=\dfrac{r^2-2x^2}{r^4}+\dfrac{r^2-2y^2}{r^4}=0$.

- $a<1$: the disk bounded by the circle does not contain the origin, so $\vec F$ is defined and differentiable on all of it and Green's theorem for flux gives flux $=\iint0\,dA=0$. (The field points radially away from the origin: it enters the disk on the side facing the origin and leaves on the other side, in equal amounts.)
- $a>1$: the disk contains the origin, where $\vec F$ is undefined. Apply the extended Green's theorem (@thm-extended-green, flux form) to the region between the circle and a small circle of radius $\varepsilon$ about the origin: the two fluxes are equal. On the small circle $\vec F=\hat{\mathbf{n}}/\varepsilon$, so the flux is $\frac1\varepsilon\cdot2\pi\varepsilon=2\pi$. The flux is $2\pi$.
:::
