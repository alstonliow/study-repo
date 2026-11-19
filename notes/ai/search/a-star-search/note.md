---
title: "A* Search and Relaxed Problems"
sources: [cs221-7, cs188-3]
requires: [ai/search/uniform-cost-search]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 7 (A*, consistency, admissibility, relaxations, combining heuristics), in our own wording; proofs written out in steps. -->

Uniform cost search explores outward from the start in every direction, because past costs know nothing about where the end states are. Ideally we would explore in order of $\text{PastCost}(s)+\text{FutureCost}(s)$, the cost of the best solution through $s$; A* does this with an estimate $h(s)$ of the future cost in place of the exact value.

::: {#def-a-star-search .definition name="A* search"}

A *heuristic* is a function $h$ from states to real numbers that estimates $\text{FutureCost}$. *A\* search* with heuristic $h$ runs uniform cost search (@def-uniform-cost-search) on the *modified search problem*, which has the same start state, actions, successors and end states and the costs

$$
\text{Cost}'(s,a)=\text{Cost}(s,a)+h(\text{Succ}(s,a))-h(s),
$$

and returns the solution found, with its cost recomputed from the original costs.

:::

```{=latex}
\begin{algorithm}
\caption{A* search}
\begin{algorithmic}
\INPUT Search problem, heuristic $h$
\OUTPUT Minimum-cost solution, or none
\STATE $\text{Cost}'(s,a)\gets\text{Cost}(s,a)+h(\text{Succ}(s,a))-h(s)$ for all $s,a$
\STATE $\mathit{sol}\gets$ \textsc{UniformCostSearch}(problem with costs $\text{Cost}'$)
\RETURN $\mathit{sol}$, with cost $\sum\text{Cost}(s,a)$ over its actions
\end{algorithmic}
\end{algorithm}
```

The modified cost of an action is its cost plus a penalty $h(s')-h(s)$ for moving to a state estimated to be farther from the end (a bonus if it is nearer).

::: {#exm-a-star-line .example name="A* on a line"}

States are the integers $-3,\dots,3$, the start is $0$, the end is $2$, and from each state one can step left or right at cost $1$. UCS explores $0,-1,1,-2,2$ (ties broken towards smaller states), wandering away from the end. With $h(s)=2-s$, a step right has modified cost $1+(-1)=0$ and a step left $1+1=2$, so A* explores only $0,1,2$ and returns the path of original cost $2$.

:::

::: {#fig-a-star-search-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab] at (-5.6,0.00) {UCS};
\node[small vertex] (r0s0) at (-4.80,0.00) {$-3$};
\node[small vertex, fill=accentLight, draw=accent] (r0s1) at (-3.20,0.00) {$-2$};
\node[lab,tick,emph] at (-3.20,-0.45) {\#4};
\node[small vertex, fill=accentLight, draw=accent] (r0s2) at (-1.60,0.00) {$-1$};
\node[lab,tick,emph] at (-1.60,-0.45) {\#2};
\node[small vertex, fill=accentLight, draw=accent] (r0s3) at (0.00,0.00) {$0$};
\node[lab,tick,emph] at (0.00,-0.45) {\#1};
\node[small vertex, fill=accentLight, draw=accent] (r0s4) at (1.60,0.00) {$1$};
\node[lab,tick,emph] at (1.60,-0.45) {\#3};
\node[small vertex, fill=accentLight, draw=accent] (r0s5) at (3.20,0.00) {$2$};
\node[lab,tick,emph] at (3.20,-0.45) {\#5};
\node[small vertex] (r0s6) at (4.80,0.00) {$3$};
\draw (r0s0) -- node[edge label] {1} (r0s1);
\draw (r0s1) -- node[edge label] {1} (r0s2);
\draw (r0s2) -- node[edge label] {1} (r0s3);
\draw (r0s3) -- node[edge label] {1} (r0s4);
\draw (r0s4) -- node[edge label] {1} (r0s5);
\draw (r0s5) -- node[edge label] {1} (r0s6);
\node[lab] at (-5.6,-1.50) {A*};
\node[small vertex] (r1s0) at (-4.80,-1.50) {$-3$};
\node[small vertex] (r1s1) at (-3.20,-1.50) {$-2$};
\node[small vertex] (r1s2) at (-1.60,-1.50) {$-1$};
\node[small vertex, fill=accentLight, draw=accent] (r1s3) at (0.00,-1.50) {$0$};
\node[lab,tick,emph] at (0.00,-1.95) {\#1};
\node[small vertex, fill=accentLight, draw=accent] (r1s4) at (1.60,-1.50) {$1$};
\node[lab,tick,emph] at (1.60,-1.95) {\#2};
\node[small vertex, fill=accentLight, draw=accent] (r1s5) at (3.20,-1.50) {$2$};
\node[lab,tick,emph] at (3.20,-1.95) {\#3};
\node[small vertex] (r1s6) at (4.80,-1.50) {$3$};
\draw[->] (r1s0) to[bend left=25] node[edge label] {0} (r1s1);
\draw[->] (r1s1) to[bend left=25] node[edge label] {2} (r1s0);
\draw[->] (r1s1) to[bend left=25] node[edge label] {0} (r1s2);
\draw[->] (r1s2) to[bend left=25] node[edge label] {2} (r1s1);
\draw[->] (r1s2) to[bend left=25] node[edge label] {0} (r1s3);
\draw[->] (r1s3) to[bend left=25] node[edge label] {2} (r1s2);
\draw[->] (r1s3) to[bend left=25] node[edge label] {0} (r1s4);
\draw[->] (r1s4) to[bend left=25] node[edge label] {2} (r1s3);
\draw[->] (r1s4) to[bend left=25] node[edge label] {0} (r1s5);
\draw[->] (r1s5) to[bend left=25] node[edge label] {2} (r1s4);
\draw[->] (r1s5) to[bend left=25] node[edge label] {0} (r1s6);
\draw[->] (r1s6) to[bend left=25] node[edge label] {2} (r1s5);
\end{tikzpicture}
\end{center}
```

Start $0$, end $2$. Top: UCS with all costs $1$ explores five states in the order shown. Bottom: modified costs for $h(s)=2-s$ ($0$ to the right, $2$ to the left); A* explores only $0,1,2$.

:::

Not every heuristic works: a heuristic with $h(s)$ much larger than $h(\text{Succ}(s,a))+\text{Cost}(s,a)$ makes a modified cost negative, and UCS needs non-negative costs.

::: {#def-consistent-heuristic .definition name="Consistent heuristic"}

A heuristic $h$ is *consistent* if

$$
\text{Cost}'(s,a)=\text{Cost}(s,a)+h(\text{Succ}(s,a))-h(s)\ \ge\ 0\quad\text{for all }s,a,\qquad h(s)=0\ \text{ whenever }\text{IsEnd}(s).
$$

:::

The first condition is a triangle inequality: the estimate from $s$ is at most the cost of one step to $s'$ plus the estimate from $s'$.

::: {#thm-a-star-correct .theorem name="Correctness of A*"}

If $h$ is consistent and all costs are non-negative, A* returns a minimum-cost solution of the original problem.

:::

::: {.proof}

1. Take any solution $s_0=s_{\text{start}}\xrightarrow{a_1}s_1\to\cdots\xrightarrow{a_m}s_m$ with $s_m$ an end state. Its modified cost is
$$
\sum_{j=1}^m\bigl[\text{Cost}(s_{j-1},a_j)+h(s_j)-h(s_{j-1})\bigr]=\sum_{j=1}^m\text{Cost}(s_{j-1},a_j)+h(s_m)-h(s_0),
$$
because the $h$ terms telescope.

2. Since $h(s_m)=0$, the modified cost of every solution equals its original cost minus $h(s_{\text{start}})$, a constant that does not depend on the solution. So the two problems have the same minimum-cost solutions.

3. By consistency all modified costs are non-negative, so UCS on the modified problem returns a minimum-cost solution of it (@thm-uniform-cost-search), which by step 2 is a minimum-cost solution of the original problem.

:::

::: {#prp-a-star-explores .proposition name="States explored by A*"}

Let $h$ be consistent and let $s_{\text{end}}$ be the end state A* reaches. Every state $s$ that A* explores satisfies

$$
\text{PastCost}(s)\ \le\ \text{PastCost}(s_{\text{end}})-h(s).
$$

:::

::: {.proof}

1. By the telescoping of @thm-a-star-correct, step 1, applied to paths from $s_{\text{start}}$ to $s$, every such path has modified cost equal to its original cost plus $h(s)-h(s_{\text{start}})$. So the modified past cost of $s$ is $\text{PastCost}(s)+h(s)-h(s_{\text{start}})$.

2. UCS on the modified problem explores states in order of non-decreasing modified past cost (@thm-uniform-cost-search) and stops at $s_{\text{end}}$, so every explored $s$ has modified past cost at most that of $s_{\text{end}}$:
$$
\text{PastCost}(s)+h(s)-h(s_{\text{start}})\ \le\ \text{PastCost}(s_{\text{end}})+h(s_{\text{end}})-h(s_{\text{start}}).
$$

3. Cancel $h(s_{\text{start}})$ and use $h(s_{\text{end}})=0$.

:::

::: {#rmk-a-star-search-1 .remark}

UCS is A* with $h=0$ and explores all states with $\text{PastCost}(s)\le\text{PastCost}(s_{\text{end}})$. The larger $h$, the fewer states A* explores; with $h=\text{FutureCost}$ it explores only states on minimum-cost solutions (with suitable tie-breaking). Useful heuristics lie in between.

:::

::: {#def-admissible-heuristic .definition name="Admissible heuristic"}

A heuristic $h$ is *admissible* if it never overestimates:

$$
h(s)\ \le\ \text{FutureCost}(s)\quad\text{for every state }s.
$$

:::

::: {#prp-consistent-admissible .proposition name="Consistent heuristics are admissible"}

Every consistent heuristic is admissible.

:::

::: {.proof}

1. If $\text{FutureCost}(s)=\infty$ there is nothing to prove. Otherwise take a minimum-cost path $s=s_0\xrightarrow{a_1}s_1\to\cdots\xrightarrow{a_m}s_m$ from $s$ to an end state $s_m$.

2. Consistency gives $h(s_{j-1})\le\text{Cost}(s_{j-1},a_j)+h(s_j)$ for each $j$. Chaining these from $j=1$ to $m$,
$$
h(s)\ \le\ \sum_{j=1}^m\text{Cost}(s_{j-1},a_j)+h(s_m)=\text{FutureCost}(s)+0.
$$

:::

## Heuristics from relaxed problems

Computing $h=\text{FutureCost}$ exactly is as hard as the original problem. Instead, solve an easier problem obtained by removing constraints: knock down the walls of a maze, make the tram free of tickets, or let the tiles of a sliding puzzle overlap. Removing a constraint lowers the cost of a forbidden action from $\infty$ to a finite value, which suggests the general notion.

::: {#def-relaxed-search-problem .definition name="Relaxation"}

A *relaxation* of a search problem has the same $s_{\text{start}}$, $\text{Actions}$, $\text{Succ}$ and $\text{IsEnd}$, and costs $\text{Cost}_{\text{rel}}$ with

$$
\text{Cost}_{\text{rel}}(s,a)\ \le\ \text{Cost}(s,a)\quad\text{for all }s,a.
$$

:::

::: {#thm-relaxation-consistent .theorem name="Relaxed future costs are consistent heuristics"}

If $\text{Cost}_{\text{rel}}\ge0$ and $h(s)=\text{FutureCost}_{\text{rel}}(s)$ is the future cost in a relaxation, then $h$ is a consistent heuristic for the original problem.

:::

::: {.proof}

1. At an end state $h(s)=0$, since the relaxation has the same end states and non-negative costs.

2. For any $s$ and $a$, one way to reach an end state from $s$ in the relaxed problem is to take $a$ and then continue optimally, so $h(s)\le\text{Cost}_{\text{rel}}(s,a)+h(\text{Succ}(s,a))$.

3. By the definition of relaxation, $\text{Cost}_{\text{rel}}(s,a)\le\text{Cost}(s,a)$, so $h(s)\le\text{Cost}(s,a)+h(\text{Succ}(s,a))$, which is consistency.

:::

::: {#rmk-a-star-search-2 .remark}

A relaxed problem pays off only if it is much easier to solve, which is why costs are lowered in a structured way. In a grid maze without walls the future cost from $(r,c)$ to the end $(r_e,c_e)$ has the closed form $|r-r_e|+|c-c_e|$. With a free tram the ticket count drops out of the state, leaving far fewer states. In the sliding puzzle with overlapping tiles each tile moves independently, so the problem splits into independent subproblems whose costs add up. Since the solution of the relaxed problem itself costs time, it should be counted when comparing A* with UCS. If the relaxed problem has cycles, its future costs can be computed by UCS on the reversed relaxed problem (every edge turned around), whose past costs from the end states are the future costs wanted.

:::

::: {#thm-max-heuristic .theorem name="Maximum of consistent heuristics"}

If $h_1$ and $h_2$ are consistent heuristics, so is $h(s)=\max\bigl(h_1(s),h_2(s)\bigr)$.

:::

::: {.proof}

1. At an end state, $h(s)=\max(0,0)=0$.

2. For any $s$ and $a$ with $s'=\text{Succ}(s,a)$, consistency of $h_1$ and $h_2$ gives $h_i(s)\le\text{Cost}(s,a)+h_i(s')$ for $i=1,2$.

3. Hence
$$
h(s)=\max_i h_i(s)\ \le\ \max_i\bigl[\text{Cost}(s,a)+h_i(s')\bigr]=\text{Cost}(s,a)+h(s'),
$$
which is consistency of $h$.

:::

So several relaxations can be combined: the maximum of their heuristics is consistent and, being larger, gives a bound in @prp-a-star-explores at least as tight as each of them.

<!-- Added 2026-11-19 from UC Berkeley CS188 (Fall 2025), Lecture 3 (A* tree search with admissible heuristics, dominance, the 8-puzzle, graph search and consistency), in our own wording; numbers checked by a short Python computation. CS188 states A* directly on the fringe ordered by f = g + h rather than through modified costs; both views give the same order of exploration. -->

::: {#rmk-a-star-search-3 .remark}

Equivalently, A\* is tree or graph search (@def-tree-search) whose fringe is ordered by $f(n)=g(n)+h(n)$, the cost $g(n)$ of the plan to node $n$ plus the heuristic at its state: along any plan the modified costs telescope to $g(n)+h(n)-h(s_{\text{start}})$, and $h(s_{\text{start}})$ is the same for every node.

:::

::: {#thm-a-star-tree-admissible .theorem name="A* tree search with an admissible heuristic"}

If $h$ is admissible, every action costs at least some $\varepsilon>0$, every state has finitely many actions and a solution exists, A\* tree search (no closed set) returns a minimum-cost solution.

:::

::: {.proof}

1. Let $A$ be a node of an optimal end state, with plan cost $C^{*}=g(A)$, and let $B$ be a node of an end state with $g(B)>C^{*}$. We show that $A$ is removed from the fringe before $B$.
2. Suppose $B$ is on the fringe. Until $A$ is removed, some node $n$ on the path from the root to $A$ is on the fringe: the root is there at the start, and whenever such an $n$ is removed and expanded, its child on that path is added.
3. Admissibility gives $h(n)\le$ the cost of the remaining part of $A$'s plan, so $f(n)=g(n)+h(n)\le g(A)=C^{*}$.
4. At end states $h=0$ (admissibility with $\text{FutureCost}=0$), so $f(B)=g(B)>C^{*}\ge f(n)$. Hence $n$ is removed before $B$.
5. Applying step 4 repeatedly, every node on the path to $A$, and finally $A$ itself (with $f(A)=C^{*}<f(B)$), is removed before $B$. Only finitely many nodes have $g\le C^{*}$ (their depth is at most $C^{*}/\varepsilon$ and the branching is finite), and every node removed before $A$ has $f\le C^{*}$, hence $g\le C^{*}$; so the search removes $A$ after finitely many steps.
6. So the first end node removed has cost $C^{*}$, and tree search returns its plan.

:::

::: {#def-heuristic-dominance .definition name="Dominance"}

A heuristic $h_a$ *dominates* $h_c$ if $h_a(s)\ge h_c(s)$ for every state $s$.

:::

Among admissible heuristics, a dominating one gives a bound in @prp-a-star-explores at least as tight, so A\* explores no more states. The heuristics form a semi-lattice under dominance: the trivial heuristic $h=0$ is at the bottom, $\text{FutureCost}$ is at the top, and the maximum of two heuristics (@thm-max-heuristic) dominates both. The trade-off is the cost of computing $h$: $\text{FutureCost}$ itself is perfect but as hard as the problem.

::: {#exm-eight-puzzle-heuristics .example name="Heuristics for the 8-puzzle"}

Eight tiles numbered $1,\dots,8$ and a blank sit in a $3\times3$ grid; an action slides a tile next to the blank into it, at cost $1$. Two relaxations give two consistent heuristics (@thm-relaxation-consistent):

- if a tile may jump to any square, each misplaced tile needs one move: $h_1(s)=$ number of tiles not on their goal square;
- if a tile may slide onto an occupied square, each tile needs as many moves as its Manhattan distance to its goal square: $h_2(s)=$ the sum of these distances.

A tile not on its goal square has Manhattan distance at least $1$, so $h_2$ dominates $h_1$. With the goal $\begin{smallmatrix}\square&1&2\\3&4&5\\6&7&8\end{smallmatrix}$ and the state $\begin{smallmatrix}4&1&2\\7&3&5\\\square&6&8\end{smallmatrix}$, the misplaced tiles are $4,7,3,6$, so $h_1=4$, their distances are $2,2,1,1$, so $h_2=6$, and the true cost is $16$ moves (found by breadth-first search). Both are far below the truth, $h_2$ less so.

:::

With graph search, admissibility is no longer enough: a state reached first by an expensive plan is closed, and a cheaper plan to it arriving later is discarded.

::: {#exm-a-star-graph-inconsistent .example name="Graph search with an inconsistent heuristic"}

Take actions $S\xrightarrow{1}A$, $S\xrightarrow{1}B$, $A\xrightarrow{1}C$, $B\xrightarrow{2}C$, $C\xrightarrow{3}G$ with end state $G$, and $h(S,A,B,C,G)=(2,4,1,1,0)$. The future costs are $(5,4,5,3,0)$, so $h$ is admissible, but $h(A)=4>\text{Cost}(A,C)+h(C)=2$, so it is not consistent. A\* graph search removes $S$ ($f=2$), $B$ ($f=2$), $C$ via $B$ ($g=3$, $f=4$), then $A$ ($f=5$); the child $C$ of $A$, with $g=2$, is discarded because $C$ is closed, and the search returns $S,B,C,G$ of cost $6$ instead of $S,A,C,G$ of cost $5$. With a consistent heuristic this cannot happen (@thm-a-star-correct): the first time a state is removed, its plan is already cheapest.

:::
