::: {.problem #prob-cs221hw-4-q4 origin="external" source="cs221hw-4-q4"}
In the previous question, we've seen how value iteration can take an MDP which describes the full dynamics of the game and return an optimal policy, and we've also seen how model-based value iteration with Monte Carlo simulation can estimate MDP dynamics if unknown at first and then learn the respective optimal policy. But suppose you are trying to control a complex system in the real world where trying to explicitly model all possible transitions and rewards is intractable. We will see how model-free reinforcement learning can nevertheless find the optimal policy.

(e) Despite its worse performance on this problem, why could the function approximation Q-learning outperform the tabular Q-learning in some other environments? Consider the situations where the exploration period is limited, where the state space is very high dimensional and difficult to explore, and/or you have space constraints.

*Expected:* 2-3 sentences discussing why `FunctionApproxQLearning` can be better in various scenarios.

*Note (these notes):* Only the written parts of this handout problem are given here; its programming parts are left out (SPEC §17.13.1, item 4).
:::
