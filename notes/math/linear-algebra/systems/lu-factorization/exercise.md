::: {.problem #prob-mit1806s10-2-q3 origin="external" source="mit1806s10-2-q3"}
Compute $L$ and $U$ for the symmetric matrix
$$A=\begin{bmatrix}a&a&a&a\\a&b&b&b\\a&b&c&c\\a&b&c&d\end{bmatrix}.$$
Find four conditions on $a,b,c,d$ to get $A=LU$ with four pivots.
:::

::: {.problem #prob-mit1806s10-2-q4 origin="external" source="mit1806s10-2-q4"}
If $A=LDU$ and also $A=L_1D_1U_1$ with all factors invertible, then $L=L_1$ and $D=D_1$ and $U=U_1$. "The three factors are unique."

Derive the equation $L_1^{-1}LD=D_1U_1U^{-1}$. Are the two sides triangular or diagonal? Deduce $L=L_1$ and $U=U_1$ (they all have diagonal 1's). Then $D=D_1$.
:::

::: {.problem #prob-mit1806s10-2-q5 origin="external" source="mit1806s10-2-q5"}
For the 6 by 6 second difference constant-diagonal matrix $K$, put the pivots and multipliers into $K=LU$. ($L$ and $U$ will have only two nonzero diagonals, because $K$ has three.) Find a formula for the $i,j$ entry of $L^{-1}$, by software like MATLAB using inv(L) or by looking for a nice pattern.
$$-1,2,-1\text{ matrix }K=\begin{bmatrix}2&-1&&&&\\-1&\bullet&\bullet&&&\\&\bullet&\bullet&\bullet&&\\&&\bullet&\bullet&\bullet&\\&&&\bullet&\bullet&-1\\&&&&-1&2\end{bmatrix}=\texttt{toeplitz([2 -1 0 0 0 0])}.$$
:::
