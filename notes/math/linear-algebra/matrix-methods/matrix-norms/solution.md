<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18065ps-7-q10" status="draft"}
1. $A=U\Sigma V^{\mathsf T}$ gives $A^{-1}=V\Sigma^{-1}U^{\mathsf T}$, an SVD with singular values $1/\sigma_2\ge1/\sigma_1$.

2. By @thm-matrix-norms-singular-values, $\lVert A^{-1}\rVert_2=1/\sigma_2$ and $\lVert A^{-1}\rVert_F^2=1/\sigma_1^2+1/\sigma_2^2$.
:::

::: {.solution for="prob-mit18065ps-8-q1" status="draft"}
$\lVert\mathbf{v}\rVert_2^2=\sum_i\lvert v_i\rvert\,\lvert v_i\rvert\le\sum_i\lvert v_i\rvert\,\max_j\lvert v_j\rvert=\lVert\mathbf{v}\rVert_1\lVert\mathbf{v}\rVert_\infty$.
:::

::: {.solution for="prob-mit18065ps-8-q7" status="draft"}
1. $(AB)_{ij}$ is the dot product of row $i$ of $A$ with column $j$ of $B$, so Cauchy–Schwarz gives the stated inequality.

2. Summing the left side over all $i,j$ gives $\lVert AB\rVert_F^2$.

3. The right side factors: $\sum_i\sum_j\lVert\mathbf{r}_i\rVert^2\lVert\mathbf{b}_j\rVert^2=\big(\sum_i\lVert\mathbf{r}_i\rVert^2\big)\big(\sum_j\lVert\mathbf{b}_j\rVert^2\big)=\lVert A\rVert_F^2\lVert B\rVert_F^2$, since the squared Frobenius norm is the sum of squared lengths of the rows (or of the columns).
:::

::: {.solution for="prob-mit18065ps-11-q6" status="draft"}
By the triangle inequality and homogeneity, $\lVert\frac{\mathbf{v}}2+\frac{\mathbf{w}}2\rVert\le\frac12\lVert\mathbf{v}\rVert+\frac12\lVert\mathbf{w}\rVert\le\frac12+\frac12=1$. The same argument with weights $1-t$ and $t$ shows every point of the segment from $\mathbf{v}$ to $\mathbf{w}$ is in the ball.
:::
