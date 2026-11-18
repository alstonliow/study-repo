<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-7-q8" status="draft"}
(a) The eigenvalues are distinct, so $B=S\Lambda S^{-1}$ with $\Lambda=\operatorname{diag}(0,1,2)$ (@thm-distinct-eigenvalues-independent). Multiplying by invertible matrices does not change the rank, so $\operatorname{rank}B=\operatorname{rank}\Lambda=2$.

(b) $\det B^{\mathsf T}B=(\det B)^2=(0\cdot1\cdot2)^2=0$.

(c) Not determined. $B=\operatorname{diag}(0,1,2)$ gives $B^{\mathsf T}B=\operatorname{diag}(0,1,4)$, while $B=\begin{bmatrix}0&1&0\\0&1&0\\0&0&2\end{bmatrix}$ (triangular, eigenvalues $0,1,2$) gives $B^{\mathsf T}B=\begin{bmatrix}0&0&0\\0&2&0\\0&0&4\end{bmatrix}$ with eigenvalues $0,2,4$.

(d) If $B\mathbf{x}=\lambda\mathbf{x}$ then $(B^2+I)\mathbf{x}=(\lambda^2+1)\mathbf{x}$ and $(B^2+I)^{-1}\mathbf{x}=\frac1{\lambda^2+1}\mathbf{x}$. The eigenvalues are $1,\ \frac12,\ \frac15$.
:::

::: {.solution for="prob-mit1806s10-7-q9" status="draft"}
1. $A$ is triangular: eigenvalues $1,4,6$.

2. $\det(B-\lambda I)=(2-\lambda)\big(\lambda^2-3\big)$ (expand along row 2), so the eigenvalues are $2,\ \sqrt3,\ -\sqrt3$. Check: the trace is $2$ and the determinant is $-6=2\cdot\sqrt3\cdot(-\sqrt3)$.

3. $C$ has rank $1$, so $0$ is an eigenvalue twice; the trace gives the third: $6$, with eigenvector $(1,1,1)$.
:::
