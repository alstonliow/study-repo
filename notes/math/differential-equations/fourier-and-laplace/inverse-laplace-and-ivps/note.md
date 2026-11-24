---
title: "Inverse Laplace Transforms and Initial Value Problems"
sources: [mit1803-28, mit1803-29]
requires: [math/differential-equations/fourier-and-laplace/laplace-transform, math/calculus/single-variable/integration-techniques/partial-fractions]
status: draft
---

<!-- Added 2026-11-24 from MIT 18.03SC Differential Equations (Fall 2011), Sessions 28 (partial fractions and the inverse Laplace transform) and 29 (solving initial value problems), in our own wording; examples are ours, checked in Python; proofs written out in steps. Partial fractions themselves (and the cover-up method) are in @sec-math-calculus-single-variable-integration-techniques-partial-fractions. -->

To solve an equation by Laplace transform, transform it, solve for $X(s)$, and read the solution back off a table. Partial fractions reduce every rational $X(s)$ to table entries.

::: {#prp-laplace-uniqueness .proposition name="Inverse Laplace transform"}
Two continuous functions on $t\ge0$ of exponential type with the same Laplace transform are equal. So a rational function $F(s)$ that is a *proper* fraction determines its *inverse transform* $f=\mathcal L^{-1}(F)$, found by writing $F$ in partial fractions and inverting each term with @prp-laplace-table and the s-shift:
$$
\mathcal L^{-1}\frac{1}{(s-a)^k}=\frac{t^{k-1}}{(k-1)!}e^{at},\qquad \mathcal L^{-1}\frac{s-a}{(s-a)^2+\omega^2}=e^{at}\cos\omega t,\qquad \mathcal L^{-1}\frac{\omega}{(s-a)^2+\omega^2}=e^{at}\sin\omega t .
$$
:::

::: {#thm-laplace-ivp .theorem name="Solving an IVP by Laplace transform"}
Let $p(D)x=f$ with $p(s)=ms^2+bs+k$, $x(0)=x_0$, $x'(0)=x_1$. Then
$$
X(s)=\frac{F(s)+m\,(sx_0+x_1)+b\,x_0}{p(s)} ,
$$
and $x=\mathcal L^{-1}(X)$.

```{=latex}
\begin{algorithm}
\caption{Solving $p(D)x=f$ with initial values by Laplace transform}
\begin{algorithmic}
\INPUT $p$, input $f$, initial values $x(0),x'(0),\dots$
\STATE transform: replace $x^{(k)}$ by $s^kX-s^{k-1}x(0)-\dots-x^{(k-1)}(0)$ and $f$ by $F(s)$
\STATE solve the algebraic equation for $X(s)$
\STATE write $X(s)$ in partial fractions (completing squares for complex roots)
\STATE invert each term with the table and the shift rules
\RETURN $x(t)=\mathcal L^{-1}(X)$
\end{algorithmic}
\end{algorithm}
```

:::

::: {.proof}
1. Transform each term with the t-derivative rule (@prp-laplace-rules): $m\bigl(s^2X-sx_0-x_1\bigr)+b\bigl(sX-x_0\bigr)+kX=F$.

2. Collect the terms with $X$: $p(s)X=F+m(sx_0+x_1)+bx_0$, and divide by $p(s)$.

3. By @prp-laplace-uniqueness the solution is the inverse transform of $X$.
:::

::: {#fig-inverse-laplace-and-ivps-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (a) at (0,1.5) {ODE for $x(t)$\\ with $x(0),x'(0)$};
\node[box] (b) at (5,1.5) {algebraic\\ equation for $X(s)$};
\node[box] (c) at (5,0) {$X(s)$ in\\ partial fractions};
\node[hl box] (d) at (0,0) {solution $x(t)$};
\draw[map] (a) -- (b) node[midway, above, lab, note] {$\mathcal L$};
\draw[map] (b) -- (c) node[midway, right, lab, note] {solve};
\draw[map] (c) -- (d) node[midway, below, lab, note] {$\mathcal L^{-1}$ (table)};
\end{tikzpicture}
\end{center}
```

Solving an initial value problem by Laplace transform: the detour through the $s$-domain replaces calculus by algebra.

:::

::: {#exm-laplace-ivp-step .example name="A step input"}
Solve $x''+3x'+2x=1$ with $x(0)=x'(0)=0$.

1. $X=\dfrac{1}{s(s+1)(s+2)}$.
2. By the cover-up method, $X=\dfrac{1/2}{s}-\dfrac{1}{s+1}+\dfrac{1/2}{s+2}$.
3. Hence $x=\tfrac12-e^{-t}+\tfrac12e^{-2t}$.
:::

::: {#fig-inverse-laplace-and-ivps-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=4cm]
\draw[->] (0,0) -- (6.4,0) node[lab, right] {$t$};
\draw[->] (0,0) -- (0,0.65) node[lab, above] {$x$};
\draw[faint, dashed] (0,0.5) -- (6,0.5);
\draw[emph, primary] (0,0) -- (0.076,0.003) -- (0.152,0.01) -- (0.228,0.021) -- (0.304,0.034) -- (0.38,0.05) -- (0.456,0.067) -- (0.532,0.085) -- (0.608,0.104) -- (0.684,0.123) -- (0.759,0.142) -- (0.835,0.16) -- (0.911,0.179) -- (0.987,0.197) -- (1.063,0.214) -- (1.139,0.231) -- (1.215,0.247) -- (1.291,0.263) -- (1.367,0.278) -- (1.443,0.292) -- (1.519,0.305) -- (1.595,0.318) -- (1.671,0.33) -- (1.747,0.341) -- (1.823,0.351) -- (1.899,0.361) -- (1.975,0.371) -- (2.051,0.38) -- (2.127,0.388) -- (2.203,0.396) -- (2.278,0.403) -- (2.354,0.41) -- (2.43,0.416) -- (2.506,0.422) -- (2.582,0.427) -- (2.658,0.432) -- (2.734,0.437) -- (2.81,0.442) -- (2.886,0.446) -- (2.962,0.45) -- (3.038,0.453) -- (3.114,0.457) -- (3.19,0.46) -- (3.266,0.463) -- (3.342,0.465) -- (3.418,0.468) -- (3.494,0.47) -- (3.57,0.472) -- (3.646,0.474) -- (3.722,0.476) -- (3.797,0.478) -- (3.873,0.479) -- (3.949,0.481) -- (4.025,0.482) -- (4.101,0.484) -- (4.177,0.485) -- (4.253,0.486) -- (4.329,0.487) -- (4.405,0.488) -- (4.481,0.489) -- (4.557,0.49) -- (4.633,0.49) -- (4.709,0.491) -- (4.785,0.492) -- (4.861,0.492) -- (4.937,0.493) -- (5.013,0.493) -- (5.089,0.494) -- (5.165,0.494) -- (5.241,0.495) -- (5.316,0.495) -- (5.392,0.495) -- (5.468,0.496) -- (5.544,0.496) -- (5.62,0.496) -- (5.696,0.497) -- (5.772,0.497) -- (5.848,0.497) -- (5.924,0.497) -- (6,0.498);
\draw (0,0.5) -- (-0.08,0.5) node[left, lab, tick] {$\tfrac12$};
\end{tikzpicture}
\end{center}
```

The step response $\tfrac12-e^{-t}+\tfrac12e^{-2t}$ of $x''+3x'+2x$: it rises from rest with zero slope to the steady value $\tfrac12$.

:::

::: {#exm-laplace-ivp-complex .example name="Complex roots"}
Solve $x''+2x'+5x=0$ with $x(0)=0$, $x'(0)=1$. Then $X=\dfrac{1}{s^2+2s+5}=\dfrac12\cdot\dfrac{2}{(s+1)^2+4}$, so $x=\tfrac12e^{-t}\sin2t$. Completing the square replaces the partial fractions with complex roots.
:::

::: {#rmk-inverse-laplace-and-ivps-1 .remark name="Why the method is popular"}
The initial conditions enter at the start rather than at the end, discontinuous and impulsive inputs are handled by the t-shift rule and $\mathcal L(\delta)=1$, and the denominator $p(s)$ shows the system's characteristic roots directly.
:::
