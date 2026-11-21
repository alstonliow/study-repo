---
title: "Which Functions Are Integrable"
sources: [cama1-7]
requires: [math/analysis/real/integration/properties-of-the-integral, math/analysis/real/continuity/extreme-and-intermediate-values]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Section 7.1, in our own wording; proofs written out in steps. Uniform continuity is a starred (non-examinable) part of the source; it is kept as its own block because later courses use it constantly. -->

Riemann's criterion (@thm-riemann-criterion) reduces integrability to making $U_D(f)-L_D(f)$ small. This works for continuous functions, monotone functions, and functions that are badly behaved only at a few points.

## Continuous functions

::: {#def-uniform-continuity .definition name="Uniform continuity"}

$f:A\to\mathbb R$ is *uniformly continuous* if
$$\forall\varepsilon>0\ \exists\delta>0\ \forall x,y\in A\quad |x-y|<\delta\Rightarrow|f(x)-f(y)|<\varepsilon.$$

:::

::: {#fig-integrable-functions-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (4.6,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.2) -- (0,3.2) node[lab, above] {$y$};
\draw[emph] (0.200,3.000) -- (0.253,2.376) -- (0.305,1.967) -- (0.358,1.678) -- (0.410,1.463) -- (0.463,1.297) -- (0.515,1.165) -- (0.568,1.057) -- (0.620,0.968) -- (0.673,0.892) -- (0.725,0.828) -- (0.778,0.772) -- (0.830,0.723) -- (0.883,0.680) -- (0.935,0.642) -- (0.988,0.608) -- (1.040,0.577) -- (1.093,0.549) -- (1.145,0.524) -- (1.198,0.501) -- (1.250,0.480) -- (1.302,0.461) -- (1.355,0.443) -- (1.407,0.426) -- (1.460,0.411) -- (1.512,0.397) -- (1.565,0.383) -- (1.617,0.371) -- (1.670,0.359) -- (1.723,0.348) -- (1.775,0.338) -- (1.828,0.328) -- (1.880,0.319) -- (1.932,0.310) -- (1.985,0.302) -- (2.038,0.294) -- (2.090,0.287) -- (2.143,0.280) -- (2.195,0.273) -- (2.248,0.267) -- (2.300,0.261) -- (2.353,0.255) -- (2.405,0.249) -- (2.458,0.244) -- (2.510,0.239) -- (2.562,0.234) -- (2.615,0.229) -- (2.668,0.225) -- (2.720,0.221) -- (2.773,0.216) -- (2.825,0.212) -- (2.878,0.209) -- (2.930,0.205) -- (2.983,0.201) -- (3.035,0.198) -- (3.088,0.194) -- (3.140,0.191) -- (3.193,0.188) -- (3.245,0.185) -- (3.298,0.182) -- (3.350,0.179) -- (3.402,0.176) -- (3.455,0.174) -- (3.508,0.171) -- (3.560,0.169) -- (3.613,0.166) -- (3.665,0.164) -- (3.718,0.161) -- (3.770,0.159) -- (3.823,0.157) -- (3.875,0.155) -- (3.928,0.153) -- (3.980,0.151) -- (4.033,0.149) -- (4.085,0.147) -- (4.138,0.145) -- (4.190,0.143) -- (4.243,0.141) -- (4.295,0.140) -- (4.348,0.138) -- (4.400,0.136);
\draw[hl] (0.25,1.818) rectangle (0.33,2.400);
\draw[hl] (2.5,0.171) rectangle (3.5,0.240);
\node[lab, right] at (0.4,2.3) {tiny $\delta$ near $0$}; \node[lab, above] at (3.0,0.35) {wide $\delta$};
\end{tikzpicture}
\end{center}
```

$f(x)=1/x$ on $(0,1]$ is continuous but not uniformly continuous: for a fixed vertical tolerance (box height), the allowed width $\delta$ shrinks to $0$ near $x=0$. Uniform continuity asks for one $\delta$ that works everywhere.

:::

The difference from continuity (@def-continuity-epsilon-delta) is the order of quantifiers: here one $\delta$ must serve every point at once. $f(x)=1/x$ is continuous on $(0,1]$ but not uniformly continuous: near $0$, points within any fixed $\delta$ of each other can have values arbitrarily far apart.

::: {#thm-uniform-continuity-compact .theorem name="Continuous on a closed interval implies uniformly continuous"}

Every continuous $f:[a,b]\to\mathbb R$ is uniformly continuous.

:::

::: {.proof}

1. Suppose not. Then there is $\varepsilon>0$ such that for every $n$ there are $x_n,y_n\in[a,b]$ with $|x_n-y_n|<\frac1n$ and $|f(x_n)-f(y_n)|\ge\varepsilon$.

2. By @thm-bolzano-weierstrass some subsequence $x_{n_k}\to x$, and $x\in[a,b]$. Since $|x_{n_k}-y_{n_k}|<\frac1{n_k}$, also $y_{n_k}\to x$.

3. By continuity at $x$ (@thm-sequential-continuity), $f(x_{n_k})\to f(x)$ and $f(y_{n_k})\to f(x)$, so $f(x_{n_k})-f(y_{n_k})\to0$, contradicting $|f(x_{n_k})-f(y_{n_k})|\ge\varepsilon$.

:::

::: {#thm-continuous-integrable .theorem name="Continuous functions are integrable"}

Every continuous $f:[a,b]\to\mathbb R$ is Riemann integrable.

:::

::: {.proof}

1. Let $\varepsilon>0$. By @thm-uniform-continuity-compact there is $\delta>0$ with $|f(x)-f(y)|<\frac{\varepsilon}{b-a}$ whenever $|x-y|<\delta$.

2. Take a dissection $D$ of mesh less than $\delta$. On each subinterval $f$ attains its supremum and infimum (@thm-extreme-value-proof) at points less than $\delta$ apart, so $M_i-m_i<\frac\varepsilon{b-a}$.

3. Hence $U_D(f)-L_D(f)=\sum(x_i-x_{i-1})(M_i-m_i)<\frac{\varepsilon}{b-a}(b-a)=\varepsilon$, and @thm-riemann-criterion applies.

:::

So $\int_a^be^{-x^2}dx$ exists, although $e^{-x^2}$ has no elementary antiderivative.

## Monotone functions

::: {#thm-monotone-integrable .theorem name="Monotone functions are integrable"}

Every monotone $f:[a,b]\to\mathbb R$ is Riemann integrable.

:::

::: {.proof}

1. Say $f$ is increasing and $f(b)>f(a)$ (if $f(b)=f(a)$, $f$ is constant). Let $\varepsilon>0$ and take a dissection of mesh less than $\delta=\frac{\varepsilon}{f(b)-f(a)}$.

2. On $[x_{i-1},x_i]$, $M_i=f(x_i)$ and $m_i=f(x_{i-1})$. So
$$U_D(f)-L_D(f)=\sum_{i=1}^n(x_i-x_{i-1})\bigl(f(x_i)-f(x_{i-1})\bigr)<\delta\sum_{i=1}^n\bigl(f(x_i)-f(x_{i-1})\bigr)=\delta\bigl(f(b)-f(a)\bigr)=\varepsilon.$$

:::

::: {#fig-integrable-functions-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (5.6,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.2) -- (0,2.4) node[lab, above] {$y$};
\fill[hl cell] (0.20,0.370) rectangle (0.80,0.580);
\fill[hl cell] (4.6,0.370) rectangle (5.2,0.580);
\fill[hl cell] (0.80,0.580) rectangle (1.40,0.790);
\fill[hl cell] (4.6,0.580) rectangle (5.2,0.790);
\fill[hl cell] (1.40,0.790) rectangle (2.00,1.000);
\fill[hl cell] (4.6,0.790) rectangle (5.2,1.000);
\fill[hl cell] (2.00,1.000) rectangle (2.60,1.510);
\fill[hl cell] (4.6,1.000) rectangle (5.2,1.510);
\fill[hl cell] (2.60,1.510) rectangle (3.20,1.720);
\fill[hl cell] (4.6,1.510) rectangle (5.2,1.720);
\fill[hl cell] (3.20,1.720) rectangle (3.80,1.930);
\fill[hl cell] (4.6,1.720) rectangle (5.2,1.930);
\draw[emph] (0.200,0.370) -- (0.250,0.387) -- (0.300,0.405) -- (0.350,0.422) -- (0.400,0.440) -- (0.450,0.457) -- (0.500,0.475) -- (0.550,0.492) -- (0.600,0.510) -- (0.650,0.527) -- (0.700,0.545) -- (0.750,0.562) -- (0.800,0.580) -- (0.850,0.597) -- (0.900,0.615) -- (0.950,0.632) -- (1.000,0.650) -- (1.050,0.667) -- (1.100,0.685) -- (1.150,0.702) -- (1.200,0.720) -- (1.249,0.737) -- (1.299,0.755) -- (1.349,0.772) -- (1.399,0.790) -- (1.449,0.807) -- (1.499,0.825) -- (1.549,0.842) -- (1.599,0.860) -- (1.649,0.877) -- (1.699,0.895) -- (1.749,0.912) -- (1.799,0.930) -- (1.849,0.947) -- (1.899,0.965) -- (1.949,0.982) -- (1.999,1.000) -- (2.049,1.017) -- (2.099,1.035) -- (2.149,1.052) -- (2.199,1.070);
\draw[emph] (2.201,1.370) -- (2.241,1.384) -- (2.281,1.398) -- (2.321,1.412) -- (2.361,1.426) -- (2.401,1.440) -- (2.441,1.454) -- (2.481,1.468) -- (2.521,1.482) -- (2.561,1.496) -- (2.601,1.510) -- (2.641,1.524) -- (2.681,1.538) -- (2.721,1.552) -- (2.761,1.566) -- (2.801,1.580) -- (2.841,1.594) -- (2.881,1.608) -- (2.921,1.622) -- (2.961,1.636) -- (3.000,1.650) -- (3.040,1.664) -- (3.080,1.678) -- (3.120,1.692) -- (3.160,1.706) -- (3.200,1.720) -- (3.240,1.734) -- (3.280,1.748) -- (3.320,1.762) -- (3.360,1.776) -- (3.400,1.790) -- (3.440,1.804) -- (3.480,1.818) -- (3.520,1.832) -- (3.560,1.846) -- (3.600,1.860) -- (3.640,1.874) -- (3.680,1.888) -- (3.720,1.902) -- (3.760,1.916) -- (3.800,1.930);
\draw[->, faint] (4.0,1.0) -- (4.5,1.0); \node[lab, below] at (4.9,0.25) {$\delta$};\draw[faint] (0.200,-0.06) -- (0.200,0.06); \node[lab, tick, below] at (0.200,-0.05) {$a$};\draw[faint] (3.800,-0.06) -- (3.800,0.06); \node[lab, tick, below] at (3.800,-0.05) {$b$};
\end{tikzpicture}
\end{center}
```

For increasing $f$ with a dissection into pieces of width $\delta$, the boxes $U_D-L_D$ stack into one column of height $f(b)-f(a)$, so $U_D(f)-L_D(f)=\delta\,(f(b)-f(a))\to0$.

:::

A monotone function can have infinitely many jumps. For example, $f(0)=0$ and $f(x)=\frac1k$ on $\left(\frac1{2^{k}},\frac1{2^{k-1}}\right]$ is increasing on $[0,1]$ with a jump at every $\frac1{2^k}$, and is integrable by the theorem.

## Isolated bad points

::: {#thm-bounded-continuous-interior-integrable .theorem name="Bounded and continuous inside"}

If $f:[a,b]\to\mathbb R$ is bounded and continuous on $(a,b)$, then $f$ is integrable on $[a,b]$.

:::

::: {.proof}

1. Let $|f|\le C$ and $\varepsilon>0$. Choose $a<x_1<z<b$ with $x_1-a<\frac{\varepsilon}{8C}$ and $b-z<\frac\varepsilon{8C}$.

2. $f$ is continuous on $[x_1,z]$, hence integrable there (@thm-continuous-integrable), so some dissection $x_1<x_2<\cdots<x_{n-1}=z$ of $[x_1,z]$ has upper and lower sums differing by less than $\frac\varepsilon2$.

3. Add the points $a$ and $b$. The two end pieces each contribute at most $\frac{\varepsilon}{8C}\cdot2C=\frac\varepsilon4$ to $U-L$, since $M_i-m_i\le2C$. So $U_D(f)-L_D(f)<\frac\varepsilon4+\frac\varepsilon2+\frac\varepsilon4=\varepsilon$.

:::

::: {#cor-piecewise-continuous-integrable .corollary name="Piecewise continuous functions"}

A bounded function on $[a,b]$ that is continuous except at finitely many points is integrable.

:::

::: {.proof}

1. Split $[a,b]$ at the points of discontinuity into finitely many closed intervals, on whose interiors $f$ is continuous.

2. On each, $f$ is integrable by @thm-bounded-continuous-interior-integrable, so on $[a,b]$ by @thm-integral-additive.

:::

::: {#fig-integrable-functions-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (4.6,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.2) -- (0,2.2) node[lab, above] {$y$};
\draw[emph] (0.200,0.460) -- (0.223,0.467) -- (0.245,0.474) -- (0.268,0.480) -- (0.290,0.487) -- (0.312,0.494) -- (0.335,0.501) -- (0.358,0.507) -- (0.380,0.514) -- (0.402,0.521) -- (0.425,0.528) -- (0.448,0.534) -- (0.470,0.541) -- (0.493,0.548) -- (0.515,0.554) -- (0.538,0.561) -- (0.560,0.568) -- (0.583,0.575) -- (0.605,0.582) -- (0.628,0.588) -- (0.650,0.595) -- (0.673,0.602) -- (0.695,0.609) -- (0.718,0.615) -- (0.740,0.622) -- (0.762,0.629) -- (0.785,0.636) -- (0.808,0.642) -- (0.830,0.649) -- (0.853,0.656) -- (0.875,0.663) -- (0.897,0.669) -- (0.920,0.676) -- (0.942,0.683) -- (0.965,0.690) -- (0.988,0.696) -- (1.010,0.703) -- (1.033,0.710) -- (1.055,0.717) -- (1.078,0.723) -- (1.100,0.730) -- (1.123,0.737) -- (1.145,0.744) -- (1.167,0.750) -- (1.190,0.757) -- (1.212,0.764) -- (1.235,0.770) -- (1.258,0.777) -- (1.280,0.784) -- (1.302,0.791) -- (1.325,0.797) -- (1.347,0.804) -- (1.370,0.811) -- (1.393,0.818) -- (1.415,0.825) -- (1.438,0.831) -- (1.460,0.838) -- (1.483,0.845) -- (1.505,0.852) -- (1.528,0.858) -- (1.550,0.865) -- (1.573,0.872) -- (1.595,0.879) -- (1.617,0.885) -- (1.640,0.892) -- (1.662,0.899) -- (1.685,0.905) -- (1.708,0.912) -- (1.730,0.919) -- (1.752,0.926) -- (1.775,0.932) -- (1.797,0.939) -- (1.820,0.946) -- (1.843,0.953) -- (1.865,0.960) -- (1.887,0.966) -- (1.910,0.973) -- (1.932,0.980) -- (1.955,0.987) -- (1.978,0.993) -- (2.000,1.000);
\draw[emph] (2.000,1.200) -- (2.027,1.195) -- (2.055,1.189) -- (2.083,1.183) -- (2.110,1.178) -- (2.138,1.173) -- (2.165,1.167) -- (2.192,1.162) -- (2.220,1.156) -- (2.248,1.151) -- (2.275,1.145) -- (2.303,1.139) -- (2.330,1.134) -- (2.357,1.129) -- (2.385,1.123) -- (2.413,1.118) -- (2.440,1.112) -- (2.468,1.107) -- (2.495,1.101) -- (2.522,1.095) -- (2.550,1.090) -- (2.578,1.085) -- (2.605,1.079) -- (2.633,1.074) -- (2.660,1.068) -- (2.688,1.062) -- (2.715,1.057) -- (2.743,1.051) -- (2.770,1.046) -- (2.798,1.040) -- (2.825,1.035) -- (2.853,1.030) -- (2.880,1.024) -- (2.908,1.018) -- (2.935,1.013) -- (2.962,1.008) -- (2.990,1.002) -- (3.018,0.997) -- (3.045,0.991) -- (3.073,0.986) -- (3.100,0.980) -- (3.127,0.975) -- (3.155,0.969) -- (3.183,0.964) -- (3.210,0.958) -- (3.238,0.953) -- (3.265,0.947) -- (3.292,0.942) -- (3.320,0.936) -- (3.348,0.930) -- (3.375,0.925) -- (3.402,0.920) -- (3.430,0.914) -- (3.458,0.909) -- (3.485,0.903) -- (3.513,0.897) -- (3.540,0.892) -- (3.567,0.887) -- (3.595,0.881) -- (3.623,0.876) -- (3.650,0.870) -- (3.678,0.865) -- (3.705,0.859) -- (3.733,0.853) -- (3.760,0.848) -- (3.788,0.843) -- (3.815,0.837) -- (3.843,0.832) -- (3.870,0.826) -- (3.897,0.821) -- (3.925,0.815) -- (3.953,0.809) -- (3.980,0.804) -- (4.008,0.798) -- (4.035,0.793) -- (4.062,0.788) -- (4.090,0.782) -- (4.117,0.777) -- (4.145,0.771) -- (4.173,0.765) -- (4.200,0.760);
\node[hollow dot] at (2.000,1.000) {};\node[dot] at (2.000,1.200) {};\fill[hl cell] (1.85,0) rectangle (2.15,2.0);\draw[faint] (2.000,-0.06) -- (2.000,0.06); \node[lab, tick, below] at (2.000,-0.05) {jump};
\end{tikzpicture}
\end{center}
```

A jump costs little: a thin strip of width $\delta$ around it (orange) adds at most $2\sup\lvert f\rvert\cdot\delta$ to $U_D(f)-L_D(f)$, and $f$ is continuous on the rest.

:::

::: {#exm-integrable-functions-1 .example}

$f(x)=\sin(1/x)$ for $x\ne0$, $f(0)=0$, is integrable on $[-1,1]$: it is bounded by $1$ and discontinuous only at $0$, although it oscillates infinitely often near $0$. So is $g$ on $[0,2]$ with $g(x)=x$ for $x\le1$ and $g(x)=x^2+1$ for $x>1$, which jumps at $1$.

:::
