::: {.problem #prob-cs221hw-4-q2 origin="external" source="cs221hw-4-q2"}
(a) Suppose we have an MDP with states $\text{States}$ and a discount factor $\gamma < 1$, but we have an MDP solver that can only solve MDPs with discount factor of $1$. How can we leverage this restricted MDP solver to solve the original MDP?

Let us define a new MDP with states $\text{States}' = \text{States} \cup \{ o \}$, where $o$ is a new state. Let's use the same actions ($\text{Actions}'(s) = \text{Actions}(s)$), but we need to keep the discount $\gamma' = 1$. Your job is to define transition probabilities $T'(s, a, s')$ and rewards $\text{Reward}'(s, a, s')$ for the new MDP in terms of the original MDP such that the optimal values $V^*(s)$ for all $s \in \text{States}$ are equal under the original MDP and the new MDP.

*Hint: You can make $o$ an end state, so that its value is always 0. What recurrence must the optimal values for each MDP satisfy? You can show that the optimal values for each MDP are the same if these recurrences are equivalent. Revisit the [MDP lecture](https://stanford-cs221.github.io/lectures/?trace=mdp) to help you solve this problem.*

*Expected:* Transition probabilities ($T'$) and reward function ($\text{Reward}'$) written in mathematical expressions, followed by a short verification to show that the two optimal values are equal. Use consistent notation from the question. Show your work briefly.

*Note (these notes):* Only the written parts of this handout problem are given here; its programming parts are left out (SPEC §17.13.1, item 4).
:::
