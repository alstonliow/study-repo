::: {.problem #prob-mit6006s20-7-q1 origin="external" source="mit6006s20-7-q1"}
**Effective Campaigning**

Representative Zena Torr is facing off against Senator Kong Grossman in a heated presidential primary: a sequence of $n$ head-to-head state contests, one per day for $n$ days. Each state contest $i\in\{1,\dots,n\}$ has a known positive integer delegate count $d_i$, and a projected delegate count $z_i<d_i$ that Rep. Torr would win if she took no further action. There are $D=\sum_id_i$ total delegates and Rep. Torr needs at least $\lfloor D/2\rfloor+1$ delegates to win. Unfortunately, Rep. Torr is projected to lose the race, since $\sum_iz_i<\lfloor D/2\rfloor+1$, so she needs to take action. Rep. Torr has a limited but effective election team which can campaign in at most one state per day. If the team campaigns on day $i$, they will win all $d_i$ delegates in state $i$, but they will not be able to campaign at all for two days after day $i$, as it will take time to relocate. Describe an $O(n)$-time algorithm to determine whether it is possible for Rep. Torr to win the primary contest by campaigning effectively.

*Note (these notes):* Problem Set 7 begins: "Please solve each of the following problems using dynamic programming. For each problem, be sure to define a set of subproblems, relate the subproblems recursively, argue the relation is acyclic, provide base cases, construct a solution to the original problem from the subproblems, and analyze running time. Correct but inefficient dynamic programs will be awarded significant partial credit."
:::

::: {.problem #prob-mit6006s20-7-q3 origin="external" source="mit6006s20-7-q3"}
**Odd Paths**

Given a weighted directed acyclic graph $G=(V,E,w)$ with integer weights and two vertices $s,t\in V$, describe a linear-time algorithm to determine the number of paths from $s$ to $t$ having odd weight. When solving this problem, you may assume that a single machine word is large enough to hold any integer computed during your algorithm.

*Note (these notes):* Problem Set 7 begins: "Please solve each of the following problems using dynamic programming. For each problem, be sure to define a set of subproblems, relate the subproblems recursively, argue the relation is acyclic, provide base cases, construct a solution to the original problem from the subproblems, and analyze running time. Correct but inefficient dynamic programs will be awarded significant partial credit."
:::
