---
title: "Graphs, Networks and Incidence Matrices"
sources: [mit1806-12]
requires: [math/linear-algebra/vector-spaces/matrix-spaces-and-rank-one, math/discrete/graph/representing-graphs]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 12, in our own wording; proofs written out in steps. Example numbers checked with sympy. The graph-theory side (unsigned incidence matrix, adjacency matrix) is in the note on representing graphs; this note is the linear-algebra side. -->

::: {#def-oriented-incidence-matrix .definition name="Incidence matrix of a directed graph" related="def-incidence-matrix"}

Let a graph have $n$ nodes and $m$ edges, each edge given a direction. Its *incidence matrix* is the $m\times n$ matrix $A$ with one row per edge: if edge $k$ goes from node $i$ to node $j$, row $k$ has $-1$ in column $i$, $+1$ in column $j$, and $0$ elsewhere.

:::

This is the transpose, with signs, of the incidence matrix of @def-incidence-matrix. The signs turn $A$ into a difference operator: if $\mathbf{x}$ assigns a *potential* $x_i$ to every node, then $(A\mathbf{x})_k=x_j-x_i$ is the potential difference across edge $k$.

::: {#exm-incidence-matrix-four-nodes .example name="Four nodes, five edges"}

Edges $1\to2$, $2\to3$, $1\to3$, $1\to4$, $3\to4$ give
$$A=\begin{bmatrix}-1&1&0&0\\0&-1&1&0\\-1&0&1&0\\-1&0&0&1\\0&0&-1&1\end{bmatrix}.$$
$N(A)$ is the line through $(1,1,1,1)$; the rank is $3$. A basis of $N(A^{\mathsf T})$ is $(1,1,-1,0,0)$ (around the loop $1\to2\to3\to1$) and $(0,0,1,-1,1)$ (around $1\to3\to4\to1$).

:::

::: {#fig-incidence-matrices-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (n1) at (0.000,0.000) {$1$};
\node[small vertex] (n2) at (2.200,0.000) {$2$};
\node[small vertex] (n3) at (2.200,1.600) {$3$};
\node[small vertex] (n4) at (0.000,1.600) {$4$};
\draw[->] (n1) -- node[edge label] {1} (n2);
\draw[->] (n2) -- node[edge label] {2} (n3);
\draw[->] (n1) -- node[edge label] {3} (n3);
\draw[->] (n1) -- node[edge label] {4} (n4);
\draw[->] (n3) -- node[edge label] {5} (n4);
\end{tikzpicture}
\end{center}
```

The graph of the example: four nodes, five directed edges, two independent loops.

:::

::: {#thm-incidence-matrix-subspaces .theorem name="The four subspaces of an incidence matrix"}

Let $A$ be the incidence matrix of a connected directed graph with $n$ nodes and $m$ edges.

1. $N(A)$ is the line of constant vectors $c\,(1,\dots,1)$, so $\operatorname{rank}A=n-1$.
2. $A\mathbf{x}=\mathbf{e}$ is solvable exactly when the potential differences $\mathbf{e}$ add to zero around every loop.
3. $N(A^{\mathsf T})$ consists of the flows $\mathbf{y}$ on the edges that satisfy *Kirchhoff's current law* $A^{\mathsf T}\mathbf{y}=\mathbf{0}$ (flow in equals flow out at every node); its dimension $m-n+1$ is the number of independent loops.
4. The rows of $A$ that belong to a spanning tree are a basis of the row space.

:::

::: {.proof}

1. If $A\mathbf{x}=\mathbf{0}$, every edge joins two nodes with equal potential. The graph is connected, so all potentials are equal. Constant vectors satisfy $A\mathbf{x}=\mathbf{0}$ because each row sums to zero. Hence $\dim N(A)=1$ and $r=n-1$ (@thm-fundamental-theorem-dimensions).

2. Component $i$ of $A^{\mathsf T}\mathbf{y}$ is the sum of the $y_k$ on edges entering node $i$ minus those leaving it. So $A^{\mathsf T}\mathbf{y}=\mathbf{0}$ is Kirchhoff's current law, and $\dim N(A^{\mathsf T})=m-r=m-n+1$. A loop traversed with signs gives such a $\mathbf{y}$.

3. $A\mathbf{x}=\mathbf{e}$ is solvable iff $\mathbf{e}\in C(A)$, iff $\mathbf{e}$ is orthogonal to every vector of $N(A^{\mathsf T})$ (@thm-fundamental-theorem-orthogonality), iff the signed sum of $\mathbf{e}$ around every loop is $0$.

4. A spanning tree has $n-1$ edges and no loop, so no combination of its rows vanishes (a vanishing combination would be a nonzero element of $N(A^{\mathsf T})$ supported on the tree, i.e. a flow without a loop, which is impossible: a leaf edge of the support would violate Kirchhoff's law at the leaf). So these $n-1=r$ rows are independent and form a basis.

:::

::: {#cor-euler-formula-from-rank .corollary name="Euler's formula"}

For a connected graph,
$$(\#\text{nodes})-(\#\text{edges})+(\#\text{independent loops})=1.$$

:::

::: {.proof}

1. By @thm-incidence-matrix-subspaces the number of independent loops is $\dim N(A^{\mathsf T})=m-n+1$.

2. So $n-m+(m-n+1)=1$.

:::

In @exm-incidence-matrix-four-nodes: $4-5+2=1$.

::: {#rmk-incidence-matrices-1 .remark name="Networks and A^T C A"}

In an electrical network, potentials $\mathbf{x}$ give potential differences $\mathbf{e}=A\mathbf{x}$; Ohm's law gives currents $\mathbf{y}=C\mathbf{e}$ with a diagonal matrix $C$ of conductances; Kirchhoff's law says $A^{\mathsf T}\mathbf{y}=\mathbf{f}$ for the external currents $\mathbf{f}$. Together: $A^{\mathsf T}CA\,\mathbf{x}=\mathbf{f}$. The matrix $A^{\mathsf T}A$ is the graph Laplacian: degrees on the diagonal, $-1$ for each edge off the diagonal.

:::
