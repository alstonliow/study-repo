<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-10-q1" status="draft"}
1. $JM$ moves rows 2 and 4 of $M$ up into rows 1 and 3 and puts zeros in rows 2 and 4. $MK$ moves columns 1 and 2 of $M$ into columns 2 and 3 and puts zeros in columns 1 and 4:
   $$JM=\begin{pmatrix}m_{21}&m_{22}&m_{23}&m_{24}\\0&0&0&0\\m_{41}&m_{42}&m_{43}&m_{44}\\0&0&0&0\end{pmatrix},\qquad MK=\begin{pmatrix}0&m_{11}&m_{12}&0\\0&m_{21}&m_{22}&0\\0&m_{31}&m_{32}&0\\0&m_{41}&m_{42}&0\end{pmatrix}.$$

2. Rows 2 and 4 of $JM=MK$ give $m_{21}=m_{22}=0$ and $m_{41}=m_{42}=0$. Columns 1 and 4 give $m_{24}=m_{44}=0$ (and $m_{21}=m_{41}=0$ again).

3. So row 2 of $M$ is $(0,0,m_{23},0)$ and row 4 is $(0,0,m_{43},0)$: two rows that are multiples of the same vector. They are dependent, so $M$ is singular.

4. If $M^{-1}JM=K$ held for some invertible $M$, then $JM=MK$, which forces $M$ to be singular, a contradiction.
:::

::: {.solution for="prob-mit1806s10-10-q2" status="draft"}
1. Let $M_i$ be the "reversal" permutation matrix of the block's size, with $1$s on the antidiagonal; $M_i^{-1}=M_i$. Conjugating by it reverses the order of both rows and columns: $(M_iJ_iM_i)_{jk}=(J_i)_{n+1-j,\,n+1-k}$, where $n$ is the block size. The $1$s of $J_i$ at positions $(r,r+1)$ move to $(n+1-r,\,n-r)$, which is just below the diagonal; the diagonal stays. So $M_i^{-1}J_iM_i=J_i^{\mathsf T}$.

2. Let $M_0$ be block diagonal with blocks $M_i$. By block multiplication $M_0^{-1}JM_0$ is block diagonal with blocks $M_i^{-1}J_iM_i=J_i^{\mathsf T}$, which is $J^{\mathsf T}$.

3. $A^{\mathsf T}=(MJM^{-1})^{\mathsf T}=(M^{\mathsf T})^{-1}J^{\mathsf T}M^{\mathsf T}$, so $A^{\mathsf T}$ is similar to $J^{\mathsf T}$, which is similar to $J$ (step 2), which is similar to $A$. Similarity is transitive, so $A^{\mathsf T}$ is similar to $A$.
:::

::: {.solution for="prob-mit1806s10-10-q3" status="draft"}
(a) If $B=M^{-1}AM$ then $B^2=M^{-1}AMM^{-1}AM=M^{-1}A^2M$.

(b) $A=0$ and $B=\begin{bmatrix}0&1\\0&0\end{bmatrix}$: $A^2=B^2=0$, but only the zero matrix is similar to $0$.

(c) $\begin{bmatrix}3&1\\0&4\end{bmatrix}$ has the distinct eigenvalues $3,4$, so it is diagonalizable: with eigenvectors $(1,0)$ and $(1,1)$, $M=\begin{bmatrix}1&1\\0&1\end{bmatrix}$ gives $M^{-1}\begin{bmatrix}3&1\\0&4\end{bmatrix}M=\begin{bmatrix}3&0\\0&4\end{bmatrix}$.

(d) $3I$ is similar only to itself ($M^{-1}(3I)M=3I$). Equivalently, $3I$ has a plane of eigenvectors and the Jordan block only a line.

(e) The two exchanges are $PAP$ with $P=P^{-1}=\begin{bmatrix}0&1\\1&0\end{bmatrix}$ (extended by $I$ for larger $A$). So $M=P$ and the new matrix $P^{-1}AP$ is similar to $A$.
:::

::: {.solution for="prob-mit1806s10-10-q4" status="draft"}
1. By @thm-jordan-form, $A=MJM^{-1}$ where every block is $J_k(0)$ with $k\le n$.

2. $J_k(0)$ shifts the standard basis: $J_k(0)\mathbf{e}_1=\mathbf{0}$ and $J_k(0)\mathbf{e}_j=\mathbf{e}_{j-1}$. So $J_k(0)^k$ sends every $\mathbf{e}_j$ to $\mathbf{0}$, and $J_k(0)^k=0$; hence also $J_k(0)^n=0$.

3. $J^n$ is block diagonal with blocks $J_k(0)^n=0$, so $J^n=0$ and $A^n=MJ^nM^{-1}=0$.
:::

::: {.solution for="prob-mit1806s10-10-q5" status="draft"}
1. From $A_1-sI=Q_1R_1$ we get $R_1=Q_1^{-1}(A_1-sI)$.

2. Then $A_2=R_1Q_1+sI=Q_1^{-1}(A_1-sI)Q_1+sI=Q_1^{-1}A_1Q_1-sI+sI=Q_1^{-1}A_1Q_1$.

3. So $A_2$ is similar to $A_1$ and has the same eigenvalues (@thm-similar-same-eigenvalues).
:::

::: {.solution for="prob-mit1806s10-10-q6" status="draft"}
No. The eigenvalues of $A^{-1}$ are the reciprocals $1/\lambda$; similarity only forces the set of eigenvalues to be closed under $\lambda\mapsto1/\lambda$. For example $A=\begin{bmatrix}2&0\\0&\frac12\end{bmatrix}$ has $A^{-1}=\begin{bmatrix}\frac12&0\\0&2\end{bmatrix}=PAP$ with $P=\begin{bmatrix}0&1\\1&0\end{bmatrix}$, so $A$ is similar to $A^{-1}$, but its eigenvalues are $2$ and $\frac12$.
:::
