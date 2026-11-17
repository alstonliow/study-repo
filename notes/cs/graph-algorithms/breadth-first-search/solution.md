<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6006s20-5-q3" status="draft"}
Let $G$ be the graph whose vertices are the friends occurring in some pair (at most $2n$) and whose edges are the $n$ pairs; friends in no pair can go to either party. Two peaceful parties exist exactly when $G$ is bipartite.

Run Full-BFS (@sec-cs-graph-algorithms-depth-first-search) and give each vertex the parity of its BFS distance from the start of its search (party $0$ or $1$). Then check every edge: if some edge joins two vertices of the same parity, answer no; otherwise yes.

*Correctness.* If no edge joins equal parities, the parities are a valid split. If an edge $\{u,v\}$ joins equal parities, the tree paths from the root to $u$ and to $v$ have lengths of equal parity, so together with the edge they form a closed walk of odd length, hence an odd cycle (@thm-odd-closed-walk), and an odd cycle cannot be split into two parties.

*Time.* Building the adjacency lists (with a hash table from friend to list) takes $O(n)$ expected time, and the search and the check are linear in the size of $G$: $O(n)$.
:::

::: {.solution for="prob-mit6006s20-5-q4" status="draft"}
Make a graph $G$ whose vertices are the $(n+1)^2$ grid intersections. Join two neighbouring intersections by an edge if the grid segment between them may be used: it lies on the boundary of the map, or the two squares on its sides are not owned by the same farmer. Each intersection has at most $4$ neighbours, so $G$ has $O(n^2)$ vertices and edges, built in $O(n^2)$ time (comparing two labels is $O(1)$ by the convention that inputs fit in words).

Add a source $s$ joined to every intersection that is a corner of a `'euphris'` square, and run BFS from $s$ (@thm-bfs). Among the intersections that are corners of a `'tigrates'` square, take the one with the smallest distance, and follow parent pointers back to $s$; dropping $s$ gives the route. A shortest path from $s$ is a shortest route from some Euphris intersection, so this is the route (unique by assumption). Total time $O(n^2)$.
:::

::: {.solution for="prob-mit6006s20-5-q5" status="draft"}
*Graph duplication.* What Liza can do next depends on her location, the set $K$ of key cards she holds ($2^4=16$ possibilities) and whether she has a pizza ($2$ possibilities). Make a directed graph $G'$ with a vertex $(\ell,K,p)$ for each of these $32|L|$ states. For each door from $\ell_1$ to $\ell_2$ (both directions for a two-way door) and each state $(\ell_1,K,p)$ in which the door is usable (it needs no card, or its card is in $K$), add an edge to $(\ell_2,K',p')$, where $K'$ adds the card at $\ell_2$ if there is one, and $p'=1$ if $p=1$ or $\ell_2\in\Pi$.

*Search.* Run BFS from $(e,K_0,p_0)$, where $K_0$ and $p_0$ record a card or pizza at $e$ itself, and stop at the first vertex $(e,K,1)$. Edges of $G'$ correspond to walking through one door with the right bookkeeping, so a shortest path in $G'$ to some $(e,K,1)$ is a route with fewest door passages that returns to $e$ with a pizza; parent pointers give it. If no such vertex is reachable, no viable route exists.

*Time.* $G'$ has $32|L|$ vertices and at most $2\cdot32|D|$ edges, so building it and running BFS take $O(|L|+|D|)$ time.
:::

::: {.solution for="prob-mit6006s20-5-q6" status="draft"}
(a) Moves never change the obstacles or the number of sliders, and sliders are indistinguishable. So a reachable configuration is determined by which $s$ of the $n^2-b$ non-obstacle squares hold sliders: at most $\binom{n^2-b}s=\frac1{s!}\prod_{i=0}^{s-1}(n^2-b-i)$ configurations.

(b) *Successors:* one per direction, so at most $r=4$. *Predecessors:* take a board without obstacles in which $s\le n$ sliders sit in the leftmost column, one in each of $s$ different rows. Tilting left sends any configuration with exactly one slider in each of those rows (and none elsewhere) to this one, and each slider can start in any of the $n$ squares of its row: $n^s$ predecessors.

(c) Breadth-first search (@thm-bfs) in the *configuration graph*, whose vertices are configurations and whose edges are single moves, starting from $B$; stop when a configuration with a slider on $t$ is generated, and read the moves off the parent pointers; if the search runs out, report "unsolvable". Generate the graph lazily: a configuration's $4$ successors are computed by `move` in $O(n^2)$ each when it is dequeued, and visited configurations are kept in a hash table (hashing a configuration costs $O(n^2)$). BFS finds a fewest-move solution because distances in this graph are numbers of moves. It only explores configurations at distance less than $k$, of which there are at most $1+4+\dots+4^{k-1}=O(4^k)$, and at most $C(n,b,s)$ in all, each costing $O(n^2)$: $O(n^2\min\{r^k,C(n,b,s)\})$ time.

(d)

```python
def solve_tilt(B, t):
    '''Breadth-first search over board configurations; uses the template's
    move(B, d), which returns the configuration after tilting B in direction d.'''
    xt, yt = t
    if B[yt][xt] == 'o':
        return []
    parent = {B: None}                 # configuration -> (previous, move)
    level = [B]
    while level:
        nxt = []
        for C in level:
            for d in ('up', 'down', 'left', 'right'):
                D = move(C, d)
                if D in parent:
                    continue
                parent[D] = (C, d)
                if D[yt][xt] == 'o':           # solved: read the moves back
                    moves = []
                    while parent[D] is not None:
                        D, d = parent[D]
                        moves.append(d)
                    return moves[::-1]
                nxt.append(D)
        level = nxt
    return None                        # no configuration with a slider on t
```
:::
