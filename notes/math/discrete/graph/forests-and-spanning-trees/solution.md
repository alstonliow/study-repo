<!-- Draft solutions (status="draft") written by Claude. CN chapter 12 has no
     sample solutions, so these were not checked against one. Owner to review. -->

::: {.solution for="prob-graph-2-07" status="draft"}
$11$.

Ignore $ef$ for a moment: it is a bridge and is in every spanning tree. The
rest consists of two cycles that share the edge $bd$: the $4$-cycle
$a\,b\,d\,c$ and the triangle $b\,d\,e$. Their outer boundary is the
$5$-cycle $a\,b\,e\,d\,c$. A spanning tree of this part has $4$ of its $6$
edges, so it drops $2$ edges and must break both cycles.

1. *Trees containing $bd$.* Drop one of the other $3$ edges of the
   $4$-cycle and one of the other $2$ edges of the triangle: $3\cdot2 = 6$.

2. *Trees not containing $bd$.* Dropping $bd$ breaks both cycles but leaves
   the outer $5$-cycle, so drop one of its $5$ edges: $5$.

3. Total: $6 + 5 = 11$. (The Matrix–Tree Theorem gives the same.)
:::

::: {.solution for="prob-graph-2-08" status="draft"}
Sort the edges by weight and add each one unless it closes a cycle:

| step | edge | weight | action |
|---|---|---|---|
| 1 | $bd$ | 1 | add |
| 2 | $cd$ | 2 | add |
| 3 | $bc$ | 3 | reject: $b\,d\,c$ would be a cycle |
| 4 | $de$ | 4 | add |
| 5 | $ce$ | 5 | reject: $c\,d\,e$ would be a cycle |
| 6 | $df$ | 6 | add |
| 7 | $ef$ | 7 | reject: $e\,d\,f$ would be a cycle |
| 8 | $ac$ | 8 | add |

After step 8 there are $5 = 6-1$ edges, so we stop ($ab$ is not needed). The
minimum weight spanning tree is
$$\{bd,\ cd,\ de,\ df,\ ac\},\qquad\text{total weight } 1+2+4+6+8 = 21.$$
:::
