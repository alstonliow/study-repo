::: {.problem #prob-mit1806s10-3-q2 origin="external" source="mit1806s10-3-q2"}
(If possible. . . ) Construct a matrix whose column space contains $(1,1,0)$ and $(0,1,1)$ and whose nullspace contains $(1,0,1)$ and $(0,0,1)$.
:::

::: {.problem #prob-mit1806s10-3-q5 origin="external" source="mit1806s10-3-q5"}
Suppose $A$ and $B$ are $n$ by $n$ matrices, and $AB=I$. Prove from $\operatorname{rank}(AB)\le\operatorname{rank}(A)$ that the rank of $A$ is $n$. So $A$ is invertible and $B$ must be its two-sided inverse (Section 2.5). Therefore $BA=I$ (which is not so obvious!).
:::

::: {.problem #prob-mit1806s10-3-q9 origin="external" source="mit1806s10-3-q9"}
(a) Suppose column $j$ of $B$ is a combination of previous columns of $B$. Show that column $j$ of $AB$ is the same combination of previous columnd of $AB$. Then $AB$ cannot have new pivot columns, so $\operatorname{rank}(AB)\le\operatorname{rank}(B)$.

(b) Find $A_1$ and $A_2$ so that $\operatorname{rank}(A_1B)=1$ and $\operatorname{rank}(A_2B)=0$ for $B=\begin{bmatrix}1&1\\1&1\end{bmatrix}$.
:::

::: {.problem #prob-mit1806s10-4-q5 origin="external" source="mit1806s10-4-q5"}
(An aside in the text, followed by) dimension of outputs + dimension of nullspace = dimension of inputs. For an $m$ by $n$ matrix of rank $r$, what are those 3 dimensions? Outputs = column space. This question wil be answered in Section 3.6, can you do it now?
:::

::: {.problem #prob-mit1806s10-4-q6 origin="external" source="mit1806s10-4-q6"}
$A$ is an $m$ by $n$ matrix of rank $r$. Suppose there are right sides $\mathbf{b}$ for which $A\mathbf{x}=\mathbf{b}$ has no solution.

(a) What are all the inequalities ($<$ or $\le$) that must be true between $m$, $n$, and $r$?

(b) How do you know that $A^{\mathsf T}\mathbf{y}=\mathbf{0}$ has solutions other than $\mathbf{y}=\mathbf{0}$?
:::

::: {.problem #prob-mit1806s10-4-q7 origin="external" source="mit1806s10-4-q7"}
$A^{\mathsf T}\mathbf{y}=\mathbf{d}$ is solvable when $\mathbf{d}$ is in which of the four subspaces? The solution is unique when the \_\_\_\_\_ contains only the zero vector.
:::

::: {.problem #prob-mit1806s10-4-q8 origin="external" source="mit1806s10-4-q8"}
Find the ranks of the 8 by 8 checkerboard matrix $B$ and the chess matrix $C$:
$$B=\begin{bmatrix}1&0&1&0&1&0&1&0\\0&1&0&1&0&1&0&1\\1&0&1&0&1&0&1&0\\0&1&0&1&0&1&0&1\\1&0&1&0&1&0&1&0\\0&1&0&1&0&1&0&1\\1&0&1&0&1&0&1&0\\0&1&0&1&0&1&0&1\end{bmatrix}\quad\text{and}\quad C=\begin{bmatrix}r&n&b&q&k&b&n&r\\p&p&p&p&p&p&p&p\\0&0&0&0&0&0&0&0\\0&0&0&0&0&0&0&0\\0&0&0&0&0&0&0&0\\0&0&0&0&0&0&0&0\\p&p&p&p&p&p&p&p\\r&n&b&q&k&b&n&r\end{bmatrix}$$
The numbers $r,n,b,k,q,p$ are all different. Find bases for the rowspace and left nullspace of $B$ and $C$. Challenge problem: Find a basis for the nullspace of $C$.
:::

::: {.problem #prob-mit1806s10-4-q9 origin="external" source="mit1806s10-4-q9"}
If $A=\mathbf{u}\mathbf{v}^{\mathsf T}$ is a 2 by 2 matrix of rank 1, redraw Figure 3.5 to show clearly the Four Fundamental Subspaces. If $B$ produces those same four subspaces, what is the exact relation of $B$ to $A$?

*Note (these notes):* Figure 3.5 of the book is @fig-four-fundamental-subspaces-1.
:::
