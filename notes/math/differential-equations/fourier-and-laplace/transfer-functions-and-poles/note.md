---
title: "Transfer Functions and Poles"
sources: [mit1803-30, mit1803-31]
requires: [math/differential-equations/fourier-and-laplace/inverse-laplace-and-ivps]
status: draft
---

<!-- Added 2026-11-24 from MIT 18.03SC Differential Equations (Fall 2011), Sessions 30 (transfer and weight functions, Green's formula) and 31 (poles, amplitude response, the connection with the exponential response formula), in our own wording; examples are ours, checked in Python; proofs written out in steps. -->

In the Laplace picture a linear time-invariant system is a single function of $s$, its transfer function. Where that function blows up, its poles, decides stability and resonance.

::: {#def-transfer-function .definition name="Transfer function"}
The *transfer function* of $p(D)x=f$ is
$$
W(s)=\frac{1}{p(s)} .
$$
With rest initial conditions, $X(s)=W(s)F(s)$: the transform of the output is the transfer function times the transform of the input.
:::

::: {#prp-transfer-weight .proposition name="Transfer function and weight function"}
The transfer function is the Laplace transform of the unit impulse response: $W=\mathcal L(w)$. Consequently Green's formula $x=w*f$ holds.
:::

::: {.proof}
1. With $f=\delta$ we have $F=1$, so the response has transform $X=W\cdot1$; that response is $w$ by definition, so $\mathcal L(w)=W$.

2. For general $f$, $X=WF=\mathcal L(w)\mathcal L(f)=\mathcal L(w*f)$ by @thm-laplace-convolution-rule, and uniqueness of the inverse transform gives $x=w*f$ (@thm-greens-formula).
:::

::: {#def-pole .definition name="Pole"}
A *pole* of a rational function $F(s)$ in lowest terms is a root of its denominator. The *pole diagram* marks the poles in the complex $s$-plane. The poles of $W=1/p$ are the characteristic roots of the system.
:::

::: {#thm-poles-long-term .theorem name="Poles and long-term behaviour"}
Let $F$ be a proper rational function and $f=\mathcal L^{-1}(F)$. Then $f(t)\to0$ as $t\to\infty$ if and only if every pole of $F$ has negative real part. More precisely, the pole with the largest real part $a$ determines the growth rate: $f$ grows or decays like $t^je^{at}$.
:::

::: {.proof}
1. In partial fractions, a pole $r$ of order $k$ contributes terms $c_j/(s-r)^j$, $j\le k$, with $c_k\neq0$.

2. By @prp-laplace-uniqueness, these invert to $c_j\,t^{j-1}e^{rt}/(j-1)!$.

3. Each such term tends to $0$ exactly when $\operatorname{Re}r<0$; terms of different poles or different powers cannot cancel, being linearly independent functions.
:::

::: {#prp-amplitude-response-transfer .proposition name="Amplitude response from the transfer function"}
If the system is stable, its gain for the input $\cos\omega t$ is $|W(i\omega)|$ and its phase lag is $-\arg W(i\omega)$.
:::

::: {.proof}
1. This is @thm-sinusoidal-response with $1/p(i\omega)=W(i\omega)$.
:::

::: {#fig-transfer-functions-and-poles-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.8cm, y=1.2cm]
\draw[->] (0,0) -- (3.2,0) node[lab, right] {$\omega$};
\draw[->] (0,0) -- (0,2.5) node[lab, above] {$|W(i\omega)|$};
\draw[emph, primary] (0,1) -- (0.015,1) -- (0.03,1.001) -- (0.045,1.002) -- (0.06,1.003) -- (0.075,1.005) -- (0.09,1.007) -- (0.106,1.01) -- (0.121,1.013) -- (0.136,1.016) -- (0.151,1.02) -- (0.166,1.025) -- (0.181,1.029) -- (0.196,1.035) -- (0.211,1.04) -- (0.226,1.046) -- (0.241,1.053) -- (0.256,1.06) -- (0.271,1.068) -- (0.286,1.076) -- (0.302,1.085) -- (0.317,1.095) -- (0.332,1.105) -- (0.347,1.115) -- (0.362,1.126) -- (0.377,1.138) -- (0.392,1.151) -- (0.407,1.164) -- (0.422,1.179) -- (0.437,1.193) -- (0.452,1.209) -- (0.467,1.226) -- (0.482,1.243) -- (0.497,1.262) -- (0.513,1.281) -- (0.528,1.302) -- (0.543,1.323) -- (0.558,1.346) -- (0.573,1.369) -- (0.588,1.394) -- (0.603,1.42) -- (0.618,1.447) -- (0.633,1.476) -- (0.648,1.506) -- (0.663,1.536) -- (0.678,1.569) -- (0.693,1.602) -- (0.709,1.636) -- (0.724,1.672) -- (0.739,1.708) -- (0.754,1.745) -- (0.769,1.782) -- (0.784,1.819) -- (0.799,1.856) -- (0.814,1.892) -- (0.829,1.926) -- (0.844,1.958) -- (0.859,1.988) -- (0.874,2.014) -- (0.889,2.035) -- (0.905,2.052) -- (0.92,2.062) -- (0.935,2.066) -- (0.95,2.062) -- (0.965,2.052) -- (0.98,2.034) -- (0.995,2.01) -- (1.01,1.979) -- (1.025,1.941) -- (1.04,1.899) -- (1.055,1.853) -- (1.07,1.803) -- (1.085,1.751) -- (1.101,1.697) -- (1.116,1.642) -- (1.131,1.587) -- (1.146,1.532) -- (1.161,1.478) -- (1.176,1.425) -- (1.191,1.374) -- (1.206,1.324) -- (1.221,1.276) -- (1.236,1.23) -- (1.251,1.186) -- (1.266,1.143) -- (1.281,1.103) -- (1.296,1.064) -- (1.312,1.027) -- (1.327,0.991) -- (1.342,0.958) -- (1.357,0.926) -- (1.372,0.895) -- (1.387,0.866) -- (1.402,0.838) -- (1.417,0.812) -- (1.432,0.786) -- (1.447,0.762) -- (1.462,0.739) -- (1.477,0.717) -- (1.492,0.696) -- (1.508,0.676) -- (1.523,0.657) -- (1.538,0.638) -- (1.553,0.621) -- (1.568,0.604) -- (1.583,0.588) -- (1.598,0.572) -- (1.613,0.558) -- (1.628,0.543) -- (1.643,0.53) -- (1.658,0.516) -- (1.673,0.504) -- (1.688,0.492) -- (1.704,0.48) -- (1.719,0.469) -- (1.734,0.458) -- (1.749,0.447) -- (1.764,0.437) -- (1.779,0.427) -- (1.794,0.418) -- (1.809,0.409) -- (1.824,0.4) -- (1.839,0.392) -- (1.854,0.383) -- (1.869,0.375) -- (1.884,0.368) -- (1.899,0.36) -- (1.915,0.353) -- (1.93,0.346) -- (1.945,0.339) -- (1.96,0.333) -- (1.975,0.326) -- (1.99,0.32) -- (2.005,0.314) -- (2.02,0.308) -- (2.035,0.303) -- (2.05,0.297) -- (2.065,0.292) -- (2.08,0.287) -- (2.095,0.282) -- (2.111,0.277) -- (2.126,0.272) -- (2.141,0.267) -- (2.156,0.263) -- (2.171,0.259) -- (2.186,0.254) -- (2.201,0.25) -- (2.216,0.246) -- (2.231,0.242) -- (2.246,0.238) -- (2.261,0.234) -- (2.276,0.231) -- (2.291,0.227) -- (2.307,0.224) -- (2.322,0.22) -- (2.337,0.217) -- (2.352,0.214) -- (2.367,0.21) -- (2.382,0.207) -- (2.397,0.204) -- (2.412,0.201) -- (2.427,0.198) -- (2.442,0.196) -- (2.457,0.193) -- (2.472,0.19) -- (2.487,0.187) -- (2.503,0.185) -- (2.518,0.182) -- (2.533,0.18) -- (2.548,0.177) -- (2.563,0.175) -- (2.578,0.173) -- (2.593,0.17) -- (2.608,0.168) -- (2.623,0.166) -- (2.638,0.164) -- (2.653,0.162) -- (2.668,0.16) -- (2.683,0.158) -- (2.698,0.156) -- (2.714,0.154) -- (2.729,0.152) -- (2.744,0.15) -- (2.759,0.148) -- (2.774,0.146) -- (2.789,0.145) -- (2.804,0.143) -- (2.819,0.141) -- (2.834,0.139) -- (2.849,0.138) -- (2.864,0.136) -- (2.879,0.135) -- (2.894,0.133) -- (2.91,0.131) -- (2.925,0.13) -- (2.94,0.129) -- (2.955,0.127) -- (2.97,0.126) -- (2.985,0.124) -- (3,0.123);
\draw (0.935,0) -- (0.935,-0.08) node[below, lab, tick] {$\omega_r$};
\draw (0,1) -- (-0.08,1) node[left, lab, tick] {$1$};
\end{tikzpicture}
\end{center}
```

The amplitude response is the height of $|W|$ along the imaginary axis; it peaks near the imaginary part of the nearby pole.

:::

::: {#exm-pole-diagram .example name="Reading a pole diagram"}
For $x''+\tfrac12x'+x=f$, the poles of $W=1/(s^2+\tfrac12s+1)$ are $-\tfrac14\pm i\tfrac{\sqrt{15}}4\approx-0.25\pm0.97i$.

1. Both have negative real part, so the system is stable and its impulse response decays like $e^{-t/4}$.
2. They lie close to the imaginary axis near $\pm i$, so $|W(i\omega)|$ is large for $\omega$ near $1$: practical resonance, as found in @exm-practical-resonance.
:::

::: {#fig-transfer-functions-and-poles-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.5]
\draw[->] (-1.4,0) -- (0.8,0) node[lab, right] {$\operatorname{Re}s$};
\draw[->] (0,-1.5) -- (0,1.6) node[lab, above] {$\operatorname{Im}s$};
\node[lab, accent] at (-0.25,0.968) {$\times$}; \node[lab, accent] at (-0.25,-0.968) {$\times$};
\draw[faint, dashed] (-0.25,1.2) -- (-0.25,-1.2);
\node[lab, note, left] at (-0.3,1.2) {$-\tfrac14\pm i\tfrac{\sqrt{15}}4$};
\draw[hl] (0,0) -- (0,1.4);
\node[lab, note, accent, right] at (0.05,0.5) {$s=i\omega$};
\end{tikzpicture}
\end{center}
```

Pole diagram of $W=1/(s^2+\tfrac12s+1)$: two poles in the left half-plane, close to the imaginary axis near $\pm i$, where $|W(i\omega)|$ is evaluated.

:::
