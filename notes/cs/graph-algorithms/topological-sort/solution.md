<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6006s20-5-q1" status="draft"}
(a) The edges are $\{0,2\},\{1,3\},\{1,4\},\{1,5\},\{2,3\},\{2,4\},\{4,5\}$: seven edges on the six vertices (for example, the cycle $1,3,2,4,1$ with $0$ hanging from $2$ and $5$ joined to both $1$ and $4$).

(b) `Adj = {'A': ['B'], 'B': ['C', 'D'], 'C': ['E', 'F'], 'D': ['E', 'F'], 'E': [], 'F': ['D', 'E']}`.

(c) *BFS* visits $A,B,C,D,E,F$, with parents $P(B)=A$, $P(C)=P(D)=B$, $P(E)=P(F)=C$ (levels $\{A\},\{B\},\{C,D\},\{E,F\}$). *DFS* visits $A,B,C,E,F,D$: from $C$ it goes to $E$ (a dead end), then to $F$, and from $F$ to $D$, whose out-neighbours $E,F$ are already visited. Its tree is the path $A\to B\to C\to F\to D$ with the extra branch $C\to E$.

(d) The only cycle is $D\to F\to D$, so exactly the edges $(D,F)$ and $(F,D)$ work. Removing $(D,F)$ leaves the unique topological order $A,B,C,F,D,E$; removing $(F,D)$ allows $A,B,C,D,F,E$ (or $A,B,D,C,F,E$).
:::

::: {.solution for="prob-mit6006-10-q1" status="draft"}
1. *A topological order rules out cycles.* Suppose $f$ is a topological order and $v_0\to v_1\to\dots\to v_k=v_0$ is a cycle. Every edge goes forward in $f$, so $f(v_0)<f(v_1)<\dots<f(v_k)=f(v_0)$, a contradiction. So the graph is a DAG.

2. *Every finite DAG has a source.* If every vertex had an incoming edge, we could walk backwards along incoming edges forever; with finitely many vertices some vertex repeats, and the repeated stretch, read forwards, is a cycle.

3. *Every DAG has a topological order*, by induction on $|V|$. The empty graph is trivial. Otherwise take a source $v$ (step 2) and put it first. $G-v$ is still a DAG, so by induction it has a topological order; append it after $v$. Edges out of $v$ go forward because $v$ is first, and edges inside $G-v$ go forward by induction; no edge enters $v$.

4. Together, a directed graph has a topological order exactly when it is a DAG. (@thm-dfs-topological-sort gives a linear-time construction for step 3.)
:::
