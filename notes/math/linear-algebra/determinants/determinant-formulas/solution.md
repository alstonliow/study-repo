<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-7-q1" status="draft"}
1. Expand along row 1. The $(1,1)$ entry is $1$ and its cofactor is the same kind of determinant of order $n-1$: $F_{n-1}$.

2. The $(1,2)$ entry is $-1$, with sign $(-1)^{1+2}=-1$, so it contributes $(-1)(-1)\det M_{12}=\det M_{12}$. The minor $M_{12}$ (delete row 1, column 2) has first column $(1,0,\dots,0)$; expanding down that column leaves the order-$(n-2)$ determinant $F_{n-2}$.

3. All other entries of row 1 are $0$. Hence $F_n=F_{n-1}+F_{n-2}$, and with $F_1=1$, $F_2=2$ we get $1,2,3,5,8,13,\dots$ In particular $F_4=5$.
:::

::: {.solution for="prob-mit1806s10-7-q2" status="draft"}
1. $F_{2n+2}=F_{2n+1}+F_{2n}$.

2. $F_{2n+1}=F_{2n}+F_{2n-1}$, so $F_{2n+2}=2F_{2n}+F_{2n-1}$.

3. $F_{2n-1}=F_{2n}-F_{2n-2}$ (Fibonacci's rule at $k=2n$), so $F_{2n+2}=3F_{2n}-F_{2n-2}$.

4. $S_1=3=F_4$ and $S_2=\det\begin{bmatrix}3&1\\1&3\end{bmatrix}=8=F_6$. Both sequences satisfy the same recursion, so $S_n=F_{2n+2}$ for all $n$ by induction.
:::

::: {.solution for="prob-mit1806s10-7-q3" status="draft"}
1. By linearity in the last row, subtracting $1$ from the $(n,n)$ entry subtracts $1\cdot C_{nn}$ from the determinant, where $C_{nn}=\det M_{nn}$ (sign $+$).

2. $M_{nn}$ is the symmetric Pascal matrix of order $n-1$, whose determinant is $1$.

3. So the new determinant is $1-1=0$.
:::

::: {.solution for="prob-mit1806s10-7-q6" status="draft"}
1. Group the terms of the big formula (@thm-big-formula-determinant) by the two columns $\{i,j\}$ ($i<j$) used by rows 1 and 2. The terms with these columns add up to $\det A_{12,ij}\cdot\det A_{345,\overline{ij}}$, where $A_{12,ij}$ is rows 1–2 and columns $i,j$, and $A_{345,\overline{ij}}$ is rows 3–5 and the other three columns, up to a sign. Moving columns $i,j$ to the front costs $(i-1)+(j-2)$ exchanges, so
   $$\det A=\sum_{i<j}(-1)^{i+j+1}\det A_{12,ij}\,\det A_{345,\overline{ij}}$$
   (ten terms; this is Laplace's expansion).

2. For the $-1,2,-1$ matrix, rows 1–2 are zero outside columns 1–3, and column 1 is zero in rows 3–5. So only $\{1,2\}$ and $\{1,3\}$ can contribute:
   $$\{1,2\}:\ (+1)\begin{vmatrix}2&-1\\-1&2\end{vmatrix}\begin{vmatrix}2&-1&0\\-1&2&-1\\0&-1&2\end{vmatrix}=3\cdot4=12,$$
   $$\{1,3\}:\ (-1)\begin{vmatrix}2&0\\-1&-1\end{vmatrix}\begin{vmatrix}-1&-1&0\\0&2&-1\\0&-1&2\end{vmatrix}=-(-2)(-3)=-6.$$

3. The sum is $12-6=6$, as it should be.
:::

::: {.solution for="prob-mit1806s10-7-q7" status="draft"}
(a) Sum over the three pairs of indices $i<j$: (determinant of columns $i,j$ of $A$) times (determinant of rows $i,j$ of $B$).

(b)

1. $AA^{\mathsf T}=\begin{bmatrix}14&30\\30&66\end{bmatrix}$, so $\det AA^{\mathsf T}=924-900=24$.

2. The $2\times2$ minors of $A$ from columns $\{1,2\},\{1,3\},\{2,3\}$ are $2,\ 4,\ 2$; those of $B=A^{\mathsf T}$ from the same rows are the same numbers.

3. The formula gives $2\cdot2+4\cdot4+2\cdot2=24$. It matches.
:::

::: {.solution for="prob-mit1806s10-7-q13" status="draft"}
(a) For $n=5,\dots,12$ the determinants are $2,-4,2,0,2,-4,2,0$: the pattern repeats with period $4$.

(b)

1. Write $A(n)=T+E$, where $T$ is the tridiagonal part (determinant $C_n$) and $E$ has $1$s only in the corners $(1,n)$ and $(n,1)$. Sort the terms of the big formula for $\det A(n)$ by which corner entries they use. (Expanding along row 1 and then down column 1 performs exactly this sorting.)

2. Terms using no corner: they are the terms of $\det T=C_n$.

3. Terms using both corners: the permutation swaps $1$ and $n$ and permutes the middle indices $2,\dots,n-1$ among the tridiagonal entries. The swap contributes a factor $-1$ to the sign, so these terms add to $-C_{n-2}$.

4. Terms using exactly one corner, say $(1,n)$: then row $n$ cannot use column $1$, so the only possibility is $n\to n-1\to\dots\to2\to1\to n$, a cycle through all $n$ positions, with sign $(-1)^{n-1}$ and all entries $1$. The other corner gives the reverse cycle, also $(-1)^{n-1}$.

5. Hence $\det A(n)=C_n-C_{n-2}+2(-1)^{n-1}=2C_n-2(-1)^n=2\big(C_n-(-1)^n\big)$, using $C_{n-2}=-C_n$.

6. Mod $4$: $n\equiv1,3$ give $2(0+1)=2$; $n\equiv2$ gives $C_n=-1$ and $2(-1-1)=-4$; $n\equiv0$ gives $C_n=1$ and $2(1-1)=0$. This is the pattern of part (a).
:::
