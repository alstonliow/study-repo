---
title: "Markov Matrices"
sources: [mit1806-24]
requires: [math/linear-algebra/eigenvalues/diagonalization]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 24 (first half), in our own wording; proofs written out in steps. Example numbers checked with sympy. The probabilistic side (Markov chains, invariant distributions, convergence) is in math/probability/markov-chains, which uses row vectors and rows that sum to 1; this note is the eigenvalue side, with columns that sum to 1 as in 18.06. -->

::: {#def-markov-matrix .definition name="Markov matrix" related="def-markov-chain"}

A square matrix $A$ is a *Markov matrix* if all its entries are $\ge0$ and each column sums to $1$. Then $\mathbf{u}_{k+1}=A\mathbf{u}_k$ moves a distribution $\mathbf{u}_k$ (entries $\ge0$, summing to $1$) to another distribution. Its transpose is the transition matrix $P$ of @def-markov-chain.

:::

::: {#thm-markov-eigenvalue-one .theorem name="Eigenvalues of a Markov matrix"}

Let $A$ be a Markov matrix.

1. $\lambda=1$ is an eigenvalue of $A$.
2. Every eigenvalue satisfies $\lvert\lambda\rvert\le1$.
3. If all entries of $A$ are positive, then $\lambda=1$ has a one-dimensional eigenspace, spanned by a vector $\mathbf{x}_1$ with positive entries, and every other eigenvalue has $\lvert\lambda\rvert<1$.

:::

::: {.proof}

1. The columns of $A-I$ sum to $0$, so the rows of $A-I$ add to the zero row: $(1,\dots,1)$ is in $N((A-I)^{\mathsf T})$. Hence $A-I$ is singular and $1$ is an eigenvalue.

2. Eigenvalues of $A$ are eigenvalues of $A^{\mathsf T}$ (@cor-determinant-inverse-transpose applied to $A-\lambda I$). Let $A^{\mathsf T}\mathbf{y}=\lambda\mathbf{y}$ and let $\lvert y_i\rvert$ be the largest $\lvert y_j\rvert$. Row $i$ of $A^{\mathsf T}$ has entries $\ge0$ summing to $1$, so $\lvert\lambda\rvert\lvert y_i\rvert=\lvert\sum_ja_{ji}y_j\rvert\le\sum_ja_{ji}\lvert y_i\rvert=\lvert y_i\rvert$.

3. With positive entries, equality in step 2 needs every $y_j$ equal to $y_i$ in modulus and in phase, so $\mathbf{y}$ is a multiple of $(1,\dots,1)$ and $\lambda=1$. Hence $\lambda\neq1$ forces $\lvert\lambda\rvert<1$, and the eigenspace of $A^{\mathsf T}$ (so also of $A$, by @thm-fundamental-theorem-dimensions applied to $A-I$) for $\lambda=1$ is one-dimensional. Positivity of $\mathbf{x}_1$ is the Perron–Frobenius theorem, which we use without proof.

:::

::: {#cor-markov-steady-state .corollary name="Steady state" related="thm-markov-convergence"}

If $A$ is a Markov matrix with positive entries and is diagonalizable, then for every starting distribution $\mathbf{u}_0$, $A^k\mathbf{u}_0\to\mathbf{x}_1$, the eigenvector for $\lambda=1$ scaled so that its entries sum to $1$ (the *steady state*).

:::

::: {.proof}

1. By @cor-powers-and-difference-equations, $A^k\mathbf{u}_0=c_1\mathbf{x}_1+\sum_{i\ge2}c_i\lambda_i^k\mathbf{x}_i$, and the sum tends to $\mathbf{0}$ because $\lvert\lambda_i\rvert<1$ (@thm-markov-eigenvalue-one).

2. Each $A^k\mathbf{u}_0$ has entries summing to $1$ (multiplying by $A$ preserves the sum, since $(1,\dots,1)A=(1,\dots,1)$), so the limit $c_1\mathbf{x}_1$ does too. With $\mathbf{x}_1$ normalised, $c_1=1$.

:::

The assumption "diagonalizable" can be dropped; @thm-markov-convergence proves convergence by probability.

::: {#exm-markov-two-states .example name="Two cities"}

Each year $10\%$ of the population of city $A$ moves to $B$ and $20\%$ of $B$ moves to $A$:
$$\begin{bmatrix}a_{k+1}\\b_{k+1}\end{bmatrix}=\begin{bmatrix}0.9&0.2\\0.1&0.8\end{bmatrix}\begin{bmatrix}a_k\\b_k\end{bmatrix}.$$
The eigenvalues are $1$ and $0.7$ (the trace is $1.7$). The eigenvector for $1$ is $(2,1)$, so the steady state is $(\frac23,\frac13)$; the eigenvector for $0.7$ is $(1,-1)$. Starting from $(1,0)=\frac13(2,1)+\frac13(1,-1)$,
$$\mathbf{u}_k=\tfrac13(2,1)+\tfrac13(0.7)^k(1,-1)\to(\tfrac23,\tfrac13).$$

:::

::: {#fig-markov-matrices-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[ball] (A) at (0,0) {$A$};
\node[ball] (B) at (3.2,0) {$B$};
\draw[->] (A) to[bend left=25] node[edge label, above] {$0.1$} (B);
\draw[->] (B) to[bend left=25] node[edge label, below] {$0.2$} (A);
\draw[->] (A) to[out=150, in=210, looseness=6] node[edge label, left] {$0.9$} (A);
\draw[->] (B) to[out=30, in=-30, looseness=6] node[edge label, right] {$0.8$} (B);
\end{tikzpicture}
\end{center}
```

The two cities of @exm-markov-two-states. The numbers leaving each city add to $1$ (a column of the Markov matrix). In the steady state $(\frac23,\frac13)$ the two flows balance: $0.1\cdot\frac23=0.2\cdot\frac13$.

:::
