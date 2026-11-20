---
title: "The Spectral Theorem"
sources: [camib-la-8, mit1806-25]
requires: [math/linear-algebra/inner-product-spaces/adjoints-and-isometries, math/linear-algebra/endomorphisms/eigenvalues-of-endomorphisms]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 8.4, in our own wording; examples ours (checked with sympy); proofs written out in steps. MIT 18.06 proves the spectral theorem for real symmetric matrices (thm-symmetric-real-eigenvalues, thm-spectral-theorem) and states the Hermitian and unitary facts (thm-hermitian-real-eigenvalues); the versions here are for self-adjoint and unitary maps on any finite-dimensional inner product space and carry generalizes=. Merges proposed to the owner. -->

<!-- Merged 2026-11-20 (owner): thm-symmetric-real-eigenvalues and thm-spectral-theorem (18.06 L25) merged into lem-self-adjoint-eigenvalues and cor-real-symmetric-orthogonally-diagonalisable, which gained the rank-one form sum lambda_i q_i q_i^T. -->

Throughout, $V$ is a finite-dimensional inner product space over $F=\mathbb R$ or $\mathbb C$, and $\alpha\in\operatorname{End}(V)$.

::: {#lem-self-adjoint-eigenvalues .lemma name="Eigenvalues of a self-adjoint map"}

If $\alpha$ is self-adjoint, then

1. every eigenvalue of $\alpha$ is real, and $\chi_\alpha$ has only real roots (even when $F=\mathbb R$, as a polynomial over $\mathbb C$);
2. eigenvectors for distinct eigenvalues are orthogonal.

:::

::: {.proof}

1. If $\alpha v=\lambda v$ with $v\ne0$, then $\lambda\lVert v\rVert^2=\langle\alpha v,v\rangle=\langle v,\alpha v\rangle=\bar\lambda\lVert v\rVert^2$, so $\lambda=\bar\lambda$.

2. For the roots of $\chi_\alpha$: in an orthonormal basis $[\alpha]=A$ with $A=A^{\mathsf H}$ (@thm-adjoint-exists). A complex root of $\chi_A$ is an eigenvalue of $\mathbf z\mapsto A\mathbf z$ on $\mathbb C^n$, which is self-adjoint for the standard inner product, so the root is real by step 1.

3. If $\alpha v=\lambda v$ and $\alpha w=\mu w$ with $\lambda\ne\mu$ (both real), then $\lambda\langle v,w\rangle=\langle\alpha v,w\rangle=\langle v,\alpha w\rangle=\mu\langle v,w\rangle$, so $\langle v,w\rangle=0$.

:::

::: {#lem-invariant-complement .lemma name="Invariant subspaces and adjoints"}

If $W\le V$ is $\alpha$-invariant ($\alpha W\subseteq W$), then $W^\perp$ is $\alpha^*$-invariant.

:::

::: {.proof}

If $v\in W^\perp$ and $w\in W$, then $\langle\alpha^*v,w\rangle=\langle v,\alpha w\rangle=0$ since $\alpha w\in W$. So $\alpha^*v\in W^\perp$.

:::

::: {#thm-spectral-theorem-self-adjoint .theorem name="Spectral theorem for self-adjoint maps"}

If $\alpha\in\operatorname{End}(V)$ is self-adjoint, then $V$ has an orthonormal basis of eigenvectors of $\alpha$, and all eigenvalues are real. Equivalently, $V$ is the orthogonal direct sum of the eigenspaces of $\alpha$.

:::

::: {.proof}

Induction on $n=\dim V$; $n=0$ is trivial.

1. By @lem-self-adjoint-eigenvalues, $\chi_\alpha$ has a root $\lambda$, and $\lambda\in\mathbb R\subseteq F$. By @prp-eigenvalue-iff-root it is an eigenvalue of $\alpha$; take an eigenvector $e_1$ with $\lVert e_1\rVert=1$.

2. $W=\langle e_1\rangle$ is $\alpha$-invariant, so $W^\perp$ is $\alpha^*=\alpha$-invariant (@lem-invariant-complement), and $\alpha|_{W^\perp}$ is self-adjoint for the restricted inner product. $\dim W^\perp=n-1$ (@thm-orthogonal-complement).

3. By induction $W^\perp$ has an orthonormal basis $e_2,\dots,e_n$ of eigenvectors. Together with $e_1\perp W^\perp$ this is an orthonormal basis of $V$ of eigenvectors.

4. Grouping the basis by eigenvalue gives the orthogonal decomposition into eigenspaces (orthogonal by @lem-self-adjoint-eigenvalues).

:::

::: {#cor-real-symmetric-orthogonally-diagonalisable .corollary name="Matrix forms"}

1. For every real symmetric $A$ there is $P\in O(n)$ with $P^{\mathsf T}AP=P^{-1}AP=\Lambda$ diagonal and real. Equivalently, with $\mathbf q_i$ the columns of $P$ (orthonormal eigenvectors),
$$A=P\Lambda P^{\mathsf T}=\lambda_1\mathbf q_1\mathbf q_1^{\mathsf T}+\dots+\lambda_n\mathbf q_n\mathbf q_n^{\mathsf T}.$$
2. For every Hermitian $A$ there is $P\in U(n)$ with $P^{\mathsf H}AP=P^{-1}AP$ diagonal and real.

:::

::: {.proof}

Apply @thm-spectral-theorem-self-adjoint to $\mathbf x\mapsto A\mathbf x$ on $\mathbb R^n$ or $\mathbb C^n$ with the standard inner product, and let the columns of $P$ be the orthonormal eigenvectors. $P$ is orthogonal or unitary by @thm-isometry-characterisations. The sum of rank-one matrices is $(P\Lambda)P^{\mathsf T}$ multiplied as columns times rows (@thm-four-ways-to-multiply).

:::

Since $P^{\mathsf T}=P^{-1}$, the diagonalisation is a similarity and a congruence at once. So for a real symmetric form, the numbers $p$ and $q$ of Sylvester's law (@thm-sylvester-law-of-inertia) are the numbers of positive and negative eigenvalues of any matrix representing it in an orthonormal basis.

::: {#cor-simultaneous-diagonalisation-forms .corollary name="Diagonalising two forms at once"}

Let $\phi,\psi$ be symmetric bilinear forms on a finite-dimensional real vector space $V$, with $\phi$ positive definite. There is a basis $v_1,\dots,v_n$ with $\phi(v_i,v_j)=\delta_{ij}$ and $\psi(v_i,v_j)=0$ for $i\ne j$. In matrix form: if $A$ is positive definite and $B$ symmetric, there is an invertible $Q$ with $Q^{\mathsf T}AQ=I$ and $Q^{\mathsf T}BQ$ diagonal.

:::

::: {.proof}

1. $\phi$ is an inner product on $V$. By @lem-riesz-finite-dimensional, for each $w$ the functional $\psi(\cdot,w)$ is $\phi(\cdot,\beta w)$ for a unique $\beta w$; this defines $\beta\in\operatorname{End}(V)$ (linear by the same argument as in @thm-adjoint-exists).

2. $\beta$ is self-adjoint for $\phi$: $\phi(v,\beta w)=\psi(v,w)=\psi(w,v)=\phi(w,\beta v)=\phi(\beta v,w)$.

3. By @thm-spectral-theorem-self-adjoint there is a $\phi$-orthonormal basis $v_i$ with $\beta v_i=\lambda_iv_i$. Then $\psi(v_i,v_j)=\phi(v_i,\beta v_j)=\lambda_j\delta_{ij}$.

4. For matrices, take $V=\mathbb R^n$, $\phi(\mathbf x,\mathbf y)=\mathbf x^{\mathsf T}A\mathbf y$, $\psi(\mathbf x,\mathbf y)=\mathbf x^{\mathsf T}B\mathbf y$, and $Q=[v_1\ \cdots\ v_n]$.

:::

The diagonal entries of $Q^{\mathsf T}BQ$ are the roots of $\det(B-tA)=0$, since $\det(Q^{\mathsf T}(B-tA)Q)=\prod_i(\lambda_i-t)$. This is the setting of small oscillations in mechanics, with $A$ the kinetic and $B$ the potential energy.

::: {#thm-unitary-diagonalisable .theorem name="Unitary maps are diagonalisable" generalizes="thm-hermitian-real-eigenvalues"}

If $V$ is a complex inner product space and $\alpha\in U(V)$, then $V$ has an orthonormal basis of eigenvectors of $\alpha$, and every eigenvalue satisfies $\lvert\lambda\rvert=1$.

:::

::: {.proof}

1. If $\alpha v=\lambda v$ with $v\ne0$, then $\lVert v\rVert=\lVert\alpha v\rVert=\lvert\lambda\rvert\lVert v\rVert$ (@thm-isometry-characterisations), so $\lvert\lambda\rvert=1$.

2. Induction on $\dim V$. Over $\mathbb C$, $\chi_\alpha$ has a root, so $\alpha$ has a unit eigenvector $e_1$ with eigenvalue $\lambda$. $W=\langle e_1\rangle$ is invariant under $\alpha$ and under $\alpha^{-1}=\alpha^*$ (since $\alpha^{-1}e_1=\lambda^{-1}e_1$).

3. By @lem-invariant-complement applied to $\alpha^*$ (whose adjoint is $\alpha$), $W^\perp$ is $\alpha$-invariant. $\alpha|_{W^\perp}$ is still an isometry, so by induction $W^\perp$ has an orthonormal basis of eigenvectors; add $e_1$.

:::

Over $\mathbb R$ this fails: a rotation of the plane by an angle other than $0$ or $\pi$ has no real eigenvector. The same proof works for every *normal* map ($\alpha\alpha^*=\alpha^*\alpha$) over $\mathbb C$.

::: {#exm-spectral-theorem .example name="Orthogonal diagonalisation and two forms"}

1. $A=\begin{bmatrix}2&1\\1&2\end{bmatrix}$ has eigenvalues $3$ and $1$ with unit eigenvectors $\frac1{\sqrt2}(1,1)^{\mathsf T}$ and $\frac1{\sqrt2}(1,-1)^{\mathsf T}$, which are orthogonal. With $P$ having these columns, $P^{\mathsf T}AP=\operatorname{diag}(3,1)$; the form $2x^2+2xy+2y^2$ is positive definite ($p=2$).
2. Take $A=\operatorname{diag}(1,4)$ (positive definite) and $B=\begin{bmatrix}0&1\\1&0\end{bmatrix}$. $\det(B-tA)=4t^2-1$ has roots $\pm\frac12$. The vectors $v_1=\frac1{\sqrt2}(1,\frac12)^{\mathsf T}$ and $v_2=\frac1{\sqrt2}(1,-\frac12)^{\mathsf T}$ satisfy $v_i^{\mathsf T}Av_j=\delta_{ij}$ and $Q^{\mathsf T}BQ=\operatorname{diag}(\frac12,-\frac12)$ for $Q=[v_1\ v_2]$.

:::
