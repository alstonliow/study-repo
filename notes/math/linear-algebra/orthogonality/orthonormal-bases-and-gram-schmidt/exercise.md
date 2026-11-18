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

::: {.problem #prob-mit1802f07-1-q4 origin="external" source="mit1802f07-1-q4"}
Orthogonal matrices are matrices $A$ that satisfy the identity $AA^T=I$ ($I$ is the identity matrix). An equivalent definition of the orthogonal matrix property is that $A^TA=I$ because the left and right inverses of a square matrix are the same (see 1G-9b). The equation $AA^T=I$ says that the rows of $A$ are perpendicular to each other and of unit length, whereas the equation $A^TA=I$ says that the columns of $A$ are perpendicular to each other and of unit length. The geometric significance of orthogonal matrices is that multiplication by an orthogonal matrix preserves lengths of vectors and the absolute values of angles between them:
$$|A\mathbf{v}|=|\mathbf{v}|\ \text{ and }\ |\angle(A\mathbf{v},A\mathbf{w})|=|\angle(\mathbf{v},\mathbf{w})|.$$
There are two types of orthogonal matrices, rotations and reflections.

a) In 2-dimensional space, rotations are given by
$$A_\theta=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}$$
Find $\mathbf{u}=A_\theta\hat{\imath}$ and $\mathbf{v}=A_\theta\hat{\jmath}$, and draw a picture of $\mathbf{u}$ and $\mathbf{v}$ for $\theta=\pi/4$.

b) Use the addition formulas for sine and cosine to deduce that $A_{\theta_1}A_{\theta_2}=A_{\theta_1+\theta_2}$. Say in words what this matrix formula means about rotations.

c) Calculate $A_\theta^{-1}$, and use this to verify that $A_\theta A_\theta^T=I$ (in other words, rotations are orthogonal matrices). Also verify that $A_\theta^{-1}=A_{-\theta}$, and give a geometric reason why this property holds.

d) Find the four orthogonal $2\times2$ matrices with first entry $a_{11}=-1/\sqrt2$. Hint: try different signs. (See 1F-9 and 1F-10).

e) Next to each of the matrices in your list in part (d), draw what the matrix does to the letter F in the plane. Explain how the sign of the determinant of the matrix is related to the appearance of the transformed F.
:::

::: {.problem #prob-mit1802n-1f-q9 origin="external" source="mit1802n-1f-q9"}
A square $n\times n$ matrix is called **orthogonal** if $A\cdot A^T=I_n$. Show that this condition is equivalent to saying that

a) each row of $A$ is a row vector of length 1,

b) two different rows are orthogonal vectors.
:::
