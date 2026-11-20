---
title: "Trace, Determinant and Eigenvalues of an Endomorphism"
sources: [camib-la-6]
requires: [math/linear-algebra/endomorphisms/determinants-over-a-field]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 6.1, in our own wording; examples ours (checked with sympy); proofs written out in steps. MIT 18.06 covers similar matrices, eigenvalues and diagonalization for real and complex matrices (def-similar-matrices, def-eigenvalue, thm-distinct-eigenvalues-independent, thm-diagonalization); the basis-free versions here carry generalizes=. Merges proposed to the owner. -->

An *endomorphism* of $V$ is a linear map $\alpha:V\to V$; they form the space $\operatorname{End}(V)=\mathcal L(V,V)$, and $\iota$ denotes the identity. Throughout, $V$ is finite-dimensional over $F$ with $\dim V=n$, and an endomorphism is represented using the same basis $\mathcal B$ for input and output: $[\alpha]_{\mathcal B}=[\alpha]_{\mathcal B,\mathcal B}$.

::: {#prp-endomorphism-change-of-basis .proposition name="Similar matrices" generalizes="def-similar-matrices"}

If $P$ is the change of basis matrix from $\mathcal B$ to $\mathcal B'$, then $[\alpha]_{\mathcal B'}=P^{-1}[\alpha]_{\mathcal B}P$. Two matrices $A,B\in\operatorname{Mat}_n(F)$ represent the same endomorphism in two bases if and only if they are *similar*: $B=P^{-1}AP$ for some $P\in\operatorname{GL}_n(F)$.

:::

::: {.proof}

1. This is @thm-change-of-basis-two-spaces with $Q=P$.

2. Conversely, if $B=P^{-1}AP$, let $\alpha$ be $\mathbf x\mapsto A\mathbf x$ and take the columns of $P$ as a new basis; then $[\alpha]$ in the new basis is $B$.

:::

So a property of square matrices that is invariant under similarity is a property of the endomorphism. Classifying endomorphisms means classifying matrices up to similarity, which is much harder than equivalence (where only the rank survives, @thm-rank-normal-form).

