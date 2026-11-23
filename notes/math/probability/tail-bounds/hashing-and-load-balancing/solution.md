<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-13-q1" status="draft"}
(a) No collision at all means the $n$ first hashes go to distinct buckets: $\frac{n!}{n^n}$, the probability that a random function on $n$ points is a bijection. It tends to $0$: $\frac{n!}{n^n}=\prod_{k=1}^n\frac kn\le\frac1n$, since the factor for $k=1$ is $\frac1n$ and the others are at most $1$.

(c) While inserting $d_k$, there is always exactly one item waiting to be placed and $k-1$ occupied buckets: after an eviction the evicted item is waiting and the occupancy is unchanged. Each hash is a fresh uniform choice, colliding with probability $\frac{k-1}n$, independently of earlier ones. So $C_k$ is the number of failures before the first success in independent trials with success probability $q=\frac{n-k+1}n$, and
$$E[C_k]=\frac1q-1=\frac{k-1}{n-k+1}$$
(@prp-standard-distributions-1-4, minus the final success).

(b) This is $k=n$: $E[C_n]=n-1$.

(d) By linearity, $E[C]=\sum_{k=1}^n\frac{k-1}{n-k+1}=\sum_{j=1}^n\frac{n-j}j=nH_n-n$, where $H_n=\sum_{j=1}^n\frac1j\approx\ln n$.
:::

::: {.solution for="prob-mit6042f10-11-q3" status="draft"}
Birthdays are independent and uniform.

(a) The $m$ surveyed people have different birthdays with probability $\frac{N!}{(N-m)!N^m}$. Given that, each of the other $k-m$ people avoids those $m$ days with probability $1-\frac mN$, independently. So
$$\Pr\{A\}=\frac{N!}{(N-m)!N^m}\Bigl(1-\frac mN\Bigr)^{k-m}\sim e^{-\frac{m^2}{2N}}e^{-\frac{m(k-m)}N}=e^{\frac{-m^2-2mk+2m^2}{2N}}=e^{\frac{m(m-2k)}{2N}}.$$

(b) Setting $\Pr\{A\}=\frac12$ gives $\frac{m(2k-m)}{2N}=\ln2$, the quadratic $m^2-2km+2N\ln2=0$, whose relevant root is
$$m=k-\sqrt{k^2-2N\ln2}=k\Bigl(1-\sqrt{1-\tfrac{2N\ln2}{k^2}}\Bigr).$$
When $k$ is large, $x=\frac{2N\ln2}{k^2}\ll1$, and the hint gives $m\sim k\cdot\frac x2=\frac{N\ln2}k$.
:::

::: {.solution for="prob-mit6042f10-12-q6" status="draft"}
(a) $\Pr(X_i=1)=\bigl(1-\frac1n\bigr)^n$ and $\Pr(X_i=0)=1-\bigl(1-\frac1n\bigr)^n$. They are not independent (for $n\ge2$): all boxes cannot be empty, so $\Pr(X_1=\dots=X_n=1)=0\ne\prod_i\Pr(X_i=1)$.

(b) By linearity, the expected number of empty boxes is $n(1-\frac1n)^n\sim\frac ne$, so $c=\frac1e$.

(c) If at least $k$ balls fall in box $1$, then some set of $k$ balls all fall there. A given set of $k$ balls does so with probability $n^{-k}$, and there are $\binom nk$ sets; by the union bound (@thm-union-bound) the probability is at most $\binom nkn^{-k}$.

(d) $\binom nkn^{-k}=\frac{n(n-1)\cdots(n-k+1)}{k!\,n^k}\le\frac1{k!}$. By the union bound over the $n$ boxes, $\Pr\{R\ge k\}\le\frac n{k!}$.

(e) Let $k=\lceil n^\epsilon\rceil$. By @prp-factorial-bounds, $k!\ge(k/e)^k$, so $\ln\frac n{k!}\le\ln n-k\ln\frac ke$. Since $k\ge n^\epsilon$, $k\ln\frac ke\ge n^\epsilon(\epsilon\ln n-1)$, which grows much faster than $\ln n$. So $\frac n{k!}\to0$, and $\Pr\{R\ge n^\epsilon\}\le\Pr\{R\ge k\}\to0$.
:::
