---
title: "Autonomous Equations and Stability"
sources: [mit1803-10]
requires: [math/differential-equations/first-order/direction-fields]
status: draft
---

<!-- Added 2026-11-24 from MIT 18.03SC Differential Equations (Fall 2011), Session 10 (first-order autonomous equations: critical points, phase lines, stability, logistic growth, harvesting), in our own wording; examples are ours, checked in Python; proofs written out in steps. -->

When the rate of change depends only on the current state and not on time, the whole behaviour of the solutions can be read off a single line.

::: {#def-autonomous-equation .definition name="Autonomous equation, critical point"}
A first-order equation is *autonomous* if it has the form
$$
y' = f(y),
$$
with no explicit dependence on $t$. A *critical point* (equilibrium) is a value $a$ with $f(a)=0$; the constant function $y=a$ is then a solution.
:::

::: {#def-phase-line-stability .definition name="Phase line, stability"}
The *phase line* is the $y$-axis with the critical points marked and an arrow on each interval between them, pointing up where $f>0$ and down where $f<0$. A critical point $a$ is

- *stable* (an attractor) if solutions starting near $a$ tend to $a$ as $t\to\infty$;
- *unstable* (a repeller) if solutions starting near $a$, but not at $a$, move away;
- *semistable* if solutions approach on one side and leave on the other.
:::

::: {#fig-autonomous-equations-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.85cm, y=0.55cm]
\draw[->] (0,-0.4) -- (0,6.4) node[lab, above] {$y$};
\draw[->] (0,0) -- (6.2,0) node[lab, right] {$t$};
\draw[faint, dashed] (0,5) -- (6,5);
\draw (0,5) -- (-0.08,5) node[left, lab, tick] {$M$};
\draw[emph, primary] (0,0.3) -- (0.076,0.322) -- (0.152,0.346) -- (0.228,0.371) -- (0.304,0.398) -- (0.38,0.427) -- (0.456,0.457) -- (0.532,0.49) -- (0.608,0.524) -- (0.684,0.561) -- (0.759,0.6) -- (0.835,0.641) -- (0.911,0.685) -- (0.987,0.731) -- (1.063,0.78) -- (1.139,0.831) -- (1.215,0.885) -- (1.291,0.942) -- (1.367,1.001) -- (1.443,1.064) -- (1.519,1.129) -- (1.595,1.196) -- (1.671,1.267) -- (1.747,1.34) -- (1.823,1.416) -- (1.899,1.494) -- (1.975,1.575) -- (2.051,1.658) -- (2.127,1.743) -- (2.203,1.83) -- (2.278,1.919) -- (2.354,2.01) -- (2.43,2.102) -- (2.506,2.195) -- (2.582,2.289) -- (2.658,2.383) -- (2.734,2.478) -- (2.81,2.573) -- (2.886,2.668) -- (2.962,2.762) -- (3.038,2.856) -- (3.114,2.948) -- (3.19,3.039) -- (3.266,3.129) -- (3.342,3.217) -- (3.418,3.303) -- (3.494,3.387) -- (3.57,3.469) -- (3.646,3.549) -- (3.722,3.626) -- (3.797,3.7) -- (3.873,3.772) -- (3.949,3.841) -- (4.025,3.907) -- (4.101,3.97) -- (4.177,4.031) -- (4.253,4.089) -- (4.329,4.144) -- (4.405,4.197) -- (4.481,4.247) -- (4.557,4.294) -- (4.633,4.339) -- (4.709,4.381) -- (4.785,4.421) -- (4.861,4.459) -- (4.937,4.495) -- (5.013,4.528) -- (5.089,4.56) -- (5.165,4.589) -- (5.241,4.617) -- (5.316,4.643) -- (5.392,4.667) -- (5.468,4.69) -- (5.544,4.711) -- (5.62,4.731) -- (5.696,4.75) -- (5.772,4.767) -- (5.848,4.784) -- (5.924,4.799) -- (6,4.813);
\draw[emph, primary] (0,1) -- (0.076,1.062) -- (0.152,1.127) -- (0.228,1.195) -- (0.304,1.265) -- (0.38,1.338) -- (0.456,1.414) -- (0.532,1.492) -- (0.608,1.573) -- (0.684,1.656) -- (0.759,1.741) -- (0.835,1.828) -- (0.911,1.917) -- (0.987,2.008) -- (1.063,2.1) -- (1.139,2.193) -- (1.215,2.287) -- (1.291,2.381) -- (1.367,2.476) -- (1.443,2.571) -- (1.519,2.666) -- (1.595,2.76) -- (1.671,2.853) -- (1.747,2.946) -- (1.823,3.037) -- (1.899,3.127) -- (1.975,3.215) -- (2.051,3.301) -- (2.127,3.385) -- (2.203,3.467) -- (2.278,3.547) -- (2.354,3.624) -- (2.43,3.698) -- (2.506,3.77) -- (2.582,3.839) -- (2.658,3.905) -- (2.734,3.969) -- (2.81,4.03) -- (2.886,4.088) -- (2.962,4.143) -- (3.038,4.196) -- (3.114,4.246) -- (3.19,4.293) -- (3.266,4.338) -- (3.342,4.38) -- (3.418,4.42) -- (3.494,4.458) -- (3.57,4.494) -- (3.646,4.527) -- (3.722,4.559) -- (3.797,4.588) -- (3.873,4.616) -- (3.949,4.642) -- (4.025,4.667) -- (4.101,4.69) -- (4.177,4.711) -- (4.253,4.731) -- (4.329,4.75) -- (4.405,4.767) -- (4.481,4.783) -- (4.557,4.799) -- (4.633,4.813) -- (4.709,4.826) -- (4.785,4.838) -- (4.861,4.85) -- (4.937,4.86) -- (5.013,4.87) -- (5.089,4.88) -- (5.165,4.888) -- (5.241,4.896) -- (5.316,4.904) -- (5.392,4.911) -- (5.468,4.917) -- (5.544,4.923) -- (5.62,4.929) -- (5.696,4.934) -- (5.772,4.939) -- (5.848,4.943) -- (5.924,4.947) -- (6,4.951);
\draw[emph, primary] (0,2.5) -- (0.076,2.595) -- (0.152,2.69) -- (0.228,2.784) -- (0.304,2.877) -- (0.38,2.969) -- (0.456,3.06) -- (0.532,3.149) -- (0.608,3.237) -- (0.684,3.323) -- (0.759,3.406) -- (0.835,3.488) -- (0.911,3.566) -- (0.987,3.643) -- (1.063,3.717) -- (1.139,3.788) -- (1.215,3.856) -- (1.291,3.922) -- (1.367,3.985) -- (1.443,4.045) -- (1.519,4.102) -- (1.595,4.157) -- (1.671,4.208) -- (1.747,4.258) -- (1.823,4.304) -- (1.899,4.349) -- (1.975,4.391) -- (2.051,4.43) -- (2.127,4.467) -- (2.203,4.502) -- (2.278,4.535) -- (2.354,4.566) -- (2.43,4.596) -- (2.506,4.623) -- (2.582,4.649) -- (2.658,4.673) -- (2.734,4.695) -- (2.81,4.716) -- (2.886,4.736) -- (2.962,4.754) -- (3.038,4.771) -- (3.114,4.787) -- (3.19,4.802) -- (3.266,4.816) -- (3.342,4.829) -- (3.418,4.841) -- (3.494,4.853) -- (3.57,4.863) -- (3.646,4.873) -- (3.722,4.882) -- (3.797,4.89) -- (3.873,4.898) -- (3.949,4.905) -- (4.025,4.912) -- (4.101,4.919) -- (4.177,4.924) -- (4.253,4.93) -- (4.329,4.935) -- (4.405,4.94) -- (4.481,4.944) -- (4.557,4.948) -- (4.633,4.952) -- (4.709,4.955) -- (4.785,4.959) -- (4.861,4.962) -- (4.937,4.964) -- (5.013,4.967) -- (5.089,4.969) -- (5.165,4.972) -- (5.241,4.974) -- (5.316,4.976) -- (5.392,4.977) -- (5.468,4.979) -- (5.544,4.981) -- (5.62,4.982) -- (5.696,4.983) -- (5.772,4.984) -- (5.848,4.986) -- (5.924,4.987) -- (6,4.988);
\draw[emph, primary] (0,6.2) -- (0.076,6.093) -- (0.152,5.997) -- (0.228,5.911) -- (0.304,5.833) -- (0.38,5.763) -- (0.456,5.699) -- (0.532,5.642) -- (0.608,5.589) -- (0.684,5.541) -- (0.759,5.498) -- (0.835,5.458) -- (0.911,5.422) -- (0.987,5.389) -- (1.063,5.358) -- (1.139,5.33) -- (1.215,5.305) -- (1.291,5.281) -- (1.367,5.259) -- (1.443,5.24) -- (1.519,5.221) -- (1.595,5.204) -- (1.671,5.189) -- (1.747,5.175) -- (1.823,5.161) -- (1.899,5.149) -- (1.975,5.138) -- (2.051,5.128) -- (2.127,5.118) -- (2.203,5.109) -- (2.278,5.101) -- (2.354,5.094) -- (2.43,5.087) -- (2.506,5.08) -- (2.582,5.074) -- (2.658,5.069) -- (2.734,5.064) -- (2.81,5.059) -- (2.886,5.055) -- (2.962,5.051) -- (3.038,5.047) -- (3.114,5.043) -- (3.19,5.04) -- (3.266,5.037) -- (3.342,5.034) -- (3.418,5.032) -- (3.494,5.03) -- (3.57,5.027) -- (3.646,5.025) -- (3.722,5.024) -- (3.797,5.022) -- (3.873,5.02) -- (3.949,5.019) -- (4.025,5.017) -- (4.101,5.016) -- (4.177,5.015) -- (4.253,5.014) -- (4.329,5.013) -- (4.405,5.012) -- (4.481,5.011) -- (4.557,5.01) -- (4.633,5.009) -- (4.709,5.009) -- (4.785,5.008) -- (4.861,5.008) -- (4.937,5.007) -- (5.013,5.006) -- (5.089,5.006) -- (5.165,5.006) -- (5.241,5.005) -- (5.316,5.005) -- (5.392,5.004) -- (5.468,5.004) -- (5.544,5.004) -- (5.62,5.004) -- (5.696,5.003) -- (5.772,5.003) -- (5.848,5.003) -- (5.924,5.003) -- (6,5.002);
\draw[->, emph] (-0.9,-0.3) -- (-0.9,6.2);
\node[dot] at (-0.9,0) {}; \node[hl dot] at (-0.9,5) {};
\draw[->, hl] (-0.9,1.8) -- (-0.9,2.6); \draw[->, hl] (-0.9,6.1) -- (-0.9,5.6);
\node[lab, note] at (-0.9,-0.75) {phase line};
\end{tikzpicture}
\end{center}
```

Logistic growth $y'=y(1-y/5)$: the phase line (left) shows $0$ unstable and $M=5$ stable; the solutions (right) move along the arrows and level off at $M$.

:::

::: {#prp-critical-point-derivative-test .proposition name="Derivative test for stability"}
Let $f$ be continuously differentiable and $f(a)=0$. If $f'(a)<0$ the critical point $a$ is stable; if $f'(a)>0$ it is unstable.
:::

::: {.proof}
1. Suppose $f'(a)<0$. By continuity of $f'$ there is $\delta>0$ with $f'<0$ on $(a-\delta,a+\delta)$, so $f$ is decreasing there.

2. Hence $f>0$ on $(a-\delta,a)$ and $f<0$ on $(a,a+\delta)$: solutions just below $a$ increase and solutions just above decrease.

3. A solution starting in $(a,a+\delta)$ decreases, cannot cross the solution $y=a$ (@thm-existence-uniqueness-first-order), so it is monotone and bounded and has a limit $L\ge a$. If $L>a$ then $y'\to f(L)<0$, and $y$ would decrease without bound, a contradiction; so $L=a$. The case below $a$ is symmetric.

4. If $f'(a)>0$ the signs in step 2 are reversed, and nearby solutions move away from $a$.
:::

::: {#exm-logistic-equation .example name="Logistic growth" related="def-logistic-function"}
A population with limited resources follows the *logistic equation*
$$
y' = ky\left(1-\frac{y}{M}\right),\qquad k,M>0 .
$$
The critical points are $0$ (unstable, $f'(0)=k>0$) and the *carrying capacity* $M$ (stable, $f'(M)=-k<0$). Separating variables gives
$$
y(t) = \frac{M}{1+\frac{M-y_0}{y_0}e^{-kt}}\qquad (y_0>0),
$$
so for $k=1$, $M=5$, $y_0=1$ we get $y=5/(1+4e^{-t})\to 5$.
:::

::: {#exm-logistic-harvesting .example name="Harvesting and a bifurcation"}
With constant harvesting $h\ge 0$ the scaled logistic model is $y'=y(1-y)-h$. Its critical points are
$$
y_\pm = \tfrac12\left(1\pm\sqrt{1-4h}\right).
$$

1. For $h<\tfrac14$ there are two: $y_+$ is stable and $y_-$ unstable. A population starting above $y_-$ settles at $y_+$; one below $y_-$ dies out.
2. At $h=\tfrac14$ they merge into a semistable point $y=\tfrac12$.
3. For $h>\tfrac14$ there are none and $y'<0$ everywhere: every population is driven to extinction.

The value $h=\tfrac14$, where the number of critical points changes, is a *bifurcation*; it is the largest sustainable harvest.
:::

::: {#fig-autonomous-equations-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=14cm, y=3.2cm]
\draw[->] (0,0) -- (0.36,0) node[lab, right] {$h$};
\draw[->] (0,0) -- (0,1.15) node[lab, above] {$y$};
\draw[hl] (0.25,0.5) -- (0.25,0.513) -- (0.249,0.526) -- (0.249,0.538) -- (0.247,0.551) -- (0.246,0.564) -- (0.244,0.577) -- (0.242,0.59) -- (0.239,0.603) -- (0.237,0.615) -- (0.234,0.628) -- (0.23,0.641) -- (0.226,0.654) -- (0.222,0.667) -- (0.218,0.679) -- (0.213,0.692) -- (0.208,0.705) -- (0.202,0.718) -- (0.197,0.731) -- (0.191,0.744) -- (0.184,0.756) -- (0.178,0.769) -- (0.17,0.782) -- (0.163,0.795) -- (0.155,0.808) -- (0.147,0.821) -- (0.139,0.833) -- (0.13,0.846) -- (0.121,0.859) -- (0.112,0.872) -- (0.102,0.885) -- (0.092,0.897) -- (0.082,0.91) -- (0.071,0.923) -- (0.06,0.936) -- (0.049,0.949) -- (0.037,0.962) -- (0.025,0.974) -- (0.013,0.987) -- (0,1);
\draw[emph, primary, dashed] (0,0) -- (0.013,0.013) -- (0.025,0.026) -- (0.037,0.038) -- (0.049,0.051) -- (0.06,0.064) -- (0.071,0.077) -- (0.082,0.09) -- (0.092,0.103) -- (0.102,0.115) -- (0.112,0.128) -- (0.121,0.141) -- (0.13,0.154) -- (0.139,0.167) -- (0.147,0.179) -- (0.155,0.192) -- (0.163,0.205) -- (0.17,0.218) -- (0.178,0.231) -- (0.184,0.244) -- (0.191,0.256) -- (0.197,0.269) -- (0.202,0.282) -- (0.208,0.295) -- (0.213,0.308) -- (0.218,0.321) -- (0.222,0.333) -- (0.226,0.346) -- (0.23,0.359) -- (0.234,0.372) -- (0.237,0.385) -- (0.239,0.397) -- (0.242,0.41) -- (0.244,0.423) -- (0.246,0.436) -- (0.247,0.449) -- (0.249,0.462) -- (0.249,0.474) -- (0.25,0.487) -- (0.25,0.5);
\node[dot] at (0.25,0.5) {};
\draw (0.25,0) -- (0.25,-0.08) node[below, lab, tick] {$\tfrac14$};
\draw (0,1) -- (-0.08,1) node[left, lab, tick] {$1$};
\draw (0,0.5) -- (-0.08,0.5) node[left, lab, tick] {$\tfrac12$};
\node[lab, note, accent, right] at (0.13,0.9) {stable $y_+$}; \node[lab, note, primary, right] at (0.13,0.08) {unstable $y_-$};
\draw[->, muted] (0.32,0.85) -- (0.32,0.35);
\end{tikzpicture}
\end{center}
```

Bifurcation diagram of $y'=y(1-y)-h$. For $h<\tfrac14$ there are a stable and an unstable equilibrium; they merge at $h=\tfrac14$, and beyond it every population declines.

:::
