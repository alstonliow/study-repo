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
