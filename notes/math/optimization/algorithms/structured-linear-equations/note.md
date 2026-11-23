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

::: {#fig-structured-linear-equations-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (a) at (0,0) {$Ax=b$};
\node[box] (z1) at (2.6,0) {$A_1z_1=b$};
\node[box] (z2) at (5.2,0) {$A_2z_2=z_1$};
\node[lab] (dots) at (7.0,0) {$\cdots$};
\node[hl box] (zk) at (8.8,0) {$A_kx=z_{k-1}$};
\draw[map] (a) -- (z1);
\draw[map] (z1) -- (z2);
\draw[map] (z2) -- (dots);
\draw[map] (dots) -- (zk);
\node[lab, note] at (0,0.65) {factor $A=A_1A_2\cdots A_k$};
\node[lab, note] at (5.2,-0.65) {each solve is easy (triangular, diagonal, orthogonal, permutation)};
\end{tikzpicture}
\end{center}
```

Factor-solve: once $A$ is factored into easy matrices, $Ax=b$ becomes a chain of easy solves. The factorization dominates the cost, and it can be reused for every new right-hand side.

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

::: {#fig-structured-linear-equations-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0,-0.24) rectangle (0.24,0);
\draw[hl cell] (0.24,-0.24) rectangle (0.48,0);
\draw[hl cell] (0.48,-0.24) rectangle (0.72,0);
\draw[hl cell] (0.72,-0.24) rectangle (0.96,0);
\draw[hl cell] (0.96,-0.24) rectangle (1.2,0);
\draw[hl cell] (1.2,-0.24) rectangle (1.44,0);
\draw[hl cell] (1.44,-0.24) rectangle (1.68,0);
\draw[hl cell] (1.68,-0.24) rectangle (1.92,0);
\draw[hl cell] (0,-0.48) rectangle (0.24,-0.24);
\draw[hl cell] (0.24,-0.48) rectangle (0.48,-0.24);
\draw[hl cell] (0.48,-0.48) rectangle (0.72,-0.24);
\draw[hl cell] (0.72,-0.48) rectangle (0.96,-0.24);
\draw[hl cell] (0.96,-0.48) rectangle (1.2,-0.24);
\draw[hl cell] (1.2,-0.48) rectangle (1.44,-0.24);
\draw[hl cell] (1.44,-0.48) rectangle (1.68,-0.24);
\draw[hl cell] (1.68,-0.48) rectangle (1.92,-0.24);
\draw[hl cell] (0,-0.72) rectangle (0.24,-0.48);
\draw[hl cell] (0.24,-0.72) rectangle (0.48,-0.48);
\draw[hl cell] (0.48,-0.72) rectangle (0.72,-0.48);
\draw[hl cell] (0.72,-0.72) rectangle (0.96,-0.48);
\draw[hl cell] (0.96,-0.72) rectangle (1.2,-0.48);
\draw[hl cell] (1.2,-0.72) rectangle (1.44,-0.48);
\draw[hl cell] (1.44,-0.72) rectangle (1.68,-0.48);
\draw[hl cell] (1.68,-0.72) rectangle (1.92,-0.48);
\draw[hl cell] (0,-0.96) rectangle (0.24,-0.72);
\draw[hl cell] (0.24,-0.96) rectangle (0.48,-0.72);
\draw[hl cell] (0.48,-0.96) rectangle (0.72,-0.72);
\draw[hl cell] (0.72,-0.96) rectangle (0.96,-0.72);
\draw[hl cell] (0.96,-0.96) rectangle (1.2,-0.72);
\draw[hl cell] (1.2,-0.96) rectangle (1.44,-0.72);
\draw[hl cell] (1.44,-0.96) rectangle (1.68,-0.72);
\draw[hl cell] (1.68,-0.96) rectangle (1.92,-0.72);
\draw[hl cell] (0,-1.2) rectangle (0.24,-0.96);
\draw[hl cell] (0.24,-1.2) rectangle (0.48,-0.96);
\draw[hl cell] (0.48,-1.2) rectangle (0.72,-0.96);
\draw[hl cell] (0.72,-1.2) rectangle (0.96,-0.96);
\draw[hl cell] (0.96,-1.2) rectangle (1.2,-0.96);
\draw[hl cell] (1.2,-1.2) rectangle (1.44,-0.96);
\draw[hl cell] (1.44,-1.2) rectangle (1.68,-0.96);
\draw[hl cell] (1.68,-1.2) rectangle (1.92,-0.96);
\draw[hl cell] (0,-1.44) rectangle (0.24,-1.2);
\draw[hl cell] (0.24,-1.44) rectangle (0.48,-1.2);
\draw[hl cell] (0.48,-1.44) rectangle (0.72,-1.2);
\draw[hl cell] (0.72,-1.44) rectangle (0.96,-1.2);
\draw[hl cell] (0.96,-1.44) rectangle (1.2,-1.2);
\draw[hl cell] (1.2,-1.44) rectangle (1.44,-1.2);
\draw[hl cell] (1.44,-1.44) rectangle (1.68,-1.2);
\draw[hl cell] (1.68,-1.44) rectangle (1.92,-1.2);
\draw[hl cell] (0,-1.68) rectangle (0.24,-1.44);
\draw[hl cell] (0.24,-1.68) rectangle (0.48,-1.44);
\draw[hl cell] (0.48,-1.68) rectangle (0.72,-1.44);
\draw[hl cell] (0.72,-1.68) rectangle (0.96,-1.44);
\draw[hl cell] (0.96,-1.68) rectangle (1.2,-1.44);
\draw[hl cell] (1.2,-1.68) rectangle (1.44,-1.44);
\draw[hl cell] (1.44,-1.68) rectangle (1.68,-1.44);
\draw[hl cell] (1.68,-1.68) rectangle (1.92,-1.44);
\draw[hl cell] (0,-1.92) rectangle (0.24,-1.68);
\draw[hl cell] (0.24,-1.92) rectangle (0.48,-1.68);
\draw[hl cell] (0.48,-1.92) rectangle (0.72,-1.68);
\draw[hl cell] (0.72,-1.92) rectangle (0.96,-1.68);
\draw[hl cell] (0.96,-1.92) rectangle (1.2,-1.68);
\draw[hl cell] (1.2,-1.92) rectangle (1.44,-1.68);
\draw[hl cell] (1.44,-1.92) rectangle (1.68,-1.68);
\draw[hl cell] (1.68,-1.92) rectangle (1.92,-1.68);
\node[lab] at (0.96,-2.22) {dense $\tfrac23n^3$};
\draw[hl cell] (2.4,-0.24) rectangle (2.64,0);
\draw[hl cell] (2.64,-0.24) rectangle (2.88,0);
\draw[cell frame] (2.88,-0.24) rectangle (3.12,0);
\draw[cell frame] (3.12,-0.24) rectangle (3.36,0);
\draw[cell frame] (3.36,-0.24) rectangle (3.6,0);
\draw[cell frame] (3.6,-0.24) rectangle (3.84,0);
\draw[cell frame] (3.84,-0.24) rectangle (4.08,0);
\draw[cell frame] (4.08,-0.24) rectangle (4.32,0);
\draw[hl cell] (2.4,-0.48) rectangle (2.64,-0.24);
\draw[hl cell] (2.64,-0.48) rectangle (2.88,-0.24);
\draw[hl cell] (2.88,-0.48) rectangle (3.12,-0.24);
\draw[cell frame] (3.12,-0.48) rectangle (3.36,-0.24);
\draw[cell frame] (3.36,-0.48) rectangle (3.6,-0.24);
\draw[cell frame] (3.6,-0.48) rectangle (3.84,-0.24);
\draw[cell frame] (3.84,-0.48) rectangle (4.08,-0.24);
\draw[cell frame] (4.08,-0.48) rectangle (4.32,-0.24);
\draw[cell frame] (2.4,-0.72) rectangle (2.64,-0.48);
\draw[hl cell] (2.64,-0.72) rectangle (2.88,-0.48);
\draw[hl cell] (2.88,-0.72) rectangle (3.12,-0.48);
\draw[hl cell] (3.12,-0.72) rectangle (3.36,-0.48);
\draw[cell frame] (3.36,-0.72) rectangle (3.6,-0.48);
\draw[cell frame] (3.6,-0.72) rectangle (3.84,-0.48);
\draw[cell frame] (3.84,-0.72) rectangle (4.08,-0.48);
\draw[cell frame] (4.08,-0.72) rectangle (4.32,-0.48);
\draw[cell frame] (2.4,-0.96) rectangle (2.64,-0.72);
\draw[cell frame] (2.64,-0.96) rectangle (2.88,-0.72);
\draw[hl cell] (2.88,-0.96) rectangle (3.12,-0.72);
\draw[hl cell] (3.12,-0.96) rectangle (3.36,-0.72);
\draw[hl cell] (3.36,-0.96) rectangle (3.6,-0.72);
\draw[cell frame] (3.6,-0.96) rectangle (3.84,-0.72);
\draw[cell frame] (3.84,-0.96) rectangle (4.08,-0.72);
\draw[cell frame] (4.08,-0.96) rectangle (4.32,-0.72);
\draw[cell frame] (2.4,-1.2) rectangle (2.64,-0.96);
\draw[cell frame] (2.64,-1.2) rectangle (2.88,-0.96);
\draw[cell frame] (2.88,-1.2) rectangle (3.12,-0.96);
\draw[hl cell] (3.12,-1.2) rectangle (3.36,-0.96);
\draw[hl cell] (3.36,-1.2) rectangle (3.6,-0.96);
\draw[hl cell] (3.6,-1.2) rectangle (3.84,-0.96);
\draw[cell frame] (3.84,-1.2) rectangle (4.08,-0.96);
\draw[cell frame] (4.08,-1.2) rectangle (4.32,-0.96);
\draw[cell frame] (2.4,-1.44) rectangle (2.64,-1.2);
\draw[cell frame] (2.64,-1.44) rectangle (2.88,-1.2);
\draw[cell frame] (2.88,-1.44) rectangle (3.12,-1.2);
\draw[cell frame] (3.12,-1.44) rectangle (3.36,-1.2);
\draw[hl cell] (3.36,-1.44) rectangle (3.6,-1.2);
\draw[hl cell] (3.6,-1.44) rectangle (3.84,-1.2);
\draw[hl cell] (3.84,-1.44) rectangle (4.08,-1.2);
\draw[cell frame] (4.08,-1.44) rectangle (4.32,-1.2);
\draw[cell frame] (2.4,-1.68) rectangle (2.64,-1.44);
\draw[cell frame] (2.64,-1.68) rectangle (2.88,-1.44);
\draw[cell frame] (2.88,-1.68) rectangle (3.12,-1.44);
\draw[cell frame] (3.12,-1.68) rectangle (3.36,-1.44);
\draw[cell frame] (3.36,-1.68) rectangle (3.6,-1.44);
\draw[hl cell] (3.6,-1.68) rectangle (3.84,-1.44);
\draw[hl cell] (3.84,-1.68) rectangle (4.08,-1.44);
\draw[hl cell] (4.08,-1.68) rectangle (4.32,-1.44);
\draw[cell frame] (2.4,-1.92) rectangle (2.64,-1.68);
\draw[cell frame] (2.64,-1.92) rectangle (2.88,-1.68);
\draw[cell frame] (2.88,-1.92) rectangle (3.12,-1.68);
\draw[cell frame] (3.12,-1.92) rectangle (3.36,-1.68);
\draw[cell frame] (3.36,-1.92) rectangle (3.6,-1.68);
\draw[cell frame] (3.6,-1.92) rectangle (3.84,-1.68);
\draw[hl cell] (3.84,-1.92) rectangle (4.08,-1.68);
\draw[hl cell] (4.08,-1.92) rectangle (4.32,-1.68);
\node[lab] at (3.36,-2.22) {banded $\approx nk^2$};
\draw[hl cell] (4.8,-0.24) rectangle (5.04,0);
\draw[cell frame] (5.04,-0.24) rectangle (5.28,0);
\draw[cell frame] (5.28,-0.24) rectangle (5.52,0);
\draw[cell frame] (5.52,-0.24) rectangle (5.76,0);
\draw[cell frame] (5.76,-0.24) rectangle (6,0);
\draw[cell frame] (6,-0.24) rectangle (6.24,0);
\draw[cell frame] (6.24,-0.24) rectangle (6.48,0);
\draw[hl cell] (6.48,-0.24) rectangle (6.72,0);
\draw[cell frame] (4.8,-0.48) rectangle (5.04,-0.24);
\draw[hl cell] (5.04,-0.48) rectangle (5.28,-0.24);
\draw[cell frame] (5.28,-0.48) rectangle (5.52,-0.24);
\draw[cell frame] (5.52,-0.48) rectangle (5.76,-0.24);
\draw[cell frame] (5.76,-0.48) rectangle (6,-0.24);
\draw[cell frame] (6,-0.48) rectangle (6.24,-0.24);
\draw[cell frame] (6.24,-0.48) rectangle (6.48,-0.24);
\draw[hl cell] (6.48,-0.48) rectangle (6.72,-0.24);
\draw[cell frame] (4.8,-0.72) rectangle (5.04,-0.48);
\draw[cell frame] (5.04,-0.72) rectangle (5.28,-0.48);
\draw[hl cell] (5.28,-0.72) rectangle (5.52,-0.48);
\draw[cell frame] (5.52,-0.72) rectangle (5.76,-0.48);
\draw[cell frame] (5.76,-0.72) rectangle (6,-0.48);
\draw[cell frame] (6,-0.72) rectangle (6.24,-0.48);
\draw[cell frame] (6.24,-0.72) rectangle (6.48,-0.48);
\draw[hl cell] (6.48,-0.72) rectangle (6.72,-0.48);
\draw[cell frame] (4.8,-0.96) rectangle (5.04,-0.72);
\draw[cell frame] (5.04,-0.96) rectangle (5.28,-0.72);
\draw[cell frame] (5.28,-0.96) rectangle (5.52,-0.72);
\draw[hl cell] (5.52,-0.96) rectangle (5.76,-0.72);
\draw[cell frame] (5.76,-0.96) rectangle (6,-0.72);
\draw[cell frame] (6,-0.96) rectangle (6.24,-0.72);
\draw[cell frame] (6.24,-0.96) rectangle (6.48,-0.72);
\draw[hl cell] (6.48,-0.96) rectangle (6.72,-0.72);
\draw[cell frame] (4.8,-1.2) rectangle (5.04,-0.96);
\draw[cell frame] (5.04,-1.2) rectangle (5.28,-0.96);
\draw[cell frame] (5.28,-1.2) rectangle (5.52,-0.96);
\draw[cell frame] (5.52,-1.2) rectangle (5.76,-0.96);
\draw[hl cell] (5.76,-1.2) rectangle (6,-0.96);
\draw[cell frame] (6,-1.2) rectangle (6.24,-0.96);
\draw[cell frame] (6.24,-1.2) rectangle (6.48,-0.96);
\draw[hl cell] (6.48,-1.2) rectangle (6.72,-0.96);
\draw[cell frame] (4.8,-1.44) rectangle (5.04,-1.2);
\draw[cell frame] (5.04,-1.44) rectangle (5.28,-1.2);
\draw[cell frame] (5.28,-1.44) rectangle (5.52,-1.2);
\draw[cell frame] (5.52,-1.44) rectangle (5.76,-1.2);
\draw[cell frame] (5.76,-1.44) rectangle (6,-1.2);
\draw[hl cell] (6,-1.44) rectangle (6.24,-1.2);
\draw[cell frame] (6.24,-1.44) rectangle (6.48,-1.2);
\draw[hl cell] (6.48,-1.44) rectangle (6.72,-1.2);
\draw[cell frame] (4.8,-1.68) rectangle (5.04,-1.44);
\draw[cell frame] (5.04,-1.68) rectangle (5.28,-1.44);
\draw[cell frame] (5.28,-1.68) rectangle (5.52,-1.44);
\draw[cell frame] (5.52,-1.68) rectangle (5.76,-1.44);
\draw[cell frame] (5.76,-1.68) rectangle (6,-1.44);
\draw[cell frame] (6,-1.68) rectangle (6.24,-1.44);
\draw[hl cell] (6.24,-1.68) rectangle (6.48,-1.44);
\draw[hl cell] (6.48,-1.68) rectangle (6.72,-1.44);
\draw[hl cell] (4.8,-1.92) rectangle (5.04,-1.68);
\draw[hl cell] (5.04,-1.92) rectangle (5.28,-1.68);
\draw[hl cell] (5.28,-1.92) rectangle (5.52,-1.68);
\draw[hl cell] (5.52,-1.92) rectangle (5.76,-1.68);
\draw[hl cell] (5.76,-1.92) rectangle (6,-1.68);
\draw[hl cell] (6,-1.92) rectangle (6.24,-1.68);
\draw[hl cell] (6.24,-1.92) rectangle (6.48,-1.68);
\draw[hl cell] (6.48,-1.92) rectangle (6.72,-1.68);
\node[lab] at (5.76,-2.22) {arrow};
\draw[hl cell] (7.2,-0.24) rectangle (7.44,0);
\draw[cell frame] (7.44,-0.24) rectangle (7.68,0);
\draw[cell frame] (7.68,-0.24) rectangle (7.92,0);
\draw[cell frame] (7.92,-0.24) rectangle (8.16,0);
\draw[cell frame] (8.16,-0.24) rectangle (8.4,0);
\draw[hl cell] (8.4,-0.24) rectangle (8.64,0);
\draw[hl cell] (8.64,-0.24) rectangle (8.88,0);
\draw[hl cell] (8.88,-0.24) rectangle (9.12,0);
\draw[cell frame] (7.2,-0.48) rectangle (7.44,-0.24);
\draw[hl cell] (7.44,-0.48) rectangle (7.68,-0.24);
\draw[cell frame] (7.68,-0.48) rectangle (7.92,-0.24);
\draw[cell frame] (7.92,-0.48) rectangle (8.16,-0.24);
\draw[cell frame] (8.16,-0.48) rectangle (8.4,-0.24);
\draw[hl cell] (8.4,-0.48) rectangle (8.64,-0.24);
\draw[hl cell] (8.64,-0.48) rectangle (8.88,-0.24);
\draw[hl cell] (8.88,-0.48) rectangle (9.12,-0.24);
\draw[cell frame] (7.2,-0.72) rectangle (7.44,-0.48);
\draw[cell frame] (7.44,-0.72) rectangle (7.68,-0.48);
\draw[hl cell] (7.68,-0.72) rectangle (7.92,-0.48);
\draw[cell frame] (7.92,-0.72) rectangle (8.16,-0.48);
\draw[cell frame] (8.16,-0.72) rectangle (8.4,-0.48);
\draw[hl cell] (8.4,-0.72) rectangle (8.64,-0.48);
\draw[hl cell] (8.64,-0.72) rectangle (8.88,-0.48);
\draw[hl cell] (8.88,-0.72) rectangle (9.12,-0.48);
\draw[cell frame] (7.2,-0.96) rectangle (7.44,-0.72);
\draw[cell frame] (7.44,-0.96) rectangle (7.68,-0.72);
\draw[cell frame] (7.68,-0.96) rectangle (7.92,-0.72);
\draw[hl cell] (7.92,-0.96) rectangle (8.16,-0.72);
\draw[cell frame] (8.16,-0.96) rectangle (8.4,-0.72);
\draw[hl cell] (8.4,-0.96) rectangle (8.64,-0.72);
\draw[hl cell] (8.64,-0.96) rectangle (8.88,-0.72);
\draw[hl cell] (8.88,-0.96) rectangle (9.12,-0.72);
\draw[cell frame] (7.2,-1.2) rectangle (7.44,-0.96);
\draw[cell frame] (7.44,-1.2) rectangle (7.68,-0.96);
\draw[cell frame] (7.68,-1.2) rectangle (7.92,-0.96);
\draw[cell frame] (7.92,-1.2) rectangle (8.16,-0.96);
\draw[hl cell] (8.16,-1.2) rectangle (8.4,-0.96);
\draw[hl cell] (8.4,-1.2) rectangle (8.64,-0.96);
\draw[hl cell] (8.64,-1.2) rectangle (8.88,-0.96);
\draw[hl cell] (8.88,-1.2) rectangle (9.12,-0.96);
\draw[hl cell] (7.2,-1.44) rectangle (7.44,-1.2);
\draw[hl cell] (7.44,-1.44) rectangle (7.68,-1.2);
\draw[hl cell] (7.68,-1.44) rectangle (7.92,-1.2);
\draw[hl cell] (7.92,-1.44) rectangle (8.16,-1.2);
\draw[hl cell] (8.16,-1.44) rectangle (8.4,-1.2);
\draw[hl cell] (8.4,-1.44) rectangle (8.64,-1.2);
\draw[hl cell] (8.64,-1.44) rectangle (8.88,-1.2);
\draw[hl cell] (8.88,-1.44) rectangle (9.12,-1.2);
\draw[hl cell] (7.2,-1.68) rectangle (7.44,-1.44);
\draw[hl cell] (7.44,-1.68) rectangle (7.68,-1.44);
\draw[hl cell] (7.68,-1.68) rectangle (7.92,-1.44);
\draw[hl cell] (7.92,-1.68) rectangle (8.16,-1.44);
\draw[hl cell] (8.16,-1.68) rectangle (8.4,-1.44);
\draw[hl cell] (8.4,-1.68) rectangle (8.64,-1.44);
\draw[hl cell] (8.64,-1.68) rectangle (8.88,-1.44);
\draw[hl cell] (8.88,-1.68) rectangle (9.12,-1.44);
\draw[hl cell] (7.2,-1.92) rectangle (7.44,-1.68);
\draw[hl cell] (7.44,-1.92) rectangle (7.68,-1.68);
\draw[hl cell] (7.68,-1.92) rectangle (7.92,-1.68);
\draw[hl cell] (7.92,-1.92) rectangle (8.16,-1.68);
\draw[hl cell] (8.16,-1.92) rectangle (8.4,-1.68);
\draw[hl cell] (8.4,-1.92) rectangle (8.64,-1.68);
\draw[hl cell] (8.64,-1.92) rectangle (8.88,-1.68);
\draw[hl cell] (8.88,-1.92) rectangle (9.12,-1.68);
\node[lab] at (8.16,-2.22) {diagonal block};
\end{tikzpicture}
\end{center}
```

Nonzero patterns (shaded) and why they matter: a dense matrix costs about $\tfrac23n^3$ flops to factor, a banded one with bandwidth $k$ only about $nk^2$. The arrow and diagonal-block patterns are dense only in a few rows and columns, which block elimination exploits.

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

::: {#fig-structured-linear-equations-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0,-0.24) rectangle (0.24,0);
\draw[cell frame] (0.24,-0.24) rectangle (0.48,0);
\draw[cell frame] (0.48,-0.24) rectangle (0.72,0);
\draw[cell frame] (0.72,-0.24) rectangle (0.96,0);
\draw[cell frame] (0.96,-0.24) rectangle (1.2,0);
\draw[hl cell] (1.2,-0.24) rectangle (1.44,0);
\draw[hl cell] (1.44,-0.24) rectangle (1.68,0);
\draw[hl cell] (1.68,-0.24) rectangle (1.92,0);
\draw[cell frame] (0,-0.48) rectangle (0.24,-0.24);
\draw[hl cell] (0.24,-0.48) rectangle (0.48,-0.24);
\draw[cell frame] (0.48,-0.48) rectangle (0.72,-0.24);
\draw[cell frame] (0.72,-0.48) rectangle (0.96,-0.24);
\draw[cell frame] (0.96,-0.48) rectangle (1.2,-0.24);
\draw[hl cell] (1.2,-0.48) rectangle (1.44,-0.24);
\draw[hl cell] (1.44,-0.48) rectangle (1.68,-0.24);
\draw[hl cell] (1.68,-0.48) rectangle (1.92,-0.24);
\draw[cell frame] (0,-0.72) rectangle (0.24,-0.48);
\draw[cell frame] (0.24,-0.72) rectangle (0.48,-0.48);
\draw[hl cell] (0.48,-0.72) rectangle (0.72,-0.48);
\draw[cell frame] (0.72,-0.72) rectangle (0.96,-0.48);
\draw[cell frame] (0.96,-0.72) rectangle (1.2,-0.48);
\draw[hl cell] (1.2,-0.72) rectangle (1.44,-0.48);
\draw[hl cell] (1.44,-0.72) rectangle (1.68,-0.48);
\draw[hl cell] (1.68,-0.72) rectangle (1.92,-0.48);
\draw[cell frame] (0,-0.96) rectangle (0.24,-0.72);
\draw[cell frame] (0.24,-0.96) rectangle (0.48,-0.72);
\draw[cell frame] (0.48,-0.96) rectangle (0.72,-0.72);
\draw[hl cell] (0.72,-0.96) rectangle (0.96,-0.72);
\draw[cell frame] (0.96,-0.96) rectangle (1.2,-0.72);
\draw[hl cell] (1.2,-0.96) rectangle (1.44,-0.72);
\draw[hl cell] (1.44,-0.96) rectangle (1.68,-0.72);
\draw[hl cell] (1.68,-0.96) rectangle (1.92,-0.72);
\draw[cell frame] (0,-1.2) rectangle (0.24,-0.96);
\draw[cell frame] (0.24,-1.2) rectangle (0.48,-0.96);
\draw[cell frame] (0.48,-1.2) rectangle (0.72,-0.96);
\draw[cell frame] (0.72,-1.2) rectangle (0.96,-0.96);
\draw[hl cell] (0.96,-1.2) rectangle (1.2,-0.96);
\draw[hl cell] (1.2,-1.2) rectangle (1.44,-0.96);
\draw[hl cell] (1.44,-1.2) rectangle (1.68,-0.96);
\draw[hl cell] (1.68,-1.2) rectangle (1.92,-0.96);
\draw[hl cell] (0,-1.44) rectangle (0.24,-1.2);
\draw[hl cell] (0.24,-1.44) rectangle (0.48,-1.2);
\draw[hl cell] (0.48,-1.44) rectangle (0.72,-1.2);
\draw[hl cell] (0.72,-1.44) rectangle (0.96,-1.2);
\draw[hl cell] (0.96,-1.44) rectangle (1.2,-1.2);
\draw[hl cell] (1.2,-1.44) rectangle (1.44,-1.2);
\draw[hl cell] (1.44,-1.44) rectangle (1.68,-1.2);
\draw[hl cell] (1.68,-1.44) rectangle (1.92,-1.2);
\draw[hl cell] (0,-1.68) rectangle (0.24,-1.44);
\draw[hl cell] (0.24,-1.68) rectangle (0.48,-1.44);
\draw[hl cell] (0.48,-1.68) rectangle (0.72,-1.44);
\draw[hl cell] (0.72,-1.68) rectangle (0.96,-1.44);
\draw[hl cell] (0.96,-1.68) rectangle (1.2,-1.44);
\draw[hl cell] (1.2,-1.68) rectangle (1.44,-1.44);
\draw[hl cell] (1.44,-1.68) rectangle (1.68,-1.44);
\draw[hl cell] (1.68,-1.68) rectangle (1.92,-1.44);
\draw[hl cell] (0,-1.92) rectangle (0.24,-1.68);
\draw[hl cell] (0.24,-1.92) rectangle (0.48,-1.68);
\draw[hl cell] (0.48,-1.92) rectangle (0.72,-1.68);
\draw[hl cell] (0.72,-1.92) rectangle (0.96,-1.68);
\draw[hl cell] (0.96,-1.92) rectangle (1.2,-1.68);
\draw[hl cell] (1.2,-1.92) rectangle (1.44,-1.68);
\draw[hl cell] (1.44,-1.92) rectangle (1.68,-1.68);
\draw[hl cell] (1.68,-1.92) rectangle (1.92,-1.68);
\draw[emph] (0,-1.2) -- (1.92,-1.2) (1.2,0) -- (1.2,-1.92);
\node[lab] at (0.6,-0.6) {$A_{11}$};
\node[lab] at (1.56,-1.56) {$A_{22}$};
\node[lab] at (1.56,-0.6) {$A_{12}$};
\node[lab] at (0.6,0.25) {$n_1$};
\node[box] (s1) at (4.4,-0.1) {solve with $A_{11}$\\ (cheap)};
\node[hl box] (s2) at (4.6,-1.75) {$S=A_{22}-A_{21}A_{11}^{-1}A_{12}$\\ solve $Sx_2=\cdots$};
\node[box] (s3) at (8.6,-0.95) {back-substitute\\ $x_1=A_{11}^{-1}(b_1-A_{12}x_2)$};
\draw[map] (s1) -- (s2);
\draw[map] (s2) -- (s3);
\draw[map] (2.0,-0.95) -- (s1.west);
\end{tikzpicture}
\end{center}
```

Block elimination on a matrix whose $(1,1)$ block is diagonal: solves with $A_{11}$ are cheap, so the work reduces to forming and factoring the small Schur complement $S$, then back-substituting for $x_1$.

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

::: {#fig-structured-linear-equations-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0,-0.24) rectangle (0.24,0);
\draw[cell frame] (0.24,-0.24) rectangle (0.48,0);
\draw[cell frame] (0.48,-0.24) rectangle (0.72,0);
\draw[cell frame] (0.72,-0.24) rectangle (0.96,0);
\draw[cell frame] (0.96,-0.24) rectangle (1.2,0);
\draw[cell frame] (1.2,-0.24) rectangle (1.44,0);
\draw[cell frame] (1.44,-0.24) rectangle (1.68,0);
\draw[cell frame] (1.68,-0.24) rectangle (1.92,0);
\draw[cell frame] (0,-0.48) rectangle (0.24,-0.24);
\draw[hl cell] (0.24,-0.48) rectangle (0.48,-0.24);
\draw[cell frame] (0.48,-0.48) rectangle (0.72,-0.24);
\draw[cell frame] (0.72,-0.48) rectangle (0.96,-0.24);
\draw[cell frame] (0.96,-0.48) rectangle (1.2,-0.24);
\draw[cell frame] (1.2,-0.48) rectangle (1.44,-0.24);
\draw[cell frame] (1.44,-0.48) rectangle (1.68,-0.24);
\draw[cell frame] (1.68,-0.48) rectangle (1.92,-0.24);
\draw[cell frame] (0,-0.72) rectangle (0.24,-0.48);
\draw[cell frame] (0.24,-0.72) rectangle (0.48,-0.48);
\draw[hl cell] (0.48,-0.72) rectangle (0.72,-0.48);
\draw[cell frame] (0.72,-0.72) rectangle (0.96,-0.48);
\draw[cell frame] (0.96,-0.72) rectangle (1.2,-0.48);
\draw[cell frame] (1.2,-0.72) rectangle (1.44,-0.48);
\draw[cell frame] (1.44,-0.72) rectangle (1.68,-0.48);
\draw[cell frame] (1.68,-0.72) rectangle (1.92,-0.48);
\draw[cell frame] (0,-0.96) rectangle (0.24,-0.72);
\draw[cell frame] (0.24,-0.96) rectangle (0.48,-0.72);
\draw[cell frame] (0.48,-0.96) rectangle (0.72,-0.72);
\draw[hl cell] (0.72,-0.96) rectangle (0.96,-0.72);
\draw[cell frame] (0.96,-0.96) rectangle (1.2,-0.72);
\draw[cell frame] (1.2,-0.96) rectangle (1.44,-0.72);
\draw[cell frame] (1.44,-0.96) rectangle (1.68,-0.72);
\draw[cell frame] (1.68,-0.96) rectangle (1.92,-0.72);
\draw[cell frame] (0,-1.2) rectangle (0.24,-0.96);
\draw[cell frame] (0.24,-1.2) rectangle (0.48,-0.96);
\draw[cell frame] (0.48,-1.2) rectangle (0.72,-0.96);
\draw[cell frame] (0.72,-1.2) rectangle (0.96,-0.96);
\draw[hl cell] (0.96,-1.2) rectangle (1.2,-0.96);
\draw[cell frame] (1.2,-1.2) rectangle (1.44,-0.96);
\draw[cell frame] (1.44,-1.2) rectangle (1.68,-0.96);
\draw[cell frame] (1.68,-1.2) rectangle (1.92,-0.96);
\draw[cell frame] (0,-1.44) rectangle (0.24,-1.2);
\draw[cell frame] (0.24,-1.44) rectangle (0.48,-1.2);
\draw[cell frame] (0.48,-1.44) rectangle (0.72,-1.2);
\draw[cell frame] (0.72,-1.44) rectangle (0.96,-1.2);
\draw[cell frame] (0.96,-1.44) rectangle (1.2,-1.2);
\draw[hl cell] (1.2,-1.44) rectangle (1.44,-1.2);
\draw[cell frame] (1.44,-1.44) rectangle (1.68,-1.2);
\draw[cell frame] (1.68,-1.44) rectangle (1.92,-1.2);
\draw[cell frame] (0,-1.68) rectangle (0.24,-1.44);
\draw[cell frame] (0.24,-1.68) rectangle (0.48,-1.44);
\draw[cell frame] (0.48,-1.68) rectangle (0.72,-1.44);
\draw[cell frame] (0.72,-1.68) rectangle (0.96,-1.44);
\draw[cell frame] (0.96,-1.68) rectangle (1.2,-1.44);
\draw[cell frame] (1.2,-1.68) rectangle (1.44,-1.44);
\draw[hl cell] (1.44,-1.68) rectangle (1.68,-1.44);
\draw[cell frame] (1.68,-1.68) rectangle (1.92,-1.44);
\draw[cell frame] (0,-1.92) rectangle (0.24,-1.68);
\draw[cell frame] (0.24,-1.92) rectangle (0.48,-1.68);
\draw[cell frame] (0.48,-1.92) rectangle (0.72,-1.68);
\draw[cell frame] (0.72,-1.92) rectangle (0.96,-1.68);
\draw[cell frame] (0.96,-1.92) rectangle (1.2,-1.68);
\draw[cell frame] (1.2,-1.92) rectangle (1.44,-1.68);
\draw[cell frame] (1.44,-1.92) rectangle (1.68,-1.68);
\draw[hl cell] (1.68,-1.92) rectangle (1.92,-1.68);
\node[lab] at (2.01,-0.88) {$+$};
\draw[hl cell] (2.26,-1.76) rectangle (2.7,0);
\node[lab] at (2.48,-2.06) {$U$};
\draw[hl cell] (2.95,-0.44) rectangle (4.71,0);
\node[lab] at (3.83,-0.74) {$V^{\mathsf T}$};
\node[lab] at (0.88,-2.06) {$D$};
\end{tikzpicture}
\end{center}
```

Diagonal plus low rank, $D+UV^{\mathsf T}$ with $U,V\in\mathbb R^{n\times k}$, $k\ll n$. The matrix inversion lemma solves it with diagonal solves and one $k\times k$ system, in $O(nk^2)$ flops instead of $O(n^3)$.

:::

::: {#rmk-structured-linear-equations-1 .remark name="Sparse factorizations"}

For sparse $A$, the cost of sparse LU or Cholesky depends on the ordering of rows and columns, chosen to limit fill-in; it can be far below $n^3$ and is often roughly linear in $n$ for banded or tree-like sparsity.

:::
