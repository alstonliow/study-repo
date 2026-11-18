<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802f07-7-q2" status="draft"}
Put the centre at the origin. The distance to the centre is $r$, so its average is
$$\frac1{\pi a^2}\iint_Rr\,dA=\frac1{\pi a^2}\int_0^{2\pi}\!\!\int_0^ar\cdot r\,dr\,d\theta=\frac1{\pi a^2}\cdot2\pi\frac{a^3}3=\frac{2a}3 .$$
:::

::: {.solution for="prob-mit1802n-3b-q1" status="draft"}
a) The region inside the circle $r=2$ with $x\le-1$. The line $x=-1$ is $r=-\sec\theta$, and it meets the circle where $\cos\theta=-\frac12$:
$$\int_{2\pi/3}^{4\pi/3}\!\!\int_{-\sec\theta}^2\,r\,dr\,d\theta .$$

c) $1-\cos\theta\ge\frac32$ when $\cos\theta\le-\frac12$:
$$\int_{2\pi/3}^{4\pi/3}\!\!\int_{3/2}^{1-\cos\theta}r\,dr\,d\theta .$$

d) The circle is $r=2a\cos\theta$ and the line is $r=a\csc\theta$; they meet at $(a,a)$, where $\theta=\frac\pi4$. A ray at angle $\theta\in[\frac\pi4,\frac\pi2]$ enters the region where it leaves the disc and exits on the line:
$$\int_{\pi/4}^{\pi/2}\!\!\int_{2a\cos\theta}^{a\csc\theta}r\,dr\,d\theta .$$
:::

::: {.solution for="prob-mit1802n-3b-q2" status="draft"}
b) $\displaystyle\int_0^{\pi/2}\!\!\int_0^a\frac{r\,dr\,d\theta}{1+r^2}=\frac\pi2\cdot\frac12\ln(1+a^2)=\frac\pi4\ln(1+a^2)$.

d) The circle is $r=\sin\theta$, and the right half is $0\le\theta\le\frac\pi2$:
$$\int_0^{\pi/2}\!\!\int_0^{\sin\theta}\frac{r\,dr}{\sqrt{1-r^2}}\,d\theta=\int_0^{\pi/2}\big(1-\cos\theta\big)\,d\theta=\frac\pi2-1 .$$
:::

::: {.solution for="prob-mit1802n-3b-q3" status="draft"}
a) $\displaystyle\int_0^{2\pi}\!\!\int_0^a\sqrt{a^2-r^2}\,r\,dr\,d\theta=2\pi\cdot\frac{a^3}3=\frac23\pi a^3$.

c) The circle is $r=2\sin\theta$, $0\le\theta\le\pi$, and the height is $r$:
$$\int_0^\pi\!\!\int_0^{2\sin\theta}r\cdot r\,dr\,d\theta=\frac83\int_0^\pi\sin^3\theta\,d\theta=\frac83\cdot\frac43=\frac{32}9 .$$
:::
