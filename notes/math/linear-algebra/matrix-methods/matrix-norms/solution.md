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

::: {.solution for="prob-mit18335ps-2-q2" status="draft"}
**(a)** Equation (3.10) of the textbook is the formula $\lVert A\rVert_\infty=\max_i\sum_j\lvert a_{ij}\rvert$, the largest absolute row sum. Derivation:

1. For $\lVert\mathbf{x}\rVert_\infty=1$, every entry obeys $\lvert(A\mathbf{x})_i\rvert\le\sum_j\lvert a_{ij}\rvert\lvert x_j\rvert\le\sum_j\lvert a_{ij}\rvert$, so $\lVert A\mathbf{x}\rVert_\infty\le\max_i\sum_j\lvert a_{ij}\rvert$.

2. Let row $k$ attain the maximum and choose $x_j=\overline{a_{kj}}/\lvert a_{kj}\rvert$ ($x_j=1$ where $a_{kj}=0$). Then $\lVert\mathbf{x}\rVert_\infty=1$ and $(A\mathbf{x})_k=\sum_j\lvert a_{kj}\rvert$, so the bound is attained.

This is @prp-induced-one-infinity-norms. The library routine for the induced $\infty$-norm accumulates, for each row, the sum of the absolute values of its entries and returns the largest of these sums, which is exactly this formula. (The source file was not consulted for these notes; the statement describes what any correct implementation must compute.)

*Note (these notes):* part (b) refers to a textbook exercise whose statement is not reproduced here and is left unsolved.
:::
