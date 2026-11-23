<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit18335ps-3-q3" status="draft"}
We count misses as in the course's ideal-cache model, with the line size treated as a constant (otherwise every bound below is divided by $L$ for the contiguous accesses).

**(a)** Each right-hand side reads all $\sim m^2/2$ entries of $R$. Once $m^2\gg Z$, the entries of $R$ read for column $k$ of $B$ have been evicted before column $k+1$ needs them, because the whole of $R$ is swept in between. So each of the $n$ solves incurs $\Theta(m^2)$ misses, and
$$Q(m,n;Z)=\Theta(m^2n)$$
(the $\Theta(mn)$ misses for reading $B$ and writing $X$ are of lower order). The cache gives no asymptotic benefit at all.

**(b)** Use a recursive block algorithm. Split
$$\begin{bmatrix}R_{11}&R_{12}\\0&R_{22}\end{bmatrix}\begin{bmatrix}X_1\\X_2\end{bmatrix}=\begin{bmatrix}B_1\\B_2\end{bmatrix}$$
into halves ($R_{11},R_{22}$ upper triangular of size $m/2$), and split $X,B$ into two column halves as well. Then, as in back substitution but with blocks:

1. solve $R_{22}X_2=B_2$ recursively (two subproblems, one per column half);

2. form $B_1-R_{12}X_2$ with a cache-optimal matrix multiplication, $\Theta(m^3/\sqrt Z)$ misses (@thm-blocked-matmul-misses or @prp-co-matrix);

3. solve $R_{11}X_1=B_1-R_{12}X_2$ recursively (two more subproblems).

So $Q(m)=4Q(m/2)+\Theta(m^3/\sqrt Z)+\Theta(m^2)$, with $Q(m)=\Theta(m^2)$ once the subproblem fits in cache ($m^2\lesssim Z$). The multiplication term shrinks by a factor $8/4=2$ per level, so the top level dominates (the recursion stops at size $\sqrt Z$, where the $\Theta(m^2)$ terms sum to $\Theta(m^2\log(m/\sqrt Z))$, which is of lower order). Hence
$$Q(m;Z)=\Theta\bigl(m^3/\sqrt Z\bigr),$$
a factor $1/\sqrt Z$ better than part (a) with $n=m$: the same savings as for matrix multiplication. A cache-aware version with $b\times b$ blocks, $b=\Theta(\sqrt Z)$, doing ordinary back substitution on blocks, achieves the same bound.
:::
