---
title: "Inner Product Spaces"
sources: [camib-la-8, mit1806-1]
requires: [math/linear-algebra/bilinear-forms/hermitian-forms, math/linear-algebra/orthogonality/fourier-series]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 8.1, in our own wording; examples ours; proofs written out in steps. MIT 18.06 has the dot product on R^n with Cauchy-Schwarz (thm-cauchy-schwarz), the complex inner product on C^n (def-complex-inner-product) and the inner product of functions (def-function-inner-product); the abstract versions here carry generalizes= or related=. Merge of the Cauchy-Schwarz blocks proposed to the owner. -->

<!-- Merged 2026-11-20 (owner): thm-cauchy-schwarz (18.06 L1, Cauchy-Schwarz and triangle inequality for the dot product) merged into thm-cauchy-schwarz-inner-product and cor-triangle-inequality-inner-product. -->

An inner product adds lengths and angles to a vector space. Here $F=\mathbb R$ or $\mathbb C$; for $F=\mathbb R$ the complex conjugations below do nothing.

::: {#def-inner-product-space .definition name="Inner product space" generalizes="def-complex-inner-product"}

An *inner product* on an $F$-vector space $V$ is a map $\langle\cdot,\cdot\rangle:V\times V\to F$ that is

1. linear in the first argument: $\langle\lambda u+\mu v,w\rangle=\lambda\langle u,w\rangle+\mu\langle v,w\rangle$;
2. conjugate symmetric: $\langle v,u\rangle=\overline{\langle u,v\rangle}$;
3. positive definite: $\langle v,v\rangle>0$ for $v\ne0$.

So it is a positive definite symmetric bilinear form (real case) or Hermitian form (complex case; @def-sesquilinear-form). $V$ with an inner product is an *inner product space* (*Euclidean* if real, *unitary* if complex), and $\lVert v\rVert=\sqrt{\langle v,v\rangle}$ is the *norm*.

:::

::: {#exm-inner-product-spaces .example name="Inner product spaces"}

1. $\mathbb C^n$ with $\langle\mathbf z,\mathbf w\rangle=\sum_iz_i\bar w_i$, and $\mathbb R^n$ with the dot product.
2. $C[a,b]$ with $\langle f,g\rangle=\int_a^bf(t)\overline{g(t)}\,dt$ (@def-function-inner-product). Positive definiteness uses continuity: if $f\ne0$ then $\lvert f\rvert^2>0$ on some interval, so the integral is positive.
3. $\operatorname{Mat}_n(\mathbb R)$ with $\langle A,B\rangle=\operatorname{tr}(A^{\mathsf T}B)=\sum_{i,j}a_{ij}b_{ij}$.
4. $\mathbb R^n$ with $\langle\mathbf x,\mathbf y\rangle=\mathbf x^{\mathsf T}S\mathbf y$ for any positive definite symmetric $S$ (@def-definite-forms).

:::

::: {#thm-cauchy-schwarz-inner-product .theorem name="Cauchy–Schwarz inequality"}

In an inner product space, $\lvert\langle u,v\rangle\rvert\le\lVert u\rVert\,\lVert v\rVert$ for all $u,v$, with equality if and only if $u$ and $v$ are linearly dependent.

:::

::: {.proof}

1. If $v=0$ both sides are $0$. Otherwise, for every $\lambda\in F$,
$$0\le\lVert u-\lambda v\rVert^2=\lVert u\rVert^2-\bar\lambda\langle u,v\rangle-\lambda\overline{\langle u,v\rangle}+\lvert\lambda\rvert^2\lVert v\rVert^2.$$

2. Take $\lambda=\dfrac{\langle u,v\rangle}{\lVert v\rVert^2}$. The last three terms become $-2\dfrac{\lvert\langle u,v\rangle\rvert^2}{\lVert v\rVert^2}+\dfrac{\lvert\langle u,v\rangle\rvert^2}{\lVert v\rVert^2}$, so $0\le\lVert u\rVert^2-\dfrac{\lvert\langle u,v\rangle\rvert^2}{\lVert v\rVert^2}$, which is the inequality.

3. Equality forces $u-\lambda v=0$ by positive definiteness. Conversely, if $u=\mu v$ then $\lvert\langle u,v\rangle\rvert=\lvert\mu\rvert\lVert v\rVert^2=\lVert u\rVert\lVert v\rVert$.

:::

::: {#cor-triangle-inequality-inner-product .corollary name="Triangle inequality"}

$\lVert u+v\rVert\le\lVert u\rVert+\lVert v\rVert$; so $\lVert\cdot\rVert$ is a norm (@def-norm) and $d(u,v)=\lVert u-v\rVert$ a metric.

:::

::: {.proof}

$\lVert u+v\rVert^2=\lVert u\rVert^2+2\operatorname{Re}\langle u,v\rangle+\lVert v\rVert^2\le\lVert u\rVert^2+2\lVert u\rVert\lVert v\rVert+\lVert v\rVert^2=(\lVert u\rVert+\lVert v\rVert)^2$, using $\operatorname{Re}z\le\lvert z\rvert$ and @thm-cauchy-schwarz-inner-product.

:::

::: {#def-orthonormal-set .definition name="Orthogonal and orthonormal" generalizes="def-orthonormal-vectors"}

$u,v$ are *orthogonal* if $\langle u,v\rangle=0$. A set $\{e_i\}$ is *orthonormal* if $\langle e_i,e_j\rangle=\delta_{ij}$; an *orthonormal basis* is an orthonormal set that is a basis.

:::

::: {#prp-parseval .proposition name="Coordinates in an orthonormal basis (Parseval)"}

An orthonormal set is linearly independent. If $e_1,\dots,e_n$ is an orthonormal basis of $V$, then for all $u,v\in V$
$$v=\sum_{i=1}^n\langle v,e_i\rangle e_i,\qquad \langle u,v\rangle=\sum_{i=1}^n\langle u,e_i\rangle\overline{\langle v,e_i\rangle},\qquad \lVert v\rVert^2=\sum_{i=1}^n\lvert\langle v,e_i\rangle\rvert^2.$$

:::

::: {.proof}

1. If $\sum_i\lambda_ie_i=0$, take the inner product with $e_j$: $\lambda_j=0$.

2. Write $v=\sum_i\lambda_ie_i$. Then $\langle v,e_j\rangle=\sum_i\lambda_i\langle e_i,e_j\rangle=\lambda_j$.

3. With $u=\sum_i\mu_ie_i$, $\langle u,v\rangle=\sum_{i,j}\mu_i\bar\lambda_j\langle e_i,e_j\rangle=\sum_i\mu_i\bar\lambda_i$; the norm formula is the case $u=v$.

:::

So in an orthonormal basis, every inner product space of dimension $n$ looks like $F^n$ with the standard inner product. Coefficients are found by inner products, not by solving equations: this is the Fourier coefficient formula of @thm-fourier-coefficients in general.
