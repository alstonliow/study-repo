---
title: "Approximate Search: Best-of-n and Beam Search"
sources: [cs221-6]
requires: [ai/search/search-problems]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 6 (best-of-n, beam search), in our own wording. -->

Exact methods take time at least proportional to the number of states (@prp-search-dp-cost). When the state is a set of locations or the sequence of words generated so far, the number of states is astronomically large and exact search is hopeless. Approximate methods look at only some of the actions and accept that they may miss the best solution.

::: {#def-search-policy .definition name="Policy and rollout"}

A *policy* $\pi$ assigns to each state $s$ a probability distribution $\pi(a\mid s)$ over $\text{Actions}(s)$. A *rollout* of $\pi$ starts at $s_{\text{start}}$ and repeatedly draws an action from $\pi(\cdot\mid s)$ and moves to $\text{Succ}(s,a)$, until it reaches an end state or a step limit.

:::

::: {#def-best-of-n .definition name="Best-of-n"}

*Best-of-$n$* performs $n$ independent rollouts of a policy $\pi$ and returns the cheapest of the solutions found.

:::

```{=latex}
\begin{algorithm}
\caption{Best-of-$n$}
\begin{algorithmic}
\INPUT Search problem, policy $\pi$, number of rollouts $n$, step limit $T$
\OUTPUT Cheapest solution found
\STATE $\mathit{best}\gets$ none
\FOR{$i=1,\dots,n$}
    \STATE $s\gets s_{\text{start}}$; $\mathit{path}\gets$ empty
    \WHILE{not $\text{IsEnd}(s)$ and $|\mathit{path}|<T$}
        \STATE draw $a\sim\pi(\cdot\mid s)$; append $a$ to $\mathit{path}$; $s\gets\text{Succ}(s,a)$
    \ENDWHILE
    \IF{$\text{IsEnd}(s)$ and $\mathit{path}$ is cheaper than $\mathit{best}$}
        \STATE $\mathit{best}\gets\mathit{path}$
    \ENDIF
\ENDFOR
\RETURN $\mathit{best}$
\end{algorithmic}
\end{algorithm}
```

::: {#prp-best-of-n-convergence .proposition name="Best-of-n converges"}

Suppose some minimum-cost solution $a_1,\dots,a_m$ with $m\le T$ has positive probability $p=\prod_{j}\pi(a_j\mid s_{j-1})$ under the policy. Then best-of-$n$ returns a minimum-cost solution with probability at least $1-(1-p)^n$, which tends to $1$ as $n\to\infty$.

:::

::: {.proof}

1. A single rollout follows exactly the actions $a_1,\dots,a_m$ with probability $p$, because each action is drawn from $\pi(\cdot\mid s)$ given the current state and the states $s_0=s_{\text{start}},s_1,\dots$ are determined by the earlier actions.

2. The $n$ rollouts are independent, so the probability that none of them follows this solution is $(1-p)^n$.

3. If at least one rollout follows it, the cheapest solution found has minimum cost. Hence the probability of success is at least $1-(1-p)^n$, and $(1-p)^n\to0$ since $0<p\le1$.

:::

::: {#rmk-approximate-search-1 .remark}

The probability $p$ can be exponentially small in the length of the solution (for a uniform policy with two actions per state it is $2^{-m}$), so the number of rollouts needed can be exponential. On the other hand the rollouts are independent and can run in parallel, and a good policy (for example a learned one) puts most of its probability on good actions.

:::

::: {#rmk-approximate-search-3 .remark editor="true"}

No static figure for best-of-$n$: its rollouts are random, so a drawing of particular rollouts would show one arbitrary run rather than the method; the beam search figure below shows a deterministic run on the same problem.

:::

::: {#def-beam-search .definition name="Beam search"}

*Beam search* with *beam width* $K$ keeps a set of at most $K$ partial solutions, the *beam*, starting from the empty solution. At each step it extends every partial solution in the beam by every action available in its last state, and keeps the $K$ cheapest extensions as the new beam; partial solutions that already end in an end state are kept unchanged. After a step limit it returns the cheapest complete solution in the beam.

:::

```{=latex}
\begin{algorithm}
\caption{Beam search}
\begin{algorithmic}
\INPUT Search problem, beam width $K$, step limit $T$
\OUTPUT Cheapest solution in the final beam
\STATE $B\gets\{\text{empty solution at }s_{\text{start}}\}$
\FOR{$t=1,\dots,T$}
    \STATE $C\gets\{\,p : p\in B\text{ ends in an end state}\,\}$
    \FOR{$p\in B$ not ending in an end state, $s$ its last state}
        \FOR{$a\in\text{Actions}(s)$}
            \STATE add $p$ extended by $a$ to $C$
        \ENDFOR
    \ENDFOR
    \STATE $B\gets$ the $K$ cheapest members of $C$
\ENDFOR
\RETURN the cheapest member of $B$ that ends in an end state
\end{algorithmic}
\end{algorithm}
```

::: {#exm-beam-search-travel .example name="Beam search on the travel problem"}

Run beam search on @exm-travel-search-problem with $n=10$, ties broken by order of generation (walk before tram). With $K=1$ the cheaper first step, walking, always wins, and the result is to walk all the way, at cost $9$. With $K=2$ the beam keeps a second candidate, and beam search finds $1\to2\to3\to4\to5\to10$ of cost $1+1+1+1+2=6$, which is optimal; larger $K$ also gives $6$.

:::

::: {#fig-approximate-search-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab,tick] at (0,0.55) {step};
\node[lab,tick,anchor=west] at (0.6,0.55) {beam (partial solution, cost)};
\node[lab,tick] at (0,0.00) {0};
\node[lab, anchor=west] at (0.60,0.00) {$1$\ \ (0)};
\node[lab,tick] at (0,-0.50) {1};
\node[lab, anchor=west] at (0.60,-0.50) {$1\to2$\ \ (1)};
\node[lab, anchor=west] at (5.20,-0.50) {$1\to2$\ \ (2)};
\node[lab,tick] at (0,-1.00) {2};
\node[lab, anchor=west] at (0.60,-1.00) {$1\to2\to3$\ \ (2)};
\node[lab, anchor=west] at (5.20,-1.00) {$1\to2\to4$\ \ (3)};
\node[lab,tick] at (0,-1.50) {3};
\node[lab, anchor=west] at (0.60,-1.50) {$1\to2\to3\to4$\ \ (3)};
\node[lab, anchor=west] at (5.20,-1.50) {$1\to2\to3\to6$\ \ (4)};
\node[lab,tick] at (0,-2.00) {4};
\node[lab, anchor=west] at (0.60,-2.00) {$1\to2\to3\to4\to5$\ \ (4)};
\node[lab, anchor=west] at (5.20,-2.00) {$1\to2\to3\to4\to8$\ \ (5)};
\node[lab,tick] at (0,-2.50) {5};
\node[lab, anchor=west] at (0.60,-2.50) {$1\to2\to3\to4\to5\to6$\ \ (5)};
\node[lab, hl, anchor=west] at (5.20,-2.50) {$1\to2\to3\to4\to5\to10$\ \ (6)};
\node[lab,tick] at (0,-3.00) {6};
\node[lab, hl, anchor=west] at (0.60,-3.00) {$1\to2\to3\to4\to5\to10$\ \ (6)};
\node[lab, anchor=west] at (5.20,-3.00) {$1\to2\to3\to4\to5\to6\to7$\ \ (6)};
\end{tikzpicture}
\end{center}
```

Beam search with $K=2$ on the travel problem with $n=10$: the beam after each step, cheapest first. A complete solution (highlighted) is kept unchanged; from step 6 on it stays the cheapest, with cost $6$. With $K=1$ only the first column would survive, which walks all the way.

:::

::: {#rmk-approximate-search-2 .remark}

The beam width trades speed for accuracy. With $K=1$ beam search is greedy search: it always takes the cheapest next action. As $K\to\infty$ nothing is ever discarded and beam search becomes exhaustive search. Beam search is deterministic and ranks candidates by cost alone, while best-of-$n$ uses the policy as prior knowledge and is simpler to parallelise. Both apply to the generation of text by a language model, where a state is the text so far and an action is the next word; spending more computation on such search at answer time is called test-time compute.

:::
