---
title: "Recursive Algorithms and Dynamic Programming"
sources: [mit6006-15, mit6006r-15]
requires: [cs/graph-algorithms/weighted-shortest-paths, math/discrete/sequences/fibonacci]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 15 and Recitation 15, in our own wording; examples our own (checked by computation); proofs written out in steps. -->

## Recursive algorithms and their shapes

When no known algorithm applies, we design one. A finite program solves inputs of every size only by looping or recursing, so we design *recursively*: solve a problem from solutions of smaller *subproblems*. Draw each subproblem as a vertex, with an edge from $A$ to $B$ when computing $B$ uses $A$. For the recursion to end, this *subproblem graph* must be acyclic. Its shape classifies the design.

| design | subproblem graph |
|---|---|
| brute force | a star: one problem, all candidates checked directly |
| decrease and conquer | a chain: one smaller subproblem (insertion sort) |
| divide and conquer | a tree: disjoint smaller subproblems (merge sort) |
| dynamic programming | a DAG: subproblems shared by several others |
| greedy | one path through the DAG, chosen without trying the others |

## The SRT BOT framework

::: {#def-srtbot .definition name="SRT BOT"}

A recursive algorithm is specified by six parts:

1. **S**ubproblems: a set $X$ of subproblems, each described in words in terms of parameters (often prefixes, suffixes or substrings of the input, or integers up to a bound).
2. **R**elation: a recurrence giving the solution of each subproblem from solutions of others.
3. **T**opological order: an order of the subproblems in which each one comes after those it uses; this shows the relation is acyclic.
4. **B**ase cases: the solutions of the subproblems where the relation does not apply.
5. **O**riginal problem: how to get the answer from the solutions of the subproblems.
6. **T**ime analysis.

:::

For example, merge sort (@def-merge-sort) has subproblems $S(i,j)$, the sorted version of $A[i..j-1]$; relation $S(i,j)=\mathrm{merge}(S(i,m),S(m,j))$ with $m=\lfloor(i+j)/2\rfloor$; order by increasing $j-i$; base cases $S(i,i+1)=[A[i]]$; original problem $S(0,n)$; time $T(n)=2T(n/2)+O(n)=O(n\log n)$. Its subproblem graph is a tree.

## Reusing subproblems

::: {#exm-fibonacci-memo .example name="Fibonacci numbers"}

To compute $F_n$ (@def-fibonacci-sequence) use subproblems $F(i)$ for $0\le i\le n$, the relation $F(i)=F(i-1)+F(i-2)$, increasing $i$ as the order, and base cases $F(0)=0$, $F(1)=1$.

1. Calling the relation recursively without remembering results takes $T(n)=T(n-1)+T(n-2)+O(1)>2T(n-2)$ steps, so $T(n)=\Omega(2^{n/2})$: the call tree recomputes $F(n-k)$ about $F_{k+1}$ times.

2. Remembering each $F(i)$ once computed, there are $n+1$ subproblems, each needing one addition, so $O(n)$ additions.

3. The numbers have $\Theta(n)$ bits, since $\varphi^{n-2}\le F_n\le2^n$ (@prp-fibonacci-1, @prp-fibonacci-2), so each addition costs $O(\lceil n/w\rceil)$ on a word-RAM, and the total is $O(n+n^2/w)$.

:::

::: {#fig-recursive-algorithms-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab,tick] (f4) at (0.00,-2.48) {$F_1$};
\node[lab,tick] (f5) at (0.48,-2.48) {$F_0$};
\node[lab,tick] (f3) at (0.24,-1.86) {$F_2$};
\draw[faint] (f3) -- (f4);
\draw[faint] (f3) -- (f5);
\node[lab,tick] (f6) at (0.96,-1.86) {$F_1$};
\node[lab,tick] (f2) at (0.60,-1.24) {$F_3$};
\draw[faint] (f2) -- (f3);
\draw[faint] (f2) -- (f6);
\node[lab,tick] (f8) at (1.44,-1.86) {$F_1$};
\node[lab,tick] (f9) at (1.92,-1.86) {$F_0$};
\node[lab,tick] (f7) at (1.68,-1.24) {$F_2$};
\draw[faint] (f7) -- (f8);
\draw[faint] (f7) -- (f9);
\node[lab,tick] (f1) at (1.14,-0.62) {$F_4$};
\draw[faint] (f1) -- (f2);
\draw[faint] (f1) -- (f7);
\node[lab,tick] (f12) at (2.40,-1.86) {$F_1$};
\node[lab,tick] (f13) at (2.88,-1.86) {$F_0$};
\node[lab,tick] (f11) at (2.64,-1.24) {$F_2$};
\draw[faint] (f11) -- (f12);
\draw[faint] (f11) -- (f13);
\node[lab,tick] (f14) at (3.36,-1.24) {$F_1$};
\node[lab,tick] (f10) at (3.00,-0.62) {$F_3$};
\draw[faint] (f10) -- (f11);
\draw[faint] (f10) -- (f14);
\node[lab,tick] (f0) at (2.07,0.00) {$F_5$};
\draw[faint] (f0) -- (f1);
\draw[faint] (f0) -- (f10);
\node[small vertex] (g0) at (5.04,-1.2) {$F_0$};
\node[small vertex] (g1) at (5.94,-1.2) {$F_1$};
\node[small vertex] (g2) at (6.84,-1.2) {$F_2$};
\node[small vertex] (g3) at (7.74,-1.2) {$F_3$};
\node[small vertex] (g4) at (8.64,-1.2) {$F_4$};
\node[small vertex] (g5) at (9.54,-1.2) {$F_5$};
\draw[->] (g1) -- (g2);
\draw[->] (g0) to[bend right=40] (g2);
\draw[->] (g2) -- (g3);
\draw[->] (g1) to[bend right=40] (g3);
\draw[->] (g3) -- (g4);
\draw[->] (g2) to[bend right=40] (g4);
\draw[->] (g4) -- (g5);
\draw[->] (g3) to[bend right=40] (g5);
\node[lab] at (7.29,0.1) {subproblem DAG: $6$ vertices};
\node[lab] at (1.68,0.55) {call tree: $15$ calls};
\end{tikzpicture}
\end{center}
```

Computing $F_5$. Left: plain recursion makes $15$ calls, solving $F_3$ twice and $F_2$ three times. Right: the subproblem DAG, with an edge from $F_j$ to $F_i$ when $F_i$ uses $F_j$; with memoization each vertex is solved once, in a topological order.

:::

::: {#def-dynamic-programming .definition name="Dynamic programming, memoization"}

*Dynamic programming* is recursion in which subproblems are shared (the subproblem graph is a DAG in which some vertices have in-degree more than $1$), and each subproblem is solved only once. It is implemented

1. *top down*: recurse as usual, but store each solution in a *memo* (a dictionary keyed by the subproblem) and look it up before recomputing (*memoization*); or
2. *bottom up*: solve all subproblems in a topological order, usually with loops, storing the solutions in a table.

:::

::: {#thm-dp-time .theorem name="Running time of a dynamic program"}

With memoization, a dynamic program runs in time $O\bigl(\sum_{x\in X}\mathrm{work}(x)\bigr)$, where $\mathrm{work}(x)$ is the time to evaluate the relation for $x$ counting each recursive call as $O(1)$ (plus the time for the memo lookups). If $\mathrm{work}(x)=O(W)$ for all $x$, this is $O(|X|\cdot W)$.

:::

::: {.proof}

Each subproblem is solved at most once: the first call stores its solution, and every later call is a lookup. Solving $x$ costs $\mathrm{work}(x)$ plus one call per subproblem it uses, and each such call is either the first one (charged to that subproblem's own solution) or a lookup costing $O(1)$, which is already counted in $\mathrm{work}(x)$.

:::

::: {#rmk-recursive-algorithms-name .remark name="Why the name"}

Richard Bellman chose the name in the 1950s, "programming" meaning planning or scheduling. Two slogans describe the method: *recurse but reuse* (top down) and *careful brute force* (bottom up: try everything, but organised so that each piece is tried once). It suits counting and optimisation problems, whose recurrences are often almost obviously correct. That a problem has a recursive solution built from optimal solutions of subproblems is called *optimal substructure*.

:::

## Two first dynamic programs

::: {#exm-dag-shortest-paths-dp .example name="Shortest paths in a DAG"}

Subproblems $\delta(s,v)$ for $v\in V$; relation $\delta(s,v)=\min\bigl(\{\delta(s,u)+w(u,v):u\in\operatorname{Adj}^-(v)\}\cup\{\infty\}\bigr)$ (guess the last edge); a topological order of $G$; base case $\delta(s,s)=0$; all subproblems are wanted. The time is $\sum_vO(1+\deg^-(v))=O(|V|+|E|)$. DAG relaxation (@thm-dag-relaxation) computes exactly these minima, edge by edge from the side of $u$ instead of $v$.

:::

::: {#exm-bowling .example name="Bowling"}

Pins $0,\dots,n-1$ stand in a row, pin $i$ with value $v_i$ (possibly negative). One throw knocks down either one pin $i$, scoring $v_i$, or two neighbouring pins $i,i+1$, scoring $v_iv_{i+1}$; a pin can be hit only once, and pins may be left standing. Maximise the total score.

1. *Subproblems:* $B(i)$, the best score using only pins $i,\dots,n-1$ (suffixes), for $0\le i\le n$.
2. *Relation:* pin $i$ is skipped, hit alone, or hit with pin $i+1$:
   $$B(i)=\max\{B(i+1),\;v_i+B(i+1),\;v_iv_{i+1}+B(i+2)\}$$
   (the last option only if $i+1<n$).
3. *Order:* decreasing $i$. 4. *Base:* $B(n)=0$. 5. *Original:* $B(0)$.
6. *Time:* $n+1$ subproblems with $O(1)$ work each, so $O(n)$.

For values $3,-2,4,4,-1,2$ the best score is $21$: hit $3$ alone, skip $-2$, hit $4,4$ together, skip $-1$, hit $2$. The best score is the weight of a heaviest path from $B(0)$ to $B(n)$ in the subproblem DAG. A divide-and-conquer attempt (split in the middle, and either hit the two middle pins together or not) also works but takes $O(n^2)$ time and does not generalise as easily.

:::

::: {#fig-recursive-algorithms-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (b0) at (0.0,0) {$B_0$};
\node[lab,tick] at (0.0,-0.5) {21};
\node[small vertex] (b1) at (1.5,0) {$B_1$};
\node[lab,tick] at (1.5,-0.5) {18};
\node[small vertex] (b2) at (3.0,0) {$B_2$};
\node[lab,tick] at (3.0,-0.5) {18};
\node[small vertex] (b3) at (4.5,0) {$B_3$};
\node[lab,tick] at (4.5,-0.5) {6};
\node[small vertex] (b4) at (6.0,0) {$B_4$};
\node[lab,tick] at (6.0,-0.5) {2};
\node[small vertex] (b5) at (7.5,0) {$B_5$};
\node[lab,tick] at (7.5,-0.5) {2};
\node[small vertex] (b6) at (9.0,0) {$B_6$};
\node[lab,tick] at (9.0,-0.5) {0};
\draw[->, hl] (b0) -- node[edge label] {$3$} (b1);
\draw[->] (b0) to[bend left=45] node[edge label] {$-6$} (b2);
\draw[->, hl] (b1) -- node[edge label] {$0$} (b2);
\draw[->] (b1) to[bend left=45] node[edge label] {$-8$} (b3);
\draw[->] (b2) -- node[edge label] {$4$} (b3);
\draw[->, hl] (b2) to[bend left=45] node[edge label] {$16$} (b4);
\draw[->] (b3) -- node[edge label] {$4$} (b4);
\draw[->] (b3) to[bend left=45] node[edge label] {$-4$} (b5);
\draw[->, hl] (b4) -- node[edge label] {$0$} (b5);
\draw[->] (b4) to[bend left=45] node[edge label] {$-2$} (b6);
\draw[->, hl] (b5) -- node[edge label] {$2$} (b6);
\node[lab,tick, anchor=east] at (-0.4,-0.5) {$B(i)$:};
\end{tikzpicture}
\end{center}
```

The subproblem DAG of bowling for pin values $3,-2,4,4,-1,2$. A straight edge $B_i\to B_{i+1}$ handles pin $i$ alone (worth $\max\{v_i,0\}$: hit it or skip it); a curved edge $B_i\to B_{i+2}$ hits pins $i,i+1$ together (worth $v_iv_{i+1}$). The numbers under the vertices are $B(i)$, and the highlighted heaviest path from $B_0$ to $B_6$ has weight $21$.

:::

::: {#rmk-recursive-algorithms-relation .remark name="How to find the relation"}

Ask a question about the optimal solution whose answer would reduce the subproblem to smaller ones ("what happens to the first pin?"), then *locally brute-force* the question: try every answer and take the best. The algorithm is efficient when each question has only polynomially many answers; usually the work per subproblem is the number of answers.

:::
