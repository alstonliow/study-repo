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
