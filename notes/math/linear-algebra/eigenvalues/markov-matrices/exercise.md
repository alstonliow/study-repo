::: {.problem #prob-mit1806s10-1-q6 origin="external" source="mit1806s10-1-q6"}
Continue Problem 29 from $\mathbf{u}_0=(1,0)$ to $\mathbf{u}_7$, and also from $\mathbf{v}_0=(0,1)$ to $\mathbf{v}_7$. What do you notice about $\mathbf{u}_7$ and $\mathbf{v}_7$? Here are two MATLAB codes, with while and for. They plot $\mathbf{u}_0$ to $\mathbf{u}_7$ and $\mathbf{v}_0$ to $\mathbf{v}_7$.

The $\mathbf{u}$'s and the $\mathbf{v}$'s are approaching a steady state vector $\mathbf{s}$. Guess that vector and check that $A\mathbf{s}=\mathbf{s}$. If you start with $\mathbf{s}$, then you stay with $\mathbf{s}$.

*Note (these notes):* Problem 29 is @prob-mit1806s10-1-q5, with $A=\begin{bmatrix}.8&.3\\.2&.7\end{bmatrix}$. The MATLAB codes of the book are not reproduced.
:::

::: {.problem #prob-mit1806s10-7-q11 origin="external" source="mit1806s10-7-q11"}
Find $\Lambda$ and $S$ to diagonalize $A_1$ in Problem 15:
$$A_1=\begin{bmatrix}.6&.9\\.4&.1\end{bmatrix}.$$
What is the limit of $\Lambda^k$ as $k\to\infty$? What is the limit of $S\Lambda^kS^{-1}$? In the columns of the matrix you see the \_\_\_\_\_.
:::

::: {.problem #prob-mit1806s10-8-q11 origin="external" source="mit1806s10-8-q11"}
Prove that the square of a Markov matrix is also a Markov matrix.
:::

::: {.problem #prob-mit1806s10-8-q12 origin="external" source="mit1806s10-8-q12"}
A Markov differential equation is not $d\mathbf{u}/dt=A\mathbf{u}$ but $d\mathbf{u}/dt=(A-I)\mathbf{u}$. The diagonal is negative, the rest of $A-I$is positive. The coulmns add to zero.

Find the eigenvalues of $B=A-I=\begin{bmatrix}-.2&.3\\.2&-.3\end{bmatrix}$. Why does $A-I$ have $\lambda=0$?

When $e^{\lambda_1t}$ and $e^{\lambda_2t}$ multiply $\mathbf{x}_1$ and $\mathbf{x}_2$, what is the steady state as $t\to\infty$?
:::

::: {.problem #prob-mit1806s10-8-q13 origin="external" source="mit1806s10-8-q13"}
(Markov again) This matrix has zero determinant. What are its eigenvalues?
$$A=\begin{bmatrix}.4&.2&.3\\.2&.4&.3\\.4&.4&.4\end{bmatrix}.$$
Find the limits of $A^k\mathbf{u}_0$ starting from $\mathbf{u}_0=(1,0,0)$ and then $\mathbf{u}_0=(100,0,0)$.
:::
