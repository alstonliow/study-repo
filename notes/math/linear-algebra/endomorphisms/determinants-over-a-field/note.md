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

::: {#lem-volume-form-permutation .lemma name="Volume forms change sign"}

Let $d$ be a volume form. Exchanging two arguments multiplies $d$ by $-1$, and for $\sigma\in S_n$,
$$d(v_{\sigma(1)},\dots,v_{\sigma(n)})=\varepsilon(\sigma)\,d(v_1,\dots,v_n).$$

:::

::: {.proof}

1. Put $v_i+v_j$ in both slots $i$ and $j$ and expand by multilinearity: $0=d(\dots,v_i+v_j,\dots,v_i+v_j,\dots)=d(\dots v_i\dots v_i\dots)+d(\dots v_i\dots v_j\dots)+d(\dots v_j\dots v_i\dots)+d(\dots v_j\dots v_j\dots)$. The first and last terms vanish, so the middle two are negatives.

2. Write $\sigma$ as a product of $k$ transpositions; each multiplies $d$ by $-1$, and $(-1)^k=\varepsilon(\sigma)$.

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


::: {#exm-determinant-characteristic-two .example name="Characteristic two"}

Over $\mathbb F_2$, $-1=1$, so $\varepsilon$ is always $1$ and the determinant is the *permanent* $\sum_\sigma\prod_ia_{i\sigma(i)}$. Swapping two columns does not change it, yet a matrix with two equal columns still has determinant $0$: for $\begin{bmatrix}a&a\\b&b\end{bmatrix}$ it is $ab+ab=2ab=0$. This is why the alternating property, not the sign change, is the right axiom over a general field.

:::
