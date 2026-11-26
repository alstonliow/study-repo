---
title: "Total Unimodularity"
sources: [mit18433-3]
requires: [math/combinatorial-optimization/polyhedra/vertices-of-polyhedra, math/discrete/graph/bipartite-graphs]
status: draft
---

<!-- Added 2026-11-26 from MIT 18.433 (Spring 2015), lecture notes on polyhedral theory and linear programming (Section 3.5), in our own wording; example our own (checked by computation); proofs written out in steps. Only the "if" direction of the Ghouila-Houri criterion is proved, as in the course. -->

A polyhedron is *integral* if all its vertices are integer vectors. Integer programming is hard in general, but if the constraint matrix has the following property, the linear relaxation of an integer program already has integral optimal vertices.

::: {#def-totally-unimodular .definition name="Totally unimodular matrix"}

A matrix $A$ is *totally unimodular* (TU) if every square submatrix of $A$ has determinant $-1$, $0$ or $+1$. In particular every entry of $A$ is in $\{-1,0,1\}$.

:::

Deleting rows or columns, transposing, multiplying a row by $-1$ and appending a unit row or column $\pm e_i$ all preserve total unimodularity (the last by expanding a determinant along the new row or column).

::: {#thm-tu-integral-polyhedron .theorem name="TU matrices give integral polyhedra"}

If $A$ is totally unimodular and $b$ is integral, then $P=\{x:Ax\le b,\ x\ge0\}$ is integral. The same holds for $\{x:Ax\ge b,\ x\ge0\}$ and $\{x:Ax=b,\ x\ge0\}$.

:::

::: {.proof}

1. Add slack variables: $Q=\{(x,s):Ax+Is=b,\ x\ge0,\ s\ge0\}$. A point $x$ is a vertex of $P$ exactly when $(x,b-Ax)$ is a vertex of $Q$ (exercise), so it suffices to show that the vertices of $Q$ are integral. The matrix $[A\ I]$ has full row rank, so the vertices of $Q$ are its basic feasible solutions (@prp-vertices-are-bfs).

2. Let $B$ be a basis of $[A\ I]$, so the basis matrix $M$ (columns of $A$ and of $I$) is invertible. Expanding $\det M$ along the identity columns, each of which has a single entry $1$, leaves $\pm$ the determinant of a square submatrix of $A$. So $\det M\in\{-1,0,1\}$, and $\det M\ne0$ as $M$ is invertible; hence $\det M=\pm1$.

3. By Cramer's rule $M^{-1}=\frac1{\det M}\operatorname{adj}M$, where the adjugate consists of subdeterminants of $M$, which are integers. So $M^{-1}$ is integral, and the basic variables $M^{-1}b$ are integral; the non-basic ones are $0$.

4. For $Ax\ge b$ replace $A,b$ by $-A,-b$. For $Ax=b$, $x\ge0$ apply the bfs argument directly to $A$ (after deleting dependent rows, which keeps $A$ TU).

:::

The converse holds for the first form: if $\{x:Ax\le b,\ x\ge0\}$ is integral for every integral $b$, then $A$ is TU.

::: {#thm-bipartite-incidence-tu .theorem name="Incidence matrices of bipartite graphs are TU"}

Let $G=(V,E)$ be bipartite, and let $A$ be its vertex–edge incidence matrix ($a_{ve}=1$ if $v$ is an end of $e$, else $0$). Then $A$ is totally unimodular.

:::

::: {.proof}

1. Induct on the size $k$ of a square submatrix $T$; the case $k=1$ is clear since entries are $0$ or $1$.

2. If some column of $T$ is zero, $\det T=0$. If some column of $T$ has exactly one $1$, expand along it: $\det T=\pm\det T'$ for a $(k-1)\times(k-1)$ submatrix $T'$, which is $0$ or $\pm1$ by induction.

3. Otherwise every column of $T$ has exactly two $1$s (an edge has two ends), one in a row of each side $L$ and $R$ of the bipartition. Then the sum of the rows of $T$ indexed by $L$ equals the sum of the rows indexed by $R$ (both are the all-ones vector), so the rows are linearly dependent and $\det T=0$.

:::

So the polytope $\{x\ge0:\sum_{e\ni v}x_e=1\ \text{for all } v\}$ of a bipartite graph has only $0$–$1$ vertices, the incidence vectors of perfect matchings (@thm-bipartite-perfect-matching-polytope). For non-bipartite graphs this fails: on a triangle, $x=(\frac12,\frac12,\frac12)$ is a vertex of $\{x\ge0:x(\delta(v))\le1\}$.

::: {#thm-ghouila-houri .theorem name="Ghouila-Houri's criterion"}

A matrix $A$ with entries in $\{-1,0,1\}$ is totally unimodular if and only if every set $R$ of rows can be split as $R=R_1\cup R_2$ (disjointly) so that for every column $j$
$$\sum_{i\in R_1}a_{ij}-\sum_{i\in R_2}a_{ij}\in\{-1,0,1\}.$$

:::

::: {.proof}

We prove "if", by induction on the size $k$ of a square submatrix $B$; for $k=1$ the entries are in $\{-1,0,1\}$.

1. Let $B$ be $k\times k$ and invertible (otherwise $\det B=0$). Write $B^{-1}=\frac1{\det B}B^*$ with $B^*$ the adjugate. Its entries are $\pm$ determinants of $(k-1)\times(k-1)$ submatrices, so they lie in $\{-1,0,1\}$ by induction.

2. Let $b^*$ be the first row of $B^*$. From $B^*B=(\det B)I$ we get $b^*B=(\det B)e_1^{\mathsf T}$, that is,
$$\sum_ib^*_ib_{ij}=\begin{cases}\det B,&j=1,\\0,&j\ne1.\end{cases}$$

3. Let $R=\{i:b^*_i\ne0\}$, so $b^*_i=\pm1$ on $R$, and split $R=R_1\cup R_2$ as the hypothesis allows (rows of $B$ are rows of $A$ restricted to some columns, so the property holds for $B$). Put $y_i=1$ on $R_1$, $-1$ on $R_2$, $0$ elsewhere. Then $(yB)_j\in\{-1,0,1\}$ for every $j$.

4. For each $j$, $(yB)_j$ and $(b^*B)_j$ are both sums over $R$ of $\pm b_{ij}$ with the same terms up to sign, so they differ by an even number. For $j\ne1$, $(b^*B)_j=0$, hence $(yB)_j$ is even and in $\{-1,0,1\}$, so it is $0$.

5. $(yB)_1\ne0$, since $y\ne0$ (as $b^*\ne0$) and $B$ is invertible. So $yB=\pm e_1^{\mathsf T}$, and $y=\pm e_1^{\mathsf T}B^{-1}=\pm\frac1{\det B}b^*$.

6. Both $y$ and $b^*$ have entries in $\{-1,0,1\}$ and the same non-zero pattern, so $|\det B|=1$.

:::

::: {#exm-interval-matrix-tu .example name="Interval matrices"}

A $0$–$1$ matrix in which the $1$s of every column are consecutive (an *interval matrix*) is TU: given a set of rows, list them from top to bottom and put them alternately into $R_1$ and $R_2$. In every column the chosen rows containing a $1$ form a consecutive run in this list, whose signs alternate $+,-,+,\dots$, so the column sum is $0$ or $1$. For example,
$$\begin{pmatrix}1&0&1\\1&1&0\\0&1&0\end{pmatrix}$$
is an interval matrix, and indeed its determinant is $1$.

:::

::: {#fig-total-unimodularity-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$1$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$0$};
\draw[hl cell] (1.100,0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$1$};
\node[lab, anchor=east] at (-0.100,0.275) {$R_1$};
\draw[hl cell] (0.000,-0.550) rectangle (0.550,0.000);
\node[lab] at (0.275,-0.275) {$1$};
\draw[hl cell] (0.550,-0.550) rectangle (1.100,0.000);
\node[lab] at (0.825,-0.275) {$1$};
\draw[cell frame] (1.100,-0.550) rectangle (1.650,0.000);
\node[lab] at (1.375,-0.275) {$0$};
\node[lab, anchor=east] at (-0.100,-0.275) {$R_2$};
\draw[cell frame] (0.000,-1.100) rectangle (0.550,-0.550);
\node[lab] at (0.275,-0.825) {$0$};
\draw[hl cell] (0.550,-1.100) rectangle (1.100,-0.550);
\node[lab] at (0.825,-0.825) {$1$};
\draw[cell frame] (1.100,-1.100) rectangle (1.650,-0.550);
\node[lab] at (1.375,-0.825) {$0$};
\node[lab, anchor=east] at (-0.100,-0.825) {$R_1$};
\node[lab] at (0.83,-1.45) {sums $R_1-R_2$: $0,\ 0,\ 1$};
\end{tikzpicture}
\end{center}
```

Ghouila-Houri for the interval matrix of the example: rows taken alternately into $R_1$ and $R_2$ give column sums $1-1=0$, $-1+1=0$ and $1$, all in $\{-1,0,1\}$, because the $1$s of each column (highlighted) are consecutive.

:::
