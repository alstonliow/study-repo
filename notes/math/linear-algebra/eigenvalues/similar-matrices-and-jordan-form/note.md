---
title: "Similar Matrices and Jordan Form"
sources: [mit1806-28]
requires: [math/linear-algebra/eigenvalues/diagonalization]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 28, in our own wording; proofs written out in steps. The existence of the Jordan form is stated without proof, as in the lecture. -->

::: {#def-similar-matrices .definition name="Similar matrices"}

$n\times n$ matrices $A$ and $B$ are *similar* if $B=M^{-1}AM$ for some invertible $M$.

:::

Similarity is an equivalence relation, and diagonalization (@thm-diagonalization) says that a matrix with $n$ independent eigenvectors is similar to its eigenvalue matrix $\Lambda$.

::: {#thm-similar-same-eigenvalues .theorem name="Similar matrices share eigenvalues"}

If $B=M^{-1}AM$, then $A$ and $B$ have the same characteristic polynomial, hence the same eigenvalues, trace and determinant. If $A\mathbf{x}=\lambda\mathbf{x}$, then $B(M^{-1}\mathbf{x})=\lambda M^{-1}\mathbf{x}$.

:::

::: {.proof}

1. $\det(B-\lambda I)=\det(M^{-1}(A-\lambda I)M)=\det M^{-1}\det(A-\lambda I)\det M=\det(A-\lambda I)$, by the product rule (@thm-product-rule-determinants).

2. Trace and determinant are read off the characteristic polynomial (@thm-trace-determinant-eigenvalues).

3. $BM^{-1}\mathbf{x}=M^{-1}AMM^{-1}\mathbf{x}=M^{-1}A\mathbf{x}=\lambda M^{-1}\mathbf{x}$.

:::

The converse fails: $\begin{bmatrix}4&0\\0&4\end{bmatrix}$ and $\begin{bmatrix}4&1\\0&4\end{bmatrix}$ have the same eigenvalues but are not similar, since $M^{-1}(4I)M=4I$ for every $M$. The second matrix has only one independent eigenvector.

::: {#def-jordan-block .definition name="Jordan block"}

A *Jordan block* $J_k(\lambda)$ is the $k\times k$ matrix with $\lambda$ on the diagonal, $1$ on the diagonal just above it, and $0$ elsewhere. It has the single eigenvalue $\lambda$ with a one-dimensional eigenspace, spanned by $\mathbf{e}_1$.

:::

::: {#thm-jordan-form .theorem name="Jordan form"}

Every square matrix $A$ is similar to a block-diagonal matrix
$$J=M^{-1}AM=\begin{bmatrix}J_{k_1}(\lambda_1)&&\\&\ddots&\\&&J_{k_s}(\lambda_s)\end{bmatrix},$$
unique up to the order of the blocks. The number of blocks for an eigenvalue $\lambda$ is the number of independent eigenvectors for $\lambda$. $A$ is diagonalizable exactly when every block is $1\times1$.

:::

::: {#prp-jordan-block-properties .proposition name="Eigenvectors of a Jordan block"}

$J_k(\lambda)-\lambda I$ has rank $k-1$, so $J_k(\lambda)$ has exactly one independent eigenvector. Two matrices with the same eigenvalues but different numbers of independent eigenvectors are not similar.

:::

::: {.proof}

1. $J_k(\lambda)-\lambda I$ has $1$s just above the diagonal and $0$ elsewhere: $k-1$ pivots, one free variable (the first). So $\dim N(J_k(\lambda)-\lambda I)=1$.

2. If $B=M^{-1}AM$, then $B-\lambda I=M^{-1}(A-\lambda I)M$ has the same rank as $A-\lambda I$ (multiplying by invertible matrices does not change the nullspace dimension: $\mathbf{x}\mapsto M\mathbf{x}$ maps $N(B-\lambda I)$ onto $N(A-\lambda I)$). So similar matrices have the same number of independent eigenvectors for each $\lambda$.

:::

::: {#fig-similar-matrices-and-jordan-form-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (e3) at (0,0) {$\mathbf e_3$};
\node[box] (e2) at (2.4,0) {$\mathbf e_2$};
\node[box] (e1) at (4.8,0) {$\mathbf e_1$};
\node[hl box] (z) at (7.2,0) {$\mathbf 0$};
\foreach \a/\b in {e3/e2,e2/e1,e1/z} \draw[map] (\a) -- node[edge label, above=3pt] {$N$} (\b);
\end{tikzpicture}
\end{center}
```

For $N=J_3(\lambda)-\lambda I$: $N\mathbf e_3=\mathbf e_2$, $N\mathbf e_2=\mathbf e_1$ and $N\mathbf e_1=\mathbf 0$, a single chain. Only the multiples of $\mathbf e_1$ are eigenvectors, and $N$ has rank $2=k-1$.

:::

::: {#exm-jordan-four-by-four .example name="Same eigenvalues, not similar"}

The $4\times4$ matrices
$$\begin{bmatrix}0&1&0&0\\0&0&1&0\\0&0&0&0\\0&0&0&0\end{bmatrix},\qquad\begin{bmatrix}0&1&0&0\\0&0&0&0\\0&0&0&1\\0&0&0&0\end{bmatrix}$$
both have eigenvalue $0$ four times and rank $2$, so both have two independent eigenvectors. They are still not similar: the first has blocks of sizes $3$ and $1$, the second two blocks of size $2$ (the square of the first is nonzero, the square of the second is $0$).

:::
