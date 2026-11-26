::: {.problem #prob-mit18433-3-q14 origin="external" source="mit18433-3-q14"}
Let $P=\{x:Ax\le b,x\ge0\}$ and let $Q=\{(x,s):Ax+Is=b,x\ge0,s\ge0\}$. Show that $x$ is an extreme point of $P$ iff $(x,b-Ax)$ is an extreme point of $Q$. Conclude that whenever $A$ and $b$ have only integral entries, $P$ is integral iff $Q$ is integral.
:::

::: {.problem #prob-mit18433-3-q15 origin="external" source="mit18433-3-q15"}
If $A$ is totally unimodular then $A^{\mathsf T}$ is totally unimodular.
:::

::: {.problem #prob-mit18433-3-q16 origin="external" source="mit18433-3-q16"}
Use total unimodularity to prove König's theorem.
:::

::: {.problem #prob-mit18433-3-q17 origin="external" source="mit18433-3-q17"}
Suppose we have $n$ activities to choose from. Activity $i$ starts at time $t_i$ and ends at time $u_i$ (or more precisely just before $u_i$); if chosen, activity $i$ gives us a profit of $p_i$ units. Our goal is to choose a subset of the activities which do not overlap (nevertheless, we can choose an activity that ends at $t$ and one that starts at the same time $t$) and such that the total profit (i.e. sum of profits) of the selected activities is maximum.

1. Defining $x_i$ as a variable that represents whether activity $i$ is selected ($x_i=1$) or not ($x_i=0$), write an integer program of the form $\max\{p^{\mathsf T}x:Ax\le b,x\in\{0,1\}^n\}$ that would solve this problem.
2. Show that the matrix $A$ is totally unimodular, implying that one can solve this problem by solving the linear program $\max\{p^{\mathsf T}x:Ax\le b,0\le x_i\le1\text{ for every }i\}$.
:::

::: {.problem #prob-mit18433-3-q18 origin="external" source="mit18433-3-q18"}
Given a bipartite graph $G$ and given an integer $k$, let $S_k$ be the set of all incidence vectors of matchings with at most $k$ edges. We are interested in finding a description of $P_k=\operatorname{conv}(S_k)$ as a system of linear inequalities. More precisely, you'll show that $\operatorname{conv}(S_k)$ is given by:
$$P_k=\Big\{x:\ \sum_jx_{ij}\le1\ \ \forall i\in A,\quad\sum_ix_{ij}\le1\ \ \forall j\in B,\quad\sum_i\sum_jx_{ij}\le k,\quad x_{ij}\ge0\ \ i\in A,j\in B\Big\}.$$
Without the last constraint, we have shown that the resulting matrix is totally unimodular.

1. With the additional constraint, is the resulting matrix totally unimodular? Either prove it or disprove it.
2. Show that $P_k$ indeed equals $\operatorname{conv}(S_k)$.
3. Suppose now that instead of a cardinality constraint on all the edges, our edges are partitioned into $E_1$ and $E_2$ and we only impose that our matching has at most $k$ edges from $E_1$ (and as many as we'd like from $E_2$). Is it still true that the convex hull of all such matchings is given by simply replacing $\sum_i\sum_jx_{ij}\le k$ by
$$\sum_i\sum_{j:(i,j)\in E_1}x_{ij}\le k?$$
:::
