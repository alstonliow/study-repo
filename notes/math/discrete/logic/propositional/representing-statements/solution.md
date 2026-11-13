<!-- Migrated from 1058note exercises/chapters (owner's solutions). -->

::: {.solution for="prob-propositional-21"}
**Truth table.**

$$\begin{array}{cc|c|c|ccc}
x_1 & x_0 & x & x+1 & y_2 & y_1 & y_0 \\
\hline
0 & 0 & 0 & 1 & 0 & 0 & 1 \\
0 & 1 & 1 & 2 & 0 & 1 & 0 \\
1 & 0 & 2 & 3 & 0 & 1 & 1 \\
1 & 1 & 3 & 4 & 1 & 0 & 0 \\
\end{array}$$

**Bit $y_2$.** This bit is $1$ only in the last row, where $x_1=x_0=1$:
$$y_2 \equiv x_1\wedge x_0$$

**Bit $y_1$.** This bit is $1$ exactly when $x_1,x_0$ differ:
$$y_1 \equiv (\neg x_1\wedge x_0)\vee(x_1\wedge\neg x_0) \equiv x_1\oplus x_0$$

**Bit $y_0$.** From the table:
$$y_0 \equiv (\neg x_1\wedge\neg x_0)\vee(x_1\wedge\neg x_0)$$

Factor out $\neg x_0$:
$$\equiv \neg x_0 \wedge(\neg x_1\vee x_1)$$

Since $\neg x_1\vee x_1\equiv\mathsf{True}$:
$$\equiv \neg x_0\wedge\mathsf{True} \equiv \neg x_0$$

This matches intuition: incrementing always flips the lowest bit.

**Summary.**
$$y_2 \equiv x_1\wedge x_0, \qquad y_1\equiv x_1\oplus x_0, \qquad y_0\equiv \neg x_0$$
:::
