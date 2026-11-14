<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-graph-1-08" status="draft"}
$2^k$.

1. In a connected bipartite graph, the colour of one vertex fixes all the
   others: neighbours get the opposite colour, and connectivity spreads this
   to every vertex. So a connected bipartite graph has exactly $2$
   2-colourings.

2. Different components do not constrain each other, so the choices
   multiply: $2^k$. The answer does not depend on $n$ or $m$.
:::
