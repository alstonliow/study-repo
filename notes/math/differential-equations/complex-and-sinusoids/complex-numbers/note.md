---
title: "Complex Numbers and the Complex Exponential"
sources: [mit1803-6]
requires: [math/calculus/single-variable/series/taylor-series]
status: draft
---

<!-- Added 2026-11-24 from MIT 18.03SC Differential Equations (Fall 2011), Session 6 (complex arithmetic, polar form, the complex exponential, roots), in our own wording; examples are ours, checked in Python; proofs written out in steps. The rigorous construction of exp, cos and sin by power series is in @sec-math-analysis-real-power-series-exponential-and-trigonometric-functions. -->

Complex numbers turn the trigonometric calculations of oscillating systems into algebra with exponentials. This note collects what the rest of the part uses.

::: {#def-complex-number .definition name="Complex numbers, conjugate, modulus"}
A *complex number* is $z=a+bi$ with $a,b\in\mathbb R$ and $i^2=-1$; $a=\operatorname{Re}z$ is its *real part* and $b=\operatorname{Im}z$ its *imaginary part*. Sums and products follow the usual rules of algebra with $i^2=-1$. The *conjugate* and *modulus* are
$$
\bar z = a-bi,\qquad |z| = \sqrt{a^2+b^2}=\sqrt{z\bar z}.
$$
Division uses the conjugate: $\dfrac{1}{z}=\dfrac{\bar z}{|z|^2}$ for $z\neq 0$.
:::

::: {#def-complex-exponential .definition name="Complex exponential"}
For real $\theta$ and complex $z=a+bi$,
$$
e^{i\theta} = \cos\theta + i\sin\theta,\qquad e^{a+bi} = e^{a}\,(\cos b + i\sin b).
$$
The first formula is *Euler's formula*; it agrees with substituting $i\theta$ into the Taylor series of $e^x$ and sorting the even and odd powers into the series of $\cos$ and $\sin$.
:::

::: {#prp-complex-exponential-rules .proposition name="Rules of the complex exponential"}
For complex $z,w$ and complex $r$,
$$
e^{z+w}=e^ze^w,\qquad \frac{d}{dt}e^{rt}=r\,e^{rt}\quad(t\in\mathbb R).
$$
:::

::: {.proof}
1. For $z=a+bi$, $w=c+di$: $e^ze^w=e^{a+c}(\cos b+i\sin b)(\cos d+i\sin d)$.

2. Multiplying out, the real part is $\cos b\cos d-\sin b\sin d=\cos(b+d)$ and the imaginary part is $\sin b\cos d+\cos b\sin d=\sin(b+d)$, so $e^ze^w=e^{a+c}(\cos(b+d)+i\sin(b+d))=e^{z+w}$.

3. For $r=a+bi$, $e^{rt}=e^{at}\cos bt+ie^{at}\sin bt$. Differentiating real and imaginary parts gives $e^{at}(a\cos bt-b\sin bt)+ie^{at}(a\sin bt+b\cos bt)$.

4. This equals $(a+bi)\,e^{at}(\cos bt+i\sin bt)=r\,e^{rt}$, as multiplying out shows.
:::

::: {#def-polar-form .definition name="Polar form, argument"}
Every $z\neq0$ can be written
$$
z = r\,e^{i\theta},\qquad r=|z|>0,
$$
where $\theta$, an *argument* $\arg z$, is the angle from the positive real axis to $z$ (unique up to multiples of $2\pi$). By @prp-complex-exponential-rules, $r_1e^{i\theta_1}\cdot r_2e^{i\theta_2}=r_1r_2\,e^{i(\theta_1+\theta_2)}$: *moduli multiply and arguments add*.
:::

::: {#fig-complex-numbers-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.2]
\draw[->] (-0.4,0) -- (2.9,0) node[lab, right] {$\operatorname{Re}$};
\draw[->] (0,-1.6) -- (0,2) node[lab, above] {$\operatorname{Im}$};
\draw[emph, primary] (0,0) -- (2,1.3) node[midway, above left, lab] {$r$};
\draw[faint, dashed] (2,0) -- (2,1.3) -- (0,1.3);
\node[dot] at (2,1.3) {};
\node[lab, right] at (2,1.3) {$z=a+bi=re^{i\theta}$};
\draw[accent] (0.6,0) arc (0:33.024:0.6); \node[lab, accent] at (0.8,0.22) {$\theta$};
\draw (2,0) -- (2,-0.08) node[below, lab, tick] {$a$};
\draw (0,1.3) -- (-0.08,1.3) node[left, lab, tick] {$b$};
\node[hollow dot] at (2,-1.3) {}; \node[lab, right] at (2,-1.3) {$\bar z$};
\end{tikzpicture}
\end{center}
```

A complex number in rectangular form $a+bi$ and polar form $re^{i\theta}$, and its conjugate, the reflection in the real axis.

:::

::: {#exm-complex-arithmetic .example name="Computing in polar form"}
1. $\dfrac{1+i}{1-i}=\dfrac{\sqrt2e^{i\pi/4}}{\sqrt2e^{-i\pi/4}}=e^{i\pi/2}=i$.
2. $(1+i)^8=(\sqrt2)^8e^{i\cdot 8\pi/4}=16e^{2\pi i}=16$.
3. The cube roots of $-8=8e^{i\pi}$ are $2e^{i(\pi+2\pi k)/3}$ for $k=0,1,2$: that is $1+\sqrt3\,i$, $-2$ and $1-\sqrt3\,i$.
:::

::: {#fig-complex-numbers-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.9]
\draw[->] (-2.6,0) -- (2.6,0) node[lab, right] {$\operatorname{Re}$};
\draw[->] (0,-2.4) -- (0,2.5) node[lab, above] {$\operatorname{Im}$};
\draw[faint] (0,0) circle (2);
\draw[primary] (0,0) -- (1,1.732); \node[hl dot] at (1,1.732) {};
\draw[primary] (0,0) -- (-2,0); \node[hl dot] at (-2,0) {};
\draw[primary] (0,0) -- (1,-1.732); \node[hl dot] at (1,-1.732) {};
\node[lab, right] at (1,1.75) {$1+\sqrt3\,i$}; \node[lab, above left] at (-2,0) {$-2$}; \node[lab, right] at (1,-1.75) {$1-\sqrt3\,i$};
\node[lab, note, muted] at (1.75,-0.25) {$|z|=2$};
\end{tikzpicture}
\end{center}
```

The three cube roots of $-8$ lie on the circle of radius $2$, spaced $120^\circ$ apart, starting from the angle $\pi/3$.

:::

::: {#exm-complex-integration .example name="Integrating with complex exponentials"}
To find $\int e^{t}\cos t\,dt$, note $e^t\cos t=\operatorname{Re}e^{(1+i)t}$. An antiderivative of $e^{(1+i)t}$ is
$$
\frac{e^{(1+i)t}}{1+i}=\frac{1-i}{2}\,e^{t}(\cos t+i\sin t),
$$
whose real part is $\tfrac12e^t(\cos t+\sin t)$. One complex integration replaces two integrations by parts.
:::
