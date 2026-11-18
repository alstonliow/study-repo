<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-7-q4" status="draft"}
1. Computing each $C_{ij}=(-1)^{i+j}\det M_{ij}$:
   $$C=\begin{bmatrix}6&-3&0\\3&1&-1\\-6&2&1\end{bmatrix},\qquad AC^{\mathsf T}=\begin{bmatrix}3&0&0\\0&3&0\\0&0&3\end{bmatrix}=(\det A)I,$$
   so $\det A=3$ (@thm-inverse-by-cofactors).

2. The entry $4$ sits in position $(1,3)$, whose cofactor is $C_{13}=0$. Expanding along row 1, $\det A=a_{11}C_{11}+a_{12}C_{12}+a_{13}C_{13}$, and $C_{13}$ does not involve row 1. So any value of $a_{13}$ gives the same determinant.
:::

::: {.solution for="prob-mit1806s10-7-q5" status="draft"}
1. Rows are the partials of $x,y,z$ with respect to $\rho,\phi,\theta$:
   $$J=\det\begin{bmatrix}\sin\phi\cos\theta&\rho\cos\phi\cos\theta&-\rho\sin\phi\sin\theta\\\sin\phi\sin\theta&\rho\cos\phi\sin\theta&\rho\sin\phi\cos\theta\\\cos\phi&-\rho\sin\phi&0\end{bmatrix}.$$

2. Expand along row 3. The $(3,1)$ cofactor is $\rho^2\cos\phi\sin\phi(\cos^2\theta+\sin^2\theta)=\rho^2\sin\phi\cos\phi$. The $(3,2)$ entry $-\rho\sin\phi$ has sign $-1$ and minor $\rho\sin^2\phi(\cos^2\theta+\sin^2\theta)=\rho\sin^2\phi$, contributing $+\rho^2\sin^3\phi$.

3. So $J=\rho^2\sin\phi\cos^2\phi+\rho^2\sin^3\phi=\rho^2\sin\phi$. The small coordinate box has edges $J$-scaled as in @thm-determinant-volume, which is why $dV=\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$.
:::
