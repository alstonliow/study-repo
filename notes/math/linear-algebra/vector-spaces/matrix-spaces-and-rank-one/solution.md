<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-3-q6" status="draft"}
1. Eliminate: subtract row 1 from rows 2 and 3, then twice row 2 from row 3, then row 2 from row 1:
   $$R=\begin{bmatrix}1&0&2&3\\0&1&0&1\\0&0&0&0\end{bmatrix}.$$
   The pivot columns are $1$ and $2$, so $r=2$.

2. Hence
   $$A=\begin{bmatrix}1&1\\1&2\\1&3\end{bmatrix}\begin{bmatrix}1&0&2&3\\0&1&0&1\end{bmatrix}.$$
   Check column 3: $2\cdot(1,1,1)+0\cdot(1,2,3)=(2,2,2)$; column 4: $3(1,1,1)+(1,2,3)=(4,5,6)$.
:::

::: {.solution for="prob-mit1806s10-4-q3" status="draft"}
1. $AS$ shifts the columns of $A$ one place to the right (with a zero first column); $SA$ shifts the rows of $A$ one place up (with a zero last row):
   $$AS=\begin{bmatrix}0&a&b\\0&d&e\\0&g&h\end{bmatrix},\qquad SA=\begin{bmatrix}d&e&f\\g&h&i\\0&0&0\end{bmatrix}.$$

2. Equating entries: $d=0$, $g=0$, $h=0$ (from the first column and the last row), then $a=e$, $b=f$, $d=h$, $e=i$. So $e=i=a$, $f=b$ and $d=g=h=0$, which is the stated form.

3. The free parameters are $a,b,c$, and the matrices $I$, $S$, $S^2$ form a basis. The dimension is $3$.
:::

::: {.solution for="prob-mit1806s10-4-q4" status="draft"}
1. Name the five: the exchanges $P_{12},P_{13},P_{23}$ and the two cyclic shifts $C_1=\begin{bmatrix}0&1&0\\0&0&1\\1&0&0\end{bmatrix}$, $C_2=C_1^{\mathsf T}$ (@exm-three-by-three-permutation-matrices).

2. $P_{12}+P_{13}+P_{23}$ has a single $1$ in every position: each exchange keeps one diagonal entry and puts $1$s in two off-diagonal positions, and together they cover every position exactly once. So it is the all-ones matrix $J$. Also $C_1+C_2$ is $J-I$. Hence
   $$I=P_{12}+P_{13}+P_{23}-C_1-C_2.$$

3. Independence: write $c_1P_{12}+c_2P_{13}+c_3P_{23}+c_4C_1+c_5C_2=0$. The diagonal entries $(1,1),(2,2),(3,3)$ are touched only by $P_{23},P_{13},P_{12}$ respectively, so $c_3=c_2=c_1=0$. Then entry $(1,2)$ gives $c_4=0$ and entry $(2,1)$ gives $c_5=0$.
:::

::: {.solution for="prob-mit1806s10-4-q10" status="draft"}
1. $A$ has rank $2$: its rows add to zero, and the first two rows are independent. So $N(A)$ is the line through $(1,1,1)$, and $C(A)$ is the plane of vectors whose components add to $0$ (orthogonal to $N(A^{\mathsf T})$, which is also the line through $(1,1,1)$ since the columns add to zero too).

2. (a) $AX=0$ means every column of $X$ is in $N(A)$: $X=\begin{bmatrix}a&b&c\\a&b&c\\a&b&c\end{bmatrix}$. Dimension $3$.

3. (b) Every column of $AX$ is in $C(A)$, and any three vectors of $C(A)$ can be produced. So the outputs are the matrices whose columns each add to $0$. Dimension $3\times2=6$.

4. The map $X\mapsto AX$ is linear on the $9$-dimensional space $\mathbf{M}$; just as for a matrix, (dimension of nullspace) + (dimension of outputs) = (dimension of inputs): $3+6=9$.
:::

::: {.solution for="prob-mit18065ps-1-q18" status="draft"}
1. The pivot columns of $\begin{bmatrix}0&A\\0&A\end{bmatrix}$ are the pivot columns of $A$ stacked twice, so the column factor is $\begin{bmatrix}C\\C\end{bmatrix}$.

2. The row factor is $\begin{bmatrix}0&R\end{bmatrix}$ (zero columns in front, one per column of the zero block).

3. Check by block multiplication: $\begin{bmatrix}C\\C\end{bmatrix}\begin{bmatrix}0&R\end{bmatrix}=\begin{bmatrix}0&CR\\0&CR\end{bmatrix}=\begin{bmatrix}0&A\\0&A\end{bmatrix}$. The columns of $\begin{bmatrix}C\\C\end{bmatrix}$ are independent because those of $C$ are, and the rows of $\begin{bmatrix}0&R\end{bmatrix}$ are independent because those of $R$ are, so the rank is still $r$.
:::
