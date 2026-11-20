---
title: "Linear Maps and Isomorphisms"
sources: [camib-la-2, mit1806-30]
requires: [math/linear-algebra/abstract-vector-spaces/bases-and-dimension, math/linear-algebra/positive-definite/linear-transformations]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 2.1, in our own wording; examples ours; proofs written out in steps. MIT 18.06 introduces linear transformations of R^n (def-linear-transformation, prp-linear-map-determined-by-basis); the versions here work over any field and carry generalizes=. -->

<!-- Merged 2026-11-20 (owner): prp-linear-map-determined-by-basis (18.06 L30) merged into thm-linear-map-from-basis (same two-step proof). -->

Linear maps are the maps between vector spaces that respect the structure. Following the Cambridge course, they are written with Greek letters $\alpha,\beta$, and $U,V,W$ are vector spaces over the same field $F$.

::: {#def-linear-map .definition name="Linear map, isomorphism" generalizes="def-linear-transformation"}

A map $\alpha:U\to V$ is *linear* if
$$\alpha(\lambda u_1+\mu u_2)=\lambda\alpha(u_1)+\mu\alpha(u_2)\qquad\text{for all }u_1,u_2\in U,\ \lambda,\mu\in F.$$
The linear maps $U\to V$ form a set $\mathcal L(U,V)$. A linear map is an *isomorphism* if it is a bijection; $U$ and $V$ are *isomorphic*, $U\cong V$, if there is an isomorphism between them.

:::

::: {#prp-linear-maps-basic .proposition name="Basic properties of linear maps"}

1. A linear map sends $0$ to $0$.
2. Compositions of linear maps are linear.
3. The inverse of a linear bijection is linear, so an isomorphism has a linear inverse.
4. $\mathcal L(U,V)$ is a vector space under $(\alpha+\beta)(u)=\alpha(u)+\beta(u)$ and $(\lambda\alpha)(u)=\lambda\alpha(u)$.

:::

::: {.proof}

1. $\alpha(0)=\alpha(0\cdot0)=0\,\alpha(0)=0$ by @prp-vector-space-zero-rules.

2. $\beta\alpha(\lambda u+\mu u')=\beta(\lambda\alpha u+\mu\alpha u')=\lambda\beta\alpha u+\mu\beta\alpha u'$.

3. Let $v,v'\in V$ and $u=\alpha^{-1}v$, $u'=\alpha^{-1}v'$. Then $\alpha(\lambda u+\mu u')=\lambda v+\mu v'$, so $\alpha^{-1}(\lambda v+\mu v')=\lambda u+\mu u'=\lambda\alpha^{-1}v+\mu\alpha^{-1}v'$.

4. Sums and multiples of linear maps are linear by a one-line check, and the vector space axioms hold pointwise because they hold in $V$.

:::

