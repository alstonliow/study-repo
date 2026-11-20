---
title: "Absolute and Unconditional Convergence"
sources: [cama1-3]
requires: [math/analysis/real/series/series-and-comparison, math/analysis/real/sequences/cauchy-sequences]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Section 3.2, in our own wording; proofs written out in steps. -->

Finite sums can be added in any order. Infinite sums can too, but only when they converge absolutely; otherwise reordering the terms can change the sum or destroy convergence.

::: {#def-absolute-convergence .definition name="Absolute convergence"}

$\sum a_n$ *converges absolutely* if $\sum|a_n|$ converges. A series that converges but not absolutely *converges conditionally*.

:::

::: {#thm-absolute-implies-convergence .theorem name="Absolute convergence implies convergence"}

If $\sum|a_n|$ converges, then $\sum a_n$ converges, and
$$\Bigl|\sum_{n=1}^\infty a_n\Bigr|\le\sum_{n=1}^\infty|a_n|.$$

:::

::: {.proof}

1. Let $S_N=\sum_{n\le N}a_n$ and $T_N=\sum_{n\le N}|a_n|$. The partial sums $S_N$ need not be monotone, so we show they are Cauchy (@thm-general-principle-of-convergence).

2. For $p>q$, the triangle inequality gives
$$|S_p-S_q|=\Bigl|\sum_{n=q+1}^p a_n\Bigr|\le\sum_{n=q+1}^p|a_n|=T_p-T_q.$$

3. $(T_N)$ converges, so it is Cauchy: given $\varepsilon>0$ there is $N$ with $T_p-T_q<\varepsilon$ for $p>q\ge N$. Then $|S_p-S_q|<\varepsilon$ too, so $(S_N)$ is Cauchy and converges.

4. $|S_N|\le T_N\le\sum|a_n|$ for all $N$; let $N\to\infty$ (@lem-limit-preserves-inequality).

:::

::: {#exm-alternating-harmonic .example name="The alternating harmonic series"}

$1-\frac12+\frac13-\frac14+\cdots$ converges, but not absolutely.

1. Pairing terms, $\frac1{2n-1}-\frac1{2n}=\frac1{2n(2n-1)}\le\frac1{n^2}$, so the even partial sums $S_{2n}$ increase and are bounded; they converge to some $s$.

2. $S_{2n+1}=S_{2n}+\frac1{2n+1}\to s$ as well, so $S_N\to s$.

3. The series of absolute values is the harmonic series, which diverges. (The sum is $s=\ln 2$.)

:::

## Rearrangements

::: {#def-unconditional-convergence .definition name="Rearrangement, unconditional convergence"}

A *rearrangement* of $\sum a_n$ is a series $\sum a_{\pi(n)}$ with $\pi:\mathbb N\to\mathbb N$ a bijection. The series *converges unconditionally* if every rearrangement converges.

:::

::: {#thm-absolute-iff-unconditional .theorem name="Absolute is unconditional"}

A real series converges absolutely if and only if it converges unconditionally. In that case every rearrangement has the same sum:
$$\sum_{n=1}^\infty a_{\pi(n)}=\sum_{n=1}^\infty a_n\quad\text{for every bijection }\pi.$$

:::

::: {.proof}

1. *Absolute $\Rightarrow$ every rearrangement converges.* Let $\varepsilon>0$ and choose $M$ with $\sum_{n>M}|a_n|<\varepsilon$. Choose $N$ so large that $\{1,\dots,M\}\subseteq\{\pi(1),\dots,\pi(N)\}$. Then $\pi(n)>M$ for every $n>N$, so for $p>q\ge N$,
$$\Bigl|\sum_{n=q+1}^p a_{\pi(n)}\Bigr|\le\sum_{n=q+1}^p|a_{\pi(n)}|\le\sum_{m>M}|a_m|<\varepsilon,$$
since the indices $\pi(q+1),\dots,\pi(p)$ are distinct and all exceed $M$. The partial sums are Cauchy, so they converge.

2. *Same sum.* Keep $\varepsilon$, $M$ and $N$ from step 1, and enlarge $N$ so that also $\pi(1),\dots,\pi(M)\le N$. For $K\ge N$, both $\sum_{n\le K}a_n$ and $\sum_{n\le K}a_{\pi(n)}$ contain $a_1,\dots,a_M$, so in their difference these cancel, and every remaining term has index greater than $M$ and appears at most once in each sum. Hence
$$\Bigl|\sum_{n\le K}a_n-\sum_{n\le K}a_{\pi(n)}\Bigr|\le2\sum_{m>M}|a_m|<2\varepsilon.$$
Letting $K\to\infty$, the two sums differ by at most $2\varepsilon$, for every $\varepsilon>0$.

3. *Not absolute $\Rightarrow$ some rearrangement diverges.* Suppose $\sum|a_n|=\infty$. If only finitely many terms are negative, $\sum a_n$ itself differs from $\sum|a_n|$ in finitely many terms and diverges. Likewise if only finitely many are positive. Otherwise list the non-negative terms as $b_1,b_2,\dots$ and the negative ones as $c_1,c_2,\dots$, each in their original order.

4. $\sum b_n$ and $\sum c_n$ cannot both converge, or $\sum|a_n|$ would; say $\sum b_n=\infty$ (the other case is symmetric).

5. Choose $0=n_0<n_1<n_2<\cdots$ so that $b_{n_{k-1}+1}+\cdots+b_{n_k}+c_k\ge1$ for each $k$; this is possible because the tails of $\sum b_n$ are unbounded.

6. The rearrangement $b_1,\dots,b_{n_1},c_1,\ b_{n_1+1},\dots,b_{n_2},c_2,\dots$ uses every term exactly once, and its partial sum after $c_k$ is at least $k$. So it diverges.

:::

::: {#rmk-absolute-convergence-1 .remark name="Riemann's rearrangement theorem"}

Step 5 can be refined: by adding positive terms until the partial sum first exceeds a target $x$, then negative terms until it first drops below $x$, and so on, a conditionally convergent real series can be rearranged to converge to *any* real number $x$, since its terms tend to $0$. For the alternating harmonic series, the order $1+\frac13-\frac12+\frac15+\frac17-\frac14+\cdots$ (two positive terms, then one negative) sums to $\frac32\ln2$ instead of $\ln2$.

:::
