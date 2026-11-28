---
title: "The Lebesgue–Stieltjes Integral"
sources: [camiii-sc-1]
requires: [math/probability/martingales/radon-nikodym]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part III Stochastic Calculus and Applications (lecture notes), Section 1, in our own wording; proofs written out in steps. -->

For $C^1$ functions $h,a$ one defines $\int h\,da=\int ha'\,dx$. Without differentiability the integrator $a$ must be turned into a measure; since $a'$ may change sign, the measure has to be signed.

::: {#def-signed-measure .definition name="Signed measure, total variation measure"}

A *signed measure* on $[0,T]$ is a difference $\mu=\mu^+-\mu^-$ of two finite positive measures with disjoint supports (the *Hahn decomposition*). Its *total variation* is $|\mu|=\mu^++\mu^-$.

:::

::: {#prp-difference-of-measures .proposition name="Any two finite measures have a signed difference"}

For finite measures $\mu_1,\mu_2$ there is a signed measure $\mu$ with $\mu(A)=\mu_1(A)-\mu_2(A)$.

:::

::: {.proof}

1. Put $\nu=\mu_1+\mu_2$. By the Radon–Nikodym theorem (@thm-radon-nikodym) $\mu_i(dt)=f_i(t)\,\nu(dt)$ with $f_i\ge0$.

2. Then $(\mu_1-\mu_2)(dt)=(f_1-f_2)^+\,d\nu-(f_1-f_2)^-\,d\nu$, and the two parts live on the disjoint sets $\{f_1>f_2\}$ and $\{f_1<f_2\}$.

:::

::: {#def-bounded-variation-function .definition name="Total variation of a function, BV, càdlàg"}

The *total variation* of $a:[0,T]\to\mathbb R$ is
$$V_a(T)=|a(0)|+\sup\Big\{\sum_{i=1}^n|a(t_i)-a(t_{i-1})|:0=t_0<\dots<t_n=T\Big\},$$
and $a$ has *bounded variation* ($a\in BV$) if $V_a(T)<\infty$. A function is *càdlàg* if it is right-continuous with left limits. A càdlàg $a:[0,\infty)\to\mathbb R$ has *finite variation* if $a|_{[0,T]}\in BV$ for every $T$.

:::

::: {#thm-bv-signed-measures .theorem name="Càdlàg BV functions are signed measures"}

The map $\mu\mapsto a(t)=\mu([0,t])$ is a bijection between signed measures on $[0,T]$ and càdlàg functions of bounded variation on $[0,T]$. The inverse sets $a^\pm=\tfrac12(V_a\pm a)$ and $\mu^\pm[0,t]=a^\pm(t)-a^\pm(0)$. Moreover $|\mu|[0,t]=V_a(t)$.

:::

::: {#exm-two-point-measure .example name="A jump function"}

Let $a=\mathbf 1_{[0,1/2)}$ on $[0,1]$ (càdlàg with $a(0)=1$). Its total variation is $V_a(1)=|a(0)|+|a(1/2)-a(1/2^-)|=1+1=2$. The associated measure is $\mu=\delta_0-\delta_{1/2}$ and $|\mu|=\delta_0+\delta_{1/2}$.

:::

::: {#fig-lebesgue-stieltjes-integral-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-0.3,0) -- (4.3,0);
\draw[emph] (0,1) -- (2,1);
\draw[emph] (2,0) -- (4,0);
\node[small vertex] at (0,1) {};
\node[tick] at (2,-0.3) {$\tfrac12$};
\node[tick] at (-0.5,1) {$a$};
\draw[hl, ->] (6.2,0) -- (6.2,1);
\draw[hl, ->] (7.8,0) -- (7.8,-1);
\node[tick] at (6.2,-0.3) {$0$};
\node[tick] at (7.8,0.3) {$\tfrac12$};
\node[lab, text=accent] at (7.0,1.5) {$\mu=\delta_0-\delta_{1/2}$};
\end{tikzpicture}
\end{center}
```

The càdlàg step function $a=\mathbf 1_{[0,1/2)}$ and its signed measure: a unit mass at $0$ and a negative unit mass at the downward jump $\tfrac12$.

:::

::: {#def-lebesgue-stieltjes .definition name="Lebesgue–Stieltjes integral"}

For a càdlàg BV function $a$ with signed measure $\mu$ and $h\in L^1(|\mu|)$,
$$\int_s^th(r)\,da(r)=\int_{(s,t]}h\,d\mu,\qquad\int_s^th(r)\,|da(r)|=\int_{(s,t]}h\,d|\mu|,$$
and $(h\cdot a)(t)=\int_0^th\,da$.

:::

Then $\big|\int h\,da\big|\le\int|h|\,|da|$, and $h\cdot a$ is again càdlàg and BV with measure $h\,d\mu$ and total variation measure $|h|\,d|\mu|$.

::: {#prp-riemann-stieltjes .proposition name="Riemann–Stieltjes sums"}

If $a$ is càdlàg BV and $h$ is bounded and left-continuous, then for subdivisions $0=t_0^{(m)}<\dots<t_{n_m}^{(m)}=t$ with mesh tending to $0$,
$$\int_0^th\,da=\lim_{m\to\infty}\sum_{i=1}^{n_m}h\big(t_{i-1}^{(m)}\big)\Big(a\big(t_i^{(m)}\big)-a\big(t_{i-1}^{(m)}\big)\Big).$$

:::

::: {.proof}

1. Define $h_m(s)=h(t_{i-1}^{(m)})$ for $s\in(t_{i-1}^{(m)},t_i^{(m)}]$. The sum above is exactly $\int_{(0,t]}h_m\,d\mu$.

2. By left-continuity $h_m(s)\to h(s)$ for every $s$, and $|h_m|\le\sup|h|$, which is $|\mu|$-integrable.

3. Dominated convergence gives $\int h_m\,d\mu\to\int h\,d\mu$.

:::

The left endpoint matters: for integrators with jumps another evaluation point changes the limit. This is the form that the stochastic integral keeps, with $a$ replaced by a martingale (@sec-math-probability-stochastic-calculus-ito-integral).
