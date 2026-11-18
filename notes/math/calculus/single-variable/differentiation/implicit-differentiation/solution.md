<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

::: {.solution for="prob-mit1801f06-2a-q4" status="draft"}
a) Let $y=\cos^{-1}x$, so $\cos y=x$ with $0\le y\le\pi$. Differentiating, $-\sin y\cdot y'=1$. On $[0,\pi]$, $\sin y\ge0$, so $\sin y=+\sqrt{1-\cos^2y}=\sqrt{1-x^2}$ and
$$\frac{d}{dx}\cos^{-1}x=\frac{-1}{\sqrt{1-x^2}}\qquad(-1<x<1).$$

b) If $\theta=\sin^{-1}x\in[-\pi/2,\pi/2]$, then $\cos(\pi/2-\theta)=\sin\theta=x$ with $\pi/2-\theta\in[0,\pi]$, so $\cos^{-1}x=\pi/2-\sin^{-1}x$. The sum $\sin^{-1}x+\cos^{-1}x=\pi/2$ is constant, so its derivative is $0$. (Geometrically: the two acute angles of a right triangle add up to $\pi/2$.)
:::

::: {.solution for="prob-mit1801f06-3-q2" status="draft"}
Differentiating implicitly, $\frac23x^{-1/3}+\frac23y^{-1/3}y'=0$, so at a point $(x_0,y_0)$ of the curve with $x_0,y_0>0$ the slope is $m=-(y_0/x_0)^{1/3}$.

The tangent line $y=y_0+m(x-x_0)$ meets the $x$-axis at
$$X=x_0-\frac{y_0}{m}=x_0+y_0^{2/3}x_0^{1/3}=x_0^{1/3}\big(x_0^{2/3}+y_0^{2/3}\big)=x_0^{1/3},$$
and by the symmetric computation it meets the $y$-axis at $Y=y_0^{1/3}$. The part of the line in the first quadrant is the segment between $(X,0)$ and $(0,Y)$, of length $\sqrt{X^2+Y^2}=\sqrt{x_0^{2/3}+y_0^{2/3}}=1$.
:::

::: {.solution for="prob-mit1801n-1f-q3" status="draft"}
$y^n=x$, so $ny^{n-1}y'=1$ and $y'=\frac1{ny^{n-1}}=\frac1n\,x^{-(n-1)/n}=\frac1n\,x^{\frac1n-1}$.
:::

::: {.solution for="prob-mit1801n-1f-q5" status="draft"}
Differentiating, $\cos x+\cos y\,y'=0$, so $y'=-\cos x/\cos y$, which is $0$ when $\cos x=0$ (and $\cos y\ne0$). Then $\sin x=\pm1$. If $\sin x=-1$, then $\sin y=\frac32$, impossible. If $\sin x=1$, i.e. $x=\frac\pi2+2k\pi$, then $\sin y=-\frac12$, i.e. $y=-\frac\pi6+2m\pi$ or $y=\frac{7\pi}6+2m\pi$, where $\cos y\ne0$. So the points are
$$\Big(\frac\pi2+2k\pi,\ -\frac\pi6+2m\pi\Big),\qquad\Big(\frac\pi2+2k\pi,\ \frac{7\pi}6+2m\pi\Big)\qquad(k,m\in\mathbb Z).$$
:::

::: {.solution for="prob-mit1801n-1f-q8" status="draft"}
With $c$ and $\theta$ constant, differentiate with respect to $b$: $0=2aa'+2b-2a'b\cos\theta-2a\cos\theta$. So
$$\frac{da}{db}=\frac{a\cos\theta-b}{a-b\cos\theta}.$$
:::

::: {.solution for="prob-mit1801n-5a-q1" status="draft"}
a) $\frac\pi3$, since $\tan\frac\pi3=\sqrt3$ and $\frac\pi3\in(-\frac\pi2,\frac\pi2)$.

b) $\frac\pi3$, since $\sin\frac\pi3=\frac{\sqrt3}2$ and $\frac\pi3\in[-\frac\pi2,\frac\pi2]$.

c) $\theta\in(0,\frac\pi2)$ with $\tan\theta=5$: a right triangle with legs $1$ (adjacent) and $5$ (opposite) has hypotenuse $\sqrt{26}$. So $\sin\theta=\frac5{\sqrt{26}}$, $\cos\theta=\frac1{\sqrt{26}}$, $\sec\theta=\sqrt{26}$.
:::

::: {.solution for="prob-mit1801n-5a-q3" status="draft"}
By @prp-inverse-trig-derivatives and the chain rule:

f) $\dfrac1{\sqrt{1-a^2/x^2}}\cdot\Big(-\dfrac a{x^2}\Big)=\dfrac{-a}{\lvert x\rvert\sqrt{x^2-a^2}}$ (for $\lvert x\rvert>\lvert a\rvert$).

h) $\dfrac1{\sqrt{1-(1-x)}}\cdot\dfrac{-1}{2\sqrt{1-x}}=\dfrac{-1}{2\sqrt x\sqrt{1-x}}$ (for $0<x<1$).
:::
