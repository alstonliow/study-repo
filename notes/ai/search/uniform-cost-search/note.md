---
title: "Uniform Cost Search"
sources: [cs221-7]
requires: [ai/search/search-problems, cs/graph-algorithms/dijkstra]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 7 (uniform cost search and its correctness), in our own wording; proof written out in steps. UCS is Dijkstra's algorithm (@sec-cs-graph-algorithms-dijkstra) run lazily on a search problem; blocks are marked related, merge proposed to the owner. -->

<!-- Merged 2026-11-18 with @sec-cs-graph-algorithms-dijkstra (owner decision): the shared core, the algorithm on an explicit graph and its correctness proof, is kept once in def-dijkstra and thm-dijkstra (MIT 6.006 version, judged more concise; it uses the existing relaxation lemmas). What only CS221 has stays here: lazy frontier, stopping at the first end state, backpointers, and the optimality of the returned solution (old proof steps 1-6 removed, step 7 kept in the new proof). -->

Dynamic programming computes future costs from the end states back to the start, which needs an order in which every state comes after its successors; with cycles there is none. Uniform cost search instead computes costs from the start, in increasing order, and so needs no such order. It requires all costs to be non-negative.

::: {#def-past-cost .definition name="Past cost"}

For a state $s$ of a search problem, $\text{PastCost}(s)$ is the minimum cost of a sequence of actions leading from $s_{\text{start}}$ to $s$ ($\infty$ if there is none).

:::

::: {#def-uniform-cost-search .definition name="Uniform cost search" related="def-dijkstra"}

*Uniform cost search* (UCS) is Dijkstra's algorithm (@def-dijkstra) run on the graph of a search problem with non-negative costs, whose vertices are the states and whose edges are $s\to\text{Succ}(s,a)$ with weight $\text{Cost}(s,a)$, with three changes. The graph is never built: a state enters the priority queue, the *frontier*, only when it is first reached, so states are *explored* (removed with their past cost known), in the frontier (with a tentative cost, its *priority*), or *unexplored*. UCS stops as soon as it removes an end state. And for each state it records the action that last lowered its priority (a *backpointer*), so that the solution can be traced back from the end state. If the frontier becomes empty, there is no solution.

:::

```{=latex}
\begin{algorithm}
\caption{Uniform cost search}
\begin{algorithmic}
\INPUT Search problem with $\text{Cost}\ge0$
\OUTPUT Minimum-cost solution, or none
\STATE $F\gets$ priority queue holding $s_{\text{start}}$ with priority $0$; $E\gets\emptyset$
\WHILE{$F$ is not empty}
    \STATE $(s,p)\gets F.\mathrm{remove\_min}()$; $E\gets E\cup\{s\}$
    \IF{$\text{IsEnd}(s)$}
        \RETURN the actions on the backpointer path from $s_{\text{start}}$ to $s$
    \ENDIF
    \FOR{$a\in\text{Actions}(s)$ with $s'=\text{Succ}(s,a)\notin E$}
        \IF{$s'\notin F$ or $p+\text{Cost}(s,a)<\text{priority}(s')$}
            \STATE $F.\mathrm{update}(s',\,p+\text{Cost}(s,a))$; $P(s')\gets(s,a)$
        \ENDIF
    \ENDFOR
\ENDWHILE
\RETURN none
\end{algorithmic}
\end{algorithm}
```

::: {#thm-uniform-cost-search .theorem name="Correctness of uniform cost search" related="thm-dijkstra"}

If all costs are non-negative, UCS removes states from the frontier in order of non-decreasing priority, and whenever it removes a state $s$,

$$
\text{priority}(s)=\text{PastCost}(s).
$$

In particular, the solution UCS returns has minimum cost.

:::

::: {.proof}

1. Leaving unexplored states out of the frontier is the same as keeping them in it with priority $\infty$: such a state is never the minimum while a state of finite priority remains, and it gets a finite priority exactly when UCS first reaches it. Stopping early only cuts off later removals. So up to the moment UCS stops, it removes the same states in the same order as Dijkstra's algorithm on the graph of the search problem, and by @thm-dijkstra each has $\text{priority}(s)=\delta(s_{\text{start}},s)=\text{PastCost}(s)$ when removed.

2. Priorities are removed in non-decreasing order: when $s$ is removed with the minimum priority $p$, every update sets a priority to $p+\text{Cost}(s,a)\ge p$, so the minimum of the frontier never drops below $p$.

3. Suppose UCS stops at an end state $s$, and let $e$ be any end state. If $e=s$ there is nothing to show. Otherwise $e$ was not removed before $s$, since UCS stops at the first end state it removes. If $\text{PastCost}(e)<\text{PastCost}(s)$, Dijkstra's order (step 2, applied to the full run) would remove $e$ before $s$, a contradiction. So $\text{PastCost}(e)\ge\text{PastCost}(s)$, and the returned solution, the backpointer path of cost $\text{priority}(s)=\text{PastCost}(s)$, has minimum cost.

:::

::: {#exm-ucs-diamond .example name="Uniform cost search with a cycle"}

Take states $A,B,C,D$, start $A$, end $D$, and undirected edges $A\text{–}B$ of cost $1$, $B\text{–}C$ of cost $1$, $C\text{–}D$ of cost $1$, $A\text{–}C$ of cost $100$ and $B\text{–}D$ of cost $100$ (each usable in both directions). The graph has cycles, so dynamic programming does not apply. UCS explores $A$ (priority $0$), then $B$ (priority $1$; $C$ gets $101$ from $A$, then $2$ via $B$, and $D$ gets $101$), then $C$ (priority $2$; $D$ improves to $3$), then $D$ with priority $3$, returning $A\to B\to C\to D$.

:::

::: {#fig-uniform-cost-search-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (A) at (0.00,0.00) {$A$};
\node[small vertex] (B) at (1.50,0.90) {$B$};
\node[small vertex] (C) at (1.50,-0.90) {$C$};
\node[small vertex] (D) at (3.00,0.00) {$D$};
\draw[hl] (A) -- node[edge label, pos=0.5] {1} (B);
\draw[hl] (B) -- node[edge label, pos=0.5] {1} (C);
\draw[hl] (C) -- node[edge label, pos=0.5] {1} (D);
\draw[faint] (A) -- node[edge label, pos=0.5] {100} (C);
\draw[faint] (B) -- node[edge label, pos=0.5] {100} (D);
\node[lab,tick] at (4.6,1.3) {explore};
\node[lab,tick] at (5.50,1.3) {A};
\node[lab,tick] at (6.30,1.3) {B};
\node[lab,tick] at (7.10,1.3) {C};
\node[lab,tick] at (7.90,1.3) {D};
\node[lab,tick] at (4.6,0.85) {A};
\node[lab,tick] at (5.50,0.85) {\textbf{0}};
\node[lab,tick] at (6.30,0.85) {1};
\node[lab,tick] at (7.10,0.85) {100};
\node[lab,tick] at (4.6,0.40) {B};
\node[lab,tick] at (6.30,0.40) {\textbf{1}};
\node[lab,tick] at (7.10,0.40) {2};
\node[lab,tick] at (7.90,0.40) {101};
\node[lab,tick] at (4.6,-0.05) {C};
\node[lab,tick] at (7.10,-0.05) {\textbf{2}};
\node[lab,tick] at (7.90,-0.05) {3};
\node[lab,tick] at (4.6,-0.50) {D};
\node[lab,tick] at (7.90,-0.50) {\textbf{3}};
\end{tikzpicture}
\end{center}
```

Uniform cost search on the graph of the example (undirected edges with their costs). Each row shows the state removed from the frontier (its priority in bold, now its past cost) and the frontier priorities after updating its neighbours. $C$ first gets priority $101$, which drops to $2$ via $B$; $D$ drops from $101$ to $3$.

:::

::: {#rmk-uniform-cost-search-1 .remark}

UCS explores states in order of increasing past cost and stops at the first end state, so it explores every state $s$ with $\text{PastCost}(s)<\text{PastCost}(s_{\text{end}})$, where $s_{\text{end}}$ is the end state reached, and some with equal past cost. With a binary heap as priority queue, each removal and each priority update costs $O(\log N)$ for $N$ states seen. Without knowledge of where the end lies, no algorithm can do better in general: it explores outward in every direction, as on a grid where it fans out in a diamond around the start.

:::
