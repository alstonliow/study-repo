---
title: "Determinants over a Field and Volume Forms"
sources: [camib-la-5, mit1806-18, mit1806-20]
requires: [math/linear-algebra/linear-maps/equivalence-and-rank]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Chapter 5, in our own wording; examples ours (checked with sympy); proofs written out in steps. MIT 18.06 defines the determinant by three row properties over R (def-determinant-properties) and derives the big formula, product rule, cofactors and the inverse formula; the versions here start from the permutation formula, work over any field (including characteristic 2, where "swapping changes the sign" no longer implies "equal rows give 0") and carry generalizes= or related=. Merges proposed to the owner. -->

<!-- Merged 2026-11-20 (owner): thm-product-rule-determinants (18.06 L18) merged into thm-determinant-multiplicative; thm-inverse-by-cofactors (L20) merged into thm-adjugate, which gained the cofactor form adj A = C^T. -->

The sign of a permutation is taken from group theory: there is a unique map $\varepsilon:S_n\to\{\pm1\}$ with $\varepsilon(\sigma\tau)=\varepsilon(\sigma)\varepsilon(\tau)$ and $\varepsilon(\tau)=-1$ for every transposition $\tau$; $\varepsilon(\sigma)=(-1)^{k}$ when $\sigma$ is a product of $k$ transpositions. Columns of $A$ are written $A^{(1)},\dots,A^{(n)}$.

