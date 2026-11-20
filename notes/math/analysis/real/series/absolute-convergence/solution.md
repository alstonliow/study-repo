<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cama1s-1-q13" status="draft"}
(a)

1. $s_{2n} = \sum_{k\le 2n}\frac1k - 2\sum_{k\le n}\frac{1}{2k} = h_{2n} - h_n$.

2. The second series takes two odd reciprocals and then one even one, so its first $3n$ terms are the reciprocals of the odd numbers up to $4n-1$, with plus signs, and of the even numbers up to $2n$, with minus signs. The odd part is $h_{4n} - \frac12 h_{2n}$ and the even part is $\frac12 h_n$, so $t_{3n} = h_{4n} - \frac12h_{2n} - \frac12h_n$.

(b)

1. $\frac1n$ decreases to $0$, so $s_n$ converges by the alternating series test, say to $s$. Grouping in pairs, $s_{2n} = \sum_{k\le n}\left(\frac{1}{2k-1} - \frac{1}{2k}\right)$ is increasing with $s_2 = \frac12$, so $s \ge \frac12 > 0$.

2. By (a), $t_{3n} = (h_{4n} - h_{2n}) + \frac12(h_{2n} - h_n) = s_{4n} + \frac12 s_{2n} \to s + \frac s2 = \frac{3s}{2}$.

3. $t_{3n+1}$ and $t_{3n+2}$ differ from $t_{3n}$ by at most $\frac{2}{4n+1} \to 0$, so $t_n \to 3s/2$.

(Numerically $s = \log 2 \approx 0.6931$ and $3s/2 \approx 1.0397$.)
:::

::: {.solution for="prob-cama1s-1-q14" status="draft"}
(a) Choose signs greedily. Let $T_0 = 0$ and $T_n = \sum_{k\le n}\sigma_kx_k$, where $\sigma_n$ is chosen so that $\sigma_nx_n$ has the opposite sign to $T_{n-1}$ (any sign if $T_{n-1} = 0$ or $x_n = 0$).

1. If $|x_n| \le |T_{n-1}|$, then $|T_n| = |T_{n-1}| - |x_n|$ and $T_n$ has the same sign as $T_{n-1}$ (or is $0$). If $|x_n| > |T_{n-1}|$ (a *crossing*), then $|T_n| = |x_n| - |T_{n-1}| < |x_n|$.

2. If there are only finitely many crossings, then from some point on $|T_n|$ decreases and $T_n$ keeps one sign, so $(T_n)$ is eventually monotone and bounded, hence convergent.

3. If there are infinitely many crossings, let $c(n)$ be the last crossing at or before $n$. By step 1, $|T_n| \le |T_{c(n)}| < |x_{c(n)}|$. Since $c(n) \to \infty$ and $x_n \to 0$, $T_n \to 0$. Either way $\sum\sigma_nx_n$ converges.

(b) Yes. Write $v_n = (x_n, y_n) \in \mathbb{R}^2$ and use the norm $\|v\| = \max(|x|,|y|)$.

1. *Lemma.* If $v_1, \dots, v_N \in \mathbb{R}^2$ have $\|v_i\| \le r$, there are signs $\varepsilon_i$ with $\left\|\sum_{i\le k}\varepsilon_iv_i\right\| \le 4r$ for every $k \le N$.

2. *Proof of the lemma.* Take $r = 1$. Call a coordinate of $\lambda \in [-1,1]^k$ fractional if it is not $\pm1$. We build $\lambda^{(k)} \in [-1,1]^k$ for $k = 2, \dots, N$ with (i) $\sum_{i\le k}\lambda^{(k)}_iv_i = 0$, (ii) at most $2$ fractional coordinates, (iii) every coordinate that is $\pm1$ in $\lambda^{(k)}$ keeps that value in all later $\lambda^{(k')}$. Start with $\lambda^{(2)} = 0$. Given $\lambda^{(k)}$, let $\mu = (\lambda^{(k)}, 0) \in [-1,1]^{k+1}$. The set of $\lambda \in [-1,1]^{k+1}$ with $\sum_{i\le k+1}\lambda_iv_i = 0$ and $\lambda_i = \mu_i$ wherever $\mu_i = \pm1$ is a non-empty (it contains $\mu$) compact polytope, so it has a vertex. In the at most $3$ free coordinates, a vertex satisfies, besides the $2$ linear equations, enough box constraints $\lambda_i = \pm1$ to have no free direction, so at most $2$ of its coordinates are fractional. Let $\lambda^{(k+1)}$ be that vertex. Finally let $\varepsilon_i = \lambda^{(N)}_i$ where this is $\pm1$ and $\varepsilon_i = 1$ otherwise. For each $k \ge 2$, by (iii) $\varepsilon_i = \lambda^{(k)}_i$ at all non-fractional coordinates of $\lambda^{(k)}$, so by (i)
$$\Big\|\sum_{i\le k}\varepsilon_iv_i\Big\| = \Big\|\sum_{i\le k}(\varepsilon_i - \lambda^{(k)}_i)v_i\Big\| \le 2\cdot 2 = 4,$$
since only the at most two fractional coordinates contribute, each at most $2\|v_i\| \le 2$. For $k \le 2$ the bound $2 \le 4$ is trivial.

3. Now let $n_j$ be the least index such that $\|v_n\| \le 2^{-j}$ for all $n \ge n_j$ (it exists since $v_n \to 0$), and split the indices into the finite blocks $B_j = [n_j, n_{j+1})$ (some may be empty), plus the finitely many indices before $n_0$, which get sign $+1$. Apply the lemma to each block $B_j$ with $r = 2^{-j}$.

4. Let $T_j$ be the signed sum over block $B_j$; then $\|T_j\| \le 4\cdot 2^{-j}$, so $\sum_j T_j$ converges absolutely. Any partial sum $\sum_{k\le n}\sigma_kv_k$ with $n \in B_j$ equals a fixed initial sum plus $\sum_{i<j}T_i$ plus a partial block sum of norm at most $4\cdot2^{-j}$. As $n \to \infty$, $j \to \infty$, so the partial sums converge. Both coordinates converge, which is the claim.

(The lemma is the planar case of a theorem of Bárány and Grinberg; the same proof works in $\mathbb{R}^d$ with bound $2d$.)
:::
