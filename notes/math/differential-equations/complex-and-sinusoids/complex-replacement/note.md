---
title: "Complex Replacement, Gain and Phase Lag"
sources: [mit1803-8, mit1803-9]
requires: [math/differential-equations/complex-and-sinusoids/sinusoidal-functions, math/differential-equations/first-order/first-order-linear-equations]
status: draft
---

<!-- Added 2026-11-24 from MIT 18.03SC Differential Equations (Fall 2011), Sessions 8 and 9 (first-order constant-coefficient equations with exponential and sinusoidal input, complex replacement, gain and phase lag), in our own wording; examples are ours, checked in Python; proofs written out in steps. -->

A stable linear system driven by a sinusoid responds, after the transient dies out, with a sinusoid of the same frequency. Its amplitude is scaled by the *gain* and its phase is delayed by the *phase lag*; complex replacement computes both with one division.

::: {#def-complex-replacement .definition name="Complex replacement"}
To solve a real linear equation with real coefficients and input $B\cos\omega t$, solve instead the *complexified* equation with input $Be^{i\omega t}$ and take the real part of its solution. (For input $B\sin\omega t$ take the imaginary part.) This works because the real part of a solution of a linear equation with real coefficients solves the equation with the real part of the input.

```{=latex}
\begin{algorithm}
\caption{Complex replacement for $p(D)x=B\cos\omega t$}
\begin{algorithmic}
\INPUT real polynomial $p$, amplitude $B$, frequency $\omega$ with $p(i\omega)\neq0$
\STATE replace the input by $Be^{i\omega t}$
\STATE $z_p\gets Be^{i\omega t}/p(i\omega)$ \COMMENT{exponential response formula}
\STATE write $p(i\omega)=|p(i\omega)|e^{i\phi}$
\RETURN $x_p=\operatorname{Re}z_p=\dfrac{B}{|p(i\omega)|}\cos(\omega t-\phi)$
\end{algorithmic}
\end{algorithm}
```

:::

::: {#prp-first-order-exponential-input .proposition name="Exponential input"}
Let $k$ be real and $r$ complex with $r\neq-k$. Then
$$
y'+ky = e^{rt}\quad\text{has the solution}\quad y_p=\frac{e^{rt}}{r+k}.
$$
:::

::: {.proof}
1. Try $y=ce^{rt}$. By @prp-complex-exponential-rules, $y'+ky=c\,(r+k)e^{rt}$.

2. This equals $e^{rt}$ when $c=1/(r+k)$.
:::

::: {#thm-first-order-sinusoidal-response .theorem name="Sinusoidal response of a first-order system"}
For $k>0$, the equation $y'+ky=k\cos\omega t$ has the periodic solution
$$
y_p = g\cos(\omega t-\phi),\qquad g=\frac{1}{\sqrt{1+(\omega/k)^2}},\quad \phi=\arctan\frac{\omega}{k},
$$
and every solution approaches $y_p$ as $t\to\infty$.
:::

::: {.proof}
1. The complexified equation $z'+kz=ke^{i\omega t}$ has, by @prp-first-order-exponential-input, the solution $z=\dfrac{k}{k+i\omega}e^{i\omega t}$.

2. Write $\dfrac{k}{k+i\omega}=\dfrac{1}{1+i\omega/k}=g\,e^{-i\phi}$, where $g=1/|1+i\omega/k|$ and $\phi=\arg(1+i\omega/k)=\arctan(\omega/k)$.

3. Then $z=g\,e^{i(\omega t-\phi)}$ and $y_p=\operatorname{Re}z=g\cos(\omega t-\phi)$.

4. Every other solution differs from $y_p$ by a multiple of $e^{-kt}$, the transient of @thm-constant-coefficient-first-order.
:::

::: {#fig-complex-replacement-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.55cm, y=1cm]
\draw[->] (0,0) -- (13.2,0) node[lab, right] {$t$};
\draw[->] (0,-1.3) -- (0,1.5) node[lab, above] {};
\draw[emph, muted] (0,1) -- (0.159,0.987) -- (0.319,0.95) -- (0.478,0.888) -- (0.638,0.803) -- (0.797,0.699) -- (0.957,0.576) -- (1.116,0.439) -- (1.276,0.291) -- (1.435,0.135) -- (1.595,-0.024) -- (1.754,-0.183) -- (1.914,-0.336) -- (2.073,-0.482) -- (2.233,-0.615) -- (2.392,-0.732) -- (2.552,-0.831) -- (2.711,-0.909) -- (2.871,-0.964) -- (3.03,-0.994) -- (3.19,-0.999) -- (3.349,-0.978) -- (3.509,-0.933) -- (3.668,-0.864) -- (3.828,-0.774) -- (3.987,-0.663) -- (4.147,-0.536) -- (4.306,-0.395) -- (4.466,-0.244) -- (4.625,-0.087) -- (4.785,0.072) -- (4.944,0.23) -- (5.104,0.381) -- (5.263,0.523) -- (5.423,0.652) -- (5.582,0.764) -- (5.742,0.857) -- (5.901,0.928) -- (6.061,0.975) -- (6.22,0.998) -- (6.38,0.995) -- (6.539,0.967) -- (6.699,0.915) -- (6.858,0.839) -- (7.018,0.742) -- (7.177,0.626) -- (7.337,0.495) -- (7.496,0.35) -- (7.656,0.197) -- (7.815,0.039) -- (7.975,-0.12) -- (8.134,-0.277) -- (8.294,-0.426) -- (8.453,-0.564) -- (8.613,-0.688) -- (8.772,-0.794) -- (8.932,-0.881) -- (9.091,-0.945) -- (9.251,-0.985) -- (9.41,-1) -- (9.57,-0.99) -- (9.729,-0.954) -- (9.889,-0.894) -- (10.048,-0.812) -- (10.208,-0.709) -- (10.367,-0.588) -- (10.527,-0.452) -- (10.686,-0.305) -- (10.846,-0.149) -- (11.005,0.009) -- (11.165,0.168) -- (11.324,0.323) -- (11.484,0.469) -- (11.643,0.603) -- (11.803,0.722) -- (11.962,0.823) -- (12.122,0.903) -- (12.281,0.96) -- (12.441,0.992) -- (12.6,0.999);
\draw[emph, primary] (0,0.5) -- (0.159,0.573) -- (0.319,0.632) -- (0.478,0.674) -- (0.638,0.699) -- (0.797,0.707) -- (0.957,0.697) -- (1.116,0.669) -- (1.276,0.624) -- (1.435,0.563) -- (1.595,0.488) -- (1.754,0.4) -- (1.914,0.303) -- (2.073,0.197) -- (2.233,0.087) -- (2.392,-0.026) -- (2.552,-0.138) -- (2.711,-0.246) -- (2.871,-0.348) -- (3.03,-0.441) -- (3.19,-0.524) -- (3.349,-0.592) -- (3.509,-0.646) -- (3.668,-0.684) -- (3.828,-0.704) -- (3.987,-0.706) -- (4.147,-0.69) -- (4.306,-0.657) -- (4.466,-0.607) -- (4.625,-0.542) -- (4.785,-0.463) -- (4.944,-0.372) -- (5.104,-0.271) -- (5.263,-0.164) -- (5.423,-0.053) -- (5.582,0.06) -- (5.742,0.171) -- (5.901,0.278) -- (6.061,0.377) -- (6.22,0.468) -- (6.38,0.546) -- (6.539,0.61) -- (6.699,0.659) -- (6.858,0.692) -- (7.018,0.706) -- (7.177,0.703) -- (7.337,0.682) -- (7.496,0.643) -- (7.656,0.589) -- (7.815,0.519) -- (7.975,0.436) -- (8.134,0.342) -- (8.294,0.24) -- (8.453,0.131) -- (8.613,0.019) -- (8.772,-0.094) -- (8.932,-0.204) -- (9.091,-0.309) -- (9.251,-0.406) -- (9.41,-0.493) -- (9.57,-0.567) -- (9.729,-0.627) -- (9.889,-0.671) -- (10.048,-0.698) -- (10.208,-0.707) -- (10.367,-0.698) -- (10.527,-0.672) -- (10.686,-0.629) -- (10.846,-0.569) -- (11.005,-0.495) -- (11.165,-0.409) -- (11.324,-0.312) -- (11.484,-0.207) -- (11.643,-0.097) -- (11.803,0.015) -- (11.962,0.127) -- (12.122,0.236) -- (12.281,0.339) -- (12.441,0.433) -- (12.6,0.517);
\node[lab, note, muted] at (6.3,1.25) {input $\cos t$}; \node[lab, note, primary] at (8.9,-0.95) {response $g\cos(t-\phi)$};
\end{tikzpicture}
\end{center}
```

For $k=\omega=1$ the periodic response has gain $1/\sqrt2$ and lags the input by $\pi/4$.

:::

::: {#def-gain-phase-lag .definition name="Gain and phase lag"}
When a stable system responds to the input $\cos\omega t$ (in the units of the output) with the periodic output $g\cos(\omega t-\phi)$, the number $g=g(\omega)$ is the *gain* and $\phi=\phi(\omega)$ is the *phase lag* at angular frequency $\omega$. For the system of @thm-first-order-sinusoidal-response the gain decreases from $1$ to $0$ and the phase lag increases from $0$ to $\pi/2$ as $\omega$ grows: slow inputs are followed closely, fast ones are smoothed out and delayed.
:::

::: {#fig-complex-replacement-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.9cm, y=1.6cm]
\draw[->] (0,0) -- (6.4,0) node[lab, right] {$\omega/k$};
\draw[->] (0,0) -- (0,1.75);
\draw[emph, primary] (0,1) -- (0.076,0.997) -- (0.152,0.989) -- (0.228,0.975) -- (0.304,0.957) -- (0.38,0.935) -- (0.456,0.91) -- (0.532,0.883) -- (0.608,0.855) -- (0.684,0.826) -- (0.759,0.796) -- (0.835,0.767) -- (0.911,0.739) -- (0.987,0.712) -- (1.063,0.685) -- (1.139,0.66) -- (1.215,0.635) -- (1.291,0.612) -- (1.367,0.59) -- (1.443,0.57) -- (1.519,0.55) -- (1.595,0.531) -- (1.671,0.514) -- (1.747,0.497) -- (1.823,0.481) -- (1.899,0.466) -- (1.975,0.452) -- (2.051,0.438) -- (2.127,0.426) -- (2.203,0.413) -- (2.278,0.402) -- (2.354,0.391) -- (2.43,0.381) -- (2.506,0.371) -- (2.582,0.361) -- (2.658,0.352) -- (2.734,0.343) -- (2.81,0.335) -- (2.886,0.327) -- (2.962,0.32) -- (3.038,0.313) -- (3.114,0.306) -- (3.19,0.299) -- (3.266,0.293) -- (3.342,0.287) -- (3.418,0.281) -- (3.494,0.275) -- (3.57,0.27) -- (3.646,0.265) -- (3.722,0.26) -- (3.797,0.255) -- (3.873,0.25) -- (3.949,0.245) -- (4.025,0.241) -- (4.101,0.237) -- (4.177,0.233) -- (4.253,0.229) -- (4.329,0.225) -- (4.405,0.221) -- (4.481,0.218) -- (4.557,0.214) -- (4.633,0.211) -- (4.709,0.208) -- (4.785,0.205) -- (4.861,0.202) -- (4.937,0.199) -- (5.013,0.196) -- (5.089,0.193) -- (5.165,0.19) -- (5.241,0.187) -- (5.316,0.185) -- (5.392,0.182) -- (5.468,0.18) -- (5.544,0.178) -- (5.62,0.175) -- (5.696,0.173) -- (5.772,0.171) -- (5.848,0.169) -- (5.924,0.166) -- (6,0.164);
\draw[emph, accent] (0,0) -- (0.076,0.076) -- (0.152,0.151) -- (0.228,0.224) -- (0.304,0.295) -- (0.38,0.363) -- (0.456,0.428) -- (0.532,0.489) -- (0.608,0.546) -- (0.684,0.6) -- (0.759,0.65) -- (0.835,0.696) -- (0.911,0.739) -- (0.987,0.779) -- (1.063,0.816) -- (1.139,0.85) -- (1.215,0.882) -- (1.291,0.912) -- (1.367,0.939) -- (1.443,0.965) -- (1.519,0.989) -- (1.595,1.011) -- (1.671,1.031) -- (1.747,1.051) -- (1.823,1.069) -- (1.899,1.086) -- (1.975,1.102) -- (2.051,1.117) -- (2.127,1.131) -- (2.203,1.145) -- (2.278,1.157) -- (2.354,1.169) -- (2.43,1.18) -- (2.506,1.191) -- (2.582,1.201) -- (2.658,1.211) -- (2.734,1.22) -- (2.81,1.229) -- (2.886,1.237) -- (2.962,1.245) -- (3.038,1.253) -- (3.114,1.26) -- (3.19,1.267) -- (3.266,1.274) -- (3.342,1.28) -- (3.418,1.286) -- (3.494,1.292) -- (3.57,1.298) -- (3.646,1.303) -- (3.722,1.308) -- (3.797,1.313) -- (3.873,1.318) -- (3.949,1.323) -- (4.025,1.327) -- (4.101,1.332) -- (4.177,1.336) -- (4.253,1.34) -- (4.329,1.344) -- (4.405,1.348) -- (4.481,1.351) -- (4.557,1.355) -- (4.633,1.358) -- (4.709,1.362) -- (4.785,1.365) -- (4.861,1.368) -- (4.937,1.371) -- (5.013,1.374) -- (5.089,1.377) -- (5.165,1.38) -- (5.241,1.382) -- (5.316,1.385) -- (5.392,1.387) -- (5.468,1.39) -- (5.544,1.392) -- (5.62,1.395) -- (5.696,1.397) -- (5.772,1.399) -- (5.848,1.401) -- (5.924,1.404) -- (6,1.406);
\draw (0,1) -- (-0.08,1) node[left, lab, tick] {$1$};
\draw (0,1.571) -- (-0.08,1.571) node[left, lab, tick] {$\pi/2$};
\draw[faint, dashed] (0,1.571) -- (6,1.571);
\node[lab, note, primary] at (4.5,0.45) {gain $g$}; \node[lab, note, accent] at (4.5,1.2) {phase lag $\phi$};
\draw (1,0) -- (1,-0.08) node[below, lab, tick] {$1$};
\end{tikzpicture}
\end{center}
```

Gain and phase lag of $y'+ky=k\cos\omega t$ as functions of $\omega/k$: fast inputs are damped and delayed by up to a quarter period.

:::

::: {#exm-first-order-sinusoidal .example name="A house heated by the sun"}
Model the inside temperature by $y'+ky=kT_{\text{out}}$ with $k=1$ per hour, and let the outside temperature vary as $\cos t$ (one radian per hour, measured from its mean). Then $\omega/k=1$, so
$$
g=\tfrac{1}{\sqrt2}\approx0.71,\qquad \phi=\tfrac{\pi}{4},
$$
and the inside swing is about $71\%$ of the outside swing, peaking $\pi/4\approx0.79$ hours later.
:::
