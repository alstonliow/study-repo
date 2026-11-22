---
title: "Trace, Determinant and Eigenvalues of an Endomorphism"
sources: [camib-la-6, mit1806-31, mit1806-22]
requires: [math/linear-algebra/endomorphisms/determinants-over-a-field]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 6.1, in our own wording; examples ours (checked with sympy); proofs written out in steps. MIT 18.06 covers similar matrices, eigenvalues and diagonalization for real and complex matrices (def-similar-matrices, def-eigenvalue, thm-distinct-eigenvalues-independent, thm-diagonalization); the basis-free versions here carry generalizes=. Merges proposed to the owner. -->

<!-- Merged 2026-11-20 (owner): thm-change-of-basis-similar (18.06 L31) merged into prp-endomorphism-change-of-basis; thm-distinct-eigenvalues-independent (L22) merged into lem-eigenspaces-independent, its "n distinct eigenvalues give a diagonalisable matrix" part added to thm-diagonalizable-iff-eigenspaces. -->

An *endomorphism* of $V$ is a linear map $\alpha:V\to V$; they form the space $\operatorname{End}(V)=\mathcal L(V,V)$, and $\iota$ denotes the identity. Throughout, $V$ is finite-dimensional over $F$ with $\dim V=n$, and an endomorphism is represented using the same basis $\mathcal B$ for input and output: $[\alpha]_{\mathcal B}=[\alpha]_{\mathcal B,\mathcal B}$.

::: {#prp-endomorphism-change-of-basis .proposition name="Similar matrices" generalizes="def-similar-matrices"}

If $P$ is the change of basis matrix from $\mathcal B$ to $\mathcal B'$, then $[\alpha]_{\mathcal B'}=P^{-1}[\alpha]_{\mathcal B}P$. Two matrices $A,B\in\operatorname{Mat}_n(F)$ represent the same endomorphism in two bases if and only if they are *similar*: $B=P^{-1}AP$ for some $P\in\operatorname{GL}_n(F)$.

:::

::: {.proof}

1. This is @thm-change-of-basis-two-spaces with $Q=P$.

2. Conversely, if $B=P^{-1}AP$, let $\alpha$ be $\mathbf x\mapsto A\mathbf x$ and take the columns of $P$ as a new basis; then $[\alpha]$ in the new basis is $B$.

:::

