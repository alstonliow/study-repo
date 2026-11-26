<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18065ps-24-q5" status="draft"}
1. $\begin{bmatrix}1&2\\4&8\end{bmatrix}$: row 1 is smaller than row 2 in both columns, so $X$ always plays row 1; then $Y$ plays column 2. Entry $2$ is the smallest in its column and the largest in its row: a saddle point. Pure strategies $\mathbf{x}^*=(1,0)$, $\mathbf{y}^*=(0,1)$, payoff $2$.

2. $\begin{bmatrix}1&4\\8&2\end{bmatrix}$: no saddle point, so both mix. If $X$ plays row 1 with probability $x$, the payoffs against the two columns are $8-7x$ and $2+2x$; equalising gives $x=\frac23$, payoff $\frac{10}3$.

3. If $Y$ plays column 1 with probability $y$, the payoffs against the two rows are $4-3y$ and $2+6y$; equalising gives $y=\frac29$, payoff $\frac{10}3$.

4. So $\mathbf{x}^*=(\frac23,\frac13)$, $\mathbf{y}^*=(\frac29,\frac79)$, and the value is $\frac{10}3$ (@thm-von-neumann-minimax).
:::

::: {.solution for="prob-mit6854ps-4-q1" status="draft"}
*1.* For fixed $x$, $x^TAy=\sum_jy_j(x^TA)_j$ is a weighted average of the numbers $(x^TA)_j$ with weights $y_j$. It is maximised by putting all weight on an index $j$ with largest $(x^TA)_j$: a pure strategy.

*2.* By 1, $\max_yx^TAy=\max_j(x^TA)_j$, the least $t$ with $\sum_ia_{ij}x_i\le t$ for all $j$. So Alice solves
$$\text{(A)}\quad\min\Big\{t:\sum_ia_{ij}x_i\le t\ \forall j,\ \sum_ix_i=1,\ x\ge0\Big\},$$
and symmetrically Bob solves
$$\text{(B)}\quad\max\Big\{u:\sum_ja_{ij}y_j\ge u\ \forall i,\ \sum_jy_j=1,\ y\ge0\Big\}.$$
Both are linear programs of polynomial size, solvable in polynomial time (@thm-lp-polynomial).

*3.* Write (A) with the constraints $t-\sum_ia_{ij}x_i\ge0$ (multipliers $y_j\ge0$) and $\sum_ix_i=1$ (free multiplier $u$). The dual has the constraints: from the free variable $t$, $\sum_jy_j=1$; from $x_i\ge0$, $u-\sum_ja_{ij}y_j\le0$; objective $\max u$. That is exactly (B). Both are feasible (any distributions with $t,u$ large or small enough), so by strong duality (@thm-strong-duality) their optimal values are equal: $\min_x\max_y=\max_y\min_x$.
:::
