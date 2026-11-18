::: {.problem #prob-mit1806s10-2-q9 origin="external" source="mit1806s10-2-q9"}
Suppose $Q^{\mathsf T}$ equals $Q^{-1}$ (transpose equal inverse, so $Q^{\mathsf T}Q=I$).

(a) Show that the columns $\mathbf{q}_1,\dots,\mathbf{q}_n$ are unit vectors: $\lVert\mathbf{q}_i\rVert^2=1$.

(b) Show that every two distinct columns of $Q$ are perpendicular: $\mathbf{q}_i^{\mathsf T}\mathbf{q}_j=0$ for $i\neq j$.

(c) Find a 2 by 2 example with first entry $q_{11}=\cos\theta$.
:::

::: {.problem #prob-mit1806s10-6-q6 origin="external" source="mit1806s10-6-q6"}
Orthonormal vectors are automatically linearly independent.

(a) Vector proof: When $c_1\mathbf{q}_1+c_2\mathbf{q}_2+c_3\mathbf{q}_3=\mathbf{0}$, what dot product leads to $c_1=0$? Similarly $c_2=0$ and $c_3=0$. Thus, the $\mathbf{q}$'s are independent.

(b) Matrix proof: Show that $Q\mathbf{x}=\mathbf{0}$ leads to $\mathbf{x}=\mathbf{0}$. Since $Q$ may be rectangular, you can use $Q^{\mathsf T}$ but not $Q^{-1}$.
:::

::: {.problem #prob-mit1806s10-6-q7 origin="external" source="mit1806s10-6-q7"}
Find the orthonormal vectors $A,B,C$ by Gram-Schmidt from $\mathbf{a},\mathbf{b},\mathbf{c}$:
$$\mathbf{a}=(1,-1,0,0)\quad\mathbf{b}=(0,1,-1,0)\quad\mathbf{c}=(0,0,1,-1).$$
Show $\{A,B,C\}$ and $\{\mathbf{a},\mathbf{b},\mathbf{c}\}$ are bases for the space of vectors perpendicular to $\mathbf{d}=(1,1,1,1)$.
:::

::: {.problem #prob-mit1806s10-6-q8 origin="external" source="mit1806s10-6-q8"}
Factor $[Q,R]=\texttt{qr}(A)$ for $A=\texttt{eye(4)}-\texttt{diag([1 1 1],}-1\texttt{)}$. You are orthogonalizing the columns $(1,-1,0,0)$, $(0,1,-1,0)$, $(0,0,1,-1)$, and $(0,0,0,1)$ of $A$. Can you scale the orthogonal columns of $Q$ to get nice integer components?
:::

::: {.problem #prob-mit1806s10-6-q9 origin="external" source="mit1806s10-6-q9"}
If $A$ is $m$ by $n$, qr(A) produces a square $A$ and zeroes below $R$: The factors from MATLAB are ($m$ by $m$)($m$ by $n$)
$$A=\begin{bmatrix}Q_1&Q_2\end{bmatrix}\begin{bmatrix}R\\0\end{bmatrix}.$$
The $n$ columns of $Q_1$ are an orthonormal basis for which fundamental subspace? The $m-n$ columns of $Q_2$ are an orthonormal basis for which fundamental subspace?

*Note (these notes):* Here $A$ is assumed to have independent columns.
:::
