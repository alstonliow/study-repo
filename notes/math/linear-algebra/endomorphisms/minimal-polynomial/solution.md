<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-las-3-q2" status="draft"}
1. $A=(\lambda-1)I+J$, where $J$ is the all-ones matrix. $J$ has rank $1$, so $\ker J$ has dimension $n-1$: $0$ is an eigenvalue of $J$ with $n-1$ independent eigenvectors. Also $J\mathbf 1=n\mathbf 1$ for $\mathbf 1=(1,\dots,1)^{\mathsf T}$.

2. So $J$ is diagonalisable with eigenvalues $n$ (once) and $0$ ($n-1$ times); equivalently $J^2=nJ$, so $m_J=t(t-n)$ for $n\ge2$.

3. $A=(\lambda-1)I+J$ has the same eigenvectors, with eigenvalues $\lambda-1+n$ (once) and $\lambda-1$ ($n-1$ times).

4. The determinant is the product of the eigenvalues, computed in the eigenvector basis: $\det A=(\lambda+n-1)(\lambda-1)^{n-1}$.
:::

::: {.solution for="prob-camib-las-3-q3" status="draft"}
1. Let $m(t)=\sum_kc_kt^k$ be the minimal polynomial of $A$ over $\mathbb C$, and $\bar m(t)=\sum_k\bar c_kt^k$.

2. Conjugating every entry of $0=m(A)=\sum_kc_kA^k$ gives $0=\sum_k\bar c_k\bar A^k=\bar m(A)$, since $A=\bar A$.

3. $\bar m$ is monic of the same degree, so $m-\bar m$ has smaller degree and kills $A$. By minimality (@lem-minimal-polynomial-divides) $m-\bar m=0$, so every $c_k$ is real.
:::
