---
title: "Solving Structured Linear Equations"
sources: [ee364a-9]
requires: [math/linear-algebra/positive-definite/positive-definite-matrices]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on numerical linear algebra, in our own wording; proofs written out in steps. Flop counts checked by hand. -->

Every step of Newton's method and of interior-point methods solves a linear system. The cost is dominated by factoring the matrix, and exploiting structure (sparsity, blocks, low rank) can reduce it by orders of magnitude.

::: {#def-flop-count .definition name="Flop count"}

A *flop* is one floating-point addition, subtraction, multiplication or division. Costs are given by their leading terms: an inner product of vectors in $\mathbb{R}^n$ costs $2n-1\approx2n$ flops, a matrix–vector product with $A\in\mathbb{R}^{m\times n}$ costs $2mn$, and a matrix–matrix product of $m\times n$ by $n\times p$ costs $2mnp$.

:::

::: {#def-factor-solve .definition name="Factor-solve method"}

To solve $Ax=b$, factor $A=A_1A_2\cdots A_k$ with each $A_i$ easy to invert (diagonal, triangular, orthogonal, permutation), then solve $A_1z_1=b$, $A_2z_2=z_1$, …, $A_kx=z_{k-1}$. The factorization is usually the expensive part, and it can be reused for several right-hand sides.

:::

::: {#prp-factorization-costs .proposition name="Costs of the standard factorizations"}

For a dense $A\in\mathbb{R}^{n\times n}$:

1. LU with partial pivoting, $A=PLU$ (@thm-lu-factorization), costs $\frac23n^3$ flops; each solve then costs $2n^2$.

2. For $A\in\mathbb S^n_{++}$, Cholesky $A=LL^{\mathsf T}$ costs $\frac13n^3$ flops.

3. Forward or back substitution with a triangular matrix costs $n^2$ flops.

:::

::: {.proof}

1. Triangular solve: row $i$ needs $i-1$ multiplications, $i-1$ subtractions and one division, so $\sum_i(2i-1)=n^2$.

2. Cholesky: step $k$ computes $L_{kk}$ and column $k$ below it, then updates the trailing $(n-k)\times(n-k)$ block by a symmetric rank-one update costing about $(n-k)^2$ flops (only half the entries). Summing, $\sum_k(n-k)^2\approx n^3/3$.

3. LU does the same updates without symmetry, $\sum_k2(n-k)^2\approx\frac23n^3$.

:::

::: {#thm-block-elimination .theorem name="Block elimination"}

Consider
$$\begin{bmatrix}A_{11}&A_{12}\\A_{21}&A_{22}\end{bmatrix}\begin{bmatrix}x_1\\x_2\end{bmatrix}=\begin{bmatrix}b_1\\b_2\end{bmatrix}$$
with $A_{11}$ invertible. Then $x_2$ solves $Sx_2=b_2-A_{21}A_{11}^{-1}b_1$ with the Schur complement $S=A_{22}-A_{21}A_{11}^{-1}A_{12}$, and $x_1=A_{11}^{-1}(b_1-A_{12}x_2)$. If $A_{11}$ is easy to solve with (diagonal, banded), forming and solving with $S$ is much cheaper than factoring the whole matrix.

:::

::: {.proof}

1. The first block row gives $x_1=A_{11}^{-1}(b_1-A_{12}x_2)$.

2. Substituting into the second, $A_{21}A_{11}^{-1}(b_1-A_{12}x_2)+A_{22}x_2=b_2$, which rearranges to $Sx_2=b_2-A_{21}A_{11}^{-1}b_1$.

:::

::: {#exm-block-elimination-cost .example name="Diagonal block"}

Let $A_{11}\in\mathbb{R}^{n_1\times n_1}$ be diagonal and $A_{22}\in\mathbb{R}^{n_2\times n_2}$ dense with $n_2\ll n_1$. Forming $S$ costs $2n_1n_2^2$ flops (scale the rows of $A_{12}$, multiply by $A_{21}$), factoring $S$ costs $\frac23n_2^3$, and the rest is lower order. For $n_1=1000$, $n_2=10$ that is about $2\times10^5$ flops, against $\frac23(1010)^3\approx6.9\times10^8$ for dense LU.

:::

::: {#prp-matrix-inversion-lemma .proposition name="Diagonal plus low rank"}

To solve $(A+BC)x=b$ with $A$ easy to invert, $B\in\mathbb{R}^{n\times p}$, $C\in\mathbb{R}^{p\times n}$, $p\ll n$: introduce $y=Cx$ and solve
$$\begin{bmatrix}A&B\\C&-I\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix}=\begin{bmatrix}b\\0\end{bmatrix}$$
by block elimination of $x$: $(I+CA^{-1}B)y=CA^{-1}b$, then $x=A^{-1}(b-By)$. This is the matrix inversion lemma $(A+BC)^{-1}=A^{-1}-A^{-1}B(I+CA^{-1}B)^{-1}CA^{-1}$.

:::

::: {.proof}

1. The second block row says $y=Cx$, and then the first is $Ax+BCx=b$, so the two systems have the same $x$.

2. Eliminating $x=A^{-1}(b-By)$ from $Cx-y=0$ gives $CA^{-1}b-CA^{-1}By-y=0$, the stated $p\times p$ system.

3. Substituting back gives $x=A^{-1}b-A^{-1}B(I+CA^{-1}B)^{-1}CA^{-1}b$ for every $b$, which is the lemma.

:::

::: {#rmk-structured-linear-equations-1 .remark name="Sparse factorizations"}

For sparse $A$, the cost of sparse LU or Cholesky depends on the ordering of rows and columns, chosen to limit fill-in; it can be far below $n^3$ and is often roughly linear in $n$ for banded or tree-like sparsity.

:::
