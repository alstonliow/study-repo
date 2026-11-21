<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18065ps-7-q2" status="draft"}
By @thm-eckart-young-spectral and @thm-eckart-young-frobenius the answer is $\sigma_1\mathbf{u}_1\mathbf{v}_1^{\mathsf T}$.

1. $\operatorname{diag}(3,2,1)$: $\sigma_1=3$, $\mathbf{u}_1=\mathbf{v}_1=\mathbf{e}_1$, so $A_1=\operatorname{diag}(3,0,0)$.

2. $\begin{bmatrix}0&3\\2&0\end{bmatrix}$: $A\mathbf{e}_2=3\mathbf{e}_1$ and $A\mathbf{e}_1=2\mathbf{e}_2$, so $\sigma_1=3$ with $\mathbf{v}_1=\mathbf{e}_2$, $\mathbf{u}_1=\mathbf{e}_1$: $A_1=\begin{bmatrix}0&3\\0&0\end{bmatrix}$.

3. $\begin{bmatrix}2&1\\1&2\end{bmatrix}$ is symmetric positive definite with eigenvalues $3$ and $1$, eigenvector $(1,1)/\sqrt2$ for $3$. So $A_1=\frac32\begin{bmatrix}1&1\\1&1\end{bmatrix}$.
:::

::: {.solution for="prob-mit18065ps-17-q2" status="draft"}
1. With $A=\operatorname{diag}(a_i)$, $a_i=\frac{2i-1}2$, and $B=-A$: $(AH-HB)_{ij}=a_iH_{ij}+H_{ij}a_j=(a_i+a_j)H_{ij}$.

2. $a_i+a_j=\frac{2i-1+2j-1}2=i+j-1$, so the entry is $(i+j-1)\cdot\frac1{i+j-1}=1$. Hence $AH-HB=\texttt{ones}(n)$, a rank one matrix, and the eigenvalues of $A$ (positive) and $B$ (negative) are separated — which is why $H$ is so close to low rank (@sec-math-linear-algebra-matrix-methods-low-rank-approximation).
:::

::: {.solution for="prob-mit18065ps-17-q6" status="draft"}
1. Multiply $AX-XB=C$ by $X^{-1}$ on both sides: $X^{-1}A-BX^{-1}=X^{-1}CX^{-1}$.

2. So $Y=X^{-1}$ satisfies the Sylvester equation
$$BY-YA=-X^{-1}CX^{-1},$$
with the roles of $A$ and $B$ exchanged. The right side has the same rank as $C$, so a low-rank right side stays low rank.
:::
