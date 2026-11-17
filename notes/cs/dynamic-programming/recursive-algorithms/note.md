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

::: {#rmk-recursive-algorithms-relation .remark name="How to find the relation"}

Ask a question about the optimal solution whose answer would reduce the subproblem to smaller ones ("what happens to the first pin?"), then *locally brute-force* the question: try every answer and take the best. The algorithm is efficient when each question has only polynomially many answers; usually the work per subproblem is the number of answers.

:::
