::: {.solution for="prob-cs70-16-q1"}
<!-- TODO: solution -->
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6041f10-3-q4" status="draft"}
Take $X=D_1-D_2$ with the $9$ ordered pairs equally likely.

(a) Counting pairs with each difference:
$$p_X(-2)=p_X(2)=\tfrac19,\quad p_X(-1)=p_X(1)=\tfrac29,\quad p_X(0)=\tfrac39.$$
The PMF is symmetric about $0$, so $E[X]=0$, and $\mathrm{Var}(X)=E[X^2]=\frac{2\cdot4\cdot1+2\cdot1\cdot2}9=\frac43$.

(b) $p_{X^2}(y)=\sum_{x:x^2=y}p_X(x)$:
$$p_{X^2}(0)=\tfrac39,\quad p_{X^2}(1)=\tfrac49,\quad p_{X^2}(4)=\tfrac29.$$
The plot has three bars, at $0$, $1$ and $4$, of heights $3/9$, $4/9$ and $2/9$.
:::