::: {#fig-eigenvalues-of-endomorphisms-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (a) at (0,1.5) {$V$, basis $\mathcal B$};
\node[box] (b) at (4.6,1.5) {$V$, basis $\mathcal B$};
\node[box] (c) at (0,0) {$V$, basis $\mathcal B'$};
\node[box] (d) at (4.6,0) {$V$, basis $\mathcal B'$};
\draw[->, emph] (a) -- (b) node[midway, above, lab] {$A$};
\draw[->, emph, accent] (c) -- (d) node[midway, below, lab] {$P^{-1}AP$};
\draw[->, emph] (c) -- (a) node[midway, left, lab] {$P$};
\draw[->, emph] (b) -- (d) node[midway, right, lab] {$P^{-1}$};
\end{tikzpicture}
\end{center}
```

For an endomorphism one basis serves for both the input and the output, so the change-of-basis matrix appears on both sides: $P^{-1}AP$ instead of $Q^{-1}AP$. Trace, determinant and characteristic polynomial survive this change.

:::

So a property of square matrices that is invariant under similarity is a property of the endomorphism. Classifying endomorphisms means classifying matrices up to similarity, which is much harder than equivalence (where only the rank survives, @thm-rank-normal-form).

::: {#lem-trace-cyclic .lemma name="Trace of a product"}

For $A\in\operatorname{Mat}_{n,m}(F)$ and $B\in\operatorname{Mat}_{m,n}(F)$, $\operatorname{tr}(AB)=\operatorname{tr}(BA)$. Hence similar matrices have the same trace: $\operatorname{tr}(P^{-1}AP)=\operatorname{tr}(APP^{-1})=\operatorname{tr}A$.

:::

::: {.proof}

$\operatorname{tr}(AB)=\sum_i\sum_ja_{ij}b_{ji}=\sum_j\sum_ib_{ji}a_{ij}=\operatorname{tr}(BA)$.

:::

::: {#fig-eigenvalues-of-endomorphisms-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0,0) rectangle (1.6,-0.8); \node[lab] at (0.8,-0.4) {$A$};
\draw[cell frame] (1.8,0) rectangle (2.6,-1.6); \node[lab] at (2.2,-0.8) {$B$};
\draw[hl cell] (3.0,0) rectangle (3.8,-0.8); \node[lab] at (3.4,-0.4) {$AB$};
\node[lab, tick] at (3.4,-1.0) {$m\times m$};
\draw[cell frame] (5,0) rectangle (5.8,-1.6); \node[lab] at (5.4,-0.8) {$B$};
\draw[cell frame] (6.0,0) rectangle (7.6,-0.8); \node[lab] at (6.8,-0.4) {$A$};
\draw[hl cell] (8.0,0) rectangle (9.6,-1.6); \node[lab] at (8.8,-0.8) {$BA$};
\node[lab, tick] at (8.8,-1.8) {$n\times n$};
\node[lab, anchor=west] at (0,-2.4) {different sizes, same trace: $\operatorname{tr}(AB)=\sum_{i,j}a_{ij}b_{ji}=\operatorname{tr}(BA)$};
\end{tikzpicture}
\end{center}
```

$AB$ and $BA$ can even have different sizes, but both traces add up the same products $a_{ij}b_{ji}$. With $B=P^{-1}$ and $A=XP$ this shows that similar matrices have the same trace.

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

::: {#lem-eigenspaces-independent .lemma name="Eigenspaces form a direct sum"}

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

In particular, if $\alpha$ has $n=\dim V$ distinct eigenvalues, it is diagonalisable.

:::

::: {.proof}

1. (1)⇒(2): a basis of eigenvectors lies in $\sum E(\lambda_i)$, so this sum is $V$, and it is direct by @lem-eigenspaces-independent.

2. (2)⇒(1): concatenating bases of the $E(\lambda_i)$ gives a basis of $V$ (@prp-direct-sum-criteria) made of eigenvectors.

3. (2)⇔(3): the sum is direct by @lem-eigenspaces-independent, so its dimension is $\sum\dim E(\lambda_i)$ (@prp-direct-sum-criteria), and a subspace of dimension $n$ is $V$.

4. With $n$ distinct eigenvalues each $\dim E(\lambda_i)\ge1$, so the sum in (3) is at least $n$, hence equal to $n$.

:::

::: {#fig-eigenvalues-of-endomorphisms-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell, fill=primaryLight] (1.80,0.00) rectangle (2.55,0.45);
\draw[cell, fill=primaryLight] (2.55,0.00) rectangle (3.30,0.45);
\node[lab, tick] at (2.55,-0.22) {$E(2)$};
\draw[cell, fill=accentLight] (3.30,0.00) rectangle (4.05,0.45);
\node[lab, tick] at (3.67,-0.22) {$E(3)$};
\node[lab, anchor=east] at (1.70,0.23) {$\operatorname{diag}(2,2,3)$};
\draw[cell, fill=primaryLight] (1.80,-1.00) rectangle (2.55,-0.55);
\node[lab, tick] at (2.17,-1.22) {$E(2)$};
\draw[cell frame] (2.55,-1.00) rectangle (3.30,-0.55);
\draw[cell, fill=accentLight] (3.30,-1.00) rectangle (4.05,-0.55);
\node[lab, tick] at (3.67,-1.22) {$E(3)$};
\node[lab, anchor=east] at (1.70,-0.78) {$\begin{bmatrix}2&1&0\\0&2&0\\0&0&3\end{bmatrix}$};
\node[lab, note, anchor=west, align=left] at (4.3,-0.3) {diagonalisable exactly when\\the eigenspaces fill $V$:\\$\sum_\lambda\dim E(\lambda)=\dim V$};
\end{tikzpicture}
\end{center}
```

Two maps with the same characteristic polynomial $(t-2)^2(t-3)$, one cell per dimension. The eigenspaces always form a direct sum (@lem-eigenspaces-independent); the second map is not diagonalisable because its eigenspace for $2$ is one dimension short.

:::

::: {#exm-endomorphism-not-diagonalisable .example name="Diagonalisable over one field, not another"}

$A=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$ is not diagonalisable over $\mathbb R$ (no eigenvalues), but over $\mathbb C$ its eigenvalues $i,-i$ are distinct and $E(i)\oplus E(-i)=\mathbb C^2$ with $E(\pm i)=\langle(1,\mp i)^{\mathsf T}\rangle$. The matrix $\begin{bmatrix}1&1\\0&1\end{bmatrix}$ is diagonalisable over no field: its only eigenvalue is $1$ and $E(1)=\langle e_1\rangle$ has dimension $1<2$. Over $\mathbb F_2$, $\begin{bmatrix}0&1\\1&0\end{bmatrix}$ has $\chi(t)=t^2-1=(t-1)^2$ and $E(1)=\langle(1,1)^{\mathsf T}\rangle$, so the swap matrix, diagonalisable over $\mathbb R$, is not diagonalisable over $\mathbb F_2$.

:::

::: {#fig-eigenvalues-of-endomorphisms-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.2]
\draw[->, faint] (-0.4,0) -- (2.6,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.4) -- (0,1.6) node[lab, above] {$y$};
\draw[faint, dashed] (0,0) rectangle (1,1);
\fill[tintA] (0,0) -- (1,0) -- (2,1) -- (1,1) -- cycle;
\draw (0,0) -- (1,0) -- (2,1) -- (1,1) -- cycle;
\draw[hl] (-0.4,0) -- (2.4,0) node[lab, below, pos=0.95] {$E(1)$};
\draw[->, emph] (0,0) -- (0,1) node[lab, left] {$e_2$};
\draw[->, emph] (0,0) -- (1,1) node[lab, above] {$Ae_2$};
\end{tikzpicture}
\end{center}
```

The shear $A=\begin{bmatrix}1&1\\0&1\end{bmatrix}$ moves the unit square to a parallelogram. Only vectors on the $x$-axis keep their direction, so there is one eigenline $E(1)$ and no basis of eigenvectors.

:::
