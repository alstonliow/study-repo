<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-probability-2-09" status="draft"}
(a) Geometric with $p = 0.0125$: the number of balls up to and including
    the dismissal ball, $\Pr(X = k) = (1-p)^{k-1}p$ for $k\ge1$.

(b) $\Pr(X = 1) = p = 0.0125$.

(c) $E(X) = 1/p = 80$ balls.

(d) The geometric distribution is memoryless:
    $$\Pr(X > 200 + k\mid X > 200) = (1-p)^k = \Pr(X > k).$$
    So the remaining number of balls has the same distribution as at the
    start, and we expect $80$ more. (Under this model the batter does not
    "get their eye in".)
:::
