---
title: "Search Problems, Exhaustive Search and Dynamic Programming"
sources: [cs221-6]
requires: [cs/algorithm-design/recursive-algorithms]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 6 (search problems, exhaustive search, dynamic programming, cycles), in our own wording; numbers checked by a short Python computation. -->

Some tasks call for reasoning rather than a reflex: finding a sequence of moves that solves a puzzle, a route between two places, or a word ladder from *cold* to *warm*. When the world is deterministic, such tasks can all be stated in one form, and then solved by general methods instead of one method per task.

::: {#def-search-problem .definition name="Search problem"}

A *search problem* consists of

$$
s_{\text{start}}\in\text{States},\qquad \text{Actions}(s),\qquad \text{Succ}(s,a),\qquad \text{Cost}(s,a),\qquad \text{IsEnd}(s),
$$

namely a start state; for each state $s$ the set of actions available in $s$; the state $\text{Succ}(s,a)$ reached by taking action $a$ in $s$; the cost $\text{Cost}(s,a)$ of doing so; and a test of whether $s$ is an end state. A *solution* is a sequence of actions leading from $s_{\text{start}}$ to an end state; its cost is the sum of the costs of its actions. The goal is a solution of minimum cost.

:::

A search problem is a directed graph with labelled edges: the states are the vertices and each action $a$ in $s$ is an edge from $s$ to $\text{Succ}(s,a)$ with weight $\text{Cost}(s,a)$. A minimum-cost solution is a shortest path from $s_{\text{start}}$ to the set of end states.

::: {#exm-travel-search-problem .example name="Walking and the tram"}

Blocks along a street are numbered $1,\dots,n$. Walking from block $i$ to $i+1$ takes 1 minute; a tram goes from $i$ to $2i$ in 2 minutes. To get from $1$ to $n$ as fast as possible, take States $=\{1,\dots,n\}$, $s_{\text{start}}=1$, $\text{IsEnd}(s)\iff s=n$, and the actions walk (to $s+1$, cost 1, allowed if $s+1\le n$) and tram (to $2s$, cost 2, allowed if $2s\le n$). For $n=10$ the solution walk, tram, walk, tram ($1\to2\to4\to5\to10$) costs $1+2+1+2=6$, and no solution is cheaper.

:::

::: {#rmk-search-problems-1 .remark}

The state must hold exactly the information needed to decide which actions are allowed, what they cost, where they lead and whether we have finished. If the tram needs a ticket and we start with $k$ tickets, the location alone no longer suffices: the state becomes the pair (location, tickets left), and the tram is allowed only when tickets remain and lowers their number by one. For $n=10$ the minimum cost is $9$ with no ticket and $6$ with one or more. If the tram may not be taken twice in a row, the state also records whether the last action was the tram. Extra information is not free: several algorithms below take time proportional to the number of states, so the state should be as small as the problem allows.

:::

## Exhaustive search

::: {#def-future-cost .definition name="Future cost"}

For a state $s$, $\text{FutureCost}(s)$ is the minimum cost of a sequence of actions leading from $s$ to an end state. If the graph of the search problem has no cycles, it satisfies the recurrence

$$
\text{FutureCost}(s)=\begin{cases}0 & \text{if }\text{IsEnd}(s),\\[2pt] \displaystyle\min_{a\in\text{Actions}(s)}\bigl[\text{Cost}(s,a)+\text{FutureCost}(\text{Succ}(s,a))\bigr] & \text{otherwise.}\end{cases}
$$

:::

The recurrence holds because a best solution from $s$ starts with some action $a$ and then must continue with a best solution from $\text{Succ}(s,a)$; trying every first action and keeping the cheapest gives the minimum. A state with no actions that is not an end state has $\text{FutureCost}=\infty$ (minimum over the empty set).

::: {#def-exhaustive-search .definition name="Exhaustive search"}

*Exhaustive search* (backtracking search) evaluates the recurrence of @def-future-cost directly by recursion from $s_{\text{start}}$, without remembering any results, and returns $\text{FutureCost}(s_{\text{start}})$ together with the actions achieving each minimum.

:::

::: {#fig-search-problems-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (t3) at (0.00,-3.30) {$4$};
\node[lab,tick,emph] at (0.42,-3.18) {0};
\node[small vertex] (t2) at (0.00,-2.20) {$3$};
\node[lab,tick,emph] at (0.42,-2.08) {1};
\node[small vertex] (t4) at (1.10,-2.20) {$4$};
\node[lab,tick,emph] at (1.52,-2.08) {0};
\node[small vertex] (t1) at (0.55,-1.10) {$2$};
\node[lab,tick,emph] at (0.97,-0.98) {2};
\node[small vertex] (t7) at (2.20,-3.30) {$4$};
\node[lab,tick,emph] at (2.62,-3.18) {0};
\node[small vertex] (t6) at (2.20,-2.20) {$3$};
\node[lab,tick,emph] at (2.62,-2.08) {1};
\node[small vertex] (t8) at (3.30,-2.20) {$4$};
\node[lab,tick,emph] at (3.72,-2.08) {0};
\node[small vertex] (t5) at (2.75,-1.10) {$2$};
\node[lab,tick,emph] at (3.17,-0.98) {2};
\node[small vertex] (t0) at (1.65,0.00) {$1$};
\node[lab,tick,emph] at (2.07,0.12) {3};
\draw[->] (t2) -- node[edge label, pos=0.5] {W:1} (t3);
\draw[->] (t1) -- node[edge label, pos=0.5] {W:1} (t2);
\draw[->] (t1) -- node[edge label, pos=0.5] {T:2} (t4);
\draw[->] (t6) -- node[edge label, pos=0.5] {W:1} (t7);
\draw[->] (t5) -- node[edge label, pos=0.5] {W:1} (t6);
\draw[->] (t5) -- node[edge label, pos=0.5] {T:2} (t8);
\draw[->] (t0) -- node[edge label, pos=0.5] {W:1} (t1);
\draw[->] (t0) -- node[edge label, pos=0.5] {T:2} (t5);
\end{tikzpicture}
\end{center}
```

Exhaustive search on the travel problem with $n=4$: each tree node is a call, labelled with its state, and the number beside it is the future cost returned. Edges show action:cost (W walk, T tram). The tree has $9$ nodes for only $4$ states; state $4$ is reached three times and state $3$ twice.

:::

```{=latex}
\begin{algorithm}
\caption{Exhaustive search}
\begin{algorithmic}
\INPUT Search problem without cycles
\OUTPUT $\text{FutureCost}(s_{\text{start}})$
\FUNCTION{FutureCost}{$s$}
    \IF{$\text{IsEnd}(s)$}
        \RETURN $0$
    \ENDIF
    \RETURN $\min_{a\in\text{Actions}(s)}\bigl[\text{Cost}(s,a)+\textsc{FutureCost}(\text{Succ}(s,a))\bigr]$
\ENDFUNCTION
\RETURN \textsc{FutureCost}$(s_{\text{start}})$
\end{algorithmic}
\end{algorithm}
```

::: {#rmk-search-problems-2 .remark}

Exhaustive search explores a tree whose nodes are partial solutions, so a state reachable in several ways is explored once per way. On the travel problem it makes $9$ calls for $n=4$ (only $4$ states), $59$ for $n=10$ and $389$ for $n=20$: the time grows exponentially. Its memory is only the recursion stack, linear in the length of a solution.

:::

## Dynamic programming

::: {#def-search-dynamic-programming .definition name="Dynamic programming for search" related="def-dynamic-programming"}

*Dynamic programming* on a search problem without cycles is exhaustive search with a cache: the first time $\text{FutureCost}(s)$ is computed it is stored, and later calls for the same $s$ return the stored value. The cache also records a best action in every state.

:::

::: {#fig-search-problems-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex, fill=accentLight, draw=accent] (v1) at (0.00,0.00) {$1$};
\node[lab,tick,emph] at (0.00,-0.50) {6};
\node[small vertex, fill=accentLight, draw=accent] (v2) at (1.35,0.00) {$2$};
\node[lab,tick,emph] at (1.35,-0.50) {5};
\node[small vertex, fill=accentLight, draw=accent] (v3) at (2.70,0.00) {$3$};
\node[lab,tick,emph] at (2.70,-0.50) {4};
\node[small vertex, fill=accentLight, draw=accent] (v4) at (4.05,0.00) {$4$};
\node[lab,tick,emph] at (4.05,-0.50) {3};
\node[small vertex, fill=accentLight, draw=accent] (v5) at (5.40,0.00) {$5$};
\node[lab,tick,emph] at (5.40,-0.50) {2};
\node[small vertex] (v6) at (6.75,0.00) {$6$};
\node[lab,tick,emph] at (6.75,-0.50) {4};
\node[small vertex] (v7) at (8.10,0.00) {$7$};
\node[lab,tick,emph] at (8.10,-0.50) {3};
\node[small vertex] (v8) at (9.45,0.00) {$8$};
\node[lab,tick,emph] at (9.45,-0.50) {2};
\node[small vertex] (v9) at (10.80,0.00) {$9$};
\node[lab,tick,emph] at (10.80,-0.50) {1};
\node[small vertex, fill=accentLight, draw=accent] (v10) at (12.15,0.00) {$10$};
\node[lab,tick,emph] at (12.15,-0.50) {0};
\draw[->, hl] (v1) -- node[edge label, pos=0.5] {W:1} (v2);
\draw[->, hl] (v2) -- node[edge label, pos=0.5] {W:1} (v3);
\draw[->, hl] (v3) -- node[edge label, pos=0.5] {W:1} (v4);
\draw[->, hl] (v4) -- node[edge label, pos=0.5] {W:1} (v5);
\draw[->] (v5) -- node[edge label, pos=0.5] {W:1} (v6);
\draw[->, hl] (v6) -- node[edge label, pos=0.5] {W:1} (v7);
\draw[->, hl] (v7) -- node[edge label, pos=0.5] {W:1} (v8);
\draw[->, hl] (v8) -- node[edge label, pos=0.5] {W:1} (v9);
\draw[->, hl] (v9) -- node[edge label, pos=0.5] {W:1} (v10);
\draw[->, faint] (v1) to[bend left=55] node[edge label, pos=0.5] {T:2} (v2);
\draw[->, faint] (v2) to[bend left=55] node[edge label, pos=0.5] {T:2} (v4);
\draw[->, faint] (v3) to[bend left=55] node[edge label, pos=0.5] {T:2} (v6);
\draw[->, faint] (v4) to[bend left=55] node[edge label, pos=0.5] {T:2} (v8);
\draw[->, hl] (v5) to[bend left=55] node[edge label, pos=0.5] {T:2} (v10);
\end{tikzpicture}
\end{center}
```

Dynamic programming on the travel problem with $n=10$. The number under each state is its cached future cost; highlighted edges are a best action from each state, and highlighted states the optimal solution $1\to2\to3\to4\to5\to10$ of cost $6$ that these best actions give (walking from $2$ to $4$ costs the same as the tram). Each state is explored once.

:::

```{=latex}
\begin{algorithm}
\caption{Dynamic programming for search}
\begin{algorithmic}
\INPUT Search problem without cycles
\OUTPUT $\text{FutureCost}(s_{\text{start}})$
\STATE $\mathit{cache}\gets$ empty map
\FUNCTION{FutureCost}{$s$}
    \IF{$s\in\mathit{cache}$}
        \RETURN $\mathit{cache}[s]$
    \ENDIF
    \IF{$\text{IsEnd}(s)$}
        \STATE $r\gets0$
    \ELSE
        \STATE $r\gets\min_{a\in\text{Actions}(s)}\bigl[\text{Cost}(s,a)+\textsc{FutureCost}(\text{Succ}(s,a))\bigr]$
    \ENDIF
    \STATE $\mathit{cache}[s]\gets r$
    \RETURN $r$
\ENDFUNCTION
\RETURN \textsc{FutureCost}$(s_{\text{start}})$
\end{algorithmic}
\end{algorithm}
```

::: {#prp-search-dp-cost .proposition name="Cost of dynamic programming for search"}

On a search problem without cycles, dynamic programming evaluates the body of the recurrence at most once per reachable state, so it does

$$
O\Bigl(\sum_{s\text{ reachable}}\bigl(1+|\text{Actions}(s)|\bigr)\Bigr)
$$

work and stores one value per reachable state.

:::

::: {.proof}

1. A call for a state already in the cache returns at once, in constant time.

2. A call for a state not yet in the cache stores its result before returning, so the body (the minimum over the actions) runs at most once per state, and only reachable states are ever called.

3. Each run of the body for $s$ makes $|\text{Actions}(s)|$ calls, each of which, apart from its own body, takes constant time. Summing over reachable states gives the bound; the cache holds one entry per state it has seen.

:::

::: {#rmk-search-problems-3 .remark}

On the travel problem with $n=10$ dynamic programming explores each of the $10$ states once (exhaustive search: $59$ calls), and the cache gives the future costs $6,5,4,3,2,4,3,2,1,0$ of states $1,\dots,10$. Dynamic programming pays off when many action sequences reach the same state; if every action leads to a new state, the cache never hits and only costs memory. Because memory is the scarcer resource, dynamic programming suits problems whose states fit in memory.

:::

## Cycles

::: {#rmk-search-problems-4 .remark}

If the graph has a cycle, the recurrence of @def-future-cost may call itself on the same state forever, so neither exhaustive search nor dynamic programming applies as stated. One remedy is to add the number of steps taken to the state, stop at a fixed limit, and give infinite cost to reaching the limit without reaching an end: every action increases the step count, so the new graph has no cycles, at the price of more states. Algorithms that handle cycles directly are in @sec-ai-search-uniform-cost-search.

:::
