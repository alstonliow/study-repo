---
title: "Graph Laplacians and Spectral Clustering"
sources: [mit18065-35]
requires: [math/linear-algebra/vector-spaces/incidence-matrices, math/linear-algebra/matrix-methods/eigenvalue-perturbation-and-interlacing]
status: draft
---

<!-- Added 2026-11-20 from MIT 18.065 (Spring 2018), Lecture 35 (video lecture and problem set; no written lecture notes), in our own wording; proofs written out in steps. Numbers checked with numpy. -->

The Laplacian of a graph is a positive semidefinite matrix whose eigenvalues and eigenvectors describe how the graph hangs together: the number of zero eigenvalues counts the pieces, and the eigenvector of the second eigenvalue suggests where to cut the graph into two clusters. The graph is undirected with $n$ nodes and $m$ edges; for the incidence matrix $A$ give each edge either direction (@def-oriented-incidence-matrix).

::: {#def-graph-laplacian .definition name="Graph Laplacian" related="rmk-incidence-matrices-1"}

The *degree matrix* $D$ is diagonal with $D_{ii}=$ the number of edges at node $i$; the *adjacency matrix* $W$ has $W_{ij}=1$ when $i$ and $j$ are joined and $0$ otherwise. The *Laplacian* is
$$L=D-W=A^{\mathsf T}A .$$
For a weighted graph, $W_{ij}=w_{ij}\ge0$, $D_{ii}=\sum_jw_{ij}$ and $L=A^{\mathsf T}CA$ with the weights on the diagonal of $C$.

:::

::: {#fig-graph-laplacians-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.000,1.650) rectangle (0.550,2.200);
\node[lab] at (0.275,1.925) {$1$};
\draw[cell, fill=primaryLight] (0.550,1.650) rectangle (1.100,2.200);
\node[lab] at (0.825,1.925) {$-1$};
\draw[cell frame] (1.100,1.650) rectangle (1.650,2.200);
\node[lab] at (1.375,1.925) {$0$};
\draw[cell frame] (1.650,1.650) rectangle (2.200,2.200);
\node[lab] at (1.925,1.925) {$0$};
\draw[cell, fill=primaryLight] (0.000,1.100) rectangle (0.550,1.650);
\node[lab] at (0.275,1.375) {$-1$};
\draw[hl cell] (0.550,1.100) rectangle (1.100,1.650);
\node[lab] at (0.825,1.375) {$2$};
\draw[cell, fill=primaryLight] (1.100,1.100) rectangle (1.650,1.650);
\node[lab] at (1.375,1.375) {$-1$};
\draw[cell frame] (1.650,1.100) rectangle (2.200,1.650);
\node[lab] at (1.925,1.375) {$0$};
\draw[cell frame] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$0$};
\draw[cell, fill=primaryLight] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$-1$};
\draw[hl cell] (1.100,0.550) rectangle (1.650,1.100);
\node[lab] at (1.375,0.825) {$2$};
\draw[cell, fill=primaryLight] (1.650,0.550) rectangle (2.200,1.100);
\node[lab] at (1.925,0.825) {$-1$};
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$0$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$0$};
\draw[cell, fill=primaryLight] (1.100,0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$-1$};
\draw[hl cell] (1.650,0.000) rectangle (2.200,0.550);
\node[lab] at (1.925,0.275) {$1$};
\node[lab, note] at (1.100,-0.350) {$L=D-A$};
\node[lab, note, anchor=west, align=left] at (2.6,1.4) {diagonal: degrees $1,2,2,1$\\off-diagonal: $-1$ for each edge\\every row sums to $0$, so $L\mathbf 1=\mathbf 0$};
\node[small vertex] (p0) at (2.9,0.3) {1};
\node[small vertex] (p1) at (3.8,0.3) {2};
\node[small vertex] (p2) at (4.7,0.3) {3};
\node[small vertex] (p3) at (5.6,0.3) {4};
\draw (p0) -- (p1) -- (p2) -- (p3);
\end{tikzpicture}
\end{center}
```

The Laplacian of the path of @exm-path-laplacian: degrees on the diagonal (highlighted), minus the adjacency matrix off it (shaded).

:::

::: {#prp-laplacian-quadratic-form .proposition name="The energy of a Laplacian"}

$$\mathbf{x}^{\mathsf T}L\mathbf{x}=\sum_{\text{edges }\{i,j\}}(x_i-x_j)^2 .$$
So $L$ is positive semidefinite, every row sums to zero, and $L\mathbf{1}=\mathbf{0}$ for $\mathbf{1}=(1,\dots,1)$.

:::

::: {.proof}

1. $L=A^{\mathsf T}A$ gives $\mathbf{x}^{\mathsf T}L\mathbf{x}=\lVert A\mathbf{x}\rVert^2$.

2. Entry $k$ of $A\mathbf{x}$ is $x_j-x_i$ for edge $k$ between $i$ and $j$; its sign does not matter after squaring.

3. $A\mathbf{1}=\mathbf{0}$ since each row of $A$ has one $+1$ and one $-1$.

:::

::: {#fig-graph-laplacians-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (q0) at (0.0,0) {1}; \node[lab, tick] at (0.0,-0.5) {$0.65$};
\node[small vertex] (q1) at (2.0,0) {2}; \node[lab, tick] at (2.0,-0.5) {$0.27$};
\node[small vertex] (q2) at (4.0,0) {3}; \node[lab, tick] at (4.0,-0.5) {$-0.27$};
\node[small vertex] (q3) at (6.0,0) {4}; \node[lab, tick] at (6.0,-0.5) {$-0.65$};
\draw[emph] (q0) -- node[above, lab, note, accent] {$0.144$} (q1);
\draw[emph] (q1) -- node[above, lab, note, accent] {$0.292$} (q2);
\draw[emph] (q2) -- node[above, lab, note, accent] {$0.144$} (q3);
\node[lab, note, anchor=west] at (6.6,0) {$\sum_{\text{edges}}(x_i-x_j)^2\approx0.586=2-\sqrt2$};
\end{tikzpicture}
\end{center}
```

