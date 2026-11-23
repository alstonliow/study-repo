<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit18335ps-3-q2" status="draft"}
**(a)**

1. Substitute $A=QTQ^*$: $AA^*=QTQ^*QT^*Q^*=QTT^*Q^*$ and $A^*A=QT^*TQ^*$. Multiplying $AA^*=A^*A$ by $Q^*$ on the left and $Q$ on the right gives $TT^*=T^*T$.

2. Compare diagonal entries. $(T^*T)_{jj}=\sum_i\lvert t_{ij}\rvert^2$ is the squared length of column $j$, and $(TT^*)_{jj}=\sum_i\lvert t_{ji}\rvert^2$ is the squared length of row $j$. Since $T$ is upper triangular, column $j$ has entries only in rows $i\le j$ and row $j$ only in columns $i\ge j$.

3. *Induction on $j$.* Suppose rows $1,\dots,j-1$ have no off-diagonal entries; then column $j$ has no entries above the diagonal, so $(T^*T)_{jj}=\lvert t_{jj}\rvert^2$. Equality with $(TT^*)_{jj}=\lvert t_{jj}\rvert^2+\sum_{i>j}\lvert t_{ji}\rvert^2$ forces $t_{ji}=0$ for all $i>j$. (For $j=1$ the hypothesis is empty.)

4. Hence $T$ is diagonal and $A=QTQ^*$ is a unitary diagonalization: the columns of $Q$ are orthonormal eigenvectors. Hermitian ($A^*=A$) and unitary ($A^*=A^{-1}$) matrices commute with $A^*$, so they are normal.

**(b)** The eigenvalues are the diagonal entries $t_{11},\dots,t_{mm}$ (zero extra cost). For the eigenvector of $\lambda=t_{ii}$, write $T-\lambda I$ in blocks around position $i$:
$$\begin{bmatrix}T_1-\lambda I&\mathbf{u}&B\\0&0&\mathbf{v}^*\\0&0&T_2-\lambda I\end{bmatrix}\begin{bmatrix}\mathbf{y}\\1\\\mathbf{0}\end{bmatrix}=\mathbf{0},$$
with $T_1$ the leading $(i-1)\times(i-1)$ block and $\mathbf{u}$ the part of column $i$ above the diagonal. The last block rows hold because the last part of the vector is zero (and $T_2-\lambda I$ is invertible since eigenvalues are distinct, so this is forced); the first block row requires the upper triangular solve $(T_1-\lambda I)\mathbf{y}=-\mathbf{u}$, whose matrix is invertible for distinct eigenvalues. So:

1. for each $i$, solve $(T_1-t_{ii}I)\mathbf{y}=-\mathbf{u}$ by back substitution: $\sim(i-1)^2$ flops (@def-back-substitution);

2. form the eigenvector $Q\mathbf{z}$ of $A$, $\mathbf{z}=(\mathbf{y},1,\mathbf{0})$, using only the first $i$ columns of $Q$: $\sim2mi$ flops.

Summing over $i$: $\sum_ii^2\sim m^3/3$ and $\sum_i2mi\sim m^3$, so the total is $\sim\tfrac43m^3$ flops, $K=\tfrac43$.
:::
