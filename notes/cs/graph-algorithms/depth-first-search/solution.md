<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6006s20-5-q2" status="draft"}
Make an undirected graph whose vertices are the $n$ plants and $n^2$ buildings and whose edges are the wires. A building is powered by plant $p$ exactly when it is in the connected component of $p$, and by assumption no component contains two plants. So the answer is the plant whose component has the most buildings.

Build an adjacency list in $O(|V|+|W|)$ time and run BFS (or DFS) from each plant, counting the buildings reached (@prp-connected-components-algorithm). The searches explore disjoint components, so together they take $O(|V|+|W|)$. There are $|V|=n+n^2$ vertices and at most $\binom{n+n^2}2=O(n^4)$ wires, so the total is $O(n^4)$.
:::
