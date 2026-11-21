---
title: "Limits of Functions and Differentiability"
sources: [cama1-5, mit1801-5]
requires: [math/analysis/real/continuity/extreme-and-intermediate-values, math/calculus/single-variable/differentiation/differentiation-rules]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Sections 5.1, 5.2 and 5.4, in our own wording; proofs written out in steps. The derivative and the rules of differentiation, with proofs, are in @sec-math-calculus-single-variable-differentiation-derivative, @sec-math-calculus-single-variable-differentiation-differentiation-rules and @sec-math-calculus-single-variable-differentiation-chain-rule; this note adds the little-o view of the derivative and the differentiability of inverse functions. Merged 2026-11-20 (owner): "Derivative of an inverse" from MIT 18.01 Lecture 5 (former id thm-inverse-function-derivative) was removed; @thm-inverse-differentiable is the single version, and its chain-rule proof (from 18.01) is kept after it. -->

## Limits of functions

For $A\subseteq\mathbb R$ and $f:A\to\mathbb R$, $\lim_{x\to a}f(x)=\ell$ is defined as in @def-limit-of-a-function, with $x$ restricted to $A$: for every $\varepsilon>0$ there is $\delta>0$ with $|f(x)-\ell|<\varepsilon$ for all $x\in A$ with $0<|x-a|<\delta$. The condition $0<|x-a|$ means the value at $a$, if there is one, plays no part. For example, if $f(x)=x$ for $x\ne2$ and $f(2)=3$, then $\lim_{x\to2}f(x)=2\ne f(2)$.

Comparing with @def-continuity-epsilon-delta: $f(x)\to\ell$ as $x\to a$ exactly when the function equal to $f$ away from $a$ and to $\ell$ at $a$ is continuous at $a$. So @thm-sequential-continuity gives:

