::: {.problem #prob-mit1806s10-1-q11 origin="external" source="mit1806s10-1-q11"}
Suppose you solve $A\mathbf{x}=\mathbf{b}$ for three special right sides $\mathbf{b}$:
$$A\mathbf{x}_1=\begin{bmatrix}1\\0\\0\end{bmatrix};\quad A\mathbf{x}_2=\begin{bmatrix}0\\1\\0\end{bmatrix};\quad A\mathbf{x}_3=\begin{bmatrix}0\\0\\1\end{bmatrix}.$$
If the three solutions $\mathbf{x}_1,\mathbf{x}_2,\mathbf{x}_3$ are the columns of a matrix $X$, what is $A$ times $X$?
:::

::: {.problem #prob-mit1806s10-1-q12 origin="external" source="mit1806s10-1-q12"}
Suppose $A$ is $m$ by $n$, $B$ is $n$ by $p$, and $C$ is $p$ by $q$. Then the multiplication count for $(AB)C$ is $mnp+mpq$. The multiplication count from $A$ times $BC$ with $mnq+npq$ separate multiplications.

(a) If $A$ is 2 by 4, $B$ is 4 by 7, and $C$ is 7 by 10, do you prefer $(AB)C$ or $A(BC)$?

(b) With $N$-component vectors, would you choose $(\mathbf{u}^{\mathsf T}\mathbf{v})\mathbf{w}^{\mathsf T}$ or $\mathbf{u}^{\mathsf T}(\mathbf{v}\mathbf{w}^{\mathsf T})$?

(c) Divide by $mnpq$ to show that $(AB)C$ is faster when $n^{-1}+q^{-1}<m^{-1}+p^{-1}$.
:::