::: {#lem-trace-cyclic .lemma name="Trace of a product"}

For $A\in\operatorname{Mat}_{n,m}(F)$ and $B\in\operatorname{Mat}_{m,n}(F)$, $\operatorname{tr}(AB)=\operatorname{tr}(BA)$. Hence similar matrices have the same trace: $\operatorname{tr}(P^{-1}AP)=\operatorname{tr}(APP^{-1})=\operatorname{tr}A$.

:::

::: {.proof}

$\operatorname{tr}(AB)=\sum_i\sum_ja_{ij}b_{ji}=\sum_j\sum_ib_{ji}a_{ij}=\operatorname{tr}(BA)$.

:::

::: {#def-trace-determinant-endomorphism .definition name="Trace, determinant and characteristic polynomial of an endomorphism"}

For $\alpha\in\operatorname{End}(V)$ and any basis $\mathcal B$, let $A=[\alpha]_{\mathcal B}$. Define $\operatorname{tr}\alpha=\operatorname{tr}A$, $\det\alpha=\det A$, and the *characteristic polynomial*
$$\chi_\alpha(t)=\det(t\iota-\alpha)=\det(tI-A).$$

:::

These do not depend on $\mathcal B$: trace by @lem-trace-cyclic, determinant by @thm-determinant-multiplicative ($\det(P^{-1}AP)=\det P^{-1}\det A\det P=\det A$), and $\chi$ because $tI-P^{-1}AP=P^{-1}(tI-A)P$. $\chi_\alpha$ is monic of degree $n$: $\chi_\alpha(t)=t^n-(\operatorname{tr}\alpha)t^{n-1}+\dots+(-1)^n\det\alpha$.

::: {#def-eigenvalue-endomorphism .definition name="Eigenvalue, eigenvector, eigenspace" generalizes="def-eigenvalue"}

$\lambda\in F$ is an *eigenvalue* of $\alpha\in\operatorname{End}(V)$ if $\alpha(v)=\lambda v$ for some $v\ne0$, an *eigenvector*. The *eigenspace* is $E(\lambda)=\ker(\alpha-\lambda\iota)$.

:::

::: {#prp-eigenvalue-iff-root .proposition name="Eigenvalues are roots of the characteristic polynomial"}

$\lambda\in F$ is an eigenvalue of $\alpha$ if and only if $\chi_\alpha(\lambda)=0$.

:::

::: {.proof}

$\lambda$ is an eigenvalue $\iff$ $\ker(\alpha-\lambda\iota)\ne\{0\}$ $\iff$ $\alpha-\lambda\iota$ is not invertible (@cor-injective-iff-surjective) $\iff$ $\det(\lambda\iota-\alpha)=0$ (@thm-determinant-invertible).

:::

The eigenvalues must lie in $F$. Rotation by $\frac\pi2$ of $\mathbb R^2$ has $\chi(t)=t^2+1$ and no real eigenvalues; as an endomorphism of $\mathbb C^2$ it has eigenvalues $\pm i$.

::: {#lem-eigenspaces-independent .lemma name="Eigenspaces form a direct sum" generalizes="thm-distinct-eigenvalues-independent"}

If $\lambda_1,\dots,\lambda_k$ are distinct eigenvalues of $\alpha$, then $E(\lambda_1)+\dots+E(\lambda_k)$ is a direct sum.

:::

::: {.proof}

By @prp-direct-sum-criteria we must show: if $v_1+\dots+v_k=0$ with $v_i\in E(\lambda_i)$, then all $v_i=0$.

1. For fixed $j$, let $p_j(t)=\prod_{i\ne j}(t-\lambda_i)$. Then $p_j(\alpha)v_i=\prod_{l\ne j}(\lambda_i-\lambda_l)\,v_i$, which is $0$ for $i\ne j$ (the factor $l=i$ vanishes).

2. Applying $p_j(\alpha)$ to $\sum_iv_i=0$ gives $\prod_{l\ne j}(\lambda_j-\lambda_l)\,v_j=0$. The scalar is non-zero because the $\lambda$'s are distinct, so $v_j=0$.

:::

::: {#def-diagonalizable-endomorphism .definition name="Diagonalisable endomorphism"}

$\alpha\in\operatorname{End}(V)$ is *diagonalisable* if $V$ has a basis of eigenvectors of $\alpha$, that is, a basis in which $[\alpha]$ is diagonal.

:::

::: {#thm-diagonalizable-iff-eigenspaces .theorem name="Diagonalisable means the eigenspaces fill V" generalizes="thm-diagonalization"}

Let $\lambda_1,\dots,\lambda_k$ be the distinct eigenvalues of $\alpha$. The following are equivalent:

1. $\alpha$ is diagonalisable;
2. $V=E(\lambda_1)\oplus\dots\oplus E(\lambda_k)$;
3. $\sum_i\dim E(\lambda_i)=n$.

:::

::: {.proof}

1. (1)⇒(2): a basis of eigenvectors lies in $\sum E(\lambda_i)$, so this sum is $V$, and it is direct by @lem-eigenspaces-independent.

2. (2)⇒(1): concatenating bases of the $E(\lambda_i)$ gives a basis of $V$ (@prp-direct-sum-criteria) made of eigenvectors.

3. (2)⇔(3): the sum is direct by @lem-eigenspaces-independent, so its dimension is $\sum\dim E(\lambda_i)$ (@prp-direct-sum-criteria), and a subspace of dimension $n$ is $V$.

:::

::: {#exm-endomorphism-not-diagonalisable .example name="Diagonalisable over one field, not another"}

$A=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$ is not diagonalisable over $\mathbb R$ (no eigenvalues), but over $\mathbb C$ its eigenvalues $i,-i$ are distinct and $E(i)\oplus E(-i)=\mathbb C^2$ with $E(\pm i)=\langle(1,\mp i)^{\mathsf T}\rangle$. The matrix $\begin{bmatrix}1&1\\0&1\end{bmatrix}$ is diagonalisable over no field: its only eigenvalue is $1$ and $E(1)=\langle e_1\rangle$ has dimension $1<2$. Over $\mathbb F_2$, $\begin{bmatrix}0&1\\1&0\end{bmatrix}$ has $\chi(t)=t^2-1=(t-1)^2$ and $E(1)=\langle(1,1)^{\mathsf T}\rangle$, so the swap matrix, diagonalisable over $\mathbb R$, is not diagonalisable over $\mathbb F_2$.

:::
