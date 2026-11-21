---
title: "The Fundamental Theorem of Calculus, Rigorously"
sources: [cama1-7]
requires: [math/analysis/real/integration/integrable-functions, math/analysis/real/differentiability/taylors-theorem, math/calculus/single-variable/integrals/fundamental-theorem]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Section 7.1 (end), in our own wording; proofs written out in steps. The two fundamental theorems and substitution are in @sec-math-calculus-single-variable-integrals-fundamental-theorem, proved there with the Riemann-sum integral; here they rest on @def-riemann-integral-darboux, and the second needs only an integrable derivative. Substitution is not repeated: its proof there carries over once the theorems below are in place. The integral test (@thm-integral-test) and improper integrals (@def-improper-integral) likewise carry over, using @thm-monotone-integrable. -->

## Differentiating an integral

::: {#thm-ftc-continuous-integrand .theorem name="Fundamental theorem of calculus, part 1" related="thm-ftc-2"}

Let $f:[a,b]\to\mathbb R$ be continuous and $F(x)=\int_a^xf(t)\,dt$. Then $F$ is differentiable on $[a,b]$ (one-sided at the ends) and
$$F'(x)=f(x).$$

:::

::: {.proof}

1. $F$ is defined because $f$ is integrable on every $[a,x]$ (@thm-continuous-integrable). By @thm-integral-additive, for $h\ne0$ with $x+h\in[a,b]$,
$$\frac{F(x+h)-F(x)}h-f(x)=\frac1h\int_x^{x+h}\bigl(f(t)-f(x)\bigr)\,dt.$$

2. Let $\varepsilon>0$. By continuity at $x$ there is $\delta>0$ with $|f(t)-f(x)|<\varepsilon$ whenever $|t-x|<\delta$.

3. If $0<|h|<\delta$, every $t$ between $x$ and $x+h$ satisfies this, so by @prp-integral-monotone the right side of step 1 has modulus at most $\frac1{|h|}\cdot\varepsilon|h|=\varepsilon$.

:::

::: {#fig-fundamental-theorem-of-calculus-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (4.6,0) node[lab, right] {$t$};
\draw[->, faint] (0,-0.2) -- (0,2.0) node[lab, above] {};
\fill[tintA] (0.3,0) -- (0.300,0.860) -- (0.325,0.872) -- (0.350,0.885) -- (0.375,0.898) -- (0.400,0.910) -- (0.425,0.923) -- (0.450,0.935) -- (0.475,0.947) -- (0.500,0.959) -- (0.525,0.971) -- (0.550,0.983) -- (0.575,0.994) -- (0.600,1.005) -- (0.625,1.016) -- (0.650,1.027) -- (0.675,1.038) -- (0.700,1.048) -- (0.725,1.059) -- (0.750,1.069) -- (0.775,1.079) -- (0.800,1.088) -- (0.825,1.098) -- (0.850,1.107) -- (0.875,1.116) -- (0.900,1.124) -- (0.925,1.133) -- (0.950,1.141) -- (0.975,1.149) -- (1.000,1.156) -- (1.025,1.164) -- (1.050,1.171) -- (1.075,1.178) -- (1.100,1.184) -- (1.125,1.190) -- (1.150,1.196) -- (1.175,1.202) -- (1.200,1.207) -- (1.225,1.213) -- (1.250,1.217) -- (1.275,1.222) -- (1.300,1.226) -- (1.325,1.230) -- (1.350,1.234) -- (1.375,1.237) -- (1.400,1.240) -- (1.425,1.242) -- (1.450,1.245) -- (1.475,1.247) -- (1.500,1.249) -- (1.525,1.250) -- (1.550,1.251) -- (1.575,1.252) -- (1.600,1.253) -- (1.625,1.253) -- (1.650,1.253) -- (1.675,1.253) -- (1.700,1.252) -- (1.725,1.251) -- (1.750,1.250) -- (1.775,1.249) -- (1.800,1.247) -- (1.825,1.245) -- (1.850,1.243) -- (1.875,1.240) -- (1.900,1.237) -- (1.925,1.234) -- (1.950,1.231) -- (1.975,1.227) -- (2.000,1.223) -- (2.025,1.219) -- (2.050,1.215) -- (2.075,1.210) -- (2.100,1.206) -- (2.125,1.201) -- (2.150,1.195) -- (2.175,1.190) -- (2.200,1.184) -- (2.225,1.178) -- (2.250,1.172) -- (2.275,1.166) -- (2.300,1.160) -- (2.3,0) -- cycle;
\fill[hl cell] (2.3,0) -- (2.300,1.160) -- (2.370,1.141) -- (2.440,1.121) -- (2.510,1.100) -- (2.580,1.078) -- (2.650,1.055) -- (2.720,1.032) -- (2.790,1.008) -- (2.860,0.984) -- (2.930,0.960) -- (3.000,0.937) -- (3.0,0) -- cycle;
\draw[emph] (0.100,0.754) -- (0.153,0.782) -- (0.205,0.810) -- (0.258,0.838) -- (0.310,0.865) -- (0.363,0.892) -- (0.415,0.918) -- (0.468,0.944) -- (0.520,0.969) -- (0.573,0.993) -- (0.625,1.016) -- (0.677,1.039) -- (0.730,1.061) -- (0.782,1.082) -- (0.835,1.101) -- (0.887,1.120) -- (0.940,1.138) -- (0.993,1.154) -- (1.045,1.170) -- (1.097,1.184) -- (1.150,1.196) -- (1.203,1.208) -- (1.255,1.218) -- (1.308,1.227) -- (1.360,1.235) -- (1.413,1.241) -- (1.465,1.246) -- (1.518,1.250) -- (1.570,1.252) -- (1.623,1.253) -- (1.675,1.253) -- (1.728,1.251) -- (1.780,1.248) -- (1.833,1.244) -- (1.885,1.239) -- (1.938,1.233) -- (1.990,1.225) -- (2.042,1.216) -- (2.095,1.207) -- (2.148,1.196) -- (2.200,1.184) -- (2.253,1.172) -- (2.305,1.158) -- (2.357,1.144) -- (2.410,1.129) -- (2.462,1.114) -- (2.515,1.098) -- (2.568,1.082) -- (2.620,1.065) -- (2.673,1.047) -- (2.725,1.030) -- (2.778,1.012) -- (2.830,0.994) -- (2.883,0.977) -- (2.935,0.959) -- (2.988,0.941) -- (3.040,0.924) -- (3.093,0.906) -- (3.145,0.889) -- (3.198,0.873) -- (3.250,0.857) -- (3.302,0.842) -- (3.355,0.827) -- (3.408,0.813) -- (3.460,0.799) -- (3.513,0.787) -- (3.565,0.775) -- (3.618,0.765) -- (3.670,0.755) -- (3.723,0.746) -- (3.775,0.739) -- (3.828,0.732) -- (3.880,0.727) -- (3.933,0.723) -- (3.985,0.720) -- (4.037,0.718) -- (4.090,0.718) -- (4.143,0.719) -- (4.195,0.721) -- (4.247,0.725) -- (4.300,0.730);
\draw[faint] (0.300,-0.06) -- (0.300,0.06); \node[lab, tick, below] at (0.300,-0.05) {$a$};\draw[faint] (2.300,-0.06) -- (2.300,0.06); \node[lab, tick, below] at (2.300,-0.05) {$x$};\draw[faint] (3.000,-0.06) -- (3.000,0.06); \node[lab, tick, below] at (3.000,-0.05) {$x+h$};
\node[lab] at (1.35,0.4) {$F(x)$}; \node[lab, right] at (4.3,1.0) {$f$};
\end{tikzpicture}
\end{center}
```

$F(x)=\int_a^xf$: the strip $F(x+h)-F(x)$ (orange) is about $f(x)\,h$ when $f$ is continuous at $x$, so $F'(x)=f(x)$.

:::

Without continuity this can fail: for the step function $f=0$ on $[-1,0]$ and $f=1$ on $(0,1]$, $F(x)=\max(x,0)$ is not differentiable at $0$.

## Integrating a derivative

::: {#thm-ftc-integrable-derivative .theorem name="Fundamental theorem of calculus, part 2" related="thm-ftc-1"}

Let $f$ be differentiable on $[a,b]$ with $f'$ Riemann integrable. Then
$$\int_a^bf'(t)\,dt=f(b)-f(a).$$

:::

::: {.proof}

1. Let $D:a=x_0<\cdots<x_n=b$ be any dissection. Telescoping, $f(b)-f(a)=\sum_{i=1}^n\bigl(f(x_i)-f(x_{i-1})\bigr)$.

2. By the mean value theorem (@thm-mean-value), $f(x_i)-f(x_{i-1})=(x_i-x_{i-1})f'(u_i)$ for some $u_i\in(x_{i-1},x_i)$.

3. Since $m_i(f')\le f'(u_i)\le M_i(f')$, summing gives $L_D(f')\le f(b)-f(a)\le U_D(f')$.

4. This holds for every $D$, so $\underline\int f'\le f(b)-f(a)\le\overline\int f'$. As $f'$ is integrable, both ends equal $\int_a^bf'$.

:::

::: {#fig-fundamental-theorem-of-calculus-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (4.6,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.2) -- (0,2.6) node[lab, above] {$y$};
\draw[emph] (0.200,0.454) -- (0.250,0.492) -- (0.300,0.529) -- (0.350,0.565) -- (0.400,0.601) -- (0.450,0.636) -- (0.500,0.670) -- (0.550,0.704) -- (0.600,0.736) -- (0.650,0.767) -- (0.700,0.797) -- (0.750,0.826) -- (0.800,0.853) -- (0.850,0.879) -- (0.900,0.904) -- (0.950,0.927) -- (1.000,0.949) -- (1.050,0.970) -- (1.100,0.989) -- (1.150,1.007) -- (1.200,1.023) -- (1.250,1.039) -- (1.300,1.052) -- (1.350,1.065) -- (1.400,1.076) -- (1.450,1.086) -- (1.500,1.095) -- (1.550,1.102) -- (1.600,1.109) -- (1.650,1.115) -- (1.700,1.119) -- (1.750,1.123) -- (1.800,1.127) -- (1.850,1.130) -- (1.900,1.132) -- (1.950,1.134) -- (2.000,1.135) -- (2.050,1.137) -- (2.100,1.138) -- (2.150,1.139) -- (2.200,1.141) -- (2.250,1.142) -- (2.300,1.144) -- (2.350,1.146) -- (2.400,1.149) -- (2.450,1.153) -- (2.500,1.157) -- (2.550,1.162) -- (2.600,1.168) -- (2.650,1.175) -- (2.700,1.183) -- (2.750,1.192) -- (2.800,1.202) -- (2.850,1.214) -- (2.900,1.226) -- (2.950,1.240) -- (3.000,1.256) -- (3.050,1.272) -- (3.100,1.290) -- (3.150,1.310) -- (3.200,1.331) -- (3.250,1.353) -- (3.300,1.377) -- (3.350,1.402) -- (3.400,1.429) -- (3.450,1.456) -- (3.500,1.485) -- (3.550,1.515) -- (3.600,1.547) -- (3.650,1.579) -- (3.700,1.613) -- (3.750,1.647) -- (3.800,1.682) -- (3.850,1.718) -- (3.900,1.755) -- (3.950,1.792) -- (4.000,1.830) -- (4.050,1.868) -- (4.100,1.907) -- (4.150,1.945) -- (4.200,1.984);
\draw[hl] (0.3,0.529) -- (1.2,1.023); \draw[faint, dashed] (1.2,0.529) -- (1.2,1.023);
\draw[hl] (1.2,1.023) -- (2.0,1.135); \draw[faint, dashed] (2.0,1.023) -- (2.0,1.135);
\draw[hl] (2.0,1.135) -- (3.0,1.256); \draw[faint, dashed] (3.0,1.135) -- (3.0,1.256);
\draw[hl] (3.0,1.256) -- (4.0,1.830); \draw[faint, dashed] (4.0,1.256) -- (4.0,1.830);
\node[dot] at (0.300,0.529) {};
\node[dot] at (1.200,1.023) {};
\node[dot] at (2.000,1.135) {};
\node[dot] at (3.000,1.256) {};
\node[dot] at (4.000,1.830) {};\draw[faint] (0.300,-0.06) -- (0.300,0.06); \node[lab, tick, below] at (0.300,-0.05) {$a$};\draw[faint] (4.000,-0.06) -- (4.000,0.06); \node[lab, tick, below] at (4.000,-0.05) {$b$};
\end{tikzpicture}
\end{center}
```

$f(b)-f(a)$ is the sum of the rises over the pieces of a dissection; by the mean value theorem each rise is $f'(\xi_i)(x_i-x_{i-1})$, which lies between the lower and upper sums of $f'$.

:::

This does not assume $f'$ continuous, only integrable. The hypothesis cannot be dropped altogether: there are differentiable functions whose derivative is unbounded on $[a,b]$, hence not Riemann integrable. When $f'$ is continuous, part 1 gives a second proof: $G(x)=\int_a^xf'$ and $f$ have the same derivative, so they differ by a constant (@cor-sign-of-derivative), which is $-f(a)$.

::: {#thm-integration-by-parts-proof .theorem name="Integration by parts"}

If $f,g$ are differentiable on $[a,b]$ with $f',g'$ integrable, then
$$\int_a^bf(x)g'(x)\,dx=f(b)g(b)-f(a)g(a)-\int_a^bf'(x)g(x)\,dx.$$

:::

::: {.proof}

1. $f,g$ are continuous (@thm-differentiable-continuous), hence integrable, so $f'g$ and $fg'$ are integrable (@prp-integral-product) and so is their sum $(fg)'$ (@thm-integral-linear).

2. By @thm-ftc-integrable-derivative and linearity, $\int_a^bfg'+\int_a^bf'g=\int_a^b(fg)'=f(b)g(b)-f(a)g(a)$. Rearrange.

:::

::: {#fig-fundamental-theorem-of-calculus-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (2.8,0) node[lab, right] {$u$};
\draw[->, faint] (0,-0.2) -- (0,2.4) node[lab, above] {$v$};
\fill[tintA] (0.500,0.400) -- (0.540,0.401) -- (0.580,0.404) -- (0.620,0.409) -- (0.660,0.415) -- (0.700,0.424) -- (0.740,0.435) -- (0.780,0.447) -- (0.820,0.461) -- (0.860,0.478) -- (0.900,0.496) -- (0.940,0.516) -- (0.980,0.538) -- (1.020,0.562) -- (1.060,0.588) -- (1.100,0.616) -- (1.140,0.646) -- (1.180,0.677) -- (1.220,0.711) -- (1.260,0.747) -- (1.300,0.784) -- (1.340,0.823) -- (1.380,0.865) -- (1.420,0.908) -- (1.460,0.953) -- (1.500,1.000) -- (1.540,1.049) -- (1.580,1.100) -- (1.620,1.153) -- (1.660,1.207) -- (1.700,1.264) -- (1.740,1.323) -- (1.780,1.383) -- (1.820,1.445) -- (1.860,1.510) -- (1.900,1.576) -- (1.940,1.644) -- (1.980,1.714) -- (2.020,1.786) -- (2.060,1.860) -- (2.100,1.936) -- (2.100,0) -- (0.500,0) -- cycle;
\fill[tintB] (0.500,0.400) -- (0.540,0.401) -- (0.580,0.404) -- (0.620,0.409) -- (0.660,0.415) -- (0.700,0.424) -- (0.740,0.435) -- (0.780,0.447) -- (0.820,0.461) -- (0.860,0.478) -- (0.900,0.496) -- (0.940,0.516) -- (0.980,0.538) -- (1.020,0.562) -- (1.060,0.588) -- (1.100,0.616) -- (1.140,0.646) -- (1.180,0.677) -- (1.220,0.711) -- (1.260,0.747) -- (1.300,0.784) -- (1.340,0.823) -- (1.380,0.865) -- (1.420,0.908) -- (1.460,0.953) -- (1.500,1.000) -- (1.540,1.049) -- (1.580,1.100) -- (1.620,1.153) -- (1.660,1.207) -- (1.700,1.264) -- (1.740,1.323) -- (1.780,1.383) -- (1.820,1.445) -- (1.860,1.510) -- (1.900,1.576) -- (1.940,1.644) -- (1.980,1.714) -- (2.020,1.786) -- (2.060,1.860) -- (2.100,1.936) -- (0,1.936) -- (0,0.400) -- cycle;
\draw[emph] (0.500,0.400) -- (0.540,0.401) -- (0.580,0.404) -- (0.620,0.409) -- (0.660,0.415) -- (0.700,0.424) -- (0.740,0.435) -- (0.780,0.447) -- (0.820,0.461) -- (0.860,0.478) -- (0.900,0.496) -- (0.940,0.516) -- (0.980,0.538) -- (1.020,0.562) -- (1.060,0.588) -- (1.100,0.616) -- (1.140,0.646) -- (1.180,0.677) -- (1.220,0.711) -- (1.260,0.747) -- (1.300,0.784) -- (1.340,0.823) -- (1.380,0.865) -- (1.420,0.908) -- (1.460,0.953) -- (1.500,1.000) -- (1.540,1.049) -- (1.580,1.100) -- (1.620,1.153) -- (1.660,1.207) -- (1.700,1.264) -- (1.740,1.323) -- (1.780,1.383) -- (1.820,1.445) -- (1.860,1.510) -- (1.900,1.576) -- (1.940,1.644) -- (1.980,1.714) -- (2.020,1.786) -- (2.060,1.860) -- (2.100,1.936);
\node[lab] at (1.5,0.45) {$\int v\,du$}; \node[lab] at (0.45,1.25) {$\int u\,dv$};
\draw[faint] (-0.06,0.400) -- (0.06,0.400); \node[lab, tick, left] at (-0.05,0.400) {$v(a)$};\draw[faint] (-0.06,1.936) -- (0.06,1.936); \node[lab, tick, left] at (-0.05,1.936) {$v(b)$};\draw[faint] (0.500,-0.06) -- (0.500,0.06); \node[lab, tick, below] at (0.500,-0.05) {$u(a)$};\draw[faint] (2.100,-0.06) -- (2.100,0.06); \node[lab, tick, below] at (2.100,-0.05) {$u(b)$};
\end{tikzpicture}
\end{center}
```

Integration by parts as areas, for increasing $u$ and $v$: the two regions fill the big rectangle minus the small one, $\int u\,dv+\int v\,du=u(b)v(b)-u(a)v(a)$.

:::

Integration by parts is the product rule integrated; substitution (@thm-substitution-definite) is the chain rule integrated.

## Taylor's theorem with integral remainder

::: {#thm-taylor-integral-remainder .theorem name="Taylor's theorem with integral remainder"}

Let $f$ be $n+1$ times differentiable on $[a,b]$ with $f^{(n+1)}$ continuous. Then
$$f(b)=\sum_{k=0}^n\frac{(b-a)^k}{k!}f^{(k)}(a)+\int_a^b\frac{(b-t)^n}{n!}f^{(n+1)}(t)\,dt.$$

:::

::: {.proof}

1. *Induction on $n$.* For $n=0$ the claim is $f(b)=f(a)+\int_a^bf'$, which is @thm-ftc-integrable-derivative.

2. Assume the claim for $n-1$ (with $f$ now $n+1$ times continuously differentiable); its remainder is $\int_a^b\frac{(b-t)^{n-1}}{(n-1)!}f^{(n)}(t)\,dt$.

3. Integrate by parts (@thm-integration-by-parts-proof) with $u=f^{(n)}$ and $v=-\frac{(b-t)^n}{n!}$, so $v'=\frac{(b-t)^{n-1}}{(n-1)!}$:
$$\int_a^b\frac{(b-t)^{n-1}}{(n-1)!}f^{(n)}(t)\,dt=\Bigl[-\frac{(b-t)^n}{n!}f^{(n)}(t)\Bigr]_a^b+\int_a^b\frac{(b-t)^n}{n!}f^{(n+1)}(t)\,dt.$$

4. The bracket equals $\frac{(b-a)^n}{n!}f^{(n)}(a)$, the next term of the Taylor polynomial. Substituting into the case $n-1$ gives the case $n$.

:::

The form of the remainder is what repeated integration by parts produces, starting from $f(b)=f(a)+\int_a^bf'(t)\,dt$ and always integrating the polynomial factor as a power of $(b-t)$, so that the boundary term at $t=b$ vanishes. Since $\int_a^b\frac{(b-t)^n}{n!}dt=\frac{(b-a)^{n+1}}{(n+1)!}$, bounding $f^{(n+1)}$ between its minimum and maximum on $[a,b]$ and applying the intermediate value theorem to it recovers the Lagrange form (@thm-taylor-lagrange).
