<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6006s20-5-q1" status="draft"}
(a) The edges are $\{0,2\},\{1,3\},\{1,4\},\{1,5\},\{2,3\},\{2,4\},\{4,5\}$: seven edges on the six vertices (for example, the cycle $1,3,2,4,1$ with $0$ hanging from $2$ and $5$ joined to both $1$ and $4$).

(b) `Adj = {'A': ['B'], 'B': ['C', 'D'], 'C': ['E', 'F'], 'D': ['E', 'F'], 'E': [], 'F': ['D', 'E']}`.

(c) *BFS* visits $A,B,C,D,E,F$, with parents $P(B)=A$, $P(C)=P(D)=B$, $P(E)=P(F)=C$ (levels $\{A\},\{B\},\{C,D\},\{E,F\}$). *DFS* visits $A,B,C,E,F,D$: from $C$ it goes to $E$ (a dead end), then to $F$, and from $F$ to $D$, whose out-neighbours $E,F$ are already visited. Its tree is the path $A\to B\to C\to F\to D$ with the extra branch $C\to E$.

(d) The only cycle is $D\to F\to D$, so exactly the edges $(D,F)$ and $(F,D)$ work. Removing $(D,F)$ leaves the unique topological order $A,B,C,F,D,E$; removing $(F,D)$ allows $A,B,C,D,F,E$ (or $A,B,D,C,F,E$).
:::

::: {.solution for="prob-mit6006s20-5-q2" status="draft"}
Make an undirected graph whose vertices are the $n$ plants and $n^2$ buildings and whose edges are the wires. A building is powered by plant $p$ exactly when it is in the connected component of $p$, and by assumption no component contains two plants. So the answer is the plant whose component has the most buildings.

Build an adjacency list in $O(|V|+|W|)$ time and run BFS (or DFS) from each plant, counting the buildings reached (@prp-connected-components-algorithm). The searches explore disjoint components, so together they take $O(|V|+|W|)$. There are $|V|=n+n^2$ vertices and at most $\binom{n+n^2}2=O(n^4)$ wires, so the total is $O(n^4)$.
:::
