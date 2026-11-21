---
title: "The First Isomorphism Theorem and Rank–Nullity"
sources: [camib-la-2]
requires: [math/linear-algebra/linear-maps/linear-maps-and-isomorphisms, math/linear-algebra/abstract-vector-spaces/direct-sums]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 2.3, in our own wording; examples ours; proofs written out in steps. MIT 18.06 gets dim N(A) = n - r by counting free variables (thm-fundamental-theorem-dimensions); the basis-free statement here carries related=. -->

::: {#thm-first-isomorphism-theorem .theorem name="First isomorphism theorem"}

Let $\alpha:U\to V$ be linear. Then
$$\bar\alpha:U/\ker\alpha\to\operatorname{im}\alpha,\qquad u+\ker\alpha\mapsto\alpha(u)$$
is a well-defined isomorphism (@def-quotient-space).

:::

::: {.proof}

1. Well defined and injective: $u+\ker\alpha=u'+\ker\alpha$ $\iff$ $u-u'\in\ker\alpha$ $\iff$ $\alpha(u)=\alpha(u')$. The forward direction says $\bar\alpha$ does not depend on the representative; the backward direction says it is injective.

2. Linear: $\bar\alpha(\lambda(u+\ker\alpha)+\mu(u'+\ker\alpha))=\bar\alpha((\lambda u+\mu u')+\ker\alpha)=\lambda\alpha(u)+\mu\alpha(u')$.

3. Surjective: every $\alpha(u)\in\operatorname{im}\alpha$ is $\bar\alpha(u+\ker\alpha)$.

:::

::: {#def-rank-nullity .definition name="Rank and nullity"}

For a linear map $\alpha:U\to V$ with $U$ finite-dimensional, the *rank* is $r(\alpha)=\dim\operatorname{im}\alpha$ and the *nullity* is $n(\alpha)=\dim\ker\alpha$.

:::

::: {#thm-rank-nullity .theorem name="Rank–nullity theorem" related="thm-fundamental-theorem-dimensions"}

If $\alpha:U\to V$ is linear and $U$ is finite-dimensional, then
$$r(\alpha)+n(\alpha)=\dim U.$$

:::

::: {.proof}

1. By @thm-first-isomorphism-theorem, $\operatorname{im}\alpha\cong U/\ker\alpha$.

2. Isomorphic spaces have the same dimension (@thm-isomorphic-iff-same-dimension), and $\dim U/\ker\alpha=\dim U-\dim\ker\alpha$ by @prp-dimension-of-quotient.

:::

::: {#fig-rank-nullity-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.0,1.5) rectangle (0.9,2.0);
\draw[hl cell] (0.9,1.5) rectangle (1.8,2.0);
\draw[cell frame] (1.8,1.5) rectangle (2.7,2.0);
\draw[cell frame] (2.7,1.5) rectangle (3.6,2.0);
\draw[cell frame] (3.6,1.5) rectangle (4.5,2.0);
\draw[cell frame] (1.8,0) rectangle (2.7,0.5);
\draw[cell frame] (2.7,0) rectangle (3.6,0.5);
\draw[cell frame] (3.6,0) rectangle (4.5,0.5);
\draw[faint] (4.5,0) rectangle (5.4,0.5);
\node[lab, left] at (0,1.75) {$U$}; \node[lab, left] at (1.8,0.25) {$V$};
\draw[decorate, decoration={brace, amplitude=4pt}] (0,2.05) -- node[lab, above=3pt] {$n(\alpha)$: sent to $0$} (1.8,2.05);
\draw[decorate, decoration={brace, amplitude=4pt}] (1.8,2.05) -- node[lab, above=3pt] {$r(\alpha)$} (4.5,2.05);
\draw[map] (3.15,1.5) -- node[lab, right] {$\alpha$, one to one} (3.15,0.5);
\draw[decorate, decoration={brace, amplitude=4pt, mirror}] (1.8,-0.05) -- node[lab, below=3pt] {$\operatorname{Im}\alpha$} (4.5,-0.05);
\end{tikzpicture}
\end{center}
```

Rank–nullity with one cell per basis vector: a basis of $\ker\alpha$ (shaded) extends to a basis of $U$, and the extra vectors map to a basis of $\operatorname{Im}\alpha$. So $\dim U=n(\alpha)+r(\alpha)$.

:::

A direct proof avoids quotients: extend a basis $e_1,\dots,e_k$ of $\ker\alpha$ to a basis $e_1,\dots,e_n$ of $U$; then $\alpha(e_{k+1}),\dots,\alpha(e_n)$ is a basis of $\operatorname{im}\alpha$. They span because $\alpha(e_i)=0$ for $i\le k$, and $\sum_{i>k}\lambda_i\alpha(e_i)=0$ puts $\sum_{i>k}\lambda_ie_i$ in $\ker\alpha=\langle e_1,\dots,e_k\rangle$, which forces every $\lambda_i=0$. The same argument shows that $\langle e_{k+1},\dots,e_n\rangle$ is a complement of $\ker\alpha$ (@prp-complements-exist) mapped isomorphically onto the image.

::: {#cor-injective-iff-surjective .corollary name="Injective, surjective and bijective agree"}

Let $\alpha:U\to V$ be linear with $\dim U=\dim V<\infty$. Then $\alpha$ is injective $\iff$ $\alpha$ is surjective $\iff$ $\alpha$ is an isomorphism.

:::

::: {.proof}

1. $\alpha$ is injective $\iff$ $n(\alpha)=0$ (@prp-kernel-image-subspaces) $\iff$ $r(\alpha)=\dim U$ by @thm-rank-nullity.

2. $r(\alpha)=\dim U=\dim V$ $\iff$ $\operatorname{im}\alpha=V$, by @cor-independent-set-extends-to-basis.

:::

The shifts on sequences (@exm-linear-maps-abstract) show that the corollary fails in infinite dimensions.

::: {#cor-invertible-matrix-conditions .corollary name="One-sided inverses of square matrices"}

For $A\in\operatorname{Mat}_n(F)$ the following are equivalent: $A$ is invertible; $AB=I$ for some $B$; $BA=I$ for some $B$; $A\mathbf x=\mathbf 0$ only for $\mathbf x=\mathbf 0$; the columns of $A$ span $F^n$. A one-sided inverse is then the inverse.

:::

::: {.proof}

1. Let $\alpha:F^n\to F^n$ be $\mathbf x\mapsto A\mathbf x$. "$A\mathbf x=\mathbf0$ only for $\mathbf0$" says $\alpha$ is injective, and "columns span" says it is surjective; by @cor-injective-iff-surjective both say $\alpha$ is bijective, that is, $A$ is invertible (its inverse map is linear, @prp-linear-maps-basic, so it is a matrix).

2. If $AB=I$, then $\alpha$ is surjective (every $\mathbf y=A(B\mathbf y)$), so $A$ is invertible. If $BA=I$, then $A\mathbf x=\mathbf0$ gives $\mathbf x=BA\mathbf x=\mathbf0$, so $A$ is invertible.

3. If $A$ is invertible and $AB=I$, then $B=A^{-1}AB=A^{-1}$; similarly for $BA=I$.

:::

::: {#exm-rank-nullity .example name="Rank–nullity for the trace"}

The trace $\operatorname{tr}:\operatorname{Mat}_n(F)\to F$ is linear and non-zero, so its image is $F$ and $r=1$. Hence the matrices of trace zero form a subspace of dimension $n^2-1$. For $n=2$ a basis is $\begin{bmatrix}1&0\\0&-1\end{bmatrix},\begin{bmatrix}0&1\\0&0\end{bmatrix},\begin{bmatrix}0&0\\1&0\end{bmatrix}$.

:::
