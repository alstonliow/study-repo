---
title: "Reinforcement Learning and Model-Based Learning"
sources: [cs221-9]
requires: [ai/reinforcement-learning/value-iteration]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 9 (the reinforcement learning setting, model-based RL, epsilon-greedy), in our own wording. -->

Value iteration needs the transition probabilities and rewards. In *reinforcement learning* (RL) they are unknown: the agent learns only from what happens when it acts.

::: {#def-reinforcement-learning .definition name="Reinforcement learning, agent"}

In *reinforcement learning* an *agent* interacts with an *environment*, here an MDP whose $T$ and $\text{Reward}$ the agent does not know. Repeatedly, the agent chooses an action in the current state, and the environment returns a reward and the next state. An agent is an algorithm with two operations: *get action* (choose an action in a state) and *incorporate feedback* (update itself from a transition $(s,a,r,s')$).

:::

A policy is fixed; an agent changes over time, using feedback to improve the policy it acts with. Good actions found by trial are repeated, that is, *reinforced*. (In many real problems the agent sees only part of the state; that setting, partially observable MDPs, is not treated here.)

::: {#def-model-based-rl .definition name="Model-based reinforcement learning"}

*Model-based* RL estimates the MDP and then plans in the estimate. During *exploration* it follows an exploration policy and counts, for each state and action, how often each next state and reward follow. It estimates

$$
\hat T(s,a,s')=\frac{N(s,a,s')}{N(s,a)},\qquad \widehat{\text{Reward}}(s,a,s')=\text{average reward observed on }(s,a,s'),
$$

where $N(s,a)$ counts the times $a$ was taken in $s$ and $N(s,a,s')$ those that led to $s'$. *Planning* runs value iteration (@sec-ai-reinforcement-learning-value-iteration) on the estimated MDP, and *exploitation* follows the resulting policy.

:::

```{=latex}
\begin{algorithm}
\caption{Model-based reinforcement learning}
\begin{algorithmic}
\INPUT Environment, exploration policy $\pi_{\text{explore}}$, number of exploration episodes $m$
\OUTPUT Policy $\hat\pi$
\STATE $N(s,a,s')\gets0$, $R(s,a,s')\gets0$ for all $s,a,s'$
\FOR{$i=1$ \TO $m$}
    \FOR{each transition $(s,a,r,s')$ of an episode following $\pi_{\text{explore}}$}
        \STATE $N(s,a,s')\gets N(s,a,s')+1$; \quad $R(s,a,s')\gets R(s,a,s')+r$
    \ENDFOR
\ENDFOR
\STATE $\hat T(s,a,s')\gets N(s,a,s')/\sum_{s''}N(s,a,s'')$; \quad $\widehat{\text{Reward}}(s,a,s')\gets R(s,a,s')/N(s,a,s')$
\STATE $\hat\pi\gets$ the policy returned by value iteration on $(\hat T,\widehat{\text{Reward}})$
\RETURN $\hat\pi$
\end{algorithmic}
\end{algorithm}
```

::: {#exm-model-based-rl-1 .example name="Learning the dice game"}

The agent explores the dice game (@exm-mdp-dice-game) for $200$ episodes, choosing quit or stay at random. In one such run it stayed $162$ times, $107$ of which led back to $\text{in}$, so $\hat T(\text{in},\text{stay},\text{in})=107/162\approx0.660$ (true value $\tfrac23$). In the estimated MDP, always staying is worth $4/(1-0.660)\approx11.78$ and quitting $10$, so planning chooses to stay, which is also optimal in the true MDP.

:::

::: {#fig-model-based-rl-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[vertex] (in) at (0,0) {in};
\node[vertex] (end) at (5,0) {end};
\node[box] (q) at (2.5,1.1) {quit};
\node[box] (s) at (2.5,-1.1) {stay};
\draw[->] (in) -- (q);
\draw[->] (in) -- (s);
\draw[->] (q) -- node[edge label,above] {$145/145$: $+10$} (end);
\draw[->] (s) -- node[edge label,below right] {$55/162$: $+4$} (end);
\draw[->] (s) to[bend left=35] node[edge label,below left] {$107/162$: $+4$} (in);
\end{tikzpicture}
\end{center}
```

The dice game as estimated from the counts of @exm-model-based-rl-1: each estimated transition probability is a count over the number of times the action was taken (true values $1$, $\tfrac13$, $\tfrac23$).

:::

The estimates converge to the truth only for state–action pairs the exploration policy visits again and again, so it must try every action with positive probability. Exploration earns less than the best policy would; this is the price of learning. In practice exploration and exploitation need not be separate stages: the policy can move gradually from one to the other.

::: {#def-epsilon-greedy .definition name="Epsilon-greedy policy"}

Given estimated Q-values $\hat Q(s,a)$ and $0\le\epsilon\le1$, the *$\epsilon$-greedy* policy in state $s$ takes, with probability $\epsilon$, an action drawn by an exploration policy (for example uniformly at random), and otherwise an action maximizing $\hat Q(s,a)$.

:::

$\epsilon=1$ is pure exploration and $\epsilon=0$ pure exploitation. Every agent must trade the two off, like choosing between a restaurant one likes and a new one; decreasing $\epsilon$ over time moves from the first to the second.
