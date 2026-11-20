<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-ats-2-q12" status="draft"}
(We write $p_{n,k}$ throughout; the printed $p_{k,n}$ in (c) means the same.)

(a) Let $\phi(t) = a_1 + (b_1 - a_1)t$, a bijection $[0,1] \to [a_1,b_1]$. If polynomials $q_n \rightrightarrows f \circ \phi$ on $[0,1]$, then $q_n \circ \phi^{-1}$ are polynomials and $\sup_{[a_1,b_1]}|q_n \circ \phi^{-1} - f| = \sup_{[0,1]}|q_n - f \circ \phi| \to 0$.

(b)

1. By the binomial theorem, $\sum_k p_{n,k}(x) = (x + (1 - x))^n = 1$.

2. Using $k\binom nk = n\binom{n-1}{k-1}$ and $k(k-1)\binom nk = n(n-1)\binom{n-2}{k-2}$, the binomial theorem gives $\sum_k kp_{n,k}(x) = nx$ and $\sum_k k(k-1)p_{n,k}(x) = n(n-1)x^2$. So $\sum_k k^2p_{n,k}(x) = n(n-1)x^2 + nx$.

3. Expanding the square:
$$\sum_k\Big(x - \frac kn\Big)^2p_{n,k} = x^2 - 2x\cdot x + \frac{n(n-1)x^2 + nx}{n^2} = \frac{x - x^2}{n} = \frac{x(1-x)}{n}.$$

(c) By the first identity, $f(x) = \sum_k f(x)p_{n,k}(x)$, so $p_n(x) - f(x) = \sum_k(f(k/n) - f(x))p_{n,k}(x)$. The triangle inequality (the $p_{n,k}$ are $\ge 0$ on $[0,1]$), with the sum split according to $|x - k/n| < \delta$ or $\ge \delta$, gives the bound.

(d)

1. $f$ is bounded, $|f| \le M$, and uniformly continuous on $[0,1]$. Given $\varepsilon > 0$, choose $\delta$ with $|f(s) - f(x)| < \varepsilon$ whenever $|s - x| < \delta$.

2. The first sum is less than $\varepsilon\sum_kp_{n,k}(x) = \varepsilon$.

3. In the second sum, $|f(k/n) - f(x)| \le 2M$ and $1 \le (x - k/n)^2/\delta^2$, so by the second identity it is at most
$$\frac{2M}{\delta^2}\sum_k\Big(x - \frac kn\Big)^2p_{n,k}(x) = \frac{2Mx(1-x)}{n\delta^2} \le \frac{M}{2n\delta^2}.$$

4. So $\sup_{[0,1]}|p_n - f| \le \varepsilon + M/(2n\delta^2) < 2\varepsilon$ for all large $n$: $p_n \rightrightarrows f$.
:::
