<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

::: {.solution for="prob-mit1801f06-8a-q3" status="draft"}
a) (Take $a,h>0$.) The side $x=a$ is $r\cos\theta=a$, i.e. $r=a\sec\theta$, and the triangle is $0\le r\le a\sec\theta$, $0\le\theta\le\beta$ with $\tan\beta=h/a$. By @prp-polar-area,
$$A=\int_0^\beta\frac12a^2\sec^2\theta\,d\theta=\frac{a^2}2\tan\beta=\frac12ah .$$

b) $r+r\sin\theta=1$ gives $r=1-y$, so $x^2+y^2=(1-y)^2$, i.e. $x^2=1-2y$, or $y=\frac{1-x^2}2$: a parabola opening downwards with vertex $(0,\frac12)$, crossing the $x$-axis at $\pm1$, with focus at the origin.

c) For $0\le\theta\le\pi$ the region is the part of the plane above the $x$-axis and under the parabola: $A=\int_{-1}^1\frac{1-x^2}2\,dx=\frac12\Big(2-\frac23\Big)=\frac23$.

d) $A=\int_0^\pi\frac12\frac{d\theta}{(1+\sin\theta)^2}$. With $u=\theta-\pi/2$, $\sin\theta=\cos u$ and $u\in[-\pi/2,\pi/2]$; then $1+\cos u=2\cos^2(u/2)$ gives
$$A=\int_{-\pi/2}^{\pi/2}\frac{du}{8\cos^4(u/2)}=\frac14\int_{-\pi/4}^{\pi/4}\sec^4w\,dw\quad(w=u/2).$$
Using $\int\sec^4w\,dw=\tan w+\frac{\tan^3w}3$ (from the note on trigonometric integrals), $A=\frac14\Big[\tan w+\frac{\tan^3w}3\Big]_{-\pi/4}^{\pi/4}=\frac14\Big(2+\frac23\Big)=\frac23$, as in (c).
:::

::: {.solution for="prob-mit1801n-4h-q1" status="draft"}
b) $r=2$, $\theta=\pi$.

f) $r=2$, $\theta=\frac{3\pi}2$ or $\theta=-\frac\pi2$.

g) $r=2$, $\theta=\frac{11\pi}6$ or $\theta=-\frac\pi6$.
:::

::: {.solution for="prob-mit1801n-4h-q2" status="draft"}
(i) $(x-a)^2+y^2=a^2$ means $x^2+y^2=2ax$, i.e. $r^2=2ar\cos\theta$, i.e. $r=2a\cos\theta$ (as in @exm-polar-circle).

(ii) $O=(0,0)$ and $Q=(2a,0)$. The angle at $P$ is a right angle (an angle in a semicircle), so in the right triangle $OPQ$, $OP=OQ\cos\theta$: $r=2a\cos\theta$, for $-\frac\pi2\le\theta\le\frac\pi2$.
:::

::: {.solution for="prob-mit1801n-4h-q3" status="draft"}
(i) $r=a(\cos^2\theta-\sin^2\theta)$; multiply by $r^2$: $r^3=a(x^2-y^2)$, i.e. $(x^2+y^2)^{3/2}=a(x^2-y^2)$.

(ii) Four leaves of length $a$ (for $a>0$), along the positive and negative $x$- and $y$-axes. For $-\frac\pi4\le\theta\le\frac\pi4$, $r\ge0$ traces the leaf on the positive $x$-axis counter-clockwise; for $\frac\pi4\le\theta\le\frac{3\pi}4$, $r\le0$, so the points are drawn in the opposite direction and trace the leaf on the **negative** $y$-axis; then the leaf on the negative $x$-axis ($\frac{3\pi}4\le\theta\le\frac{5\pi}4$) and finally the leaf on the positive $y$-axis.
:::

::: {.solution for="prob-mit1801n-4i-q2" status="draft"}
One leaf is $-\frac\pi6\le\theta\le\frac\pi6$. By @prp-polar-area,
$$A=\frac12\int_{-\pi/6}^{\pi/6}a^2\cos^2(3\theta)\,d\theta=\frac{a^2}2\cdot\frac\pi6=\frac{\pi a^2}{12},$$
since $\cos^2$ averages $\frac12$ over this interval (a full period of $\cos^2 3\theta$ has length $\frac\pi3$).
:::

::: {.solution for="prob-mit1801n-4i-q3" status="draft"}
$A=\frac12\int_0^\pi e^{6\theta}d\theta=\frac{e^{6\pi}-1}{12}$.
:::
