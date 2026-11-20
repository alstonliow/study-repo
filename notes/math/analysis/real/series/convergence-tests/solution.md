<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cama1s-1-q8" status="draft"}
1. For $w \ne \pm 1$, $\dfrac{1}{1-w} - \dfrac{1}{1-w^2} = \dfrac{(1+w) - 1}{1-w^2} = \dfrac{w}{1-w^2}$. With $w = z^{2^k}$ the $k$-th term ($k \ge 0$) is $\dfrac{1}{1-z^{2^k}} - \dfrac{1}{1-z^{2^{k+1}}}$. (The hypothesis also gives $z \ne 1$, since $z = 1$ would give $z^2 = 1$.)

2. So the partial sum of the terms $k = 0, \dots, N$ telescopes to $\dfrac{1}{1-z} - \dfrac{1}{1-z^{2^{N+1}}}$.

3. If $|z| < 1$, then $z^{2^{N+1}} \to 0$ and the sum is $\dfrac{1}{1-z} - 1 = \dfrac{z}{1-z}$.

4. If $|z| > 1$, then $|z^{2^{N+1}}| \to \infty$, so $\dfrac{1}{1-z^{2^{N+1}}} \to 0$ and the sum is $\dfrac{1}{1-z}$.

5. If $|z| = 1$, the $k$-th term has modulus $\dfrac{1}{|1 - z^{2^{k+1}}|} \ge \dfrac12$, so the terms do not tend to $0$ and the series diverges.
:::

::: {.solution for="prob-cama1s-1-q9" status="draft"}
1. $\left|\frac{\sin n}{n^2}\right| \le \frac{1}{n^2}$ and $\sum 1/n^2$ converges, so the first series converges absolutely.

2. For $z \ne 0$ the ratio of consecutive terms of $\sum n^2z^n/5^n$ has modulus $\frac{(n+1)^2}{n^2}\frac{|z|}{5} \to \frac{|z|}{5}$. By the ratio test it converges (absolutely) for $|z| < 5$ and diverges for $|z| > 5$; for $|z| = 5$ the terms have modulus $n^2 \not\to 0$, so it diverges. Answer: $|z| < 5$.

3. $1/(4+\sqrt n)$ decreases to $0$, so the alternating series test gives convergence. It is not absolutely convergent, since $1/(4+\sqrt n) \ge 1/(5\sqrt n) \ge 1/(5n)$.

4. For $\sum z^n(1-z)/n$: if $z = 1$ every term is $0$, so it converges. If $|z| < 1$ it converges absolutely by comparison with $\sum |z|^n$. If $|z| > 1$ then $|z|^n/n \to \infty$, so the terms do not tend to $0$ and it diverges. If $|z| = 1$, $z \ne 1$: the partial sums $\sum_{k=1}^n z^k = z\frac{1-z^n}{1-z}$ are bounded by $2/|1-z|$, and $1/n$ decreases to $0$, so $\sum z^n/n$ converges by the Abel (Dirichlet) test, and so does $(1-z)\sum z^n/n$. Answer: $|z| \le 1$.
:::

::: {.solution for="prob-cama1s-1-q11" status="draft"}
1. For odd $n$ both terms are positive. For even $n \ge 2$, $a_n = \frac{1}{\sqrt n} - \frac1n > 0$ because $\sqrt n < n$.

2. $0 < a_n \le \frac{1}{\sqrt n} + \frac1n \to 0$.

3. $(-1)^{n-1}a_n = \frac{(-1)^{n-1}}{\sqrt n} + \frac1n$. The series $\sum (-1)^{n-1}/\sqrt n$ converges by the alternating series test. If $\sum(-1)^{n-1}a_n$ converged, then so would the difference $\sum 1/n$, which diverges. So $\sum(-1)^{n-1}a_n$ diverges. (The alternating series test fails here because $(a_n)$ is not decreasing.)
:::

::: {.solution for="prob-cama1s-1-q12" status="draft"}
(a) Write $a_j = S_j - S_{j-1}$. Then
$$\sum_{j=m}^n a_jb_j = \sum_{j=m}^n S_jb_j - \sum_{j=m-1}^{n-1} S_jb_{j+1} = S_nb_n - S_{m-1}b_m + \sum_{j=m}^{n-1} S_j(b_j - b_{j+1}).$$

(b)

1. Let $|S_j| \le M$ for all $j$. Take $m = 1$ in (a): $\sum_{j=1}^n a_jb_j = S_nb_n + \sum_{j=1}^{n-1} S_j(b_j - b_{j+1})$.

2. $|S_nb_n| \le Mb_n \to 0$.

3. $|S_j(b_j - b_{j+1})| \le M(b_j - b_{j+1})$, and $\sum_{j=1}^{n-1}(b_j - b_{j+1}) = b_1 - b_n \le b_1$, so $\sum S_j(b_j - b_{j+1})$ converges absolutely by comparison.

4. Hence the partial sums $\sum_{j=1}^n a_jb_j$ converge.

(c) It converges. Take $a_n = \cos n$, $b_n = 1/n$. Using $2\sin\frac12\cos j = \sin(j+\frac12) - \sin(j-\frac12)$, the sum telescopes:
$$\sum_{j=1}^n \cos j = \frac{\sin(n+\frac12) - \sin\frac12}{2\sin\frac12}, \qquad \text{so } \Big|\sum_{j=1}^n\cos j\Big| \le \frac{1}{\sin\frac12}.$$
Now apply (b).

(d) If $b_n$ decreases to $0$, take $a_n = (-1)^{n-1}$; then $S_n \in \{0, 1\}$ is bounded, so $\sum(-1)^{n-1}b_n$ converges by (b).
:::
