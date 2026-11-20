<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cama1s-1-q7" status="draft"}
Let $S_n = a_1 + \cdots + a_n$ and $b_n = a_n/S_n$. Then $b_n/a_n = 1/S_n \to 0$ because $S_n \to \infty$.

1. For $m > n$, since $S_k \le S_m$ for $k \le m$,
$$\sum_{k=n+1}^m b_k = \sum_{k=n+1}^m \frac{a_k}{S_k} \ge \frac{1}{S_m}\sum_{k=n+1}^m a_k = 1 - \frac{S_n}{S_m}.$$

2. For fixed $n$, choose $m$ so large that $S_m \ge 2S_n$; then the block sum is at least $1/2$. So the partial sums of $\sum b_n$ are not Cauchy, and $\sum b_n$ diverges.
:::

::: {.solution for="prob-cama1s-1-q10" status="draft"}
Sums start at $n = 2$ (and at $n = 3$ for the second series, where $\log\log n > 0$).

1. If $\alpha \le 0$, then $1/[n(\log n)^\alpha] \ge 1/n$ for $n \ge 3$, so the series diverges by comparison with the harmonic series.

2. If $\alpha > 0$, the terms are positive and decreasing, so by Cauchy condensation the series converges if and only if $\sum_k 2^k \cdot \dfrac{1}{2^k (k\log 2)^\alpha} = (\log 2)^{-\alpha}\sum_k k^{-\alpha}$ converges, that is, if and only if $\alpha > 1$.

3. The terms $1/(n\log n\log\log n)$ are positive and decreasing for $n \ge 3$. Condensation gives
$$\sum_k \frac{2^k}{2^k\, k\log 2\,\log(k\log 2)} = \frac{1}{\log 2}\sum_k \frac{1}{k\log(k\log 2)},$$
and for large $k$, $\log(k\log 2) \le \log k$, so these terms are at least $1/(k\log k)$, whose sum diverges by step 2 with $\alpha = 1$. So $\sum 1/(n\log n\log\log n)$ diverges.
:::

::: {.solution for="prob-cama1s-4-q10" status="draft"}
(a)

1. Expanding $p_N$ gives $1 + s_N$ plus further products of the $a_n$, all $\ge 0$. So $p_N \ge 1 + s_N \ge s_N$.

2. $1 + x \le e^x$ for $x \ge 0$ (from the exponential series), so $p_N \le e^{a_1}\cdots e^{a_N} = e^{s_N}$.

3. Both $(p_N)$ and $(s_N)$ are increasing, so each converges iff it is bounded. By steps 1 and 2, $(p_N)$ is bounded iff $(s_N)$ is bounded.

(b) The product is $2$. Since $1 + \frac{1}{n^2-1} = \frac{n^2}{(n-1)(n+1)} = \frac{n}{n-1}\cdot\frac{n}{n+1}$, both parts telescope:
$$\prod_{n=2}^N\Big(1 + \frac{1}{n^2-1}\Big) = \frac N1\cdot\frac{2}{N+1} = \frac{2N}{N+1} \to 2.$$
:::
