<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-7-q8" status="draft"}
(a) The eigenvalues are distinct, so $B=S\Lambda S^{-1}$ with $\Lambda=\operatorname{diag}(0,1,2)$ (@lem-eigenspaces-independent). Multiplying by invertible matrices does not change the rank, so $\operatorname{rank}B=\operatorname{rank}\Lambda=2$.

(b) $\det B^{\mathsf T}B=(\det B)^2=(0\cdot1\cdot2)^2=0$.

(c) Not determined. $B=\operatorname{diag}(0,1,2)$ gives $B^{\mathsf T}B=\operatorname{diag}(0,1,4)$, while $B=\begin{bmatrix}0&1&0\\0&1&0\\0&0&2\end{bmatrix}$ (triangular, eigenvalues $0,1,2$) gives $B^{\mathsf T}B=\begin{bmatrix}0&0&0\\0&2&0\\0&0&4\end{bmatrix}$ with eigenvalues $0,2,4$.

(d) If $B\mathbf{x}=\lambda\mathbf{x}$ then $(B^2+I)\mathbf{x}=(\lambda^2+1)\mathbf{x}$ and $(B^2+I)^{-1}\mathbf{x}=\frac1{\lambda^2+1}\mathbf{x}$. The eigenvalues are $1,\ \frac12,\ \frac15$.
:::

::: {.solution for="prob-mit1806s10-7-q9" status="draft"}
1. $A$ is triangular: eigenvalues $1,4,6$.

2. $\det(B-\lambda I)=(2-\lambda)\big(\lambda^2-3\big)$ (expand along row 2), so the eigenvalues are $2,\ \sqrt3,\ -\sqrt3$. Check: the trace is $2$ and the determinant is $-6=2\cdot\sqrt3\cdot(-\sqrt3)$.

3. $C$ has rank $1$, so $0$ is an eigenvalue twice; the trace gives the third: $6$, with eigenvector $(1,1,1)$.
:::

::: {.solution for="prob-mit18065ps-4-q2" status="draft"}
1. $\det(A-\lambda I)=\lambda^2-\lambda-2=(\lambda-2)(\lambda+1)$, so $\lambda=2$ and $-1$; their sum $1$ is the trace $0+1$.

2. $\lambda=2$: $\mathbf{x}=(1,1)$. $\lambda=-1$: $\mathbf{x}=(2,-1)$, since $A(2,-1)=(-2,1)$.

3. From $A\mathbf{x}=\lambda\mathbf{x}$ we get $A^{-1}\mathbf{x}=\frac1\lambda\mathbf{x}$. So $A^{-1}$ has the *same* eigenvectors, with eigenvalues $\frac12$ and $-1$; their sum $-\frac12$ is the trace $-\frac12+0$ of $A^{-1}$. In general the eigenvalues are $1/\lambda_1$ and $1/\lambda_2$.
:::

::: {.solution for="prob-mit18065ps-4-q11" status="draft"}
1. $A^{\mathsf T}-\lambda I=(A-\lambda I)^{\mathsf T}$, and a matrix and its transpose have the same determinant. So the characteristic polynomials agree.

2. Example: $A=\begin{bmatrix}1&1\\0&0\end{bmatrix}$ has eigenvectors $(1,0)$ for $\lambda=1$ and $(1,-1)$ for $\lambda=0$. $A^{\mathsf T}=\begin{bmatrix}1&0\\1&0\end{bmatrix}$ has eigenvectors $(1,1)$ for $\lambda=1$ and $(0,1)$ for $\lambda=0$. Different.
:::
