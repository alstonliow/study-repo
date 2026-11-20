<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-2-q7" status="draft"}
(a) A cyclic shift of the three rows: row 1 to position 2, row 2 to position 3, row 3 to position 1,
$$P=\begin{bmatrix}0&0&1\\1&0&0\\0&1&0\end{bmatrix}.$$
Applying it three times returns every row to its place, so $P^3=I$, while $P\neq I$.

(b) Keep the first row fixed and cycle the other three: $\widehat P=\begin{bmatrix}1&0\\0&P\end{bmatrix}$. Then $\widehat P^3=I$, so $\widehat P^4=\widehat P\neq I$.
:::

::: {.solution for="prob-mit1806s10-2-q8" status="draft"}
1. **Unit lower triangular $L$: a group.** Products of such matrices are again unit lower triangular, and Gauss–Jordan on $L$ uses only downward steps, so $L^{-1}$ is unit lower triangular too.

2. **Symmetric $S$: not a group.** $\begin{bmatrix}1&1\\1&0\end{bmatrix}\begin{bmatrix}1&0\\0&2\end{bmatrix}=\begin{bmatrix}1&2\\1&0\end{bmatrix}$ is not symmetric.

3. **Positive matrices $M$: not a group.** $\begin{bmatrix}2&1\\1&1\end{bmatrix}^{-1}=\begin{bmatrix}1&-1\\-1&2\end{bmatrix}$ has negative entries.

4. **Diagonal invertible $D$: a group.** Products and inverses are diagonal with nonzero diagonal.

5. **Permutation matrices $P$: a group** (@prp-permutation-inverse-transpose: $P_1P_2$ is a permutation and $P^{-1}=P^{\mathsf T}$ is one).

6. **$Q^{\mathsf T}=Q^{-1}$: a group.** $(Q_1Q_2)^{\mathsf T}=Q_2^{\mathsf T}Q_1^{\mathsf T}=Q_2^{-1}Q_1^{-1}=(Q_1Q_2)^{-1}$, and $(Q^{-1})^{\mathsf T}=(Q^{\mathsf T})^{\mathsf T}=Q=(Q^{-1})^{-1}$.

7. **Two more:** the invertible upper triangular matrices; the matrices with determinant $1$ (by the product rule, @thm-determinant-multiplicative). Also the nonzero multiples $cI$ of the identity.
:::
