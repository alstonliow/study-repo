<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-5-q1" status="draft"}
1. The left sides satisfy $(x_1-x_2)+(x_2-x_3)-(x_1-x_3)=0$. So take $(y_1,y_2,y_3)=(1,1,-1)$.

2. The right sides then add to $1+1-1=1$, giving $0=1$. Hence the system has no solution: $\mathbf{y}=(1,1,-1)$ is in $N(A^{\mathsf T})$ but $\mathbf{y}^{\mathsf T}\mathbf{b}=1\ne0$, so $\mathbf{b}\notin C(A)=N(A^{\mathsf T})^{\perp}$ (@thm-fundamental-theorem-orthogonality).
:::

::: {.solution for="prob-mit1806s10-5-q2" status="draft"}
$A\mathbf{x}$ is in the *column space* of $A$, and the column space and $N(A^{\mathsf T})$ are *orthogonal* (orthogonal complements). A vector in both is orthogonal to itself, so $A\mathbf{x}=\mathbf{0}$. (Compare the length argument in @thm-ata-invertible.)
:::

::: {.solution for="prob-mit1806s10-5-q3" status="draft"}
1. The columns of $N$ are a basis of $N(A)$. A vector $\mathbf{z}$ is in the nullspace of $N^{\mathsf T}$ exactly when it is orthogonal to every column of $N$, i.e. to all of $N(A)$.

2. $N(A)^{\perp}$ is the *row space* $C(A^{\mathsf T})$ (@thm-fundamental-theorem-orthogonality). So B=null(N') gives a basis of the row space.

3. A numerical check: for a random $6\times12$ matrix $A$, the rows of $B^{\mathsf T}$ and the rows of $A$ have the same reduced row echelon form (up to rounding), so they span the same space.
:::

::: {.solution for="prob-mit1806s10-5-q4" status="draft"}
a. Each subspace is then a line, so $r=1$. The only conditions are the orthogonality ones: $\mathbf{r}\cdot\mathbf{n}=0$ and $\mathbf{c}\cdot\mathbf{l}=0$. The dimension counts $1+1=2$ hold automatically.

b. $A=\mathbf{c}\mathbf{r}^{\mathsf T}$. Every column is a multiple of $\mathbf{c}$ and every row a multiple of $\mathbf{r}^{\mathsf T}$, so $C(A)$ and $C(A^{\mathsf T})$ are right; the nullspaces are their orthogonal complements, the lines through $\mathbf{n}$ and $\mathbf{l}$.
:::

::: {.solution for="prob-mit1806s10-5-q5" status="draft"}
a.

1. Two vectors as a basis means two independent vectors: each pair would have to span a 2-dimensional subspace of $\mathbb{R}^2$. Then $\dim C(A^{\mathsf T})+\dim N(A)=2+2=4>2$, which contradicts @thm-fundamental-theorem-dimensions.

2. So, read literally, no $2\times2$ matrix works. The problem makes sense for an $n\times n$ matrix with $n=4$ and the vectors in $\mathbb{R}^4$: then the conditions are that each pair is independent, and $\mathbf{r}_i\cdot\mathbf{n}_j=0$, $\mathbf{c}_i\cdot\mathbf{l}_j=0$ for all $i,j$ (orthogonality need only be checked on bases).

b. In that reading, $A=\begin{bmatrix}\mathbf{c}_1&\mathbf{c}_2\end{bmatrix}\begin{bmatrix}\mathbf{r}_1&\mathbf{r}_2\end{bmatrix}^{\mathsf T}$ works: its columns are combinations of $\mathbf{c}_1,\mathbf{c}_2$, and it has rank $2$ because the left factor has independent columns and the right factor independent rows (see Problem 34 of this set, in this note). So $C(A)$ and $C(A^{\mathsf T})$ are as required, and the nullspaces are their orthogonal complements.
:::

::: {.solution for="prob-mit1806s10-5-q11" status="draft"}
1. $B^{\mathsf T}$ has independent columns, so $(B^{\mathsf T})^{\mathsf T}B^{\mathsf T}=BB^{\mathsf T}$ is invertible (@thm-ata-invertible).

2. The $r\times r$ matrix $A^{\mathsf T}(AB)B^{\mathsf T}=(A^{\mathsf T}A)(BB^{\mathsf T})$ is a product of invertible matrices, so it has rank $r$.

3. Multiplying by a matrix cannot raise the rank (@prob-mit1806s10-3-q9 and its transpose), so $\operatorname{rank}(AB)\ge r$. And $AB$ is $m\times n$ with $C(AB)\subseteq C(A)$ of dimension $r$, so $\operatorname{rank}(AB)=r$.
:::
