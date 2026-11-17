<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6042f10-5-q3" status="draft"}
(a) The sentence "By induction, each of these two pieces is connected" is unjustified. The hypotheses $P(k)$ apply only to tangled graphs, and nothing shows that the two pieces (as subgraphs) are tangled.

(b) Two disjoint triangles: $n=6$ and $\lceil6/3\rceil=2$. A set of $1$ or $2$ vertices lies inside the triangles in such a way that some vertex of the set has a neighbour outside it (each triangle has $3$ vertices), so an edge leaves it. The graph is tangled but not connected.

(c) Suppose $G$ is mangled with $n\ge2$ vertices but not connected. Let $C$ be a smallest connected component. There are at least two components, so $|C|\le\frac n2\le\lceil\frac n2\rceil$. Since $G$ is mangled, some edge leaves $C$; but no edge leaves a component. This contradiction shows $G$ is connected.
:::
