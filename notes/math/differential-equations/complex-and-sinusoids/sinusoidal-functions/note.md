---
title: "Sinusoidal Functions"
sources: [mit1803-7]
requires: [math/differential-equations/complex-and-sinusoids/complex-numbers]
status: draft
---

<!-- Added 2026-11-24 from MIT 18.03SC Differential Equations (Fall 2011), Session 7 (sinusoidal functions: amplitude, frequency, phase, the sum identity), in our own wording; examples are ours, checked in Python; proofs written out in steps. -->

Oscillating systems are described by *sinusoids*. Every sum of a cosine and a sine of the same frequency is again a single shifted cosine, and complex numbers find its amplitude and phase at once.

::: {#def-sinusoid .definition name="Sinusoidal function"}
A *sinusoidal function* is
$$
f(t) = A\cos(\omega t-\phi),\qquad A>0,\ \omega>0 .
$$
Here $A$ is the *amplitude*, $\omega$ the *angular frequency* (radians per unit time), $\phi$ the *phase lag*. The *period* is $P=2\pi/\omega$, the *frequency* is $\nu=1/P=\omega/2\pi$, and the *time lag* $\phi/\omega$ is how far the graph is shifted right compared with $A\cos\omega t$.
:::

::: {#fig-sinusoidal-functions-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.55cm, y=0.8cm]
\draw[->] (0,0) -- (13.2,0) node[lab, right] {$t$};
\draw[->] (0,-1.8) -- (0,2.1) node[lab, above] {};
\draw[faint, dashed] (0,1.5) -- (0.159,1.481) -- (0.319,1.424) -- (0.478,1.332) -- (0.638,1.205) -- (0.797,1.048) -- (0.957,0.864) -- (1.116,0.658) -- (1.276,0.436) -- (1.435,0.202) -- (1.595,-0.036) -- (1.754,-0.274) -- (1.914,-0.505) -- (2.073,-0.723) -- (2.233,-0.922) -- (2.392,-1.098) -- (2.552,-1.247) -- (2.711,-1.363) -- (2.871,-1.445) -- (3.03,-1.491) -- (3.19,-1.498) -- (3.349,-1.468) -- (3.509,-1.4) -- (3.668,-1.297) -- (3.828,-1.16) -- (3.987,-0.995) -- (4.147,-0.804) -- (4.306,-0.592) -- (4.466,-0.366) -- (4.625,-0.13) -- (4.785,0.109) -- (4.944,0.345) -- (5.104,0.572) -- (5.263,0.785) -- (5.423,0.978) -- (5.582,1.146) -- (5.742,1.285) -- (5.901,1.392) -- (6.061,1.463) -- (6.22,1.497) -- (6.38,1.493) -- (6.539,1.451) -- (6.699,1.372) -- (6.858,1.259) -- (7.018,1.113) -- (7.177,0.939) -- (7.337,0.742) -- (7.496,0.525) -- (7.656,0.295) -- (7.815,0.058) -- (7.975,-0.181) -- (8.134,-0.415) -- (8.294,-0.638) -- (8.453,-0.846) -- (8.613,-1.032) -- (8.772,-1.192) -- (8.932,-1.321) -- (9.091,-1.417) -- (9.251,-1.477) -- (9.41,-1.5) -- (9.57,-1.484) -- (9.729,-1.431) -- (9.889,-1.342) -- (10.048,-1.218) -- (10.208,-1.063) -- (10.367,-0.882) -- (10.527,-0.678) -- (10.686,-0.457) -- (10.846,-0.224) -- (11.005,0.014) -- (11.165,0.252) -- (11.324,0.484) -- (11.484,0.703) -- (11.643,0.905) -- (11.803,1.083) -- (11.962,1.234) -- (12.122,1.354) -- (12.281,1.439) -- (12.441,1.488) -- (12.6,1.499);
\draw[emph, primary] (0,0.75) -- (0.159,0.947) -- (0.319,1.12) -- (0.478,1.264) -- (0.638,1.376) -- (0.797,1.453) -- (0.957,1.494) -- (1.116,1.496) -- (1.276,1.461) -- (1.435,1.388) -- (1.595,1.281) -- (1.754,1.14) -- (1.914,0.971) -- (2.073,0.777) -- (2.233,0.563) -- (2.392,0.336) -- (2.552,0.099) -- (2.711,-0.14) -- (2.871,-0.375) -- (3.03,-0.601) -- (3.19,-0.812) -- (3.349,-1.002) -- (3.509,-1.166) -- (3.668,-1.301) -- (3.828,-1.403) -- (3.987,-1.47) -- (4.147,-1.499) -- (4.306,-1.49) -- (4.466,-1.443) -- (4.625,-1.359) -- (4.785,-1.241) -- (4.944,-1.092) -- (5.104,-0.915) -- (5.263,-0.714) -- (5.423,-0.496) -- (5.582,-0.265) -- (5.742,-0.027) -- (5.901,0.212) -- (6.061,0.445) -- (6.22,0.667) -- (6.38,0.872) -- (6.539,1.055) -- (6.699,1.211) -- (6.858,1.336) -- (7.018,1.427) -- (7.177,1.482) -- (7.337,1.5) -- (7.496,1.479) -- (7.656,1.421) -- (7.815,1.327) -- (7.975,1.199) -- (8.134,1.041) -- (8.294,0.856) -- (8.453,0.65) -- (8.613,0.427) -- (8.772,0.193) -- (8.932,-0.046) -- (9.091,-0.283) -- (9.251,-0.514) -- (9.41,-0.731) -- (9.57,-0.93) -- (9.729,-1.105) -- (9.889,-1.252) -- (10.048,-1.367) -- (10.208,-1.448) -- (10.367,-1.492) -- (10.527,-1.498) -- (10.686,-1.466) -- (10.846,-1.397) -- (11.005,-1.292) -- (11.165,-1.154) -- (11.324,-0.988) -- (11.484,-0.796) -- (11.643,-0.584) -- (11.803,-0.357) -- (11.962,-0.121) -- (12.122,0.118) -- (12.281,0.354) -- (12.441,0.581) -- (12.6,0.793);
\draw[<->, accent] (0,1.7) -- (1.047,1.7) node[midway, above, lab, note] {$\phi/\omega$};
\draw[<->, accent] (1.047,-1.75) -- (7.33,-1.75) node[midway, below, lab, note] {period $2\pi/\omega$};
\draw[faint] (1.047,0) -- (1.047,1.7); \draw[faint] (7.33,-1.75) -- (7.33,1.5);
\draw (0,1.5) -- (-0.08,1.5) node[left, lab, tick] {$A$};
\end{tikzpicture}
\end{center}
```

The sinusoid $A\cos(\omega t-\phi)$ (solid) is $A\cos\omega t$ (dashed) shifted right by the time lag $\phi/\omega$.

:::

::: {#prp-sinusoid-identity .proposition name="Sum of a cosine and a sine"}
For real $a,b$, not both zero,
$$
a\cos\omega t+b\sin\omega t = A\cos(\omega t-\phi),\qquad A=\sqrt{a^2+b^2},\quad \phi=\arg(a+bi).
$$
:::

::: {.proof}
1. Write $a+bi=Ae^{i\phi}$ (@def-polar-form), so $a-bi=Ae^{-i\phi}$.

2. Then $(a-bi)e^{i\omega t}=(a-bi)(\cos\omega t+i\sin\omega t)$ has real part $a\cos\omega t+b\sin\omega t$.

3. Also $(a-bi)e^{i\omega t}=Ae^{i(\omega t-\phi)}$, whose real part is $A\cos(\omega t-\phi)$.
:::

::: {#fig-sinusoidal-functions-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.6]
\draw[emph, primary] (0,0) -- (1,0) node[midway, below, lab] {$a=1$} -- (1,1.732) node[midway, right, lab] {$b=\sqrt3$} -- cycle;
\node[lab, above left] at (0.5,0.866) {$A=2$};
\draw[accent] (0.35,0) arc (0:60:0.35); \node[lab, accent] at (0.5,0.25) {$\phi$};
\draw (0.88,0) -- (0.88,0.12) -- (1,0.12);
\end{tikzpicture}
\end{center}
```

The triangle of $\cos t+\sqrt3\sin t$: legs $a$ and $b$, hypotenuse the amplitude $A=2$, angle the phase lag $\phi=\pi/3$.

:::

::: {#exm-sinusoid-identity .example name="Rewriting a sum as one cosine"}
For $\cos t+\sqrt3\sin t$: $a+bi=1+\sqrt3\,i=2e^{i\pi/3}$, so
$$
\cos t+\sqrt3\sin t = 2\cos\left(t-\tfrac{\pi}{3}\right).
$$
The amplitude is $2$, the period $2\pi$, the phase lag $\pi/3$ and the time lag $\pi/3$.
:::

::: {#rmk-sinusoidal-functions-1 .remark name="The right triangle"}
The identity is easy to remember with the right triangle of legs $a$ and $b$: its hypotenuse is the amplitude $A$ and the angle at the origin is the phase lag $\phi$. Take care with the quadrant: $\phi=\arctan(b/a)$ only when $a>0$.
:::
