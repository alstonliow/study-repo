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

::: {#fig-absolute-convergence-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (4.6,0) node[lab, right] {$n$};
\draw[->, faint] (0,-1.2) -- (0,1.9) node[lab, above] {};
\fill[tintA] (0.28,0) rectangle (0.52,1.600); \draw[faint] (0.28,0) rectangle (0.52,1.600);
\fill[tintB] (0.68,0) rectangle (0.92,-0.800); \draw[faint] (0.68,0) rectangle (0.92,-0.800);
\fill[tintA] (1.08,0) rectangle (1.32,0.533); \draw[faint] (1.08,0) rectangle (1.32,0.533);
\fill[tintB] (1.48,0) rectangle (1.72,-0.400); \draw[faint] (1.48,0) rectangle (1.72,-0.400);
\fill[tintA] (1.88,0) rectangle (2.12,0.320); \draw[faint] (1.88,0) rectangle (2.12,0.320);
\fill[tintB] (2.28,0) rectangle (2.52,-0.267); \draw[faint] (2.28,0) rectangle (2.52,-0.267);
\fill[tintA] (2.68,0) rectangle (2.92,0.229); \draw[faint] (2.68,0) rectangle (2.92,0.229);
\fill[tintB] (3.08,0) rectangle (3.32,-0.200); \draw[faint] (3.08,0) rectangle (3.32,-0.200);
\fill[tintA] (3.48,0) rectangle (3.72,0.178); \draw[faint] (3.48,0) rectangle (3.72,0.178);
\fill[tintB] (3.88,0) rectangle (4.12,-0.160); \draw[faint] (3.88,0) rectangle (4.12,-0.160);
\node[lab, right] at (4.3,0.4) {$a_n^+$}; \node[lab, right] at (4.3,-0.4) {$a_n^-$};
\end{tikzpicture}
\end{center}
```

Split the terms into positive parts (above) and negative parts (below). If $\sum\lvert a_n\rvert$ converges, both $\sum a_n^+$ and $\sum a_n^-$ do, and $\sum a_n$ is their difference.

:::

::: {#exm-alternating-harmonic .example name="The alternating harmonic series"}

$1-\frac12+\frac13-\frac14+\cdots$ converges, but not absolutely.

1. Pairing terms, $\frac1{2n-1}-\frac1{2n}=\frac1{2n(2n-1)}\le\frac1{n^2}$, so the even partial sums $S_{2n}$ increase and are bounded; they converge to some $s$.

2. $S_{2n+1}=S_{2n}+\frac1{2n+1}\to s$ as well, so $S_N\to s$.

3. The series of absolute values is the harmonic series, which diverges. (The sum is $s=\ln 2$.)

:::

::: {#fig-absolute-convergence-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (6.6,0) node[lab, right] {$N$};
\draw[->, faint] (0,-0.2) -- (0,2.4) node[lab, above] {$S_N$};
\draw[faint] (0.260,2.000) -- (0.520,1.000) -- (0.780,1.667) -- (1.040,1.167) -- (1.300,1.567) -- (1.560,1.233) -- (1.820,1.519) -- (2.080,1.269) -- (2.340,1.491) -- (2.600,1.291) -- (2.860,1.473) -- (3.120,1.306) -- (3.380,1.460) -- (3.640,1.317) -- (3.900,1.451) -- (4.160,1.326) -- (4.420,1.443) -- (4.680,1.332) -- (4.940,1.438) -- (5.200,1.338) -- (5.460,1.433) -- (5.720,1.342) -- (5.980,1.429) -- (6.240,1.345);
\node[dot] at (0.260,2.000) {};
\node[dot] at (0.520,1.000) {};
\node[dot] at (0.780,1.667) {};
\node[dot] at (1.040,1.167) {};
\node[dot] at (1.300,1.567) {};
\node[dot] at (1.560,1.233) {};
\node[dot] at (1.820,1.519) {};
\node[dot] at (2.080,1.269) {};
\node[dot] at (2.340,1.491) {};
\node[dot] at (2.600,1.291) {};
\node[dot] at (2.860,1.473) {};
\node[dot] at (3.120,1.306) {};
\node[dot] at (3.380,1.460) {};
\node[dot] at (3.640,1.317) {};
\node[dot] at (3.900,1.451) {};
\node[dot] at (4.160,1.326) {};
\node[dot] at (4.420,1.443) {};
\node[dot] at (4.680,1.332) {};
\node[dot] at (4.940,1.438) {};
\node[dot] at (5.200,1.338) {};
\node[dot] at (5.460,1.433) {};
\node[dot] at (5.720,1.342) {};
\node[dot] at (5.980,1.429) {};
\node[dot] at (6.240,1.345) {};
\draw[hl, dashed] (0,1.386) -- (6.4,1.386) node[lab, right] {$\ln2$};
\end{tikzpicture}
\end{center}
```

Partial sums of $1-\frac12+\frac13-\cdots$ jump above and below $\ln2$ with shrinking steps, so they converge, although $\sum\frac1n$ diverges.

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

::: {#fig-absolute-convergence-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (6.6,0) node[lab, right] {$N$};
\draw[->, faint] (0,-0.2) -- (0,3.6) node[lab, above] {};
\draw[faint] (0.155,2.000) -- (0.310,2.667) -- (0.465,3.067) -- (0.620,2.067) -- (0.775,2.352) -- (0.930,2.575) -- (1.085,2.756) -- (1.240,2.910) -- (1.395,3.044) -- (1.550,2.544) -- (1.705,2.661) -- (1.860,2.767) -- (2.015,2.862) -- (2.170,2.949) -- (2.325,3.029) -- (2.480,2.695) -- (2.635,2.769) -- (2.790,2.838) -- (2.945,2.903) -- (3.100,2.964) -- (3.255,3.021) -- (3.410,2.771) -- (3.565,2.825) -- (3.720,2.876) -- (3.875,2.925) -- (4.030,2.971) -- (4.185,3.016) -- (4.340,2.816) -- (4.495,2.858) -- (4.650,2.899) -- (4.805,2.938) -- (4.960,2.976) -- (5.115,3.012) -- (5.270,2.846) -- (5.425,2.881) -- (5.580,2.915) -- (5.735,2.948) -- (5.890,2.979) -- (6.045,3.010) -- (6.200,2.867);
\draw[emph] (0.155,2.000) -- (0.310,1.000) -- (0.465,1.667) -- (0.620,1.167) -- (0.775,1.567) -- (0.930,1.233) -- (1.085,1.519) -- (1.240,1.269) -- (1.395,1.491) -- (1.550,1.291) -- (1.705,1.473) -- (1.860,1.306) -- (2.015,1.460) -- (2.170,1.317) -- (2.325,1.451) -- (2.480,1.326) -- (2.635,1.443) -- (2.790,1.332) -- (2.945,1.438) -- (3.100,1.338) -- (3.255,1.433) -- (3.410,1.342) -- (3.565,1.429) -- (3.720,1.345);
\draw[hl, dashed] (0,3) -- (6.4,3) node[lab, right] {$1.5$};
\draw[faint, dashed] (0,1.386) -- (6.4,1.386) node[lab, right] {$\ln2$};
\end{tikzpicture}
\end{center}
```

The same terms $\pm\frac1n$ in two orders: the usual order (dark) tends to $\ln2$; taking positive terms until the sum passes $1.5$, then negative terms until it drops below, and so on (light) tends to $1.5$. A conditionally convergent series is not unconditionally convergent.

:::

::: {#rmk-absolute-convergence-1 .remark name="Riemann's rearrangement theorem"}

Step 5 can be refined: by adding positive terms until the partial sum first exceeds a target $x$, then negative terms until it first drops below $x$, and so on, a conditionally convergent real series can be rearranged to converge to *any* real number $x$, since its terms tend to $0$. For the alternating harmonic series, the order $1+\frac13-\frac12+\frac15+\frac17-\frac14+\cdots$ (two positive terms, then one negative) sums to $\frac32\ln2$ instead of $\ln2$.

:::
