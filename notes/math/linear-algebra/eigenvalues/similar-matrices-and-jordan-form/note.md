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

::: {#fig-similar-matrices-and-jordan-form-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (x) at (0,1.6) {$\mathbf x$}; \node[box] (Ax) at (4.6,1.6) {$A\mathbf x$};
\node[box] (y) at (0,0) {$M^{-1}\mathbf x$}; \node[box] (By) at (4.6,0) {$M^{-1}A\mathbf x$};
\draw[->, emph] (x) -- node[above, lab] {$A$} (Ax);
\draw[->, emph, accent] (y) -- node[below, lab] {$B=M^{-1}AM$} (By);
\draw[->, emph] (x) -- node[left, lab] {$M^{-1}$} (y);
\draw[->, emph] (Ax) -- node[right, lab] {$M^{-1}$} (By);
\end{tikzpicture}
\end{center}
```

Similar matrices describe one map in two coordinate systems: $B$ acts on coordinates with respect to the columns of $M$. That is why they share eigenvalues, trace and determinant.

:::

Similarity is an equivalence relation, and diagonalization (@thm-diagonalization) says that a matrix with $n$ independent eigenvectors is similar to its eigenvalue matrix $\Lambda$.

::: {#thm-similar-same-eigenvalues .theorem name="Similar matrices share eigenvalues"}

If $B=M^{-1}AM$, then $A$ and $B$ have the same characteristic polynomial, hence the same eigenvalues, trace and determinant. If $A\mathbf{x}=\lambda\mathbf{x}$, then $B(M^{-1}\mathbf{x})=\lambda M^{-1}\mathbf{x}$.

:::

::: {.proof}

1. $\det(B-\lambda I)=\det(M^{-1}(A-\lambda I)M)=\det M^{-1}\det(A-\lambda I)\det M=\det(A-\lambda I)$, by the product rule (@thm-determinant-multiplicative).

2. Trace and determinant are read off the characteristic polynomial (@thm-trace-determinant-eigenvalues).

3. $BM^{-1}\mathbf{x}=M^{-1}AMM^{-1}\mathbf{x}=M^{-1}A\mathbf{x}=\lambda M^{-1}\mathbf{x}$.

:::

The converse fails: $\begin{bmatrix}4&0\\0&4\end{bmatrix}$ and $\begin{bmatrix}4&1\\0&4\end{bmatrix}$ have the same eigenvalues but are not similar, since $M^{-1}(4I)M=4I$ for every $M$. The second matrix has only one independent eigenvector.

::: {#def-jordan-block .definition name="Jordan block"}

A *Jordan block* $J_k(\lambda)$ is the $k\times k$ matrix with $\lambda$ on the diagonal, $1$ on the diagonal just above it, and $0$ elsewhere. It has the single eigenvalue $\lambda$ with a one-dimensional eigenspace, spanned by $\mathbf{e}_1$.

:::

::: {#fig-similar-matrices-and-jordan-form-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.000,1.650) rectangle (0.550,2.200);
\node[lab] at (0.275,1.925) {$\lambda$};
\draw[cell, fill=primaryLight] (0.550,1.650) rectangle (1.100,2.200);
\node[lab] at (0.825,1.925) {$1$};
\draw[cell frame] (1.100,1.650) rectangle (1.650,2.200);
\draw[cell frame] (1.650,1.650) rectangle (2.200,2.200);
\draw[cell frame] (0.000,1.100) rectangle (0.550,1.650);
\draw[hl cell] (0.550,1.100) rectangle (1.100,1.650);
\node[lab] at (0.825,1.375) {$\lambda$};
\draw[cell, fill=primaryLight] (1.100,1.100) rectangle (1.650,1.650);
\node[lab] at (1.375,1.375) {$1$};
\draw[cell frame] (1.650,1.100) rectangle (2.200,1.650);
\draw[cell frame] (0.000,0.550) rectangle (0.550,1.100);
\draw[cell frame] (0.550,0.550) rectangle (1.100,1.100);
\draw[hl cell] (1.100,0.550) rectangle (1.650,1.100);
\node[lab] at (1.375,0.825) {$\lambda$};
\draw[cell, fill=primaryLight] (1.650,0.550) rectangle (2.200,1.100);
\node[lab] at (1.925,0.825) {$1$};
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\draw[cell frame] (1.100,0.000) rectangle (1.650,0.550);
\draw[hl cell] (1.650,0.000) rectangle (2.200,0.550);
\node[lab] at (1.925,0.275) {$\lambda$};
\node[lab, note] at (1.100,-0.350) {$J_4(\lambda)$};
\node[lab, note, anchor=west, align=left] at (2.6,1.1) {one eigenvalue $\lambda$ on the diagonal,\\$1$s just above it, zeros elsewhere;\\only one eigenvector, $\mathbf e_1$};
\end{tikzpicture}
\end{center}
```

A $4\times4$ Jordan block. $J-\lambda I$ shifts $\mathbf e_4\to\mathbf e_3\to\mathbf e_2\to\mathbf e_1\to\mathbf 0$, so its nullspace is only the line through $\mathbf e_1$.

:::

<!-- Merged 2026-11-20 (owner): the block thm-jordan-form was removed in favour of thm-jordan-normal-form (Cambridge IB Linear Algebra), which states it for any field or inner product space with a full proof. -->

**Jordan form.** Every square complex matrix $A$ is similar to a block-diagonal matrix $J=M^{-1}AM$ of Jordan blocks $J_{k_1}(\lambda_1),\dots,J_{k_s}(\lambda_s)$, unique up to the order of the blocks. The number of blocks for $\lambda$ is the number of independent eigenvectors for $\lambda$, and $A$ is diagonalizable exactly when every block is $1\times1$. Statement and proof: @thm-jordan-normal-form.

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

::: {#fig-similar-matrices-and-jordan-form-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[shift={(0,0)}]
\node[small vertex] (n1) at (0,0) {$\mathbf e_1$};
\node[small vertex] (n2) at (1.0,0) {$\mathbf e_2$};
\draw[->, emph] (n2) -- (n1);
\node[small vertex] (n3) at (2.0,0) {$\mathbf e_3$};
\draw[->, emph] (n3) -- (n2);
\node[lab, tick] (z1) at (0.0,-0.85) {$\mathbf 0$};
\draw[->, emph, accent] (n1) -- (z1);
\node[small vertex] (n4) at (3.5,0) {$\mathbf e_4$};
\node[lab, tick] (z4) at (3.5,-0.85) {$\mathbf 0$};
\draw[->, emph, accent] (n4) -- (z4);
\node[lab, note] at (1.5,-1.4) {blocks of sizes $3$ and $1$};
\end{scope}
\begin{scope}[shift={(5.2,0)}]
\node[small vertex] (n1) at (0,0) {$\mathbf e_1$};
\node[small vertex] (n2) at (1.0,0) {$\mathbf e_2$};
\draw[->, emph] (n2) -- (n1);
\node[lab, tick] (z1) at (0.0,-0.85) {$\mathbf 0$};
\draw[->, emph, accent] (n1) -- (z1);
\node[small vertex] (n3) at (2.5,0) {$\mathbf e_3$};
\node[small vertex] (n4) at (3.5,0) {$\mathbf e_4$};
\draw[->, emph] (n4) -- (n3);
\node[lab, tick] (z3) at (2.5,-0.85) {$\mathbf 0$};
\draw[->, emph, accent] (n3) -- (z3);
\node[lab, note] at (1.5,-1.4) {two blocks of size $2$};
\end{scope}
\end{tikzpicture}
\end{center}
```

The two matrices of @exm-jordan-four-by-four as chains (an arrow means \"$N$ sends this vector to\"). Both have two chains, hence two eigenvectors, but on the left a vector needs three steps to reach $\mathbf 0$ and on the right only two, so $N^2\neq0$ in one case and $N^2=0$ in the other.

:::
