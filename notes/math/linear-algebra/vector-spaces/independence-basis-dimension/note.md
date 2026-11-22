---
title: "Independence, Basis and Dimension"
sources: [mit1806-9]
requires: [math/linear-algebra/vector-spaces/solving-ax-b]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 9, in our own wording; proofs written out in steps. -->

::: {#def-linear-independence .definition name="Linear independence"}

Vectors $\mathbf{v}_1,\dots,\mathbf{v}_k$ are *linearly independent* if the only combination giving the zero vector is the trivial one:
$$c_1\mathbf{v}_1+\dots+c_k\mathbf{v}_k=\mathbf{0}\ \Longrightarrow\ c_1=\dots=c_k=0.$$
Otherwise they are *dependent*.

:::

::: {#fig-independence-basis-dimension-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[shift={(0,0)}]
\draw[->, muted] (-1.6,0) -- (1.7,0);
\draw[->, muted] (0,-1.6) -- (0,1.7);
\draw[->, emph, primary] (0,0) -- (1,0) node[below, lab] {$\mathbf v_1$};
\draw[->, emph, primary] (0,0) -- (0,1) node[left, lab] {$\mathbf v_2$};
\draw[->, emph, accent] (0,0) -- (1.5,1) node[right, lab] {$\mathbf v_3$};
\draw[faint, dashed] (1,0) -- (1.5,1); \draw[faint, dashed] (0.5,1) -- (1.5,1); \draw[->, primary, faint] (0,0) -- (0.5,0);
\end{scope}
\node[lab, note, anchor=west, align=left] at (2.2,0.3) {$\mathbf v_3=(1.5,1)=1.5\,\mathbf v_1+\mathbf v_2$\\so $1.5\,\mathbf v_1+\mathbf v_2-\mathbf v_3=\mathbf 0$:\\three vectors in $\mathbb R^2$ are dependent};
\end{tikzpicture}
\end{center}
```

A third vector in the plane is always a combination of two independent ones, so a nontrivial combination of the three gives $\mathbf 0$. In matrix terms: a $2\times3$ matrix has a free column, hence a nonzero nullspace vector.

:::

::: {#fig-independence-basis-dimension-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.1]
\fill[tintA] (0,0) -- (1.6,0.4) -- (2.0,1.8) -- (0.4,1.4) -- cycle;
\draw[->, emph, primary] (0,0) -- (1.6,0.4) node[lab, below right] {$\mathbf v_1$};
\draw[->, emph, accent] (0,0) -- (0.4,1.4) node[lab, left] {$\mathbf v_2$};
\node[lab] at (1,-0.7) {independent};
\begin{scope}[xshift=4cm]
\draw[faint, dashed] (-0.6,-0.3) -- (2.6,1.3);
\draw[->, hl] (0,0) -- (1.6,0.8) node[lab, above left] {$\mathbf v_2=2\mathbf v_1$};
\draw[->, emph, primary] (0,0) -- (0.8,0.4) node[lab, below right] {$\mathbf v_1$};
\node[lab] at (1,-0.7) {dependent: $2\mathbf v_1-\mathbf v_2=\mathbf 0$};
\end{scope}
\end{tikzpicture}
\end{center}
```

Two vectors in the plane. Independent vectors (left) span a parallelogram and all of $\mathbb R^2$; dependent vectors (right) lie on one line, and a nontrivial combination gives $\mathbf 0$.

:::

::: {#prp-independence-and-nullspace .proposition name="Independence of columns"}

The columns of $A$ are independent if and only if $N(A)=\{\mathbf{0}\}$, if and only if $\operatorname{rank}A=n$ (no free variables).

:::

::: {.proof}

1. A combination of the columns with coefficients $\mathbf{c}$ is $A\mathbf{c}$ (@def-matrix-times-vector). So a nontrivial combination giving $\mathbf{0}$ is a nonzero vector of $N(A)$.

2. By @thm-special-solutions, $N(A)\ne\{\mathbf{0}\}$ exactly when there is a free variable, i.e. $r<n$.

:::

By @cor-more-unknowns-than-equations, any $n>m$ vectors in $\mathbb{R}^m$ are dependent.

::: {#def-span .definition name="Span"}

The *span* of $\mathbf{v}_1,\dots,\mathbf{v}_k$ is the set of all their linear combinations, the smallest subspace containing them. The vectors *span* a space $V$ if their span is $V$. The column space $C(A)$ is the span of the columns (@def-column-space).

:::

::: {#fig-independence-basis-dimension-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[shift={(0,0)}]
\draw[->, muted] (-1.40,0) -- (1.5,0);
\draw[->, muted] (0,-1.40) -- (0,1.5);
\draw[emph, primary, faint] (-1.2,-0.6) -- (1.3,0.65);
\draw[->, emph, primary] (0,0) -- (0.8,0.4) node[above, lab] {$\mathbf v$};
\node[lab, note] at (0,-1.7) {span of $\mathbf v$: a line};
\end{scope}
\begin{scope}[shift={(3.5,0)}]
\draw[->, muted] (-1.40,0) -- (1.5,0);
\draw[->, muted] (0,-1.40) -- (0,1.5);
\draw[emph, primary, faint] (-1.2,-0.6) -- (1.3,0.65);
\draw[->, emph, primary] (0,0) -- (0.8,0.4) node[above, lab] {$\mathbf v$};
\draw[->, emph, accent] (0,0) -- (-1.2,-0.6) node[below, lab] {$-1.5\mathbf v$};
\node[lab, note] at (0,-1.7) {adding $-1.5\mathbf v$: same line};
\end{scope}
\begin{scope}[shift={(7,0)}]
\draw[->, muted] (-1.40,0) -- (1.5,0);
\draw[->, muted] (0,-1.40) -- (0,1.5);
\fill[tintA] (-1.3,-1.3) rectangle (1.3,1.3);
\draw[->, emph, primary] (0,0) -- (0.8,0.4) node[right, lab] {$\mathbf v$};
\draw[->, emph, secondary] (0,0) -- (-0.3,0.9) node[above, lab] {$\mathbf w$};
\node[lab, note] at (0,-1.7) {span of $\mathbf v,\mathbf w$: the plane};
\end{scope}
\end{tikzpicture}
\end{center}
```

Spans in $\mathbb R^2$. A dependent vector adds nothing to a span; an independent one raises its dimension. A basis is a spanning set with no redundant vector.

:::

::: {#def-basis .definition name="Basis"}

A *basis* of a vector space $V$ is a list of vectors that is linearly independent and spans $V$.

:::

<!-- Merged 2026-11-20 (owner): the block prp-basis-unique-coordinates was removed in favour of prp-basis-iff-unique-expression (Cambridge IB Linear Algebra), which states it for any field or inner product space with a full proof. -->

**Coordinates are unique.** If $\mathbf{v}_1,\dots,\mathbf{v}_k$ is a basis of $V$, every $\mathbf{v}\in V$ is exactly one combination $c_1\mathbf{v}_1+\dots+c_k\mathbf{v}_k$: a combination exists because the basis spans, and two different ones would subtract to a non-trivial combination equal to $\mathbf{0}$. This is @prp-basis-iff-unique-expression, which also proves the converse.

<!-- Merged 2026-11-20 (owner): the block thm-dimension-well-defined was removed in favour of thm-dimension-invariant (Cambridge IB Linear Algebra), which states it for any field or inner product space with a full proof. -->

**All bases have the same size.** If $\mathbf{v}_1,\dots,\mathbf{v}_m$ and $\mathbf{w}_1,\dots,\mathbf{w}_n$ are both bases of $V$, then $m=n$, and this number is the *dimension* $\dim V$. For subspaces of $\mathbb R^m$ one can see it by elimination: if $n>m$, the $m\times n$ matrix of coefficients of the $\mathbf w$'s in terms of the $\mathbf v$'s has a non-zero null vector (@cor-more-unknowns-than-equations), which gives a dependence among the $\mathbf w$'s. The proof over any field, by the Steinitz exchange lemma, is @thm-dimension-invariant.

::: {#cor-basis-from-independent-set .corollary name="Bases in a space of known dimension"}

In a space of dimension $d$: any $d$ independent vectors form a basis; any $d$ vectors that span form a basis; more than $d$ vectors are dependent; fewer than $d$ cannot span.

:::

::: {.proof}

1. By @thm-steinitz-exchange, if $m$ vectors span $V$, then any $n>m$ vectors of $V$ are dependent. With a basis of size $d$ this gives "more than $d$ vectors are dependent".

2. If $d$ independent vectors did not span, adding a vector outside their span would keep them independent (a dependence would have to use the new vector, which would then lie in the span). That gives $d+1$ independent vectors, contradicting step 1.

3. If $k$ vectors span, removing vectors that are combinations of the others keeps the span and ends with an independent spanning list, a basis of size $\le k$. So $k\ge d$, with equality only if nothing was removed.

:::

::: {#exm-basis-of-column-space .example name="Bases of C(A) and N(A)"}

For $A$ in @exm-nullspace-three-by-four, the pivot columns $(1,2,3)$ and $(0,1,1)$ form a basis of $C(A)$, so $\dim C(A)=2=r$. The special solutions $\mathbf{s}_1,\mathbf{s}_2$ form a basis of $N(A)$, so $\dim N(A)=2=n-r$. In general the pivot columns of $A$ (not of $R$) are a basis of $C(A)$: elimination does not change which combinations of columns vanish.

:::

::: {#fig-independence-basis-dimension-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell, fill=primaryLight] (0.000,1.100) rectangle (0.550,1.650);
\node[lab] at (0.275,1.375) {$1$};
\draw[cell frame] (0.550,1.100) rectangle (1.100,1.650);
\node[lab] at (0.825,1.375) {$2$};
\draw[cell, fill=primaryLight] (1.100,1.100) rectangle (1.650,1.650);
\node[lab] at (1.375,1.375) {$0$};
\draw[cell frame] (1.650,1.100) rectangle (2.200,1.650);
\node[lab] at (1.925,1.375) {$1$};
\draw[cell, fill=primaryLight] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$2$};
\draw[cell frame] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$4$};
\draw[cell, fill=primaryLight] (1.100,0.550) rectangle (1.650,1.100);
\node[lab] at (1.375,0.825) {$1$};
\draw[cell frame] (1.650,0.550) rectangle (2.200,1.100);
\node[lab] at (1.925,0.825) {$4$};
\draw[cell, fill=primaryLight] (0.000,-0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$3$};
\draw[cell frame] (0.550,-0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$6$};
\draw[cell, fill=primaryLight] (1.100,-0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$1$};
\draw[cell frame] (1.650,-0.000) rectangle (2.200,0.550);
\node[lab] at (1.925,0.275) {$5$};
\node[lab, note] at (1.100,-0.350) {$A$: columns $1,3$ are a basis of $C(A)$};
\draw[->] (2.6,0.825) -- (3.6,0.825) node[midway, above, lab, note] {rref};
\draw[hl cell] (4.600,1.100) rectangle (5.150,1.650);
\node[lab] at (4.875,1.375) {$1$};
\draw[cell frame] (5.150,1.100) rectangle (5.700,1.650);
\node[lab] at (5.425,1.375) {$2$};
\draw[cell frame] (5.700,1.100) rectangle (6.250,1.650);
\node[lab] at (5.975,1.375) {$0$};
\draw[cell frame] (6.250,1.100) rectangle (6.800,1.650);
\node[lab] at (6.525,1.375) {$1$};
\draw[cell frame] (4.600,0.550) rectangle (5.150,1.100);
\node[lab] at (4.875,0.825) {$0$};
\draw[cell frame] (5.150,0.550) rectangle (5.700,1.100);
\node[lab] at (5.425,0.825) {$0$};
\draw[hl cell] (5.700,0.550) rectangle (6.250,1.100);
\node[lab] at (5.975,0.825) {$1$};
\draw[cell frame] (6.250,0.550) rectangle (6.800,1.100);
\node[lab] at (6.525,0.825) {$2$};
\draw[cell frame] (4.600,-0.000) rectangle (5.150,0.550);
\node[lab] at (4.875,0.275) {$0$};
\draw[cell frame] (5.150,-0.000) rectangle (5.700,0.550);
\node[lab] at (5.425,0.275) {$0$};
\draw[cell frame] (5.700,-0.000) rectangle (6.250,0.550);
\node[lab] at (5.975,0.275) {$0$};
\draw[cell frame] (6.250,-0.000) rectangle (6.800,0.550);
\node[lab] at (6.525,0.275) {$0$};
\node[lab, note] at (5.700,-0.350) {$R$: pivots in columns $1,3$};
\node[lab, note, align=center] at (3.1,-1.1) {same relations in $A$ and $R$:\quad col$_2=2\,$col$_1$,\quad col$_4=$col$_1+2\,$col$_3$};
\end{tikzpicture}
\end{center}
```

@exm-basis-of-column-space. Row operations keep every relation among the columns, so the columns of $A$ in the pivot positions of $R$ are independent and span $C(A)$. The columns of $R$ themselves are not a basis of $C(A)$: their third entries are all zero.

:::
