---
title: "Hidden Markov Models and the Forward Algorithm"
sources: [cs188-18, cs188-19]
requires: [ai/bayesian-networks/conditional-independence]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley CS188 (Fall 2025), Lecture 18 (Markov models, the mini-forward algorithm, stationary distributions, hidden Markov models, filtering, passage of time, observation, the forward algorithm) and the first part of Lecture 19, in our own wording; proofs written out in steps; the weather numbers are our own and were computed exactly in Python. Markov chains themselves are in @sec-math-probability-markov-chains-finite-markov-chains. -->

A Markov chain (@def-markov-chain) models a quantity that changes over time, such as the weather or a robot's position. Predicting it forward without observations is the *mini-forward algorithm*, $P(X_{t+1}=x')=\sum_xP(x'\mid x)P(X_t=x)$ (@thm-markov-distribution-at-time-n); for a chain that is irreducible and aperiodic the prediction forgets where it started and tends to the stationary distribution (@thm-markov-convergence). Usually, though, the quantity is not seen directly; only noisy evidence about it is.

::: {#def-hmm .definition name="Hidden Markov model"}

A *hidden Markov model* (HMM) has hidden states $X_1,X_2,\dots$ forming a Markov chain with initial distribution $P(X_1)$ and transition model $P(X_{t+1}\mid X_t)$ (the same at every $t$), and evidence variables $E_1,E_2,\dots$ with an *emission* (sensor) model $P(E_t\mid X_t)$, also the same at every $t$. As a Bayesian network it has edges $X_t\to X_{t+1}$ and $X_t\to E_t$, so
$$
P(x_1,e_1,\dots,x_T,e_T)=P(x_1)P(e_1\mid x_1)\prod_{t=2}^{T}P(x_t\mid x_{t-1})P(e_t\mid x_t).
$$

:::

Reading d-separation (@def-d-separation) off the graph: given $X_t$, the future states and evidence are independent of the past ones, and each $E_t$ is independent of everything else given $X_t$. Examples are speech recognition (hidden words, observed sound), robot localisation (hidden position, observed sensor readings) and tracking (hidden position of a target, noisy range readings).

::: {#def-filtering .definition name="Belief, filtering"}

The *belief* at time $t$ is the distribution of the current state given the evidence so far,
$$
B_t(x)=P(X_t=x\mid e_1,\dots,e_t),
$$
and computing it is *filtering* (or *monitoring*). We also write $B'_{t+1}(x)=P(X_{t+1}=x\mid e_1,\dots,e_t)$ for the prediction one step ahead, before $e_{t+1}$ arrives.

:::

::: {#thm-forward-algorithm .theorem name="The forward algorithm"}

In a hidden Markov model, $B_1(x)\propto P(e_1\mid x)P(X_1=x)$ and, for $t\ge1$,
$$
B'_{t+1}(x')=\sum_xP(x'\mid x)\,B_t(x)\quad\text{(elapse time)},\qquad B_{t+1}(x')\propto P(e_{t+1}\mid x')\,B'_{t+1}(x')\quad\text{(observe)},
$$
where $\propto$ means: normalise over $x'$ so that the values sum to $1$.

:::

::: {.proof}

Write $e_{1:t}$ for $e_1,\dots,e_t$.

1. Time $1$: by Bayes' rule (@thm-bayes-theorem), $P(X_1=x\mid e_1)\propto P(e_1\mid x)P(X_1=x)$.
2. Elapse time: condition on $X_t$ (law of total probability), $P(x'\mid e_{1:t})=\sum_xP(x'\mid x,e_{1:t})P(x\mid e_{1:t})$. Given $X_t$, $X_{t+1}$ is independent of the earlier evidence, so $P(x'\mid x,e_{1:t})=P(x'\mid x)$.
3. Observe: by Bayes' rule with everything conditioned on $e_{1:t}$, $P(x'\mid e_{1:t+1})\propto P(e_{t+1}\mid x',e_{1:t})P(x'\mid e_{1:t})$. Given $X_{t+1}$, $E_{t+1}$ is independent of the earlier evidence, so the first factor is $P(e_{t+1}\mid x')$.

:::

```{=latex}
\begin{algorithm}
\caption{Forward algorithm (filtering)}
\begin{algorithmic}
\INPUT HMM, evidence $e_1,\dots,e_T$
\OUTPUT Beliefs $B_1,\dots,B_T$
\STATE $B(x)\gets P(e_1\mid x)P(X_1=x)$ for all $x$; normalise $B$
\FOR{$t=1$ \textbf{to} $T-1$}
    \STATE $B'(x')\gets\sum_xP(x'\mid x)B(x)$ for all $x'$ \COMMENT{elapse time}
    \STATE $B(x')\gets P(e_{t+1}\mid x')B'(x')$ for all $x'$; normalise $B$ \COMMENT{observe}
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

Each step costs $O(|X|^{2})$ for the sum over predecessor states and $O(|X|)$ for the observation, whatever the length of the history, so the belief can be updated online as evidence arrives. Elapsing time spreads the belief out (uncertainty grows as the state moves); observing sharpens it. Normalising may be postponed: the unnormalised values are $P(X_t=x,e_{1:t})$, whose sum is the probability of the evidence.

::: {#exm-forward-weather .example name="Rain from umbrellas"}

The weather $X_t\in\{\text{rain},\text{sun}\}$ stays the same from one day to the next with probability $0.7$; an office worker who sees no window observes only whether a colleague brings an umbrella, $P(\text{umbrella}\mid\text{rain})=0.8$ and $P(\text{umbrella}\mid\text{sun})=0.3$; and $P(X_1=\text{rain})=0.5$. With evidence umbrella, umbrella, no umbrella:

| day | prediction $B'_t(\text{rain})$ | evidence | belief $B_t(\text{rain})$ |
|---|---|---|---|
| 1 | $0.5$ | umbrella | $\tfrac{0.4}{0.4+0.15}=\tfrac{8}{11}\approx0.727$ |
| 2 | $0.7\cdot\tfrac{8}{11}+0.3\cdot\tfrac{3}{11}=\tfrac{13}{22}\approx0.591$ | umbrella | $\tfrac{104}{131}\approx0.794$ |
| 3 | $\approx0.618$ | no umbrella | $\approx0.316$ |

Each elapse step pulls the belief towards $0.5$, the stationary distribution of the weather chain, and each observation pushes it towards the state that explains the evidence better.

:::

::: {#fig-hidden-markov-models-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\draw[gridline] (-0.2,2) -- (6.2,2);
\node[lab, tick, anchor=east] at (-0.2,2) {$1$};
\draw (-0.2,0) -- (6.2,0);
\node[lab, tick, anchor=east] at (-0.2,0) {$0$};
\draw[faint, fill=neutral] (0.00,0) rectangle (0.60,1.000);
\draw[bar] (0.70,0) rectangle (1.30,1.455);
\node[lab, tick, align=center] at (0.65,-0.45) {day 1\\umbrella};
\node[lab, tick] at (0.30,1.200) {0.50};
\node[lab, tick] at (1.00,1.655) {0.73};
\draw[faint, fill=neutral] (2.10,0) rectangle (2.70,1.182);
\draw[bar] (2.80,0) rectangle (3.40,1.588);
\node[lab, tick, align=center] at (2.75,-0.45) {day 2\\umbrella};
\node[lab, tick] at (2.40,1.382) {0.59};
\node[lab, tick] at (3.10,1.788) {0.79};
\draw[faint, fill=neutral] (4.20,0) rectangle (4.80,1.235);
\draw[bar] (4.90,0) rectangle (5.50,0.631);
\node[lab, tick, align=center] at (4.85,-0.45) {day 3\\no umbrella};
\node[lab, tick] at (4.50,1.435) {0.62};
\node[lab, tick] at (5.20,0.831) {0.32};
\end{tikzpicture}
\end{center}
```

The forward algorithm on the umbrella example (@exm-forward-weather): for each day, the probability of rain after elapsing time (light bar, $B'_t$) and after observing the evidence (dark bar, $B_t$).

:::

::: {#rmk-hmm-ghostbusters .remark name="Tracking a ghost"}

In the lecture's Ghostbusters game a ghost moves on a grid by a known random rule and sensors report noisy distances. The belief over the grid is updated by the forward algorithm: after each move the probability mass flows to neighbouring cells, after each reading it concentrates on cells consistent with it. With many states, the sum over $x$ in the elapse step becomes the bottleneck, which motivates particle filtering (@sec-ai-temporal-models-particle-filtering).

:::
