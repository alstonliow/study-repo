---
title: "Sparse Direct Solvers"
sources: [mit18335-24]
requires: [math/numerical/direct-solvers/cholesky-factorization, math/discrete/graph/basic-definitions]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lecture 24 (sparse-direct solvers; slides on sparse matrix algorithms), in our own wording; proofs written out in steps. -->

A matrix is *sparse* when it has so many zeros that it pays to exploit them: store only the nonzeros and skip operations on zeros. Elimination, however, creates new nonzeros. How many depends entirely on the order of the unknowns, and choosing a good order is a graph problem.

::: {#def-sparse-storage .definition name="Sparse storage"}

A sparse $m\times m$ matrix with $\operatorname{nnz}$ nonzeros is stored in *compressed sparse column* (CSC) form: an array of the nonzero values listed column by column, an array of their row indices, and an array of $m+1$ pointers to where each column starts, about $2\operatorname{nnz}+m$ numbers in all. A matrix–vector product then costs $O(\operatorname{nnz})$ flops instead of $O(m^2)$.

:::

::: {#def-fill-in .definition name="Fill-in and the graph of a matrix"}

The *graph* $G(A)$ of a symmetric $m\times m$ matrix has vertices $1,\dots,m$ and an edge $\{i,j\}$ whenever $a_{ij}\ne0$, $i\ne j$. *Fill-in* consists of the positions where the Cholesky factor $R$ (or $L$, $U$) is nonzero but $A$ is zero.

:::

::: {#prp-elimination-graph .proposition name="Elimination as a graph operation"}

Eliminating unknown $k$ in symmetric Gaussian elimination (ignoring accidental cancellation) corresponds to deleting vertex $k$ from the graph and joining all its remaining neighbours pairwise. The fill-in created at that step is the set of new edges.

:::

::: {.proof}

1. Step $k$ replaces the trailing block by $S=K-\mathbf{w}\mathbf{w}^{\mathsf H}/a_{kk}$ (as in @thm-cholesky-existence), where $\mathbf{w}$ is the part of column $k$ below the diagonal.

2. $(\mathbf{w}\mathbf{w}^{\mathsf H})_{ij}\ne0$ exactly when $w_i\ne0$ and $w_j\ne0$, i.e. when $i$ and $j$ are both neighbours of $k$.

3. So $s_{ij}$ can be nonzero where $k_{ij}=0$ precisely for pairs of neighbours of $k$ that were not already adjacent; these become edges of the graph of $S$, while vertex $k$ leaves it.

:::

::: {#exm-arrowhead-ordering .example name="The arrowhead matrix"}

Let $A$ be symmetric positive definite with nonzeros only on the diagonal, in the first row and in the first column. Its graph is a star with centre $1$. Eliminating vertex $1$ first joins all other vertices pairwise: the trailing block becomes completely full, and $R$ has $m(m+1)/2$ nonzeros. Ordering the centre *last* (reversing the order of the unknowns) eliminates leaves of the star, which have one neighbour each and create no fill: $R$ has only $2m-1$ nonzeros, and the factorization costs $O(m)$ instead of $O(m^3)$.

:::

::: {#fig-sparse-direct-solvers-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-0.04,0.05) -- (-0.10,0.05) -- (-0.10,-2.09) -- (-0.04,-2.09);
\draw[faint] (2.08,0.05) -- (2.14,0.05) -- (2.14,-2.09) -- (2.08,-2.09);
\node[tick] at (0.17,-0.17) {$\times$};
\node[tick] at (0.51,-0.17) {$\times$};
\node[tick] at (0.85,-0.17) {$\times$};
\node[tick] at (1.19,-0.17) {$\times$};
\node[tick] at (1.53,-0.17) {$\times$};
\node[tick] at (1.87,-0.17) {$\times$};
\node[tick] at (0.17,-0.51) {$\times$};
\node[tick] at (0.51,-0.51) {$\times$};
\node[tick] at (0.17,-0.85) {$\times$};
\node[tick] at (0.85,-0.85) {$\times$};
\node[tick] at (0.17,-1.19) {$\times$};
\node[tick] at (1.19,-1.19) {$\times$};
\node[tick] at (0.17,-1.53) {$\times$};
\node[tick] at (1.53,-1.53) {$\times$};
\node[tick] at (0.17,-1.87) {$\times$};
\node[tick] at (1.87,-1.87) {$\times$};
\node[note] at (1.02,-2.39) {$A$, hub first};
\draw[map] (2.19,-1.02) -- (2.64,-1.02);
\draw[faint] (2.75,0.05) -- (2.69,0.05) -- (2.69,-2.09) -- (2.75,-2.09);
\draw[faint] (4.87,0.05) -- (4.93,0.05) -- (4.93,-2.09) -- (4.87,-2.09);
\node[tick] at (2.96,-0.17) {$\times$};
\node[tick] at (3.30,-0.17) {$\times$};
\node[tick] at (3.64,-0.17) {$\times$};
\node[tick] at (3.98,-0.17) {$\times$};
\node[tick] at (4.32,-0.17) {$\times$};
\node[tick] at (4.66,-0.17) {$\times$};
\node[tick] at (3.30,-0.51) {$\times$};
\fill[accentLight] (3.49,-0.66) rectangle (3.79,-0.36);
\node[tick] at (3.64,-0.51) {$\bullet$};
\fill[accentLight] (3.83,-0.66) rectangle (4.13,-0.36);
\node[tick] at (3.98,-0.51) {$\bullet$};
\fill[accentLight] (4.17,-0.66) rectangle (4.47,-0.36);
\node[tick] at (4.32,-0.51) {$\bullet$};
\fill[accentLight] (4.51,-0.66) rectangle (4.81,-0.36);
\node[tick] at (4.66,-0.51) {$\bullet$};
\node[tick] at (3.64,-0.85) {$\times$};
\fill[accentLight] (3.83,-1.00) rectangle (4.13,-0.70);
\node[tick] at (3.98,-0.85) {$\bullet$};
\fill[accentLight] (4.17,-1.00) rectangle (4.47,-0.70);
\node[tick] at (4.32,-0.85) {$\bullet$};
\fill[accentLight] (4.51,-1.00) rectangle (4.81,-0.70);
\node[tick] at (4.66,-0.85) {$\bullet$};
\node[tick] at (3.98,-1.19) {$\times$};
\fill[accentLight] (4.17,-1.34) rectangle (4.47,-1.04);
\node[tick] at (4.32,-1.19) {$\bullet$};
\fill[accentLight] (4.51,-1.34) rectangle (4.81,-1.04);
\node[tick] at (4.66,-1.19) {$\bullet$};
\node[tick] at (4.32,-1.53) {$\times$};
\fill[accentLight] (4.51,-1.68) rectangle (4.81,-1.38);
\node[tick] at (4.66,-1.53) {$\bullet$};
\node[tick] at (4.66,-1.87) {$\times$};
\node[note] at (3.81,-2.39) {$R$};
\end{tikzpicture}

\vspace{4pt}

\begin{tikzpicture}
\draw[faint] (-0.04,0.05) -- (-0.10,0.05) -- (-0.10,-2.09) -- (-0.04,-2.09);
\draw[faint] (2.08,0.05) -- (2.14,0.05) -- (2.14,-2.09) -- (2.08,-2.09);
\node[tick] at (0.17,-0.17) {$\times$};
\node[tick] at (1.87,-0.17) {$\times$};
\node[tick] at (0.51,-0.51) {$\times$};
\node[tick] at (1.87,-0.51) {$\times$};
\node[tick] at (0.85,-0.85) {$\times$};
\node[tick] at (1.87,-0.85) {$\times$};
\node[tick] at (1.19,-1.19) {$\times$};
\node[tick] at (1.87,-1.19) {$\times$};
\node[tick] at (1.53,-1.53) {$\times$};
\node[tick] at (1.87,-1.53) {$\times$};
\node[tick] at (0.17,-1.87) {$\times$};
\node[tick] at (0.51,-1.87) {$\times$};
\node[tick] at (0.85,-1.87) {$\times$};
\node[tick] at (1.19,-1.87) {$\times$};
\node[tick] at (1.53,-1.87) {$\times$};
\node[tick] at (1.87,-1.87) {$\times$};
\node[note] at (1.02,-2.39) {$A$, hub last};
\draw[map] (2.19,-1.02) -- (2.64,-1.02);
\draw[faint] (2.75,0.05) -- (2.69,0.05) -- (2.69,-2.09) -- (2.75,-2.09);
\draw[faint] (4.87,0.05) -- (4.93,0.05) -- (4.93,-2.09) -- (4.87,-2.09);
\node[tick] at (2.96,-0.17) {$\times$};
\node[tick] at (4.66,-0.17) {$\times$};
\node[tick] at (3.30,-0.51) {$\times$};
\node[tick] at (4.66,-0.51) {$\times$};
\node[tick] at (3.64,-0.85) {$\times$};
\node[tick] at (4.66,-0.85) {$\times$};
\node[tick] at (3.98,-1.19) {$\times$};
\node[tick] at (4.66,-1.19) {$\times$};
\node[tick] at (4.32,-1.53) {$\times$};
\node[tick] at (4.66,-1.53) {$\times$};
\node[tick] at (4.66,-1.87) {$\times$};
\node[note] at (3.81,-2.39) {$R$};
\end{tikzpicture}
\end{center}
```

The arrowhead matrix of @exm-arrowhead-ordering with its hub first (top) fills in completely ($\bullet$ = fill); ordered with the hub last (bottom), its Cholesky factor has no fill at all.

:::

::: {#fig-sparse-direct-solvers-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.9]
\begin{scope}
\node[small vertex, fill=accentLight, draw=accent] (c) at (0,0) {$1$};
\foreach \i/\a in {2/90,3/18,4/-54,5/-126,6/162} {\node[small vertex] (v\i) at (\a:1.3) {$\i$}; \draw (c) -- (v\i);}
\node[note] at (0,-1.9) {star graph};
\end{scope}
\draw[map] (1.9,0) -- (3.1,0) node[midway, note, above] {eliminate $1$};
\begin{scope}[xshift=5cm]
\foreach \i/\a in {2/90,3/18,4/-54,5/-126,6/162} {\node[small vertex] (w\i) at (\a:1.3) {$\i$};}
\foreach \i/\j in {2/3,2/4,2/5,2/6,3/4,3/5,3/6,4/5,4/6,5/6} {\draw[hl] (w\i) -- (w\j);}
\node[note] at (0,-1.9) {complete graph: full fill};
\end{scope}
\end{tikzpicture}
\end{center}
```

Graph view of @prp-elimination-graph: eliminating the centre of a star joins its five neighbours pairwise; the ten new edges are the fill-in of the trailing block.

:::

::: {#rmk-sparse-direct-solvers-1 .remark name="Ordering heuristics"}

Finding the ordering with the least fill is NP-hard, so solvers use heuristics. *Minimum degree* eliminates next a vertex of smallest current degree (each step creates at most $\binom{d}{2}$ fill edges for degree $d$); its approximate variant (AMD) is the default in many codes. *Reverse Cuthill–McKee* reduces the bandwidth so that the banded factorization of @sec-math-numerical-direct-solvers-cholesky-factorization applies. *Nested dissection* is described next. After ordering, a symbolic phase computes the nonzero structure of $R$, and the numerical phase works on dense submatrices ("supernodes" or "frontal matrices") with level 3 BLAS (@def-blas-levels).

:::

::: {#def-nested-dissection .definition name="Nested dissection"}

Find a small set $S$ of vertices (a *separator*) whose removal splits the graph into two parts $G_1$, $G_2$ of comparable size with no edges between them. Order the vertices of $G_1$ first, then $G_2$, then $S$ last, and order $G_1$ and $G_2$ recursively in the same way. Eliminating $G_1$ never creates fill in $G_2$ (they share no edges and every fill edge stays inside a part or joins a part to $S$), so the factor has a block structure with zero blocks between the two halves.

:::

::: {#thm-nested-dissection-grid .theorem name="Nested dissection on a grid"}

For the five-point Laplacian on a $k\times k$ grid ($n=k^2$ unknowns), nested dissection with separators along grid lines gives a Cholesky factor with $O(n\log n)$ nonzeros in $O(n^{3/2})$ flops. The natural row-by-row ordering, a band of width $k$, gives $O(n^{3/2})$ nonzeros and $O(n^2)$ flops.

:::

::: {.proof}

1. *Banded order.* Row-by-row numbering makes $A$ banded with bandwidth $k=\sqrt n$; the band fills completely, giving $O(nk)=O(n^{3/2})$ nonzeros and $O(nk^2)=O(n^2)$ flops.

2. *Separator cost.* A separator of the $k\times k$ grid is a line of $k$ vertices. It is eliminated last, after its two sides, and by then it can be adjacent to all of its own vertices and to the separators bounding its region (a constant number of lines of length $O(k)$): it is a dense block of size $O(k)$, costing $O(k^2)$ nonzeros and $O(k^3)$ flops.

3. *Recursion.* Splitting twice (vertically, then horizontally) gives four grids of side $k/2$. With $N(k)$ and $W(k)$ the nonzeros and flops for a $k\times k$ region, $N(k)=4N(k/2)+O(k^2)$ and $W(k)=4W(k/2)+O(k^3)$.

4. By the master theorem, $N(k)=O(k^2\log k)=O(n\log n)$ (balanced case: the $O(k^2)$ work is equal at all $\log k$ levels) and $W(k)=O(k^3)=O(n^{3/2})$ (top level dominates).

:::

::: {#fig-sparse-direct-solvers-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.32]
\foreach \x in {0,...,14} {\foreach \y in {0,...,14} {\fill[rule] (\x,\y) circle (2.2pt);}}
\foreach \y in {0,...,14} {\fill[accent] (7,\y) circle (4pt);}
\foreach \x in {0,...,6,8,9,...,14} {\fill[primary] (\x,7) circle (3.4pt);}
\foreach \y in {0,...,6,8,9,...,14} {\fill[ink] (3,\y) circle (2.8pt); \fill[ink] (11,\y) circle (2.8pt);}
\node[note] at (7,-1.3) {first separator (last in the order)};
\node[note] at (19,7) {second level};
\draw[faint, ->] (16.2,7) -- (14.6,7);
\node[note] at (18.6,3) {third level};
\draw[faint, ->] (16.4,3) -- (11.5,3);
\end{tikzpicture}
\end{center}
```

Nested dissection of a $15\times15$ grid: the middle column (largest dots) separates the grid and is numbered last; the middle row of each half comes next from the end, then the middle columns of the quarters, and so on recursively.

:::
