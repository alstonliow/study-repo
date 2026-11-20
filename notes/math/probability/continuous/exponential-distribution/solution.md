<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-14-q3" status="draft"}
The life span is $T\sim\mathrm{Exp}(\lambda)$ with $\frac1\lambda=50$ (@thm-exponential-mean-variance), so $\Pr(T>t)=e^{-t/50}$ (@prp-exponential-tail).

(a) $\Pr(T\le30)=1-e^{-0.6}\approx0.451$.

(b) A new bulb: $\Pr(T>30)=e^{-0.6}\approx0.549$.

(c) By memorylessness (@prp-exponential-memoryless), $\Pr(T>60\mid T>30)=\Pr(T>30)=e^{-0.6}\approx0.549$.
:::

::: {.solution for="prob-mit1805s22-4-q1" status="draft"}
(a) For $x\ge0$, $P(X\ge x)=\int_x^\infty\lambda e^{-\lambda u}\,du=e^{-\lambda x}$.

(b) Integrating by parts, $E[X]=\int_0^\infty x\lambda e^{-\lambda x}\,dx=\frac1\lambda$ and $E[X^2]=\int_0^\infty x^2\lambda e^{-\lambda x}\,dx=\frac2{\lambda^2}$, so $\mathrm{Var}(X)=\frac1{\lambda^2}$ and the standard deviation is $\frac1\lambda$.

(c) $T\ge t$ exactly when both $X_i\ge t$, so for $t\ge0$, $P(T\ge t)=e^{-\lambda t}e^{-\lambda t}=e^{-2\lambda t}$. Hence $F_T(t)=1-e^{-2\lambda t}$ and $f_T(t)=2\lambda e^{-2\lambda t}$ for $t\ge0$: $T\sim\exp(2\lambda)$.

(d) The lifetimes are $\exp(2)$, $\exp(3)$, $\exp(5)$. As in (c), the first failure time $T$ has $P(T\ge t)=e^{-(2+3+5)t}$, so $T\sim\exp(10)$ and $E[T]=\frac1{10}$ year (about $36.5$ days).
:::