::: {#thm-linear-map-from-basis .theorem name="A linear map is free on a basis"}

Let $e_1,\dots,e_n$ be a basis of $U$ and $v_1,\dots,v_n$ any vectors of $V$. There is exactly one linear map $\alpha:U\to V$ with $\alpha(e_i)=v_i$ for all $i$.

:::

::: {.proof}

1. Uniqueness: a linear $\alpha$ must satisfy $\alpha(\sum\lambda_ie_i)=\sum\lambda_iv_i$, and every $u$ is such a sum.

2. Existence: define $\alpha(\sum\lambda_ie_i)=\sum\lambda_iv_i$. This is well defined because the coefficients $\lambda_i$ of $u$ are unique (@prp-basis-iff-unique-expression). It is linear, because the coefficients of $\lambda u+\mu u'$ are $\lambda\lambda_i+\mu\lambda_i'$.

:::

::: {#def-kernel-image .definition name="Kernel and image"}

For a linear map $\alpha:U\to V$, the *kernel* and *image* are
$$\ker\alpha=\{u\in U:\alpha(u)=0\},\qquad \operatorname{im}\alpha=\{\alpha(u):u\in U\}.$$

:::

::: {#prp-kernel-image-subspaces .proposition name="Kernel and image are subspaces"}

$\ker\alpha\le U$ and $\operatorname{im}\alpha\le V$. Moreover $\alpha$ is injective if and only if $\ker\alpha=\{0\}$.

:::

::: {.proof}

1. If $\alpha u=\alpha u'=0$, then $\alpha(\lambda u+\mu u')=0$; and $0\in\ker\alpha$.

2. $\lambda\alpha(u)+\mu\alpha(u')=\alpha(\lambda u+\mu u')\in\operatorname{im}\alpha$; and $0=\alpha(0)$.

3. If $\alpha$ is injective and $\alpha u=0=\alpha(0)$, then $u=0$. Conversely, if $\ker\alpha=\{0\}$ and $\alpha u=\alpha u'$, then $\alpha(u-u')=0$, so $u=u'$.

:::

The nullspace and column space of a matrix (@def-nullspace, @def-column-space) are the kernel and image of $\mathbf x\mapsto A\mathbf x$.

::: {#thm-isomorphic-iff-same-dimension .theorem name="Classification of finite-dimensional spaces"}

Let $U$ and $V$ be finite-dimensional over $F$.

1. An isomorphism maps a basis to a basis; a linear map that maps some basis to a basis is an isomorphism.
2. $U\cong V$ if and only if $\dim U=\dim V$. In particular every $n$-dimensional space is isomorphic to $F^n$.

:::

::: {.proof}

1. Let $\alpha$ be an isomorphism and $e_1,\dots,e_n$ a basis of $U$. If $\sum\lambda_i\alpha(e_i)=0$, then $\alpha(\sum\lambda_ie_i)=0$, so $\sum\lambda_ie_i=0$ by injectivity and all $\lambda_i=0$. Every $v=\alpha(u)$ with $u=\sum\lambda_ie_i$ equals $\sum\lambda_i\alpha(e_i)$. So $\alpha(e_1),\dots,\alpha(e_n)$ is a basis.

2. If $\alpha$ maps a basis $e_i$ to a basis $f_i$, let $\beta:V\to U$ be the linear map with $\beta(f_i)=e_i$ (@thm-linear-map-from-basis). Then $\beta\alpha$ and $\alpha\beta$ fix a basis, so they are the identities by the uniqueness in @thm-linear-map-from-basis, and $\alpha$ is bijective.

3. If $U\cong V$, item 1 gives bases of the same size. If $\dim U=\dim V=n$, map a basis of $U$ to a basis of $V$ and apply item 1.

:::

Choosing a basis $e_1,\dots,e_n$ of $V$ is the same as choosing an isomorphism $F^n\to V$, $(\lambda_i)\mapsto\sum\lambda_ie_i$; its inverse sends a vector to its *coordinates*. The isomorphism is not canonical: it depends on the basis.

::: {#exm-linear-maps-abstract .example name="Linear maps without matrices in sight"}

1. Differentiation $D:F[t]\to F[t]$, $p\mapsto p'$, is linear. Over $\mathbb R$ its kernel is the constants and it is surjective.
2. For distinct $a_1,\dots,a_n\in F$, evaluation $\operatorname{ev}:F[t]_{<n}\to F^n$, $p\mapsto(p(a_1),\dots,p(a_n))$, is linear between spaces of dimension $n$. Its kernel is $\{0\}$, since a non-zero polynomial of degree $<n$ has fewer than $n$ roots (@thm-at-most-d-roots). So it is an isomorphism (by @thm-rank-nullity it is then surjective), which is Lagrange interpolation.
3. On $\mathbb R^{\mathbb N}$, the shift $(x_1,x_2,\dots)\mapsto(x_2,x_3,\dots)$ is surjective but not injective, and $(x_1,x_2,\dots)\mapsto(0,x_1,x_2,\dots)$ is injective but not surjective. In infinite dimensions a space can be isomorphic to a proper subspace of itself.

:::
