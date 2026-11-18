<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

::: {.solution for="prob-mit1801f06-8b-q1" status="draft"}
a) The limit is $0$ for every real $m$. For $m\le0$ both factors are bounded and $e^{-x}\to0$. For $m>0$ write it as $\frac{x^m}{e^x}$ ($\infty/\infty$) and apply @thm-lhopital $\lceil m\rceil$ times: each time the power drops by one while $e^x$ stays, until the numerator is $m(m-1)\cdots x^{m-\lceil m\rceil}$, which is bounded for $x\ge1$.

b) The integrand is continuous on $[0,\infty)$, so only the infinite end matters. By (a) with $m=n+2$, $\frac{x^ne^{-x}}{x^{-2}}=x^{n+2}e^{-x}\to0$, so $x^ne^{-x}\le x^{-2}$ for $x\ge b$, some $b\ge1$. Since $\int_b^\infty x^{-2}dx$ converges (@thm-p-integrals), so does $\int_b^\infty x^ne^{-x}dx$ by @thm-comparison-integrals. (A limit of $0$ rather than a positive number is enough for convergence, by this direct comparison.)

c) With $u=x^{n+1}$, $v=-e^{-x}$ (@thm-integration-by-parts):
$$\int_0^Nx^{n+1}e^{-x}dx=\Big[-x^{n+1}e^{-x}\Big]_0^N+(n+1)\int_0^Nx^ne^{-x}dx .$$
The boundary term is $-N^{n+1}e^{-N}\to0$ by (a) (and it is $0$ at $x=0$). Letting $N\to\infty$, $A(n+1)=(n+1)A(n)$, so $c_n=n+1$.

d) $A(0)=\int_0^\infty e^{-x}dx=1$. By induction $A(n)=n\,A(n-1)=\dots=n!$.

e) $A(-\tfrac12)=\int_0^\infty x^{-1/2}e^{-x}dx$. On $(0,1]$, $x^{-1/2}e^{-x}\le x^{-1/2}$, whose integral converges ($p=\frac12<1$); on $[1,\infty)$, $x^{-1/2}e^{-x}\le e^{-x}$. So it converges. Substituting $x=u^2$, $dx=2u\,du$:
$$A(-\tfrac12)=\int_0^\infty\frac{e^{-u^2}}{u}\,2u\,du=2\int_0^\infty e^{-u^2}du=\sqrt\pi,$$
using the Gaussian integral (@prp-gaussian-integral).
:::

::: {.solution for="prob-mit1801n-6b-q1" status="draft"}
$\frac1{\sqrt{x^3+5}}<x^{-3/2}$ and $\int_1^\infty x^{-3/2}dx$ converges (@thm-p-integrals, $p=\frac32>1$), so the integral **converges** (@thm-comparison-integrals).
:::

::: {.solution for="prob-mit1801n-6b-q2" status="draft"}
$\frac{x^2}{x^3+2}\Big/\frac1x\to1$ as $x\to\infty$, and $\int_1^\infty\frac{dx}x$ diverges, so by limit comparison the integral **diverges** (the part over $[0,1]$ is finite).
:::

::: {.solution for="prob-mit1801n-6b-q7" status="draft"}
a) $\frac18$ (@exm-improper-basic).

f) With $u=\ln x$: $\int_1^\infty\frac{du}{u^2}=1$. Convergent, value $1$.

k) Integrating by parts twice, $\int e^{-2x}\cos x\,dx=\frac{e^{-2x}(\sin x-2\cos x)}5$. At $\infty$ this tends to $0$, at $0$ it is $-\frac25$, so the integral converges to $\frac25$.

m) $-\frac1{2(x+2)^2}\Big|_0^\infty=0+\frac18=\frac18$.
:::

::: {.solution for="prob-mit1801n-6b-q8" status="draft"}
$\int_0^xe^{-t^2}dt$ increases to $\frac{\sqrt\pi}2>0$ (and is at least $\int_0^1e^{-t^2}dt>0$ for $x\ge1$), while $e^{x^2}\to\infty$. So the product tends to $+\infty$.
:::
