<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-ats-2-q6" status="draft"}
(a) and (c) are; (b) is not.

(a) $f$ is the distance from $x$ to the set $S = \{n^2\}$. For any $s \in S$, $|x - s| \le |x - y| + |y - s|$; taking the infimum over $s$ gives $f(x) \le |x - y| + f(y)$, and symmetrically. So $|f(x) - f(y)| \le |x - y|$: $f$ is $1$-Lipschitz, hence uniformly continuous.

(b) Let $x_n = \sqrt{n\pi}$ and $y_n = \sqrt{n\pi + \pi/2}$. Then $y_n - x_n = \dfrac{\pi/2}{y_n + x_n} \to 0$, but $|f(y_n) - f(x_n)| = |\sin(n\pi + \pi/2) - \sin(n\pi)| = 1$.

(c) $f'(x) = \dfrac{3x^2\cos x^3}{x^2 + 1} - \dfrac{2x\sin x^3}{(x^2 + 1)^2}$. Since $\frac{x^2}{x^2+1} \le 1$ and $\frac{2x}{(x^2+1)^2} \le 1$, $|f'| \le 4$. By the mean value theorem $f$ is $4$-Lipschitz, hence uniformly continuous.
:::

::: {.solution for="prob-camib-ats-2-q7" status="draft"}
(a)

1. Suppose not. Then there are $\varepsilon > 0$ and points $x_n \to \infty$ with $f(x_n) \ge \varepsilon$. Passing to a subsequence, we may assume $x_{n+1} > x_n + 1$.

2. By uniform continuity, choose $\delta \in (0,1)$ with $|f(x) - f(y)| < \varepsilon/2$ whenever $|x - y| < \delta$. Then $f \ge \varepsilon/2$ on each $[x_n, x_n + \delta]$, and these intervals are disjoint.

3. Since $f \ge 0$, $\int_0^{x_N + 1}f \ge \sum_{n\le N}\int_{x_n}^{x_n+\delta}f \ge N\varepsilon\delta/2 \to \infty$, contradicting convergence of $\int_0^\infty f$.

(b) No. Let $f$ be $0$ except for a triangular spike of height $1$ on $[n - n^{-2}, n + n^{-2}]$ for each $n \ge 2$. It is continuous and non-negative, $\int_0^\infty f = \sum_{n\ge2}n^{-2} < \infty$, but $f(n) = 1$ for all $n \ge 2$. (The spikes get steeper, so $f$ is not uniformly continuous.)
:::
