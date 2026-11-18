<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-2-q10" status="draft"}
(a) True. If $A^{\mathsf T}=A$ and $B^{\mathsf T}=B$, then $(cA+dB)^{\mathsf T}=cA^{\mathsf T}+dB^{\mathsf T}=cA+dB$.

(b) True. If $A^{\mathsf T}=-A$ and $B^{\mathsf T}=-B$, then $(cA+dB)^{\mathsf T}=-cA-dB=-(cA+dB)$.

(c) False. It does not contain the zero matrix (which is symmetric). Also addition fails: $\begin{bmatrix}0&1\\0&0\end{bmatrix}+\begin{bmatrix}0&0\\1&0\end{bmatrix}=\begin{bmatrix}0&1\\1&0\end{bmatrix}$ is a sum of two unsymmetric matrices that is symmetric.
:::

::: {.solution for="prob-mit1806s10-2-q11" status="draft"}
1. The column space gets larger unless $\mathbf{b}$ is already in $C(A)$, i.e. $\mathbf{b}$ is a combination of the columns of $A$.

2. Example: $A=\begin{bmatrix}1&0\\0&0\end{bmatrix}$, $C(A)$ is the $x$-axis. With $\mathbf{b}=(0,1)$ the column space grows to $\mathbb{R}^2$; with $\mathbf{b}=(2,0)$ it stays the $x$-axis.

3. $C([A\ \mathbf{b}])$ consists of the combinations $A\mathbf{x}+t\mathbf{b}$. If $\mathbf{b}=A\mathbf{x}_0$, these are all in $C(A)$, so nothing changes. If $\mathbf{b}\notin C(A)$, then $\mathbf{b}$ itself is a new vector. And $\mathbf{b}=A\mathbf{x}_0$ for some $\mathbf{x}_0$ is exactly solvability (@thm-column-space-solvability).
:::

::: {.solution for="prob-mit1806s10-2-q12" status="draft"}
(a) Take $\mathbf{s}+\mathbf{t}$ and $\mathbf{s}'+\mathbf{t}'$ in $\mathbf{S}+\mathbf{T}$ and a scalar $c$. Then $(\mathbf{s}+\mathbf{t})+(\mathbf{s}'+\mathbf{t}')=(\mathbf{s}+\mathbf{s}')+(\mathbf{t}+\mathbf{t}')$ and $c(\mathbf{s}+\mathbf{t})=c\mathbf{s}+c\mathbf{t}$, again a vector of $\mathbf{S}$ plus a vector of $\mathbf{T}$. It contains $\mathbf{0}=\mathbf{0}+\mathbf{0}$. So it is a subspace, hence a vector space.

(b)

1. For two different lines through $\mathbf{0}$, $\mathbf{S}+\mathbf{T}$ is the plane containing them, while $\mathbf{S}\cup\mathbf{T}$ is just the two lines, which is not closed under addition (if the lines are equal, both are that line).

2. The span of $\mathbf{S}\cup\mathbf{T}$ consists of all combinations of vectors from the union. Grouping the terms from $\mathbf{S}$ and those from $\mathbf{T}$, each combination is $\mathbf{s}+\mathbf{t}$, so the span is inside $\mathbf{S}+\mathbf{T}$.

3. Conversely every $\mathbf{s}+\mathbf{t}$ is a combination of vectors of the union. So the span equals $\mathbf{S}+\mathbf{T}$: the smallest subspace containing both.
:::

::: {.solution for="prob-mit1806s10-2-q13" status="draft"}
1. Column $j$ of $AB$ is $A$ times column $j$ of $B$, a combination of the columns of $A$ (@thm-four-ways-to-multiply). So every combination of the columns of $[A\ AB]$ is a combination of the columns of $A$; and $C(A)\subseteq C([A\ AB])$ trivially. The two column spaces are equal.

2. $A=\begin{bmatrix}0&1\\0&0\end{bmatrix}$ has $C(A)$ = the line through $(1,0)$, but $A^2=0$, so $C(A^2)=\{\mathbf{0}\}$.

3. $C(A)=\mathbb{R}^n$ means $A\mathbf{x}=\mathbf{b}$ is solvable for every $\mathbf{b}$, which for a square matrix happens exactly when $A$ is *invertible* (@thm-rank-and-solutions).
:::
