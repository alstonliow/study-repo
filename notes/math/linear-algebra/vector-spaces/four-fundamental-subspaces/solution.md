<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-3-q2" status="draft"}
1. Not possible. The column space lies in $\mathbb{R}^3$ and the nullspace in $\mathbb{R}^3$, so $A$ is $3\times3$.

2. The column space contains two independent vectors, so $r=\dim C(A)\ge2$.

3. The nullspace contains two independent vectors, so $3-r=\dim N(A)\ge2$, i.e. $r\le1$ (@thm-fundamental-theorem-dimensions). The two requirements contradict each other.
:::

::: {.solution for="prob-mit1806s10-3-q5" status="draft"}
1. $n=\operatorname{rank}I=\operatorname{rank}(AB)\le\operatorname{rank}A\le n$, so $\operatorname{rank}A=n$.

2. A square matrix of full rank is invertible (@thm-rank-and-solutions). Multiplying $AB=I$ on the left by $A^{-1}$ gives $B=A^{-1}$, and then $BA=A^{-1}A=I$.

3. The inequality itself: every column of $AB$ is a combination of the columns of $A$, so $C(AB)\subseteq C(A)$ and $\dim C(AB)\le\dim C(A)$.
:::

::: {.solution for="prob-mit1806s10-3-q9" status="draft"}
(a)

1. Let $\mathbf{b}_k$ be the columns of $B$ and suppose $\mathbf{b}_j=\sum_{k<j}c_k\mathbf{b}_k$.

2. Column $j$ of $AB$ is $A\mathbf{b}_j=\sum_{k<j}c_kA\mathbf{b}_k$, the same combination of the earlier columns $A\mathbf{b}_k$ of $AB$.

3. A pivot column is one that is not a combination of the earlier columns. By step 2, every non-pivot column of $B$ gives a non-pivot column of $AB$; so $AB$ has at most as many pivot columns as $B$: $\operatorname{rank}(AB)\le\operatorname{rank}(B)$.

(b) $A_1=I$ gives $A_1B=B$ of rank $1$. $A_2=\begin{bmatrix}1&-1\\1&-1\end{bmatrix}$ gives $A_2B=0$, of rank $0$ (so does $A_2=0$).
:::

::: {.solution for="prob-mit1806s10-4-q5" status="draft"}
Inputs are vectors in $\mathbb{R}^n$: dimension $n$. Outputs $A\mathbf{x}$ fill the column space: dimension $r$. The nullspace has dimension $n-r$ (one special solution per free variable, @thm-special-solutions). Indeed $r+(n-r)=n$.
:::

::: {.solution for="prob-mit1806s10-4-q6" status="draft"}
(a) Always $r\le m$ and $r\le n$. Since $C(A)\neq\mathbb{R}^m$, $r=\dim C(A)<m$.

(b) $\dim N(A^{\mathsf T})=m-r>0$ (@thm-fundamental-theorem-dimensions), so the left nullspace contains nonzero vectors.
:::

::: {.solution for="prob-mit1806s10-4-q7" status="draft"}
$A^{\mathsf T}\mathbf{y}$ ranges over the column space of $A^{\mathsf T}$, which is the row space $C(A^{\mathsf T})$ (@thm-column-space-solvability for $A^{\mathsf T}$). So it is solvable exactly when $\mathbf{d}$ is in the row space. Two solutions differ by a vector of $N(A^{\mathsf T})$, so the solution is unique when the *left nullspace* contains only $\mathbf{0}$.
:::

::: {.solution for="prob-mit1806s10-4-q8" status="draft"}
**Checkerboard $B$.**

1. Rows $3,5,7$ equal row 1 and rows $4,6,8$ equal row 2; rows 1 and 2 are independent. So $\operatorname{rank}B=2$ and rows 1, 2 are a basis of the row space.

2. The left nullspace has dimension $8-2=6$. Each repeated row gives a vector: $\mathbf{e}_3-\mathbf{e}_1,\ \mathbf{e}_5-\mathbf{e}_1,\ \mathbf{e}_7-\mathbf{e}_1,\ \mathbf{e}_4-\mathbf{e}_2,\ \mathbf{e}_6-\mathbf{e}_2,\ \mathbf{e}_8-\mathbf{e}_2$. They are independent (each has its own $+1$ in positions $3,\dots,8$), so they form a basis. ($B$ is symmetric, so this is also a basis of $N(B)$.)

**Chess matrix $C$** (assume $r\neq0$).

3. Rows 3–6 are zero, row 7 equals row 2 and row 8 equals row 1. If $p\neq0$, rows 1 and 2 are independent (row 2 is constant, row 1 is not since $r\ne n$), so $\operatorname{rank}C=2$, with rows 1 and 2 as a row-space basis. If $p=0$, $\operatorname{rank}C=1$, with row 1 as a basis.

4. Left nullspace for $p\neq0$ (dimension $6$): $\mathbf{e}_8-\mathbf{e}_1,\ \mathbf{e}_7-\mathbf{e}_2,\ \mathbf{e}_3,\ \mathbf{e}_4,\ \mathbf{e}_5,\ \mathbf{e}_6$. For $p=0$ (dimension $7$): $\mathbf{e}_8-\mathbf{e}_1,\ \mathbf{e}_2,\dots,\mathbf{e}_7$.

5. **Challenge**, $p\neq0$: $N(C)$ has dimension $8-2=6$ and is given by $r x_1+n x_2+b x_3+q x_4+k x_5+b x_6+n x_7+r x_8=0$ and $x_1+\dots+x_8=0$. Equal columns give three solutions: $\mathbf{e}_1-\mathbf{e}_8$, $\mathbf{e}_2-\mathbf{e}_7$, $\mathbf{e}_3-\mathbf{e}_6$. For three more, put $x_j=1$ for one $j\in\{3,4,5\}$ with weight $w_j\in\{b,q,k\}$, and solve for $x_1,x_2$ from $rx_1+nx_2=-w_j$, $x_1+x_2=-1$:
   $$x_1=\frac{n-w_j}{r-n},\qquad x_2=\frac{w_j-r}{r-n}.$$
   The six vectors are independent: the first three are the only ones touching positions $8,7,6$, and the last three have their $1$s in different positions among $3,4,5$.

6. For $p=0$ only the first equation remains, $\dim N(C)=7$: the three vectors above together with $\mathbf{e}_j-\frac{w_j}r\mathbf{e}_1$ for $j=2,3,4,5$ ($w_2=n$).
:::

::: {.solution for="prob-mit1806s10-4-q9" status="draft"}
1. In $\mathbb{R}^2$ (inputs): the row space is the line through $\mathbf{v}$ and the nullspace is the perpendicular line through $\mathbf{v}^{\perp}$. In $\mathbb{R}^2$ (outputs): the column space is the line through $\mathbf{u}$ and the left nullspace is the perpendicular line. Each of the four subspaces is a line, and $A$ sends the row-space line onto the column-space line, everything else to $\mathbf{0}$.

2. If $B$ has the same four subspaces, then $B$ has rank $1$ with $C(B)$ the line through $\mathbf{u}$ and row space the line through $\mathbf{v}$. So $B=\mathbf{u}'\mathbf{v}'^{\mathsf T}$ with $\mathbf{u}'=a\mathbf{u}$ and $\mathbf{v}'=b\mathbf{v}$ (@prp-rank-one-iff), i.e. $B=cA$ for some number $c\neq0$.
:::
