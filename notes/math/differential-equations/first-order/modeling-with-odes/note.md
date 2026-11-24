---
title: "Modelling with Differential Equations"
sources: [mit1803-1]
requires: [math/calculus/single-variable/integrals/separable-differential-equations]
status: draft
---

<!-- Added 2026-11-24 from MIT 18.03SC Differential Equations (Fall 2011), Session 1 (natural growth and decay, models), in our own wording; examples are ours, checked in Python. Separation of variables itself is in @sec-math-calculus-single-variable-integrals-separable-differential-equations. -->

A differential equation relates an unknown function to its derivatives. Most equations in this part come from a *model*: a statement about how fast a quantity changes, written down in symbols and then solved or analysed.

::: {#def-ode-order-solution .definition name="Ordinary differential equation, order, solution"}
An *ordinary differential equation* (ODE) for an unknown function $y(t)$ of one variable is an equation
$$
F\bigl(t, y, y', \dots, y^{(n)}\bigr) = 0 .
$$
Its *order* is the highest derivative $n$ that appears. A *solution* on an interval $I$ is a function $y$ that is $n$ times differentiable on $I$ and satisfies the equation at every $t\in I$. The *general solution* is a formula, with arbitrary constants, that gives every solution.
:::

::: {#def-initial-value-problem .definition name="Initial value problem"}
An *initial value problem* (IVP) is an ODE of order $n$ together with *initial conditions*
$$
y(t_0)=y_0,\quad y'(t_0)=y_1,\quad \dots,\quad y^{(n-1)}(t_0)=y_{n-1}.
$$
A first-order equation needs one condition, a second-order equation two.
:::

::: {#exm-natural-growth .example name="Natural growth and decay" related="exm-exponential-growth"}
If a quantity $x$ changes at a rate proportional to its size, then
$$
x' = kx,\qquad x(0)=x_0 ,
$$
with solution $x(t)=x_0e^{kt}$. For $k>0$ (a population with unlimited food, money at continuous interest) it grows; for $k<0$ (radioactive decay) it decays.

1. The *doubling time* for $k>0$ solves $e^{kT}=2$, so $T=\ln 2/k$.
2. The *half-life* for $k<0$ solves $e^{kT}=\tfrac12$, so $T=\ln 2/|k|$.

The constant $k$ has units of $1/\text{time}$; checking units is the first test of a model.
:::

::: {#fig-modeling-with-odes-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.4cm, y=1cm]
\draw[->] (0,0) -- (4.3,0) node[lab, right] {$t$};
\draw[->] (0,0) -- (0,3.4) node[lab, above] {$x$};
\draw[emph, primary] (0,1) -- (0.051,1.026) -- (0.101,1.052) -- (0.152,1.079) -- (0.203,1.107) -- (0.253,1.135) -- (0.304,1.164) -- (0.354,1.194) -- (0.405,1.224) -- (0.456,1.256) -- (0.506,1.288) -- (0.557,1.321) -- (0.608,1.355) -- (0.658,1.39) -- (0.709,1.425) -- (0.759,1.462) -- (0.81,1.499) -- (0.861,1.538) -- (0.911,1.577) -- (0.962,1.618) -- (1.013,1.659) -- (1.063,1.702) -- (1.114,1.745) -- (1.165,1.79) -- (1.215,1.836) -- (1.266,1.883) -- (1.316,1.931) -- (1.367,1.981) -- (1.418,2.032) -- (1.468,2.084) -- (1.519,2.137) -- (1.57,2.192) -- (1.62,2.248) -- (1.671,2.306) -- (1.722,2.365) -- (1.772,2.426) -- (1.823,2.488) -- (1.873,2.552) -- (1.924,2.617) -- (1.975,2.684) -- (2.025,2.753) -- (2.076,2.823) -- (2.127,2.896) -- (2.177,2.97) -- (2.228,3.046) -- (2.278,3.124) -- (2.329,3.205) -- (2.38,3.287);
\draw[emph, accent] (0,2.5) -- (0.051,2.438) -- (0.101,2.377) -- (0.152,2.317) -- (0.203,2.259) -- (0.253,2.203) -- (0.304,2.148) -- (0.354,2.094) -- (0.405,2.042) -- (0.456,1.991) -- (0.506,1.941) -- (0.557,1.892) -- (0.608,1.845) -- (0.658,1.799) -- (0.709,1.754) -- (0.759,1.71) -- (0.81,1.667) -- (0.861,1.626) -- (0.911,1.585) -- (0.962,1.545) -- (1.013,1.507) -- (1.063,1.469) -- (1.114,1.432) -- (1.165,1.397) -- (1.215,1.362) -- (1.266,1.328) -- (1.316,1.294) -- (1.367,1.262) -- (1.418,1.231) -- (1.468,1.2) -- (1.519,1.17) -- (1.57,1.141) -- (1.62,1.112) -- (1.671,1.084) -- (1.722,1.057) -- (1.772,1.031) -- (1.823,1.005) -- (1.873,0.98) -- (1.924,0.955) -- (1.975,0.931) -- (2.025,0.908) -- (2.076,0.885) -- (2.127,0.863) -- (2.177,0.842) -- (2.228,0.821) -- (2.278,0.8) -- (2.329,0.78) -- (2.38,0.761) -- (2.43,0.742) -- (2.481,0.723) -- (2.532,0.705) -- (2.582,0.687) -- (2.633,0.67) -- (2.684,0.653) -- (2.734,0.637) -- (2.785,0.621) -- (2.835,0.606) -- (2.886,0.591) -- (2.937,0.576) -- (2.987,0.561) -- (3.038,0.547) -- (3.089,0.534) -- (3.139,0.52) -- (3.19,0.507) -- (3.241,0.495) -- (3.291,0.482) -- (3.342,0.47) -- (3.392,0.458) -- (3.443,0.447) -- (3.494,0.436) -- (3.544,0.425) -- (3.595,0.414) -- (3.646,0.404) -- (3.696,0.394) -- (3.747,0.384) -- (3.797,0.374) -- (3.848,0.365) -- (3.899,0.356) -- (3.949,0.347) -- (4,0.338);
\draw[faint, dashed] (0,2) -- (1.386,2) -- (1.386,0);
\draw (1.386,0) -- (1.386,-0.08) node[below, lab, tick] {$T$};
\draw (0,1) -- (-0.08,1) node[left, lab, tick] {$x_0$};
\draw (0,2) -- (-0.08,2) node[left, lab, tick] {$2x_0$};
\node[lab, note, primary] at (3.4,2.9) {$k>0$}; \node[lab, note, accent] at (3.4,0.75) {$k<0$};
\end{tikzpicture}
\end{center}
```

Natural growth ($k=0.5$) and decay ($k=-0.5$). The growing curve doubles in the time $T=\ln2/k$; the decaying one halves in the same time.

:::

::: {#exm-newtons-cooling .example name="Newton's law of cooling"}
A body at temperature $T(t)$ in surroundings at constant temperature $T_e$ loses heat at a rate proportional to the temperature difference:
$$
T' = k\,(T_e - T),\qquad k>0 .
$$
The solution is $T(t)=T_e+(T(0)-T_e)e^{-kt}$: the difference from the surroundings decays exponentially.

Coffee at $90^\circ$C in a room at $20^\circ$C cools to $60^\circ$C in 10 minutes.

1. From $70e^{-10k}=40$ we get $k=\ln(7/4)/10\approx 0.0560$ per minute.
2. After 20 minutes the difference is $70\,(4/7)^2=40\cdot 4/7$, so $T(20)\approx 42.9^\circ$C.
:::

::: {#fig-modeling-with-odes-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.17cm, y=0.04cm]
\draw[->] (0,0) -- (42,0) node[lab, right] {$t$};
\draw[->] (0,0) -- (0,98) node[lab, above] {$T$};
\draw[faint, dashed] (0,20) -- (40,20);
\draw[emph, primary] (0,90) -- (0.506,88.044) -- (1.013,86.143) -- (1.519,84.296) -- (2.025,82.499) -- (2.532,80.753) -- (3.038,79.056) -- (3.544,77.406) -- (4.051,75.802) -- (4.557,74.243) -- (5.063,72.728) -- (5.57,71.255) -- (6.076,69.823) -- (6.582,68.431) -- (7.089,67.078) -- (7.595,65.763) -- (8.101,64.484) -- (8.608,63.241) -- (9.114,62.033) -- (9.62,60.859) -- (10.127,59.718) -- (10.633,58.608) -- (11.139,57.529) -- (11.646,56.481) -- (12.152,55.462) -- (12.658,54.471) -- (13.165,53.508) -- (13.671,52.572) -- (14.177,51.662) -- (14.684,50.777) -- (15.19,49.918) -- (15.696,49.082) -- (16.203,48.269) -- (16.709,47.48) -- (17.215,46.712) -- (17.722,45.966) -- (18.228,45.24) -- (18.734,44.535) -- (19.241,43.85) -- (19.747,43.183) -- (20.253,42.536) -- (20.759,41.906) -- (21.266,41.294) -- (21.772,40.699) -- (22.278,40.121) -- (22.785,39.559) -- (23.291,39.012) -- (23.797,38.481) -- (24.304,37.965) -- (24.81,37.463) -- (25.316,36.975) -- (25.823,36.501) -- (26.329,36.04) -- (26.835,35.592) -- (27.342,35.156) -- (27.848,34.733) -- (28.354,34.321) -- (28.861,33.921) -- (29.367,33.532) -- (29.873,33.154) -- (30.38,32.787) -- (30.886,32.429) -- (31.392,32.082) -- (31.899,31.745) -- (32.405,31.416) -- (32.911,31.098) -- (33.418,30.787) -- (33.924,30.486) -- (34.43,30.193) -- (34.937,29.908) -- (35.443,29.632) -- (35.949,29.362) -- (36.456,29.101) -- (36.962,28.847) -- (37.468,28.6) -- (37.975,28.359) -- (38.481,28.126) -- (38.987,27.899) -- (39.494,27.678) -- (40,27.464);
\draw[emph, accent] (0,5) -- (0.506,5.419) -- (1.013,5.826) -- (1.519,6.222) -- (2.025,6.607) -- (2.532,6.981) -- (3.038,7.345) -- (3.544,7.699) -- (4.051,8.042) -- (4.557,8.376) -- (5.063,8.701) -- (5.57,9.017) -- (6.076,9.324) -- (6.582,9.622) -- (7.089,9.912) -- (7.595,10.194) -- (8.101,10.468) -- (8.608,10.734) -- (9.114,10.993) -- (9.62,11.244) -- (10.127,11.489) -- (10.633,11.727) -- (11.139,11.958) -- (11.646,12.183) -- (12.152,12.401) -- (12.658,12.613) -- (13.165,12.82) -- (13.671,13.02) -- (14.177,13.215) -- (14.684,13.405) -- (15.19,13.589) -- (15.696,13.768) -- (16.203,13.942) -- (16.709,14.112) -- (17.215,14.276) -- (17.722,14.436) -- (18.228,14.591) -- (18.734,14.742) -- (19.241,14.889) -- (19.747,15.032) -- (20.253,15.171) -- (20.759,15.306) -- (21.266,15.437) -- (21.772,15.564) -- (22.278,15.688) -- (22.785,15.809) -- (23.291,15.926) -- (23.797,16.04) -- (24.304,16.15) -- (24.81,16.258) -- (25.316,16.362) -- (25.823,16.464) -- (26.329,16.563) -- (26.835,16.659) -- (27.342,16.752) -- (27.848,16.843) -- (28.354,16.931) -- (28.861,17.017) -- (29.367,17.1) -- (29.873,17.181) -- (30.38,17.26) -- (30.886,17.337) -- (31.392,17.411) -- (31.899,17.483) -- (32.405,17.554) -- (32.911,17.622) -- (33.418,17.688) -- (33.924,17.753) -- (34.43,17.816) -- (34.937,17.877) -- (35.443,17.936) -- (35.949,17.994) -- (36.456,18.05) -- (36.962,18.104) -- (37.468,18.157) -- (37.975,18.209) -- (38.481,18.259) -- (38.987,18.307) -- (39.494,18.355) -- (40,18.401);
\node[dot] at (10,60) {}; \node[dot] at (20,42.857) {};
\node[lab, note, right] at (10,63) {$(10,60)$}; \node[lab, note, right] at (20,46) {$(20,42.9)$};
\draw (0,90) -- (-0.08,90) node[left, lab, tick] {$90$};
\draw (0,20) -- (-0.08,20) node[left, lab, tick] {$20$};
\draw (0,5) -- (-0.08,5) node[left, lab, tick] {$5$};
\draw (10,0) -- (10,-0.08) node[below, lab, tick] {$10$};
\draw (20,0) -- (20,-0.08) node[below, lab, tick] {$20$};
\draw (40,0) -- (40,-0.08) node[below, lab, tick] {$40$};
\end{tikzpicture}
\end{center}
```

Newton's law of cooling in a room at $20^\circ$C: the hot coffee cools and a cold drink at $5^\circ$C warms, both approaching the room temperature exponentially.

:::

::: {#rmk-modeling-with-odes-1 .remark name="The modelling loop"}
A model is built in four steps: choose the variables and their units; write the rate of change as a function of the state (a *rate law*); solve or analyse the equation; compare with data and revise. The equations of this part are deliberately simple, so their solutions can be understood completely and then reused as building blocks.
:::