The energy $\mathbf x^{\mathsf T}L\mathbf x=\sum_{\text{edges }ij}(x_i-x_j)^2$ for the Fiedler vector of the path (node values below, edge terms above). The middle edge, where the sign changes, carries the most energy; the total is the eigenvalue $\lambda_2$.

:::

::: {#thm-laplacian-components .theorem name="Zero eigenvalues count connected components"}

The multiplicity of the eigenvalue $0$ of $L$ equals the number of connected components of the graph. In particular the second smallest eigenvalue $\lambda_2(L)$ is positive exactly when the graph is connected.

:::

::: {.proof}

1. $L\mathbf{x}=\mathbf{0}$ if and only if $\mathbf{x}^{\mathsf T}L\mathbf{x}=0$, because $L$ is positive semidefinite ($\lVert A\mathbf{x}\rVert^2=0$ forces $A\mathbf{x}=\mathbf{0}$, so $L\mathbf{x}=A^{\mathsf T}A\mathbf{x}=\mathbf{0}$).

2. By @prp-laplacian-quadratic-form this says $x_i=x_j$ for every edge, so $\mathbf{x}$ is constant on each connected component.

3. The vectors that are constant on each component form a space with one basis vector (the indicator) per component.

:::

::: {#fig-graph-laplacians-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex, fill=primaryLight] (a) at (0,0) {1}; \node[small vertex, fill=primaryLight] (b) at (1,0.7) {2}; \node[small vertex, fill=primaryLight] (c) at (1,-0.7) {3};
\node[small vertex, fill=accentLight] (d) at (3,0.4) {4}; \node[small vertex, fill=accentLight] (e) at (4,0.4) {5}; \node[small vertex, fill=accentLight] (f) at (3.5,-0.5) {6};
\draw (a) -- (b) -- (c) -- (a); \draw (d) -- (e) -- (f) -- (d);
\node[lab, note, anchor=west, align=left] at (4.8,0.1) {$L\mathbf x=\mathbf 0$ for $\mathbf x=(1,1,1,0,0,0)$ (nodes 1--3)\\and for $(0,0,0,1,1,1)$ (nodes 4--6):\\two components, eigenvalue $0$ twice};
\end{tikzpicture}
\end{center}
```

A graph with two connected components. A vector that is constant on each component has zero energy, so the indicator vectors of the components span the nullspace of $L$.

:::

::: {#def-fiedler-vector .definition name="Fiedler vector and spectral clustering"}

Order the eigenvalues of $L$ as $0=\lambda_1\le\lambda_2\le\dots\le\lambda_n$. An eigenvector $\mathbf{z}$ for $\lambda_2$ is a *Fiedler vector*. *Spectral clustering* into two groups puts node $i$ in one group when $z_i\ge0$ and in the other when $z_i<0$.

:::

::: {#thm-fiedler-minimises-energy .theorem name="The Fiedler vector minimises energy"}

$$\lambda_2(L)=\min\Big\{\frac{\mathbf{x}^{\mathsf T}L\mathbf{x}}{\mathbf{x}^{\mathsf T}\mathbf{x}}:\ \mathbf{x}\ne\mathbf{0},\ \mathbf{x}^{\mathsf T}\mathbf{1}=0\Big\},$$
and the minimum is reached at a Fiedler vector.

:::

::: {.proof}

1. $\mathbf{1}/\sqrt n$ is a unit eigenvector for $\lambda_1=0$; extend it to an orthonormal eigenvector basis $\mathbf{q}_1=\mathbf{1}/\sqrt n,\mathbf{q}_2,\dots,\mathbf{q}_n$ (@cor-real-symmetric-orthogonally-diagonalisable).

2. $\mathbf{x}\perp\mathbf{1}$ means $\mathbf{x}=\sum_{k\ge2}c_k\mathbf{q}_k$, so the Rayleigh quotient is a weighted average of $\lambda_2,\dots,\lambda_n$ (step 1 of @thm-courant-fischer), at least $\lambda_2$, with equality at $\mathbf{q}_2$.

:::

::: {#rmk-graph-laplacians-1 .remark name="Why the sign pattern finds clusters"}

To cut the nodes into sets $S$ and $\bar S$ of similar size with few edges between them, try $x_i=+1$ on $S$ and $-1$ on $\bar S$: then $\mathbf{x}^{\mathsf T}L\mathbf{x}=4\times$(edges cut), and $\mathbf{x}\perp\mathbf{1}$ when the sets have equal size. Minimising over such $\pm1$ vectors is hard; allowing any real $\mathbf{x}\perp\mathbf{1}$ relaxes the problem to @thm-fiedler-minimises-energy, and the signs of the Fiedler vector round the answer back. For $k$ clusters one uses the eigenvectors of $\lambda_2,\dots,\lambda_k$ as coordinates and runs $k$-means on the rows.

:::

::: {#exm-path-laplacian .example name="A path of four nodes"}

For the path $1-2-3-4$,
$$L=\begin{bmatrix}1&-1&0&0\\-1&2&-1&0\\0&-1&2&-1\\0&0&-1&1\end{bmatrix},$$
with eigenvalues $0,\ 2-\sqrt2,\ 2,\ 2+\sqrt2$ (that is, $2-2\cos(k\pi/4)$ for $k=0,\dots,3$). The Fiedler vector is approximately $(0.65,\,0.27,\,-0.27,\,-0.65)$, so spectral clustering cuts the middle edge and returns $\{1,2\}$ and $\{3,4\}$.

:::

::: {#fig-graph-laplacians-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex, hl] (n0) at (0.0,0) {1};
\node[lab] at (0.0,-0.55) {$+0.65$};
\node[small vertex, hl] (n1) at (1.6,0) {2};
\node[lab] at (1.6,-0.55) {$+0.27$};
\node[small vertex] (n2) at (3.2,0) {3};
\node[lab] at (3.2,-0.55) {$-0.27$};
\node[small vertex] (n3) at (4.80,0) {4};
\node[lab] at (4.80,-0.55) {$-0.65$};
\draw (n0) -- (n1);
\draw (n1) -- (n2);
\draw (n2) -- (n3);
\draw[emph, dashed] (2.4,0.6) -- (2.4,-0.9);
\end{tikzpicture}
\end{center}
```

The path $1-2-3-4$ with the entries of its Fiedler vector. The signs split the nodes into $\{1,2\}$ and $\{3,4\}$, cutting one edge (dashed).

:::
