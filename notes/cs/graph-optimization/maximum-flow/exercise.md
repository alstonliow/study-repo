::: {.problem #prob-mit6854ps-1-q5 origin="external" source="mit6854ps-1-q5"}
Consider a capacitated network $G=(V,E)$. Let $\lambda_{uv}$ denote the maximum flow value from $u$ to $v$. Prove that
$$\lambda_{st}\ge\min(\lambda_{su},\lambda_{ut})$$
for any $s,t,u\in V$.
:::

::: {.problem #prob-mit6854ps-3-q5 origin="external" source="mit6854ps-3-q5"}
We will rederive the max-flow min-cut theorem from linear programming duality. Consider the maximum flow problem on a directed graph $G=(V,E)$ with source $s\in V$, sink $t\in V$ and edge capacities $u:E\to\mathbb R$. The max-flow problem is a linear program:
$$\max w$$
subject to
$$\sum_jx_{ij}-\sum_jx_{ji}=\begin{cases}w&i=s\\0&i\ne s,t\\-w&i=t\end{cases}$$
$$x_{i,j}\le u_{i,j}\qquad(i,j)\in E$$
$$0\le x_{i,j}\qquad(i,j)\in E.$$
The variables are the $x_{ij}$'s (one per edge) and $w$.

1. Show that its dual is equivalent to:
$$\min\sum_{(i,j)\in E}u_{ij}y_{ij}$$
subject to
$$z_i-z_j+y_{ij}\ge0\quad(i,j)\in E,\qquad z_s=0,\ z_t=1,\qquad y_{ij}\ge0\quad(i,j)\in E.$$

2. Given a cut $(S:\bar S)$ with $s\in S$ and $t\notin S$, show that a feasible solution $y,z$ to the dual can be obtained of value equal to the capacity of the cut: $U(S:\bar S)=\sum_{(i,j)\in E}u_{ij}y_{ij}$.

3. Given any (not necessarily integral!) optimal solution $y^*,z^*$ of the dual linear program and an optimal solution $x^*$ of the primal linear program, show how to construct from $z^*$ a cut separating $s$ from $t$ of value equal to the maximum flow. This shows the max-flow–min-cut theorem.
:::
