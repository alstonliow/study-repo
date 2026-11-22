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

::: {#fig-direct-sums-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-1.2,-0.4) -- (3.3,1.1) node[lab, right] {$U$};
\draw[faint] (0.45,-0.9) -- (-1.0,2.0) node[lab, above] {$W$};
\draw[dashed] (2.4,0.8) -- (1.8,2.0) -- (-0.6,1.2);
\draw[->, hl] (0,0) -- (2.4,0.8) node[lab, below right] {$u\in U$};
\draw[->, hl] (0,0) -- (-0.6,1.2) node[lab, left] {$w\in W$};
\draw[->, emph] (0,0) -- (1.8,2.0) node[lab, above right] {$v=u+w$};
\node[dot] at (0,0) {}; \node[lab, below left] at (0,0) {$0$};
\end{tikzpicture}
\end{center}
```

$\mathbb R^2=U\oplus W$ for two different lines $U$ and $W$ through $0$: each $v$ splits as $u+w$ in exactly one way, along the parallelogram.

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

::: {#fig-direct-sums-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[x={(-0.5cm,-0.4cm)}, y={(1cm,0)}, z={(0,1cm)}]
\fill[tintA] (-1.2,-1.5,0) -- (1.8,-1.5,0) -- (1.8,1.8,0) -- (-1.2,1.8,0) -- cycle;
\fill[tintC] (-1.2,0,-1) -- (1.8,0,-1) -- (1.8,0,1.6) -- (-1.2,0,1.6) -- cycle;
\draw[bold, accent] (-1.2,0,0) -- (1.8,0,0);
\fill[ink] (0,0,0) circle[pt];
\node[lab, note, primary] at (0,1.7,0.25) {$U$}; \node[lab, note, secondary] at (0,0,1.85) {$W$}; \node[lab, note, accent] at (2.1,0,0.25) {$U\cap W$};
\end{scope}
\node[lab, note, anchor=west, align=left] at (2.6,0.2) {$U+W=\mathbb R^3$, but the sum is not direct:\\$\dim U+\dim W=4>3$, and a vector of\\$U\cap W$ can be moved between the parts};
\end{tikzpicture}
\end{center}
```

Two planes in $\mathbb R^3$ fail tests 2–4 of @prp-direct-sum-criteria: they meet in a line, so $0=u+(-u)$ with $u\in U\cap W$ is a non-trivial decomposition of $0$, and the dimensions add up to too much.

:::

For three or more subspaces, pairwise intersections $\{0\}$ are not enough: three distinct lines through $0$ in $\mathbb R^2$ meet pairwise in $\{0\}$, yet their sum $\mathbb R^2$ has dimension $2<3$.

::: {#prp-complements-exist .proposition name="Complements exist"}

Every subspace $U$ of a finite-dimensional space $V$ has a complement: there is $W\le V$ with $V=U\oplus W$.

:::

::: {.proof}

1. Extend a basis $u_1,\dots,u_m$ of $U$ to a basis $u_1,\dots,u_m,w_{m+1},\dots,w_n$ of $V$ (@cor-independent-set-extends-to-basis).

2. Let $W=\langle w_{m+1},\dots,w_n\rangle$. The concatenation of the bases of $U$ and $W$ is a basis of $V$, so $V=U\oplus W$ by @prp-direct-sum-criteria.

:::

::: {#fig-direct-sums-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[shift={(0,0)}]
\draw[->, muted] (-1.70,0) -- (1.8,0);
\draw[->, muted] (0,-1.70) -- (0,1.8);
\draw[bold, primary] (-1.6,0) -- (1.6,0) node[above, lab, note] {$U$};
\draw[emph, accent] (0,-1.5) -- (0,1.5) node[above, lab, note] {$W_1$};
\draw[emph, secondary] (-1.0,-1.5) -- (1.0,1.5) node[above, lab, note] {$W_2$};
\draw[emph, muted] (1.5,-1.0) -- (-1.5,1.0) node[above, lab, note] {$W_3$};
\end{scope}
\node[lab, note, anchor=west, align=left] at (2.2,0.2) {every line $W\ne U$ through $0$\\is a complement: $\mathbb R^2=U\oplus W$};
\end{tikzpicture}
\end{center}
```

Complements exist but are not unique: any line through $0$ other than $U$ itself completes $U$ to $\mathbb R^2$. Extending a basis of $U$ in different ways gives different complements.

:::

A complement is not unique: in $\mathbb R^2$ every line through $0$ other than $U$ itself is a complement of the line $U$. What is determined is its dimension $\dim V-\dim U$, and its isomorphism type, which is that of $V/U$ (@def-quotient-space).

::: {#def-external-direct-sum .definition name="External direct sum"}

For $F$-vector spaces $U_1,\dots,U_k$, the *external direct sum* $U_1\oplus\dots\oplus U_k$ is the set of tuples $(u_1,\dots,u_k)$ with $u_i\in U_i$, with entrywise addition and scalar multiplication.

:::

::: {#fig-direct-sums-5}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, muted] (-0.3,0) -- (3.2,0) node[right, lab] {$V$}; \draw[->, muted] (0,-0.3) -- (0,2.4) node[above, lab] {$W$};
\fill[ink] (2,1.5) circle[pt] node[above right, lab] {$(v,w)$};
\draw[faint, dashed] (2,1.5) -- (2,0) node[below, lab, tick] {$(v,0)$}; \draw[faint, dashed] (2,1.5) -- (0,1.5) node[left, lab, tick] {$(0,w)$};
\node[lab, note, anchor=west, align=left] at (3.6,1.2) {$V\oplus W=V\times W$ with\\$(v,w)+(v',w')=(v+v',w+w')$;\\$V\times\{0\}$ and $\{0\}\times W$ are an\\internal direct sum of it};
\end{tikzpicture}
\end{center}
```

The external direct sum drawn as a product with $V$ and $W$ as axes (each may have any dimension). Every pair splits uniquely as $(v,0)+(0,w)$.

:::

The two notions agree: the copies $\{(0,\dots,u_i,\dots,0)\}$ of the $U_i$ are subspaces of the external sum, which is their internal direct sum. Hence $\dim(U_1\oplus\dots\oplus U_k)=\sum\dim U_i$, and $F^n$ is the direct sum of $n$ copies of $F$.

::: {#exm-direct-sum-matrices .example name="Symmetric and antisymmetric matrices"}

Let $F$ be a field with $1+1\ne0$ (so not $\mathbb F_2$). Every $A\in\operatorname{Mat}_n(F)$ is
$$A=\tfrac12(A+A^{\mathsf T})+\tfrac12(A-A^{\mathsf T}),$$
a symmetric plus an antisymmetric matrix, and a matrix that is both has $A=A^{\mathsf T}=-A$, so $2A=0$ and $A=0$. Hence $\operatorname{Mat}_n(F)$ is the direct sum of the symmetric matrices (dimension $\frac{n(n+1)}2$) and the antisymmetric ones (dimension $\frac{n(n-1)}2$); the dimensions add up to $n^2$. Over $\mathbb F_2$ the decomposition fails: there $A^{\mathsf T}=-A$ means symmetric, so the two subspaces are not complementary.

:::

::: {#fig-direct-sums-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,1.100) rectangle (0.550,1.650);
\node[lab] at (0.275,1.375) {$1$};
\draw[cell frame] (0.550,1.100) rectangle (1.100,1.650);
\node[lab] at (0.825,1.375) {$2$};
\draw[cell frame] (1.100,1.100) rectangle (1.650,1.650);
\node[lab] at (1.375,1.375) {$0$};
\draw[cell frame] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$4$};
\draw[cell frame] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$3$};
\draw[cell frame] (1.100,0.550) rectangle (1.650,1.100);
\node[lab] at (1.375,0.825) {$1$};
\draw[cell frame] (0.000,-0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$2$};
\draw[cell frame] (0.550,-0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$5$};
\draw[cell frame] (1.100,-0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$6$};
\node[lab, note] at (0.825,-0.350) {$A$};
\node[lab] at (1.95,0.825) {$=$};
\draw[hl cell] (2.250,1.100) rectangle (2.800,1.650);
\node[lab] at (2.525,1.375) {$1$};
\draw[cell, fill=primaryLight] (2.800,1.100) rectangle (3.350,1.650);
\node[lab] at (3.075,1.375) {$3$};
\draw[cell, fill=primaryLight] (3.350,1.100) rectangle (3.900,1.650);
\node[lab] at (3.625,1.375) {$1$};
\draw[cell, fill=primaryLight] (2.250,0.550) rectangle (2.800,1.100);
\node[lab] at (2.525,0.825) {$3$};
\draw[hl cell] (2.800,0.550) rectangle (3.350,1.100);
\node[lab] at (3.075,0.825) {$3$};
\draw[cell, fill=primaryLight] (3.350,0.550) rectangle (3.900,1.100);
\node[lab] at (3.625,0.825) {$3$};
\draw[cell, fill=primaryLight] (2.250,-0.000) rectangle (2.800,0.550);
\node[lab] at (2.525,0.275) {$1$};
\draw[cell, fill=primaryLight] (2.800,-0.000) rectangle (3.350,0.550);
\node[lab] at (3.075,0.275) {$3$};
\draw[hl cell] (3.350,-0.000) rectangle (3.900,0.550);
\node[lab] at (3.625,0.275) {$6$};
\node[lab, note] at (3.075,-0.350) {$\frac12(A+A^{\mathsf T})$};
\node[lab] at (4.2,0.825) {$+$};
\draw[cell frame] (4.500,1.100) rectangle (5.050,1.650);
\node[lab] at (4.775,1.375) {$0$};
\draw[hl cell] (5.050,1.100) rectangle (5.600,1.650);
\node[lab] at (5.325,1.375) {$-1$};
\draw[hl cell] (5.600,1.100) rectangle (6.150,1.650);
\node[lab] at (5.875,1.375) {$-1$};
\draw[hl cell] (4.500,0.550) rectangle (5.050,1.100);
\node[lab] at (4.775,0.825) {$1$};
\draw[cell frame] (5.050,0.550) rectangle (5.600,1.100);
\node[lab] at (5.325,0.825) {$0$};
\draw[hl cell] (5.600,0.550) rectangle (6.150,1.100);
\node[lab] at (5.875,0.825) {$-2$};
\draw[hl cell] (4.500,-0.000) rectangle (5.050,0.550);
\node[lab] at (4.775,0.275) {$1$};
\draw[hl cell] (5.050,-0.000) rectangle (5.600,0.550);
\node[lab] at (5.325,0.275) {$2$};
\draw[cell frame] (5.600,-0.000) rectangle (6.150,0.550);
\node[lab] at (5.875,0.275) {$0$};
\node[lab, note] at (5.325,-0.350) {$\frac12(A-A^{\mathsf T})$};
\node[lab, note, anchor=west, align=left] at (6.4,0.825) {symmetric: $6$ free entries\\antisymmetric: $3$ free entries\\$6+3=9=\dim\operatorname{Mat}_3$};
\end{tikzpicture}
\end{center}
```

@exm-direct-sum-matrices for one $3\times3$ matrix over $\mathbb R$. The antisymmetric part has zeros on its diagonal and opposite entries in mirror positions.

:::
