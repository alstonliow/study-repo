---
title: "Infinite Series and Convergence Tests"
sources: [mit1801-36]
requires: [math/calculus/series/improper-integrals]
relations:
  related: [math/discrete/sequences/approximating-sums]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lecture 36, in our own wording; proofs written out in steps. Series, partial sums, geometric series and the divergence of the harmonic series are in the note on sums and series; the stacking-blocks example is @exm-book-overhang. -->

A series $\sum_{n=1}^\infty a_n$ converges if its partial sums $S_N=\sum_{n=1}^Na_n$ have a limit (@def-series-partial-sum). The geometric series $\sum r^n$ converges exactly when $\lvert r\rvert<1$, and the harmonic series $\sum\frac1n$ diverges (@thm-the-harmonic-series-diverges).

::: {#thm-nth-term-test .theorem name="Divergence test"}

If $\sum a_n$ converges, then $a_n\to0$. So if $a_n\not\to0$, the series diverges.

:::

::: {.proof}

1. $a_n=S_n-S_{n-1}$, and both partial sums tend to the same limit $S$, so $a_n\to S-S=0$.

:::

The converse fails: $\frac1n\to0$ but $\sum\frac1n$ diverges.

::: {#thm-integral-test .theorem name="Integral test"}

If $f$ is positive and decreasing on $[1,\infty)$ and $a_n=f(n)$, then $\sum_{n=1}^\infty a_n$ and $\int_1^\infty f(x)\,dx$ both converge or both diverge.

:::

::: {.proof}

1. Since $f$ decreases, $a_{n+1}\le\int_n^{n+1}f\le a_n$ (compare with rectangles, as in @thm-integral-bounds).

2. Summing, $S_N-a_1\le\int_1^Nf\le S_{N-1}$.

3. The partial sums and the integrals $\int_1^Nf$ are both non-decreasing, and each is bounded if and only if the other is. A non-decreasing sequence converges exactly when it is bounded.

:::

::: {#cor-p-series .corollary name="$p$-series"}

$\displaystyle\sum_{n=1}^\infty\frac1{n^p}$ converges if and only if $p>1$.

:::

::: {.proof}

1. For $p\le0$ the terms do not tend to $0$ (@thm-nth-term-test). For $p>0$, apply @thm-integral-test with $f(x)=x^{-p}$ and @thm-p-integrals.

:::

::: {#thm-limit-comparison-series .theorem name="Limit comparison"}

If $a_n,b_n>0$ and $a_n/b_n\to L$ with $0<L<\infty$, then $\sum a_n$ and $\sum b_n$ both converge or both diverge.

:::

::: {.proof}

1. For $n$ large, $\frac L2b_n\le a_n\le2Lb_n$, so the partial sums of one series are bounded exactly when those of the other are (as in @thm-comparison-integrals).

:::

::: {#exm-series-tests .example name="Testing series"}

- $\sum\frac{1}{n^2+1}$ converges (compare with $\frac1{n^2}$).
- $\sum\frac1{\sqrt{n^2+1}}$ diverges (compare with $\frac1n$).
- $\sum\frac1{n\ln n}$ ($n\ge2$) diverges: $\int_2^N\frac{dx}{x\ln x}=\ln\ln N-\ln\ln2\to\infty$.

:::

::: {#thm-ratio-test .theorem name="Ratio test"}

If $a_n>0$ and $a_{n+1}/a_n\to L$, then $\sum a_n$ converges if $L<1$ and diverges if $L>1$ (no conclusion if $L=1$).

:::

::: {.proof}

1. If $L<1$, pick $r$ with $L<r<1$. For $n\ge N$, $a_{n+1}\le ra_n$, so $a_{N+k}\le a_Nr^k$ and the tail is bounded by a convergent geometric series.

2. If $L>1$, eventually $a_{n+1}>a_n$, so $a_n\not\to0$.

:::

For example $\sum\frac{n^2}{2^n}$ converges, since the ratio tends to $\frac12$.
