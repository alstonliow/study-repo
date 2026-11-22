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

::: {#fig-linear-maps-and-isomorphisms-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[shift={(0,0)}]
\draw[gridline] (-1.4,-1.4) grid[step=0.5] (1.4,1.4);
\draw[->, muted] (-1.5,0) -- (1.60,0);
\draw[->, muted] (0,-1.5) -- (0,1.60);
\draw[->, emph, primary] (0,0) -- (1,0) node[below, lab] {$e_1$};
\draw[->, emph, secondary] (0,0) -- (0,1) node[left, lab] {$e_2$};
\end{scope}
\draw[->] (1.8,0) -- (2.8,0) node[midway, above, lab, note] {$\alpha$};
\begin{scope}[shift={(4.6,0)}]
\draw[->, muted] (-1.5,0) -- (1.6,0); \draw[->, muted] (0,-1.5) -- (0,1.6);
\draw[gridline] (-0.52,-1.70) -- (-1.48,0.70); \draw[gridline] (-0.80,-1.60) -- (1.60,-0.40);
\draw[gridline] (-0.02,-1.45) -- (-0.98,0.95); \draw[gridline] (-1.00,-1.10) -- (1.40,0.10);
\draw[gridline] (0.98,-0.95) -- (0.02,1.45); \draw[gridline] (-1.40,-0.10) -- (1.00,1.10);
\draw[gridline] (1.48,-0.70) -- (0.52,1.70); \draw[gridline] (-1.60,0.40) -- (0.80,1.60);
\draw[->, emph, primary] (0,0) -- (1,0.5) node[right, lab] {$\alpha(e_1)$};
\draw[->, emph, secondary] (0,0) -- (-0.4,1) node[above, lab] {$\alpha(e_2)$};
\end{scope}
\end{tikzpicture}
\end{center}
```

A linear map is free on a basis: choose any images for $e_1$ and $e_2$, and linearity forces the image of every other vector, $\alpha(x_1e_1+x_2e_2)=x_1\alpha(e_1)+x_2\alpha(e_2)$. The grid goes to the grid spanned by the chosen images.

:::

::: {#def-kernel-image .definition name="Kernel and image"}

For a linear map $\alpha:U\to V$, the *kernel* and *image* are
$$\ker\alpha=\{u\in U:\alpha(u)=0\},\qquad \operatorname{im}\alpha=\{\alpha(u):u\in U\}.$$

:::

::: {#fig-linear-maps-and-isomorphisms-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[tintA, draw=ink] (0,0) ellipse (1.1 and 1.6); \node[lab] at (0,1.85) {$U$};
\draw[tintB, draw=ink] (4,0) ellipse (1.1 and 1.6); \node[lab] at (4,1.85) {$V$};
\draw[regionA] (0,-0.75) ellipse (0.7 and 0.45); \node[lab] at (0,-0.75) {$\ker\alpha$};
\draw[regionB] (4,0.35) ellipse (0.75 and 0.8); \node[lab] at (4,0.6) {$\operatorname{Im}\alpha$};
\node[dot] (z) at (4,0) {}; \node[lab, below] at (4,0) {$0$};
\draw[map] (0.3,-0.65) to[bend right=12] (z);
\draw[map] (0.2,0.7) to[bend left=12] node[lab, above] {$\alpha$} (3.8,0.9);
\end{tikzpicture}
\end{center}
```

A linear map $\alpha:U\to V$ sends the whole kernel to $0$; its image is a subspace of $V$. $\alpha$ is injective when $\ker\alpha=\{0\}$ and surjective when $\operatorname{Im}\alpha=V$.

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

::: {#fig-linear-maps-and-isomorphisms-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, muted] (-0.3,0) -- (4.3,0) node[right, lab, tick] {$t$}; \draw[->, muted] (0,-0.3) -- (0,2.6);
\draw[emph, primary] (0.500,-0.350) -- (0.537,-0.231) -- (0.575,-0.116) -- (0.613,-0.003) -- (0.650,0.108) -- (0.688,0.215) -- (0.725,0.319) -- (0.762,0.421) -- (0.800,0.520) -- (0.837,0.616) -- (0.875,0.709) -- (0.912,0.800) -- (0.950,0.887) -- (0.988,0.972) -- (1.025,1.054) -- (1.062,1.134) -- (1.100,1.210) -- (1.137,1.284) -- (1.175,1.354) -- (1.212,1.422) -- (1.250,1.488) -- (1.288,1.550) -- (1.325,1.609) -- (1.362,1.666) -- (1.400,1.720) -- (1.438,1.771) -- (1.475,1.819) -- (1.512,1.865) -- (1.550,1.908) -- (1.587,1.947) -- (1.625,1.984) -- (1.662,2.019) -- (1.700,2.050) -- (1.738,2.079) -- (1.775,2.104) -- (1.812,2.127) -- (1.850,2.147) -- (1.887,2.165) -- (1.925,2.179) -- (1.962,2.191) -- (2.000,2.200) -- (2.037,2.206) -- (2.075,2.209) -- (2.112,2.210) -- (2.150,2.208) -- (2.188,2.202) -- (2.225,2.194) -- (2.263,2.184) -- (2.300,2.170) -- (2.337,2.154) -- (2.375,2.134) -- (2.412,2.112) -- (2.450,2.088) -- (2.487,2.060) -- (2.525,2.029) -- (2.562,1.996) -- (2.600,1.960) -- (2.637,1.921) -- (2.675,1.879) -- (2.712,1.835) -- (2.750,1.788) -- (2.788,1.737) -- (2.825,1.684) -- (2.862,1.629) -- (2.900,1.570) -- (2.938,1.509) -- (2.975,1.444) -- (3.012,1.377) -- (3.050,1.308) -- (3.087,1.235) -- (3.125,1.159) -- (3.163,1.081) -- (3.200,1.000) -- (3.237,0.916) -- (3.275,0.829) -- (3.312,0.740) -- (3.350,0.647) -- (3.387,0.552) -- (3.425,0.454) -- (3.462,0.354) -- (3.500,0.250);
\fill[accent] (1,1.0) circle[pt]; \draw[faint, dashed] (1,0) node[below, lab, tick] {$a_1$} -- (1,1.0);
\fill[accent] (2,2.2) circle[pt]; \draw[faint, dashed] (2,0) node[below, lab, tick] {$a_2$} -- (2,2.2);
\fill[accent] (3,1.4) circle[pt]; \draw[faint, dashed] (3,0) node[below, lab, tick] {$a_3$} -- (3,1.4);
\node[lab, note, anchor=west, align=left] at (4.5,1.2) {$\operatorname{ev}:F[t]_{<3}\to F^3$\\$p\mapsto(p(a_1),p(a_2),p(a_3))$\\exactly one $p$ for each list of values};
\end{tikzpicture}
\end{center}
```

Item 2 of @exm-linear-maps-abstract for $n=3$: a polynomial of degree $<3$ is the same information as its values at three distinct points. Both spaces have dimension $3$ and the evaluation map is an isomorphism between them.

:::

Choosing a basis $e_1,\dots,e_n$ of $V$ is the same as choosing an isomorphism $F^n\to V$, $(\lambda_i)\mapsto\sum\lambda_ie_i$; its inverse sends a vector to its *coordinates*. The isomorphism is not canonical: it depends on the basis.

::: {#exm-linear-maps-abstract .example name="Linear maps without matrices in sight"}

1. Differentiation $D:F[t]\to F[t]$, $p\mapsto p'$, is linear. Over $\mathbb R$ its kernel is the constants and it is surjective.
2. For distinct $a_1,\dots,a_n\in F$, evaluation $\operatorname{ev}:F[t]_{<n}\to F^n$, $p\mapsto(p(a_1),\dots,p(a_n))$, is linear between spaces of dimension $n$. Its kernel is $\{0\}$, since a non-zero polynomial of degree $<n$ has fewer than $n$ roots (@thm-at-most-d-roots). So it is an isomorphism (by @thm-rank-nullity it is then surjective), which is Lagrange interpolation.
3. On $\mathbb R^{\mathbb N}$, the shift $(x_1,x_2,\dots)\mapsto(x_2,x_3,\dots)$ is surjective but not injective, and $(x_1,x_2,\dots)\mapsto(0,x_1,x_2,\dots)$ is injective but not surjective. In infinite dimensions a space can be isomorphic to a proper subspace of itself.

:::

::: {#fig-linear-maps-and-isomorphisms-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.00,0.8) rectangle (0.60,1.3); \node[lab] at (0.30,1.05) {$x_1$};
\draw[cell frame] (0.60,0.8) rectangle (1.20,1.3); \node[lab] at (0.90,1.05) {$x_2$};
\draw[cell frame] (1.20,0.8) rectangle (1.80,1.3); \node[lab] at (1.50,1.05) {$x_3$};
\draw[cell frame] (1.80,0.8) rectangle (2.40,1.3); \node[lab] at (2.10,1.05) {$x_4$};
\node[lab] at (2.65,1.05) {$\cdots$};
\draw[->] (3.0,1.05) -- (3.8,1.05) node[midway, above, lab, note] {left};
\draw[cell frame] (4.00,0.8) rectangle (4.60,1.3); \node[lab] at (4.30,1.05) {$x_2$};
\draw[cell frame] (4.60,0.8) rectangle (5.20,1.3); \node[lab] at (4.90,1.05) {$x_3$};
\draw[cell frame] (5.20,0.8) rectangle (5.80,1.3); \node[lab] at (5.50,1.05) {$x_4$};
\draw[cell frame] (5.80,0.8) rectangle (6.40,1.3); \node[lab] at (6.10,1.05) {$x_5$};
\node[lab] at (6.65,1.05) {$\cdots$};
\node[lab, note, anchor=west] at (7.0,1.05) {onto, not one-to-one ($x_1$ is lost)};
\draw[cell frame] (0.00,-0.3) rectangle (0.60,0.2); \node[lab] at (0.30,-0.05) {$x_1$};
\draw[cell frame] (0.60,-0.3) rectangle (1.20,0.2); \node[lab] at (0.90,-0.05) {$x_2$};
\draw[cell frame] (1.20,-0.3) rectangle (1.80,0.2); \node[lab] at (1.50,-0.05) {$x_3$};
\draw[cell frame] (1.80,-0.3) rectangle (2.40,0.2); \node[lab] at (2.10,-0.05) {$x_4$};
\node[lab] at (2.65,-0.05) {$\cdots$};
\draw[->] (3.0,-0.05) -- (3.8,-0.05) node[midway, above, lab, note] {right};
\draw[hl cell] (4.00,-0.3) rectangle (4.60,0.2); \node[lab] at (4.30,-0.05) {$0$};
\draw[cell frame] (4.60,-0.3) rectangle (5.20,0.2); \node[lab] at (4.90,-0.05) {$x_1$};
\draw[cell frame] (5.20,-0.3) rectangle (5.80,0.2); \node[lab] at (5.50,-0.05) {$x_2$};
\draw[cell frame] (5.80,-0.3) rectangle (6.40,0.2); \node[lab] at (6.10,-0.05) {$x_3$};
\node[lab] at (6.65,-0.05) {$\cdots$};
\node[lab, note, anchor=west] at (7.0,-0.05) {one-to-one, not onto (first entry $0$)};
\end{tikzpicture}
\end{center}
```

Item 3 of @exm-linear-maps-abstract: the two shifts on sequences. In finite dimensions a map from a space to itself is one-to-one exactly when it is onto; for infinite sequences these two maps show that this fails.

:::
