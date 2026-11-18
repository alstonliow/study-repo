<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

::: {.solution for="prob-mit1801f06-7-q5" status="draft"}
The first hump is $-\pi/2\le x\le\pi/2$, which is symmetric about the $y$-axis; rotating it around the $y$-axis gives the same solid as rotating its right half $0\le x\le\pi/2$. By shells (@def-disks-and-shells),
$$V=\int_0^{\pi/2}2\pi x\cos x\,dx .$$
By @thm-integration-by-parts with $u=x$, $v=\sin x$: $\int x\cos x\,dx=x\sin x-\int\sin x\,dx=x\sin x+\cos x$. Hence
$$V=2\pi\big[x\sin x+\cos x\big]_0^{\pi/2}=2\pi\Big(\frac\pi2-1\Big)=\pi^2-2\pi\approx3.59 .$$
:::

::: {.solution for="prob-mit1801n-5f-q1" status="draft"}
With $u=\ln x$, $v=\frac{x^{a+1}}{a+1}$ (@thm-integration-by-parts): $\frac{x^{a+1}\ln x}{a+1}-\int\frac{x^a}{a+1}dx=\frac{x^{a+1}\ln x}{a+1}-\frac{x^{a+1}}{(a+1)^2}+c$.
:::

::: {.solution for="prob-mit1801n-5f-q2" status="draft"}
d) With $u=x^n$, $v=\frac{e^{ax}}a$ ($a\ne0$):
$$\int x^ne^{ax}dx=\frac{x^ne^{ax}}a-\frac na\int x^{n-1}e^{ax}dx .$$

b) With $a=1$, applied twice (@prp-reduction-formulas): $\int x^2e^x\,dx=x^2e^x-2\big(xe^x-e^x\big)=(x^2-2x+2)e^x+c$.
:::

::: {.solution for="prob-mit1801n-5f-q3" status="draft"}
With $u=\sin^{-1}(4x)$, $v=x$: $x\sin^{-1}(4x)-\int\frac{4x\,dx}{\sqrt{1-16x^2}}=x\sin^{-1}(4x)+\frac14\sqrt{1-16x^2}+c$.
:::
