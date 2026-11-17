::: {.problem #prob-mit6046s15-8-q2 origin="external" source="mit6046s15-8-q2"}
**NP-Completeness**

In this problem, you will prove NP-completeness of a few decision problems. To prove NP-hardness, you may reduce from any problem that has been shown, in class or in CLRS, to be NP-complete.

(a) Let TRIPLE-SAT denote the following decision problem: given a Boolean formula $\phi$, decide whether $\phi$ has at least three distinct satisfying assignments. Prove that TRIPLE-SAT is NP-complete.

(b) In Problem Set 1, we considered how one might locate donut shops at some of the vertices of a street network, modeled as an arbitrary undirected graph $G=(V,E)$. Each vertex $u$ has a nonnegative integer value $p(u)$, which describes the potential profit obtainable from a shop located at $u$. Two shops cannot be located at adjacent vertices. The problem was to design an algorithm that outputs a subset $U\subseteq V$ that maximizes the total profit $\sum_{u\in U}p(u)$. No doubt, you found an algorithm with time complexity that was exponential in the graph parameters. Now we will see why.

Define DONUT to be the following decision problem: given an undirected graph $G=(V,E)$, given a mapping $p$ from vertices $u\in V$ to nonnegative integer profits $p(u)$, and given a nonnegative integer $k$, decide whether there is a subset $U\subseteq V$ such that no two vertices in $U$ are neighbors in $G$, and such that $\sum_{u\in U}p(u)\ge k$. Prove that DONUT is NP-hard. (Hint: Try a reduction from 3SAT.)

Also, explain why this implies that, if there is a polynomial-time algorithm to solve the original problem, i.e., to output a subset $U$ that maximizes the total profit, then P = NP.

(c) Suppose we have one machine and a set of $n$ tasks $a_1,a_2,\dots,a_n$. Each task $a_j$ requires $t_j$ units of time on the machine, yields a profit of $p_j$, and has a deadline $d_j$. Here, the $t_j$, $p_j$, and $d_j$ values are nonnegative integers. The machine can process only one task at a time. Not all tasks have to be run, but if a task starts running, it must run without interruption and must complete by its deadline.

A schedule for a subset of the tasks describes when each of the tasks in the subset starts running. A schedule must observe the constraints given above. The profit for the schedule is the sum of all the $p_j$ values for the tasks $a_j$ in the schedule.

The problem is to produce a schedule for a subset of the tasks that returns the greatest possible amount of profit. State this problem as a decision problem and show that it is NP-complete. In showing this, you may reduce from any problem that has been shown, in class or in CLRS, to be NP-complete.
:::
