<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-7-q10" status="draft"}
1. $A$ is triangular with eigenvalues $4$ and $2$. $N(A-4I)=N\begin{bmatrix}0&0\\1&-2\end{bmatrix}$ is the line through $(2,1)$; $N(A-2I)=N\begin{bmatrix}2&0\\1&0\end{bmatrix}$ is the line through $(0,1)$.

2. So $S$ has one column a nonzero multiple of $(2,1)$ and the other a nonzero multiple of $(0,1)$, in either order: $S=\begin{bmatrix}2a&0\\a&b\end{bmatrix}$ or $\begin{bmatrix}0&2a\\b&a\end{bmatrix}$, $a,b\neq0$.

3. $A^{-1}$ has the same eigenvectors (eigenvalues $\frac14,\frac12$), so the same matrices $S$ diagonalize it.
:::

::: {.solution for="prob-mit1806s10-7-q12" status="draft"}
1. Write $S\Lambda S^{-1}=(S\Lambda)(S^{-1})$. The columns of $S\Lambda$ are $\lambda_i\mathbf{x}_i$, and the rows of $S^{-1}$ are $\mathbf{y}_i^{\mathsf T}$, where $\mathbf{y}_i$ is column $i$ of $(S^{-1})^{\mathsf T}$.

2. Columns times rows (@thm-four-ways-to-multiply) gives $\sum_i(\lambda_i\mathbf{x}_i)\mathbf{y}_i^{\mathsf T}$.
:::
