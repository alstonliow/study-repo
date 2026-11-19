---
title: "Exploration Functions and Regret"
sources: [cs188-11]
requires: [ai/reinforcement-learning/model-free-rl]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley CS188 (Fall 2025), Lecture 11 (exploration versus exploitation, epsilon-greedy, exploration functions, regret), in our own wording; the numbers in the example are our own. -->

Q-learning (@def-q-learning) learns optimal Q-values whatever policy generates the data, as long as every action is tried often enough in every state. Which actions to try is the agent's choice, and a poor choice wastes reward. The $\epsilon$-greedy policy (@def-epsilon-greedy) explores, but blindly: it keeps trying actions known to be bad as often as promising untried ones, and unless $\epsilon$ is lowered over time it keeps exploring for ever.

::: {#def-exploration-function .definition name="Exploration function"}

Let $N(s,a)$ count how often action $a$ has been taken in state $s$. An *exploration function* $f(u,n)$ turns an estimated value $u$ and a visit count $n$ into an *optimistic* value, decreasing in $n$ and approaching $u$ as $n\to\infty$; a common choice is $f(u,n)=u+k/(n+1)$ for a constant $k>0$. *Q-learning with an exploration function* acts greedily with respect to $f(\hat Q(s,a),N(s,a))$ and updates with the target
$$
r_t+\gamma\max_{a'}f\bigl(\hat Q(s_{t+1},a'),N(s_{t+1},a')\bigr).
$$

:::

Rarely tried actions look better than their estimates, so the agent tries them; once tried often, they are judged on their estimates alone. Using $f$ in the target as well propagates the bonus backwards: a state is attractive if it *leads* to unexplored states, so the agent heads for unexplored regions, not just unexplored actions next to it.

::: {#exm-exploration-function .example name="One state, two actions"}

In a state $s$, action $a_1$ has been tried $9$ times with $\hat Q(s,a_1)=5$, and $a_2$ once with $\hat Q(s,a_2)=3$. Greedy action selection always picks $a_1$, and $\epsilon$-greedy with $\epsilon=0.1$ picks $a_2$ only $5\%$ of the time (half of the random choices). With $f(u,n)=u+10/(n+1)$ the optimistic values are $5+1=6$ for $a_1$ and $3+5=8$ for $a_2$, so the agent tries $a_2$ again. If it keeps returning about $3$, after four more tries its value is $3+10/6\approx4.7<6$, and the agent goes back to $a_1$ for good unless $a_2$ surprises it.

:::

::: {#def-regret .definition name="Regret"}

The *regret* of a learning agent is the difference between the total (expected) reward an optimal policy would have collected and the total reward the agent collects while learning, including its mistakes from exploring.

:::

Every agent that learns pays some regret, since it must try actions to learn their values. Two agents that both end with optimal policies can differ widely in regret: random exploration has high regret, while exploration that stops trying actions once they are known to be bad has lower regret. Minimising regret means learning to be optimal while also being as good as possible along the way.
