---
title: "The Lebesgue Integral and Monotone Convergence"
sources: [camii-pm-3]
requires: [math/analysis/measure-theory/measurable-functions]
status: draft
---

<!-- Added 2026-11-21 from Cambridge Part II Probability and Measure (Michaelmas 2016 lecture notes), Sections 3.1 and 3.3, in our own wording; proofs written out in steps. The source states the comparison with the Riemann integral without proof; the proof here is our own. -->

The Riemann integral cuts the domain into pieces; the Lebesgue integral cuts the range, and measures the set where $f$ takes values in each piece. Throughout, $(E,\mathcal E,\mu)$ is a measure space and $0\cdot\infty=0$.

::: {#def-integral-simple-function .definition name="Simple function and its integral"}

A *simple function* is a finite sum $g=\sum_{k=1}^ma_k\mathbf 1_{A_k}$ with $a_k\in[0,\infty)$ and $A_k\in\mathcal E$. Its integral is

$$
\mu(g)=\int_Eg\,d\mu=\sum_{k=1}^ma_k\,\mu(A_k).
$$

:::

The value does not depend on the representation: cutting $E$ into the finitely many atoms $\bigcap_kA_k^{\varepsilon_k}$ ($\varepsilon_k\in\{0,1\}$, $A^1=A$, $A^0=A^c$) on which $g$ is constant, both sides of any two representations reduce to $\sum_{\text{atoms }C}g(C)\,\mu(C)$ by additivity. From this, $\mu(\alpha g+\beta h)=\alpha\mu(g)+\beta\mu(h)$ for simple $g,h$ and $\alpha,\beta\ge0$, and $g\le h$ implies $\mu(g)\le\mu(h)$.

::: {#def-lebesgue-integral .definition name="Lebesgue integral"}

For measurable $f:E\to[0,\infty]$,

$$
\mu(f)=\int_Ef\,d\mu=\sup\{\mu(g):\ g\text{ simple},\ g\le f\}.
$$

A measurable $f:E\to\mathbb R$ is *integrable* if $\mu(|f|)<\infty$; then $\mu(f)=\mu(f^+)-\mu(f^-)$ with $f^\pm=(\pm f)\vee0$. We write $\int_Af\,d\mu=\mu(f\mathbf 1_A)$, and $\int f(x)\,dx$ when $\mu$ is Lebesgue measure.

:::

::: {#fig-lebesgue-integral-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-0.2,0) -- (5.4,0) node[lab, right] {$x$};
\draw[->] (0,-0.2) -- (0,3.2) node[lab, above] {};
\draw[emph] (0.000,1.200) -- (0.020,1.228) -- (0.040,1.257) -- (0.060,1.285) -- (0.080,1.313) -- (0.100,1.342) -- (0.120,1.370) -- (0.140,1.398) -- (0.160,1.426) -- (0.180,1.454) -- (0.200,1.481) -- (0.220,1.509) -- (0.240,1.536) -- (0.260,1.563) -- (0.280,1.590) -- (0.300,1.617) -- (0.320,1.644) -- (0.340,1.670) -- (0.360,1.696) -- (0.380,1.722) -- (0.400,1.747) -- (0.420,1.772) -- (0.440,1.797) -- (0.460,1.822) -- (0.480,1.846) -- (0.500,1.870) -- (0.520,1.893) -- (0.540,1.916) -- (0.560,1.939) -- (0.580,1.961) -- (0.600,1.983) -- (0.620,2.004) -- (0.640,2.025) -- (0.660,2.046) -- (0.680,2.066) -- (0.700,2.086) -- (0.720,2.105) -- (0.740,2.123) -- (0.760,2.141) -- (0.780,2.159) -- (0.800,2.176) -- (0.820,2.193) -- (0.840,2.209) -- (0.860,2.224) -- (0.880,2.239) -- (0.900,2.254) -- (0.920,2.268) -- (0.940,2.281) -- (0.960,2.294) -- (0.980,2.306) -- (1.000,2.317) -- (1.020,2.328) -- (1.040,2.339) -- (1.060,2.348) -- (1.080,2.358) -- (1.100,2.366) -- (1.120,2.374) -- (1.140,2.381) -- (1.160,2.388) -- (1.180,2.394) -- (1.200,2.400) -- (1.220,2.405) -- (1.240,2.409) -- (1.260,2.413) -- (1.280,2.416) -- (1.300,2.419) -- (1.320,2.421) -- (1.340,2.422) -- (1.360,2.423) -- (1.380,2.423) -- (1.400,2.422) -- (1.420,2.421) -- (1.440,2.419) -- (1.460,2.417) -- (1.480,2.414) -- (1.500,2.411) -- (1.520,2.407) -- (1.540,2.403) -- (1.560,2.398) -- (1.580,2.392) -- (1.600,2.386) -- (1.620,2.379) -- (1.640,2.372) -- (1.660,2.364) -- (1.680,2.356) -- (1.700,2.347) -- (1.720,2.338) -- (1.740,2.328) -- (1.760,2.318) -- (1.780,2.308) -- (1.800,2.297) -- (1.820,2.285) -- (1.840,2.273) -- (1.860,2.261) -- (1.880,2.248) -- (1.900,2.235) -- (1.920,2.222) -- (1.940,2.208) -- (1.960,2.193) -- (1.980,2.179) -- (2.000,2.164) -- (2.020,2.149) -- (2.040,2.133) -- (2.060,2.117) -- (2.080,2.101) -- (2.100,2.085) -- (2.120,2.068) -- (2.140,2.052) -- (2.160,2.035) -- (2.180,2.017) -- (2.200,2.000) -- (2.220,1.983) -- (2.240,1.965) -- (2.260,1.947) -- (2.280,1.929) -- (2.300,1.911) -- (2.320,1.893) -- (2.340,1.874) -- (2.360,1.856) -- (2.380,1.838) -- (2.400,1.819) -- (2.420,1.801) -- (2.440,1.783) -- (2.460,1.764) -- (2.480,1.746) -- (2.500,1.728) -- (2.520,1.709) -- (2.540,1.691) -- (2.560,1.673) -- (2.580,1.655) -- (2.600,1.637) -- (2.620,1.620) -- (2.640,1.602) -- (2.660,1.585) -- (2.680,1.568) -- (2.700,1.551) -- (2.720,1.534) -- (2.740,1.518) -- (2.760,1.501) -- (2.780,1.485) -- (2.800,1.470) -- (2.820,1.454) -- (2.840,1.439) -- (2.860,1.424) -- (2.880,1.410) -- (2.900,1.396) -- (2.920,1.382) -- (2.940,1.369) -- (2.960,1.356) -- (2.980,1.343) -- (3.000,1.331) -- (3.020,1.319) -- (3.040,1.308) -- (3.060,1.297) -- (3.080,1.287) -- (3.100,1.277) -- (3.120,1.267) -- (3.140,1.258) -- (3.160,1.249) -- (3.180,1.241) -- (3.200,1.234) -- (3.220,1.227) -- (3.240,1.220) -- (3.260,1.214) -- (3.280,1.209) -- (3.300,1.204) -- (3.320,1.200) -- (3.340,1.196) -- (3.360,1.193) -- (3.380,1.190) -- (3.400,1.188) -- (3.420,1.187) -- (3.440,1.186) -- (3.460,1.186) -- (3.480,1.186) -- (3.500,1.187) -- (3.520,1.188) -- (3.540,1.190) -- (3.560,1.193) -- (3.580,1.197) -- (3.600,1.200) -- (3.620,1.205) -- (3.640,1.210) -- (3.660,1.216) -- (3.680,1.222) -- (3.700,1.229) -- (3.720,1.237) -- (3.740,1.245) -- (3.760,1.254) -- (3.780,1.263) -- (3.800,1.273) -- (3.820,1.284) -- (3.840,1.295) -- (3.860,1.307) -- (3.880,1.319) -- (3.900,1.332) -- (3.920,1.345) -- (3.940,1.359) -- (3.960,1.374) -- (3.980,1.389) -- (4.000,1.405) -- (4.020,1.421) -- (4.040,1.438) -- (4.060,1.455) -- (4.080,1.473) -- (4.100,1.491) -- (4.120,1.510) -- (4.140,1.529) -- (4.160,1.549) -- (4.180,1.569) -- (4.200,1.590) -- (4.220,1.611) -- (4.240,1.633) -- (4.260,1.655) -- (4.280,1.677) -- (4.300,1.700) -- (4.320,1.723) -- (4.340,1.747) -- (4.360,1.771) -- (4.380,1.795) -- (4.400,1.820) -- (4.420,1.844) -- (4.440,1.870) -- (4.460,1.895) -- (4.480,1.921) -- (4.500,1.947) -- (4.520,1.974) -- (4.540,2.000) -- (4.560,2.027) -- (4.580,2.054) -- (4.600,2.081) -- (4.620,2.109) -- (4.640,2.136) -- (4.660,2.164) -- (4.680,2.192) -- (4.700,2.220) -- (4.720,2.248) -- (4.740,2.276) -- (4.760,2.304) -- (4.780,2.333) -- (4.800,2.361) -- (4.820,2.390) -- (4.840,2.418) -- (4.860,2.446) -- (4.880,2.475) -- (4.900,2.503) -- (4.920,2.531) -- (4.940,2.560) -- (4.960,2.588) -- (4.980,2.616) -- (5.000,2.644);
\draw[gridline] (0,0.250) -- (5.0,0.250);
\draw[gridline] (0,0.500) -- (5.0,0.500);
\draw[gridline] (0,0.750) -- (5.0,0.750);
\draw[gridline] (0,1.000) -- (5.0,1.000);
\draw[gridline] (0,1.250) -- (5.0,1.250);
\draw[gridline] (0,1.500) -- (5.0,1.500);
\draw[gridline] (0,1.750) -- (5.0,1.750);
\draw[gridline] (0,2.000) -- (5.0,2.000);
\draw[gridline] (0,2.250) -- (5.0,2.250);
\draw[gridline] (0,2.500) -- (5.0,2.500);
\draw[gridline] (0,2.750) -- (5.0,2.750);
\draw[gridline] (0,3.000) -- (5.0,3.000);
\draw[hl] (0.000,1.000) -- (0.020,1.000) -- (0.040,1.250) -- (0.060,1.250) -- (0.080,1.250) -- (0.100,1.250) -- (0.120,1.250) -- (0.140,1.250) -- (0.160,1.250) -- (0.180,1.250) -- (0.200,1.250) -- (0.220,1.500) -- (0.240,1.500) -- (0.260,1.500) -- (0.280,1.500) -- (0.300,1.500) -- (0.320,1.500) -- (0.340,1.500) -- (0.360,1.500) -- (0.380,1.500) -- (0.400,1.500) -- (0.420,1.750) -- (0.440,1.750) -- (0.460,1.750) -- (0.480,1.750) -- (0.500,1.750) -- (0.520,1.750) -- (0.540,1.750) -- (0.560,1.750) -- (0.580,1.750) -- (0.600,1.750) -- (0.620,2.000) -- (0.640,2.000) -- (0.660,2.000) -- (0.680,2.000) -- (0.700,2.000) -- (0.720,2.000) -- (0.740,2.000) -- (0.760,2.000) -- (0.780,2.000) -- (0.800,2.000) -- (0.820,2.000) -- (0.840,2.000) -- (0.860,2.000) -- (0.880,2.000) -- (0.900,2.250) -- (0.920,2.250) -- (0.940,2.250) -- (0.960,2.250) -- (0.980,2.250) -- (1.000,2.250) -- (1.020,2.250) -- (1.040,2.250) -- (1.060,2.250) -- (1.080,2.250) -- (1.100,2.250) -- (1.120,2.250) -- (1.140,2.250) -- (1.160,2.250) -- (1.180,2.250) -- (1.200,2.250) -- (1.220,2.250) -- (1.240,2.250) -- (1.260,2.250) -- (1.280,2.250) -- (1.300,2.250) -- (1.320,2.250) -- (1.340,2.250) -- (1.360,2.250) -- (1.380,2.250) -- (1.400,2.250) -- (1.420,2.250) -- (1.440,2.250) -- (1.460,2.250) -- (1.480,2.250) -- (1.500,2.250) -- (1.520,2.250) -- (1.540,2.250) -- (1.560,2.250) -- (1.580,2.250) -- (1.600,2.250) -- (1.620,2.250) -- (1.640,2.250) -- (1.660,2.250) -- (1.680,2.250) -- (1.700,2.250) -- (1.720,2.250) -- (1.740,2.250) -- (1.760,2.250) -- (1.780,2.250) -- (1.800,2.250) -- (1.820,2.250) -- (1.840,2.250) -- (1.860,2.250) -- (1.880,2.000) -- (1.900,2.000) -- (1.920,2.000) -- (1.940,2.000) -- (1.960,2.000) -- (1.980,2.000) -- (2.000,2.000) -- (2.020,2.000) -- (2.040,2.000) -- (2.060,2.000) -- (2.080,2.000) -- (2.100,2.000) -- (2.120,2.000) -- (2.140,2.000) -- (2.160,2.000) -- (2.180,2.000) -- (2.200,2.000) -- (2.220,1.750) -- (2.240,1.750) -- (2.260,1.750) -- (2.280,1.750) -- (2.300,1.750) -- (2.320,1.750) -- (2.340,1.750) -- (2.360,1.750) -- (2.380,1.750) -- (2.400,1.750) -- (2.420,1.750) -- (2.440,1.750) -- (2.460,1.750) -- (2.480,1.500) -- (2.500,1.500) -- (2.520,1.500) -- (2.540,1.500) -- (2.560,1.500) -- (2.580,1.500) -- (2.600,1.500) -- (2.620,1.500) -- (2.640,1.500) -- (2.660,1.500) -- (2.680,1.500) -- (2.700,1.500) -- (2.720,1.500) -- (2.740,1.500) -- (2.760,1.500) -- (2.780,1.250) -- (2.800,1.250) -- (2.820,1.250) -- (2.840,1.250) -- (2.860,1.250) -- (2.880,1.250) -- (2.900,1.250) -- (2.920,1.250) -- (2.940,1.250) -- (2.960,1.250) -- (2.980,1.250) -- (3.000,1.250) -- (3.020,1.250) -- (3.040,1.250) -- (3.060,1.250) -- (3.080,1.250) -- (3.100,1.250) -- (3.120,1.250) -- (3.140,1.250) -- (3.160,1.000) -- (3.180,1.000) -- (3.200,1.000) -- (3.220,1.000) -- (3.240,1.000) -- (3.260,1.000) -- (3.280,1.000) -- (3.300,1.000) -- (3.320,1.000) -- (3.340,1.000) -- (3.360,1.000) -- (3.380,1.000) -- (3.400,1.000) -- (3.420,1.000) -- (3.440,1.000) -- (3.460,1.000) -- (3.480,1.000) -- (3.500,1.000) -- (3.520,1.000) -- (3.540,1.000) -- (3.560,1.000) -- (3.580,1.000) -- (3.600,1.000) -- (3.620,1.000) -- (3.640,1.000) -- (3.660,1.000) -- (3.680,1.000) -- (3.700,1.000) -- (3.720,1.000) -- (3.740,1.000) -- (3.760,1.250) -- (3.780,1.250) -- (3.800,1.250) -- (3.820,1.250) -- (3.840,1.250) -- (3.860,1.250) -- (3.880,1.250) -- (3.900,1.250) -- (3.920,1.250) -- (3.940,1.250) -- (3.960,1.250) -- (3.980,1.250) -- (4.000,1.250) -- (4.020,1.250) -- (4.040,1.250) -- (4.060,1.250) -- (4.080,1.250) -- (4.100,1.250) -- (4.120,1.500) -- (4.140,1.500) -- (4.160,1.500) -- (4.180,1.500) -- (4.200,1.500) -- (4.220,1.500) -- (4.240,1.500) -- (4.260,1.500) -- (4.280,1.500) -- (4.300,1.500) -- (4.320,1.500) -- (4.340,1.500) -- (4.360,1.750) -- (4.380,1.750) -- (4.400,1.750) -- (4.420,1.750) -- (4.440,1.750) -- (4.460,1.750) -- (4.480,1.750) -- (4.500,1.750) -- (4.520,1.750) -- (4.540,2.000) -- (4.560,2.000) -- (4.580,2.000) -- (4.600,2.000) -- (4.620,2.000) -- (4.640,2.000) -- (4.660,2.000) -- (4.680,2.000) -- (4.700,2.000) -- (4.720,2.000) -- (4.740,2.250) -- (4.760,2.250) -- (4.780,2.250) -- (4.800,2.250) -- (4.820,2.250) -- (4.840,2.250) -- (4.860,2.250) -- (4.880,2.250) -- (4.900,2.500) -- (4.920,2.500) -- (4.940,2.500) -- (4.960,2.500) -- (4.980,2.500) -- (5.000,2.500);
\node[lab, text=accent] at (4.3,0.9) {$f_2$};
\node[lab] at (4.3,2.9) {$f$};
\end{tikzpicture}
\end{center}
```

The Lebesgue integral slices the range: $f_n=2^{-n}\lfloor2^nf\rfloor$ (here $n=2$, levels $k/4$) is a simple function below $f$, constant on the measurable sets where $f$ lies between two levels; $\mu(f_n)\uparrow\mu(f)$.

:::

For simple $f$ the two definitions agree, by monotonicity for simple functions. The integral is monotone: $0\le f\le h$ implies $\mu(f)\le\mu(h)$, since every simple $g\le f$ is also $\le h$.

::: {#thm-monotone-convergence-integral .theorem name="Monotone convergence theorem"}

Let $f_n,f:E\to[0,\infty]$ be measurable with $f_n\uparrow f$ pointwise. Then

$$
\mu(f_n)\uparrow\mu(f).
$$

:::

::: {.proof}

1. By monotonicity $\mu(f_n)$ increases to a limit $M\le\mu(f)$. It remains to show $\mu(g)\le M$ for every simple $g=\sum_ka_k\mathbf 1_{A_k}\le f$.

2. Fix $t\in(0,1)$ and let $E_n=\{f_n\ge tg\}$. These sets are measurable and increase, and $\bigcup_nE_n=E$: where $g(x)=0$ every $n$ works, and where $g(x)>0$ we have $f_n(x)\uparrow f(x)\ge g(x)>tg(x)$.

3. $tg\mathbf 1_{E_n}$ is simple and $\le f_n$, so
$$M\ge\mu(f_n)\ge\mu(tg\mathbf 1_{E_n})=t\sum_ka_k\,\mu(A_k\cap E_n).$$

4. Let $n\to\infty$: by continuity from below $\mu(A_k\cap E_n)\uparrow\mu(A_k)$, so $M\ge t\mu(g)$. Let $t\uparrow1$.

:::

Combined with @prp-dyadic-approximation, monotone convergence says $\mu(f)=\lim_n\mu(f_n)$ for the dyadic simple approximations $f_n\uparrow f$; integrals can be computed along any increasing sequence of simple functions.

::: {#thm-integral-linear-monotone .theorem name="Linearity and positivity"}

1. For measurable $f,h\ge0$ and $\alpha,\beta\ge0$: $\mu(\alpha f+\beta h)=\alpha\mu(f)+\beta\mu(h)$.
2. For integrable $f,h$ and $\alpha,\beta\in\mathbb R$: $\alpha f+\beta h$ is integrable, $\mu(\alpha f+\beta h)=\alpha\mu(f)+\beta\mu(h)$, and $f\le h$ implies $\mu(f)\le\mu(h)$.
3. For measurable $f\ge0$: $\mu(f)=0$ if and only if $f=0$ a.e. Consequently, integrable functions that are equal a.e. have equal integrals.

:::

::: {.proof}

1. Take simple $f_n\uparrow f$ and $h_n\uparrow h$ (@prp-dyadic-approximation). Then $\alpha f_n+\beta h_n$ is simple and increases to $\alpha f+\beta h$. Apply monotone convergence on both sides of the identity for simple functions.

2. $|\alpha f+\beta h|\le|\alpha||f|+|\beta||h|$, so part 1 and monotonicity give integrability. If $u=f+h$, then $u^+-u^-=f^+-f^-+h^+-h^-$, i.e. $u^++f^-+h^-=u^-+f^++h^+$; integrating with part 1 and rearranging (all terms finite) gives $\mu(u)=\mu(f)+\mu(h)$. Scaling by $\alpha<0$ swaps $f^+$ and $f^-$. If $f\le h$, then $\mu(h)-\mu(f)=\mu(h-f)\ge0$.

3. If $f=0$ a.e., every simple $g\le f$ is $0$ off a null set, so $\mu(g)=0$. Conversely, if $\mu(\{f>0\})>0$, then $\{f>0\}=\bigcup_n\{f>\tfrac1n\}$ gives some $n$ with $\mu(\{f>\tfrac1n\})>0$, and $\mu(f)\ge\tfrac1n\mu(\{f>\tfrac1n\})>0$. For integrable $f=h$ a.e., apply this to $|f-h|$ and use $|\mu(f)-\mu(h)|\le\mu(|f-h|)$.

:::

::: {#cor-series-nonnegative-integral .corollary name="Integrating series term by term"}

For measurable $g_n\ge0$, $\displaystyle\mu\Big(\sum_{n=1}^\infty g_n\Big)=\sum_{n=1}^\infty\mu(g_n)$.

:::

::: {.proof}

The partial sums increase to the full sum. Apply part 1 of @thm-integral-linear-monotone to each partial sum and monotone convergence to the limit.

:::

::: {#prp-integral-pi-system .proposition name="Integrals over a generating π-system"}

Let $\mathcal A$ be a π-system with $E\in\mathcal A$ and $\sigma(\mathcal A)=\mathcal E$, and $f$ integrable with $\mu(f\mathbf 1_A)=0$ for all $A\in\mathcal A$. Then $f=0$ a.e.

:::

::: {.proof}

1. The sets $A$ with $\mu(f\mathbf 1_A)=0$ form a d-system: differences by linearity; increasing unions $A_n\uparrow A$ because $\mu(f\mathbf 1_{A_n})=\mu(f^+\mathbf 1_{A_n})-\mu(f^-\mathbf 1_{A_n})$ and both terms converge, by monotone convergence, to the finite numbers $\mu(f^\pm\mathbf 1_A)$. By Dynkin's lemma it is all of $\mathcal E$.

2. Take $A=\{f>0\}$: then $f^+=f\mathbf 1_A$ has integral $0$, so $f^+=0$ a.e. by part 3 of @thm-integral-linear-monotone. Likewise $f^-=0$ a.e.

:::

## Riemann and Lebesgue

::: {#thm-riemann-is-lebesgue .theorem name="Riemann integrable functions are Lebesgue integrable"}

Let $f:[a,b]\to\mathbb R$ be Riemann integrable. Then $f$ is measurable for the completion of $\mathcal B([a,b])$, Lebesgue integrable, and

$$
\int_{[a,b]}f\,d\lambda=\int_a^bf(x)\,dx .
$$

:::

::: {.proof}

1. Choose dissections $D_1\subseteq D_2\subseteq\cdots$ of $[a,b]$ whose upper and lower sums satisfy $U(f,D_n)-L(f,D_n)\to0$ (@def-dissection-upper-lower-sums); refining only improves both.

2. Let $\phi_n$ and $\psi_n$ be the step functions equal on each open interval of $D_n$ to the infimum and supremum of $f$ there (and to $f$ at the finitely many division points). Then $\phi_n\le f\le\psi_n$, $\phi_n$ increases and $\psi_n$ decreases, and $\int\phi_n\,d\lambda=L(f,D_n)$, $\int\psi_n\,d\lambda=U(f,D_n)$, the end points being null.

3. Let $\phi=\lim\phi_n$ and $\psi=\lim\psi_n$, which are Borel with $\phi\le f\le\psi$. By monotone convergence applied to $\psi_1-\psi_n\uparrow\psi_1-\psi$ and $\phi_n-\phi_1\uparrow\phi-\phi_1$ (all bounded on a set of finite measure),
$$\int(\psi-\phi)\,d\lambda=\lim_n\big(U(f,D_n)-L(f,D_n)\big)=0 .$$

4. So $\psi=\phi$ a.e. by part 3 of @thm-integral-linear-monotone, and $f$ differs from the Borel function $\phi$ only on a subset of a null set. Its integral is $\int\phi\,d\lambda=\lim L(f,D_n)$, the Riemann integral.

:::

The converse fails: $\mathbf 1_{[0,1]\setminus\mathbb Q}$ is not Riemann integrable, but it is Lebesgue integrable with integral $\lambda([0,1]\setminus\mathbb Q)=1$. On unbounded domains the improper Riemann integral of $\sin x/x$ converges although the function is not Lebesgue integrable.

## Measures with a density

::: {#prp-density-measure .proposition name="Measure with a density"}

Let $f:E\to[0,\infty]$ be measurable. Then $\nu(A)=\mu(f\mathbf 1_A)$ defines a measure on $\mathcal E$, the measure with *density* $f$ with respect to $\mu$, and for every measurable $g\ge0$

$$
\nu(g)=\mu(fg).
$$

:::

::: {.proof}

1. $\nu(\emptyset)=0$. For disjoint $A_n$ with union $A$, $f\mathbf 1_A=\sum_nf\mathbf 1_{A_n}$, so $\nu(A)=\sum_n\nu(A_n)$ by @cor-series-nonnegative-integral.

2. For $g=\mathbf 1_A$ the formula is the definition; by linearity it holds for simple $g$; by monotone convergence, applied to simple $g_n\uparrow g$ and to $fg_n\uparrow fg$, it holds for all measurable $g\ge0$.

:::

Similarly, for an image measure $\nu=\mu\circ\phi^{-1}$ one has $\nu(g)=\mu(g\circ\phi)$, proved by the same three steps (indicator, simple, monotone limit). A random variable $X$ has a *density* $f$ when its law is the measure with density $f$ with respect to Lebesgue measure, which recovers @def-probability-density.
