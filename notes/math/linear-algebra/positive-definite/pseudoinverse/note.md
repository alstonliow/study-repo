---
title: "Left and Right Inverses and the Pseudoinverse"
sources: [mit1806-33]
requires: [math/linear-algebra/positive-definite/change-of-basis]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 33, in our own wording; proofs written out in steps. Example numbers checked with sympy. -->

::: {#prp-left-right-inverse .proposition name="Left and right inverses"}

Let $A$ be $m\times n$ with rank $r$.

1. If $r=n$ (independent columns), $A_{\text{left}}^{-1}=(A^{\mathsf T}A)^{-1}A^{\mathsf T}$ satisfies $A_{\text{left}}^{-1}A=I_n$.
2. If $r=m$ (independent rows), $A_{\text{right}}^{-1}=A^{\mathsf T}(AA^{\mathsf T})^{-1}$ satisfies $AA_{\text{right}}^{-1}=I_m$.

Multiplied in the other order, they give projections: $AA_{\text{left}}^{-1}$ projects onto $C(A)$ and $A_{\text{right}}^{-1}A$ projects onto the row space.

:::

::: {.proof}

1. $A^{\mathsf T}A$ is invertible when the columns are independent (@thm-ata-invertible), and $(A^{\mathsf T}A)^{-1}A^{\mathsf T}A=I$.

2. Apply step 1 to $A^{\mathsf T}$, which has independent columns when $r=m$, and transpose.

3. $AA_{\text{left}}^{-1}=A(A^{\mathsf T}A)^{-1}A^{\mathsf T}$ is the projection matrix of @thm-projection-onto-subspace; the other is the same formula for $A^{\mathsf T}$.

:::

When $r<m$ and $r<n$ neither one-sided inverse exists. But $A$ is still one-to-one from its row space onto its column space (@cor-orthogonal-decomposition), and that correspondence can be inverted.

::: {#def-pseudoinverse .definition name="Pseudoinverse"}

If $A=U\Sigma V^{\mathsf T}$ (@thm-svd), the *pseudoinverse* of $A$ is the $n\times m$ matrix
$$A^{+}=V\Sigma^{+}U^{\mathsf T}=\frac1{\sigma_1}\mathbf{v}_1\mathbf{u}_1^{\mathsf T}+\dots+\frac1{\sigma_r}\mathbf{v}_r\mathbf{u}_r^{\mathsf T},$$
where $\Sigma^{+}$ is $n\times m$ with $1/\sigma_1,\dots,1/\sigma_r$ on its diagonal.

:::

::: {#thm-pseudoinverse-properties .theorem name="What the pseudoinverse does"}

1. $A^{+}\mathbf{u}_i=\mathbf{v}_i/\sigma_i$ for $i\le r$ and $A^{+}\mathbf{u}_i=\mathbf{0}$ for $i>r$: $A^{+}$ inverts $A$ from $C(A)$ back to the row space, and sends $N(A^{\mathsf T})$ to $\mathbf{0}$.
2. $AA^{+}$ is the projection onto $C(A)$ and $A^{+}A$ is the projection onto $C(A^{\mathsf T})$.
3. If $A$ is invertible, $A^{+}=A^{-1}$; if $A$ has independent columns, $A^{+}=A_{\text{left}}^{-1}$.
4. $\mathbf{x}^{+}=A^{+}\mathbf{b}$ is the least squares solution of $A\mathbf{x}=\mathbf{b}$ (@def-least-squares-solution) of smallest length.

:::

::: {.proof}

1. $\mathbf{u}_j^{\mathsf T}\mathbf{u}_i$ is $1$ for $j=i$ and $0$ otherwise, so in the sum defining $A^{+}$ only the term $j=i$ survives (or none if $i>r$).

2. $AA^{+}=\sum_{i\le r}\mathbf{u}_i\mathbf{u}_i^{\mathsf T}$, using $\mathbf{v}_i^{\mathsf T}\mathbf{v}_j=\delta_{ij}$; this is the projection onto the span of $\mathbf{u}_1,\dots,\mathbf{u}_r$, which is $C(A)$ (@cor-svd-four-subspaces and @prp-projection-with-orthonormal-columns). Similarly $A^{+}A=\sum_{i\le r}\mathbf{v}_i\mathbf{v}_i^{\mathsf T}$.

3. For independent columns, $A^{+}A=I_n$ by step 2 (the row space is all of $\mathbb{R}^n$), and $A^{+}$ vanishes on $N(A^{\mathsf T})$, as does $A_{\text{left}}^{-1}=(A^{\mathsf T}A)^{-1}A^{\mathsf T}$. Both agree on $C(A)$ (they invert $A$ there), so they are equal. The invertible case is the special case $m=n=r$.

4. $A\mathbf{x}^{+}=AA^{+}\mathbf{b}$ is the projection of $\mathbf{b}$ onto $C(A)$, so $\mathbf{x}^{+}$ is a least squares solution (@thm-least-squares-normal-equations). Every least squares solution is $\mathbf{x}^{+}+\mathbf{x}_n$ with $\mathbf{x}_n\in N(A)$; since $\mathbf{x}^{+}$ lies in the row space, which is orthogonal to $N(A)$, $\lVert\mathbf{x}^{+}+\mathbf{x}_n\rVert^2=\lVert\mathbf{x}^{+}\rVert^2+\lVert\mathbf{x}_n\rVert^2$ (@prp-pythagoras-orthogonal).

:::

::: {#exm-pseudoinverse-rank-one .example name="Pseudoinverse of a rank one matrix"}

$A=\begin{bmatrix}1&2\\2&4\end{bmatrix}=5\,\mathbf{u}\mathbf{u}^{\mathsf T}$ with $\mathbf{u}=\frac1{\sqrt5}(1,2)$ is singular. Its SVD has $\sigma_1=5$, $\mathbf{u}_1=\mathbf{v}_1=\mathbf{u}$, so
$$A^{+}=\frac15\mathbf{u}\mathbf{u}^{\mathsf T}=\frac1{25}\begin{bmatrix}1&2\\2&4\end{bmatrix}.$$
For $\mathbf{b}=(5,0)$: $A^{+}\mathbf{b}=\frac15(1,2)$, and $A\,A^{+}\mathbf{b}=(1,2)$ is the projection of $\mathbf{b}$ onto the line $C(A)$.

:::
