---
title: "Step and Delta Functions"
sources: [mit1803-24]
requires: [math/differential-equations/first-order/first-order-linear-equations, math/calculus/single-variable/integrals/fundamental-theorem]
status: draft
---

<!-- Added 2026-11-24 from MIT 18.03SC Differential Equations (Fall 2011), Session 24 (the unit step, the delta function, generalized derivatives, rest initial conditions), in our own wording; examples are ours, checked in Python. The delta function is treated informally, as in the course. -->

Switches and blows are idealised by the unit step and the delta function. The delta function is not a function in the ordinary sense, but it obeys simple rules that make it a convenient input.

::: {#def-unit-step .definition name="Unit step function"}
The *unit step* (Heaviside function) is
$$
u(t)=\begin{cases}0,&t<0,\\1,&t>0.\end{cases}
$$
The function $u(t-a)$ switches on at time $a$, and $u(t-a)-u(t-b)$ is the indicator of the window $a<t<b$. *Rest initial conditions* for a system with input $q$ mean that $q(t)=0$ and $y(t)=0$ for all $t<0$.
:::

::: {#def-delta-function .definition name="Delta function"}
The *delta function* $\delta(t)$ is the limit as $h\to0^+$ of the boxes $\frac1h\bigl(u(t)-u(t-h)\bigr)$ of area $1$. It is characterised by
$$
\delta(t)=0\ \ (t\neq0),\qquad \int_{a}^{b}f(t)\,\delta(t-c)\,dt=f(c)\quad(a<c<b)
$$
for continuous $f$ (the *sifting property*). It models a unit impulse delivered at one instant.
:::

::: {#fig-step-and-delta-functions-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.6cm, y=0.75cm]
\draw[->] (-0.4,0) -- (2.4,0) node[lab, right] {$t$};
\draw[->] (0,0) -- (0,4.6) node[lab, above] {};
\draw[emph, muted] (-0.3,0) -- (0,0) -- (0,1.0) -- (1,1.0) -- (1,0) -- (2.2,0);
\draw[emph, primary] (-0.3,0) -- (0,0) -- (0,2.0) -- (0.5,2.0) -- (0.5,0) -- (2.2,0);
\draw[emph, accent] (-0.3,0) -- (0,0) -- (0,4.0) -- (0.25,4.0) -- (0.25,0) -- (2.2,0);
\node[lab, note, muted] at (1.2,1.25) {$h=1$}; \node[lab, note, primary] at (0.85,2.25) {$h=\tfrac12$}; \node[lab, note, accent] at (0.65,4.15) {$h=\tfrac14$};
\draw (0,1) -- (-0.08,1) node[left, lab, tick] {$1$};
\draw (0,2) -- (-0.08,2) node[left, lab, tick] {$2$};
\draw (0,4) -- (-0.08,4) node[left, lab, tick] {$4$};
\end{tikzpicture}
\end{center}
```

Boxes of width $h$ and height $1/h$, each of area $1$. As $h\to0$ they approach the delta function.

:::

::: {#def-generalized-derivative .definition name="Generalized derivative"}
If $f$ is piecewise differentiable with jumps $J_k=f(c_k^+)-f(c_k^-)$ at points $c_k$, its *generalized derivative* is
$$
f'(t)=f'_r(t)+\sum_kJ_k\,\delta(t-c_k),
$$
where $f'_r$ is the ordinary derivative away from the jumps. In particular $u'(t)=\delta(t)$, consistent with $\int_{-\infty}^t\delta(s)\,ds=u(t)$.
:::

::: {#exm-generalized-derivative .example name="A generalized derivative"}
Let $f(t)=u(t-1)\cdot2t$, which is $0$ for $t<1$ and $2t$ for $t>1$. It jumps by $2$ at $t=1$, so
$$
f'(t)=2u(t-1)+2\,\delta(t-1).
$$
:::

::: {#fig-step-and-delta-functions-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.5cm, y=0.55cm]
\draw[->] (-0.4,0) -- (3.2,0) node[lab, right] {$t$};
\draw[->] (0,-0.4) -- (0,6.3) node[lab, above] {};
\draw[emph, primary] (-0.3,0) -- (1,0); \draw[emph, primary] (1,2) -- (2.8,5.6);
\node[hollow dot] at (1,0) {}; \node[dot] at (1,2) {};
\draw[emph, accent] (1.03,0) -- (1.03,0); \draw[->, hl] (1,0) -- (1,2);
\draw[emph, accent] (1,2) -- (2.8,2);
\node[lab, note, primary] at (2.4,5.2) {$f$}; \node[lab, note, accent] at (2.4,2.3) {$f'$: $2u(t-1)$};
\node[lab, note, accent, left] at (0.95,1.2) {$2\delta(t-1)$};
\draw (1,0) -- (1,-0.08) node[below, lab, tick] {$1$};
\draw (0,2) -- (-0.08,2) node[left, lab, tick] {$2$};
\end{tikzpicture}
\end{center}
```

The function $f=u(t-1)\cdot2t$ jumps by $2$ at $t=1$; its generalized derivative is $2u(t-1)$ plus the impulse $2\delta(t-1)$ (arrow).

:::

::: {#exm-impulse-first-order .example name="An impulse into a first-order system"}
Money in an account with continuous interest rate $k$ and a deposit of $D$ at time $t=a$: $y'-ky=D\,\delta(t-a)$ with $y=0$ for $t<a$. Integrating across $t=a$ shows that $y$ jumps by $D$; afterwards $y'=ky$, so
$$
y(t)=D\,u(t-a)\,e^{k(t-a)} .
$$
An impulse into a first-order system acts as a sudden change of initial condition.
:::
