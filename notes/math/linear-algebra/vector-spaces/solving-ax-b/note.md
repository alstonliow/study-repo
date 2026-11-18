---
title: "Solving Ax = b"
sources: [mit1806-8]
requires: [math/linear-algebra/vector-spaces/nullspace]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 8, in our own wording; proofs written out in steps. Example numbers checked with sympy. -->

To solve $A\mathbf{x}=\mathbf{b}$, eliminate on the augmented matrix $[A\ \mathbf{b}]$. A zero row of $R$ turns into an equation $0=c$; the system is solvable exactly when every such $c$ is $0$.

::: {#thm-complete-solution .theorem name="Complete solution of Ax = b"}

If $A\mathbf{x}=\mathbf{b}$ has a solution $\mathbf{x}_p$, then its solutions are exactly
$$\mathbf{x}=\mathbf{x}_p+\mathbf{x}_n,\qquad \mathbf{x}_n\in N(A).$$
A *particular solution* is found by setting all free variables to $0$ and solving for the pivot variables.

:::

::: {.proof}

1. If $A\mathbf{x}_n=\mathbf{0}$ then $A(\mathbf{x}_p+\mathbf{x}_n)=\mathbf{b}+\mathbf{0}=\mathbf{b}$.

2. Conversely, if $A\mathbf{x}=\mathbf{b}$ then $A(\mathbf{x}-\mathbf{x}_p)=\mathbf{0}$, so $\mathbf{x}-\mathbf{x}_p\in N(A)$.

3. With the free variables at $0$, each nonzero row of the reduced system gives its pivot variable directly, so the particular solution exists whenever the zero rows are consistent.

:::

::: {#exm-complete-solution .example name="A complete solution"}

For $A$ of @exm-nullspace-three-by-four, row 3 of $A$ is row 1 plus row 2, so $A\mathbf{x}=\mathbf{b}$ is solvable only if $b_3=b_1+b_2$. For $\mathbf{b}=(1,4,5)$:
$$[A\ \mathbf{b}]\to\begin{bmatrix}1&2&0&1&1\\0&0&1&2&2\\0&0&0&0&0\end{bmatrix},\qquad \mathbf{x}_p=(1,0,2,0),$$
$$\mathbf{x}=(1,0,2,0)+c\,(-2,1,0,0)+d\,(-1,0,-2,1).$$

:::

::: {#thm-rank-and-solutions .theorem name="Rank decides the number of solutions"}

Let $A$ be $m\times n$ with rank $r$ (so $r\le m$ and $r\le n$).

1. $r=m=n$ (square, invertible): exactly one solution for every $\mathbf{b}$.
2. $r=n<m$ (full column rank): no free variables, $N(A)=\{\mathbf{0}\}$; zero or one solution.
3. $r=m<n$ (full row rank): no zero rows in $R$; infinitely many solutions for every $\mathbf{b}$.
4. $r<m$ and $r<n$: zero or infinitely many solutions.

:::

::: {.proof}

1. Solvability for every $\mathbf{b}$ fails exactly when $R$ has a zero row ($r<m$): choose $\mathbf{b}$ so that that row of the eliminated right side is nonzero, which is possible because the elimination matrix is invertible.

2. When a solution exists, @thm-complete-solution says it is unique exactly when $N(A)=\{\mathbf{0}\}$, i.e. when there are no free variables ($r=n$), by @thm-special-solutions; otherwise there are infinitely many.

3. Combining the two answers gives the four cases.

:::

::: {#rmk-solving-ax-b-1 .remark name="The shape of R in the four cases"}

The reduced forms are $R=I$; $R=\begin{bmatrix}I\\0\end{bmatrix}$; $R=\begin{bmatrix}I&F\end{bmatrix}$; $R=\begin{bmatrix}I&F\\0&0\end{bmatrix}$ (with the pivot columns moved to the front).

:::
