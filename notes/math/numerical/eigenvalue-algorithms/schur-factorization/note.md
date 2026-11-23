---
title: "The Schur Factorization"
sources: [mit18335-14]
requires: [math/linear-algebra/eigenvalues/similar-matrices-and-jordan-form, math/linear-algebra/eigenvalues/complex-matrices, math/numerical/qr-and-least-squares/householder-qr]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lecture 14 (eigenproblems and Schur factorizations), in our own wording; proofs written out in steps, the example checked with numpy. -->

Eigenvalue algorithms compute a factorization that reveals the eigenvalues. Diagonalization $A=X\Lambda X^{-1}$ need not exist, and when it does $X$ may be badly conditioned. The Schur factorization always exists and uses only a unitary similarity, so it can be computed stably; it is the target of the QR algorithm.

::: {#def-eigenvalue-revealing-factorizations .definition name="Eigenvalue-revealing factorizations"}

For a square matrix $A\in\mathbb{C}^{m\times m}$:

1. a *diagonalization* is $A=X\Lambda X^{-1}$ with $\Lambda$ diagonal (it exists iff $A$ is nondefective, @thm-diagonalization);

2. a *unitary diagonalization* is $A=Q\Lambda Q^{\mathsf H}$ with $Q$ unitary and $\Lambda$ diagonal;

3. a *Schur factorization* is $A=QTQ^{\mathsf H}$ with $Q$ unitary and $T$ upper triangular.

In each, the eigenvalues of $A$ are the diagonal entries of the middle factor, because similar matrices have the same eigenvalues (@thm-similar-same-eigenvalues) and a triangular matrix has its diagonal as eigenvalues.

:::

::: {#thm-schur-factorization .theorem name="Schur factorization" related="thm-spectral-theorem-self-adjoint"}

Every $A\in\mathbb{C}^{m\times m}$ has a Schur factorization $A=QTQ^{\mathsf H}$. The diagonal of $T$ can be made to list the eigenvalues in any prescribed order.

:::

::: {.proof}

1. *Induction on $m$.* For $m=1$ take $Q=(1)$, $T=A$.

2. Let $\lambda$ be any eigenvalue of $A$ (one exists over $\mathbb{C}$ by the fundamental theorem of algebra) and $\mathbf{q}_1$ a unit eigenvector. Extend it to a unitary $U=[\mathbf{q}_1\ U_2]$, for instance by a Householder reflector mapping $\mathbf{e}_1$ to a multiple of $\mathbf{q}_1$.

3. Then $U^{\mathsf H}AU=\begin{bmatrix}\mathbf{q}_1^{\mathsf H}A\mathbf{q}_1&\mathbf{q}_1^{\mathsf H}AU_2\\U_2^{\mathsf H}A\mathbf{q}_1&U_2^{\mathsf H}AU_2\end{bmatrix}=\begin{bmatrix}\lambda&\mathbf{b}^{\mathsf H}\\\mathbf{0}&C\end{bmatrix}$, because $A\mathbf{q}_1=\lambda\mathbf{q}_1$ and $U_2^{\mathsf H}\mathbf{q}_1=\mathbf{0}$.

4. By induction $C=VT_2V^{\mathsf H}$ with $V$ unitary of size $m-1$ and $T_2$ upper triangular. Put $Q=U\begin{bmatrix}1&0\\0&V\end{bmatrix}$; then $Q^{\mathsf H}AQ=\begin{bmatrix}\lambda&\mathbf{b}^{\mathsf H}V\\\mathbf{0}&T_2\end{bmatrix}$, which is upper triangular.

5. The eigenvalue $\lambda$ chosen at each level of the induction can be any eigenvalue of the current matrix, so any order is possible.

:::

::: {#fig-schur-factorization-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-0.04,0.05) -- (-0.10,0.05) -- (-0.10,-1.41) -- (-0.04,-1.41);
\draw[faint] (1.40,0.05) -- (1.46,0.05) -- (1.46,-1.41) -- (1.40,-1.41);
\node[tick] at (0.17,-0.17) {$\times$};
\node[tick] at (0.51,-0.17) {$\times$};
\node[tick] at (0.85,-0.17) {$\times$};
\node[tick] at (1.19,-0.17) {$\times$};
\node[tick] at (0.17,-0.51) {$\times$};
\node[tick] at (0.51,-0.51) {$\times$};
\node[tick] at (0.85,-0.51) {$\times$};
\node[tick] at (1.19,-0.51) {$\times$};
\node[tick] at (0.17,-0.85) {$\times$};
\node[tick] at (0.51,-0.85) {$\times$};
\node[tick] at (0.85,-0.85) {$\times$};
\node[tick] at (1.19,-0.85) {$\times$};
\node[tick] at (0.17,-1.19) {$\times$};
\node[tick] at (0.51,-1.19) {$\times$};
\node[tick] at (0.85,-1.19) {$\times$};
\node[tick] at (1.19,-1.19) {$\times$};
\node[note] at (0.68,-1.71) {$A$};
\node[lbl] at (1.74,-0.68) {$=$};
\draw[faint] (2.07,0.05) -- (2.01,0.05) -- (2.01,-1.41) -- (2.07,-1.41);
\draw[faint] (3.51,0.05) -- (3.57,0.05) -- (3.57,-1.41) -- (3.51,-1.41);
\node[tick] at (2.28,-0.17) {$\times$};
\node[tick] at (2.62,-0.17) {$\times$};
\node[tick] at (2.96,-0.17) {$\times$};
\node[tick] at (3.30,-0.17) {$\times$};
\node[tick] at (2.28,-0.51) {$\times$};
\node[tick] at (2.62,-0.51) {$\times$};
\node[tick] at (2.96,-0.51) {$\times$};
\node[tick] at (3.30,-0.51) {$\times$};
\node[tick] at (2.28,-0.85) {$\times$};
\node[tick] at (2.62,-0.85) {$\times$};
\node[tick] at (2.96,-0.85) {$\times$};
\node[tick] at (3.30,-0.85) {$\times$};
\node[tick] at (2.28,-1.19) {$\times$};
\node[tick] at (2.62,-1.19) {$\times$};
\node[tick] at (2.96,-1.19) {$\times$};
\node[tick] at (3.30,-1.19) {$\times$};
\node[note] at (2.79,-1.71) {$Q$};
\node[lbl] at (3.85,-0.68) {};
\draw[faint] (4.18,0.05) -- (4.12,0.05) -- (4.12,-1.41) -- (4.18,-1.41);
\draw[faint] (5.62,0.05) -- (5.68,0.05) -- (5.68,-1.41) -- (5.62,-1.41);
\fill[accentLight] (4.24,-0.32) rectangle (4.54,-0.02);
\node[tick] at (4.39,-0.17) {$\times$};
\node[tick] at (4.73,-0.17) {$\times$};
\node[tick] at (5.07,-0.17) {$\times$};
\node[tick] at (5.41,-0.17) {$\times$};
\fill[accentLight] (4.58,-0.66) rectangle (4.88,-0.36);
\node[tick] at (4.73,-0.51) {$\times$};
\node[tick] at (5.07,-0.51) {$\times$};
\node[tick] at (5.41,-0.51) {$\times$};
\fill[accentLight] (4.92,-1.00) rectangle (5.22,-0.70);
\node[tick] at (5.07,-0.85) {$\times$};
\node[tick] at (5.41,-0.85) {$\times$};
\fill[accentLight] (5.26,-1.34) rectangle (5.56,-1.04);
\node[tick] at (5.41,-1.19) {$\times$};
\node[note] at (4.90,-1.71) {$T$};
\node[lbl] at (5.96,-0.68) {};
\draw[faint] (6.29,0.05) -- (6.23,0.05) -- (6.23,-1.41) -- (6.29,-1.41);
\draw[faint] (7.73,0.05) -- (7.79,0.05) -- (7.79,-1.41) -- (7.73,-1.41);
\node[tick] at (6.50,-0.17) {$\times$};
\node[tick] at (6.84,-0.17) {$\times$};
\node[tick] at (7.18,-0.17) {$\times$};
\node[tick] at (7.52,-0.17) {$\times$};
\node[tick] at (6.50,-0.51) {$\times$};
\node[tick] at (6.84,-0.51) {$\times$};
\node[tick] at (7.18,-0.51) {$\times$};
\node[tick] at (7.52,-0.51) {$\times$};
\node[tick] at (6.50,-0.85) {$\times$};
\node[tick] at (6.84,-0.85) {$\times$};
\node[tick] at (7.18,-0.85) {$\times$};
\node[tick] at (7.52,-0.85) {$\times$};
\node[tick] at (6.50,-1.19) {$\times$};
\node[tick] at (6.84,-1.19) {$\times$};
\node[tick] at (7.18,-1.19) {$\times$};
\node[tick] at (7.52,-1.19) {$\times$};
\node[note] at (7.01,-1.71) {$Q^{\mathsf H}$};
\end{tikzpicture}
\end{center}
```

The shapes in a Schur factorization $A=QTQ^{\mathsf H}$: a full matrix equals a unitary matrix times an upper triangular one times the conjugate transpose. The diagonal of $T$ (shaded) holds the eigenvalues.

:::

::: {#prp-schur-invariant-subspaces .proposition name="Schur vectors span nested invariant subspaces"}

If $A=QTQ^{\mathsf H}$ is a Schur factorization with columns $\mathbf{q}_1,\dots,\mathbf{q}_m$, then for each $k$ the span $S_k=\operatorname{span}\{\mathbf{q}_1,\dots,\mathbf{q}_k\}$ is invariant under $A$ ($AS_k\subseteq S_k$), and the restriction of $A$ to $S_k$ has eigenvalues $t_{11},\dots,t_{kk}$.

:::

::: {.proof}

1. $AQ=QT$ and $T$ is upper triangular, so column $j$ reads $A\mathbf{q}_j=\sum_{i\le j}t_{ij}\mathbf{q}_i\in S_j\subseteq S_k$ for $j\le k$.

2. In the basis $\mathbf{q}_1,\dots,\mathbf{q}_k$ of $S_k$, the restriction has matrix $T_{1:k,1:k}$, upper triangular with diagonal $t_{11},\dots,t_{kk}$.

:::

::: {#fig-schur-factorization-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionC] (0,0) ellipse (3.6 and 1.6); \node[lab] at (2.6,1.25) {$\mathbb{C}^3=S_3$};
\draw[regionB] (-0.6,0) ellipse (2.3 and 1.05); \node[lab] at (0.9,0.6) {$S_2$};
\draw[regionA] (-1.4,0) ellipse (1.0 and 0.5); \node[lab] at (-1.4,0) {$S_1=\operatorname{span}\mathbf{q}_1$};
\end{tikzpicture}
\end{center}
```

The Schur vectors give a chain $S_1\subset S_2\subset S_3$ of invariant subspaces. Only $S_1$ is spanned by an eigenvector in general; the later $\mathbf{q}_k$ are not eigenvectors unless $T$ is diagonal.

:::

::: {#exm-schur-two-by-two .example name="Schur factorization of a non-normal matrix"}

$A=\begin{bmatrix}1&2\\-1&4\end{bmatrix}$ has eigenvalues $2$ and $3$, with eigenvector $(2,1)$ for $\lambda=2$. Taking $\mathbf{q}_1=(2,1)/\sqrt5$ and $\mathbf{q}_2=(-1,2)/\sqrt5$,
$$Q^{\mathsf T}AQ=\begin{bmatrix}2&3\\0&3\end{bmatrix}=T.$$
The off-diagonal entry $3$ measures how far $A$ is from normal: since $\lVert T\rVert_F=\lVert A\rVert_F$, here $\sum\lvert\lambda_i\rvert^2=13<22=\lVert A\rVert_F^2$, and the gap $9=3^2$ is $\lvert t_{12}\rvert^2$.

:::

::: {#rmk-schur-factorization-1 .remark name="Normal matrices and the real Schur form"}

1. A matrix is *normal* if $AA^{\mathsf H}=A^{\mathsf H}A$. A triangular matrix is normal only if it is diagonal, so the normal matrices are exactly those with $T$ diagonal, i.e. the unitarily diagonalizable ones; Hermitian and unitary matrices are examples (see the exercises).

2. For real $A$ one avoids complex arithmetic with the *real Schur form* $A=QTQ^{\mathsf T}$, $Q$ real orthogonal and $T$ real block upper triangular with $1\times1$ blocks (real eigenvalues) and $2\times2$ blocks (pairs of complex conjugate eigenvalues) on the diagonal.

3. From a Schur factorization the eigenvectors follow by back substitution: an eigenvector of $T$ for $t_{kk}$ solves the triangular system $(T_{1:k,1:k}-t_{kk}I)\mathbf{y}=\mathbf{0}$ with $y_k=1$, and $Q\mathbf{y}$ is an eigenvector of $A$.

:::
