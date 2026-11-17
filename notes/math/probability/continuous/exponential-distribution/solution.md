<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-14-q3" status="draft"}
The life span is $T\sim\mathrm{Exp}(\lambda)$ with $\frac1\lambda=50$ (@thm-exponential-mean-variance), so $\Pr(T>t)=e^{-t/50}$ (@prp-exponential-tail).

(a) $\Pr(T\le30)=1-e^{-0.6}\approx0.451$.

(b) A new bulb: $\Pr(T>30)=e^{-0.6}\approx0.549$.

(c) By memorylessness (@prp-exponential-memoryless), $\Pr(T>60\mid T>30)=\Pr(T>30)=e^{-0.6}\approx0.549$.
:::
