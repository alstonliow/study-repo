---
title: "Diagonalization and Powers of A"
sources: [mit1806-22]
requires: [math/linear-algebra/eigenvalues/eigenvalues-and-eigenvectors]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 22, in our own wording; proofs written out in steps. Example numbers checked with sympy. -->

::: {#thm-diagonalization .theorem name="Diagonalization"}

Suppose the $n\times n$ matrix $A$ has $n$ independent eigenvectors $\mathbf{x}_1,\dots,\mathbf{x}_n$ with eigenvalues $\lambda_1,\dots,\lambda_n$. Put them as the columns of the *eigenvector matrix* $S$ and let $\Lambda=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$. Then
$$AS=S\Lambda,\qquad A=S\Lambda S^{-1},\qquad A^k=S\Lambda^kS^{-1}.$$

:::

::: {.proof}

1. Column $j$ of $AS$ is $A\mathbf{x}_j=\lambda_j\mathbf{x}_j$, which is column $j$ of $S\Lambda$.

2. The columns of $S$ are independent, so $S$ is invertible (@prp-independence-and-nullspace); multiply on the right by $S^{-1}$.

3. $A^k=(S\Lambda S^{-1})(S\Lambda S^{-1})\cdots=S\Lambda^kS^{-1}$, since the inner factors $S^{-1}S$ cancel.

:::

::: {#thm-distinct-eigenvalues-independent .theorem name="Distinct eigenvalues give independent eigenvectors"}

Eigenvectors belonging to different eigenvalues are linearly independent. In particular, if the $n$ eigenvalues of $A$ are distinct, $A$ is diagonalizable.

:::

::: {.proof}

1. Suppose the claim is false, and take a shortest dependent list $\mathbf{x}_1,\dots,\mathbf{x}_k$ of eigenvectors with distinct eigenvalues: $c_1\mathbf{x}_1+\dots+c_k\mathbf{x}_k=\mathbf{0}$ with all $c_i\neq0$ (otherwise a shorter list would be dependent), and $k\ge2$ since eigenvectors are nonzero.

2. Apply $A-\lambda_kI$: $(A-\lambda_kI)\mathbf{x}_i=(\lambda_i-\lambda_k)\mathbf{x}_i$, so $\sum_{i<k}c_i(\lambda_i-\lambda_k)\mathbf{x}_i=\mathbf{0}$.

3. The coefficients $c_i(\lambda_i-\lambda_k)$ are nonzero for $i<k$, which gives a shorter dependent list, a contradiction.

:::

::: {#rmk-diagonalization-1 .remark name="Repeated eigenvalues"}

With a repeated eigenvalue there may be too few eigenvectors. $A=\begin{bmatrix}2&1\\0&2\end{bmatrix}$ has $\lambda=2$ twice, but $N(A-2I)$ is only the line through $(1,0)$. Such a matrix cannot be diagonalized (@sec-math-linear-algebra-eigenvalues-similar-matrices-and-jordan-form). The *algebraic multiplicity* (as a root) can exceed the *geometric multiplicity* ($\dim N(A-\lambda I)$), never the other way round.

:::

::: {#cor-powers-and-difference-equations .corollary name="Difference equations"}

If $A$ is diagonalizable and $\mathbf{u}_{k+1}=A\mathbf{u}_k$, write $\mathbf{u}_0=c_1\mathbf{x}_1+\dots+c_n\mathbf{x}_n$ (that is, $\mathbf{c}=S^{-1}\mathbf{u}_0$). Then
$$\mathbf{u}_k=A^k\mathbf{u}_0=c_1\lambda_1^k\mathbf{x}_1+\dots+c_n\lambda_n^k\mathbf{x}_n.$$
Hence $A^k\to0$ as $k\to\infty$ exactly when every $\lvert\lambda_i\rvert<1$.

:::

::: {.proof}

1. $A^k\mathbf{x}_i=\lambda_i^k\mathbf{x}_i$, by applying $A\mathbf{x}_i=\lambda_i\mathbf{x}_i$ $k$ times; then use linearity.

2. $\lambda_i^k\to0$ for all $i$ iff every $\lvert\lambda_i\rvert<1$; since the $\mathbf{x}_i$ are independent, $A^k\mathbf{u}_0\to\mathbf{0}$ for every $\mathbf{u}_0$ iff this holds.

:::

::: {#exm-fibonacci-by-eigenvalues .example name="Fibonacci numbers"}

The rule $F_{k+2}=F_{k+1}+F_k$ becomes $\mathbf{u}_{k+1}=A\mathbf{u}_k$ with $\mathbf{u}_k=(F_{k+1},F_k)$ and $A=\begin{bmatrix}1&1\\1&0\end{bmatrix}$. The eigenvalues solve $\lambda^2-\lambda-1=0$:
$$\lambda_1=\frac{1+\sqrt5}2\approx1.618,\qquad\lambda_2=\frac{1-\sqrt5}2\approx-0.618,$$
with eigenvectors $(\lambda_i,1)$. From $\mathbf{u}_0=(1,0)=\frac{1}{\lambda_1-\lambda_2}\big((\lambda_1,1)-(\lambda_2,1)\big)$,
$$F_k=\frac{\lambda_1^k-\lambda_2^k}{\sqrt5}.$$
Since $\lvert\lambda_2\rvert<1$, $F_k$ is the integer nearest to $\lambda_1^k/\sqrt5$, and $F_{k+1}/F_k\to\lambda_1$. For example $F_{10}=55$ and $\lambda_1^{10}/\sqrt5\approx55.004$.

:::

::: {#fig-diagonalization-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.38]
\draw[->] (-4.5,0) -- (14.5,0) node[lab, right] {$F_{k+1}$};
\draw[->] (0,-2) -- (0,9.5) node[lab, above] {$F_k$};
\draw[emph, primary] (-3.2,-2) -- (14,8.65) node[lab, right] {$(\lambda_1,1)$};
\draw[emph, muted, dashed] (1.24,-2) -- (-4.3,6.96) node[lab, above] {$(\lambda_2,1)$};
\draw[faint] (1,0) -- (1,1) -- (2,1) -- (3,2) -- (5,3) -- (8,5) -- (13,8);
\foreach \p/\k in {(1,0)/0,(1,1)/1,(2,1)/2,(3,2)/3,(5,3)/4,(8,5)/5,(13,8)/6} \node[hl dot] at \p {};
\node[lab, below] at (1,0) {$\mathbf u_0$};
\node[lab, below right] at (13,8) {$\mathbf u_6$};
\end{tikzpicture}
\end{center}
```

The vectors $\mathbf u_k=(F_{k+1},F_k)$ of @exm-fibonacci-by-eigenvalues. The component along $(\lambda_2,1)$ shrinks like $\lambda_2^k$, so the points line up along the eigenvector $(\lambda_1,1)$ and $F_{k+1}/F_k\to\lambda_1$.

:::
