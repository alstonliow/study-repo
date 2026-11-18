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

::: {#def-basis .definition name="Basis"}

A *basis* of a vector space $V$ is a list of vectors that is linearly independent and spans $V$.

:::

::: {#prp-basis-unique-coordinates .proposition name="Coordinates in a basis are unique"}

If $\mathbf{v}_1,\dots,\mathbf{v}_k$ is a basis of $V$, every $\mathbf{v}\in V$ is exactly one combination $c_1\mathbf{v}_1+\dots+c_k\mathbf{v}_k$.

:::

::: {.proof}

1. A combination exists because the basis spans $V$.

2. If two combinations give $\mathbf{v}$, subtracting gives a combination equal to $\mathbf{0}$ with coefficients $c_i-d_i$. By independence all $c_i-d_i=0$.

:::

::: {#thm-dimension-well-defined .theorem name="All bases have the same size"}

If $\mathbf{v}_1,\dots,\mathbf{v}_m$ and $\mathbf{w}_1,\dots,\mathbf{w}_n$ are both bases of $V$, then $m=n$. This common number is the *dimension* $\dim V$.

:::

::: {.proof}

1. Suppose $n>m$. Each $\mathbf{w}_j$ is a combination of the $\mathbf{v}$'s: $\mathbf{w}_j=\sum_ia_{ij}\mathbf{v}_i$. Collect the coefficients in the $m\times n$ matrix $A=[a_{ij}]$.

2. Since $n>m$, there is $\mathbf{c}\ne\mathbf{0}$ with $A\mathbf{c}=\mathbf{0}$ (@cor-more-unknowns-than-equations).

3. Then $\sum_jc_j\mathbf{w}_j=\sum_i\big(\sum_ja_{ij}c_j\big)\mathbf{v}_i=\sum_i(A\mathbf{c})_i\mathbf{v}_i=\mathbf{0}$, a nontrivial combination of the $\mathbf{w}$'s. This contradicts their independence.

4. By symmetry $m>n$ is impossible too, so $m=n$.

:::

::: {#cor-basis-from-independent-set .corollary name="Bases in a space of known dimension"}

In a space of dimension $d$: any $d$ independent vectors form a basis; any $d$ vectors that span form a basis; more than $d$ vectors are dependent; fewer than $d$ cannot span.

:::

::: {.proof}

1. Step 3 of the proof of @thm-dimension-well-defined shows: if $m$ vectors span $V$, then any $n>m$ vectors of $V$ are dependent. With a basis of size $d$ this gives "more than $d$ vectors are dependent".

2. If $d$ independent vectors did not span, adding a vector outside their span would keep them independent (a dependence would have to use the new vector, which would then lie in the span). That gives $d+1$ independent vectors, contradicting step 1.

3. If $k$ vectors span, removing vectors that are combinations of the others keeps the span and ends with an independent spanning list, a basis of size $\le k$. So $k\ge d$, with equality only if nothing was removed.

:::

::: {#exm-basis-of-column-space .example name="Bases of C(A) and N(A)"}

For $A$ in @exm-nullspace-three-by-four, the pivot columns $(1,2,3)$ and $(0,1,1)$ form a basis of $C(A)$, so $\dim C(A)=2=r$. The special solutions $\mathbf{s}_1,\mathbf{s}_2$ form a basis of $N(A)$, so $\dim N(A)=2=n-r$. In general the pivot columns of $A$ (not of $R$) are a basis of $C(A)$: elimination does not change which combinations of columns vanish.

:::