::: {#def-determinant-leibniz .definition name="Determinant over a field" related="thm-big-formula-determinant"}

For $A\in\operatorname{Mat}_n(F)$,
$$\det A=\sum_{\sigma\in S_n}\varepsilon(\sigma)\prod_{i=1}^na_{i\sigma(i)}.$$

:::

::: {#lem-determinant-transpose .lemma name="Transpose and triangular matrices"}

1. $\det A^{\mathsf T}=\det A$.
2. If $A$ is upper (or lower) triangular, $\det A=a_{11}a_{22}\cdots a_{nn}$.

:::

::: {.proof}

1. $\det A^{\mathsf T}=\sum_\sigma\varepsilon(\sigma)\prod_ia_{\sigma(i)i}$. Re-index the product by $j=\sigma(i)$: it is $\prod_ja_{j\sigma^{-1}(j)}$. As $\sigma$ runs over $S_n$ so does $\sigma^{-1}$, and $\varepsilon(\sigma^{-1})=\varepsilon(\sigma)$. So the sum is $\det A$.

2. If $A$ is upper triangular and $\sigma\ne\mathrm{id}$, some $i$ has $\sigma(i)<i$ (otherwise $\sigma(n)=n$, then $\sigma(n-1)=n-1$, and so on), so the term contains $a_{i\sigma(i)}=0$. Only $\sigma=\mathrm{id}$ survives. Lower triangular follows by item 1.

:::

::: {#def-volume-form .definition name="Volume form"}

A *volume form* on $F^n$ is a map $d:F^n\times\dots\times F^n\to F$ ($n$ arguments) that is

1. *multilinear*: linear in each argument when the others are fixed;
2. *alternating*: $d(v_1,\dots,v_n)=0$ whenever $v_i=v_j$ for some $i\ne j$.

:::

::: {#fig-determinants-over-a-field-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.1]
\draw[->, faint] (-0.4,0) -- (3.2,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.4) -- (0,2.2) node[lab, above] {$y$};
\fill[shade] (0,0) rectangle (1,1); \node[lab, tick] at (0.5,0.5) {$1$};
\fill[tintB] (0,0) -- (2,0.5) -- (3,2) -- (1,1.5) -- cycle;
\draw (0,0) -- (2,0.5) -- (3,2) -- (1,1.5) -- cycle;
\draw[->, emph] (0,0) -- (2,0.5) node[lab, below right] {$Ae_1$};
\draw[->, emph] (0,0) -- (1,1.5) node[lab, above left] {$Ae_2$};
\node[lab] at (2.0,1.0) {$\det A$};
\end{tikzpicture}
\end{center}
```

Over $\mathbb R$ the determinant is the volume form normalised on the unit cube: for $A=\begin{bmatrix}2&1\\0.5&1.5\end{bmatrix}$ the image of the unit square has signed area $\det A=2.5$. Over a general field only the algebraic rules (multilinear, alternating) remain.

:::

::: {#lem-volume-form-permutation .lemma name="Volume forms change sign"}

Let $d$ be a volume form. Exchanging two arguments multiplies $d$ by $-1$, and for $\sigma\in S_n$,
$$d(v_{\sigma(1)},\dots,v_{\sigma(n)})=\varepsilon(\sigma)\,d(v_1,\dots,v_n).$$

:::

::: {.proof}

1. Put $v_i+v_j$ in both slots $i$ and $j$ and expand by multilinearity: $0=d(\dots,v_i+v_j,\dots,v_i+v_j,\dots)=d(\dots v_i\dots v_i\dots)+d(\dots v_i\dots v_j\dots)+d(\dots v_j\dots v_i\dots)+d(\dots v_j\dots v_j\dots)$. The first and last terms vanish, so the middle two are negatives.

2. Write $\sigma$ as a product of $k$ transpositions; each multiplies $d$ by $-1$, and $(-1)^k=\varepsilon(\sigma)$.

:::

::: {#fig-determinants-over-a-field-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[shift={(0,0)}]
\fill[tintA] (0.000,0.000) -- (1.600,0.300) -- (2.000,1.600) -- (0.400,1.300) -- cycle;
\draw[->, emph, primary] (0,0) -- (1.6, 0.3) node[below right, lab] {$v_1$};
\draw[->, emph, secondary] (0,0) -- (0.4, 1.3) node[left, lab] {$v_2$};
\draw[->, accent] (0.72,0.14) arc[start angle=10.6, end angle=72.9, radius=0.73];
\node[lab, note] at (0.8,-0.5) {$d(v_1,v_2)>0$};
\end{scope}
\begin{scope}[shift={(4,0)}]
\fill[tintB] (0.000,0.000) -- (1.600,0.300) -- (2.000,1.600) -- (0.400,1.300) -- cycle;
\draw[->, emph, primary] (0,0) -- (1.6, 0.3) node[below right, lab] {$v_1$};
\draw[->, emph, secondary] (0,0) -- (0.4, 1.3) node[left, lab] {$v_2$};
\draw[->, accent] (0.18,0.59) arc[start angle=72.9, end angle=10.6, radius=0.61];
\node[lab, note] at (0.8,-0.5) {$\;d(v_2,v_1)=-d(v_1,v_2)$};
\end{scope}
\end{tikzpicture}
\end{center}
```

A volume form measures oriented area. Swapping the two arguments keeps the parallelogram but reverses the direction of turning from the first vector to the second, and the sign changes.

:::

::: {#thm-volume-forms-unique .theorem name="Volume forms are multiples of the determinant"}

$A\mapsto\det A$, viewed as a function of the columns $A^{(1)},\dots,A^{(n)}$, is a volume form. Every volume form $d$ on $F^n$ satisfies
$$d(A^{(1)},\dots,A^{(n)})=d(e_1,\dots,e_n)\,\det A.$$
So the determinant is the unique volume form with $d(e_1,\dots,e_n)=1$.

:::

::: {.proof}

1. $\det$ is multilinear in the columns: each term $\prod_ia_{i\sigma(i)}$ contains exactly one entry from each column.

2. $\det$ is alternating: suppose columns $j\ne k$ are equal and let $\tau=(j\ k)$. The map $\sigma\mapsto\tau\sigma$ pairs the even permutations with the odd ones. Since columns $j$ and $k$ agree, $a_{i,\tau\sigma(i)}$ and $a_{i,\sigma(i)}$ are equal for every $i$, so the terms for $\sigma$ and $\tau\sigma$ have the same product and opposite signs, and cancel. (Using $\det A^{\mathsf T}=\det A$, rows and columns may be swapped in this argument.)

3. For any volume form $d$, expand each column $A^{(j)}=\sum_ia_{ij}e_i$ by multilinearity:
$$d(A^{(1)},\dots,A^{(n)})=\sum_{i_1,\dots,i_n}a_{i_11}\cdots a_{i_nn}\,d(e_{i_1},\dots,e_{i_n}).$$

4. Terms with two equal indices vanish (alternating). The others have $i_j=\rho(j)$ for a permutation $\rho$, and $d(e_{\rho(1)},\dots,e_{\rho(n)})=\varepsilon(\rho)d(e_1,\dots,e_n)$ by @lem-volume-form-permutation.

5. So $d(A^{(1)},\dots,A^{(n)})=d(e_1,\dots,e_n)\sum_\rho\varepsilon(\rho)\prod_ja_{\rho(j)j}=d(e_1,\dots,e_n)\det A^{\mathsf T}$, which is $d(e_1,\dots,e_n)\det A$ by @lem-determinant-transpose.

:::

::: {#thm-determinant-multiplicative .theorem name="The determinant is multiplicative"}

For $A,B\in\operatorname{Mat}_n(F)$, $\det(AB)=\det A\det B$.

:::

::: {.proof}

1. Fix $A$ and let $d(v_1,\dots,v_n)=\det[Av_1\ \cdots\ Av_n]$. Since $v\mapsto Av$ is linear and $\det$ is a volume form, $d$ is multilinear and alternating.

2. By @thm-volume-forms-unique, $d(B^{(1)},\dots,B^{(n)})=d(e_1,\dots,e_n)\det B$.

3. The left side is $\det(AB)$, because column $j$ of $AB$ is $AB^{(j)}$; and $d(e_1,\dots,e_n)=\det A$.

:::

::: {#fig-determinants-over-a-field-5}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintD] (0,0) rectangle (1,1); \draw[faint] (0,0) rectangle (1,1); \node[lab, note] at (0.5,-0.3) {area $1$};
\draw[->] (1.3,0.5) -- (2.2,0.5) node[midway, above, lab, note] {$B$};
\begin{scope}[shift={(2.6,0)}]
\fill[tintA] (0.000,0.000) -- (1.500,0.000) -- (2.000,1.000) -- (0.500,1.000) -- cycle;
\node[lab, note] at (1,-0.3) {$\times\det B$};
\end{scope}
\draw[->] (4.9,0.5) -- (5.8,0.5) node[midway, above, lab, note] {$A$};
\begin{scope}[shift={(6.2,0)}]
\fill[tintB] (0.000,0.000) -- (1.800,0.400) -- (2.600,1.600) -- (0.800,1.200) -- cycle;
\node[lab, note] at (1.3,-0.3) {$\times\det A\det B$};
\end{scope}
\end{tikzpicture}
\end{center}
```

Over $\mathbb R$, $\det(AB)=\det A\det B$ says that scale factors for volume multiply: $B$ scales every area by $\det B$, then $A$ scales the result by $\det A$.

:::

::: {#thm-determinant-invertible .theorem name="Invertibility and the determinant"}

For $A\in\operatorname{Mat}_n(F)$ the following are equivalent:

1. $A$ is invertible;
2. $\det A\ne0$;
3. $r(A)=n$, that is, the columns are linearly independent.

If $A$ is invertible, $\det(A^{-1})=(\det A)^{-1}$.

:::

::: {.proof}

1. (1)⇒(2): $1=\det I=\det(AA^{-1})=\det A\det A^{-1}$ by @thm-determinant-multiplicative.

2. (2)⇒(3): if the columns are dependent, say $A^{(j)}=\sum_{k\ne j}\lambda_kA^{(k)}$, expand column $j$ by multilinearity: each term has two equal columns, so $\det A=0$.

3. (3)⇒(1): a square matrix of rank $n$ is invertible (@cor-invertible-matrix-conditions).

:::

The determinant of an endomorphism is defined from any matrix representing it (@def-trace-determinant-endomorphism); by @thm-determinant-multiplicative similar matrices have equal determinants.

::: {#lem-block-triangular-determinant .lemma name="Block triangular determinants"}

For square matrices $A\in\operatorname{Mat}_k(F)$, $B\in\operatorname{Mat}_l(F)$ and any $C\in\operatorname{Mat}_{k,l}(F)$,
$$\det\begin{bmatrix}A&C\\0&B\end{bmatrix}=\det A\,\det B.$$

:::

::: {.proof}

1. Let $X$ be the block matrix. In $\det X=\sum_\sigma\varepsilon(\sigma)\prod_ix_{i\sigma(i)}$, a term is non-zero only if $\sigma$ sends every $i>k$ to some $\sigma(i)>k$, since $x_{ij}=0$ for $i>k\ge j$.

2. Such a $\sigma$ maps $\{k+1,\dots,k+l\}$ into, hence onto, itself, so it also maps $\{1,\dots,k\}$ onto itself: $\sigma=\sigma_1\sigma_2$ with $\sigma_1$ permuting the first $k$ indices and $\sigma_2$ the last $l$, and $\varepsilon(\sigma)=\varepsilon(\sigma_1)\varepsilon(\sigma_2)$.

3. The term is then $\varepsilon(\sigma_1)\prod_{i\le k}a_{i\sigma_1(i)}\cdot\varepsilon(\sigma_2)\prod_{i>k}x_{i\sigma_2(i)}$, which involves only $A$ and $B$. Summing over $\sigma_1$ and $\sigma_2$ independently gives $\det A\det B$.

:::

::: {#fig-determinants-over-a-field-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0,0) rectangle (2.4,-2.4);
\draw[hl cell] (0.0,0.0) rectangle (1.2,-1.2); \node[lab, tick] at (0.6,-0.6) {$A$};
\draw[hl cell] (1.2,-1.2) rectangle (2.4,-2.4); \node[lab, tick] at (1.80,-1.80) {$C$};
\node[lab] at (1.8,-0.6) {$B$}; \node[lab, muted] at (0.6,-1.8) {$0$};
\node[lab, anchor=west] at (2.8,-1.2) {$\det\begin{bmatrix}A&B\\0&C\end{bmatrix}=\det A\cdot\det C$};
\node[lab, note, anchor=west] at (2.8,-1.9) {the block $B$ does not matter};
\end{tikzpicture}
\end{center}
```

Block triangular determinants. In the big formula a permutation that picks an entry from the zero block contributes nothing, so only permutations that keep the first block of indices among themselves survive, and they split into a permutation for $A$ and one for $C$.

:::

By induction, a block upper triangular matrix has determinant the product of the determinants of its diagonal blocks.

::: {#thm-adjugate .theorem name="The adjugate"}

Let $\hat A_{ij}$ be $A$ with row $i$ and column $j$ deleted, and let $\operatorname{adj}A$ be the matrix with $(\operatorname{adj}A)_{ij}=(-1)^{i+j}\det\hat A_{ji}$. Then
$$(\operatorname{adj}A)\,A=A\,(\operatorname{adj}A)=(\det A)\,I.$$
In particular $A^{-1}=\frac1{\det A}\operatorname{adj}A$ when $\det A\ne0$. In terms of the cofactors $C_{ij}=(-1)^{i+j}\det\hat A_{ij}$ (@def-cofactor), $\operatorname{adj}A=C^{\mathsf T}$.

:::

::: {.proof}

1. Expansion along column $k$: $\det A=\sum_ia_{ik}(-1)^{i+k}\det\hat A_{ik}$. Indeed, writing $A^{(k)}=\sum_ia_{ik}e_i$ and using multilinearity, $\det A=\sum_ia_{ik}\det B_i$, where $B_i$ is $A$ with column $k$ replaced by $e_i$. Move column $k$ of $B_i$ to the end by $n-k$ adjacent column exchanges and row $i$ to the bottom by $n-i$ adjacent row exchanges (each changes the sign, by @lem-volume-form-permutation and, for rows, @lem-determinant-transpose). The result is $\begin{bmatrix}\hat A_{ik}&0\\ \ast&1\end{bmatrix}$, whose determinant is $\det\hat A_{ik}$ by @lem-block-triangular-determinant (transposed). So $\det B_i=(-1)^{(n-k)+(n-i)}\det\hat A_{ik}=(-1)^{i+k}\det\hat A_{ik}$. This is @thm-cofactor-expansion, now valid over any field.

2. $[(\operatorname{adj}A)A]_{jk}=\sum_i(-1)^{i+j}\det\hat A_{ij}\,a_{ik}$. For $j=k$ this is the expansion of $\det A$ along column $k$.

3. For $j\ne k$, let $B$ be $A$ with column $j$ replaced by column $k$. Deleting column $j$ gives $\hat B_{ij}=\hat A_{ij}$, so the sum is the expansion of $\det B$ along column $j$. $B$ has two equal columns, so $\det B=0$.

4. Applying this to $A^{\mathsf T}$ and transposing gives $A(\operatorname{adj}A)=(\det A)I$, since $\operatorname{adj}(A^{\mathsf T})=(\operatorname{adj}A)^{\mathsf T}$.

:::

::: {#fig-determinants-over-a-field-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$a$};
\draw[cell frame] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$b$};
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$c$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$d$};
\node[lab, note] at (0.550,-0.350) {$A$};
\draw[->] (1.3,0.55) -- (2.3,0.55) node[midway, above, lab, tick] {adjugate};
\draw[hl cell] (2.500,0.550) rectangle (3.050,1.100);
\node[lab] at (2.775,0.825) {$d$};
\draw[cell, fill=primaryLight] (3.050,0.550) rectangle (3.600,1.100);
\node[lab] at (3.325,0.825) {$-b$};
\draw[cell, fill=primaryLight] (2.500,0.000) rectangle (3.050,0.550);
\node[lab] at (2.775,0.275) {$-c$};
\draw[hl cell] (3.050,0.000) rectangle (3.600,0.550);
\node[lab] at (3.325,0.275) {$a$};
\node[lab, note] at (3.050,-0.350) {$\operatorname{adj}A$};
\node[lab, anchor=west, align=left] at (3.9,0.55) {$\operatorname{adj}A\cdot A=\begin{bmatrix}ad-bc&0\\0&ad-bc\end{bmatrix}=(\det A)\,I$};
\end{tikzpicture}
\end{center}
```

The adjugate for $n=2$: swap the diagonal entries and negate the others. Entry $(i,j)$ of $\operatorname{adj}A$ is the cofactor $C_{ji}$; the off-diagonal products vanish because they expand a matrix with two equal rows.

:::


::: {#exm-determinant-characteristic-two .example name="Characteristic two"}

Over $\mathbb F_2$, $-1=1$, so $\varepsilon$ is always $1$ and the determinant is the *permanent* $\sum_\sigma\prod_ia_{i\sigma(i)}$. Swapping two columns does not change it, yet a matrix with two equal columns still has determinant $0$: for $\begin{bmatrix}a&a\\b&b\end{bmatrix}$ it is $ab+ab=2ab=0$. This is why the alternating property, not the sign change, is the right axiom over a general field.

:::
