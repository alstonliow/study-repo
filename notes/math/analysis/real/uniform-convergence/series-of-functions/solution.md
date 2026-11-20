<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-ats-4-q14" status="draft"}
(a) Converges pointwise absolutely, not uniformly.

1. The terms are $\ge 0$. At $x = 0$ the sum is $0$; for $x > 0$ it is a geometric series with sum $S(x) = \dfrac{xe^{-x}}{1 - e^{-x}} = \dfrac{x}{e^x - 1}$.

2. $S(x) \to 1$ as $x \to 0^+$ but $S(0) = 0$. A uniform limit of the continuous partial sums would be continuous, so the convergence is not uniform (hence not uniform absolute either).

(b) Converges pointwise absolutely, not uniformly.

1. At $x = 0$ all terms vanish. For $x > 0$, $0 \le f_n(x) \le \dfrac{n^2x}{n^4x^2} = \dfrac{1}{n^2x}$, which is summable.

2. $f_n(1/n^2) = \frac12$, so $\sup_I|f_n| \ge \frac12$ does not tend to $0$. The terms of a uniformly convergent series tend to $0$ uniformly, so the convergence is not uniform.

(c) Converges uniformly on $[0,1]$; absolutely at each $x \in [0,1)$ but not at $x = 1$, so not pointwise absolute (or uniform absolute) on $I$.

1. For fixed $x \in [0,1]$, $x^n/n$ decreases to $0$, so the series converges by the alternating series test, and the tail after $N$ terms is at most $x^{N+1}/(N+1) \le 1/(N+1)$, uniformly in $x$. So the convergence is uniform.

2. $\sum x^n/n$ converges for $x < 1$ (comparison with $\sum x^n$) and diverges at $x = 1$ (harmonic series).
:::

::: {.solution for="prob-camib-ats-4-q15" status="draft"}
(a) Fix $x \in X$. For $n \ge 2|x|$, $|x - n| \ge n - |x| \ge n/2$, so $(x - n)^{-2} \le 4/n^2$, which is summable. So the series converges (absolutely).

(b) No. For each $N$, the tail $\sum_{n>N}(x - n)^{-2}$ is at least $(x - (N+1))^{-2}$, which is unbounded as $x \to N + 1$ within $X$. So $\sup_X|f - \sum_{n\le N}| = \infty$ for all $N$.

(c) Fix $R > 0$. On $X \cap (-R,R)$, for $n \ge 2R$ the terms are bounded by $4/n^2$, so by the Weierstrass M-test $\sum_{n\ge2R}(x - n)^{-2}$ converges uniformly there and its sum is continuous. Adding the finitely many continuous terms with $n < 2R$, $f$ is continuous on $X \cap (-R,R)$. Continuity is local and $R$ is arbitrary, so $f \in C(X)$.
:::
