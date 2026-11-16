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
