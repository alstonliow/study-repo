---
title: "Sylvester's Law of Inertia"
sources: [camib-la-7]
requires: [math/linear-algebra/bilinear-forms/symmetric-forms-and-quadratic-forms]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 7.1 (second half), in our own wording; examples ours (checked with sympy); proofs written out in steps. MIT 18.06 defines positive definite matrices (def-positive-definite) and relates the signs of pivots and eigenvalues (prp-signs-of-pivots-and-eigenvalues); the form versions here carry generalizes= and related=. -->

Over $\mathbb R$ a symmetric form can be diagonalised (@thm-symmetric-form-diagonalizable) and the diagonal entries rescaled to $1$, $-1$ or $0$. The number of each sign does not depend on the choice of basis.

::: {#def-definite-forms .definition name="Definite forms" generalizes="def-positive-definite"}

A symmetric bilinear form $\phi$ on a real vector space $V$ is *positive definite* if $\phi(v,v)>0$ for all $v\ne0$, *positive semi-definite* if $\phi(v,v)\ge0$ for all $v$, and *negative (semi-)definite* if $-\phi$ is positive (semi-)definite. A real symmetric matrix $A$ has these properties when the form $\mathbf x^{\mathsf T}A\mathbf y$ does.

:::

::: {#thm-real-symmetric-forms .theorem name="Classification over the reals"}

Let $\phi$ be a symmetric bilinear form on an $n$-dimensional real vector space. There is a basis in which
$$[\phi]=\begin{bmatrix}I_p&&\\&-I_q&\\&&0\end{bmatrix}$$
for some $p,q\ge0$ with $p+q=r(\phi)$.

:::

::: {.proof}

1. Take a diagonal basis (@thm-symmetric-form-diagonalizable) and order it so that $\phi(e_i,e_i)=\lambda_i$ is positive for $i\le p$, negative for $p<i\le p+q$, and zero after.

2. Replace $e_i$ by $e_i/\sqrt{\lvert\lambda_i\rvert}$ for $i\le p+q$. Then $\phi(e_i,e_i)=\lambda_i/\lvert\lambda_i\rvert=\pm1$.

3. The rank of a diagonal matrix is the number of non-zero entries, so $p+q=r(\phi)$.

:::

::: {#thm-sylvester-law-of-inertia .theorem name="Sylvester's law of inertia" related="prp-signs-of-pivots-and-eigenvalues"}

The numbers $p$ and $q$ in @thm-real-symmetric-forms depend only on $\phi$: $p$ is the largest dimension of a subspace on which $\phi$ is positive definite, and $q$ the largest dimension of one on which it is negative definite.

:::

::: {.proof}

Let $e_1,\dots,e_n$ be a basis as in @thm-real-symmetric-forms. We show $p=\max\{\dim U:\phi|_U\text{ positive definite}\}$; the statement for $q$ follows by applying it to $-\phi$.

1. $\phi$ is positive definite on $P=\langle e_1,\dots,e_p\rangle$: for $v=\sum_{i\le p}\lambda_ie_i\ne0$, $\phi(v,v)=\sum\lambda_i^2>0$. So the maximum is at least $p$.

2. Let $N=\langle e_{p+1},\dots,e_n\rangle$. For $v=\sum_{i>p}\lambda_ie_i$, $\phi(v,v)=-\sum_{p<i\le p+q}\lambda_i^2\le0$.

3. Let $U$ be any subspace on which $\phi$ is positive definite. A vector $v\in U\cap N$ has $\phi(v,v)\le0$ by step 2, so $v=0$. Hence $U\cap N=\{0\}$, and by @thm-dimension-of-sum-and-intersection, $\dim U\le n-\dim N=p$.

:::

::: {#def-signature .definition name="Signature"}

The *signature* of a real symmetric form $\phi$ is $s(\phi)=p-q$, with $p,q$ as in @thm-real-symmetric-forms. (Some authors call the pair $(p,q)$ the signature.)

:::

::: {#cor-real-symmetric-congruence .corollary name="Congruence of real symmetric matrices"}

Every real symmetric matrix is congruent to exactly one matrix $\operatorname{diag}(I_p,-I_q,0)$. Two real symmetric matrices are congruent if and only if they have the same rank and the same signature. A form is positive definite exactly when $p=n$.

:::

::: {.proof}

1. Existence is @thm-real-symmetric-forms, uniqueness of $p$ and $q$ is @thm-sylvester-law-of-inertia, and rank and signature determine $p=\frac{r+s}2$ and $q=\frac{r-s}2$.

2. If $p=n$, then $\phi(v,v)=\sum\lambda_i^2>0$ for $v\ne0$. Conversely, if $\phi$ is positive definite on $V$, then $p\ge\dim V=n$ by the characterisation of $p$.

:::

By the spectral theorem (@cor-real-symmetric-orthogonally-diagonalisable) one diagonal basis comes from orthonormal eigenvectors of the matrix; so $p$ and $q$ are the numbers of positive and negative eigenvalues, counted with multiplicity.

::: {#exm-sylvester .example name="Signature in two ways"}

For $q(x,y,z)=x^2+2xy+3y^2+4yz+z^2$, completing the square gave $x'^2+2y'^2-z'^2$ (@exm-diagonalising-quadratic-form), so $p=2$, $q=1$, rank $3$ and signature $1$. Its matrix $\begin{bmatrix}1&1&0\\1&3&2\\0&2&1\end{bmatrix}$ has characteristic polynomial $t^3-5t^2+2t+2=(t-1)(t^2-4t-2)$, with roots $1$ and $2\pm\sqrt6$: two positive and one negative, although the eigenvalues themselves differ from $1,2,-1$. The same counts, as Sylvester's law requires. The form $xy$ on $\mathbb R^2$ equals $\big(\frac{x+y}2\big)^2-\big(\frac{x-y}2\big)^2$, so it has $p=q=1$ and signature $0$: it is positive on the line $y=x$ and negative on $y=-x$.

:::

::: {#fig-sylvester-law-of-inertia-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0,0) rectangle (2,2);
\fill[tintA] (0,0) rectangle (-2,-2);
\fill[tintB] (0,0) rectangle (-2,2);
\fill[tintB] (0,0) rectangle (2,-2);
\draw[->] (-2.2,0) -- (2.4,0) node[lab, anchor=west] {$x$};
\draw[->] (0,-2.2) -- (0,2.4) node[lab, anchor=south] {$y$};
\draw[emph, primary] (-2,-2) -- (2,2) node[lab, anchor=south west] {$y=x$: $q>0$};
\draw[emph, accent] (-2,2) -- (2,-2) node[lab, anchor=north west] {$y=-x$: $q<0$};
\node[lab] at (1.3,0.5) {$q>0$};
\node[lab] at (-1.3,0.5) {$q<0$};
\node[lab] at (-1.3,-0.5) {$q>0$};
\node[lab] at (1.3,-0.5) {$q<0$};
\end{tikzpicture}
\end{center}
```

The form $q(x,y)=xy$ is positive on two opposite quadrants and negative on the other two. The largest subspaces on which it is positive or negative definite are lines, such as $y=x$ and $y=-x$, so $p=q=1$.

:::
