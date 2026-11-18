<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-2-q3" status="draft"}
1. Subtract row 1 from rows 2, 3, 4 (multipliers $1$):
   $$\begin{bmatrix}a&a&a&a\\0&b-a&b-a&b-a\\0&b-a&c-a&c-a\\0&b-a&c-a&d-a\end{bmatrix}.$$

2. Subtract the new row 2 from rows 3 and 4, then the new row 3 from row 4 (all multipliers $1$):
   $$U=\begin{bmatrix}a&a&a&a\\0&b-a&b-a&b-a\\0&0&c-b&c-b\\0&0&0&d-c\end{bmatrix},\qquad L=\begin{bmatrix}1&0&0&0\\1&1&0&0\\1&1&1&0\\1&1&1&1\end{bmatrix}.$$

3. The pivots are $a,\ b-a,\ c-b,\ d-c$. Four pivots (no zero met along the way) require
   $$a\neq0,\quad b\neq a,\quad c\neq b,\quad d\neq c.$$
:::

::: {.solution for="prob-mit1806s10-2-q4" status="draft"}
1. From $LDU=L_1D_1U_1$, multiply by $L_1^{-1}$ on the left and $U^{-1}$ on the right: $L_1^{-1}LD=D_1U_1U^{-1}$.

2. Inverses and products of lower triangular matrices with unit diagonal are lower triangular with unit diagonal; so $L_1^{-1}L$ is, and $L_1^{-1}LD$ is lower triangular. Likewise $U_1U^{-1}$ is upper triangular with unit diagonal and $D_1U_1U^{-1}$ is upper triangular.

3. A matrix that is both lower and upper triangular is diagonal. So both sides are diagonal, and then $L_1^{-1}L=(L_1^{-1}LD)D^{-1}$ is diagonal. A diagonal matrix with unit diagonal is $I$, so $L=L_1$. Similarly $U_1U^{-1}=D_1^{-1}(\text{diagonal})$ is diagonal with unit diagonal, so $U=U_1$.

4. The equation becomes $D=D_1$.
:::

::: {.solution for="prob-mit1806s10-2-q5" status="draft"}
1. Elimination on $K$: the first pivot is $2$; subtracting $\frac12$ row 1 from row 2 leaves pivot $2-\frac12=\frac32$. In general, if pivot $i$ is $\frac{i+1}{i}$, the multiplier for the next row is $\ell_{i+1,i}=-\frac{i}{i+1}$ and the next pivot is $2-\frac{i}{i+1}=\frac{i+2}{i+1}$. So the pivots are
   $$2,\ \tfrac32,\ \tfrac43,\ \tfrac54,\ \tfrac65,\ \tfrac76,$$
   $U$ has these on the diagonal and $-1$ above it, and $L$ has $1$ on the diagonal and $-\frac12,-\frac23,-\frac34,-\frac45,-\frac56$ below it.

2. Computing $L^{-1}$ (by software or by Gauss–Jordan) shows the pattern
   $$(L^{-1})_{ij}=\frac ji\quad(j\le i),\qquad (L^{-1})_{ij}=0\quad(j>i).$$

3. Check: row $i$ of $L$ is $-\frac{i-1}{i}\mathbf{e}_{i-1}^{\mathsf T}+\mathbf{e}_i^{\mathsf T}$, so entry $(i,j)$ of $LL^{-1}$ for $j<i$ is $-\frac{i-1}i\cdot\frac j{i-1}+\frac ji=0$, and for $j=i$ it is $1$.
:::
