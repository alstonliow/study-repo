<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-graph-1-09 origin="external" source="fit1058-cn-11.12-q9"}
Consider the four-vertex multigraph below (Figure 11.8). Determine if it has
a trail that includes every edge, and also if it has an Euler tour.

```{=latex}
\begin{center}
    \begin{tikzpicture}[every node/.style={circle,fill,inner sep=1.8pt}]
        \node (A) at (0,1.4) {};
        \node (B) at (2.4,1.4) {};
        \node (C) at (2.4,0) {};
        \node (D) at (0,0) {};
        \draw (A)--(B)--(C)--(D)--(A);
        \draw (A)--(C); \draw (B)--(D);
        \draw (A) to[bend left=35] (B);
        \draw (B) to[bend left=50] (C);
        \draw (C) to[bend left=35] (D);
        \draw (D) to[bend left=50] (A);
    \end{tikzpicture}
    \end{center}
```
:::

::: {.problem #prob-graph-1-10 origin="external" source="fit1058-cn-11.12-q10"}
Each of the five platonic solids (tetrahedron, cube, octahedron,
dodecahedron, icosahedron) has a skeleton graph. For each of these five
graphs: find a Hamiltonian cycle; determine if it is Eulerian, and if so,
find an Euler tour.
:::

::: {.problem #prob-graph-1-11 origin="external" source="fit1058-cn-11.12-q11"}
Let $Q_n$ be the graph whose vertices are all $n$-bit strings, two being
adjacent iff they differ in exactly one bit.

(a) Draw the cube $Q_3$.

(b) Find a Hamiltonian cycle in $Q_3$.

(c) Describe a method for constructing a Hamiltonian cycle in $Q_n$ for
    each $n$. Think recursively.

(d) Find an Eulerian cycle in $Q_4$.
:::

::: {.problem #prob-graph-1-12 origin="external" source="fit1058-cn-11.12-q12"}
Theorem 64 (Euler): *A connected (simple) graph has an Euler tour iff
every vertex has even degree.* Using Theorem 64 as a black box (don’t re-do
its proof), show that a connected *multigraph* is Eulerian iff every
vertex has even degree. (Hint: from any multigraph $G$, construct a simple
graph $H$ such that applying Theorem 64 to $H$ helps.)
:::
