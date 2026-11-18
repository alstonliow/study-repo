::: {.problem #prob-mit1806s10-6-q10 origin="external" source="mit1806s10-6-q10"}
If the entries in every row of $A$ add to zero, solve $A\mathbf{x}=\mathbf{0}$ to prove $\det A=0$. If those entries add to one, show that $\det(A-I)=0$. Does this mean $\det A=I$?
:::

::: {.problem #prob-mit1806s10-6-q11 origin="external" source="mit1806s10-6-q11"}
Use row operations to show that the 3 by 3 "Vandermonde determinant" is
$$\det\begin{bmatrix}1&a&a^2\\1&b&b^2\\1&c&c^2\end{bmatrix}=(b-a)(c-a)(c-b).$$
:::

::: {.problem #prob-mit1806s10-6-q12 origin="external" source="mit1806s10-6-q12"}
(MATLAB) The Hilbert matrix hilb(n) has $i,j$ entry equal to $1/(i+j-1)$. Print the determinants of hilb(1), hilb(2), ..., hilb(10). Hilbert matrices are hard to work with! What are the pivots of hilb(5)?
:::

::: {.problem #prob-mit1806s10-6-q13 origin="external" source="mit1806s10-6-q13"}
(MATLAB) What is the typical determinant (experimentally) of rand(n) and randn(n) for $n=50,100,200,400$? (And what does "Inf" mean in MATLAB?)
:::
