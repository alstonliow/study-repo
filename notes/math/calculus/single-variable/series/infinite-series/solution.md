<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

::: {.solution for="prob-mit1801n-7a-q1" status="draft"}
a) A geometric series with ratio $\frac14$: it converges to $\frac1{1-1/4}=\frac43$.

b) The terms $(-1)^n$ do not tend to $0$, so it diverges (@thm-nth-term-test); the partial sums alternate $1,0,1,0,\ldots$

c) The terms $\frac n{n+1}\to1\ne0$, so it diverges (the partial sums grow without bound).
:::

::: {.solution for="prob-mit1801n-7b-q1" status="draft"}
Apply @thm-integral-test (the functions below are positive and decreasing for $x\ge2$; finitely many terms do not affect convergence).

a) $\int_2^N\frac{x\,dx}{x^2+4}=\frac12\ln(x^2+4)\Big|_2^N\to\infty$: **diverges**.

b) $\int_0^\infty\frac{dx}{1+x^2}=\frac\pi2$ is finite: **converges**.

f) $\int_1^\infty x^{-p}dx$ converges exactly when $p>1$ (@thm-p-integrals); for $p\le0$ the terms do not tend to $0$. So the series converges if and only if $p>1$ (@cor-p-series).
:::

::: {.solution for="prob-mit1801n-7b-q2" status="draft"}
Use @thm-limit-comparison-series with a $p$-series (@cor-p-series).

a) $\frac{1/(n^2+3n)}{1/n^2}\to1$ and $\sum\frac1{n^2}$ converges: **converges**.

c) $\frac{1/\sqrt{n^2+n}}{1/n}=\frac1{\sqrt{1+1/n}}\to1$ and $\sum\frac1n$ diverges: **diverges**.

d) $\frac{\sin(1/n^2)}{1/n^2}\to1$ (@thm-two-trig-limits) and $\sum\frac1{n^2}$ converges: **converges**.

e) $\frac{\sqrt n/(n^2+1)}{n^{-3/2}}=\frac{n^2}{n^2+1}\to1$ and $\sum n^{-3/2}$ converges: **converges**.
:::
