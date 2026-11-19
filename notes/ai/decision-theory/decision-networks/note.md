---
title: "Decision Networks"
sources: [cs188-17]
requires: [ai/decision-theory/utilities, ai/bayesian-networks/bayesian-networks]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley CS188 (Fall 2025), Lecture 17 (decision networks, decisions as outcome trees, the umbrella and Ghostbusters examples), in our own wording; the numbers of the umbrella example are our own and were checked by a short exact computation in Python. -->

A Bayesian network (@def-bayesian-network) describes what we believe; to act on the beliefs we add the choices available and how much we like each outcome. The maximum expected utility principle (@thm-meu-representation) then says what to do.

::: {#def-decision-network .definition name="Decision network"}

A *decision network* is a Bayesian network over *chance nodes* together with

- *action nodes* (drawn as rectangles), whose values the agent chooses; an action node has no distribution, and it may be a parent of chance nodes;
- one *utility node* (drawn as a diamond), whose parents are chance and action nodes and which holds a table $U(\text{parents})$.

Given observed evidence $e$, the *expected utility* of action $a$ and the *maximum expected utility* are
$$
\mathrm{EU}(a\mid e)=\sum_{x}P(x\mid e,a)\,U(x,a),\qquad \mathrm{MEU}(e)=\max_a\mathrm{EU}(a\mid e),
$$
where $x$ ranges over the values of the chance parents of the utility node. The agent takes an action attaining $\mathrm{MEU}(e)$.

:::

To evaluate a decision network: instantiate the evidence; for each value $a$ of the action node, fix it, compute the posterior $P(x\mid e,a)$ of the utility node's chance parents by any Bayesian network inference method, and average the utility; then choose the best $a$. This is one step of expectimax (@def-game-recurrences): a max node for the action, followed by a chance node whose branch probabilities are posteriors given everything observed so far, as one sees when drawing the decision as an *outcome tree*.

::: {#exm-umbrella-decision .example name="Umbrella"}

The chance node $W\in\{\text{sun},\text{rain}\}$ has $P(\text{rain})=0.3$; the action $A\in\{\text{leave},\text{take}\}$ is whether to take an umbrella; and the utility, with parents $A,W$, is
$$
U(\text{leave},\text{sun})=100,\quad U(\text{leave},\text{rain})=0,\quad U(\text{take},\text{sun})=20,\quad U(\text{take},\text{rain})=70.
$$
Without evidence, $\mathrm{EU}(\text{leave})=0.7\cdot100=70$ and $\mathrm{EU}(\text{take})=0.7\cdot20+0.3\cdot70=35$, so $\mathrm{MEU}(\emptyset)=70$ and the agent leaves the umbrella.

Now add a forecast $F\in\{\text{good},\text{bad}\}$, a child of $W$, with $P(\text{bad}\mid\text{rain})=0.8$ and $P(\text{bad}\mid\text{sun})=0.1$. Then $P(\text{bad})=0.3\cdot0.8+0.7\cdot0.1=0.31$ and $P(\text{rain}\mid\text{bad})=0.24/0.31\approx0.774$, so
$$
\mathrm{EU}(\text{leave}\mid\text{bad})\approx22.6,\qquad \mathrm{EU}(\text{take}\mid\text{bad})\approx58.7,
$$
and with a bad forecast the agent takes the umbrella, $\mathrm{MEU}(\text{bad})=18.2/0.31\approx58.7$. With a good forecast $P(\text{rain}\mid\text{good})=0.06/0.69\approx0.087$, $\mathrm{EU}(\text{leave}\mid\text{good})=63/0.69\approx91.3$ against $\mathrm{EU}(\text{take}\mid\text{good})\approx24.3$, so it leaves the umbrella.

:::

::: {#fig-decision-networks-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\node[vertex] (W) at (0,0) {$W$};
\node[vertex] (F) at (0,-1.3) {$F$};
\node[box] (A) at (2.4,1) {$A$};
\node[diamond, draw=ink, fill=accentSoft, aspect=1.5] (U) at (2.4,-0.3) {$U$};
\draw[->] (W) -- (F);
\draw[->] (W) -- (U);
\draw[->] (A) -- (U);
\end{tikzpicture}
\end{center}
```

The umbrella decision network of @exm-umbrella-decision: chance nodes $W$ (weather) and $F$ (forecast, added in the second part), the action node $A$ and the utility node $U$ with parents $A$ and $W$.

:::

::: {#rmk-decision-networks-ghostbusters .remark name="Larger decision networks"}

In the Ghostbusters game of the lecture, the hidden ghost position is a chance node, colour readings from sensors are evidence nodes, and the action is where to "bust"; the utility is high only if the bust location equals the ghost's. The MEU action is to bust the most probable location, so the decision reduces to inference. When actions also change the world over time, one decision network per time step chained together gives an MDP whose states are only partly observed (@sec-ai-decision-theory-value-of-information).

:::
