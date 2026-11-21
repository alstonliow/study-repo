---
title: "Central Limit Theorem"
sources: [cs70-20.5, camii-pm-7]
requires: [math/probability/continuous/normal-distribution, math/probability/discrete/concentration-inequalities]
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 20 (cs70-20.5), in our own wording. The example is our own, checked by an exact computation. -->

The law of large numbers (@thm-law-of-large-numbers) says that the average $\frac{S_n}n$ of $n$ i.i.d. observations concentrates at the mean $\mu$. The central limit theorem says more: for large $n$ the *shape* of its distribution is close to the normal distribution $N\bigl(\mu,\frac{\sigma^2}n\bigr)$, whatever the distribution of a single observation. The mean and variance are known already (@prp-sample-mean); the new point is the normal shape. To get a limit that does not depend on $n$, standardize:
$$\frac{S_n/n-\mu}{\sigma/\sqrt n}=\frac{S_n-n\mu}{\sigma\sqrt n},$$
which has mean $0$ and variance $1$ for every $n$.

::: {#thm-central-limit-theorem .theorem name="Central limit theorem"}

Let $X_1,X_2,\dots$ be i.i.d. random variables with finite mean $\mu$ and finite variance $\sigma^2>0$, and let $S_n=X_1+\dots+X_n$. Then for every constant $c$,
$$\Pr\Bigl(\frac{S_n-n\mu}{\sigma\sqrt n}\le c\Bigr)\to\frac1{\sqrt{2\pi}}\int_{-\infty}^c e^{-x^2/2}\,dx\qquad\text{as }n\to\infty.$$

:::

<!-- Proof added 2026-11-21 from Cambridge Part II Probability and Measure (Michaelmas 2016 lecture notes), Section 7.2, in our own wording; it uses characteristic functions and Lévy's continuity theorem from math/probability/measure-theoretic/weak-convergence. -->

::: {.proof}

1. Replacing $X_i$ by $(X_i-\mu)/\sigma$, assume $\mu=0$, $\sigma=1$; let $\varphi(u)=E[e^{iuX_1}]$ and $Y_n=S_n/\sqrt n$.

2. *Expansion of $\varphi$.* The $u$-derivatives of $e^{iuX_1}$ of order $1$ and $2$ are bounded by $|X_1|$ and $X_1^2$, which are integrable. Differentiating under the integral twice (@thm-differentiation-under-integral) and using dominated convergence for continuity, $\varphi$ is $C^2$ with $\varphi'(0)=iE[X_1]=0$ and $\varphi''(0)=-E[X_1^2]=-1$. By Taylor's theorem, $\varphi(u)=1-\frac{u^2}2+r(u)$ with $r(u)/u^2\to0$ as $u\to0$.

3. *Characteristic function of $Y_n$.* By independence (@prp-convolution-properties), $\varphi_{Y_n}(u)=\varphi(u/\sqrt n)^n$.

4. For complex numbers of modulus at most $1$, $|a_1\cdots a_n-b_1\cdots b_n|\le\sum_k|a_k-b_k|$ (telescope one factor at a time). With $a_k=\varphi(u/\sqrt n)$ and $b_k=1-\frac{u^2}{2n}$, which has modulus at most $1$ once $n\ge u^2/4$,
$$\Big|\varphi_{Y_n}(u)-\Big(1-\frac{u^2}{2n}\Big)^n\Big|\le n\,\big|r(u/\sqrt n)\big|=u^2\,\frac{|r(u/\sqrt n)|}{u^2/n}\to0 .$$

5. Since $(1-\frac{u^2}{2n})^n\to e^{-u^2/2}$, the characteristic function of $N(0,1)$ (@prp-gaussian-fourier), $\varphi_{Y_n}(u)\to e^{-u^2/2}$ for every $u$. By Lévy's continuity theorem (@thm-levy-continuity), $Y_n\to Z\sim N(0,1)$ weakly.

6. *From weak convergence to the distribution function.* Fix $c$ and $k\ge1$, and let $h$ be continuous with $\mathbf 1_{(-\infty,c]}\le h\le\mathbf 1_{(-\infty,c+1/k]}$. Then $\limsup_n\Pr(Y_n\le c)\le\lim_nE[h(Y_n)]=E[h(Z)]\le\Phi(c+\frac1k)$. Similarly, with $h$ between $\mathbf 1_{(-\infty,c-1/k]}$ and $\mathbf 1_{(-\infty,c]}$, $\liminf_n\Pr(Y_n\le c)\ge\Phi(c-\frac1k)$. Let $k\to\infty$; $\Phi$ is continuous.

:::

::: {#fig-central-limit-theorem-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=40cm]
\fill[bar] (-3.310,0) rectangle (-3.170,0.00019);
\fill[bar] (-3.130,0) rectangle (-2.990,0.00039);
\fill[bar] (-2.950,0) rectangle (-2.810,0.00077);
\fill[bar] (-2.770,0) rectangle (-2.630,0.00141);
\fill[bar] (-2.590,0) rectangle (-2.450,0.00245);
\fill[bar] (-2.410,0) rectangle (-2.270,0.00403);
\fill[bar] (-2.230,0) rectangle (-2.090,0.00634);
\fill[bar] (-2.050,0) rectangle (-1.910,0.00954);
\fill[bar] (-1.870,0) rectangle (-1.730,0.01375);
\fill[bar] (-1.690,0) rectangle (-1.550,0.01904);
\fill[bar] (-1.510,0) rectangle (-1.370,0.02539);
\fill[bar] (-1.330,0) rectangle (-1.190,0.03262);
\fill[bar] (-1.150,0) rectangle (-1.010,0.04046);
\fill[bar] (-0.970,0) rectangle (-0.830,0.04846);
\fill[bar] (-0.790,0) rectangle (-0.650,0.05612);
\fill[bar] (-0.610,0) rectangle (-0.470,0.06287);
\fill[bar] (-0.430,0) rectangle (-0.290,0.06816);
\fill[bar] (-0.250,0) rectangle (-0.110,0.07153);
\fill[bar] (-0.070,0) rectangle (0.070,0.07269);
\fill[bar] (0.110,0) rectangle (0.250,0.07153);
\fill[bar] (0.290,0) rectangle (0.430,0.06816);
\fill[bar] (0.470,0) rectangle (0.610,0.06287);
\fill[bar] (0.650,0) rectangle (0.790,0.05612);
\fill[bar] (0.830,0) rectangle (0.970,0.04846);
\fill[bar] (1.010,0) rectangle (1.150,0.04046);
\fill[bar] (1.190,0) rectangle (1.330,0.03262);
\fill[bar] (1.370,0) rectangle (1.510,0.02539);
\fill[bar] (1.550,0) rectangle (1.690,0.01904);
\fill[bar] (1.730,0) rectangle (1.870,0.01375);
\fill[bar] (1.910,0) rectangle (2.050,0.00954);
\fill[bar] (2.090,0) rectangle (2.230,0.00634);
\fill[bar] (2.270,0) rectangle (2.410,0.00403);
\fill[bar] (2.450,0) rectangle (2.590,0.00245);
\fill[bar] (2.630,0) rectangle (2.770,0.00141);
\fill[bar] (2.810,0) rectangle (2.950,0.00077);
\fill[bar] (2.990,0) rectangle (3.130,0.00039);
\fill[bar] (3.170,0) rectangle (3.310,0.00019);
\draw[emph, accent, domain=-4.5:4.5, samples=100] plot (\x,{exp(-(\x/0.18)*(\x/0.18)/(2*29.1667))/(5.4006*sqrt(2*pi))});
\draw[muted] (-4.6,0) -- (4.6,0);
\foreach \s in {20,25,...,50} \node[tick, below] at ({(\s-35)*0.18},0) {$\s$};
\node[lab, accent] at (2.6,0.06) {$N(35,\tfrac{350}{12})$};
\end{tikzpicture}
\end{center}
```

The exact distribution of the sum of $10$ fair dice (bars) and the normal density with the same mean and variance. Already for $n=10$ they are close.

:::

::: {#rmk-central-limit-theorem-meaning}

1. The proof above uses characteristic functions, which exist for every distribution; moment generating functions would need extra assumptions.

2. Every trace of the original distribution disappears except $\mu$ and $\sigma^2$. The standard deviation of the average is $\sigma/\sqrt n$, so its bell curve becomes a spike at $\mu$ at the rate $1/\sqrt n$.

3. This is why the normal distribution models aggregate data so well, such as measurement errors or the heights in a population: each value is a sum of many small, roughly independent effects.

4. In practice one replaces $\frac{S_n-n\mu}{\sigma\sqrt n}$ by a standard normal variable for moderately large $n$. The theorem gives no error bound; for one, see the Berry–Esseen theorem.

:::

::: {#fig-central-limit-theorem-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (7.6,0) node[lab, right] {$z$};
\draw[faint] (2.600,2.539) -- (2.640,2.456) -- (2.680,2.376) -- (2.720,2.298) -- (2.760,2.222) -- (2.800,2.150) -- (2.840,2.079) -- (2.880,2.011) -- (2.920,1.945) -- (2.960,1.881) -- (3.000,1.820) -- (3.040,1.760) -- (3.080,1.702) -- (3.120,1.646) -- (3.160,1.592) -- (3.200,1.540) -- (3.240,1.490) -- (3.280,1.441) -- (3.320,1.394) -- (3.360,1.348) -- (3.400,1.304) -- (3.440,1.261) -- (3.480,1.220) -- (3.520,1.180) -- (3.560,1.141) -- (3.600,1.104) -- (3.640,1.067) -- (3.680,1.032) -- (3.720,0.999) -- (3.760,0.966) -- (3.800,0.934) -- (3.840,0.904) -- (3.880,0.874) -- (3.920,0.845) -- (3.960,0.818) -- (4.000,0.791) -- (4.040,0.765) -- (4.080,0.740) -- (4.120,0.716) -- (4.160,0.692) -- (4.200,0.669) -- (4.240,0.647) -- (4.280,0.626) -- (4.320,0.606) -- (4.360,0.586) -- (4.400,0.567) -- (4.440,0.548) -- (4.480,0.530) -- (4.520,0.513) -- (4.560,0.496) -- (4.600,0.480) -- (4.640,0.464) -- (4.680,0.449) -- (4.720,0.434) -- (4.760,0.420) -- (4.800,0.406) -- (4.840,0.393) -- (4.880,0.380) -- (4.920,0.367) -- (4.960,0.355) -- (5.000,0.344) -- (5.040,0.332) -- (5.080,0.322) -- (5.120,0.311) -- (5.160,0.301) -- (5.200,0.291) -- (5.240,0.281) -- (5.280,0.272) -- (5.320,0.263) -- (5.360,0.255) -- (5.400,0.246) -- (5.440,0.238) -- (5.480,0.230) -- (5.520,0.223) -- (5.560,0.216) -- (5.600,0.208) -- (5.640,0.202) -- (5.680,0.195) -- (5.720,0.189) -- (5.760,0.182) -- (5.800,0.176) -- (5.840,0.171) -- (5.880,0.165) -- (5.920,0.160) -- (5.960,0.154) -- (6.000,0.149) -- (6.040,0.144) -- (6.080,0.140) -- (6.120,0.135) -- (6.160,0.131) -- (6.200,0.126) -- (6.240,0.122) -- (6.280,0.118) -- (6.320,0.114) -- (6.360,0.111) -- (6.400,0.107) -- (6.440,0.104) -- (6.480,0.100) -- (6.520,0.097) -- (6.560,0.094) -- (6.600,0.091) -- (6.640,0.088) -- (6.680,0.085) -- (6.720,0.082) -- (6.760,0.079) -- (6.800,0.077) -- (6.840,0.074) -- (6.880,0.072) -- (6.920,0.069) -- (6.960,0.067) -- (7.000,0.065) -- (7.040,0.063) -- (7.080,0.061) -- (7.120,0.059) -- (7.160,0.057) -- (7.200,0.055);
\draw[emph] (1.240,0.000) -- (1.280,0.002) -- (1.320,0.007) -- (1.360,0.015) -- (1.400,0.027) -- (1.440,0.043) -- (1.480,0.064) -- (1.520,0.089) -- (1.560,0.119) -- (1.600,0.152) -- (1.640,0.189) -- (1.680,0.230) -- (1.720,0.274) -- (1.760,0.320) -- (1.800,0.368) -- (1.840,0.418) -- (1.880,0.469) -- (1.920,0.520) -- (1.960,0.573) -- (2.000,0.625) -- (2.040,0.677) -- (2.080,0.728) -- (2.120,0.778) -- (2.160,0.827) -- (2.200,0.874) -- (2.240,0.920) -- (2.280,0.964) -- (2.320,1.006) -- (2.360,1.045) -- (2.400,1.083) -- (2.440,1.118) -- (2.480,1.150) -- (2.520,1.180) -- (2.560,1.207) -- (2.600,1.232) -- (2.640,1.254) -- (2.680,1.274) -- (2.720,1.291) -- (2.760,1.305) -- (2.800,1.318) -- (2.840,1.327) -- (2.880,1.335) -- (2.920,1.340) -- (2.960,1.343) -- (3.000,1.344) -- (3.040,1.343) -- (3.080,1.340) -- (3.120,1.336) -- (3.160,1.329) -- (3.200,1.321) -- (3.240,1.312) -- (3.280,1.301) -- (3.320,1.288) -- (3.360,1.275) -- (3.400,1.260) -- (3.440,1.244) -- (3.480,1.228) -- (3.520,1.210) -- (3.560,1.191) -- (3.600,1.172) -- (3.640,1.152) -- (3.680,1.132) -- (3.720,1.111) -- (3.760,1.090) -- (3.800,1.068) -- (3.840,1.046) -- (3.880,1.024) -- (3.920,1.001) -- (3.960,0.978) -- (4.000,0.956) -- (4.040,0.933) -- (4.080,0.910) -- (4.120,0.887) -- (4.160,0.865) -- (4.200,0.842) -- (4.240,0.820) -- (4.280,0.798) -- (4.320,0.776) -- (4.360,0.754) -- (4.400,0.732) -- (4.440,0.711) -- (4.480,0.690) -- (4.520,0.670) -- (4.560,0.649) -- (4.600,0.629) -- (4.640,0.610) -- (4.680,0.591) -- (4.720,0.572) -- (4.760,0.553) -- (4.800,0.535) -- (4.840,0.518) -- (4.880,0.501) -- (4.920,0.484) -- (4.960,0.467) -- (5.000,0.451) -- (5.040,0.436) -- (5.080,0.420) -- (5.120,0.406) -- (5.160,0.391) -- (5.200,0.377) -- (5.240,0.363) -- (5.280,0.350) -- (5.320,0.337) -- (5.360,0.325) -- (5.400,0.313) -- (5.440,0.301) -- (5.480,0.290) -- (5.520,0.279) -- (5.560,0.268) -- (5.600,0.258) -- (5.640,0.248) -- (5.680,0.238) -- (5.720,0.229) -- (5.760,0.220) -- (5.800,0.211) -- (5.840,0.203) -- (5.880,0.194) -- (5.920,0.187) -- (5.960,0.179) -- (6.000,0.172) -- (6.040,0.165) -- (6.080,0.158) -- (6.120,0.151) -- (6.160,0.145) -- (6.200,0.139) -- (6.240,0.133) -- (6.280,0.128) -- (6.320,0.122) -- (6.360,0.117) -- (6.400,0.112) -- (6.440,0.107) -- (6.480,0.103) -- (6.520,0.098) -- (6.560,0.094) -- (6.600,0.090) -- (6.640,0.086) -- (6.680,0.082) -- (6.720,0.079) -- (6.760,0.075) -- (6.800,0.072) -- (6.840,0.069) -- (6.880,0.066) -- (6.920,0.063) -- (6.960,0.060) -- (7.000,0.057) -- (7.040,0.055) -- (7.080,0.052) -- (7.120,0.050) -- (7.160,0.048) -- (7.200,0.045);
\draw[hl] (0.040,0.000) -- (0.080,0.000) -- (0.120,0.001) -- (0.160,0.001) -- (0.200,0.001) -- (0.240,0.001) -- (0.280,0.002) -- (0.320,0.002) -- (0.360,0.003) -- (0.400,0.004) -- (0.440,0.005) -- (0.480,0.006) -- (0.520,0.007) -- (0.560,0.009) -- (0.600,0.011) -- (0.640,0.013) -- (0.680,0.016) -- (0.720,0.019) -- (0.760,0.023) -- (0.800,0.027) -- (0.840,0.031) -- (0.880,0.037) -- (0.920,0.043) -- (0.960,0.050) -- (1.000,0.057) -- (1.040,0.066) -- (1.080,0.075) -- (1.120,0.085) -- (1.160,0.096) -- (1.200,0.108) -- (1.240,0.121) -- (1.280,0.136) -- (1.320,0.151) -- (1.360,0.167) -- (1.400,0.185) -- (1.440,0.203) -- (1.480,0.223) -- (1.520,0.244) -- (1.560,0.265) -- (1.600,0.288) -- (1.640,0.312) -- (1.680,0.337) -- (1.720,0.363) -- (1.760,0.389) -- (1.800,0.417) -- (1.840,0.445) -- (1.880,0.474) -- (1.920,0.503) -- (1.960,0.533) -- (2.000,0.563) -- (2.040,0.594) -- (2.080,0.625) -- (2.120,0.656) -- (2.160,0.687) -- (2.200,0.718) -- (2.240,0.749) -- (2.280,0.779) -- (2.320,0.810) -- (2.360,0.839) -- (2.400,0.869) -- (2.440,0.897) -- (2.480,0.925) -- (2.520,0.952) -- (2.560,0.978) -- (2.600,1.004) -- (2.640,1.028) -- (2.680,1.051) -- (2.720,1.072) -- (2.760,1.093) -- (2.800,1.112) -- (2.840,1.130) -- (2.880,1.146) -- (2.920,1.161) -- (2.960,1.175) -- (3.000,1.187) -- (3.040,1.198) -- (3.080,1.207) -- (3.120,1.214) -- (3.160,1.220) -- (3.200,1.225) -- (3.240,1.228) -- (3.280,1.229) -- (3.320,1.229) -- (3.360,1.228) -- (3.400,1.225) -- (3.440,1.221) -- (3.480,1.215) -- (3.520,1.208) -- (3.560,1.200) -- (3.600,1.191) -- (3.640,1.180) -- (3.680,1.169) -- (3.720,1.156) -- (3.760,1.142) -- (3.800,1.128) -- (3.840,1.112) -- (3.880,1.096) -- (3.920,1.079) -- (3.960,1.061) -- (4.000,1.043) -- (4.040,1.024) -- (4.080,1.004) -- (4.120,0.984) -- (4.160,0.964) -- (4.200,0.943) -- (4.240,0.922) -- (4.280,0.900) -- (4.320,0.879) -- (4.360,0.857) -- (4.400,0.835) -- (4.440,0.813) -- (4.480,0.791) -- (4.520,0.770) -- (4.560,0.748) -- (4.600,0.726) -- (4.640,0.704) -- (4.680,0.683) -- (4.720,0.662) -- (4.760,0.641) -- (4.800,0.620) -- (4.840,0.599) -- (4.880,0.579) -- (4.920,0.559) -- (4.960,0.540) -- (5.000,0.520) -- (5.040,0.502) -- (5.080,0.483) -- (5.120,0.465) -- (5.160,0.447) -- (5.200,0.430) -- (5.240,0.413) -- (5.280,0.397) -- (5.320,0.381) -- (5.360,0.365) -- (5.400,0.350) -- (5.440,0.336) -- (5.480,0.322) -- (5.520,0.308) -- (5.560,0.294) -- (5.600,0.282) -- (5.640,0.269) -- (5.680,0.257) -- (5.720,0.245) -- (5.760,0.234) -- (5.800,0.223) -- (5.840,0.213) -- (5.880,0.203) -- (5.920,0.193) -- (5.960,0.184) -- (6.000,0.175) -- (6.040,0.166) -- (6.080,0.158) -- (6.120,0.150) -- (6.160,0.143) -- (6.200,0.135) -- (6.240,0.129) -- (6.280,0.122) -- (6.320,0.116) -- (6.360,0.110) -- (6.400,0.104) -- (6.440,0.098) -- (6.480,0.093) -- (6.520,0.088) -- (6.560,0.083) -- (6.600,0.079) -- (6.640,0.074) -- (6.680,0.070) -- (6.720,0.066) -- (6.760,0.063) -- (6.800,0.059) -- (6.840,0.056) -- (6.880,0.052) -- (6.920,0.049) -- (6.960,0.047) -- (7.000,0.044) -- (7.040,0.041) -- (7.080,0.039) -- (7.120,0.037) -- (7.160,0.034) -- (7.200,0.032);
\draw[emph, dashed, domain=0:7.2, samples=80, smooth, variable=\x] plot ({\x}, {3.60*exp(-((\x-3.6)^2)/(2*1.2^2))/(1.2*sqrt(2*pi))});
\draw (3.6,0) -- (3.6,-0.08) node[tick, below] {$0$};
\draw (1.2,0) -- (1.2,-0.08) node[tick, below] {$-2$};
\draw (6.0,0) -- (6.0,-0.08) node[tick, below] {$2$};
\node[tick] at (1.0,2.0) {$n=1$};
\node[tick] at (5.2,1.3) {$n=4$};
\node[tick, text=accent] at (1.6,1.6) {$n=16$};
\end{tikzpicture}
\end{center}
```

Densities of the standardised sum $(S_n-n)/\sqrt n$ of $n$ independent $\operatorname{Exp}(1)$ variables for $n=1,4,16$, against the standard normal (dashed). The skew fades as $n$ grows

:::

::: {#exm-clt-dice .example name="Sum of a hundred dice"}

Roll $100$ fair dice and let $S$ be the total. One die has mean $\frac72$ and variance $\frac{35}{12}$ (@prp-standard-distributions-1), so $S$ has mean $350$ and standard deviation $\sqrt{100\cdot\frac{35}{12}}\approx17.08$. Then
$$\Pr(S\ge380)=\Pr\Bigl(\frac{S-350}{17.08}\ge1.757\Bigr)\approx1-\Phi(1.757)\approx0.039,$$
where $\Phi$ is the standard normal c.d.f. The exact value, from the distribution of $S$, is $0.0420$. Using $379.5$ in place of $380$ (a *continuity correction*, since $S$ takes integer values) gives $0.0421$.

:::
