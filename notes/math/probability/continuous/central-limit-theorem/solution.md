<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-14-q2" status="draft"}
(a) One toss of Bob $i$'s coin has mean $0$ and variance $i^2$. Group the tosses into $n$ rounds, one toss of each Bob per round: each round contributes an independent sum with mean $0$ and variance $\sum_{i=1}^ki^2=\frac{k(k+1)(2k+1)}6$. By the central limit theorem (@thm-central-limit-theorem), $(X_1+\dots+X_k)/\sqrt n$ is approximately $N\bigl(0,\frac{k(k+1)(2k+1)}6\bigr)$.

(b) Let $Z_n=\frac1{\sqrt n}\sum_{k=1}^n\frac{X_k-\mu}\sigma$, which tends to $N(0,1)$ in distribution. The event is $|Z_n|\le n^{\alpha-1/2}$.

- $\alpha=\frac12$: the limit is $\Phi(1)-\Phi(-1)=2\Phi(1)-1\approx0.683$.
- $\alpha>\frac12$: the interval $[-n^{\alpha-1/2},n^{\alpha-1/2}]$ grows. By Chebyshev, $\Pr(|Z_n|>t)\le\frac1{t^2}$, so the probability tends to $1$.
- $\alpha<\frac12$: the interval shrinks to $0$. For any fixed $\varepsilon>0$ it is eventually inside $[-\varepsilon,\varepsilon]$, whose probability tends to $2\Phi(\varepsilon)-1$, which is as small as we like. So the limit is $0$.
:::
