---
title: "The Exponential and Trigonometric Functions"
sources: [cama1-6]
requires: [math/analysis/real/power-series/differentiating-power-series]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Sections 6.1–6.3, in our own wording; proofs written out in steps. Earlier notes use $e^x$, $\sin$ and $\cos$ with their familiar properties; here they are defined by power series and those properties are proved, including the definition of $\pi$. -->

## Products of series

::: {#thm-cauchy-product .theorem name="Cauchy product"}

Let $\sum_{n\ge0}a_n$ and $\sum_{n\ge0}b_n$ converge absolutely, and let $c_n=\sum_{k=0}^na_kb_{n-k}$. Then $\sum c_n$ converges absolutely and
$$\sum_{n=0}^\infty c_n=\Bigl(\sum_{n=0}^\infty a_n\Bigr)\Bigl(\sum_{n=0}^\infty b_n\Bigr).$$

:::

::: {.proof}

1. Let $S,T$ be the two sums and $U=\sum|a_n|$, $V=\sum|b_n|$. Consider the series $(*)$ whose terms are all the products $a_jb_k$, listed in "square shells": first $a_0b_0$, then the products with $\max(j,k)=1$, then those with $\max(j,k)=2$, and so on.

2. The first $(N+1)^2$ terms of $(*)$ are exactly the products with $j,k\le N$. So their moduli add up to $\bigl(\sum_{n\le N}|a_n|\bigr)\bigl(\sum_{n\le N}|b_n|\bigr)\le UV$. Every partial sum of the moduli is below such a square partial sum, so $(*)$ converges absolutely.

3. The same partial sums of $(*)$ itself are $\bigl(\sum_{n\le N}a_n\bigr)\bigl(\sum_{n\le N}b_n\bigr)\to ST$. A convergent series has the limit of any subsequence of its partial sums, so $(*)$ sums to $ST$.

4. Listing the same products in "diagonals" $j+k=0,1,2,\dots$ is a rearrangement of $(*)$, so by @thm-absolute-iff-unconditional it converges absolutely to $ST$ as well. Its partial sum through the diagonal $j+k=N$ is $c_0+\cdots+c_N$; hence $\sum c_n=ST$, and $\sum|c_n|$ converges because $|c_n|\le\sum_{j+k=n}|a_jb_k|$.

:::

Applied to $a_nz^n$ and $b_nz^n$: inside both discs of convergence, $\bigl(\sum a_nz^n\bigr)\bigl(\sum b_nz^n\bigr)=\sum c_nz^n$, as when multiplying polynomials.

## The exponential function

::: {#def-exponential-series .definition name="Exponential function" related="def-number-e"}

For $z\in\mathbb C$,
$$e^z=\exp(z)=\sum_{n=0}^\infty\frac{z^n}{n!}.$$

:::

::: {#fig-exponential-and-trigonometric-functions-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-2.4,0) -- (2.2,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.4) -- (0,3.0) node[lab, above] {$y$};
\draw[hl] (-2.200,0.100) -- (-2.159,0.104) -- (-2.118,0.108) -- (-2.076,0.113) -- (-2.035,0.118) -- (-1.994,0.123) -- (-1.953,0.128) -- (-1.911,0.133) -- (-1.870,0.139) -- (-1.829,0.145) -- (-1.788,0.151) -- (-1.746,0.157) -- (-1.705,0.164) -- (-1.664,0.170) -- (-1.623,0.178) -- (-1.581,0.185) -- (-1.540,0.193) -- (-1.499,0.201) -- (-1.458,0.210) -- (-1.416,0.218) -- (-1.375,0.228) -- (-1.334,0.237) -- (-1.292,0.247) -- (-1.251,0.258) -- (-1.210,0.268) -- (-1.169,0.280) -- (-1.127,0.291) -- (-1.086,0.304) -- (-1.045,0.317) -- (-1.004,0.330) -- (-0.962,0.344) -- (-0.921,0.358) -- (-0.880,0.373) -- (-0.839,0.389) -- (-0.798,0.405) -- (-0.756,0.422) -- (-0.715,0.440) -- (-0.674,0.459) -- (-0.633,0.478) -- (-0.591,0.498) -- (-0.550,0.519) -- (-0.509,0.541) -- (-0.467,0.564) -- (-0.426,0.588) -- (-0.385,0.612) -- (-0.344,0.638) -- (-0.302,0.665) -- (-0.261,0.693) -- (-0.220,0.722) -- (-0.179,0.753) -- (-0.138,0.784) -- (-0.096,0.817) -- (-0.055,0.852) -- (-0.014,0.888) -- (0.027,0.925) -- (0.069,0.964) -- (0.110,1.005) -- (0.151,1.047) -- (0.192,1.091) -- (0.234,1.137) -- (0.275,1.185) -- (0.316,1.235) -- (0.357,1.287) -- (0.399,1.341) -- (0.440,1.397) -- (0.481,1.456) -- (0.522,1.518) -- (0.564,1.582) -- (0.605,1.648) -- (0.646,1.718) -- (0.688,1.790) -- (0.729,1.865) -- (0.770,1.944) -- (0.811,2.026) -- (0.853,2.111) -- (0.894,2.200) -- (0.935,2.292) -- (0.976,2.389) -- (1.018,2.490) -- (1.059,2.594) -- (1.100,2.704);
\draw[faint] (-1.499,-0.449) -- (-1.458,-0.412) -- (-1.416,-0.375) -- (-1.375,-0.338) -- (-1.334,-0.300) -- (-1.292,-0.263) -- (-1.251,-0.226) -- (-1.210,-0.189) -- (-1.169,-0.152) -- (-1.127,-0.115) -- (-1.086,-0.078) -- (-1.045,-0.041) -- (-1.004,-0.003) -- (-0.962,0.034) -- (-0.921,0.071) -- (-0.880,0.108) -- (-0.839,0.145) -- (-0.798,0.182) -- (-0.756,0.219) -- (-0.715,0.256) -- (-0.674,0.294) -- (-0.633,0.331) -- (-0.591,0.368) -- (-0.550,0.405) -- (-0.509,0.442) -- (-0.467,0.479) -- (-0.426,0.516) -- (-0.385,0.553) -- (-0.344,0.591) -- (-0.302,0.628) -- (-0.261,0.665) -- (-0.220,0.702) -- (-0.179,0.739) -- (-0.138,0.776) -- (-0.096,0.813) -- (-0.055,0.851) -- (-0.014,0.888) -- (0.027,0.925) -- (0.069,0.962) -- (0.110,0.999) -- (0.151,1.036) -- (0.192,1.073) -- (0.234,1.110) -- (0.275,1.148) -- (0.316,1.185) -- (0.357,1.222) -- (0.399,1.259) -- (0.440,1.296) -- (0.481,1.333) -- (0.522,1.370) -- (0.564,1.407) -- (0.605,1.445) -- (0.646,1.482) -- (0.688,1.519) -- (0.729,1.556) -- (0.770,1.593) -- (0.811,1.630) -- (0.853,1.667) -- (0.894,1.704) -- (0.935,1.742) -- (0.976,1.779) -- (1.018,1.816) -- (1.059,1.853) -- (1.100,1.890);
\draw[faint] (-2.200,1.098) -- (-2.159,1.054) -- (-2.118,1.012) -- (-2.076,0.971) -- (-2.035,0.932) -- (-1.994,0.894) -- (-1.953,0.858) -- (-1.911,0.824) -- (-1.870,0.791) -- (-1.829,0.759) -- (-1.788,0.729) -- (-1.746,0.701) -- (-1.705,0.674) -- (-1.664,0.648) -- (-1.623,0.624) -- (-1.581,0.602) -- (-1.540,0.581) -- (-1.499,0.562) -- (-1.458,0.544) -- (-1.416,0.528) -- (-1.375,0.513) -- (-1.334,0.500) -- (-1.292,0.489) -- (-1.251,0.478) -- (-1.210,0.470) -- (-1.169,0.463) -- (-1.127,0.457) -- (-1.086,0.453) -- (-1.045,0.451) -- (-1.004,0.450) -- (-0.962,0.451) -- (-0.921,0.453) -- (-0.880,0.456) -- (-0.839,0.462) -- (-0.798,0.468) -- (-0.756,0.477) -- (-0.715,0.487) -- (-0.674,0.498) -- (-0.633,0.511) -- (-0.591,0.525) -- (-0.550,0.541) -- (-0.509,0.559) -- (-0.467,0.578) -- (-0.426,0.598) -- (-0.385,0.620) -- (-0.344,0.644) -- (-0.302,0.669) -- (-0.261,0.696) -- (-0.220,0.724) -- (-0.179,0.754) -- (-0.138,0.785) -- (-0.096,0.818) -- (-0.055,0.852) -- (-0.014,0.888) -- (0.027,0.925) -- (0.069,0.964) -- (0.110,1.004) -- (0.151,1.046) -- (0.192,1.090) -- (0.234,1.135) -- (0.275,1.182) -- (0.316,1.230) -- (0.357,1.279) -- (0.399,1.330) -- (0.440,1.383) -- (0.481,1.437) -- (0.522,1.493) -- (0.564,1.550) -- (0.605,1.609) -- (0.646,1.670) -- (0.688,1.731) -- (0.729,1.795) -- (0.770,1.860) -- (0.811,1.926) -- (0.853,1.994) -- (0.894,2.064) -- (0.935,2.135) -- (0.976,2.208) -- (1.018,2.282) -- (1.059,2.357) -- (1.100,2.434);
\draw[faint] (-2.118,-0.412) -- (-2.076,-0.371) -- (-2.035,-0.332) -- (-1.994,-0.294) -- (-1.953,-0.258) -- (-1.911,-0.224) -- (-1.870,-0.190) -- (-1.829,-0.158) -- (-1.788,-0.128) -- (-1.746,-0.098) -- (-1.705,-0.070) -- (-1.664,-0.043) -- (-1.623,-0.016) -- (-1.581,0.009) -- (-1.540,0.033) -- (-1.499,0.057) -- (-1.458,0.080) -- (-1.416,0.102) -- (-1.375,0.123) -- (-1.334,0.144) -- (-1.292,0.165) -- (-1.251,0.185) -- (-1.210,0.204) -- (-1.169,0.223) -- (-1.127,0.242) -- (-1.086,0.261) -- (-1.045,0.280) -- (-1.004,0.298) -- (-0.962,0.317) -- (-0.921,0.336) -- (-0.880,0.354) -- (-0.839,0.373) -- (-0.798,0.392) -- (-0.756,0.412) -- (-0.715,0.432) -- (-0.674,0.452) -- (-0.633,0.473) -- (-0.591,0.494) -- (-0.550,0.516) -- (-0.509,0.539) -- (-0.467,0.562) -- (-0.426,0.587) -- (-0.385,0.612) -- (-0.344,0.638) -- (-0.302,0.665) -- (-0.261,0.693) -- (-0.220,0.722) -- (-0.179,0.753) -- (-0.138,0.784) -- (-0.096,0.817) -- (-0.055,0.852) -- (-0.014,0.888) -- (0.027,0.925) -- (0.069,0.964) -- (0.110,1.005) -- (0.151,1.047) -- (0.192,1.091) -- (0.234,1.137) -- (0.275,1.185) -- (0.316,1.234) -- (0.357,1.286) -- (0.399,1.340) -- (0.440,1.396) -- (0.481,1.454) -- (0.522,1.514) -- (0.564,1.577) -- (0.605,1.642) -- (0.646,1.710) -- (0.688,1.780) -- (0.729,1.853) -- (0.770,1.928) -- (0.811,2.006) -- (0.853,2.087) -- (0.894,2.171) -- (0.935,2.258) -- (0.976,2.347) -- (1.018,2.440) -- (1.059,2.535) -- (1.100,2.634);
\node[lab, right] at (1.1,2.7) {$e^x$};
\end{tikzpicture}
\end{center}
```

$\exp$ (orange) with the partial sums $1+x$, $1+x+\frac{x^2}2$, \dots, $\sum_{k\le3}\frac{x^k}{k!}$ (grey); the series converges for every $x$.

:::

The ratio of consecutive terms is $\frac{|z|}{n+1}\to0$, so the series converges absolutely for every $z$ (radius $\infty$).

::: {#thm-exponential-properties .theorem name="Properties of the exponential"}

For all $z,w\in\mathbb C$:

1. $e^{z+w}=e^ze^w$; in particular $e^z\ne0$ and $e^{-z}=1/e^z$;
2. $\exp$ is differentiable with $\dfrac{d}{dz}e^z=e^z$.

:::

::: {.proof}

1. By @thm-cauchy-product, $e^ze^w=\sum_nc_n$ with
$$c_n=\sum_{k=0}^n\frac{z^k}{k!}\frac{w^{n-k}}{(n-k)!}=\frac1{n!}\sum_{k=0}^n\binom nkz^kw^{n-k}=\frac{(z+w)^n}{n!}$$
by the binomial theorem (@thm-binomial-theorem). So $e^ze^w=e^{z+w}$. Taking $w=-z$ gives $e^ze^{-z}=e^0=1$.

2. Differentiating term by term (@thm-power-series-differentiable), $\sum_{n\ge1}\frac{nz^{n-1}}{n!}=\sum_{m\ge0}\frac{z^m}{m!}=e^z$.

:::

By @exm-taylors-theorem-1, $e^x$ is the only differentiable $f:\mathbb R\to\mathbb R$ with $f'=f$ and $f(0)=1$. For real $x$, $e^x>0$: for $x\ge0$ every term is non-negative and the first is $1$, and $e^{-x}=1/e^x$.

## Sine and cosine

::: {#def-sine-cosine-series .definition name="Sine and cosine"}

For $z\in\mathbb C$,
$$\cos z=\frac{e^{iz}+e^{-iz}}2=\sum_{n=0}^\infty\frac{(-1)^nz^{2n}}{(2n)!},\qquad \sin z=\frac{e^{iz}-e^{-iz}}{2i}=\sum_{n=0}^\infty\frac{(-1)^nz^{2n+1}}{(2n+1)!}.$$

:::

The series follow from $e^{\pm iz}$: the powers $i^n$ make the odd terms cancel in the first combination and the even terms in the second. By definition $e^{iz}=\cos z+i\sin z$. For real $x$ the series have real coefficients, so $\cos x$ and $\sin x$ are real.

::: {#prp-sine-cosine-identities .proposition name="Basic identities"}

For all $z,w\in\mathbb C$:
$$\frac{d}{dz}\sin z=\cos z,\qquad\frac d{dz}\cos z=-\sin z,\qquad\sin^2z+\cos^2z=1,$$
$$\cos(z+w)=\cos z\cos w-\sin z\sin w,\qquad\sin(z+w)=\sin z\cos w+\cos z\sin w.$$
In particular $|\sin x|\le1$ and $|\cos x|\le1$ for real $x$.

:::

::: {.proof}

1. *Derivatives.* By the chain rule and $(e^z)'=e^z$, $(\sin z)'=\frac{ie^{iz}+ie^{-iz}}{2i}=\cos z$ and $(\cos z)'=\frac{ie^{iz}-ie^{-iz}}{2}=-\sin z$.

2. *Pythagoras.* $\cos^2z=\frac{e^{2iz}+2+e^{-2iz}}4$ and $\sin^2z=-\frac{e^{2iz}-2+e^{-2iz}}4$; they add up to $1$. For real $x$ both squares are non-negative, so each is at most $1$.

3. *Addition formula for $\cos$.* Expand
$$\cos z\cos w-\sin z\sin w=\frac{(e^{iz}+e^{-iz})(e^{iw}+e^{-iw})+(e^{iz}-e^{-iz})(e^{iw}-e^{-iw})}4.$$
The mixed terms $e^{i(z-w)}$ and $e^{-i(z-w)}$ cancel, leaving $\frac{2e^{i(z+w)}+2e^{-i(z+w)}}4=\cos(z+w)$.

4. *Addition formula for $\sin$.* Differentiate the identity of step 3 with respect to $z$, keeping $w$ fixed: $-\sin z\cos w-\cos z\sin w=-\sin(z+w)$.

:::

## The number $\pi$

::: {#lem-sine-cosine-bounds .lemma name="Polynomial bounds"}

For real $x\ge0$:
$$\sin x\le x,\qquad\cos x\ge1-\frac{x^2}2,\qquad\sin x\ge x-\frac{x^3}6,\qquad\cos x\le1-\frac{x^2}2+\frac{x^4}{24}.$$

:::

::: {.proof}

Each difference $D$ below vanishes at $0$ and has $D'\ge0$ on $[0,\infty)$, so $D\ge0$ there by @cor-sign-of-derivative.

1. $D_1=x-\sin x$: $D_1'=1-\cos x\ge0$ since $\cos x\le1$.

2. $D_2=\cos x-1+\frac{x^2}2$: $D_2'=x-\sin x=D_1\ge0$.

3. $D_3=\sin x-x+\frac{x^3}6$: $D_3'=\cos x-1+\frac{x^2}2=D_2\ge0$.

4. $D_4=1-\frac{x^2}2+\frac{x^4}{24}-\cos x$: $D_4'=-x+\frac{x^3}6+\sin x=D_3\ge0$.

:::

The same argument continues: truncating the series of $\sin x$ or $\cos x$ ($x\ge0$) after a positive term gives an upper bound, after a negative term a lower bound.

::: {#def-pi .definition name="The number $\pi$"}

$\pi/2$ is the smallest positive zero of $\cos$ on $\mathbb R$.

:::

::: {#fig-exponential-and-trigonometric-functions-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (4.6,0) node[lab, right] {$x$};
\draw[->, faint] (0,-1.3) -- (0,1.4) node[lab, above] {};
\draw[emph] (0.000,1.000) -- (0.054,0.997) -- (0.107,0.986) -- (0.161,0.970) -- (0.214,0.946) -- (0.268,0.916) -- (0.322,0.880) -- (0.375,0.838) -- (0.429,0.790) -- (0.483,0.737) -- (0.536,0.679) -- (0.590,0.616) -- (0.643,0.549) -- (0.697,0.478) -- (0.751,0.404) -- (0.804,0.327) -- (0.858,0.248) -- (0.912,0.168) -- (0.965,0.086) -- (1.019,0.003) -- (1.073,-0.079) -- (1.126,-0.161) -- (1.180,-0.242) -- (1.233,-0.321) -- (1.287,-0.398) -- (1.341,-0.472) -- (1.394,-0.543) -- (1.448,-0.611) -- (1.501,-0.674) -- (1.555,-0.732) -- (1.609,-0.786) -- (1.662,-0.834) -- (1.716,-0.877) -- (1.770,-0.913) -- (1.823,-0.944) -- (1.877,-0.968) -- (1.930,-0.985) -- (1.984,-0.996) -- (2.038,-1.000) -- (2.091,-0.997) -- (2.145,-0.987) -- (2.199,-0.971) -- (2.252,-0.948) -- (2.306,-0.919) -- (2.360,-0.883) -- (2.413,-0.841) -- (2.467,-0.794) -- (2.520,-0.741) -- (2.574,-0.683) -- (2.628,-0.621) -- (2.681,-0.554) -- (2.735,-0.484) -- (2.788,-0.410) -- (2.842,-0.333) -- (2.896,-0.255) -- (2.949,-0.174) -- (3.003,-0.092) -- (3.057,-0.010) -- (3.110,0.073) -- (3.164,0.154) -- (3.218,0.235) -- (3.271,0.315) -- (3.325,0.392) -- (3.378,0.466) -- (3.432,0.538) -- (3.486,0.605) -- (3.539,0.669) -- (3.593,0.728) -- (3.646,0.782) -- (3.700,0.831) -- (3.754,0.874) -- (3.807,0.911) -- (3.861,0.942) -- (3.915,0.966) -- (3.968,0.984) -- (4.022,0.995) -- (4.075,1.000) -- (4.129,0.998) -- (4.183,0.988) -- (4.236,0.973) -- (4.290,0.950);
\draw[faint] (0.000,0.000) -- (0.054,0.082) -- (0.107,0.164) -- (0.161,0.245) -- (0.214,0.324) -- (0.268,0.401) -- (0.322,0.475) -- (0.375,0.546) -- (0.429,0.613) -- (0.483,0.676) -- (0.536,0.735) -- (0.590,0.788) -- (0.643,0.836) -- (0.697,0.878) -- (0.751,0.915) -- (0.804,0.945) -- (0.858,0.969) -- (0.912,0.986) -- (0.965,0.996) -- (1.019,1.000) -- (1.073,0.997) -- (1.126,0.987) -- (1.180,0.970) -- (1.233,0.947) -- (1.287,0.917) -- (1.341,0.882) -- (1.394,0.840) -- (1.448,0.792) -- (1.501,0.739) -- (1.555,0.681) -- (1.609,0.618) -- (1.662,0.551) -- (1.716,0.481) -- (1.770,0.407) -- (1.823,0.330) -- (1.877,0.251) -- (1.930,0.171) -- (1.984,0.089) -- (2.038,0.007) -- (2.091,-0.076) -- (2.145,-0.158) -- (2.199,-0.239) -- (2.252,-0.318) -- (2.306,-0.395) -- (2.360,-0.469) -- (2.413,-0.540) -- (2.467,-0.608) -- (2.520,-0.671) -- (2.574,-0.730) -- (2.628,-0.784) -- (2.681,-0.832) -- (2.735,-0.875) -- (2.788,-0.912) -- (2.842,-0.943) -- (2.896,-0.967) -- (2.949,-0.985) -- (3.003,-0.996) -- (3.057,-1.000) -- (3.110,-0.997) -- (3.164,-0.988) -- (3.218,-0.972) -- (3.271,-0.949) -- (3.325,-0.920) -- (3.378,-0.885) -- (3.432,-0.843) -- (3.486,-0.796) -- (3.539,-0.743) -- (3.593,-0.686) -- (3.646,-0.623) -- (3.700,-0.557) -- (3.754,-0.487) -- (3.807,-0.413) -- (3.861,-0.336) -- (3.915,-0.258) -- (3.968,-0.177) -- (4.022,-0.096) -- (4.075,-0.013) -- (4.129,0.069) -- (4.183,0.151) -- (4.236,0.232) -- (4.290,0.312);
\node[hl dot] at (1.021,0.000) {};\node[lab, below] at (1.021,-0.05) {$\frac\pi2$};\draw[faint] (2.042,-0.06) -- (2.042,0.06); \node[lab, tick, below] at (2.042,-0.05) {$\pi$};\draw[faint] (4.084,-0.06) -- (4.084,0.06); \node[lab, tick, below] at (4.084,-0.05) {$2\pi$};
\node[lab] at (0.4,1.15) {$\cos$}; \node[lab] at (1.6,1.15) {$\sin$};
\end{tikzpicture}
\end{center}
```

$\cos$ starts at $1$ and must reach $0$ before $x=2$; its first zero is $\frac\pi2$ by definition. From the addition formulas, $\sin$ and $\cos$ then repeat with period $2\pi$.

:::

This makes sense. By @lem-sine-cosine-bounds, $\cos x\ge1-\frac{x^2}2>0$ on $[0,1]$, and $\cos2\le1-2+\frac{16}{24}=-\frac13<0$. By the intermediate value theorem (@thm-intermediate-value-proof) $\cos$ has a zero in $(1,2)$. The set of zeros in $[1,2]$ is non-empty; its infimum $c$ is again a zero, since by continuity $\cos c$ is the limit of $\cos$ at zeros approaching $c$. So $1<\pi/2<2$.

::: {#prp-sine-cosine-periodic .proposition name="Shifts and periodicity"}

$\sin\frac\pi2=1$, and for all $z\in\mathbb C$
$$\cos\Bigl(z+\frac\pi2\Bigr)=-\sin z,\quad\sin\Bigl(z+\frac\pi2\Bigr)=\cos z,\quad\cos(z+\pi)=-\cos z,\quad\sin(z+\pi)=-\sin z,$$
so $\sin$ and $\cos$ have period $2\pi$, and $e^{z+2\pi i}=e^z$.

:::

::: {.proof}

1. On $[0,\frac\pi2)$, $\cos>0$, so $\sin$ is strictly increasing there (@cor-sign-of-derivative) and $\sin\frac\pi2>\sin0=0$. Since $\sin^2\frac\pi2=1-\cos^2\frac\pi2=1$, we get $\sin\frac\pi2=1$.

2. By the addition formulas with $w=\frac\pi2$: $\cos(z+\frac\pi2)=\cos z\cdot0-\sin z\cdot1=-\sin z$ and $\sin(z+\frac\pi2)=\sin z\cdot0+\cos z\cdot1=\cos z$.

3. Applying step 2 twice gives the shifts by $\pi$, and applying those twice gives period $2\pi$.

4. $e^{2\pi i}=\cos2\pi+i\sin2\pi=1$, so $e^{z+2\pi i}=e^ze^{2\pi i}=e^z$.

:::

::: {#fig-exponential-and-trigonometric-functions-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-1.7,0) -- (1.9,0); \draw[->, faint] (0,-1.6) -- (0,1.7);
\draw[emph] (0,0) circle (1.3);
\draw[hl] (1.3,0) arc (0:51.57:1.3); \node[lab, right] at (1.221,0.565) {$x$};
\draw[->, emph] (0,0) -- (0.808,1.018);
\node[dot] at (0.808,1.018) {}; \node[lab, above right] at (0.808,1.018) {$(\cos x,\sin x)$};
\draw[faint, dashed] (0.808,1.018) -- (0.808,0);
\end{tikzpicture}
\end{center}
```

Since $\cos^2x+\sin^2x=1$, the point $(\cos x,\sin x)$ lies on the unit circle; going once round corresponds to adding $2\pi$ to $x$.

:::

## Hyperbolic functions

The *hyperbolic cosine and sine* (@def-hyperbolic-functions) are
$$\cosh z=\frac{e^z+e^{-z}}2=\sum_{n\ge0}\frac{z^{2n}}{(2n)!},\qquad\sinh z=\frac{e^z-e^{-z}}2=\sum_{n\ge0}\frac{z^{2n+1}}{(2n+1)!}.$$
The same calculations as above (compare @prp-hyperbolic-identities) give $(\cosh z)'=\sinh z$, $(\sinh z)'=\cosh z$ and $\cosh^2z-\sinh^2z=1$, and comparing definitions, $\cosh(iz)=\cos z$ and $\sinh(iz)=i\sin z$. Over $\mathbb C$, trigonometric and hyperbolic functions are the same functions rotated by $i$.
