---
title: "Differentiating Power Series"
sources: [cama1-6]
requires: [math/analysis/real/power-series/radius-of-convergence, math/analysis/real/differentiability/differentiability-and-inverses]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Section 6.2, in our own wording; proofs written out in steps. -->

A polynomial is differentiated term by term. Inside its disc of convergence a power series can be too, but this needs proof: the sum rule covers finite sums only. The proof below bounds the error directly; with uniform convergence (in a later course) it becomes shorter.

::: {#lem-power-difference .lemma name="An algebraic identity"}

For $a,b\in\mathbb C$ and $n\ge2$,
$$b^n-a^n-n(b-a)a^{n-1}=(b-a)^2\sum_{k=1}^{n-1}k\,a^{k-1}b^{n-1-k}.$$

:::

::: {.proof}

1. $b^n-a^n=(b-a)\sum_{j=0}^{n-1}a^jb^{n-1-j}$, so the left side is $(b-a)\sum_{j=0}^{n-1}a^j\bigl(b^{n-1-j}-a^{n-1-j}\bigr)$.

2. Apply the same factorisation to each bracket: $b^{m}-a^{m}=(b-a)\sum_{i=0}^{m-1}a^ib^{m-1-i}$ with $m=n-1-j$.

3. The left side becomes $(b-a)^2\sum_{j}\sum_{i}a^{i+j}b^{n-2-i-j}$. For fixed $k-1=i+j$ (from $0$ to $n-2$) there are $k$ pairs $(i,j)$, which gives the right side.

:::

With $a=z$, $b=z+h$ this reads
$$(z+h)^n-z^n-nhz^{n-1}=h^2\sum_{k=1}^{n-1}k\,z^{k-1}(z+h)^{n-1-k}.\tag{1}$$

::: {#lem-derived-series-converges .lemma name="The derived series has the same disc"}

If $\sum a_nz^n$ has radius of convergence $R$ and $|z|<R$, then $\sum na_nz^{n-1}$ and $\sum\binom n2a_nz^{n-2}$ converge absolutely.

:::

::: {.proof}

1. Choose $r$ with $|z|<r<R$. Then $\sum|a_n|r^n$ converges (@thm-radius-of-convergence), so $|a_n|r^n\le C$ for all $n$.

2. Hence $n|a_nz^{n-1}|\le\frac Cr\,n\left(\frac{|z|}r\right)^{n-1}$, and $\sum n\rho^{n-1}$ converges for $0\le\rho<1$ by the ratio test (@exm-convergence-tests-1). Comparison gives the first claim.

3. Apply step 2 to the series $\sum na_nz^{n-1}$ itself, whose radius is at least $R$ by step 2: $\sum n(n-1)a_nz^{n-2}$ converges absolutely; divide by $2$.

:::

::: {#fig-differentiating-power-series-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (7.2,0) node[lab, right] {$n$};
\draw[->, faint] (0,-0.2) -- (0,2.6) node[lab, above] {};
\fill[shade] (0.230,0) rectangle (0.430,0.900);
\fill[shade] (0.560,0) rectangle (0.760,1.440);
\fill[shade] (0.890,0) rectangle (1.090,1.728);
\fill[shade] (1.220,0) rectangle (1.420,1.843);
\fill[shade] (1.550,0) rectangle (1.750,1.843);
\fill[shade] (1.880,0) rectangle (2.080,1.769);
\fill[shade] (2.210,0) rectangle (2.410,1.652);
\fill[shade] (2.540,0) rectangle (2.740,1.510);
\fill[shade] (2.870,0) rectangle (3.070,1.359);
\fill[shade] (3.200,0) rectangle (3.400,1.208);
\fill[shade] (3.530,0) rectangle (3.730,1.063);
\fill[shade] (3.860,0) rectangle (4.060,0.928);
\fill[shade] (4.190,0) rectangle (4.390,0.804);
\fill[shade] (4.520,0) rectangle (4.720,0.693);
\fill[shade] (4.850,0) rectangle (5.050,0.594);
\fill[shade] (5.180,0) rectangle (5.380,0.507);
\fill[shade] (5.510,0) rectangle (5.710,0.431);
\fill[shade] (5.840,0) rectangle (6.040,0.365);
\fill[shade] (6.170,0) rectangle (6.370,0.308);
\fill[shade] (6.500,0) rectangle (6.700,0.259);
\draw[hl] (0.330,2.000) -- (0.408,1.951) -- (0.487,1.902) -- (0.565,1.855) -- (0.643,1.810) -- (0.722,1.765) -- (0.800,1.721) -- (0.879,1.679) -- (0.957,1.637) -- (1.035,1.597) -- (1.114,1.557) -- (1.192,1.519) -- (1.271,1.481) -- (1.349,1.445) -- (1.427,1.409) -- (1.506,1.374) -- (1.584,1.340) -- (1.662,1.307) -- (1.741,1.275) -- (1.819,1.243) -- (1.898,1.213) -- (1.976,1.183) -- (2.054,1.153) -- (2.133,1.125) -- (2.211,1.097) -- (2.289,1.070) -- (2.368,1.043) -- (2.446,1.018) -- (2.525,0.993) -- (2.603,0.968) -- (2.681,0.944) -- (2.760,0.921) -- (2.838,0.898) -- (2.916,0.876) -- (2.995,0.854) -- (3.073,0.833) -- (3.152,0.812) -- (3.230,0.792) -- (3.308,0.773) -- (3.387,0.754) -- (3.465,0.735) -- (3.543,0.717) -- (3.622,0.699) -- (3.700,0.682) -- (3.778,0.665) -- (3.857,0.649) -- (3.935,0.633) -- (4.014,0.617) -- (4.092,0.602) -- (4.170,0.587) -- (4.249,0.572) -- (4.327,0.558) -- (4.405,0.544) -- (4.484,0.531) -- (4.562,0.518) -- (4.641,0.505) -- (4.719,0.493) -- (4.797,0.480) -- (4.876,0.469) -- (4.954,0.457) -- (5.033,0.446) -- (5.111,0.435) -- (5.189,0.424) -- (5.268,0.413) -- (5.346,0.403) -- (5.424,0.393) -- (5.503,0.384) -- (5.581,0.374) -- (5.659,0.365) -- (5.738,0.356) -- (5.816,0.347) -- (5.895,0.338) -- (5.973,0.330) -- (6.051,0.322) -- (6.130,0.314) -- (6.208,0.306) -- (6.287,0.299) -- (6.365,0.291) -- (6.443,0.284) -- (6.522,0.277) -- (6.600,0.270);\node[lab, right] at (6.7,0.4) {$r^{n-1}$, $r=0.9$}; \node[lab] at (2.5,2.3) {$n\lvert z\rvert^{n-1}$, $\lvert z\rvert=0.8$};
\end{tikzpicture}
\end{center}
```

Why the derived series has the same radius: the factor $n$ grows, but $n\lvert z\rvert^{n-1}$ (bars) is eventually below $r^{n-1}$ for any $r$ with $\lvert z\rvert<r$ (orange), so comparison with a geometric series applies.

:::

::: {#thm-power-series-differentiable .theorem name="Term-by-term differentiation"}

Let $\sum a_nz^n$ have radius of convergence $R$. On $|z|<R$ the function $f(z)=\sum_{n\ge0}a_nz^n$ is differentiable, and
$$f'(z)=\sum_{n=1}^\infty na_nz^{n-1}.$$

:::

::: {.proof}

1. Let $g(z)$ be the right side, which converges by @lem-derived-series-converges. By @prp-derivative-little-o we must show $f(z+h)-f(z)-hg(z)=o(h)$.

2. For $|z+h|<R$, the three series converge, and the terms with $n=0,1$ cancel, so by (1)
$$f(z+h)-f(z)-hg(z)=\sum_{n\ge2}a_n\bigl((z+h)^n-z^n-nhz^{n-1}\bigr)=h^2\sum_{n\ge2}a_n\sum_{k=1}^{n-1}k\,z^{k-1}(z+h)^{n-1-k}.$$

3. Fix $r$ with $|z|<r<R$ and take $h$ so small that $|z+h|\le r$. Each inner sum then has modulus at most $\sum_{k=1}^{n-1}k\,r^{n-2}=\binom n2r^{n-2}$.

4. So the modulus of the outer sum is at most $M=\sum_{n\ge2}|a_n|\binom n2r^{n-2}$, which is finite by @lem-derived-series-converges (applied at $r<R$) and does not depend on $h$.

5. Hence $|f(z+h)-f(z)-hg(z)|\le M|h|^2$, which is $o(h)$.

:::

::: {#fig-differentiating-power-series-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-1.8,0) -- (2.0,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.2) -- (0,3.2) node[lab, above] {$y$};
\draw[emph] (-1.520,0.462) -- (-1.488,0.466) -- (-1.456,0.471) -- (-1.424,0.476) -- (-1.392,0.481) -- (-1.360,0.486) -- (-1.328,0.492) -- (-1.296,0.497) -- (-1.264,0.503) -- (-1.232,0.508) -- (-1.200,0.514) -- (-1.168,0.520) -- (-1.136,0.526) -- (-1.104,0.533) -- (-1.072,0.539) -- (-1.040,0.545) -- (-1.008,0.552) -- (-0.976,0.559) -- (-0.944,0.566) -- (-0.912,0.573) -- (-0.880,0.581) -- (-0.848,0.588) -- (-0.816,0.596) -- (-0.784,0.604) -- (-0.752,0.612) -- (-0.720,0.621) -- (-0.688,0.629) -- (-0.656,0.638) -- (-0.624,0.647) -- (-0.592,0.657) -- (-0.560,0.667) -- (-0.528,0.677) -- (-0.496,0.687) -- (-0.464,0.698) -- (-0.432,0.709) -- (-0.400,0.720) -- (-0.368,0.732) -- (-0.336,0.744) -- (-0.304,0.756) -- (-0.272,0.769) -- (-0.240,0.783) -- (-0.208,0.796) -- (-0.176,0.811) -- (-0.144,0.826) -- (-0.112,0.841) -- (-0.080,0.857) -- (-0.048,0.874) -- (-0.016,0.891) -- (0.016,0.909) -- (0.048,0.928) -- (0.080,0.947) -- (0.112,0.968) -- (0.144,0.989) -- (0.176,1.011) -- (0.208,1.034) -- (0.240,1.059) -- (0.272,1.084) -- (0.304,1.111) -- (0.336,1.139) -- (0.368,1.169) -- (0.400,1.200) -- (0.432,1.233) -- (0.464,1.268) -- (0.496,1.304) -- (0.528,1.343) -- (0.560,1.385) -- (0.592,1.429) -- (0.624,1.475) -- (0.656,1.525) -- (0.688,1.579) -- (0.720,1.636) -- (0.752,1.698) -- (0.784,1.765) -- (0.816,1.837) -- (0.848,1.915) -- (0.880,2.000) -- (0.912,2.093) -- (0.944,2.195) -- (0.976,2.308) -- (1.008,2.432) -- (1.040,2.571);
\draw[hl] (-1.520,0.237) -- (-1.498,0.240) -- (-1.476,0.244) -- (-1.454,0.247) -- (-1.432,0.251) -- (-1.410,0.254) -- (-1.388,0.258) -- (-1.366,0.262) -- (-1.344,0.266) -- (-1.322,0.270) -- (-1.300,0.274) -- (-1.278,0.278) -- (-1.256,0.282) -- (-1.234,0.287) -- (-1.212,0.291) -- (-1.190,0.296) -- (-1.168,0.301) -- (-1.146,0.306) -- (-1.124,0.311) -- (-1.102,0.316) -- (-1.080,0.321) -- (-1.058,0.326) -- (-1.036,0.332) -- (-1.014,0.337) -- (-0.992,0.343) -- (-0.970,0.349) -- (-0.948,0.355) -- (-0.926,0.361) -- (-0.904,0.367) -- (-0.882,0.374) -- (-0.860,0.381) -- (-0.838,0.388) -- (-0.816,0.395) -- (-0.794,0.402) -- (-0.772,0.409) -- (-0.750,0.417) -- (-0.728,0.425) -- (-0.706,0.433) -- (-0.684,0.442) -- (-0.662,0.450) -- (-0.640,0.459) -- (-0.618,0.468) -- (-0.596,0.478) -- (-0.574,0.487) -- (-0.552,0.498) -- (-0.530,0.508) -- (-0.508,0.518) -- (-0.486,0.529) -- (-0.464,0.541) -- (-0.442,0.553) -- (-0.420,0.565) -- (-0.398,0.577) -- (-0.376,0.590) -- (-0.354,0.603) -- (-0.332,0.617) -- (-0.310,0.632) -- (-0.288,0.646) -- (-0.266,0.662) -- (-0.244,0.678) -- (-0.222,0.694) -- (-0.200,0.711) -- (-0.178,0.729) -- (-0.156,0.747) -- (-0.134,0.766) -- (-0.112,0.786) -- (-0.090,0.807) -- (-0.068,0.828) -- (-0.046,0.850) -- (-0.024,0.874) -- (-0.002,0.898) -- (0.020,0.923) -- (0.042,0.949) -- (0.064,0.977) -- (0.086,1.005) -- (0.108,1.035) -- (0.130,1.066) -- (0.152,1.099) -- (0.174,1.133) -- (0.196,1.169) -- (0.218,1.206) -- (0.240,1.246) -- (0.262,1.287) -- (0.284,1.330) -- (0.306,1.376) -- (0.328,1.424) -- (0.350,1.475) -- (0.372,1.528) -- (0.394,1.584) -- (0.416,1.644) -- (0.438,1.706) -- (0.460,1.773) -- (0.482,1.843) -- (0.504,1.918) -- (0.526,1.997) -- (0.548,2.082) -- (0.570,2.172) -- (0.592,2.268) -- (0.614,2.370) -- (0.636,2.479) -- (0.658,2.596) -- (0.680,2.722) -- (0.702,2.857) -- (0.724,3.002);
\draw[faint, dashed] (1.6,-0.1) -- (1.6,3.1); \node[lab, below] at (1.6,-0.1) {$1$};
\node[lab, left] at (0.9,2.6) {$\sum nx^{n-1}=\frac1{(1-x)^2}$}; \node[lab, right] at (1.05,2.0) {$\sum x^n$};
\end{tikzpicture}
\end{center}
```

Term by term: $\sum x^n=\frac1{1-x}$ (dark) differentiates to $\sum nx^{n-1}=\frac1{(1-x)^2}$ (orange), valid on the same interval $\lvert x\rvert<1$.

:::

::: {#fig-differentiating-power-series-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0,0) circle (1.6); \draw[faint, dashed] (0,0) circle (1.6); \draw[hl] (0,0) circle (1.1);
\draw[->, faint] (-2.0,0) -- (2.2,0); \draw[->, faint] (0,-1.9) -- (0,1.9);
\node[dot] at (0.55,0.45) {}; \node[lab, above] at (0.55,0.45) {$z$};
\node[lab] at (1.2,-1.35) {$R$}; \node[lab] at (0.62,-0.62) {$r$};
\end{tikzpicture}
\end{center}
```

For $\lvert z\rvert<R$ choose $r$ with $\lvert z\rvert<r<R$. On the disc of radius $r$ (orange) the derived series converges too, so the series can be differentiated term by term at $z$, with the same radius $R$.

:::

Applying the theorem repeatedly, a power series is infinitely differentiable inside its disc of convergence, and $a_n=f^{(n)}(0)/n!$; this justifies @thm-taylor-coefficients.
