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

::: {#fig-series-and-comparison-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0.000,0) rectangle (3.000,0.5); \draw[faint] (0.000,0) rectangle (3.000,0.5);\node[lab, tick] at (1.500,0.25) {$\frac1{2}$};
\fill[tintB] (3.000,0) rectangle (4.000,0.5); \draw[faint] (3.000,0) rectangle (4.000,0.5);\node[lab, tick] at (3.500,0.25) {$\frac1{6}$};
\fill[tintA] (4.000,0) rectangle (4.500,0.5); \draw[faint] (4.000,0) rectangle (4.500,0.5);\node[lab, tick] at (4.250,0.25) {$\frac1{12}$};
\fill[tintB] (4.500,0) rectangle (4.800,0.5); \draw[faint] (4.500,0) rectangle (4.800,0.5);
\fill[tintA] (4.800,0) rectangle (5.000,0.5); \draw[faint] (4.800,0) rectangle (5.000,0.5);
\fill[tintB] (5.000,0) rectangle (5.143,0.5); \draw[faint] (5.000,0) rectangle (5.143,0.5);
\fill[tintA] (5.143,0) rectangle (5.250,0.5); \draw[faint] (5.143,0) rectangle (5.250,0.5);
\draw[emph] (0,0) rectangle (6,0.5); \node[lab, below] at (0,-0.05) {$0$}; \node[lab, below] at (6,-0.05) {$1$};
\end{tikzpicture}
\end{center}
```

$\frac1{n(n+1)}=\frac1n-\frac1{n+1}$: the pieces $\frac12,\frac16,\frac1{12},\dots$ fill $[0,1]$ from the left, and after $N$ pieces exactly $\frac1{N+1}$ is left.

:::

::: {#thm-comparison-test .theorem name="Comparison test" related="thm-limit-comparison-series"}

Let $a_n,b_n\ge0$, and suppose there are $C>0$ and $N$ with $a_n\le Cb_n$ for all $n\ge N$. If $\sum b_n$ converges, so does $\sum a_n$; equivalently, if $\sum a_n$ diverges, so does $\sum b_n$.

:::

::: {.proof}

1. Let $S_M=\sum_{n=1}^M a_n$. For $M>N$,
$$S_M=S_N+\sum_{n=N+1}^M a_n\le S_N+C\sum_{n=N+1}^M b_n\le S_N+C\sum_{n=1}^\infty b_n.$$

2. The right side does not depend on $M$, so the partial sums of $\sum a_n$ are bounded above, and the series converges by @prp-nonnegative-series-bounded.

:::

::: {#fig-series-and-comparison-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (6.3,0) node[lab, right] {$n$};
\draw[->, faint] (0,-0.2) -- (0,2.6) node[lab, above] {};
\draw[cell frame] (0.35,0) rectangle (0.75,2.400); \fill[shade] (0.35,0) rectangle (0.75,1.600);
\draw[cell frame] (0.90,0) rectangle (1.30,1.200); \fill[shade] (0.90,0) rectangle (1.30,0.650);
\draw[cell frame] (1.45,0) rectangle (1.85,0.800); \fill[shade] (1.45,0) rectangle (1.85,0.384);
\draw[cell frame] (2.00,0) rectangle (2.40,0.600); \fill[shade] (2.00,0) rectangle (2.40,0.264);
\draw[cell frame] (2.55,0) rectangle (2.95,0.480); \fill[shade] (2.55,0) rectangle (2.95,0.197);
\draw[cell frame] (3.10,0) rectangle (3.50,0.400); \fill[shade] (3.10,0) rectangle (3.50,0.156);
\draw[cell frame] (3.65,0) rectangle (4.05,0.343); \fill[shade] (3.65,0) rectangle (4.05,0.127);
\draw[cell frame] (4.20,0) rectangle (4.60,0.300); \fill[shade] (4.20,0) rectangle (4.60,0.107);
\draw[cell frame] (4.75,0) rectangle (5.15,0.267); \fill[shade] (4.75,0) rectangle (5.15,0.092);
\draw[cell frame] (5.30,0) rectangle (5.70,0.240); \fill[shade] (5.30,0) rectangle (5.70,0.080);
\node[lab, right] at (0.85,2.3) {$b_n$}; \node[lab, right] at (0.75,1.0) {$a_n$};
\end{tikzpicture}
\end{center}
```

Comparison: if $0\le a_n\le b_n$, the shaded bars fit inside the outlined ones, so the partial sums of $\sum a_n$ are bounded by $\sum b_n$ whenever that converges.

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

::: {#fig-series-and-comparison-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0.00,0) rectangle (0.36,2.400); \draw[faint] (0.00,0) rectangle (0.36,2.400);
\draw[hl] (0.00,2.400) -- (0.36,2.400);
\fill[tintB] (0.36,0) rectangle (0.72,1.200); \draw[faint] (0.36,0) rectangle (0.72,1.200);
\draw[hl] (0.36,1.200) -- (0.72,1.200);
\fill[tintB] (0.72,0) rectangle (1.08,0.800); \draw[faint] (0.72,0) rectangle (1.08,0.800);
\draw[hl] (0.72,1.200) -- (1.08,1.200);
\fill[tintA] (1.08,0) rectangle (1.44,0.600); \draw[faint] (1.08,0) rectangle (1.44,0.600);
\draw[hl] (1.08,0.600) -- (1.44,0.600);
\fill[tintA] (1.44,0) rectangle (1.80,0.480); \draw[faint] (1.44,0) rectangle (1.80,0.480);
\draw[hl] (1.44,0.600) -- (1.80,0.600);
\fill[tintA] (1.80,0) rectangle (2.16,0.400); \draw[faint] (1.80,0) rectangle (2.16,0.400);
\draw[hl] (1.80,0.600) -- (2.16,0.600);
\fill[tintA] (2.16,0) rectangle (2.52,0.343); \draw[faint] (2.16,0) rectangle (2.52,0.343);
\draw[hl] (2.16,0.600) -- (2.52,0.600);
\node[lab, tick, below] at (1.80,0) {block $k=2$};
\fill[tintB] (2.52,0) rectangle (2.88,0.300); \draw[faint] (2.52,0) rectangle (2.88,0.300);
\draw[hl] (2.52,0.300) -- (2.88,0.300);
\fill[tintB] (2.88,0) rectangle (3.24,0.267); \draw[faint] (2.88,0) rectangle (3.24,0.267);
\draw[hl] (2.88,0.300) -- (3.24,0.300);
\fill[tintB] (3.24,0) rectangle (3.60,0.240); \draw[faint] (3.24,0) rectangle (3.60,0.240);
\draw[hl] (3.24,0.300) -- (3.60,0.300);
\fill[tintB] (3.60,0) rectangle (3.96,0.218); \draw[faint] (3.60,0) rectangle (3.96,0.218);
\draw[hl] (3.60,0.300) -- (3.96,0.300);
\fill[tintB] (3.96,0) rectangle (4.32,0.200); \draw[faint] (3.96,0) rectangle (4.32,0.200);
\draw[hl] (3.96,0.300) -- (4.32,0.300);
\fill[tintB] (4.32,0) rectangle (4.68,0.185); \draw[faint] (4.32,0) rectangle (4.68,0.185);
\draw[hl] (4.32,0.300) -- (4.68,0.300);
\fill[tintB] (4.68,0) rectangle (5.04,0.171); \draw[faint] (4.68,0) rectangle (5.04,0.171);
\draw[hl] (4.68,0.300) -- (5.04,0.300);
\fill[tintB] (5.04,0) rectangle (5.40,0.160); \draw[faint] (5.04,0) rectangle (5.40,0.160);
\draw[hl] (5.04,0.300) -- (5.40,0.300);
\node[lab, tick, below] at (3.96,0) {block $k=3$};\draw[faint] (0,0) -- (5.6,0);
\end{tikzpicture}
\end{center}
```

Cauchy condensation for decreasing $a_n$ (bars, here $a_n=1/n$): the $2^k$ terms of block $k$ lie between $2^ka_{2^{k+1}}$ and $2^ka_{2^k}$ (orange level), so $\sum a_n$ and $\sum2^ka_{2^k}$ converge together.

:::

::: {#exm-series-and-comparison-3 .example name="The $p$-series again" related="cor-p-series"}

For $a_n=1/n^p$ with $p>0$, the condensed series is $\sum_k2^k\cdot2^{-kp}=\sum_k(2^{1-p})^k$, a geometric series with ratio $2^{1-p}$. It converges if and only if $2^{1-p}<1$, i.e. $p>1$. For $p=1$ every condensed term is $1$, which recovers the divergence of the harmonic series.

:::
