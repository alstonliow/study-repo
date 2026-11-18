::: {.problem #prob-mit1806s10-3-q6 origin="external" source="mit1806s10-3-q6"}
Neat fact Every $m$ by $n$ matrix of rank $r$ reduces to ($m$ by $r$) times ($r$ by $n$):
$$A=(\text{pivot columns of }A)\,(\text{first }r\text{ rows of }R)=(\text{COL})\,(\text{ROW}).$$
Write the 3 by 4 matrix $A$ in equation (1) at the start of this section as the product of the 3 by 2 matrix from the pivot columns and the 2 by 4 matrix from $R$.

*Note (these notes):* The matrix of equation (1) is $A=\begin{bmatrix}1&1&2&4\\1&2&2&5\\1&3&2&6\end{bmatrix}$.
:::

::: {.problem #prob-mit1806s10-4-q3 origin="external" source="mit1806s10-4-q3"}
If $AS=SA$ for the shift matrix $S$, show that $A$ must have this special form:
$$\text{If}\quad\begin{bmatrix}a&b&c\\d&e&f\\g&h&i\end{bmatrix}\begin{bmatrix}0&1&0\\0&0&1\\0&0&0\end{bmatrix}=\begin{bmatrix}0&1&0\\0&0&1\\0&0&0\end{bmatrix}\begin{bmatrix}a&b&c\\d&e&f\\g&h&i\end{bmatrix},\quad\text{then}\quad A=\begin{bmatrix}a&b&c\\0&a&b\\0&0&a\end{bmatrix}.$$
"The subspace of matrices that commute with the shift $S$ has dimension \_\_\_\_\_."
:::

::: {.problem #prob-mit1806s10-4-q4 origin="external" source="mit1806s10-4-q4"}
Write a 3 by 3 identity matrix as a combination of the other five permutation matrices. Then show that those five matrices are linearly indpendent. (Assume a combination gives $c_1P_1+\dots+c_5P_5=0$, and check entries to prove $c_i$ is zero.) The five permutation matrices are a basis for the subspace of 3 by 3 matrices with row and column sums all equal.
:::

::: {.problem #prob-mit1806s10-4-q10 origin="external" source="mit1806s10-4-q10"}
$\mathbf{M}$ is the space of 3 by 3 matrices. Multiply each matrix $X$ in $\mathbf{M}$ by
$$A=\begin{bmatrix}1&0&-1\\-1&1&0\\0&-1&1\end{bmatrix}.\qquad\text{Notice: }A\begin{bmatrix}1\\1\\1\end{bmatrix}=\begin{bmatrix}0\\0\\0\end{bmatrix}.$$

(a) Which matrices $X$ lead to $AX=0$?

(b) Which matrices have the form $AX$ for some matrix $X$?

(a) finds the "nullspace" of that operation $AX$ and (b) finds the "column space". What are the dimensions of those two subspaces of $\mathbf{M}$? Why do the dimensions add to $(n-r)+r=9$?
:::
