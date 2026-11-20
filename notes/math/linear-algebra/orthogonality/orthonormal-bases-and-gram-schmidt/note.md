---
title: "Orthogonal Matrices and Gram–Schmidt"
sources: [mit1806-17]
requires: [math/linear-algebra/orthogonality/least-squares]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 17, in our own wording; proofs written out in steps. Example numbers checked with sympy. -->

::: {#def-orthonormal-vectors .definition name="Orthonormal vectors"}

Vectors $\mathbf{q}_1,\dots,\mathbf{q}_n$ are *orthonormal* if
$$\mathbf{q}_i^{\mathsf T}\mathbf{q}_j=\begin{cases}0&i\neq j,\\1&i=j.\end{cases}$$
If $Q$ has these vectors as columns, this says $Q^{\mathsf T}Q=I$.

:::

Orthonormal vectors are independent: taking the dot product of $\sum c_j\mathbf{q}_j=\mathbf{0}$ with $\mathbf{q}_i$ gives $c_i=0$.

::: {#def-orthogonal-matrix .definition name="Orthogonal matrix"}

A *square* matrix $Q$ with orthonormal columns is an *orthogonal matrix*. Then $Q^{\mathsf T}=Q^{-1}$, so also $QQ^{\mathsf T}=I$ and the rows are orthonormal.

:::

Examples: permutation matrices (@prp-permutation-inverse-transpose); rotations $\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}$; the Hadamard-type matrix $\frac12\begin{bmatrix}1&1&1&1\\1&-1&1&-1\\1&1&-1&-1\\1&-1&-1&1\end{bmatrix}$.

::: {#prp-orthonormal-columns-preserve-length .proposition name="Q preserves lengths and dot products"}

If $Q^{\mathsf T}Q=I$ then $\lVert Q\mathbf{x}\rVert=\lVert\mathbf{x}\rVert$ and $(Q\mathbf{x})^{\mathsf T}(Q\mathbf{y})=\mathbf{x}^{\mathsf T}\mathbf{y}$.

:::

::: {.proof}

1. $(Q\mathbf{x})^{\mathsf T}(Q\mathbf{y})=\mathbf{x}^{\mathsf T}Q^{\mathsf T}Q\mathbf{y}=\mathbf{x}^{\mathsf T}\mathbf{y}$.

2. Taking $\mathbf{y}=\mathbf{x}$ gives the statement about lengths.

:::

::: {#prp-projection-with-orthonormal-columns .proposition name="Projections are easy with orthonormal columns"}

If $Q$ has orthonormal columns, the projection onto $C(Q)$ is
$$P=QQ^{\mathsf T},\qquad P\mathbf{b}=(\mathbf{q}_1^{\mathsf T}\mathbf{b})\mathbf{q}_1+\dots+(\mathbf{q}_n^{\mathsf T}\mathbf{b})\mathbf{q}_n,$$
and the normal equations become $\hat{\mathbf{x}}=Q^{\mathsf T}\mathbf{b}$.

:::

::: {.proof}

1. In @thm-projection-onto-subspace, $A^{\mathsf T}A=Q^{\mathsf T}Q=I$, so $\hat{\mathbf{x}}=Q^{\mathsf T}\mathbf{b}$ and $P=QQ^{\mathsf T}$.

2. Component $i$ of $Q^{\mathsf T}\mathbf{b}$ is $\mathbf{q}_i^{\mathsf T}\mathbf{b}$, and $Q\hat{\mathbf{x}}=\sum_i\hat x_i\mathbf{q}_i$.

:::

<!-- Merged 2026-11-20 (owner): the block def-gram-schmidt was removed in favour of thm-gram-schmidt-abstract (Cambridge IB Linear Algebra), which states it for any field or inner product space with a full proof. -->

**The Gram–Schmidt process.** Given independent vectors $\mathbf{a}_1,\dots,\mathbf{a}_n$, put for $k=1,\dots,n$
$$\mathbf{A}_k=\mathbf{a}_k-\sum_{j<k}(\mathbf{q}_j^{\mathsf T}\mathbf{a}_k)\,\mathbf{q}_j,\qquad \mathbf{q}_k=\frac{\mathbf{A}_k}{\lVert\mathbf{A}_k\rVert}.$$
Each step subtracts from $\mathbf{a}_k$ its projection onto the span of the earlier $\mathbf{q}$'s and normalises what is left. The $\mathbf q_k$ are orthonormal and $\mathbf q_1,\dots,\mathbf q_k$ span the same space as $\mathbf a_1,\dots,\mathbf a_k$; this is @thm-gram-schmidt-abstract (with the dot product $\langle\mathbf a,\mathbf q\rangle=\mathbf q^{\mathsf T}\mathbf a$), which also gives the pseudocode.

::: {#fig-orthonormal-bases-and-gram-schmidt-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, emph] (0.000,0.000) -- (2.600,0.500);
\node[lab, right] at (2.600,0.500) {$\mathbf a_1$};
\draw[->, emph] (0.000,0.000) -- (1.200,1.800);
\node[lab, above] at (1.200,1.800) {$\mathbf a_2$};
\draw[->, faint] (0.000,0.000) -- (1.491,0.287);
\draw[dashed] (1.491,0.287) -- (1.200,1.800);
\draw[->, hl] (0.000,0.000) -- (-0.291,1.513);
\node[lab, above left] at (-0.291,1.513) {$\mathbf A_2$};
\draw[->, hl] (0.000,0.000) -- (0.982,0.189);
\node[lab, below] at (0.982,0.189) {$\mathbf q_1$};
\end{tikzpicture}
\end{center}
```

One Gram–Schmidt step: subtract from $\mathbf a_2$ its projection on $\mathbf q_1$; what is left, $\mathbf A_2$, is perpendicular to $\mathbf q_1$.

:::

<!-- Merged 2026-11-20 (owner): the block thm-gram-schmidt was removed in favour of thm-gram-schmidt-abstract (Cambridge IB Linear Algebra), which states it for any field or inner product space with a full proof. -->

::: {#thm-qr-factorization .theorem name="A = QR"}

If $A$ is $m\times n$ with independent columns, then $A=QR$, where $Q$ is $m\times n$ with orthonormal columns and $R=Q^{\mathsf T}A$ is $n\times n$, upper triangular and invertible.

:::

::: {.proof}

1. Run Gram–Schmidt on the columns of $A$. By @thm-gram-schmidt-abstract, $\mathbf{a}_k$ is a combination of $\mathbf{q}_1,\dots,\mathbf{q}_k$, namely $\mathbf{a}_k=\sum_{j\le k}(\mathbf{q}_j^{\mathsf T}\mathbf{a}_k)\mathbf{q}_j$.

2. So $A=QR$ with $r_{jk}=\mathbf{q}_j^{\mathsf T}\mathbf{a}_k$ for $j\le k$ and $r_{jk}=0$ for $j>k$, i.e. $R=Q^{\mathsf T}A$ is upper triangular.

3. Its diagonal entries $r_{kk}=\mathbf{q}_k^{\mathsf T}\mathbf{a}_k=\lVert\mathbf{A}_k\rVert>0$, so $R$ is invertible.

:::

::: {#exm-gram-schmidt-three-vectors .example name="Gram–Schmidt in R^3"}

Start with $\mathbf{a}_1=(1,1,0)$, $\mathbf{a}_2=(1,0,1)$, $\mathbf{a}_3=(0,1,1)$.

1. $\mathbf{q}_1=\frac1{\sqrt2}(1,1,0)$.
2. $\mathbf{A}_2=(1,0,1)-\frac12(1,1,0)=\frac12(1,-1,2)$, so $\mathbf{q}_2=\frac1{\sqrt6}(1,-1,2)$.
3. $\mathbf{A}_3=(0,1,1)-\frac12(1,1,0)-\frac16(1,-1,2)=\frac23(-1,1,1)$, so $\mathbf{q}_3=\frac1{\sqrt3}(-1,1,1)$.

Then $R=Q^{\mathsf T}A=\begin{bmatrix}\sqrt2&1/\sqrt2&1/\sqrt2\\0&\sqrt6/2&1/\sqrt6\\0&0&2/\sqrt3\end{bmatrix}$.

:::

With $A=QR$, least squares becomes $R\hat{\mathbf{x}}=Q^{\mathsf T}\mathbf{b}$, solved by back substitution.
