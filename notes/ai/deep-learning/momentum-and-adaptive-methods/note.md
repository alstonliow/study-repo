---
title: "Momentum, Adaptive Learning Rates and Adam"
sources: [cs231n-7, cs231na-1]
requires: [ai/machine-learning/convex-optimization]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS231n course notes (Neural networks part 3: parameter updates, momentum, Nesterov momentum, learning rate annealing, second-order methods, Adagrad, RMSprop, Adam) and Assignment 1 (update rules), in our own wording; the propositions and their proofs are our own; the numbers were computed in Python. -->

Stochastic gradient descent (@def-stochastic-gradient-descent) uses one learning rate for all parameters and only the current minibatch gradient. On the ravine-shaped losses of networks, steep in some directions and flat in others, it oscillates across the ravine and crawls along it. Two ideas help: average past gradients (*momentum*), and scale each parameter's step by the size of its past gradients (*adaptive learning rates*). Write $\mathbf{g}_t$ for the minibatch gradient at step $t$; operations on vectors are elementwise.

::: {#prp-momentum-velocity-form .proposition name="Momentum in velocity form" related="def-heavy-ball-momentum"}

With *velocity* $\mathbf{v}_0=\mathbf 0$, momentum $\mu\in[0,1)$ and learning rate $\eta$, the update

$$
\mathbf{v}_{t+1}=\mu\mathbf{v}_t-\eta\,\mathbf{g}_t,\qquad \boldsymbol\theta_{t+1}=\boldsymbol\theta_t+\mathbf{v}_{t+1}
$$

is the heavy ball method of @def-heavy-ball-momentum with $s=\eta$ and $\beta=\mu$. If $\mathbf{g}_t=\mathbf{g}$ for all $t$, then $\mathbf{v}_t=-\eta\frac{1-\mu^t}{1-\mu}\mathbf{g}\to-\frac{\eta}{1-\mu}\mathbf{g}$.

:::

::: {.proof}

1. From the second equation, $\mathbf{v}_t=\boldsymbol\theta_t-\boldsymbol\theta_{t-1}$ for $t\ge1$. Substituting in the first gives $\boldsymbol\theta_{t+1}=\boldsymbol\theta_t-\eta\mathbf{g}_t+\mu(\boldsymbol\theta_t-\boldsymbol\theta_{t-1})$, the heavy ball update.
2. With constant $\mathbf{g}$, unrolling gives $\mathbf{v}_t=-\eta(1+\mu+\dots+\mu^{t-1})\mathbf{g}=-\eta\frac{1-\mu^t}{1-\mu}\mathbf{g}$, which tends to $-\frac{\eta}{1-\mu}\mathbf{g}$ since $\mu^t\to0$.

:::

So in a direction where the gradient keeps its sign, momentum $\mu=0.9$ moves up to ten times faster than plain SGD, while in a direction where it alternates, successive contributions cancel. *Nesterov momentum* evaluates the gradient at the look-ahead point $\boldsymbol\theta_t+\mu\mathbf{v}_t$ instead of at $\boldsymbol\theta_t$; it is usually slightly better.

::: {#def-adagrad-rmsprop .definition name="AdaGrad and RMSProp"}

With a small $\varepsilon>0$ (say $10^{-8}$), *AdaGrad* keeps the sum of squared gradients and *RMSProp* a moving average of them, with decay rate $\rho$ (say $0.99$):

$$
\text{AdaGrad: }\ \mathbf{c}_t=\mathbf{c}_{t-1}+\mathbf{g}_t^2,\qquad \text{RMSProp: }\ \mathbf{c}_t=\rho\,\mathbf{c}_{t-1}+(1-\rho)\,\mathbf{g}_t^2,
$$

with $\mathbf{c}_0=\mathbf 0$, and both update $\boldsymbol\theta_{t+1}=\boldsymbol\theta_t-\eta\,\mathbf{g}_t/(\sqrt{\mathbf{c}_t}+\varepsilon)$.

:::

::: {#prp-adagrad-decay .proposition name="AdaGrad's steps shrink"}

Under AdaGrad the effective learning rate $\eta/(\sqrt{c_{t,j}}+\varepsilon)$ of each parameter $j$ is non-increasing in $t$. If $g_{t,j}=g\ne0$ for all $t$, the step in coordinate $j$ is about $\eta/\sqrt t$, which tends to $0$. Under RMSProp with constant $g_{t,j}=g$, the step tends to $\eta\,\lvert g\rvert/(\lvert g\rvert+\varepsilon)\approx\eta$.

:::

::: {.proof}

1. $c_{t,j}=\sum_{s\le t}g_{s,j}^2$ never decreases, so $\eta/(\sqrt{c_{t,j}}+\varepsilon)$ never increases.
2. With constant $g$, $c_{t,j}=tg^2$, so the step is $\eta\lvert g\rvert/(\sqrt t\lvert g\rvert+\varepsilon)\approx\eta/\sqrt t$: $1,\ 0.5,\ 0.1$ times $\eta$ at $t=1,4,100$.
3. For RMSProp, $c_{t,j}=(1-\rho^t)g^2\to g^2$, so the step tends to $\eta\lvert g\rvert/(\lvert g\rvert+\varepsilon)$.

:::

Steep directions (large past gradients) get small steps and flat ones large steps, which equalizes progress across the ravine. AdaGrad's monotone decay can stop learning too early in long non-convex training; RMSProp forgets old gradients and avoids this.

::: {#def-adam .definition name="Adam"}

*Adam* with rates $\beta_1,\beta_2\in[0,1)$ (say $0.9$ and $0.999$), $\mathbf{m}_0=\mathbf{v}_0=\mathbf 0$ and steps $t=1,2,\dots$ computes

$$
\mathbf{m}_t=\beta_1\mathbf{m}_{t-1}+(1-\beta_1)\mathbf{g}_t,\qquad \mathbf{v}_t=\beta_2\mathbf{v}_{t-1}+(1-\beta_2)\mathbf{g}_t^2,
$$

$$
\hat{\mathbf{m}}_t=\frac{\mathbf{m}_t}{1-\beta_1^t},\qquad \hat{\mathbf{v}}_t=\frac{\mathbf{v}_t}{1-\beta_2^t},\qquad \boldsymbol\theta_{t+1}=\boldsymbol\theta_t-\eta\,\frac{\hat{\mathbf{m}}_t}{\sqrt{\hat{\mathbf{v}}_t}+\varepsilon}.
$$

:::

```{=latex}
\begin{algorithm}
\caption{Adam}
\begin{algorithmic}
\INPUT initial $\boldsymbol\theta$, gradient oracle, $\eta,\beta_1,\beta_2,\varepsilon$, number $T$ of steps
\OUTPUT final $\boldsymbol\theta$
\STATE $\mathbf{m}\gets\mathbf0$; $\mathbf{v}\gets\mathbf0$
\FOR{$t=1$ \TO $T$}
    \STATE $\mathbf{g}\gets$ minibatch gradient at $\boldsymbol\theta$
    \STATE $\mathbf{m}\gets\beta_1\mathbf{m}+(1-\beta_1)\mathbf{g}$; $\mathbf{v}\gets\beta_2\mathbf{v}+(1-\beta_2)\mathbf{g}^2$
    \STATE $\hat{\mathbf{m}}\gets\mathbf{m}/(1-\beta_1^t)$; $\hat{\mathbf{v}}\gets\mathbf{v}/(1-\beta_2^t)$
    \STATE $\boldsymbol\theta\gets\boldsymbol\theta-\eta\,\hat{\mathbf{m}}/(\sqrt{\hat{\mathbf{v}}}+\varepsilon)$
\ENDFOR
\RETURN $\boldsymbol\theta$
\end{algorithmic}
\end{algorithm}
```

::: {#prp-adam-bias-correction .proposition name="Bias correction"}

If $\mathbf{g}_t=\mathbf{g}$ for all $t$, then $\mathbf{m}_t=(1-\beta_1^t)\mathbf{g}$ and $\mathbf{v}_t=(1-\beta_2^t)\mathbf{g}^2$, so $\hat{\mathbf{m}}_t=\mathbf{g}$ and $\hat{\mathbf{v}}_t=\mathbf{g}^2$ at every step, and (with $\varepsilon=0$) each coordinate with $g_j\ne0$ moves by exactly $\eta$ against the sign of $g_j$.

:::

::: {.proof}

1. Unrolling with $\mathbf{m}_0=\mathbf 0$: $\mathbf{m}_t=(1-\beta_1)\sum_{s=1}^{t}\beta_1^{t-s}\mathbf{g}_s$. For constant $\mathbf{g}$ this is $(1-\beta_1)\frac{1-\beta_1^t}{1-\beta_1}\mathbf{g}=(1-\beta_1^t)\mathbf{g}$.
2. The same computation with $\beta_2$ and $\mathbf{g}^2$ gives $\mathbf{v}_t=(1-\beta_2^t)\mathbf{g}^2$.
3. Dividing, $\hat{\mathbf{m}}_t=\mathbf{g}$, $\hat{\mathbf{v}}_t=\mathbf{g}^2$, and the step is $\eta\,g_j/\lvert g_j\rvert$.

:::

::: {#fig-momentum-and-adaptive-methods-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (6.4,0) node[lab, right] {$t$};
\draw[emph] (0.000,0.000) -- (0.200,0.200) -- (0.400,0.380) -- (0.600,0.542) -- (0.800,0.688) -- (1.000,0.819) -- (1.200,0.937) -- (1.400,1.043) -- (1.600,1.139) -- (1.800,1.225) -- (2.000,1.303) -- (2.200,1.372) -- (2.400,1.435) -- (2.600,1.492) -- (2.800,1.542) -- (3.000,1.588) -- (3.200,1.629) -- (3.400,1.666) -- (3.600,1.700) -- (3.800,1.730) -- (4.000,1.757) -- (4.200,1.781) -- (4.400,1.803) -- (4.600,1.823) -- (4.800,1.840) -- (5.000,1.856) -- (5.200,1.871) -- (5.400,1.884) -- (5.600,1.895) -- (5.800,1.906) -- (6.000,1.915);
\draw[hl] (0.2,2) -- (6,2);
\draw (0,2) -- (-0.08,2) node[tick, left] {$1$};
\draw (2,0) -- (2,-0.08) node[tick, below] {$10$};
\draw (6,0) -- (6,-0.08) node[tick, below] {$30$};
\node[tick] at (2.6,1.25) {$\mathbf m_t=1-\beta_1^t$};
\node[tick, text=accent] at (4.2,2.25) {$\hat{\mathbf m}_t=\mathbf m_t/(1-\beta_1^t)$};
\end{tikzpicture}
\end{center}
```

With a constant gradient $1$ and $\beta_1=0.9$, the moving average $\mathbf m_t$ starts at $0$ and is biased low for the first steps; dividing by $1-\beta_1^t$ removes the bias

:::

::: {#fig-momentum-and-adaptive-methods-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[faint] (0,0) ellipse (1.000 and 0.224);
\draw[faint] (0,0) ellipse (2.000 and 0.447);
\draw[faint] (0,0) ellipse (3.000 and 0.671);
\draw[faint] (0,0) ellipse (4.000 and 0.894);
\draw[faint, ->] (-4.000,1.000) -- (-3.640,-0.800) -- (-3.312,0.640) -- (-3.014,-0.512) -- (-2.743,0.410) -- (-2.496,-0.328) -- (-2.271,0.262) -- (-2.067,-0.210) -- (-1.881,0.168) -- (-1.712,-0.134) -- (-1.558,0.107) -- (-1.417,-0.086) -- (-1.290,0.069) -- (-1.174,-0.055) -- (-1.068,0.044) -- (-0.972,-0.035) -- (-0.885,0.028) -- (-0.805,-0.023) -- (-0.732,0.018) -- (-0.667,-0.014) -- (-0.607,0.012) -- (-0.552,-0.009) -- (-0.502,0.007) -- (-0.457,-0.006) -- (-0.416,0.005) -- (-0.379,-0.004);
\draw[->] (-4.000,1.000) -- (-3.880,0.400) -- (-3.668,-0.320) -- (-3.388,-0.704) -- (-3.062,-0.589) -- (-2.710,-0.143) -- (-2.347,0.299) -- (-1.986,0.473) -- (-1.637,0.329) -- (-1.310,0.016) -- (-1.008,-0.244) -- (-0.737,-0.306) -- (-0.497,-0.172) -- (-0.291,0.039) -- (-0.117,0.184) -- (0.025,0.189) -- (0.139,0.080) -- (0.225,-0.055) -- (0.287,-0.130) -- (0.329,-0.112) -- (0.352,-0.031) -- (0.360,0.053) -- (0.356,0.088) -- (0.341,0.063) -- (0.320,0.005) -- (0.293,-0.044);
\draw[hl, ->] (-4.000,1.000) -- (-3.700,0.700) -- (-3.401,0.407) -- (-3.103,0.132) -- (-2.808,-0.110) -- (-2.515,-0.300) -- (-2.227,-0.424) -- (-1.944,-0.481) -- (-1.667,-0.481) -- (-1.398,-0.434) -- (-1.138,-0.355) -- (-0.888,-0.255) -- (-0.650,-0.144) -- (-0.426,-0.032) -- (-0.217,0.073) -- (-0.024,0.161) -- (0.151,0.226) -- (0.308,0.265) -- (0.445,0.277) -- (0.562,0.263) -- (0.658,0.228) -- (0.734,0.177) -- (0.791,0.115) -- (0.829,0.049) -- (0.848,-0.016) -- (0.851,-0.074);
\node[dot] at (0,0) {};
\node[lab,anchor=east] at (-4.1,1.0) {start};
\end{tikzpicture}
\end{center}
```

Twenty-five steps from $(-4,1)$ on the ravine $f(\mathbf w)=\tfrac12(w_1^2+20w_2^2)$ (level sets faint): plain gradient descent with $\eta=0.09$ zig-zags across the steep direction (faint path); momentum ($\mu=0.8$, $\eta=0.03$, plain path) builds up speed along the flat direction; Adam ($\eta=0.3$, highlighted) takes steps of about equal size in both coordinates from the start.

:::

Without the correction the first steps would be tiny: with $g=0.5$ and $\beta_1=0.9$, $m_1=0.05$ instead of $0.5$. Adam is momentum (on $\mathbf{m}$) combined with RMSProp (on $\mathbf{v}$); unlike AdaGrad its denominator does not grow without bound, so its steps do not die out. It is a good default; SGD with momentum and a tuned schedule sometimes generalizes slightly better.

::: {#rmk-learning-rate-schedules .remark name="Annealing the learning rate"}

A fixed learning rate makes the iterates bounce around a minimum at a distance set by the gradient noise. Common *schedules* lower it during training: *step decay* (divide by $2$ to $10$ every few epochs, or when the validation error stops improving), *exponential decay* $\eta_t=\eta_0e^{-kt}$, $1/t$ *decay* $\eta_t=\eta_0/(1+kt)$, and *cosine decay* from $\eta_0$ to $0$ over the run, often after a short linear *warm-up*.

:::

::: {#fig-momentum-and-adaptive-methods-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (6.4,0) node[lab, right] {epoch};
\draw[->] (0,0) -- (0,2.6) node[lab, above] {learning rate};
\draw[faint] (0.000,2.000) -- (2.000,2.000) -- (2.000,1.000) -- (4.000,1.000) -- (4.000,0.500) -- (6.000,0.500);
\draw[emph, domain=0:6, samples=80, smooth, variable=\x] plot ({\x}, {1+cos(deg(pi*\x/6))});
\draw[hl] (0.000,0.000) -- (0.600,2.000) -- (6.000,0.050);
\node[tick] at (2.6,1.15) {step};
\node[tick] at (3.6,1.55) {cosine};
\node[tick, text=accent, right] at (0.7,2.4) {warm-up, linear decay};
\end{tikzpicture}
\end{center}
```

Three learning rate schedules: step decay, cosine decay, and a linear warm-up followed by linear decay

:::

::: {#rmk-second-order-methods .remark name="Second-order methods"}

Newton's method (@def-newton-step) rescales the gradient by the inverse Hessian and needs no learning rate. With millions of parameters the Hessian cannot even be stored; quasi-Newton methods such as L-BFGS approximate its inverse from recent gradients, but they need exact full-batch gradients and work poorly with minibatch noise. Deep networks are therefore trained by first-order methods; the adaptive methods above can be read as cheap diagonal rescalings.

:::
