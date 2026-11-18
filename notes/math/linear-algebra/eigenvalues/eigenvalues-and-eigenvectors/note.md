---
title: "Eigenvalues and Eigenvectors"
sources: [mit1806-21]
requires: [math/linear-algebra/determinants/cramers-rule-and-volume]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 21, in our own wording; proofs written out in steps. Example numbers checked with sympy. -->

::: {#def-eigenvalue .definition name="Eigenvalue and eigenvector"}

Let $A$ be an $n\times n$ matrix. A nonzero vector $\mathbf{x}$ is an *eigenvector* of $A$ with *eigenvalue* $\lambda$ if
$$A\mathbf{x}=\lambda\mathbf{x}.$$
The eigenvectors for $\lambda$, together with $\mathbf{0}$, form the *eigenspace* $N(A-\lambda I)$.

:::

An eigenvector keeps its direction under $A$; the eigenvalue says how it is stretched, shrunk or reversed. Eigenvalue $0$ means $\mathbf{x}\in N(A)$, so $A$ is singular.

::: {#thm-characteristic-equation .theorem name="The characteristic equation"}

$\lambda$ is an eigenvalue of $A$ if and only if
$$\det(A-\lambda I)=0.$$
The left side is a polynomial of degree $n$ in $\lambda$ (the *characteristic polynomial*), so $A$ has exactly $n$ eigenvalues in $\mathbb{C}$, counted with multiplicity.

:::

::: {.proof}

1. $A\mathbf{x}=\lambda\mathbf{x}$ with $\mathbf{x}\neq\mathbf{0}$ means $(A-\lambda I)\mathbf{x}=\mathbf{0}$ has a nonzero solution, i.e. $A-\lambda I$ is singular.

2. By @thm-determinant-consequences (property 8) this happens exactly when $\det(A-\lambda I)=0$.

3. In the big formula (@thm-big-formula-determinant) the only term of degree $n$ comes from the diagonal: $(a_{11}-\lambda)\cdots(a_{nn}-\lambda)$, which has leading coefficient $(-1)^n$. By the fundamental theorem of algebra it has $n$ complex roots with multiplicity.

:::

::: {#thm-trace-determinant-eigenvalues .theorem name="Trace and determinant"}

If $A$ has eigenvalues $\lambda_1,\dots,\lambda_n$ (with multiplicity), then
$$\lambda_1+\dots+\lambda_n=\operatorname{tr}A=a_{11}+\dots+a_{nn},\qquad \lambda_1\lambda_2\cdots\lambda_n=\det A.$$

:::

::: {.proof}

1. Since the eigenvalues are the roots, $\det(A-\lambda I)=(\lambda_1-\lambda)\cdots(\lambda_n-\lambda)$.

2. Setting $\lambda=0$ gives $\det A=\lambda_1\cdots\lambda_n$.

3. Compare the coefficients of $\lambda^{n-1}$. On the right it is $(-1)^{n-1}(\lambda_1+\dots+\lambda_n)$. On the left, only the diagonal term of the big formula contributes to $\lambda^{n-1}$ (any other term omits at least two diagonal entries), giving $(-1)^{n-1}(a_{11}+\dots+a_{nn})$.

:::

::: {#exm-eigenvalues-two-by-two .example name="A 2 by 2 example"}

For $A=\begin{bmatrix}4&1\\2&3\end{bmatrix}$:
$$\det(A-\lambda I)=(4-\lambda)(3-\lambda)-2=\lambda^2-7\lambda+10=(\lambda-5)(\lambda-2).$$
So $\lambda_1=5$, $\lambda_2=2$; check: $5+2=7=\operatorname{tr}A$ and $5\cdot2=10=\det A$. The eigenvectors solve $(A-\lambda I)\mathbf{x}=\mathbf{0}$: $\mathbf{x}_1=(1,1)$ and $\mathbf{x}_2=(1,-2)$.

:::

::: {#fig-eigenvalues-and-eigenvectors-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.800,0) -- (2.400,0) node[lab, right] {$x$};
\draw[->, faint] (0,-1.800) -- (0,2.300) node[lab, above] {$y$};
\draw[->, emph] (0.000,0.000) -- (0.380,0.380);
\node[lab, left] at (0.380,0.380) {$\mathbf x_1$};
\draw[->, hl] (0.000,0.000) -- (1.900,1.900);
\node[lab, right] at (1.900,1.900) {$A\mathbf x=5\mathbf x$};
\draw[->, emph] (0.000,0.000) -- (0.380,-0.760);
\node[lab, left] at (0.380,-0.760) {$\mathbf x_2$};
\draw[->, hl] (0.000,0.000) -- (0.760,-1.520);
\node[lab, right] at (0.760,-1.520) {$A\mathbf x=2\mathbf x$};
\end{tikzpicture}
\end{center}
```

The eigenvectors keep their direction: $A\mathbf x_1=5\mathbf x_1$ and $A\mathbf x_2=2\mathbf x_2$ (thick: the images).

:::

::: {#exm-eigenvalues-special-matrices .example name="Projections, permutations, rotations"}

1. A projection $P$ has eigenvalues $1$ (vectors in its column space) and $0$ (vectors in its nullspace).
2. The exchange $\begin{bmatrix}0&1\\1&0\end{bmatrix}$ has $\lambda=1$ for $(1,1)$ and $\lambda=-1$ for $(1,-1)$.
3. The rotation $\begin{bmatrix}0&-1\\1&0\end{bmatrix}$ turns every real vector by $90^\circ$, so it has no real eigenvector. Its characteristic polynomial $\lambda^2+1$ has roots $\pm i$.
4. A triangular matrix has its diagonal entries as eigenvalues, since $\det(A-\lambda I)$ is the product of $a_{ii}-\lambda$.

:::

::: {#rmk-eigenvalues-and-eigenvectors-1 .remark name="What eigenvalues do not do"}

Elimination changes eigenvalues, and in general the eigenvalues of $A+B$ and of $AB$ are not sums or products of the eigenvalues of $A$ and $B$. They are when $A$ and $B$ share the same eigenvectors. Adding $cI$ shifts every eigenvalue by $c$ and keeps the eigenvectors.

:::
