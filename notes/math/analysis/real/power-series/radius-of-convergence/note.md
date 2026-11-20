---
title: "Complex Power Series and the Radius of Convergence"
sources: [cama1-6]
requires: [math/analysis/real/series/convergence-tests, math/analysis/real/sequences/limsup-and-liminf, math/calculus/single-variable/series/taylor-series]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Section 6 (introduction), in our own wording; proofs written out in steps. @def-power-series asserts that a radius of convergence exists; this note proves it, for complex power series. -->

A *complex power series* is $\sum_{n=0}^\infty a_nz^n$ with $a_n,z\in\mathbb C$; where it converges it defines a function of $z$. Its set of convergence is always a disc, up to the boundary circle, by the following lemma.

::: {#lem-power-series-smaller-modulus .lemma name="Convergence spreads inwards"}

If $\sum a_nz^n$ converges and $|w|<|z|$, then $\sum a_nw^n$ converges absolutely.

:::

::: {.proof}

1. The terms of a convergent series tend to $0$ (@thm-nth-term-test), so they are bounded: $|a_nz^n|\le C$ for all $n$.

2. Then $|a_nw^n|=|a_nz^n|\left|\frac wz\right|^n\le C\left|\frac wz\right|^n$.

3. Since $|w/z|<1$, the right side is a convergent geometric series, and @thm-comparison-test gives absolute convergence.

:::

Equivalently, if $\sum a_nz^n$ diverges and $|w|>|z|$, then $\sum a_nw^n$ diverges.

::: {#def-radius-of-convergence .definition name="Radius of convergence" related="def-power-series"}

The *radius of convergence* of $\sum a_nz^n$ is
$$R=\sup\Bigl\{|z|:\sum a_nz^n\text{ converges}\Bigr\}\in[0,\infty],$$
with $R=\infty$ if the set is unbounded. The open disc $\{z:|z|<R\}$ is the *disc of convergence*.

:::

::: {#thm-radius-of-convergence .theorem name="Convergence inside, divergence outside"}

If $|z|<R$, then $\sum a_nz^n$ converges absolutely; if $|z|>R$, it diverges.

:::

::: {.proof}

1. If $|z|<R$, then $|z|$ is not an upper bound of the set in @def-radius-of-convergence, so there is $z_0$ with $|z_0|>|z|$ at which the series converges. By @lem-power-series-smaller-modulus it converges absolutely at $z$.

2. If $|z|>R$ and the series converged at $z$, then $|z|$ would belong to the set whose supremum is $R$, so $|z|\le R$, a contradiction.

:::

On the circle $|z|=R$ anything can happen:

::: {#exm-radius-of-convergence-1 .example name="Three series with radius $1$"}

1. $\sum z^n$ diverges at every point with $|z|=1$, since its terms do not tend to $0$.

2. $\sum z^n/n$ diverges at $z=1$ and converges at every other point of the circle (@exm-convergence-tests-2).

3. $\sum z^n/n^2$ converges at every point of the circle, absolutely, since $\sum1/n^2<\infty$ (@exm-series-and-comparison-2); for $|z|>1$ its terms are unbounded.

:::

The ratio test (@thm-ratio-test-general) often gives $R$: if $|a_{n+1}/a_n|\to L$, then $R=1/L$ (with $1/0=\infty$). A formula that always works uses the root instead of the ratio. For an unbounded sequence, put $\limsup=\infty$ (@def-limsup-liminf), and read $1/0=\infty$, $1/\infty=0$.

::: {#thm-cauchy-hadamard .theorem name="Cauchy–Hadamard formula"}

The radius of convergence of $\sum a_nz^n$ is
$$R=\frac{1}{\limsup_{n\to\infty}\sqrt[n]{|a_n|}}.$$

:::

::: {.proof}

1. Write $L=\limsup\sqrt[n]{|a_n|}$. We show convergence when $|z|L<1$ and divergence when $|z|L>1$; by @thm-radius-of-convergence this pins down $R=1/L$.

2. *$|z|L<1$.* Choose $q$ with $|z|L<q<1$. Since $\sup_{m\ge n}|z|\sqrt[m]{|a_m|}$ decreases to $|z|L$, there is $N$ with $|z|\sqrt[n]{|a_n|}\le q$ for all $n\ge N$, i.e. $|a_nz^n|\le q^n$. Comparison with the geometric series gives absolute convergence.

3. *$|z|L>1$.* For every $n$, $\sup_{m\ge n}|z|\sqrt[m]{|a_m|}>1$, so $|z|\sqrt[m]{|a_m|}>1$ for infinitely many $m$. For those $m$, $|a_mz^m|>1$, so the terms do not tend to $0$ and the series diverges.

:::

::: {#exm-radius-of-convergence-2 .example}

For $\sum z^n/2^n$, $\sqrt[n]{|a_n|}=\frac12$ for every $n$, so $R=2$. For $\sum n^2z^n$ the ratio test is quicker: $\frac{(n+1)^2}{n^2}\to1$, so $R=1$.

:::
