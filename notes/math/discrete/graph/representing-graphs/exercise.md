<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-graph-1-02 origin="external" source="fit1058-cn-11.12-q2"}
Consider the four graph representations of §11.4: edge lists, adjacency
matrices, adjacency lists, incidence matrices. Suppose graphs have $n$
vertices named $1$ to $n$ and $m$ edges, and vertex numbers are stored in
binary using $\lfloor\log_2n\rfloor+1$ bits each. Determine the total number
of bits used to represent a graph using

(a) an edge list, with the vertex and edge sets listed in full;

(b) an adjacency matrix;

(c) an adjacency list;

(d) an incidence matrix.

In each case, give a simple big-O upper bound in terms of $n$ and $m$
(without floor or ceiling).
:::

::: {.problem #prob-mit6042f10-5-q5 origin="external" source="mit6042f10-5-q5"}
The adjacency matrix of a graph is given below (Section 5.1.6 in the book defines adjacency matrices)
$$\begin{pmatrix}
0&1&1&1&0&1\\
1&0&0&1&1&1\\
1&0&0&1&1&1\\
1&1&1&0&1&0\\
0&1&1&1&0&1\\
1&1&1&0&1&0
\end{pmatrix}$$

(a) Draw the graph defined by this adjacency matrix. Label the vertices of your graph $1, 2, \ldots, 6$ so that vertex $i$ corresponds to row and column $i$ of the matrix.

(b) In a graph, we define the distance between to vertices to be the length of the shortest path between them. We define the diameter of a graph to be the largest distance between any two nodes. What is the diameter of this graph? Explain why.

(c) Find a cycle in this graph of maximum length and explain why it has maximum length.

(d) Give a coloring of the vertices that uses the minimum number of colors. Prove that this a minimum coloring.
:::
