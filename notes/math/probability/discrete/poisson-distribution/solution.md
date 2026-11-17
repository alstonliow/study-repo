<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-probability-2-08" status="draft"}
(a) Poisson with mean $\lambda = 0.83$:
    $\Pr(N = k) = e^{-0.83}\,0.83^k/k!$.

(b) $\Pr(N = 0) = e^{-0.83}\approx 0.436$.

(c) In $t$ minutes the count is Poisson with mean $0.83t$, so
    $\Pr(\text{at least one}) = 1 - e^{-0.83t}$. We need
    $$1 - e^{-0.83t}\ge 0.95\iff e^{-0.83t}\le 0.05\iff t\ge\frac{\ln 20}{0.83}\approx 3.61.$$
    So be prepared to wait about $3.6$ minutes.
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-12-q6" status="draft"}
For $n\ge0$, split the event $X_1+X_2=n$ by the value of $X_1$ and use independence:
$$\Pr(X_1+X_2=n)=\sum_{k=0}^n\frac{e^{-\lambda_1}\lambda_1^k}{k!}\cdot\frac{e^{-\lambda_2}\lambda_2^{n-k}}{(n-k)!}=\frac{e^{-(\lambda_1+\lambda_2)}}{n!}\sum_{k=0}^n\binom nk\lambda_1^k\lambda_2^{n-k}=\frac{e^{-(\lambda_1+\lambda_2)}(\lambda_1+\lambda_2)^n}{n!},$$
by the binomial theorem. This is the $\mathrm{Poisson}(\lambda_1+\lambda_2)$ distribution, as in @thm-sum-of-poissons.
:::
