::: {.problem #prob-mit1806s10-10-q1 origin="external" source="mit1806s10-10-q1"}
These Jordan matrices have eigenvalues $0,0,0,0$. They have two eigenvectors (one from each block). But the block sizes don't match and they are *not similar*:
$$J=\begin{pmatrix}0&1&0&0\\0&0&0&0\\0&0&0&1\\0&0&0&0\end{pmatrix}\qquad\text{and}\qquad K=\begin{pmatrix}0&1&0&0\\0&0&1&0\\0&0&0&0\\0&0&0&0\end{pmatrix}$$
For any matrix $M$, compare $JM$ with $MK$. If they are equal show that $M$ is not invertible. Then $M^{-1}JM=K$ is impossible; $J$ is not similar to $K$.
:::

::: {.problem #prob-mit1806s10-10-q2 origin="external" source="mit1806s10-10-q2"}
Prove that $A^{\mathsf T}$ is always similar to $A$ (we know that the $\lambda$'s are the same):

1. For one Jordan block $J_i$: find $M_i$ so that $M_i^{-1}J_iM_i=J_i^{\mathsf T}$ (see example 3).
2. For any $J$ with blocks $J_i$: build $M_0$ from blocks so that $M_0^{-1}JM_0=J^{\mathsf T}$.
3. For any $A=MJM^{-1}$: Show that $A^{\mathsf T}$ is similar to $J^{\mathsf T}$ and so to $J$ and so to $A$.
:::

::: {.problem #prob-mit1806s10-10-q3 origin="external" source="mit1806s10-10-q3"}
Why are these statements all true?

(a) If $A$ is similar to $B$ then $A^2$ is similar to $B^2$.

(b) $A^2$ and $B^2$ can be similar when $A$ and $B$ are not similar.

(c) $\begin{bmatrix}3&0\\0&4\end{bmatrix}$ is similar to $\begin{bmatrix}3&1\\0&4\end{bmatrix}$.

(d) $\begin{bmatrix}3&0\\0&3\end{bmatrix}$ is not similar to $\begin{bmatrix}3&1\\0&3\end{bmatrix}$.

(e) If we exchange rows 1 and 2 of $A$, and then exchange columns 1 and 2 the eigenvalues stay the same. In this case $M=?$
:::

::: {.problem #prob-mit1806s10-10-q4 origin="external" source="mit1806s10-10-q4"}
If an $n\times n$ matrix $A$ has all eigenvalues $\lambda=0$ prove that $A^n$ is the zero matrix.
:::

::: {.problem #prob-mit1806s10-10-q5 origin="external" source="mit1806s10-10-q5"}
For the shifted $QR$ method in the Worked Example 6.6 B, show that $A_2$ is similar to $A_1$. No change in eigenvalues, and the $A$'s quickly approach a diagonal matrix.

*Note (these notes):* In the shifted $QR$ method one factors $A_1-sI=Q_1R_1$ (with $Q_1$ orthogonal) and sets $A_2=R_1Q_1+sI$.
:::

::: {.problem #prob-mit1806s10-10-q6 origin="external" source="mit1806s10-10-q6"}
If $A$ is similar to $A^{-1}$, must all the eigenvalues equal 1 or $-1$?
:::