::: {#thm-sequential-limit .theorem name="Limits through sequences"}

$\lim_{x\to a}f(x)=\ell$ if and only if $f(x_n)\to\ell$ for every sequence $(x_n)$ in $A\setminus\{a\}$ with $x_n\to a$.

:::

::: {#fig-differentiability-and-inverses-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (4.6,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.2) -- (0,2.2) node[lab, above] {$y$};
\draw[emph] (0.200,0.538) -- (0.251,0.572) -- (0.302,0.605) -- (0.354,0.636) -- (0.405,0.666) -- (0.456,0.695) -- (0.508,0.722) -- (0.559,0.747) -- (0.610,0.771) -- (0.661,0.792) -- (0.712,0.812) -- (0.764,0.829) -- (0.815,0.844) -- (0.866,0.857) -- (0.917,0.868) -- (0.969,0.877) -- (1.020,0.884) -- (1.071,0.890) -- (1.123,0.893) -- (1.174,0.895) -- (1.225,0.895) -- (1.276,0.894) -- (1.327,0.892) -- (1.379,0.889) -- (1.430,0.885) -- (1.481,0.880) -- (1.532,0.875) -- (1.584,0.870) -- (1.635,0.865) -- (1.686,0.860) -- (1.737,0.856) -- (1.789,0.852) -- (1.840,0.849) -- (1.891,0.848) -- (1.942,0.847) -- (1.994,0.848) -- (2.045,0.851) -- (2.096,0.855) -- (2.147,0.861) -- (2.199,0.869) -- (2.250,0.879) -- (2.301,0.892) -- (2.353,0.906) -- (2.404,0.922) -- (2.455,0.940) -- (2.506,0.961) -- (2.558,0.983) -- (2.609,1.008) -- (2.660,1.034) -- (2.711,1.062) -- (2.762,1.091) -- (2.814,1.122) -- (2.865,1.154) -- (2.916,1.188) -- (2.967,1.222) -- (3.019,1.257) -- (3.070,1.292) -- (3.121,1.328) -- (3.172,1.364) -- (3.224,1.400) -- (3.275,1.435) -- (3.326,1.470) -- (3.377,1.504) -- (3.429,1.537) -- (3.480,1.569) -- (3.531,1.600) -- (3.582,1.629) -- (3.634,1.657) -- (3.685,1.683) -- (3.736,1.706) -- (3.788,1.729) -- (3.839,1.749) -- (3.890,1.766) -- (3.941,1.782) -- (3.992,1.796) -- (4.044,1.808) -- (4.095,1.817) -- (4.146,1.825) -- (4.197,1.831) -- (4.249,1.835) -- (4.300,1.837);
\node[hollow dot] at (2.400,0.921) {};
\node[hl dot] at (3.800,1.734) {};\node[hl dot] at (3.800,0.000) {};
\node[hl dot] at (1.500,0.878) {};\node[hl dot] at (1.500,0.000) {};
\node[hl dot] at (2.950,1.210) {};\node[hl dot] at (2.950,0.000) {};
\node[hl dot] at (2.080,0.854) {};\node[hl dot] at (2.080,0.000) {};
\node[hl dot] at (2.580,0.994) {};\node[hl dot] at (2.580,0.000) {};
\draw[faint] (2.400,-0.06) -- (2.400,0.06); \node[lab, tick, below] at (2.400,-0.05) {$a$};\draw[faint] (-0.06,0.921) -- (0.06,0.921); \node[lab, tick, left] at (-0.05,0.921) {$\ell$};
\end{tikzpicture}
\end{center}
```

$\lim_{x\to a}f(x)=\ell$ exactly when $f(x_n)\to\ell$ for every sequence $x_n\to a$ with $x_n\ne a$ (orange points on the axis and on the graph).

:::

Consequently the limit laws for functions (@prp-limit-laws-functions) follow from those for sequences.

## The derivative as a linear approximation

::: {#def-little-o .definition name="Little-o notation"}

$o(h)$ denotes any function $\varepsilon(h)\,h$ with $\varepsilon(h)\to0$ as $h\to0$; that is, a quantity $r(h)$ with
$$\frac{r(h)}{h}\to0\quad\text{as }h\to0.$$

:::

::: {#prp-derivative-little-o .proposition name="Derivative as a linear approximation"}

$f$ is differentiable at $x$ with derivative $\lambda$ (@def-derivative) if and only if
$$f(x+h)=f(x)+\lambda h+o(h).$$

:::

::: {.proof}

1. Put $r(h)=f(x+h)-f(x)-\lambda h$ for $h\ne0$. Then $\dfrac{r(h)}{h}=\dfrac{f(x+h)-f(x)}{h}-\lambda$.

2. So $r(h)/h\to0$ exactly when the difference quotient tends to $\lambda$.

:::

::: {#fig-differentiability-and-inverses-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (3.6,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.2) -- (0,2.6) node[lab, above] {$y$};
\draw[emph] (0.000,0.300) -- (0.040,0.300) -- (0.080,0.302) -- (0.120,0.304) -- (0.160,0.306) -- (0.200,0.310) -- (0.240,0.314) -- (0.280,0.320) -- (0.320,0.326) -- (0.360,0.332) -- (0.400,0.340) -- (0.440,0.348) -- (0.480,0.358) -- (0.520,0.368) -- (0.560,0.378) -- (0.600,0.390) -- (0.640,0.402) -- (0.680,0.416) -- (0.720,0.430) -- (0.760,0.444) -- (0.800,0.460) -- (0.840,0.476) -- (0.880,0.494) -- (0.920,0.512) -- (0.960,0.530) -- (1.000,0.550) -- (1.040,0.570) -- (1.080,0.592) -- (1.120,0.614) -- (1.160,0.636) -- (1.200,0.660) -- (1.240,0.684) -- (1.280,0.710) -- (1.320,0.736) -- (1.360,0.762) -- (1.400,0.790) -- (1.440,0.818) -- (1.480,0.848) -- (1.520,0.878) -- (1.560,0.908) -- (1.600,0.940) -- (1.640,0.972) -- (1.680,1.006) -- (1.720,1.040) -- (1.760,1.074) -- (1.800,1.110) -- (1.840,1.146) -- (1.880,1.184) -- (1.920,1.222) -- (1.960,1.260) -- (2.000,1.300) -- (2.040,1.340) -- (2.080,1.382) -- (2.120,1.424) -- (2.160,1.466) -- (2.200,1.510) -- (2.240,1.554) -- (2.280,1.600) -- (2.320,1.646) -- (2.360,1.692) -- (2.400,1.740) -- (2.440,1.788) -- (2.480,1.838) -- (2.520,1.888) -- (2.560,1.938) -- (2.600,1.990) -- (2.640,2.042) -- (2.680,2.096) -- (2.720,2.150) -- (2.760,2.204) -- (2.800,2.260) -- (2.840,2.316) -- (2.880,2.374) -- (2.920,2.432) -- (2.960,2.490) -- (3.000,2.550) -- (3.040,2.610) -- (3.080,2.672) -- (3.120,2.734) -- (3.160,2.796) -- (3.200,2.860);
\draw[hl] (0.200,-0.050) -- (0.238,-0.024) -- (0.275,0.002) -- (0.312,0.029) -- (0.350,0.055) -- (0.388,0.081) -- (0.425,0.108) -- (0.463,0.134) -- (0.500,0.160) -- (0.538,0.186) -- (0.575,0.213) -- (0.613,0.239) -- (0.650,0.265) -- (0.688,0.291) -- (0.725,0.318) -- (0.762,0.344) -- (0.800,0.370) -- (0.837,0.396) -- (0.875,0.422) -- (0.913,0.449) -- (0.950,0.475) -- (0.988,0.501) -- (1.025,0.527) -- (1.062,0.554) -- (1.100,0.580) -- (1.137,0.606) -- (1.175,0.633) -- (1.212,0.659) -- (1.250,0.685) -- (1.287,0.711) -- (1.325,0.737) -- (1.363,0.764) -- (1.400,0.790) -- (1.438,0.816) -- (1.475,0.842) -- (1.512,0.869) -- (1.550,0.895) -- (1.587,0.921) -- (1.625,0.948) -- (1.662,0.974) -- (1.700,1.000) -- (1.738,1.026) -- (1.775,1.052) -- (1.812,1.079) -- (1.850,1.105) -- (1.887,1.131) -- (1.925,1.157) -- (1.962,1.184) -- (2.000,1.210) -- (2.038,1.236) -- (2.075,1.263) -- (2.113,1.289) -- (2.150,1.315) -- (2.188,1.341) -- (2.225,1.368) -- (2.263,1.394) -- (2.300,1.420) -- (2.338,1.446) -- (2.375,1.472) -- (2.413,1.499) -- (2.450,1.525) -- (2.488,1.551) -- (2.525,1.578) -- (2.562,1.604) -- (2.600,1.630) -- (2.638,1.656) -- (2.675,1.683) -- (2.713,1.709) -- (2.750,1.735) -- (2.788,1.761) -- (2.825,1.788) -- (2.863,1.814) -- (2.900,1.840) -- (2.938,1.866) -- (2.975,1.893) -- (3.013,1.919) -- (3.050,1.945) -- (3.088,1.971) -- (3.125,1.998) -- (3.163,2.024) -- (3.200,2.050);
\node[dot] at (1.400,0.790) {};\node[dot] at (2.700,2.123) {};
\draw[dashed] (2.7,1.700) -- node[lab, right] {$o(h)$} (2.7,2.123);
\draw[faint, dashed] (1.4,0.790) -- (2.7,0.790) node[lab, tick, below, midway] {$h$};
\draw[faint] (1.400,-0.06) -- (1.400,0.06); \node[lab, tick, below] at (1.400,-0.05) {$a$};\draw[faint] (2.700,-0.06) -- (2.700,0.06); \node[lab, tick, below] at (2.700,-0.05) {$a+h$};
\end{tikzpicture}
\end{center}
```

$f(a+h)=f(a)+f'(a)h+o(h)$: the tangent line (orange) is the linear part, and the gap to the graph is small even compared with $h$.

:::

The line $f(x)+\lambda h$ is the best linear approximation to $f$ near $x$: any other slope leaves an error that is not $o(h)$. The rules of differentiation become short calculations with the conventions $o(h)+o(h)=o(h)$, $c\cdot o(h)=o(h)$ for a bounded factor $c$, and $h\cdot h=o(h)$. For example, the product rule:
$$f(x+h)g(x+h)=\bigl(f(x)+hf'(x)+o(h)\bigr)\bigl(g(x)+hg'(x)+o(h)\bigr)=f(x)g(x)+h\bigl(f'(x)g(x)+f(x)g'(x)\bigr)+o(h).$$
The same view generalises directly to functions of several variables, where the derivative is a linear map (@sec-math-calculus-multivariable-differentiation-differentials-and-chain-rule).

*Higher derivatives* are defined recursively: $f$ is $(n+1)$ times differentiable if it is $n$ times differentiable and its $n$-th derivative $f^{(n)}$ is differentiable; then $f^{(n+1)}=(f^{(n)})'$.

## Inverse functions

::: {#thm-inverse-differentiable .theorem name="Differentiability of the inverse"}

Let $f:[a,b]\to[c,d]$ be continuous, strictly increasing, with $f(a)=c$, $f(b)=d$, differentiable on $(a,b)$ with $f'$ never $0$ there. Then the inverse $g$ is differentiable at every $y\in(c,d)$, and
$$g'(y)=\frac1{f'(g(y))}.$$

:::

::: {.proof}

1. $g$ exists and is continuous by @thm-continuous-inverse. Fix $y\in(c,d)$, let $x=g(y)$, and for small $k\ne0$ let $h=h(k)=g(y+k)-x$.

2. Since $g$ is injective, $h\ne0$; and $f(x+h)=y+k$, so $k=f(x+h)-f(x)$. Hence
$$\frac{g(y+k)-g(y)}{k}=\frac{h}{f(x+h)-f(x)}=\left(\frac{f(x+h)-f(x)}{h}\right)^{-1}.$$

3. As $k\to0$, $h(k)\to0$ because $g$ is continuous at $y$. So the bracket tends to $f'(x)\ne0$ (@thm-sequential-limit), and its reciprocal to $1/f'(x)$.

:::

::: {#fig-differentiability-and-inverses-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (3.0,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.2) -- (0,3.0) node[lab, above] {$y$};
\draw[faint, dashed] (0,0) -- (2.8,2.8) node[lab, right] {$y=x$};
\draw[emph] (0.000,0.000) -- (0.028,0.008) -- (0.055,0.017) -- (0.083,0.025) -- (0.110,0.033) -- (0.138,0.042) -- (0.165,0.050) -- (0.193,0.059) -- (0.220,0.068) -- (0.247,0.077) -- (0.275,0.086) -- (0.303,0.095) -- (0.330,0.104) -- (0.358,0.114) -- (0.385,0.124) -- (0.412,0.134) -- (0.440,0.145) -- (0.468,0.156) -- (0.495,0.167) -- (0.523,0.178) -- (0.550,0.190) -- (0.578,0.202) -- (0.605,0.215) -- (0.633,0.228) -- (0.660,0.241) -- (0.688,0.255) -- (0.715,0.269) -- (0.743,0.284) -- (0.770,0.299) -- (0.798,0.315) -- (0.825,0.332) -- (0.853,0.349) -- (0.880,0.366) -- (0.908,0.384) -- (0.935,0.403) -- (0.963,0.422) -- (0.990,0.443) -- (1.018,0.463) -- (1.045,0.485) -- (1.073,0.507) -- (1.100,0.530) -- (1.127,0.553) -- (1.155,0.578) -- (1.183,0.603) -- (1.210,0.629) -- (1.238,0.656) -- (1.265,0.683) -- (1.292,0.712) -- (1.320,0.741) -- (1.348,0.771) -- (1.375,0.802) -- (1.403,0.835) -- (1.430,0.868) -- (1.458,0.902) -- (1.485,0.937) -- (1.513,0.973) -- (1.540,1.010) -- (1.568,1.048) -- (1.595,1.087) -- (1.623,1.127) -- (1.650,1.169) -- (1.678,1.211) -- (1.705,1.255) -- (1.733,1.300) -- (1.760,1.346) -- (1.788,1.393) -- (1.815,1.441) -- (1.843,1.491) -- (1.870,1.542) -- (1.898,1.594) -- (1.925,1.647) -- (1.953,1.702) -- (1.980,1.758) -- (2.008,1.816) -- (2.035,1.875) -- (2.062,1.935) -- (2.090,1.996) -- (2.118,2.059) -- (2.145,2.124) -- (2.173,2.190) -- (2.200,2.257);
\draw[hl] (0.000,0.000) -- (0.009,0.029) -- (0.017,0.057) -- (0.026,0.086) -- (0.035,0.115) -- (0.044,0.144) -- (0.053,0.172) -- (0.062,0.201) -- (0.071,0.230) -- (0.080,0.259) -- (0.090,0.287) -- (0.100,0.316) -- (0.110,0.345) -- (0.120,0.374) -- (0.131,0.402) -- (0.141,0.431) -- (0.153,0.460) -- (0.164,0.489) -- (0.176,0.517) -- (0.188,0.546) -- (0.201,0.575) -- (0.214,0.604) -- (0.228,0.632) -- (0.242,0.661) -- (0.256,0.690) -- (0.271,0.719) -- (0.287,0.747) -- (0.303,0.776) -- (0.320,0.805) -- (0.337,0.834) -- (0.355,0.863) -- (0.374,0.891) -- (0.393,0.920) -- (0.413,0.949) -- (0.433,0.977) -- (0.455,1.006) -- (0.477,1.035) -- (0.500,1.064) -- (0.523,1.092) -- (0.548,1.121) -- (0.573,1.150) -- (0.599,1.179) -- (0.626,1.208) -- (0.654,1.236) -- (0.683,1.265) -- (0.713,1.294) -- (0.744,1.323) -- (0.775,1.351) -- (0.808,1.380) -- (0.842,1.409) -- (0.877,1.437) -- (0.913,1.466) -- (0.950,1.495) -- (0.988,1.524) -- (1.027,1.552) -- (1.067,1.581) -- (1.109,1.610) -- (1.152,1.639) -- (1.196,1.667) -- (1.241,1.696) -- (1.287,1.725) -- (1.335,1.754) -- (1.384,1.782) -- (1.435,1.811) -- (1.486,1.840) -- (1.540,1.869) -- (1.594,1.897) -- (1.650,1.926) -- (1.707,1.955) -- (1.766,1.984) -- (1.826,2.013) -- (1.888,2.041) -- (1.951,2.070) -- (2.016,2.099) -- (2.083,2.127) -- (2.151,2.156) -- (2.220,2.185) -- (2.291,2.214) -- (2.364,2.242) -- (2.439,2.271) -- (2.515,2.300);
\node[dot] at (1.500,0.956) {};\node[hl dot] at (0.956,1.500) {};
\node[lab, below right] at (1.500,0.956) {$f$}; \node[lab, above left] at (0.956,1.500) {$f^{-1}$};
\end{tikzpicture}
\end{center}
```

The graph of $f^{-1}$ (orange) is the graph of $f$ reflected in $y=x$. Reflection swaps rise and run, so the slope at the mirrored point is $1/f'(x)$, which needs $f'(x)\ne0$.

:::

The theorem does not assume that $g$ is differentiable; it proves it. If $g$ is already known to be differentiable, the formula follows in one line by differentiating $f(g(y))=y$ with the chain rule (@thm-derivative-chain-rule): $f'(g(y))\,g'(y)=1$. In Leibniz notation, $\frac{dx}{dy}=\frac{1}{dy/dx}$. For example $x^{1/q}$ is the inverse of $x^q$ on $(0,\infty)$, so its derivative is $\frac{1}{q(x^{1/q})^{q-1}}=\frac1qx^{1/q-1}$; by the chain rule $x^{p/q}=(x^{1/q})^p$ then has derivative $\frac pqx^{p/q-1}$.

## Complex differentiability

::: {#def-complex-differentiable .definition name="Complex differentiability"}

$f:\mathbb C\to\mathbb C$ is *differentiable* at $z$ with derivative $f'(z)$ if
$$\lim_{h\to0}\frac{f(z+h)-f(z)}{h}=f'(z),$$
where now $h$ ranges over non-zero complex numbers; equivalently $f(z+h)=f(z)+hf'(z)+o(h)$.

:::

The sum, product, quotient and chain rules hold with the same proofs, and polynomials have the expected derivatives. But because $h$ may approach $0$ from every direction, the condition is much stronger than in the real case.

::: {#exm-differentiability-1 .example name="Conjugation is not differentiable"}

For $f(z)=\bar z$, $\dfrac{f(z+h)-f(z)}{h}=\dfrac{\bar h}{h}$, which is $1$ for real $h$ and $-1$ for purely imaginary $h$; so the limit does not exist, at any $z$. Geometrically, $z\mapsto\bar z$ is a linear map of $\mathbb R^2$ (a reflection), but the only $\mathbb C$-linear maps are $z\mapsto bz$, which rotate and scale.

Likewise $|z|$ is nowhere complex-differentiable: at $z\ne0$, differentiability of $|z|$ would make $|z|^2/z=\bar z$ differentiable by the product and quotient rules; at $z=0$ it fails already along the real axis.

:::
