::: {.problem #prob-cs188hw-5-q1 origin="external" source="cs188hw-5-q1"}
**Exploring the World.** In this question, our CS188 agent is stuck in a maze. We use Q-learning with an epsilon greedy strategy to solve the task. There are 4 actions available: north (N), east (E), south (S), and west (W).

1. What is the probability of each action if the agent is following an epsilon greedy strategy and the best action in state $s$ under the current policy is $N$? Given that we are following an epsilon-greedy algorithm, we have a value $\varepsilon$. Use this value $\varepsilon$ in your answer. $p(a_i\mid s)$ is the probability of taking action $a_i$ in state $s$.

   $p(N\mid s)=$ $p(E\mid s)=$ $p(S\mid s)=$ $p(W\mid s)=$
2. We also modify the reward function $R(s,a,s')$ to visit more states and choose new actions. Which of the following rewards would encourage the agent to visit unseen states and actions?

   $N(s,a)$ refers to the number of times that you have visited state $s$ and taken action $a$ in your samples.
   - $R(s,a,s')+\sqrt{N(s,a)}$
   - $R(s,a,s')-\sqrt{N(s,a)}$
   - $R(s,a,s')+\sqrt{\frac{1}{N(s,a)+1}}$
   - $-\sqrt{\frac{1}{N(s,a)+1}}$
   - $\sqrt{\frac{1}{N(s,a)+1}}$
   - $\exp(R(s,a,s')-N(s,a))$
3. Which of the following modified rewards will eventually converge to the optimal policy with respect to the original reward function $R(s,a,s')$? $N(s,a)$ is the same as defined in part (b).
   - $R(s,a,s')+\sqrt{N(s,a)}$
   - $R(s,a,s')-\sqrt{N(s,a)}$
   - $R(s,a,s')+\sqrt{\frac{1}{N(s,a)+1}}$
   - $-\sqrt{\frac{1}{N(s,a)+1}}$
   - $\sqrt{\frac{1}{N(s,a)+1}}$
   - $\exp(R(s,a,s')-N(s,a))$
:::
