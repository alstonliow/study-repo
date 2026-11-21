<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18065ps-24-q5" status="draft"}
1. $\begin{bmatrix}1&2\\4&8\end{bmatrix}$: row 1 is smaller than row 2 in both columns, so $X$ always plays row 1; then $Y$ plays column 2. Entry $2$ is the smallest in its column and the largest in its row: a saddle point. Pure strategies $\mathbf{x}^*=(1,0)$, $\mathbf{y}^*=(0,1)$, payoff $2$.

2. $\begin{bmatrix}1&4\\8&2\end{bmatrix}$: no saddle point, so both mix. If $X$ plays row 1 with probability $x$, the payoffs against the two columns are $8-7x$ and $2+2x$; equalising gives $x=\frac23$, payoff $\frac{10}3$.

3. If $Y$ plays column 1 with probability $y$, the payoffs against the two rows are $4-3y$ and $2+6y$; equalising gives $y=\frac29$, payoff $\frac{10}3$.

4. So $\mathbf{x}^*=(\frac23,\frac13)$, $\mathbf{y}^*=(\frac29,\frac79)$, and the value is $\frac{10}3$ (@thm-von-neumann-minimax).
:::
