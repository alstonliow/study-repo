<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-8-q6" status="draft"}
(a) The eigenvalues are $1\pm b$ (eigenvectors $(1,\pm1)$). Any $b$ with $\lvert b\rvert>1$ works, e.g. $b=2$: eigenvalues $3$ and $-1$.

(b) The pivots are $1$ and $1-b^2$, whose product is $\det=1-b^2<0$. So the second pivot is negative. (In general the signs of the pivots match the signs of the eigenvalues, @prp-signs-of-pivots-and-eigenvalues.)

(c) The eigenvalues add up to the trace, $1+1=2>0$, so they cannot both be negative.
:::

::: {.solution for="prob-mit1806s10-8-q7" status="draft"}
1. The hidden assumption is that $\mathbf{x}$ is real. An eigenvector for a complex $\lambda$ has complex components, and then $\mathbf{x}^{\mathsf T}A\mathbf{x}$ and $\mathbf{x}^{\mathsf T}\mathbf{x}$ need not be real, and $\mathbf{x}^{\mathsf T}\mathbf{x}$ can even be $0$.

2. Test: $A\mathbf{x}=(-1,i)=i\,(i,1)$, so $\lambda=i$. But $\mathbf{x}^{\mathsf T}\mathbf{x}=i^2+1=0$ and $\mathbf{x}^{\mathsf T}A\mathbf{x}=i\cdot(-1)+1\cdot i=0$: the "formula" is $0/0$. The correct tool is $\bar{\mathbf{x}}^{\mathsf T}\mathbf{x}>0$, which proves realness only when $A$ is symmetric (@lem-self-adjoint-eigenvalues).
:::

::: {.solution for="prob-mit1806s10-8-q8" status="draft"}
1. $A$ exchanges rows 1 and 3: it is a permutation, hence invertible, orthogonal and Markov (entries $\ge0$, columns add to $1$). It is symmetric, hence diagonalizable. It is not a projection: $A^2=I\neq A$.

2. $B$ is the projection onto the line through $(1,1,1)$: $B^2=B=B^{\mathsf T}$. It is Markov and symmetric, hence diagonalizable. It is singular (rank $1$), so not invertible and not orthogonal, and not a permutation.

3. Factorizations. $A$: $LU$ needs a row exchange first (the $(1,1)$ entry is $0$), so only $PA=LU$; $QR$ yes ($A$ is itself orthogonal, $R=I$); $S\Lambda S^{-1}$ and $Q\Lambda Q^{\mathsf T}$ yes (symmetric). $B$: $LU$ yes ($B=\frac13\begin{bmatrix}1&0&0\\1&1&0\\1&0&1\end{bmatrix}\begin{bmatrix}1&1&1\\0&0&0\\0&0&0\end{bmatrix}$, with zero pivots after the first); $QR$ as in @thm-qr-factorization needs independent columns, so not for $B$; $S\Lambda S^{-1}$ and $Q\Lambda Q^{\mathsf T}$ yes (symmetric).
:::

::: {.solution for="prob-mit1806s10-8-q10" status="draft"}
1. $a_{11}=\mathbf{e}_1^{\mathsf T}A\mathbf{e}_1=(Q^{\mathsf T}\mathbf{e}_1)^{\mathsf T}\Lambda(Q^{\mathsf T}\mathbf{e}_1)$. Let $\mathbf{v}=Q^{\mathsf T}\mathbf{e}_1$, the first row of $Q$ written as a column. Then
   $$a_{11}=\sum_i\lambda_iv_i^2=\lambda_1q_{11}^2+\lambda_2q_{12}^2+\dots+\lambda_nq_{1n}^2.$$

2. $Q^{\mathsf T}$ preserves length (@prp-orthonormal-columns-preserve-length), so $\sum v_i^2=\lVert\mathbf{e}_1\rVert^2=1$.

3. Hence $a_{11}$ is a weighted average of the eigenvalues, and $a_{11}\le\lambda_{\max}\sum v_i^2=\lambda_{\max}$. The same argument works for every diagonal entry.
:::

::: {.solution for="prob-mit1806s10-9-q7" status="draft"}
1. With $s_{jk}=\sin\frac{jk\pi}6$,
   $$S=\begin{bmatrix}\frac12&\frac{\sqrt3}2&1&\frac{\sqrt3}2&\frac12\\\frac{\sqrt3}2&\frac{\sqrt3}2&0&-\frac{\sqrt3}2&-\frac{\sqrt3}2\\1&0&-1&0&1\\\frac{\sqrt3}2&-\frac{\sqrt3}2&0&\frac{\sqrt3}2&-\frac{\sqrt3}2\\\frac12&-\frac{\sqrt3}2&1&-\frac{\sqrt3}2&\frac12\end{bmatrix}.$$

2. For column $k$, row $j$ of $K\mathbf{s}_k$ is $-\sin\frac{(j-1)k\pi}6+2\sin\frac{jk\pi}6-\sin\frac{(j+1)k\pi}6=\big(2-2\cos\frac{k\pi}6\big)\sin\frac{jk\pi}6$ (sum-to-product), and the boundary rows work because $\sin0=\sin\frac{6k\pi}6=0$. So $K\mathbf{s}_k=\lambda_k\mathbf{s}_k$ with $\lambda_k=2-2\cos\frac{k\pi}6$.

3. The eigenvalues are $2-\sqrt3,\ 1,\ 2,\ 3,\ 2+\sqrt3$, all positive. Their sum is $10=\operatorname{tr}K$ and their product is $(4-3)\cdot1\cdot2\cdot3=6=\det K$.
:::

::: {.solution for="prob-mit18065ps-6-q1" status="draft"}
1. $\mathbf{x}^{\mathsf T}\mathbf{x}=\sum_{i,j}c_ic_j\mathbf{v}_i^{\mathsf T}\mathbf{v}_j$, and $\mathbf{v}_i^{\mathsf T}\mathbf{v}_j$ is $1$ for $i=j$, $0$ otherwise. Only the squares survive.

2. $S\mathbf{x}=\sum_jc_j\lambda_j\mathbf{v}_j$, so $\mathbf{x}^{\mathsf T}S\mathbf{x}=\sum_{i,j}c_ic_j\lambda_j\mathbf{v}_i^{\mathsf T}\mathbf{v}_j=\sum_j\lambda_jc_j^2$ by the same orthonormality.
:::
