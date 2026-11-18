<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-1-q7" status="draft"}
1. The blank is *linear combination*: then elimination turns row 3 into a zero row.

2. Take any combination of the two left sides and a right side that does not match. For instance $2\cdot(x+y+z)+1\cdot(x-2y-z)=3x+z$, which would have to equal $2\cdot0+1\cdot1=1$. So the equation
   $$3x+z=2$$
   cannot hold together with the first two: they force $3x+z=1$.
:::

::: {.solution for="prob-mit1806s10-1-q8" status="draft"}
(a) The zero row: row 100 after elimination is a combination of the original rows, and it is zero.

(b) The zero vector: a nonzero solution $\mathbf{x}$ gives $x_1(\text{col }1)+\dots+x_{100}(\text{col }100)=\mathbf{0}$.

(c) For example the matrix whose every row is $(1,2,3,\dots,100)$. It has rank $1$.

(d) Row picture: all 100 equations are the same, $x_1+2x_2+\dots+100x_{100}=0$, so the 100 hyperplanes coincide, and the solutions fill that whole 99-dimensional hyperplane. Column picture: column $j$ is $j(1,1,\dots,1)$, so all columns lie on one line, and the solutions are the combinations of 100 vectors along that line that cancel.
:::

::: {.solution for="prob-mit1806s10-1-q9" status="draft"}
(a) $\sum_ja_{3j}x_j$.

(b) Row 2 of $E_{21}A$ is row 2 minus row 1 of $A$, so the entry is $a_{21}-a_{11}$.

(c) Applying $E_{21}$ again subtracts row 1 a second time: $a_{21}-2a_{11}$.

(d) $E_{21}$ does not change row 1, so the first component is still $\sum_ja_{1j}x_j$.
:::

::: {.solution for="prob-mit1806s10-1-q10" status="draft"}
1. Each row of the right side is the corresponding row of Pascal minus the row above it (for example $(1,3,3,1)-(1,2,1,0)=(0,1,2,1)$). So
   $$E=\begin{bmatrix}1&0&0&0\\-1&1&0&0\\0&-1&1&0\\0&0&-1&1\end{bmatrix}.$$

2. The same idea on the smaller Pascal in rows 2–4 uses $E_2$, which subtracts row 2 from row 3 and row 3 from row 4; then $E_3$ subtracts row 3 from row 4:
   $$E_2=\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&-1&1&0\\0&0&-1&1\end{bmatrix},\qquad E_3=\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&-1&1\end{bmatrix}.$$

3. Then $M=E_3E_2E$ reduces Pascal to $I$, so $M$ is the inverse of Pascal's matrix:
   $$M=\begin{bmatrix}1&0&0&0\\-1&1&0&0\\1&-2&1&0\\-1&3&-3&1\end{bmatrix},$$
   the binomial coefficients with alternating signs.
:::
