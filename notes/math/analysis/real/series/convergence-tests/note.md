---
title: "Convergence Tests and Complex Series"
sources: [cama1-3, mit1801-36]
requires: [math/analysis/real/series/absolute-convergence]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Sections 3.3 and 3.4, in our own wording; proofs written out in steps. The condensation test is in @sec-math-analysis-real-series-series-and-comparison. Merged 2026-11-20 (owner): the 18.01 ratio test (former id thm-ratio-test, MIT 18.01 Lecture 36) was removed; @thm-ratio-test-general is the single version, and its divergence part 3 with proof comes from 18.01. -->

## Alternating series

::: {#thm-alternating-series-test .theorem name="Alternating series test"}

If $(a_n)$ is decreasing, non-negative and $a_n\to0$, then
$$\sum_{n=1}^\infty(-1)^{n+1}a_n=a_1-a_2+a_3-a_4+\cdots$$
converges, and its sum lies between $0$ and $a_1$.

:::

::: {.proof}

1. Let $S_N$ be the partial sums. Grouping in pairs, $S_{2n}=(a_1-a_2)+\cdots+(a_{2n-1}-a_{2n})$ is a sum of non-negative brackets, so $(S_{2n})$ is increasing and $S_{2n}\ge0$.

2. Grouping the other way, $S_{2n+1}=a_1-(a_2-a_3)-\cdots-(a_{2n}-a_{2n+1})$, so $(S_{2n+1})$ is decreasing and $S_{2n+1}\le a_1$.

3. Since $S_{2n+1}-S_{2n}=a_{2n+1}\ge0$, we get $0\le S_{2n}\le S_{2n+1}\le a_1$. Both subsequences are monotone and bounded, so they converge (@thm-monotone-convergence).

4. Their difference $a_{2n+1}$ tends to $0$, so the limits agree, and then $S_N$ converges to the common limit, which lies in $[0,a_1]$.

:::

::: {#fig-convergence-tests-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-0.2,0) -- (6.4,0);
\draw[->, emph] (6.000,0.25) -- (3.000,0.25);
\draw[->, hl] (3.000,0.47) -- (5.000,0.47);
\draw[->, emph] (5.000,0.69) -- (3.500,0.69);
\draw[->, hl] (3.500,0.91) -- (4.700,0.91);
\draw[->, emph] (4.700,1.13) -- (3.700,1.13);
\draw[->, hl] (3.700,1.35) -- (4.557,1.35);
\draw[->, emph] (4.557,1.57) -- (3.807,1.57);
\draw[faint] (0.000,-0.06) -- (0.000,0.06); \node[lab, tick, below] at (0.000,-0.05) {$0$};\draw[faint] (6.000,-0.06) -- (6.000,0.06); \node[lab, tick, below] at (6.000,-0.05) {$1$};\draw[faint] (4.159,-0.06) -- (4.159,0.06); \node[lab, tick, below] at (4.159,-0.05) {$s$};
\node[lab, right] at (6.2,1.0) {$S_1,S_2,\dots$};
\end{tikzpicture}
\end{center}
```

Alternating series test: each step goes the other way and is shorter than the last, so $S_2\le S_4\le\dots\le s\le\dots\le S_3\le S_1$ (here $\sum(-1)^{n+1}/n$).

:::

For example $1-\frac1{\sqrt[3]2}+\frac1{\sqrt[3]3}-\cdots$ converges, though $\sum n^{-1/3}=\infty$.

## The ratio test

::: {#thm-ratio-test-general .theorem name="Ratio test (general form)"}

Let $a_n\ne0$ for all $n$ (real or complex).

1. If there are $c<1$ and $N$ with $\dfrac{|a_{n+1}|}{|a_n|}\le c$ for all $n\ge N$, then $\sum a_n$ converges absolutely.
2. In particular, if $\dfrac{|a_{n+1}|}{|a_n|}\to\rho<1$, then $\sum a_n$ converges absolutely.
3. If $\dfrac{|a_{n+1}|}{|a_n|}\to\rho>1$, then $\sum a_n$ diverges.

:::

::: {.proof}

1. By induction, $|a_{N+k}|\le c^k|a_N|$ for all $k\ge0$.

2. $\sum_k c^k|a_N|$ is a convergent geometric series (@thm-convergence-condition), so $\sum|a_n|$ converges by @thm-comparison-test, and $\sum a_n$ converges by @thm-absolute-implies-convergence.

3. If the ratios tend to $\rho<1$, take $\varepsilon=\frac{1-\rho}2$: eventually the ratios are at most $\frac{1+\rho}2<1$, and part 1 applies with $c=\frac{1+\rho}2$.

4. If the ratios tend to $\rho>1$, then eventually $|a_{n+1}|>|a_n|$, so $|a_n|$ is eventually increasing and positive, hence $a_n\not\to0$ and the series diverges (@thm-nth-term-test).

:::

::: {#fig-convergence-tests-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (6.6,0) node[lab, right] {$n$};
\draw[->, faint] (0,-0.2) -- (0,2.4) node[lab, above] {};
\node[dot] at (0.350,1.782) {};
\node[dot] at (0.700,0.758) {};
\node[dot] at (1.050,0.628) {};
\node[dot] at (1.400,0.623) {};
\node[dot] at (1.750,0.281) {};
\node[dot] at (2.100,0.197) {};
\node[dot] at (2.450,0.214) {};
\node[dot] at (2.800,0.105) {};
\node[dot] at (3.150,0.063) {};
\node[dot] at (3.500,0.072) {};
\node[dot] at (3.850,0.039) {};
\node[dot] at (4.200,0.020) {};
\node[dot] at (4.550,0.024) {};
\node[dot] at (4.900,0.015) {};
\node[dot] at (5.250,0.007) {};
\node[dot] at (5.600,0.008) {};
\node[dot] at (5.950,0.005) {};
\draw[hl] (0.350,1.820) -- (0.420,1.695) -- (0.490,1.578) -- (0.560,1.469) -- (0.630,1.368) -- (0.700,1.274) -- (0.770,1.186) -- (0.840,1.105) -- (0.910,1.029) -- (0.980,0.958) -- (1.050,0.892) -- (1.120,0.830) -- (1.190,0.773) -- (1.260,0.720) -- (1.330,0.670) -- (1.400,0.624) -- (1.470,0.581) -- (1.540,0.541) -- (1.610,0.504) -- (1.680,0.469) -- (1.750,0.437) -- (1.820,0.407) -- (1.890,0.379) -- (1.960,0.353) -- (2.030,0.329) -- (2.100,0.306) -- (2.170,0.285) -- (2.240,0.265) -- (2.310,0.247) -- (2.380,0.230) -- (2.450,0.214) -- (2.520,0.199) -- (2.590,0.186) -- (2.660,0.173) -- (2.730,0.161) -- (2.800,0.150) -- (2.870,0.140) -- (2.940,0.130) -- (3.010,0.121) -- (3.080,0.113) -- (3.150,0.105) -- (3.220,0.098) -- (3.290,0.091) -- (3.360,0.085) -- (3.430,0.079) -- (3.500,0.073) -- (3.570,0.068) -- (3.640,0.064) -- (3.710,0.059) -- (3.780,0.055) -- (3.850,0.051) -- (3.920,0.048) -- (3.990,0.045) -- (4.060,0.042) -- (4.130,0.039) -- (4.200,0.036) -- (4.270,0.034) -- (4.340,0.031) -- (4.410,0.029) -- (4.480,0.027) -- (4.550,0.025) -- (4.620,0.023) -- (4.690,0.022) -- (4.760,0.020) -- (4.830,0.019) -- (4.900,0.018) -- (4.970,0.016) -- (5.040,0.015) -- (5.110,0.014) -- (5.180,0.013) -- (5.250,0.012) -- (5.320,0.011) -- (5.390,0.011) -- (5.460,0.010) -- (5.530,0.009) -- (5.600,0.009) -- (5.670,0.008) -- (5.740,0.007) -- (5.810,0.007) -- (5.880,0.006) -- (5.950,0.006);\node[lab, above right] at (0.4,1.85) {$Cr^n$};
\end{tikzpicture}
\end{center}
```

If $\lvert a_{n+1}/a_n\rvert\le r<1$ from some point on, the terms stay below a geometric sequence $Cr^n$ (orange), and $\sum a_n$ converges by comparison.

:::

::: {#rmk-convergence-tests-1 .remark name="A fixed bound is needed"}

It is not enough that every ratio is less than $1$. For $a_n=1/n$, $\frac{a_{n+1}}{a_n}=\frac n{n+1}<1$ for all $n$, but the ratios tend to $1$ and the series diverges. When the ratio tends to $1$, the test says nothing: $\sum1/n$ diverges and $\sum1/n^2$ converges, and both have ratio tending to $1$.

:::

::: {#exm-convergence-tests-1 .example}

If $|b|<1$, then $\sum nb^n$ converges: $\dfrac{(n+1)|b|^{n+1}}{n|b|^n}=\left(1+\frac1n\right)|b|\to|b|<1$. (Its sum is $\frac{b}{(1-b)^2}$, for instance $2$ when $b=\frac12$.)

:::

## Complex series

Convergence, Cauchy sequences, series and absolute convergence are defined for complex numbers exactly as for real ones, with $|\cdot|$ the modulus. What does not carry over is anything using the order: $\mathbb C$ is not an ordered field, since in an ordered field $i^2=-1$ would have to be non-negative (@lem-square-nonnegative). So suprema and monotone sequences are unavailable, but the results proved from them still hold, by applying the real versions to real and imaginary parts:

- If $z_n=x_n+iy_n$, then $z_n\to z$ if and only if $x_n\to\operatorname{Re}z$ and $y_n\to\operatorname{Im}z$, because $|x_n-x|,|y_n-y|\le|z_n-z|\le|x_n-x|+|y_n-y|$.
- So a Cauchy sequence in $\mathbb C$ converges: its real and imaginary parts are Cauchy, hence convergent.
- Bolzano–Weierstrass holds in $\mathbb C$: take a subsequence whose real parts converge, then a further subsequence whose imaginary parts converge.
- Absolute convergence implies convergence, with the same proof; hence the ratio test above holds for complex series.

The complex case also has a test with no real analogue among those above.

::: {#thm-abel-test .theorem name="Abel's test"}

Let $a_1\ge a_2\ge\cdots\ge0$ with $a_n\to0$, and let $z\in\mathbb C$ with $|z|=1$, $z\ne1$. Then $\sum a_nz^n$ converges.

:::

::: {.proof}

1. We show the partial sums are Cauchy. Write $z^n=\dfrac{z^{n+1}-z^n}{z-1}$, so for $M\le N$
$$\sum_{n=M}^Na_nz^n=\frac1{z-1}\sum_{n=M}^Na_n(z^{n+1}-z^n).$$

2. *Summation by parts.* Shift the index in the second half of the sum:
$$\sum_{n=M}^Na_n(z^{n+1}-z^n)=a_Nz^{N+1}-a_Mz^M+\sum_{n=M}^{N-1}(a_n-a_{n+1})z^{n+1}.$$

3. Take moduli, using $|z|=1$ and $a_n-a_{n+1}\ge0$:
$$\Bigl|\sum_{n=M}^Na_nz^n\Bigr|\le\frac{1}{|z-1|}\Bigl(a_N+a_M+\sum_{n=M}^{N-1}(a_n-a_{n+1})\Bigr)=\frac{2a_M}{|z-1|}.$$

4. Since $a_M\to0$, the right side is less than any $\varepsilon>0$ for all large $M$, whatever $N\ge M$ is. So the partial sums are Cauchy and converge.

:::

Step 2 is a discrete analogue of integration by parts: differences move from $z^n$ onto the coefficients $a_n$.

::: {#exm-convergence-tests-2 .example name="Where $\sum z^n/n$ converges"}

$\sum_{n\ge1}z^n/n$ converges if $|z|<1$, and also if $|z|=1$ with $z\ne1$; it diverges if $z=1$ or $|z|>1$.

1. If $|z|<1$, the ratio of moduli is $\frac{n}{n+1}|z|\to|z|<1$, so the ratio test applies.

2. If $|z|>1$, the terms do not tend to $0$, since $|z|^n/n\to\infty$ (@exm-exponential-beats-polynomial with $k=1$, inverted).

3. If $z=1$, this is the harmonic series. If $|z|=1$, $z\ne1$, Abel's test applies with $a_n=1/n$. For $z=-1$ it is minus the alternating harmonic series (@exm-alternating-harmonic).

:::

::: {#fig-convergence-tests-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0,0) circle (1.5);
\draw[hl] (0,0) circle (1.5);
\draw[->, faint] (-2.1,0) -- (2.3,0) node[lab, right] {$\operatorname{Re}z$};
\draw[->, faint] (0,-1.9) -- (0,1.9) node[lab, above] {$\operatorname{Im}z$};
\node[hollow dot] at (1.5,0) {}; \node[lab, right] at (1.55,-0.35) {$z=1$: diverges};
\node[lab] at (-0.6,0.5) {$\lvert z\rvert<1$};
\node[lab] at (-1.6,1.5) {$\lvert z\rvert=1$, $z\ne1$}; \node[lab] at (1.9,-1.5) {diverges};
\end{tikzpicture}
\end{center}
```

Where $\sum z^n/n$ converges: the open unit disc (ratio test) and every point of the unit circle except $z=1$ (Abel's test).

:::
