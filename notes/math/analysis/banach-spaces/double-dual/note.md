---
title: "The Double Dual and Reflexivity"
sources: [camii-lan-1, camii-lans-1]
requires: [math/analysis/banach-spaces/hahn-banach, math/analysis/banach-spaces/sequence-spaces]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Linear Analysis (lecture notes), Sections 1.4 and 1.7, in our own wording; proofs written out in steps. Example Sheet 1 question 4 (duals of the sequence spaces) is in math/analysis/banach-spaces/sequence-spaces. -->

Every vector $x$ gives a functional on $X^*$ by evaluation. The Hahn–Banach theorem shows this is an isometry; whether it is onto is the question of reflexivity.

::: {#def-canonical-embedding .definition name="Canonical embedding into the double dual"}

For a normed space $X$ let $X^{**}=(X^*)^*$. The *canonical map* $J:X\to X^{**}$ is $(Jx)(F)=F(x)$.

:::

::: {#fig-double-dual-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (a) at (0,0) {$X$}; \node[box] (b) at (3,0) {$X^*$}; \node[box] (c) at (6,0) {$X^{**}$};
\draw[map] (a) -- (b); \draw[map] (b) -- (c);
\draw[map, hl] (a) to[bend left=35] node[lab, above] {$J$} (c);
\node[lab, below] at (3,-0.7) {$(Jx)(F)=F(x)$};
\end{tikzpicture}
\end{center}
```

The canonical embedding $J$ of $X$ into its double dual.

:::

::: {#thm-canonical-embedding-isometry .theorem name="$J$ is an isometric embedding"}

$J$ is linear and $\|Jx\|=\|x\|$ for all $x$. Hence $X$ is isometrically isomorphic to a subspace of $X^{**}$, and $\overline{J(X)}$ is a completion of $X$.

:::

::: {.proof}

1. $|(Jx)(F)|=|F(x)|\le\|F\|\|x\|$, so $\|Jx\|\le\|x\|$.

2. By @cor-hahn-banach-separates (ii) there is $F$ with $\|F\|\le1$ and $F(x)=\|x\|$, so $\|Jx\|\ge\|x\|$.

3. $X^{**}$ is a Banach space (@cor-dual-banach), so the closure of $J(X)$ is a complete space containing an isometric copy of $X$ as a dense subspace.

:::

::: {#def-reflexive-banach .definition name="Reflexive space"}

$X$ is *reflexive* if $J(X)=X^{**}$, i.e. $J$ is an (isometric) isomorphism onto the double dual.

:::

::: {#prp-reflexive-banach .proposition name="Reflexive spaces are complete"}

A reflexive normed space is a Banach space. Finite-dimensional spaces and $\ell^p$ for $1<p<\infty$ are reflexive; $c_0$, $\ell^1$ and $\ell^\infty$ are not.

:::

::: {.proof}

1. If $J$ is onto then $X\cong X^{**}$ isometrically, and $X^{**}$ is complete.

2. In finite dimensions $\dim X=\dim X^*=\dim X^{**}$ and $J$ is injective, hence onto.

3. For $1<p<\infty$ with conjugate $q$, @thm-dual-lp gives $(\ell^p)^*=\ell^q$ and $(\ell^q)^*=\ell^p$. Following the identifications, $J$ becomes the identity of $\ell^p$, so it is onto.

4. $c_0^{**}\cong(\ell^1)^*\cong\ell^\infty\supsetneq c_0$, compatibly with $J$ (the image of $J$ is $c_0$), so $c_0$ is not reflexive.

5. Using the two facts stated in the remark below: if $\ell^\infty$ were reflexive, its closed subspace $c_0$ would be too; and if $\ell^1$ were reflexive, so would be its dual $\ell^\infty$. Both contradict step 4.

:::

::: {#rmk-double-dual-1 .remark name="What is used in the last step"}

The last step uses two standard facts that follow from the Hahn–Banach theorem and which we do not prove here: a space is reflexive if and only if its dual is, and closed subspaces of reflexive spaces are reflexive.
<!-- TODO: write out the two facts (X reflexive iff X* reflexive; closed subspaces of reflexive spaces are reflexive) as blocks; the lecture notes only assert non-reflexivity of l1 and c0 via the sequence-space duals. -->

:::

::: {#prp-adjoint-norm .proposition name="The adjoint has the same norm"}

For $T\in B(X,Y)$, $\|T^*\|=\|T\|$, and $T^{**}\circ J_X=J_Y\circ T$.

:::

::: {.proof}

1. $\|T^*\|\le\|T\|$ was shown in @def-dual-operator.

2. For $x\in X$, @cor-hahn-banach-separates gives $G\in Y^*$ with $\|G\|\le1$ and $G(Tx)=\|Tx\|$. Then $\|Tx\|=(T^*G)(x)\le\|T^*\|\|x\|$, so $\|T\|\le\|T^*\|$.

3. $(T^{**}J_Xx)(G)=(J_Xx)(T^*G)=G(Tx)=(J_YTx)(G)$.

:::
