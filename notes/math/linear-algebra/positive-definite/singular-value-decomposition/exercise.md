::: {.problem #prob-mit1806s10-10-q7 origin="external" source="mit1806s10-10-q7"}
Find the eigenvalues and unit eigenvectors of $A^{\mathsf T}A$ and $AA^{\mathsf T}$. Keep each $A\mathbf{v}=\sigma\mathbf{u}$ for the Fibonacci matrix $A=\begin{bmatrix}1&1\\1&0\end{bmatrix}$. Construct the singular value decomposition and verify that $A$ equals $U\Sigma V^{\mathsf T}$.
:::

::: {.problem #prob-mit1806s10-10-q8 origin="external" source="mit1806s10-10-q8"}
Suppose $A$ has orthogonal columns $\mathbf{w}_1,\dots,\mathbf{w}_n$ of lengths $\sigma_1,\dots,\sigma_n$. What are $U$, $\Sigma$ and $V$ in the SVD?
:::

::: {.problem #prob-mit1806s10-10-q9 origin="external" source="mit1806s10-10-q9"}
The $1,-1$ first difference matrix $A$ has $A^{\mathsf T}A$ the second difference matrix. The singular vectors of $A$ are sine vectors $\mathbf{v}$ and cosine vectors $\mathbf{u}$. Then $A\mathbf{v}=\sigma\mathbf{u}$ is the discrete form of $d/dx(\sin cx)=c(\cos cx)$. This is the best SVD I have seen.
$$A=\begin{pmatrix}1&0&0\\-1&1&0\\0&-1&1\\0&0&-1\end{pmatrix}\qquad A^{\mathsf T}A=\begin{pmatrix}2&-1&0\\-1&2&-1\\0&-1&2\end{pmatrix}.$$
Then the orthogonal sine matrix is
$$V=\frac1{\sqrt2}\begin{pmatrix}\sin\pi/4&\sin2\pi/4&\sin3\pi/4\\\sin2\pi/4&\sin4\pi/4&\sin6\pi/4\\\sin3\pi/4&\sin6\pi/4&\sin9\pi/4\end{pmatrix}.$$

(a) Put numbers in $V$: The unit eigenvectors of $A^{\mathsf T}A$ are singular vectors of $A$. Show that the columns of $V$ have $A^{\mathsf T}A\mathbf{v}=\lambda\mathbf{v}$ with $\lambda=2-\sqrt2,\ 2,\ 2+\sqrt2$.

(b) Multiply $AV$ and verify taht its columns are orthogonal. They are $\sigma_1\mathbf{u}_1$ and $\sigma_2\mathbf{u}_2$ and $\sigma_3\mathbf{u}_3$. The first columns of the cosine matrix $U$ are $\mathbf{u}_1,\mathbf{u}_2,\mathbf{u}_3$.

(c) Since $A$ is $4\times3$ weneed a fourth orthogonal vector $\mathbf{u}_4$. It comes from the nullspace of $A^{\mathsf T}$. What is $\mathbf{u}_4$?
:::

::: {.problem #prob-mit18065ps-6-q6 origin="external" source="mit18065ps-6-q6"}
Find the $\sigma$'s and $\mathbf{v}$'s and $\mathbf{u}$'s in the SVD for $A=\begin{bmatrix}3&4\\0&5\end{bmatrix}$. Use equation (12).

*Note (these notes):* Equation (12) of the textbook is $\mathbf{u}_i=A\mathbf{v}_i/\sigma_i$, as in @thm-svd.
:::
