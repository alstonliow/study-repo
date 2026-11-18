<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6006s20-6-q3" status="draft"}
*Graph.* Make two copies of the clearings: copy $0$ (before detonation) and copy $1$ (after). In copy $0$, direct each slope from its higher to its lower endpoint according to the elevations $e$; in copy $1$, according to the new elevations ($e'_i$ for $c_i\in C_D$, $e_i$ otherwise), omitting a slope whose endpoints now have equal elevation. Weights are the lengths. Add an edge of weight $0$ from $D$ in copy $0$ to $D$ in copy $1$ (detonating).

*Acyclic.* Within a copy every edge strictly decreases elevation, so there is no cycle, and the only edge between copies goes from copy $0$ to copy $1$. So the graph is a DAG.

*Answer.* Run DAG relaxation (@thm-dag-relaxation) from $L$ in copy $0$ and return the smaller of the distances to $S$ in copy $0$ and in copy $1$. A route without detonation is a path in copy $0$; a route that detonates at $D$ is a path in copy $0$ to $D$, the $0$-weight edge, and a path in copy $1$. The graph has $O(n)$ vertices and edges, so the time is $O(n)$.
:::

::: {.solution for="prob-mit6006r-11-q2" status="draft"}
1. *Graph.* Make a vertex per class and, for each class $c$ with prerequisite $p$, a directed edge $p\to c$ whose weight is the surveyed stress of taking $c$ after only $p$. Add a source $x$ with a weight-$0$ edge to every class that has no prerequisites (such a class can be taken at any time).

2. *Paths are plans.* A path $x\to c_1\to\dots\to c_m=$ 19.854 is a sequence of classes in which each class is taken right after one of its prerequisites, and its weight is the total stress. Conversely, if a plan takes exactly one prerequisite before each class, the classes that 19.854 depends on form such a path. So we want a minimum-weight path from $x$ to 19.854.

3. *Acyclic.* The prerequisite relation has no cycles (otherwise no class on the cycle could ever be taken), so the graph is a DAG. Run DAG relaxation from $x$: a topological sort, then relax the edges in that order. This takes $O(|V|+|E|)$, which is linear in the size of the input. Follow parent pointers back from 19.854 to read off the sequence.
:::
