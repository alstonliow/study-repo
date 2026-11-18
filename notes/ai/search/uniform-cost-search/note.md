---
title: "Uniform Cost Search"
sources: [cs221-7]
requires: [ai/search/search-problems, cs/data-structures/binary-heaps]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 7 (uniform cost search and its correctness), in our own wording; proof written out in steps. UCS is Dijkstra's algorithm (@sec-cs-graph-algorithms-dijkstra) run lazily on a search problem; blocks are marked related, merge proposed to the owner. -->

Dynamic programming computes future costs from the end states back to the start, which needs an order in which every state comes after its successors; with cycles there is none. Uniform cost search instead computes costs from the start, in increasing order, and so needs no such order. It requires all costs to be non-negative.

::: {#def-past-cost .definition name="Past cost"}

For a state $s$ of a search problem, $\text{PastCost}(s)$ is the minimum cost of a sequence of actions leading from $s_{\text{start}}$ to $s$ ($\infty$ if there is none).

:::

::: {#def-uniform-cost-search .definition name="Uniform cost search" related="def-dijkstra"}

*Uniform cost search* (UCS) on a search problem with non-negative costs keeps every state in one of three sets: *explored* (its past cost is known), *frontier* (seen, with a tentative cost called its *priority*), and *unexplored*. Initially the frontier holds $s_{\text{start}}$ with priority $0$. Repeatedly, it removes a frontier state $s$ of minimum priority and moves it to the explored set; if $\text{IsEnd}(s)$, it stops and returns the solution traced back through stored backpointers. Otherwise, for each action $a$ with $s'=\text{Succ}(s,a)$ not explored, it sets the priority of $s'$ to $\text{priority}(s)+\text{Cost}(s,a)$ if $s'$ is unexplored or this value is smaller than its current priority, and records $(s,a)$ as the backpointer of $s'$. If the frontier becomes empty, there is no solution.

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

If all costs are non-negative, then whenever UCS moves a state $s$ from the frontier to the explored set,

$$
\text{priority}(s)=\text{PastCost}(s).
$$

In particular, the solution UCS returns has minimum cost.

:::

::: {.proof}

1. The priority of a frontier state is always the cost of an actual path to it, namely the backpointer path, so $\text{priority}(s)\ge\text{PastCost}(s)$ at all times. It remains to show $\text{priority}(s)\le\text{cost}(\pi)$ for every path $\pi$ from $s_{\text{start}}$ to $s$, at the moment $s$ is removed.

2. We use induction on the order of removal. The first state removed is $s_{\text{start}}$, with priority $0=\text{PastCost}(s_{\text{start}})$ since costs are non-negative.

3. Now let $s\ne s_{\text{start}}$ be removed, and assume every state explored earlier has priority equal to its past cost. Take any path $\pi$ from $s_{\text{start}}$ to $s$. It starts in the explored set and ends outside it, so it has a first edge $(t,u)$ with $t$ explored and $u$ not explored.

4. When $t$ was explored, UCS considered the edge $(t,u)$, so afterwards $u$ is in the frontier with $\text{priority}(u)\le\text{priority}(t)+\text{Cost}(t,u)$; priorities only decrease, so this still holds.

5. The part of $\pi$ up to $t$ costs at least $\text{PastCost}(t)=\text{priority}(t)$ (induction hypothesis), and the part after $u$ costs at least $0$. Therefore
$$
\text{cost}(\pi)\ \ge\ \text{priority}(t)+\text{Cost}(t,u)\ \ge\ \text{priority}(u)\ \ge\ \text{priority}(s),
$$
the last step because $s$ has minimum priority in the frontier.

6. So $\text{priority}(s)\le\text{cost}(\pi)$ for every such $\pi$, hence $\text{priority}(s)=\text{PastCost}(s)$.

7. Suppose UCS stops at an end state $s$, and let $\pi$ be a path to any end state $e$. If $e=s$, $\text{cost}(\pi)\ge\text{priority}(s)$ by step 6. Otherwise $e$ has not been explored, since UCS stops at the first end state it explores; so $\pi$ leaves the set explored before $s$, and steps 3 to 5 give $\text{cost}(\pi)\ge\text{priority}(s)$ again. Hence the returned solution, of cost $\text{priority}(s)$, has minimum cost.

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
