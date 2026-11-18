<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit1801f06-8a-q3" status="draft"}
a) (Take $a,h>0$.) The side $x=a$ is $r\cos\theta=a$, i.e. $r=a\sec\theta$, and the triangle is $0\le r\le a\sec\theta$, $0\le\theta\le\beta$ with $\tan\beta=h/a$. By @prp-polar-area,
$$A=\int_0^\beta\frac12a^2\sec^2\theta\,d\theta=\frac{a^2}2\tan\beta=\frac12ah .$$

b) $r+r\sin\theta=1$ gives $r=1-y$, so $x^2+y^2=(1-y)^2$, i.e. $x^2=1-2y$, or $y=\frac{1-x^2}2$: a parabola opening downwards with vertex $(0,\frac12)$, crossing the $x$-axis at $\pm1$, with focus at the origin.

c) For $0\le\theta\le\pi$ the region is the part of the plane above the $x$-axis and under the parabola: $A=\int_{-1}^1\frac{1-x^2}2\,dx=\frac12\Big(2-\frac23\Big)=\frac23$.

d) $A=\int_0^\pi\frac12\frac{d\theta}{(1+\sin\theta)^2}$. With $u=\theta-\pi/2$, $\sin\theta=\cos u$ and $u\in[-\pi/2,\pi/2]$; then $1+\cos u=2\cos^2(u/2)$ gives
$$A=\int_{-\pi/2}^{\pi/2}\frac{du}{8\cos^4(u/2)}=\frac14\int_{-\pi/4}^{\pi/4}\sec^4w\,dw\quad(w=u/2).$$
Using $\int\sec^4w\,dw=\tan w+\frac{\tan^3w}3$ (from the note on trigonometric integrals), $A=\frac14\Big[\tan w+\frac{\tan^3w}3\Big]_{-\pi/4}^{\pi/4}=\frac14\Big(2+\frac23\Big)=\frac23$, as in (c).
:::
