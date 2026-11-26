<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18433-5-q8" status="draft"}
1. *Deadline order.* Take an on-time schedule of $J$ (jobs in slots $1,2,\dots$). If a job $a$ runs just before a job $b$ with $d_b<d_a$, swap them: $b$ finishes earlier, and $a$ now finishes when $b$ did, by time $d_b<d_a$. Repeating such swaps sorts the jobs by deadline and keeps all on time.

2. Hence $J$ is feasible iff, in deadline order, the $t$-th job has deadline at least $t$, iff $|J\cap D_t|\le t$ for every $t$, where $D_t=\{j:d_j\le t\}$.

3. The sets $D_1\subseteq D_2\subseteq\cdots$ form a chain, hence a laminar family, with bounds $k(D_t)=t$. By exercise 7, $M$ is a (laminar) matroid.

4. *Algorithm.* Jobs with $c_j\le0$ can be dropped. Run the greedy algorithm (@def-matroid-greedy): consider jobs by decreasing profit and keep a job if the kept set stays feasible (test 2). By @thm-matroid-greedy the kept set has maximum profit. Schedule it in deadline order, then the remaining jobs in any order (they earn nothing).
:::
