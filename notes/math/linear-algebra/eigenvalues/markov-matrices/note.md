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

::: {#fig-markov-matrices-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell, fill=primaryLight] (0.000,0.400) rectangle (0.700,1.100);
\node[lab] at (0.350,0.750) {$0.9$};
\draw[hl cell] (0.700,0.400) rectangle (1.400,1.100);
\node[lab] at (1.050,0.750) {$0.2$};
\draw[cell, fill=primaryLight] (0.000,-0.300) rectangle (0.700,0.400);
\node[lab] at (0.350,0.050) {$0.1$};
\draw[hl cell] (0.700,-0.300) rectangle (1.400,0.400);
\node[lab] at (1.050,0.050) {$0.8$};
\node[lab, note, anchor=west, align=left] at (1.8,0.55) {entries $\ge0$, each column sums to $1$:\\column $j$ says where the people\\in state $j$ go};
\end{tikzpicture}
\end{center}
```

The Markov matrix of @exm-markov-two-states. Because each column sums to $1$, the total population $a_k+b_k$ stays the same from year to year.

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

::: {#fig-markov-matrices-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0,0) circle[radius=1.4];
\draw[->, muted] (-1.7,0) -- (1.8,0); \draw[->, muted] (0,-1.6) -- (0,1.6);
\fill[accent] (1.4,0) circle[pt] node[above right, lab] {$1$}; \fill[primary] (0.98,0) circle[pt] node[above left, lab] {$0.7$};
\node[lab, note, anchor=west, align=left] at (2.1,0.3) {every eigenvalue of a Markov matrix\\has $\lvert\lambda\rvert\le1$, and $\lambda=1$ is one of them};
\end{tikzpicture}
\end{center}
```

The eigenvalues of the matrix in @exm-markov-two-states inside the unit disc. $\lambda=1$ gives the steady state; the components for eigenvalues of size less than $1$ die out.

:::

::: {#cor-markov-steady-state .corollary name="Steady state" related="thm-markov-convergence"}

If $A$ is a Markov matrix with positive entries and is diagonalizable, then for every starting distribution $\mathbf{u}_0$, $A^k\mathbf{u}_0\to\mathbf{x}_1$, the eigenvector for $\lambda=1$ scaled so that its entries sum to $1$ (the *steady state*).

:::

::: {.proof}

1. By @cor-powers-and-difference-equations, $A^k\mathbf{u}_0=c_1\mathbf{x}_1+\sum_{i\ge2}c_i\lambda_i^k\mathbf{x}_i$, and the sum tends to $\mathbf{0}$ because $\lvert\lambda_i\rvert<1$ (@thm-markov-eigenvalue-one).

2. Each $A^k\mathbf{u}_0$ has entries summing to $1$ (multiplying by $A$ preserves the sum, since $(1,\dots,1)A=(1,\dots,1)$), so the limit $c_1\mathbf{x}_1$ does too. With $\mathbf{x}_1$ normalised, $c_1=1$.

:::

::: {#fig-markov-matrices-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[y={(0,2.4cm)}]
\draw[->, muted] (0,0) -- (6.3,0) node[right, lab, tick] {$k$}; \draw[->, muted] (0,0) -- (0,1.15);
\draw[faint, dashed] (0,0.667) -- (6,0.667) node[right, lab, tick] {$\frac23$}; \draw[faint, dashed] (0,0.333) -- (6,0.333) node[right, lab, tick] {$\frac13$};
\draw[faint] (0,1) -- (-0.1,1) node[left, lab, tick] {$1$};
\fill[primary] (0.00,1.000) circle[pt]; \fill[accent] (0.00,0.000) circle[pt];
\fill[primary] (0.45,0.900) circle[pt]; \fill[accent] (0.45,0.100) circle[pt];
\fill[primary] (0.90,0.830) circle[pt]; \fill[accent] (0.90,0.170) circle[pt];
\fill[primary] (1.35,0.781) circle[pt]; \fill[accent] (1.35,0.219) circle[pt];
\fill[primary] (1.80,0.747) circle[pt]; \fill[accent] (1.80,0.253) circle[pt];
\fill[primary] (2.25,0.723) circle[pt]; \fill[accent] (2.25,0.277) circle[pt];
\fill[primary] (2.70,0.706) circle[pt]; \fill[accent] (2.70,0.294) circle[pt];
\fill[primary] (3.15,0.694) circle[pt]; \fill[accent] (3.15,0.306) circle[pt];
\fill[primary] (3.60,0.686) circle[pt]; \fill[accent] (3.60,0.314) circle[pt];
\fill[primary] (4.05,0.680) circle[pt]; \fill[accent] (4.05,0.320) circle[pt];
\fill[primary] (4.50,0.676) circle[pt]; \fill[accent] (4.50,0.324) circle[pt];
\fill[primary] (4.95,0.673) circle[pt]; \fill[accent] (4.95,0.327) circle[pt];
\fill[primary] (5.40,0.671) circle[pt]; \fill[accent] (5.40,0.329) circle[pt];
\node[lab, note, primary] at (1.2,0.95) {$a_k$}; \node[lab, note, accent] at (1.2,0.08) {$b_k$};
\end{tikzpicture}
\end{center}
```

The populations of @exm-markov-two-states, starting with everyone in city $A$. The difference from the steady state $(\frac23,\frac13)$ shrinks by the factor $0.7$, the second eigenvalue, every year.

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
