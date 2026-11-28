<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-probability-2-08"}
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

::: {.solution for="prob-eecs126hw-7-q3" status="draft"}
Throughout, $m/n=\ln n-\ln\lambda+o(1)$, so $m/n^2\to0$. Inequalities (2) and (3) are meant as $\limsup\le$ and $\liminf\ge$.

(a) Let $E_i$ be the event that bin $i$ is empty. For a set of $j$ bins, all are empty with probability $(1-j/n)^m$. By inclusion–exclusion, $P(\bigcup_iE_i)=\sum_{j\ge1}(-1)^{j+1}\binom nj(1-\frac jn)^m$, and $p_0=1-P(\bigcup_iE_i)$.

(b) Choose which $k$ bins are empty ($\binom nk$ ways, disjoint events by symmetry). The $m$ balls avoid those $k$ bins with probability $(1-k/n)^m$; given that, they are uniform on the other $n-k$ bins, and none of those is empty with probability $p_0(m,n-k)$.

(c) $\binom nk\le\frac{n^k}{k!}$ and $(1-\frac kn)^m\le e^{-km/n}$, so the left side is at most $\frac{(ne^{-m/n})^k}{k!}\to\frac{\lambda^k}{k!}$.

(d) i. $\binom nk=\frac{n(n-1)\cdots(n-k+1)}{k!}\ge\frac{(n-k)^k}{k!}=\frac{n^k}{k!}(1-\frac kn)^k$.

ii. For $n\ge2k$, $-\frac kn-\frac{k^2}{n^2}\le\ln(1-\frac kn)\le-\frac kn$, so
$$k\ln n-\frac{km}{n}-\frac{k^2m}{n^2}\le\ln\Bigl\{n^k\Bigl(1-\frac kn\Bigr)^m\Bigr\}\le k\ln n-\frac{km}{n}.$$
Here $k\ln n-\frac{km}{n}=k\ln(ne^{-m/n})\to k\ln\lambda$ and $\frac{k^2m}{n^2}\to0$.

iii. $k$ is fixed and $n\to\infty$, so $(1-\frac kn)^k\to1$. Combining i–iii, the left side of (3) is at least a quantity tending to $\frac{\lambda^k}{k!}$.

(e) Write $a_j=\binom nj(1-\frac jn)^m$, so $a_j\to\frac{\lambda^j}{j!}$ for each fixed $j$ by (c)–(d). The inclusion–exclusion partial sums alternately over- and under-estimate (Bonferroni inequalities): for every $r$,
$$\sum_{j=0}^{2r+1}(-1)^ja_j\le p_0(m,n)\le\sum_{j=0}^{2r}(-1)^ja_j.$$
Taking limits and then $r\to\infty$, both bounds tend to $\sum_j(-1)^j\frac{\lambda^j}{j!}=e^{-\lambda}$.

For $p_k$, use (1): $(n-k)e^{-m/(n-k)}=ne^{-m/n}\cdot(1-\frac kn)e^{-mk/(n(n-k))}\to\lambda$ because $m/n^2\to0$, so $p_0(m,n-k)\to e^{-\lambda}$ and $p_k(m,n)\to\frac{\lambda^k}{k!}e^{-\lambda}$.
:::
