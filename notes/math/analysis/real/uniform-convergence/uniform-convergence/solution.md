<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-ats-1-q11" status="draft"}
1. *Baire property of $\mathbb{R}$.* If $\mathbb{R} = \bigcup_N F_N$ with each $F_N$ closed, then some $F_N$ contains an open interval. Otherwise each $F_N$ has empty interior; start with $I_0 = [0,1]$, and given a closed interval $I_{N-1}$ of positive length, its interior minus $F_N$ is a non-empty open set, so it contains a closed interval $I_N$ of positive length with $I_N \cap F_N = \emptyset$. The nested intervals $I_N$ have a common point, which lies in no $F_N$: a contradiction.

2. Suppose continuous $f_n \to 1_{\mathbb{Q}}$ pointwise. Let $F_N = \{x : |f_n(x) - f_m(x)| \le \frac13 \text{ for all } n, m \ge N\}$, an intersection of closed sets, hence closed. Pointwise convergence gives $\bigcup_N F_N = \mathbb{R}$, so some $F_N$ contains an open interval $J$.

3. For $x \in J$ and $n \ge N$, $|f_n(x) - f_N(x)| \le \frac13$; letting $n \to \infty$, $|1_{\mathbb{Q}}(x) - f_N(x)| \le \frac13$.

4. $f_N$ is continuous, so $J$ contains a smaller open interval $J'$ on which $f_N$ varies by less than $\frac14$. Take $q \in J' \cap \mathbb{Q}$ and $r \in J' \setminus \mathbb{Q}$. Then
$$1 = |1_{\mathbb{Q}}(q) - 1_{\mathbb{Q}}(r)| \le \tfrac13 + |f_N(q) - f_N(r)| + \tfrac13 < \tfrac13 + \tfrac14 + \tfrac13 < 1,$$
a contradiction.
:::

::: {.solution for="prob-camib-ats-1-q12" status="draft"}
In each case the pointwise limit is $0$, so a uniform limit, if any, is $0$.

(a) Not uniform: $\sup_{(0,1)}x^{2n} = 1$ for every $n$ (let $x \to 1$).

(b) Uniform, to $0$: $\frac{d}{dx}(xe^{-nx}) = (1 - nx)e^{-nx}$, so the maximum on $[0,\infty)$ is at $x = 1/n$ and equals $1/(en) \to 0$.

(c) Not uniform on $\mathbb{R}$: at $x = -n\pi/2$, $|f_n(x)| = e^{n\pi/2}$, so $\sup_{\mathbb{R}}|f_n| = \infty$. (On $[0,\infty)$ it is uniform: $|f_n(x)| \le xe^{-x}/n \le 1/(en)$.)
:::

::: {.solution for="prob-camib-ats-1-q13" status="draft"}
"Convergent" means pointwise convergent.

(a) Diagonal argument.

1. $(f_n(1))_n$ is bounded by $g(1)$, so by Bolzano–Weierstrass there is an infinite set $S_1 \subset \mathbb{N}$ of indices along which $f_n(1)$ converges.

2. Given $S_{k-1}$, the values $f_n(k)$, $n \in S_{k-1}$, are bounded by $g(k)$, so there is an infinite $S_k \subset S_{k-1}$ along which $f_n(k)$ converges.

3. Let $n_k$ be the $k$-th element of $S_k$. Then $n_1 < n_2 < \cdots$ (the $k$-th element of $S_k$ is at least the $k$-th element of $S_{k-1}$, which exceeds its $(k-1)$-th), and for each $j$, $n_k \in S_j$ for all $k \ge j$. So $f_{n_k}(j)$ converges for every $j \in \mathbb{N}$.

(b) Not necessarily. For $x \in \mathbb{R}$ let $f_n(x)$ be the $n$-th binary digit of $x - \lfloor x\rfloor$ (using the expansion that does not end in recurring $1$s). Then $|f_n| \le 1$. Given any subsequence $n_1 < n_2 < \cdots$, let $x \in [0,1)$ have digit $k \bmod 2$ at position $n_k$ and $0$ at all other positions. This expansion has infinitely many $0$s, so it is the one used, and $f_{n_k}(x)$ alternates $1, 0, 1, 0, \ldots$, which does not converge.
:::
