<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-ats-2-q5" status="draft"}
Write $\|h\|_\infty = \sup_{[a,b]}|h|$. Then $d_{C^k}(f,g) = \|f - g\|_{C^k}$ with $\|f\|_{C^k} = \sum_{j\le k}\|f^{(j)}\|_\infty$, which is a norm; so $d_{C^k}$ is a metric.

(a)

1. Let $(f_n)$ be Cauchy in $C^k$. For each $j \le k$, $\|f_n^{(j)} - f_m^{(j)}\|_\infty \le d_{C^k}(f_n,f_m)$, so $(f_n^{(j)})_n$ is uniformly Cauchy and converges uniformly to some $g_j$, which is continuous as a uniform limit of continuous functions.

2. For $j < k$, $f_n^{(j)}(x) = f_n^{(j)}(a) + \int_a^x f_n^{(j+1)}$. Uniform convergence lets us pass to the limit under the integral: $g_j(x) = g_j(a) + \int_a^x g_{j+1}$. By the fundamental theorem of calculus, $g_j$ is differentiable with $g_j' = g_{j+1}$.

3. So $f = g_0 \in C^k$ with $f^{(j)} = g_j$, and $d_{C^k}(f_n,f) = \sum_j\|f_n^{(j)} - g_j\|_\infty \to 0$.

(b) Let $(If)(x) = \int_a^x f$. By the fundamental theorem of calculus, $If \in C^{k+1}$ with $(If)^{(j)} = f^{(j-1)}$ for $1 \le j \le k+1$. Also $\|If - Ig\|_\infty \le (b - a)\|f - g\|_\infty$. Hence
$$d_{C^{k+1}}(If, Ig) \le (b - a)\|f - g\|_\infty + \sum_{j=0}^k\|f^{(j)} - g^{(j)}\|_\infty \le (1 + b - a)\,d_{C^k}(f,g),$$
so $I$ is Lipschitz, hence continuous.

(c) $d_{C^k}(f',g') = \sum_{j=0}^k\|f^{(j+1)} - g^{(j+1)}\|_\infty \le d_{C^{k+1}}(f,g)$, so differentiation is $1$-Lipschitz from $C^{k+1}$ to $C^k$.
:::

::: {.solution for="prob-camib-ats-2-q8" status="draft"}
(a) $\ell^\infty$ is the space of bounded functions $\mathbb{N} \to \mathbb{R}$ with the uniform metric, which is complete. Directly:

1. Let $(x^{(m)})$ be Cauchy. For each $k$, $|x^{(m)}_k - x^{(p)}_k| \le d(x^{(m)},x^{(p)})$, so $(x^{(m)}_k)_m$ is Cauchy in $\mathbb{R}$ and converges to some $x_k$.

2. Given $\varepsilon > 0$, choose $N$ with $|x^{(m)}_k - x^{(p)}_k| \le \varepsilon$ for all $k$ and $m, p \ge N$. Letting $p \to \infty$: $|x^{(m)}_k - x_k| \le \varepsilon$ for all $k$ and $m \ge N$.

3. So $x = x^{(N)} + (x - x^{(N)})$ is bounded, that is, $x \in \ell^\infty$, and $d(x^{(m)},x) \le \varepsilon$ for $m \ge N$.

(b)

1. *Well defined.* $(x_n - y_n)^2 \le 2x_n^2 + 2y_n^2$, so the series converges by comparison.

2. *Metric.* $d \ge 0$, $d = 0$ iff $x = y$, and $d$ is symmetric. For the triangle inequality, for each $K$ the Euclidean triangle inequality in $\mathbb{R}^K$ gives
$$\Big(\sum_{n\le K}(x_n - z_n)^2\Big)^{1/2} \le \Big(\sum_{n\le K}(x_n - y_n)^2\Big)^{1/2} + \Big(\sum_{n\le K}(y_n - z_n)^2\Big)^{1/2} \le d(x,y) + d(y,z);$$
let $K \to \infty$.

3. *Complete.* Let $(x^{(m)})$ be Cauchy. As in (a), each coordinate converges, $x^{(m)}_k \to x_k$. Given $\varepsilon$, choose $N$ with $d(x^{(m)},x^{(p)}) \le \varepsilon$ for $m,p \ge N$. For every $K$, $\sum_{k\le K}(x^{(m)}_k - x^{(p)}_k)^2 \le \varepsilon^2$; let $p \to \infty$, then $K \to \infty$: $\sum_k(x^{(m)}_k - x_k)^2 \le \varepsilon^2$ for $m \ge N$.

4. So $x^{(N)} - x \in \ell^2$, hence $x \in \ell^2$ by step 1 (as $\ell^2$ is closed under sums), and $d(x^{(m)},x) \le \varepsilon$ for $m \ge N$.
:::
