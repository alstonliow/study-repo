::: {.problem #prob-cs221hw-4-q1 origin="external" source="cs221hw-4-q1"}
In this problem, you will perform value iteration updates manually on a basic game to build your intuitions about solving MDPs. In this MDP, we have that:

- The set of possible states in this game is $\text{States} = \{-2, -1, 0, +1, +2\}$.
- The set of possible actions is $\text{Actions}(s) = \{a_1, a_2\}$ for all states that are not end states.
- The starting state is $0$ and there are two end states, $-2$ and $+2$.

Recall that the transition function $T: \text{States} \times \text{Actions} \rightarrow \Delta\text{States}$ (distribution over states) encodes the probability of transitioning to a next state $s'$ after being in state $s$ and taking action $a$ as $T(s, a, s')$.

In this MDP, the transition dynamics are given as follows: $\forall i \in \{-1, 0, 1\} \subseteq \text{States}$,

- $T(i, a_1, i-1) = 0.8$ and $T(i, a_1, i+1) = 0.2$
- $T(i, a_2, i-1) = 0.7$ and $T(i, a_2, i+1) = 0.3$

Think of this MDP as a chain formed by states $\{-2, -1, 0, +1, +2\}$. In words, action $a_1$ has an 80% chance of moving the agent backwards in the chain and a 20% chance of moving the agent forward. Similarly, action $a_2$ has a 70% chance of sending the agent backwards and a 30% chance of moving the agent forward. We will use a discount factor $\gamma = 1$.

The reward function for this MDP is:

$$\text{Reward}(s,a,s') = \begin{cases} 10 & \text{if } s' = -2, \\ 50 & \text{if } s' = +2, \\ -5 & \text{otherwise}. \end{cases}$$

(a) What is the value of $V^*_i(s)$ for each $s \in \text{States}$ after each iteration $i \in \{1, 2\}$ of value iteration? Recall that $\forall s \in \text{States}$, $V^*_0(s) = 0$ and, for any $i$, end state $s_{\text{end}}$, we have $V^*_i(s_\text{end}) = 0$.

*Expected:* The $V^*_i(s)$ of all 5 states after each iteration $i = 1, 2$ (10 values in total), with your work shown: for each non-end state and each iteration, write out the expected value of each action (for example, $0.8 \cdot (\ldots) + 0.2 \cdot (\ldots)$) and which one is the max. We need to see this work to give partial credit, so don't report only the final values.

(b) Using $V^*_2(\cdot)$, what is the corresponding optimal policy $\pi^*$ for all non-end states?

*Expected:* For each non-end state, the expected value of $a_1$ and of $a_2$ computed using $V^*_2$ (written out as in 1a), and the resulting optimal action $\pi^*(s)$.

*Note (these notes):* Only the written parts of this handout problem are given here; its programming parts are left out (SPEC §17.13.1, item 4).
:::
