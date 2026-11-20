---
title: "Direct Sums"
sources: [camib-la-1]
requires: [math/linear-algebra/abstract-vector-spaces/bases-and-dimension]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 1.3, in our own wording; examples ours; proofs written out in steps. -->

A direct sum splits a vector space into pieces that do not overlap, so that each vector has exactly one component in each piece.

::: {#def-internal-direct-sum .definition name="Internal direct sum"}

Let $U_1,\dots,U_k$ be subspaces of $V$. $V$ is the *(internal) direct sum* of them, written
$$V=U_1\oplus\dots\oplus U_k,$$
if every $v\in V$ can be written as $v=u_1+\dots+u_k$ with $u_i\in U_i$ in exactly one way. If $V=U\oplus W$, then $W$ is a *complement* of $U$ in $V$.

:::

::: {#prp-direct-sum-criteria .proposition name="Tests for a direct sum"}

Let $U_1,\dots,U_k\le V$ with $V$ finite-dimensional. The following are equivalent:

1. $V=U_1\oplus\dots\oplus U_k$;
2. $V=U_1+\dots+U_k$, and $u_1+\dots+u_k=0$ with $u_i\in U_i$ forces every $u_i=0$;
3. if $\mathcal B_i$ is a basis of $U_i$, then the list $\mathcal B_1,\dots,\mathcal B_k$ (concatenated) is a basis of $V$;
4. $V=U_1+\dots+U_k$ and $\dim V=\sum_i\dim U_i$.

For two subspaces, $V=U\oplus W$ if and only if $V=U+W$ and $U\cap W=\{0\}$.

:::

::: {.proof}

1. (1)⇔(2): existence of an expression is $V=\sum U_i$. If two expressions $\sum u_i=\sum u_i'$ of the same vector differ, then $\sum(u_i-u_i')=0$ is a non-trivial expression of $0$; conversely a non-trivial expression of $0$ is a second expression besides $0+\dots+0$.

2. (2)⇒(3): the concatenated list spans $\sum U_i=V$. If a combination of it is $0$, group the terms as $u_1+\dots+u_k=0$ with $u_i\in U_i$; by (2) every $u_i=0$, and independence of $\mathcal B_i$ makes its coefficients $0$.

3. (3)⇒(4): count the basis vectors.

4. (4)⇒(2): the concatenated list spans $V$ and has $\dim V$ elements, so it is a basis (@cor-independent-set-extends-to-basis). If $\sum u_i=0$, expanding each $u_i$ in $\mathcal B_i$ gives a combination of this basis equal to $0$, so all coefficients and hence all $u_i$ vanish.

5. For two subspaces: if $0=u+w$ with $u\in U$, $w\in W$, then $u=-w\in U\cap W$; so (2) holds exactly when $U\cap W=\{0\}$.

:::

For three or more subspaces, pairwise intersections $\{0\}$ are not enough: three distinct lines through $0$ in $\mathbb R^2$ meet pairwise in $\{0\}$, yet their sum $\mathbb R^2$ has dimension $2<3$.

::: {#prp-complements-exist .proposition name="Complements exist"}

Every subspace $U$ of a finite-dimensional space $V$ has a complement: there is $W\le V$ with $V=U\oplus W$.

:::

::: {.proof}

1. Extend a basis $u_1,\dots,u_m$ of $U$ to a basis $u_1,\dots,u_m,w_{m+1},\dots,w_n$ of $V$ (@cor-independent-set-extends-to-basis).

2. Let $W=\langle w_{m+1},\dots,w_n\rangle$. The concatenation of the bases of $U$ and $W$ is a basis of $V$, so $V=U\oplus W$ by @prp-direct-sum-criteria.

:::

A complement is not unique: in $\mathbb R^2$ every line through $0$ other than $U$ itself is a complement of the line $U$. What is determined is its dimension $\dim V-\dim U$, and its isomorphism type, which is that of $V/U$ (@def-quotient-space).

::: {#def-external-direct-sum .definition name="External direct sum"}

For $F$-vector spaces $U_1,\dots,U_k$, the *external direct sum* $U_1\oplus\dots\oplus U_k$ is the set of tuples $(u_1,\dots,u_k)$ with $u_i\in U_i$, with entrywise addition and scalar multiplication.

:::

The two notions agree: the copies $\{(0,\dots,u_i,\dots,0)\}$ of the $U_i$ are subspaces of the external sum, which is their internal direct sum. Hence $\dim(U_1\oplus\dots\oplus U_k)=\sum\dim U_i$, and $F^n$ is the direct sum of $n$ copies of $F$.

::: {#exm-direct-sum-matrices .example name="Symmetric and antisymmetric matrices"}

Let $F$ be a field with $1+1\ne0$ (so not $\mathbb F_2$). Every $A\in\operatorname{Mat}_n(F)$ is
$$A=\tfrac12(A+A^{\mathsf T})+\tfrac12(A-A^{\mathsf T}),$$
a symmetric plus an antisymmetric matrix, and a matrix that is both has $A=A^{\mathsf T}=-A$, so $2A=0$ and $A=0$. Hence $\operatorname{Mat}_n(F)$ is the direct sum of the symmetric matrices (dimension $\frac{n(n+1)}2$) and the antisymmetric ones (dimension $\frac{n(n-1)}2$); the dimensions add up to $n^2$. Over $\mathbb F_2$ the decomposition fails: there $A^{\mathsf T}=-A$ means symmetric, so the two subspaces are not complementary.

:::
