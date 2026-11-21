<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18065ps-30-q1" status="draft"}
1. Ordinary convolution = polynomial product: $(2+x+3x^2)(3+x+2x^2)=6+5x+14x^2+5x^3+6x^4$, so $\mathbf{c}*\mathbf{d}=(6,5,14,5,6)$.

2. Cyclic convolution folds entries $3,4$ onto $0,1$: $\mathbf{c}\circledast\mathbf{d}=(6+5,\,5+6,\,14)=(11,11,14)$.

3. Check: the sums are $36=6\cdot6=(\sum c_i)(\sum d_i)$ in both cases.
:::

::: {.solution for="prob-mit18065ps-31-q3" status="draft"}
1. $\sum_ke_k=\sum_k\sum_{i+j=k}c_id_j$ runs over every pair $(i,j)$ exactly once, so it equals $\sum_i\sum_jc_id_j=(\sum c_i)(\sum d_j)$.

2. Equivalently, $\mathbf{e}$ holds the coefficients of $c(x)d(x)$, and setting $x=1$ adds up coefficients: $e(1)=c(1)d(1)$.

3. The check: $(1,2,3)*(5,0,4)=(5,10,19,8,12)$, whose sum $54$ equals $6\cdot9$. It catches most arithmetic errors, but not errors that cancel in the sum (or put a correct amount in the wrong position).
:::

::: {.solution for="prob-mit18065ps-31-q5" status="draft"}
1. $C$ is the all-ones matrix, with eigenvalues $4,0,0,0$.

2. By @thm-circulant-eigenvectors the eigenvalues are the entries of $F\mathbf{c}$: $(F\mathbf{c})_k=1+w^k+w^{2k}+w^{3k}$ with $w=i$. For $k=0$ this is $4$; for $k=1,2,3$ it is $0$.

3. $1+z+z^2+z^3=(z^4-1)/(z-1)$ for $z\ne1$, so its roots are the fourth roots of unity other than $1$: $z=i,\,-1,\,-i$. These are $w^1,w^2,w^3$, which is why the last three entries of $F\mathbf{c}$ vanish.
:::

::: {.solution for="prob-mit18065ps-32-q4" status="draft"}
1. $D\mathbf{q}_k=\lambda_k(D)\mathbf{q}_k$ and $C\mathbf{q}_k=\lambda_k(C)\mathbf{q}_k$ for the same vector $\mathbf{q}_k$.

2. So $CD\mathbf{q}_k=C(\lambda_k(D)\mathbf{q}_k)=\lambda_k(D)\lambda_k(C)\mathbf{q}_k$: $\mathbf{q}_k$ is an eigenvector of $CD$ with eigenvalue $\lambda_k(C)\lambda_k(D)$.

3. In matrix form, $C=F\Lambda_CF^{-1}$ and $D=F\Lambda_DF^{-1}$ give $CD=F\Lambda_C\Lambda_DF^{-1}=DC$, since diagonal matrices commute.
:::
