::: {.problem #prob-mit1806s10-1-q13 origin="external" source="mit1806s10-1-q13"}
If $A$ has row 1 + row 2 = row 3, show that $A$ is not invertible:

(a) Explain why $A\mathbf{x}=(1,0,0)$ cannot have a solution.

(b) Which right sides $(b_1,b_2,b_3)$ might allow a solution to $A\mathbf{x}=\mathbf{b}$?

(c) What happens to row 3 in elimination?
:::

::: {.problem #prob-mit1806s10-2-q1 origin="external" source="mit1806s10-2-q1"}
Use Gauss-Jordan elimination on $[U\ I]$ to find the upper triangular $U^{-1}$:
$$UU^{-1}=I\qquad\begin{bmatrix}1&a&b\\0&1&c\\0&0&1\end{bmatrix}\begin{bmatrix}\mathbf{x}_1&\mathbf{x}_2&\mathbf{x}_3\end{bmatrix}=\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}.$$
:::

::: {.problem #prob-mit1806s10-2-q2 origin="external" source="mit1806s10-2-q2"}
$A$ is a 4 by 4 matrix with 1's on the diagonal and $-a,-b,-c$ on the diagonal above. Find $A^{-1}$ for this bidiagonal matrix.
:::

::: {.problem #prob-mit1806s10-2-q6 origin="external" source="mit1806s10-2-q6"}
If you print $K^{-1}$, it doesn't look good. But if you print $7K^{-1}$ (when $K$ is 6 by 6), that matrix looks wonderful. Write down $7K^{-1}$ by hand, following this pattern:

1. Row 1 and column 1 are $(6,5,4,3,2,1)$.
2. On and above the main diagonal, row $i$ is $i$ times row 1.
3. On and below the main diagonal, column $j$ is $j$ times column 1.

Multiply $K$ times that $7K^{-1}$ to produce $7I$. Here is that pattern for $n=3$:
$$\text{3 by 3 case}\quad\text{The determinant of this }K\text{ is }4\qquad (K)(4K^{-1})=\begin{bmatrix}2&-1&0\\-1&2&-1\\0&-1&2\end{bmatrix}\begin{bmatrix}3&2&1\\2&4&2\\1&2&3\end{bmatrix}=\begin{bmatrix}4&&\\&4&\\&&4\end{bmatrix}.$$

*Note (these notes):* $K$ is the 6 by 6 matrix of @prob-mit1806s10-2-q5.
:::
