<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs221hw-1-q1" status="draft"}
**(a)** $C=AB$ has $mp$ entries and each, $C_{ij}=\sum_{k=1}^{n}A_{ik}B_{kj}$, costs $n$ multiplications and $n-1$ additions. The total is $\Theta(mnp)$, so $O(mnp)$.

**(b)** In `einops` notation each axis is named; an axis that appears in the inputs but not in the output is summed over.

1. $X\mathbf w$: `'n d, d -> n'`. The output keeps $n$ and sums over $d$: entry $i$ is $\sum_{k} X_{ik}w_k$.
2. $XX^\top$: `'n d, m d -> n m'` (both operands are $X$; the second copy's row axis is renamed $m$ so it stays separate). Entry $(i,j)$ is $\sum_k X_{ik}X_{jk}$, the dot product of rows $i$ and $j$.
3. $\operatorname{diag}(X^\top X)$: `'n d, n d -> d'`. Both operands share $n$ and $d$; $d$ is kept and $n$ is summed, giving $\sum_i X_{id}^2$, the squared norm of column $d$, which is exactly the diagonal entry $(X^\top X)_{dd}$.
:::
