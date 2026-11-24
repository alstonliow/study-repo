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

::: {.solution for="prob-mit6006-11-q1" status="draft"}
Call an edge $(u,v)$ *tight* if $\delta(s,u)$ is finite and $\delta(s,v)=\delta(s,u)+w(u,v)$. Let $R$ be the set of vertices reachable from $s$; for them $\delta(s,\cdot)$ is finite.

1. *Tight paths are shortest.* Along a path $s=u_0,\dots,u_k=v$ of tight edges the weights telescope: $\sum w(u_{i-1},u_i)=\delta(s,v)-\delta(s,s)=\delta(s,v)$. So once every $v\in R$ has a parent-pointer chain of tight edges ending at $s$, the pointers describe shortest paths.

2. *After step (i), every $v\in R\setminus\{s\}$ has a tight parent edge.* A shortest $s$–$v$ path exists (no negative cycles), and its last edge $(u,v)$ is tight with $u\in R$, so the loop sees it. $P(s)$ is never overwritten.

3. *What can go wrong.* Following pointers from $v$ either reaches $s$ or enters a cycle of pointers. Around such a cycle the tight equations sum to: cycle weight $=\sum(\delta(s,\text{head})-\delta(s,\text{tail}))=0$. So the only failures are the zero-weight cycles of step (ii); $s$ lies on none of them.

4. *A needed correction.* Step (iii) must only use vertices $u$ whose chain already reaches $s$. Read literally ("unmarked" = not on a cycle), it can fail. Example: $s\to x$ (weight 1), $x\to y$, $y\to x$, $y\to u$, $u\to x$ (weight 0), with step (i) giving $P(x)=y$, $P(y)=x$, $P(u)=y$. Here $u$ is unmarked, but its chain runs into the cycle. If $u$ is processed first, it sets $P(x)=u$, which creates the new zero-weight cycle $x\to u\to y\to x$; $x$ is now unmarked, so the edge from $s$ never repairs it. So in step (ii) we mark every vertex of $R$ whose chain does *not* reach $s$: the cycle vertices and everything hanging below them. When $P(v)=u$ is set, we unmark $v$ together with all marked vertices whose chain passes through $v$.

5. *Invariant: every unmarked vertex has a chain of tight edges to $s$.* It holds after the corrected step (ii). When step (iii) sets $P(v)=u$, $u$ is unmarked, so $v$'s new chain is the tight edge $(u,v)$ followed by $u$'s chain. A vertex below $v$ reaches $v$ through unchanged tight pointers. Unmarked vertices never change their pointers, so nothing breaks later.

6. *Every vertex of $R$ ends unmarked.* Marks are only removed, and each vertex is processed after it becomes unmarked. Suppose some $x\in R$ is still marked at the end. Take a shortest $s$–$x$ path. All its edges are tight, and $s$ is unmarked, so some edge $(u,v)$ on it has $u$ unmarked and $v$ marked at the end. When $u$ was processed, $v$ was marked (marks are never added), so step (iii) unmarked $v$. This contradicts $v$ being marked at the end.

7. *Linear time.* Step (i) looks at each edge once: $O(|V|+|E|)$. For step (ii), store the children of each vertex under the pointers. A DFS from $s$ over children finds the vertices whose chain reaches $s$; the rest of $R$ is marked, in $O(|V|)$. In step (iii) each vertex enters the worklist once, when it becomes unmarked, and its outgoing edges are scanned once: $O(|V|+|E|)$. Unmarking the vertices below $v$ walks child lists, skipping any child whose pointer has changed. Each vertex is unmarked at most once, so this totals $O(|V|)$.

8. By steps 1, 5 and 6, the final pointers give shortest paths for every vertex of $R$, in $O(|V|+|E|)$ time.
:::
