<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-graph-1-02" status="draft"}
Write $b = \lfloor\log_2 n\rfloor + 1$ for the bits per vertex number.

(a) The vertex list has $n$ numbers and the edge list has $2m$ (two ends per
    edge): $(n + 2m)\,b$ bits, which is $O\bigl((n+m)\log n\bigr)$.

(b) One bit per entry of an $n\times n$ matrix: $n^2$ bits, $O(n^2)$.

(c) The line for vertex $v$ holds $v$ and its $\deg(v)$ neighbours, so
    $(1+\deg v)\,b$ bits. Summing and using $\sum_v\deg v = 2m$ gives
    $(n + 2m)\,b$ bits, $O\bigl((n+m)\log n\bigr)$.

(d) One bit per entry of an $n\times m$ matrix: $nm$ bits, $O(nm)$.

For sparse graphs ($m$ about $n$) the lists are much smaller than the
matrices. For dense graphs ($m$ about $n^2$) the adjacency matrix is the most
compact.
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6042f10-5-q5" status="draft"}
(a) Every vertex has degree $4$; the only non-adjacent pairs are $\{1,5\}$, $\{2,3\}$ and $\{4,6\}$. So the graph is $K_6$ minus a perfect matching (the octahedron): take three "opposite" pairs $\{1,5\},\{2,3\},\{4,6\}$ and join every two vertices from different pairs.

(b) The diameter is $2$. Adjacent vertices are at distance $1$. A non-adjacent pair, such as $1$ and $5$, has a common neighbour ($2$, for instance), so it is at distance $2$, and not $1$.

(c) $1,2,4,3,5,6,1$ is a cycle (check the matrix: $12,24,43,35,56,61$ are edges). It passes through all $6$ vertices, and no cycle can be longer than the number of vertices.

(d) Colour the opposite pairs alike: $\{1,5\}$ red, $\{2,3\}$ green, $\{4,6\}$ blue. Each colour class is a non-adjacent pair, so this is a $3$-colouring. Fewer colours are impossible because $1,2,4$ form a triangle, whose vertices need three different colours.
:::
