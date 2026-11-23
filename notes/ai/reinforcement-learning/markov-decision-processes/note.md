---
title: "Markov Decision Processes"
sources: [cs221-8]
requires: [ai/search/search-problems, math/probability/discrete/conditional-expectation, math/probability/markov-chains/finite-markov-chains]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 8 (MDPs, policies, utility, value, Monte Carlo evaluation), in our own wording. The Bellman equation for a policy is stated as a theorem with our own proof. -->

A search problem (@sec-ai-search-search-problems) assumes every action has one known outcome. In a *Markov decision process* an action leads to a random next state, so the agent must plan for every outcome. With the actions fixed by a policy, an MDP is a Markov chain with rewards (@sec-math-probability-markov-chains-finite-markov-chains).

::: {#def-mdp .definition name="Markov decision process"}

A *Markov decision process* (MDP) consists of a finite set of states with a start state $s_{\text{start}}$; a set $\text{Actions}(s)$ for each state $s$; *transition probabilities* $T(s,a,s')\ge0$ with $\sum_{s'}T(s,a,s')=1$ for each $s$ and $a\in\text{Actions}(s)$; a *reward* $\text{Reward}(s,a,s')\in\mathbb{R}$; a predicate $\text{IsEnd}(s)$ marking end states; and a *discount factor* $0\le\gamma\le1$.

:::

The process is *Markov*: the next state depends on the past only through the current state and action. A search problem is the special case where each $T(s,a,\cdot)$ puts all its mass on one state and rewards are negative costs.

::: {#exm-mdp-dice-game .example name="Dice game"}

In each round you choose to *quit* or *stay*. Quitting pays $10$ and ends the game. Staying pays $4$, then a die is rolled; on $1$ or $2$ the game ends, otherwise there is another round. The states are $\text{in}$ and $\text{end}$, with $T(\text{in},\text{quit},\text{end})=1$, $\text{Reward}=10$, and $T(\text{in},\text{stay},\text{end})=\tfrac13$, $T(\text{in},\text{stay},\text{in})=\tfrac23$, both with reward $4$; take $\gamma=1$.

:::

::: {#fig-markov-decision-processes-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[vertex] (in) at (0,0) {in};
\node[vertex] (end) at (5,0) {end};
\node[box] (q) at (2.5,1.1) {quit};
\node[box] (s) at (2.5,-1.1) {stay};
\draw[->] (in) -- (q);
\draw[->] (in) -- (s);
\draw[->] (q) -- node[edge label,above] {$1$: $+10$} (end);
\draw[->] (s) -- node[edge label,below] {$\frac13$: $+4$} (end);
\draw[->] (s) to[bend left=35] node[edge label,below] {$\frac23$: $+4$} (in);
\end{tikzpicture}
\end{center}
```

The dice game of @exm-mdp-dice-game. State nodes are circles and action nodes boxes; each edge from an action node carries a transition probability and a reward.

:::

::: {#exm-mdp-flaky-tram .example name="Flaky tram"}

Locations are $1,\dots,n$, starting at $1$ and ending at $n$. From $i$ one can walk to $i+1$ (one minute, reward $-1$) or, if $2i\le n$, take the tram to $2i$ (two minutes, reward $-2$), but the tram breaks down with probability $p$ and leaves us at $i$. Maximizing expected reward means minimizing expected travel time. We use $n=10$, $p=0.4$, $\gamma=1$.

:::

::: {#def-mdp-policy .definition name="Policy, rollout, utility"}

A *policy* $\pi$ maps each non-end state $s$ to an action $\pi(s)\in\text{Actions}(s)$. Following $\pi$ from a state $s_0$ produces a random *rollout* (episode, trajectory) $s_0,a_0,r_0,s_1,a_1,r_1,\dots$ with $a_t=\pi(s_t)$, $s_{t+1}$ drawn from $T(s_t,a_t,\cdot)$ and $r_t=\text{Reward}(s_t,a_t,s_{t+1})$, until an end state is reached. Its *utility* is the discounted sum of rewards

$$
u=r_0+\gamma r_1+\gamma^2r_2+\cdots=\sum_{t\ge0}\gamma^tr_t .
$$

:::

A solution of a search problem is a fixed sequence of actions; a solution of an MDP must be a policy, because later actions depend on random outcomes. A deterministic policy still gives random rollouts and so random utilities. With $\gamma=1$ the future counts as much as the present; with $\gamma=0$ only the first reward counts; in between, a reward $t$ steps ahead is worth $\gamma^t$ of one now.

::: {#def-mdp-value .definition name="Value, Q-value"}

The *value* $V_\pi(s)$ of a policy $\pi$ from state $s$ is the expected utility of a rollout of $\pi$ from $s$, and the *Q-value* $Q_\pi(s,a)$ is the expected utility of first taking action $a$ in $s$ and then following $\pi$. (We assume these expectations are finite: for example $\gamma<1$, or end states are reached with probability $1$.)

:::

::: {#thm-bellman-policy .theorem name="Bellman equations for a policy"}

For every policy $\pi$, $V_\pi(s)=0$ if $\text{IsEnd}(s)$, and otherwise

$$
V_\pi(s)=Q_\pi(s,\pi(s)),\qquad Q_\pi(s,a)=\sum_{s'}T(s,a,s')\bigl[\text{Reward}(s,a,s')+\gamma V_\pi(s')\bigr].
$$

:::

::: {.proof}

1. From an end state there are no rewards, so the utility is $0$. From another state, following $\pi$ means taking $a=\pi(s)$ first, so $V_\pi(s)=Q_\pi(s,\pi(s))$.

2. Condition on the first transition: after taking $a$ in $s$ we land in $s'$ with probability $T(s,a,s')$ and receive $\text{Reward}(s,a,s')$; the rest of the utility is $\gamma$ times the utility of a rollout of $\pi$ from $s'$.

3. By the Markov property that rollout is distributed as a fresh rollout from $s'$, so its expected utility is $V_\pi(s')$. The law of total expectation (@sec-math-probability-discrete-conditional-expectation) gives the formula for $Q_\pi(s,a)$.

:::

::: {#exm-mdp-dice-values .example name="Values in the dice game"}

For the policy "always quit", $V(\text{in})=10$. For "always stay", the Bellman equation reads $V(\text{in})=\tfrac13(4+0)+\tfrac23(4+V(\text{in}))=4+\tfrac23V(\text{in})$, so $V(\text{in})=12$: staying is better. Its utility is $4$ times the number of rounds, which is geometric with mean $3$.

:::

::: {#def-monte-carlo-estimate .definition name="Monte Carlo estimate"}

The *Monte Carlo* estimate of an expectation $E[f(X)]$ draws independent samples $x_1,\dots,x_m$ of $X$ and returns $\frac1m\sum_{i}f(x_i)$. It is unbiased, and by the law of large numbers (@sec-math-probability-tail-bounds-concentration-inequalities) it converges to $E[f(X)]$ as $m\to\infty$, with standard deviation proportional to $1/\sqrt m$. *Monte Carlo policy evaluation* estimates $V_\pi(s)$ as the average utility of $m$ rollouts of $\pi$ from $s$.

:::

```{=latex}
\begin{algorithm}
\caption{Monte Carlo policy evaluation}
\begin{algorithmic}
\INPUT A simulator of the MDP, policy $\pi$, state $s$, number of rollouts $m$
\OUTPUT Estimate of $V_\pi(s)$
\FOR{$i=1$ \TO $m$}
    \STATE roll out $\pi$ from $s$, collecting rewards $r_0,r_1,\dots$ until an end state
    \STATE $u_i\gets\sum_t\gamma^tr_t$
\ENDFOR
\RETURN $\frac1m\sum_{i=1}^mu_i$
\end{algorithmic}
\end{algorithm}
```

::: {#rmk-markov-decision-processes-1 .remark editor="No figure for Monte Carlo evaluation: a picture of individual random rollouts or of a running average shows nothing beyond the law of large numbers; policy evaluation by recurrence, which converges to the same value, has its figure in @sec-ai-reinforcement-learning-policy-evaluation."}

On the flaky tram with $n=10$, $p=0.4$, always walking has utility exactly $-9$, while always taking the tram where possible (from $1$, $2$, $4$, $5$) has random utility. Averaging $100000$ rollouts of the tram policy gives about $-12.0$ (its exact value is $-12$: three tram rides of expected cost $2/0.6$ each, then two walks), so walking is better than this policy.

:::

Monte Carlo needs only the ability to simulate. When $T$ and $\text{Reward}$ are known, the Bellman equations give the values exactly and faster (@sec-ai-reinforcement-learning-policy-evaluation).
