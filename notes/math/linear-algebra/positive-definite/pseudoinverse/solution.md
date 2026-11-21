<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18065ps-9-q2" status="draft"}
1. If $A=U\Sigma V^{\mathsf T}$ then $A^{+}=V\Sigma^{+}U^{\mathsf T}$, where $\Sigma^{+}$ inverts the $r$ nonzero singular values. Both have $r$ nonzero singular values, so both have rank $r$.

2. Not in general. $A=\begin{bmatrix}0&1\\0&0\end{bmatrix}$ has $A^{+}=\begin{bmatrix}0&0\\1&0\end{bmatrix}$; the only eigenvector line of $A$ is along $(1,0)$, that of $A^{+}$ along $(0,1)$.

3. When $A$ is invertible, $A^{+}=A^{-1}$: same eigenvectors, eigenvalues $1/\lambda$. When $A=Q\Lambda Q^{\mathsf T}$ is symmetric, $A^{+}=Q\Lambda^{+}Q^{\mathsf T}$: same eigenvectors, eigenvalues $1/\lambda_i$ for $\lambda_i\ne0$ and $0$ for $\lambda_i=0$. For other square matrices the eigenvalues of $A^{+}$ are not determined by those of $A$ (in the example both have only $\lambda=0$).
:::
