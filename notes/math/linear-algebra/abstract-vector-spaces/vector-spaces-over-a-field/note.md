---
title: "Vector Spaces over a Field"
sources: [camib-la-1]
requires: [math/linear-algebra/vector-spaces/vector-spaces-and-subspaces, math/discrete/relations/equivalence-relations]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 1.1, in our own wording; examples ours; proofs written out in steps. The real vector space of MIT 18.06 is the case F = R of def-vector-space-over-field. -->

The vector spaces of @sec-math-linear-algebra-vector-spaces-vector-spaces-and-subspaces have real scalars. Nothing in the axioms needs more than the arithmetic of a field, so from here on scalars come from an arbitrary field $F$ (@def-field): $\mathbb R$, $\mathbb C$, $\mathbb Q$ or a finite field $\mathbb F_p$. Vectors are written in plain letters $u,v,w$, since they need not be columns of numbers.

::: {#def-vector-space-over-field .definition name="Vector space over a field" generalizes="def-vector-space"}

Let $F$ be a field. An *$F$-vector space* is a set $V$ with an addition $V\times V\to V$ and a scalar multiplication $F\times V\to V$, $(\lambda,v)\mapsto\lambda v$, such that $(V,+)$ is an abelian group (associative, commutative, with a zero $0$ and inverses $-v$) and for all $\lambda,\mu\in F$ and $u,v\in V$:
$$\lambda(\mu v)=(\lambda\mu)v,\qquad \lambda(u+v)=\lambda u+\lambda v,\qquad (\lambda+\mu)v=\lambda v+\mu v,\qquad 1v=v.$$

:::

::: {#prp-vector-space-zero-rules .proposition name="Zero and negatives"}

In every $F$-vector space, $0v=0$, $\lambda0=0$ and $(-1)v=-v$ for all $v\in V$, $\lambda\in F$.

:::

::: {.proof}

1. $0v=(0+0)v=0v+0v$; adding $-(0v)$ to both sides gives $0v=0$.

2. $\lambda0=\lambda(0+0)=\lambda0+\lambda0$, so $\lambda0=0$ in the same way.

3. $v+(-1)v=(1+(-1))v=0v=0$, so $(-1)v$ is the additive inverse of $v$.

:::

::: {#exm-vector-spaces-over-fields .example name="Vector spaces over various fields"}

1. $F^n$, columns of $n$ elements of $F$, with entrywise operations. For $F=\mathbb F_2$ this is the space of bit strings of length $n$ under XOR.
2. For any set $X$, the functions $X\to F$ form a vector space $F^X$ under pointwise operations. With $X=\{1,\dots,n\}$ this is $F^n$; with $X=\mathbb N$ it is the space of sequences.
3. The polynomials $F[t]$ with coefficients in $F$, and the matrices $\operatorname{Mat}_{m,n}(F)$.
4. $\mathbb C$ is a $\mathbb C$-vector space and also an $\mathbb R$-vector space; $\mathbb R$ is a $\mathbb Q$-vector space. The field of scalars is part of the structure.

:::

::: {#def-subspace-over-field .definition name="Subspace, sum of subspaces" generalizes="def-subspace"}

A subset $U$ of an $F$-vector space $V$ is a *subspace*, written $U\le V$, if $0\in U$ and $\lambda u+\mu w\in U$ for all $u,w\in U$ and $\lambda,\mu\in F$. For subspaces $U,W\le V$ the *sum* is
$$U+W=\{u+w:u\in U,\ w\in W\}.$$

:::

::: {#prp-sum-and-intersection-subspaces .proposition name="Sums and intersections are subspaces" generalizes="prp-intersection-of-subspaces"}

If $U,W\le V$, then $U\cap W$ and $U+W$ are subspaces of $V$. $U+W$ is the smallest subspace containing $U\cup W$.

:::

::: {.proof}

1. $0=0+0$ lies in $U+W$ and in $U\cap W$.

2. If $u_1+w_1,\,u_2+w_2\in U+W$, then $\lambda(u_1+w_1)+\mu(u_2+w_2)=(\lambda u_1+\mu u_2)+(\lambda w_1+\mu w_2)\in U+W$.

3. If $v_1,v_2\in U\cap W$, then $\lambda v_1+\mu v_2$ lies in $U$ and in $W$.

4. Every subspace containing $U$ and $W$ contains all sums $u+w$, so it contains $U+W$; and $U+W$ contains $U$ (take $w=0$) and $W$.

:::

The union of two subspaces is usually not a subspace: in $\mathbb R^2$ the two axes are subspaces, but $(1,0)+(0,1)$ lies on neither.

::: {#def-quotient-space .definition name="Quotient space"}

Let $U\le V$. The *coset* of $v\in V$ is $v+U=\{v+u:u\in U\}$. The *quotient space* $V/U$ is the set of cosets, with
$$(v+U)+(w+U)=(v+w)+U,\qquad \lambda(v+U)=\lambda v+U.$$

:::

::: {#prp-quotient-space-well-defined .proposition name="The quotient is a vector space"}

The operations on $V/U$ are well defined, and make $V/U$ an $F$-vector space with zero $0+U=U$. Moreover $v+U=w+U$ if and only if $v-w\in U$.

:::

::: {.proof}

1. The relation $v\sim w\iff v-w\in U$ is an equivalence relation (@def-equivalence-relation): $v-v=0\in U$; $w-v=-(v-w)\in U$; and $(v-w)+(w-x)=v-x$. Its classes are the cosets, so $v+U=w+U$ exactly when $v-w\in U$.

2. If $v+U=v'+U$ and $w+U=w'+U$, then $(v+w)-(v'+w')=(v-v')+(w-w')\in U$ and $\lambda v-\lambda v'=\lambda(v-v')\in U$. So sums and multiples do not depend on the representatives.

3. Each axiom of @def-vector-space-over-field for $V/U$ follows from the same axiom in $V$ applied to representatives.

:::

::: {#exm-quotient-space .example name="A plane modulo a line"}

Let $V=\mathbb R^2$ and $U$ the line $y=0$. Then $(a,b)+U=(a',b')+U$ exactly when $b=b'$: the cosets are the horizontal lines, and $(a,b)+U\mapsto b$ identifies $V/U$ with $\mathbb R$. In general, $V/U$ forgets the directions in $U$.

:::

::: {#fig-vector-spaces-over-a-field-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-2.4,0) -- (2.6,0) node[lab, anchor=west] {$x$};
\draw[->] (0,-1.4) -- (0,2.5) node[lab, anchor=south] {$y$};
\draw[faint, primary] (-2.3,-0.80) -- (2.3,-0.80);
\draw[faint, primary] (-2.3,0.80) -- (2.3,0.80);
\draw[faint, primary] (-2.3,1.60) -- (2.3,1.60);
\draw[emph, primary] (-2.3,0) -- (2.3,0) node[lab, anchor=north east] {$U=0+U$};
\draw[emph, accent] (-2.3,0.8) -- (2.3,0.8) node[lab, anchor=west] {$(a,1)+U$};
\node[dot] at (-1.2,0.8) {}; \node[lab, anchor=south] at (-1.2,0.85) {$(-\tfrac32,1)$};
\node[dot] at (0.8,0.8) {}; \node[lab, anchor=south] at (0.8,0.85) {$(1,1)$};
\node[lab, anchor=east] at (-2.35,1.6) {$b=2$};
\node[lab, anchor=east] at (-2.35,-0.8) {$b=-1$};
\end{tikzpicture}
\end{center}
```

The quotient of the plane by the line $U$ ($y=0$): each coset is a horizontal line, and two points give the same coset when they differ by a vector of $U$. Cosets are added and scaled like their heights $b$, so $V/U\cong\mathbb R$.

:::
