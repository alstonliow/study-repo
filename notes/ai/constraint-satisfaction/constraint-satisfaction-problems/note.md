---
title: "Constraint Satisfaction Problems"
sources: [cs188-4]
requires: [ai/search/tree-and-graph-search]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley CS188 (Fall 2025), Lecture 4 (CSPs, constraint graphs, examples, varieties of CSPs and constraints, the standard search formulation), in our own wording; counts checked by a short Python computation. -->

In a search problem (@def-search-problem) the path matters: the answer is a plan. In many problems only the final state matters, and a state has a fixed structure, values for a set of variables. Exploiting that structure gives general methods much faster than blind search.

::: {#def-csp .definition name="Constraint satisfaction problem"}

A *constraint satisfaction problem* (CSP) consists of variables $X_1,\dots,X_n$, a *domain* $D_i$ of possible values for each $X_i$, and a set of *constraints*. A constraint has a *scope*, a tuple of variables $(X_{i_1},\dots,X_{i_k})$, and a relation $R\subseteq D_{i_1}\times\dots\times D_{i_k}$ listing the allowed combinations of their values.

An *assignment* gives values to some of the variables; it is *consistent* if it violates no constraint whose variables it all assigns, and *complete* if it assigns every variable. A *solution* is a complete consistent assignment.

:::

A constraint with one variable is *unary* (it just shrinks a domain), with two *binary*, and with more *higher-order*. Constraints can be listed explicitly or given implicitly by a test, such as $X_i\ne X_j$.

::: {#exm-map-colouring-csp .example name="Map colouring"}

Five regions $A,B,C,D,E$ are to be coloured red, green or blue so that neighbours differ, where the neighbouring pairs are $AB$, $AC$, $BC$, $BD$, $CD$, $CE$, $DE$. As a CSP: variables $A,\dots,E$, every domain $\{r,g,b\}$, and one binary constraint $X\ne Y$ for each neighbouring pair. Of the $3^{5}=243$ complete assignments exactly $6$ are solutions, for instance $A=r$, $B=g$, $C=b$, $D=r$, $E=g$: the triangle $A,B,C$ uses all three colours, and then $D$ (next to $B,C$) and $E$ (next to $C,D$) are forced, so the solutions correspond to the $3!$ colourings of the triangle.

:::

::: {#def-constraint-graph .definition name="Constraint graph"}

The *constraint graph* of a CSP with only unary and binary constraints has the variables as vertices and an edge between two variables whenever a constraint involves both. With higher-order constraints, each constraint becomes a vertex of its own joined to the variables in its scope (a *constraint hypergraph*).

:::

The graph of @exm-map-colouring-csp is the map's adjacency graph. Algorithms below use the graph's structure: how many neighbours a variable has, and whether the graph is a tree.

::: {#exm-n-queens-csp .example name="N-queens"}

Place $N$ queens on an $N\times N$ board so that no two attack each other. One formulation has a variable $Q_k$ for each column $k=1,\dots,N$ whose value is the row of the queen in that column, domain $\{1,\dots,N\}$, and for each pair of columns $j<k$ the constraint
$$
Q_j\ne Q_k\quad\text{and}\quad |Q_j-Q_k|\ne k-j,
$$
forbidding a shared row and a shared diagonal. One queen per column is built into the variables. For $N=4$ the solutions are $(Q_1,\dots,Q_4)=(2,4,1,3)$ and $(3,1,4,2)$.

:::

::: {#rmk-constraint-satisfaction-problems-1 .remark name="More examples and varieties"}

- *Cryptarithmetic*: in a sum such as $\mathrm{TWO}+\mathrm{TWO}=\mathrm{FOUR}$ each letter is a digit, all letters differ (one higher-order constraint, or many binary $\ne$), and auxiliary carry variables turn the column sums into constraints on three or four variables each.
- *Sudoku*: one variable per empty cell with domain $\{1,\dots,9\}$, and an all-different constraint on each row, column and $3\times3$ box.
- Domains may be finite (Boolean satisfiability is the case $|D_i|=2$), infinite (job-shop scheduling with integer start times, where constraints must be given implicitly) or continuous (linear programming, solvable in polynomial time).
- *Soft constraints* (preferences, such as "red is better than green") attach costs to assignments, turning the CSP into a constrained optimisation problem.
- Real instances: timetables, assignment of rooms and teachers, hardware configuration, transport scheduling, circuit layout. Many involve real-valued variables.

:::

Finite-domain CSPs include graph 3-colouring, which is NP-complete, so no polynomial-time algorithm is expected in general; the methods that follow are exponential in the worst case but very effective in practice.

::: {#prp-csp-search-formulation .proposition name="CSPs as search problems"}

A CSP is a search problem whose states are consistent partial assignments, starting from the empty assignment, with actions that assign a value to an unassigned variable consistently, and whose end states are the complete assignments. If at each depth only one fixed variable may be assigned, the search tree has at most $\prod_i|D_i|$ leaves, against $n!\prod_i|D_i|$ when any unassigned variable may be chosen, and both trees give the same set of solutions.

:::

::: {.proof}

1. Every solution is reached by assigning its $n$ values one at a time, each step keeping the assignment consistent, so it is an end state of the search problem; conversely an end state is a complete consistent assignment.
2. Assignments commute: the assignment reached does not depend on the order in which its values were set. So restricting depth $k$ to the $k$-th variable of a fixed order loses no solution.
3. With the order fixed, a leaf at depth $n$ is determined by one value per variable, so there are at most $\prod_i|D_i|$ of them. Without it, every complete assignment is reached once for each of the $n!$ orders of its variables.

:::

All solutions lie at depth exactly $n$, so depth-first search is the natural strategy; breadth-first search would store the whole tree above the solutions. Because the path is irrelevant, the problem also suits local search (@sec-ai-constraint-satisfaction-local-search), which works with complete assignments.
