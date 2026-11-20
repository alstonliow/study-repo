---
title: "Series of Non-negative Terms and Comparison"
sources: [cama1-3]
requires: [math/analysis/real/sequences/monotone-sequences, math/calculus/single-variable/limits/sums-and-series]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Sections 3.1 and 3.3 (condensation test), in our own wording; proofs written out in steps. The definition of a series, the geometric series and the divergence of the harmonic series are in @sec-math-calculus-single-variable-limits-sums-and-series; the divergence test is @thm-nth-term-test. -->

A series $\sum a_n$ converges when its partial sums $S_N=\sum_{n=1}^N a_n$ converge (@def-series-partial-sum). For series with non-negative terms the partial sums increase, so by @thm-monotone-convergence the only question is whether they stay bounded. This note collects the tests that answer it by comparison.

::: {#prp-nonnegative-series-bounded .proposition name="Non-negative series"}

If $a_n\ge0$ for all $n$, then $\sum a_n$ converges if and only if its partial sums are bounded above.

:::

::: {.proof}

1. Since $S_{N+1}-S_N=a_{N+1}\ge0$, the partial sums increase.

2. An increasing sequence converges exactly when it is bounded above: if bounded, by @thm-monotone-convergence; if convergent, by @lem-convergent-bounded.

:::

So for non-negative terms we may write $\sum a_n<\infty$ for "converges" and $\sum a_n=\infty$ for "diverges".

::: {#exm-series-and-comparison-1 .example name="A telescoping series"}

Since $\frac1{n(n-1)}=\frac1{n-1}-\frac1n$, the partial sums telescope:
$$\sum_{n=2}^N\frac1{n(n-1)}=1-\frac1N\to1,\qquad\text{so}\qquad\sum_{n=2}^\infty\frac1{n(n-1)}=1.$$

:::

::: {#thm-comparison-test .theorem name="Comparison test" related="thm-limit-comparison-series"}

Let $a_n,b_n\ge0$, and suppose there are $C>0$ and $N$ with $a_n\le Cb_n$ for all $n\ge N$. If $\sum b_n$ converges, so does $\sum a_n$; equivalently, if $\sum a_n$ diverges, so does $\sum b_n$.

:::

::: {.proof}

1. Let $S_M=\sum_{n=1}^M a_n$. For $M>N$,
$$S_M=S_N+\sum_{n=N+1}^M a_n\le S_N+C\sum_{n=N+1}^M b_n\le S_N+C\sum_{n=1}^\infty b_n.$$

2. The right side does not depend on $M$, so the partial sums of $\sum a_n$ are bounded above, and the series converges by @prp-nonnegative-series-bounded.

:::

The limit comparison test @thm-limit-comparison-series is a special case: if $a_n/b_n\to L$ then eventually $a_n\le(L+1)b_n$.

::: {#exm-series-and-comparison-2 .example name="Comparisons"}

1. $\sum\frac1{n^2}<\infty$: for $n\ge2$, $\frac1{n^2}\le\frac1{n(n-1)}$, and the latter series converges (@exm-series-and-comparison-1).

2. $\sum\frac1{\sqrt n}=\infty$: $\frac1{\sqrt n}\ge\frac1n$ and the harmonic series diverges (@thm-the-harmonic-series-diverges).

3. $\sum\frac n{2^n}<\infty$: for $n\ge4$ we have $n\le2^{n/2}$ (true at $n=4$, and going from $n$ to $n+1$ multiplies the left side by $\frac{n+1}n\le\frac54<\sqrt2$). So $\frac n{2^n}\le 2^{-n/2}=(1/\sqrt2)^n$, a convergent geometric series.

4. $\sum_{n\ge1}\frac{n+5}{n^3-7n^2/2}$ converges: for $n\ge8$, $n^3-\frac72n^2=n^2(n-\frac72)\ge\frac{n^3}2$ and $n+5\le2n$, so each term is at most $\frac{4}{n^2}$. The finitely many terms with $n<8$ do not affect convergence.

:::

## Grouping in dyadic blocks

Grouping terms into blocks of lengths $1,2,4,8,\dots$ settles the $p$-series (@cor-p-series) without integrals.

::: {#thm-cauchy-condensation .theorem name="Cauchy condensation test"}

If $(a_n)$ is decreasing and non-negative, then
$$\sum_{n=1}^\infty a_n<\infty \iff \sum_{k=0}^\infty 2^ka_{2^k}<\infty.$$

:::

::: {.proof}

1. *Lower bound.* The block $a_{2^{k-1}+1}+\cdots+a_{2^k}$ has $2^{k-1}$ terms, each at least $a_{2^k}$. So
$$\sum_{n=1}^{2^K}a_n\ge a_1+\sum_{k=1}^K2^{k-1}a_{2^k}=a_1+\tfrac12\sum_{k=1}^K2^ka_{2^k}.$$
If the condensed series diverges, the partial sums of $\sum a_n$ are unbounded.

2. *Upper bound.* The block $a_{2^k}+\cdots+a_{2^{k+1}-1}$ has $2^k$ terms, each at most $a_{2^k}$. So
$$\sum_{n=1}^{2^{K+1}-1}a_n\le\sum_{k=0}^K2^ka_{2^k}.$$
If the condensed series converges, the partial sums of $\sum a_n$ are bounded (every $S_N$ is at most some $S_{2^{K+1}-1}$), so $\sum a_n$ converges by @prp-nonnegative-series-bounded.

:::

::: {#exm-series-and-comparison-3 .example name="The $p$-series again" related="cor-p-series"}

For $a_n=1/n^p$ with $p>0$, the condensed series is $\sum_k2^k\cdot2^{-kp}=\sum_k(2^{1-p})^k$, a geometric series with ratio $2^{1-p}$. It converges if and only if $2^{1-p}<1$, i.e. $p>1$. For $p=1$ every condensed term is $1$, which recovers the divergence of the harmonic series.

:::
