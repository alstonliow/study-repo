---
title: "Operators and the Exponential Response Formula"
sources: [mit1803-14, mit1803-15, mit1803-17]
requires: [math/differential-equations/second-order-linear/second-order-linear-equations, math/differential-equations/complex-and-sinusoids/complex-replacement]
status: draft
---

<!-- Added 2026-11-24 from MIT 18.03SC Differential Equations (Fall 2011), Sessions 14 (exponential and sinusoidal input), 15 (p(D) notation, stability) and 17 (operators, the exponential shift rule, time invariance), in our own wording; examples are ours, checked in Python; proofs written out in steps. -->

Writing a constant-coefficient equation as a polynomial in the derivative operator $D$ turns the search for particular solutions into evaluating that polynomial. For exponential and sinusoidal input this gives the answer in one line.

::: {#def-polynomial-differential-operator .definition name="Polynomial differential operator"}
Let $D=\dfrac{d}{dt}$. For a polynomial $p(s)=a_ns^n+\dots+a_1s+a_0$ with constant coefficients, the operator $p(D)$ acts by
$$
p(D)\,y = a_ny^{(n)}+\dots+a_1y'+a_0y .
$$
The equation $a_ny^{(n)}+\dots+a_0y=q$ is written $p(D)y=q$, and $p$ is its characteristic polynomial. Products of operators compose: $(p\,q)(D)=p(D)\,q(D)$.
:::

::: {#prp-operator-rules .proposition name="Substitution and exponential shift"}
For complex $r$ and any $n$ times differentiable $u$,
$$
p(D)\,e^{rt}=p(r)\,e^{rt},\qquad p(D)\bigl(e^{rt}u\bigr)=e^{rt}\,p(D+r)\,u .
$$
:::

::: {.proof}
1. By @prp-complex-exponential-rules, $D^ke^{rt}=r^ke^{rt}$; summing $a_kD^ke^{rt}$ gives the first rule.

2. By the product rule $D(e^{rt}u)=e^{rt}(D+r)u$.

3. Applying this $k$ times, $D^k(e^{rt}u)=e^{rt}(D+r)^ku$ (induction on $k$).

4. Summing with the coefficients $a_k$ gives $p(D)(e^{rt}u)=e^{rt}p(D+r)u$.
:::

::: {#thm-exponential-response-formula .theorem name="Exponential response formula"}
If $p(r)\neq0$, then
$$
p(D)\,y = e^{rt}\quad\text{has the solution}\quad y_p=\frac{e^{rt}}{p(r)} .
$$
:::

::: {.proof}
1. By @prp-operator-rules, $p(D)\dfrac{e^{rt}}{p(r)}=\dfrac{p(r)e^{rt}}{p(r)}=e^{rt}$.
:::

::: {#thm-sinusoidal-response .theorem name="Sinusoidal response"}
Let $p$ have real coefficients and $p(i\omega)\neq0$. Then $p(D)y=\cos\omega t$ has the solution
$$
y_p=\operatorname{Re}\frac{e^{i\omega t}}{p(i\omega)}=\frac{1}{|p(i\omega)|}\cos(\omega t-\phi),\qquad \phi=\arg p(i\omega).
$$
:::

::: {.proof}
1. By complex replacement (@def-complex-replacement) it suffices to solve $p(D)z=e^{i\omega t}$.

2. @thm-exponential-response-formula gives $z=e^{i\omega t}/p(i\omega)$.

3. Writing $p(i\omega)=|p(i\omega)|e^{i\phi}$, we get $z=e^{i(\omega t-\phi)}/|p(i\omega)|$, whose real part is the stated $y_p$.
:::

::: {#exm-exponential-response .example name="A sinusoidal response"}
For $y''+y'+2y=\cos t$: $p(i)=-1+i+2=1+i=\sqrt2\,e^{i\pi/4}$, so
$$
y_p=\tfrac{1}{\sqrt2}\cos\left(t-\tfrac{\pi}{4}\right).
$$
:::

::: {#fig-exponential-response-formula-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.55cm, y=1cm]
\draw[->] (0,0) -- (13.2,0) node[lab, right] {$t$};
\draw[->] (0,-1.3) -- (0,1.5) node[lab, above] {};
\draw[emph, muted] (0,1) -- (0.159,0.987) -- (0.319,0.95) -- (0.478,0.888) -- (0.638,0.803) -- (0.797,0.699) -- (0.957,0.576) -- (1.116,0.439) -- (1.276,0.291) -- (1.435,0.135) -- (1.595,-0.024) -- (1.754,-0.183) -- (1.914,-0.336) -- (2.073,-0.482) -- (2.233,-0.615) -- (2.392,-0.732) -- (2.552,-0.831) -- (2.711,-0.909) -- (2.871,-0.964) -- (3.03,-0.994) -- (3.19,-0.999) -- (3.349,-0.978) -- (3.509,-0.933) -- (3.668,-0.864) -- (3.828,-0.774) -- (3.987,-0.663) -- (4.147,-0.536) -- (4.306,-0.395) -- (4.466,-0.244) -- (4.625,-0.087) -- (4.785,0.072) -- (4.944,0.23) -- (5.104,0.381) -- (5.263,0.523) -- (5.423,0.652) -- (5.582,0.764) -- (5.742,0.857) -- (5.901,0.928) -- (6.061,0.975) -- (6.22,0.998) -- (6.38,0.995) -- (6.539,0.967) -- (6.699,0.915) -- (6.858,0.839) -- (7.018,0.742) -- (7.177,0.626) -- (7.337,0.495) -- (7.496,0.35) -- (7.656,0.197) -- (7.815,0.039) -- (7.975,-0.12) -- (8.134,-0.277) -- (8.294,-0.426) -- (8.453,-0.564) -- (8.613,-0.688) -- (8.772,-0.794) -- (8.932,-0.881) -- (9.091,-0.945) -- (9.251,-0.985) -- (9.41,-1) -- (9.57,-0.99) -- (9.729,-0.954) -- (9.889,-0.894) -- (10.048,-0.812) -- (10.208,-0.709) -- (10.367,-0.588) -- (10.527,-0.452) -- (10.686,-0.305) -- (10.846,-0.149) -- (11.005,0.009) -- (11.165,0.168) -- (11.324,0.323) -- (11.484,0.469) -- (11.643,0.603) -- (11.803,0.722) -- (11.962,0.823) -- (12.122,0.903) -- (12.281,0.96) -- (12.441,0.992) -- (12.6,0.999);
\draw[emph, primary] (0,0.5) -- (0.159,0.573) -- (0.319,0.632) -- (0.478,0.674) -- (0.638,0.699) -- (0.797,0.707) -- (0.957,0.697) -- (1.116,0.669) -- (1.276,0.624) -- (1.435,0.563) -- (1.595,0.488) -- (1.754,0.4) -- (1.914,0.303) -- (2.073,0.197) -- (2.233,0.087) -- (2.392,-0.026) -- (2.552,-0.138) -- (2.711,-0.246) -- (2.871,-0.348) -- (3.03,-0.441) -- (3.19,-0.524) -- (3.349,-0.592) -- (3.509,-0.646) -- (3.668,-0.684) -- (3.828,-0.704) -- (3.987,-0.706) -- (4.147,-0.69) -- (4.306,-0.657) -- (4.466,-0.607) -- (4.625,-0.542) -- (4.785,-0.463) -- (4.944,-0.372) -- (5.104,-0.271) -- (5.263,-0.164) -- (5.423,-0.053) -- (5.582,0.06) -- (5.742,0.171) -- (5.901,0.278) -- (6.061,0.377) -- (6.22,0.468) -- (6.38,0.546) -- (6.539,0.61) -- (6.699,0.659) -- (6.858,0.692) -- (7.018,0.706) -- (7.177,0.703) -- (7.337,0.682) -- (7.496,0.643) -- (7.656,0.589) -- (7.815,0.519) -- (7.975,0.436) -- (8.134,0.342) -- (8.294,0.24) -- (8.453,0.131) -- (8.613,0.019) -- (8.772,-0.094) -- (8.932,-0.204) -- (9.091,-0.309) -- (9.251,-0.406) -- (9.41,-0.493) -- (9.57,-0.567) -- (9.729,-0.627) -- (9.889,-0.671) -- (10.048,-0.698) -- (10.208,-0.707) -- (10.367,-0.698) -- (10.527,-0.672) -- (10.686,-0.629) -- (10.846,-0.569) -- (11.005,-0.495) -- (11.165,-0.409) -- (11.324,-0.312) -- (11.484,-0.207) -- (11.643,-0.097) -- (11.803,0.015) -- (11.962,0.127) -- (12.122,0.236) -- (12.281,0.339) -- (12.441,0.433) -- (12.6,0.517);
\node[lab, note, muted] at (6.3,1.25) {$\cos t$}; \node[lab, note, primary] at (9.6,-0.95) {$\tfrac1{\sqrt2}\cos(t-\tfrac\pi4)$};
\end{tikzpicture}
\end{center}
```

Input $\cos t$ and the periodic response of $y''+y'+2y=\cos t$: amplitude $1/|p(i)|$, lagging by $\arg p(i)=\pi/4$.

:::

::: {#def-lti-stability .definition name="Stability of a constant-coefficient system"}
The equation $p(D)y=q$ is *stable* if every solution of the homogeneous equation $p(D)y=0$ tends to $0$ as $t\to\infty$. Then all solutions with the same input approach each other, and the long-term response does not depend on the initial conditions.
:::

::: {#thm-stability-criterion .theorem name="Stability criterion"}
$p(D)y=q$ is stable if and only if every characteristic root has negative real part. For $p(s)=a_2s^2+a_1s+a_0$ with $a_2>0$ this holds if and only if $a_1>0$ and $a_0>0$.
:::

::: {.proof}
1. Each root $r$ of multiplicity $m$ contributes solutions $t^je^{rt}$, $j<m$ (as in @thm-second-order-characteristic-roots), and these tend to $0$ exactly when $\operatorname{Re}r<0$; every homogeneous solution is a combination of them.

2. For the quadratic, the roots satisfy $r_1+r_2=-a_1/a_2$ and $r_1r_2=a_0/a_2$.

3. If both roots are real and negative, or complex with negative real part $\operatorname{Re}r$, then $r_1+r_2<0$ and $r_1r_2>0$, so $a_1,a_0>0$.

4. Conversely, if $a_1,a_0>0$: complex roots have real part $-a_1/(2a_2)<0$; real roots have positive product, so equal signs, and negative sum, so both negative.
:::

::: {#fig-exponential-response-formula-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1]
\fill[tintA] (-2.4,-1.8) rectangle (0,1.8);
\draw[->] (-2.5,0) -- (1.6,0) node[lab, right] {$\operatorname{Re}s$};
\draw[->] (0,-1.9) -- (0,2) node[lab, above] {$\operatorname{Im}s$};
\node[lab, note, primary] at (-1.3,1.45) {stable};
\node[lab, note, muted] at (0.85,1.45) {unstable};
\node[lab, primary] at (-1,1.2) {$\times$};
\node[lab, primary] at (-1,-1.2) {$\times$};
\node[lab, primary] at (-1.8,0) {$\times$};
\node[lab, primary] at (-0.5,0) {$\times$};
\node[lab, accent] at (0.7,0.6) {$\times$}; \node[lab, accent] at (0.7,-0.6) {$\times$};
\end{tikzpicture}
\end{center}
```

A system is stable when all characteristic roots lie in the open left half-plane (shaded); one root with positive real part makes it unstable.

:::

::: {#rmk-exponential-response-formula-1 .remark name="Time invariance"}
Constant coefficients make the system *time invariant*: if $y(t)$ is the response to $q(t)$, then $y(t-a)$ is the response to $q(t-a)$. This is why a delayed input simply produces a delayed output, a fact used again for step and impulse inputs.
:::
