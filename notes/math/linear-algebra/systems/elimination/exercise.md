::: {.problem #prob-mit1806s10-1-q7 origin="external" source="mit1806s10-1-q7"}
Three planes can fail to have an intersection point, even if no planes are parallel. The system is singular if row 3 of $A$ is a \_\_\_\_\_ of the first two rows. Find a third equation that can't be solved together with $x+y+z=0$ and $x-2y-z=1$.
:::

::: {.problem #prob-mit1806s10-1-q8 origin="external" source="mit1806s10-1-q8"}
Start with 100 equations $A\mathbf{x}=\mathbf{0}$ for 100 unknowns $\mathbf{x}=(x_1,\dots,x_{100})$. Suppose elimination reduces the 100th equation to $0=0$, so the system is "singular".

(a) Elimination takes linear combinations of the rows. So this singular system has the singular property: Some linear combination of the 100 rows is \_\_\_\_\_.

(b) Singular systems $A\mathbf{x}=\mathbf{0}$ have infinitely many solutions. This means that some linear combination of the 100 columns is \_\_\_\_\_.

(c) Invent a 100 by 100 singular matrix with no zero entries.

(d) For your matrix, describe in words the row picture and the column picture of $A\mathbf{x}=\mathbf{0}$. Not necessary to draw 100-dimensional space.
:::

::: {.problem #prob-mit1806s10-1-q9 origin="external" source="mit1806s10-1-q9"}
The entries of $A$ and $\mathbf{x}$ are $a_{ij}$ and $x_j$. So the first component of $A\mathbf{x}$ is $\sum a_{1j}x_j=a_{11}x_1+\dots+a_{1n}x_n$. If $E_{21}$ subtracts row 1 from row 2, write a formula for

(a) the third component of $A\mathbf{x}$

(b) the $(2,1)$ entry of $E_{21}A$

(c) the $(2,1)$ entry of $E_{21}(E_{21}A)$

(d) the first component of $E_{21}A\mathbf{x}$.
:::

::: {.problem #prob-mit1806s10-1-q10 origin="external" source="mit1806s10-1-q10"}
Find the triangular matrix $E$ that reduces "Pascal's matrix" to a smaller Pascal:
$$E\begin{bmatrix}1&0&0&0\\1&1&0&0\\1&2&1&0\\1&3&3&1\end{bmatrix}=\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&1&1&0\\0&1&2&1\end{bmatrix}.$$
Which matrix $M$ (multiplying several $E$'s) reduces Pascal all the way to $I$?
:::
