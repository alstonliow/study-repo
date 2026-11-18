<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-8-q9" status="draft"}
1. $\det(A-\lambda I)=(4-\lambda)(-\lambda)-(2+i)(2-i)=\lambda^2-4\lambda-5=(\lambda-5)(\lambda+1)$. The eigenvalues are $5$ and $-1$, both real.

2. Proof: conjugate $A\mathbf{x}=\lambda\mathbf{x}$ to $\bar A\bar{\mathbf{x}}=\bar\lambda\bar{\mathbf{x}}$ and transpose: $\bar{\mathbf{x}}^{\mathsf T}\bar A^{\mathsf T}=\bar\lambda\bar{\mathbf{x}}^{\mathsf T}$, i.e. $\bar{\mathbf{x}}^{\mathsf T}A=\bar\lambda\bar{\mathbf{x}}^{\mathsf T}$.

3. Multiply on the right by $\mathbf{x}$: $\bar{\mathbf{x}}^{\mathsf T}A\mathbf{x}=\bar\lambda\,\bar{\mathbf{x}}^{\mathsf T}\mathbf{x}$. Multiplying $A\mathbf{x}=\lambda\mathbf{x}$ on the left by $\bar{\mathbf{x}}^{\mathsf T}$ gives $\bar{\mathbf{x}}^{\mathsf T}A\mathbf{x}=\lambda\,\bar{\mathbf{x}}^{\mathsf T}\mathbf{x}$.

4. $\bar{\mathbf{x}}^{\mathsf T}\mathbf{x}=\sum\lvert x_i\rvert^2>0$, so $\lambda=\bar\lambda$ (@thm-hermitian-real-eigenvalues).
:::
