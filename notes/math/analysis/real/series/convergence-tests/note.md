---
title: "Convergence Tests and Complex Series"
sources: [cama1-3]
requires: [math/analysis/real/series/absolute-convergence]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Sections 3.3 and 3.4, in our own wording; proofs written out in steps. The condensation test is in @sec-math-analysis-real-series-series-and-comparison. -->

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

For example $1-\frac1{\sqrt[3]2}+\frac1{\sqrt[3]3}-\cdots$ converges, though $\sum n^{-1/3}=\infty$.

## The ratio test

::: {#thm-ratio-test-general .theorem name="Ratio test (general form)" related="thm-ratio-test"}

Let $a_n\ne0$ for all $n$ (real or complex).

1. If there are $c<1$ and $N$ with $\dfrac{|a_{n+1}|}{|a_n|}\le c$ for all $n\ge N$, then $\sum a_n$ converges absolutely.
2. In particular, if $\dfrac{|a_{n+1}|}{|a_n|}\to\rho<1$, then $\sum a_n$ converges absolutely.

:::

::: {.proof}

1. By induction, $|a_{N+k}|\le c^k|a_N|$ for all $k\ge0$.

2. $\sum_k c^k|a_N|$ is a convergent geometric series (@thm-convergence-condition), so $\sum|a_n|$ converges by @thm-comparison-test, and $\sum a_n$ converges by @thm-absolute-implies-convergence.

3. If the ratios tend to $\rho<1$, take $\varepsilon=\frac{1-\rho}2$: eventually the ratios are at most $\frac{1+\rho}2<1$, and part 1 applies with $c=\frac{1+\rho}2$.

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
