---
title: "Arc Consistency and k-Consistency"
sources: [cs188-4, cs188-5]
requires: [ai/constraint-satisfaction/backtracking-search]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley CS188 (Fall 2025), Lecture 4 (consistency of an arc, AC-3, limitations of arc consistency) and Lecture 5 (k-consistency, strong k-consistency), in our own wording; proofs written out in steps; the 4-queens numbers were checked by running AC-3 in Python. -->

Forward checking (@def-forward-checking) compares a new value only with the unassigned neighbours of its variable. Constraints among unassigned variables also prune: if every value left for $Y$ conflicts with some value of $X$, that value of $X$ is useless. In this note all constraints are binary.

::: {#def-arc-consistency .definition name="Arc consistency"}

For variables $X,Y$ joined by a constraint, the *arc* $X\to Y$ is *consistent* if for every value $x$ in the current domain of $X$ there is a value $y$ in the domain of $Y$ such that $X=x,\ Y=y$ satisfies the constraint. *Revising* the arc deletes from the domain of $X$ every value without such a $y$. A CSP is *arc consistent* if all its arcs, in both directions, are consistent.

:::

Values are always deleted at the tail $X$ of the arc. Revising $X\to Y$ can make an arc $Z\to X$ inconsistent again, because a value of $Z$ may have relied on a deleted value of $X$; so arcs must be rechecked.

::: {#def-ac3 .definition name="AC-3"}

*AC-3* keeps a queue of arcs, initially all of them. It removes an arc $X\to Y$ and revises it; if this deleted a value, it adds every arc $Z\to X$ with $Z\ne Y$ back to the queue. It stops when the queue is empty, or reports failure as soon as a domain becomes empty.

:::

```{=latex}
\begin{algorithm}
\caption{AC-3}
\begin{algorithmic}
\INPUT Binary CSP with domains $D$
\OUTPUT Arc consistent domains, or failure
\STATE $Q\gets$ all arcs $X\to Y$
\WHILE{$Q$ is not empty}
    \STATE remove an arc $X\to Y$ from $Q$
    \STATE $R\gets\{x\in D_X : \text{no } y\in D_Y \text{ satisfies the constraint with } x\}$
    \IF{$R\ne\emptyset$}
        \STATE $D_X\gets D_X\setminus R$
        \IF{$D_X=\emptyset$}
            \RETURN failure
        \ENDIF
        \STATE add $Z\to X$ to $Q$ for every neighbour $Z\ne Y$ of $X$
    \ENDIF
\ENDWHILE
\RETURN $D$
\end{algorithmic}
\end{algorithm}
```

::: {#thm-ac3 .theorem name="Correctness and cost of AC-3"}

Let a binary CSP have $n$ variables, $e$ constraints and domains of size at most $d$.

1. AC-3 deletes only values that belong to no solution.
2. When it stops without failure, the CSP is arc consistent.
3. It runs in time $O(ed^{3})$.

:::

::: {.proof}

1. Deletions are sound. Suppose all values deleted so far belong to no solution, and revising $X\to Y$ deletes $x$. Then no remaining $y\in D_Y$ is compatible with $x$, and every value of $Y$ deleted earlier belongs to no solution. A solution with $X=x$ would give $Y$ a value compatible with $x$, which must be one of these; so there is none. By induction, all deletions are sound.
2. Invariant: every arc not in $Q$ is consistent. Initially $Q$ holds all arcs. Revising $X\to Y$ makes it consistent. Deleting values from $D_X$ can only break arcs $Z\to X$ with tail $Z\ne X$, and those with $Z\ne Y$ are put back on $Q$; the arc $Y\to X$ stays consistent, because every value $y$ that had a support $x$ still has it unless $x$ was deleted, and a deleted $x$ had no compatible $y$ at all, so it supported nothing.
3. When $Q$ is empty, by the invariant every arc is consistent.
4. Cost. There are $2e$ arcs. An arc $Z\to X$ is added back only when a value is deleted from $D_X$, which happens at most $d$ times; so each arc enters $Q$ at most $d+1$ times and there are $O(ed)$ revisions. A revision compares every pair $(x,y)\in D_X\times D_Y$, $O(d^{2})$ work, for a total of $O(ed^{3})$.

:::

Forward checking is the special case that revises only the arcs $Y\to X$ pointing to the newly assigned $X$. Maintaining arc consistency after every assignment (running AC-3 inside backtracking search, @def-backtracking-search) costs more per node but often removes far more of the tree.

::: {#exm-arc-consistency-four-queens .example name="Arc consistency on 4-queens"}

In @exm-n-queens-csp with $N=4$ and all domains $\{1,2,3,4\}$, every arc is already consistent: each row of $Q_j$ has a compatible row of $Q_k$. After assigning $Q_1=1$, AC-3 first reduces the domains to $Q_2\in\{3,4\}$, $Q_3\in\{2,4\}$, $Q_4\in\{2,3\}$ (the arcs into $Q_1$); then arcs among the other three delete more: $Q_3=4$ is compatible with neither $Q_2=3$ (diagonal) nor $Q_2=4$ (same row), leaving $Q_3\in\{2\}$, and neither $Q_4=2$ nor $Q_4=3$ is compatible with $Q_3=2$, so the domain of $Q_4$ becomes empty. So $Q_1=1$ is refuted without any search, where forward checking needed two more assignments (@exm-backtracking-four-queens). After $Q_1=2$ instead, AC-3 leaves exactly one value per variable, the solution $(2,4,1,3)$.

:::

::: {#fig-arc-consistency-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\node[lab] at (1.10,2.55) {start};
\draw[cell frame] (0.000,1.800) rectangle (0.550,2.350);
\node[lab] at (0.275,2.075) {$1$};
\draw[cell frame] (0.550,1.800) rectangle (1.100,2.350);
\node[lab] at (0.825,2.075) {$2$};
\draw[cell frame] (1.100,1.800) rectangle (1.650,2.350);
\node[lab] at (1.375,2.075) {$3$};
\draw[cell frame] (1.650,1.800) rectangle (2.200,2.350);
\node[lab] at (1.925,2.075) {$4$};
\node[lab, anchor=east] at (-0.100,2.075) {$Q_1$};
\draw[cell frame] (0.000,1.200) rectangle (0.550,1.750);
\node[lab] at (0.275,1.475) {$1$};
\draw[cell frame] (0.550,1.200) rectangle (1.100,1.750);
\node[lab] at (0.825,1.475) {$2$};
\draw[cell frame] (1.100,1.200) rectangle (1.650,1.750);
\node[lab] at (1.375,1.475) {$3$};
\draw[cell frame] (1.650,1.200) rectangle (2.200,1.750);
\node[lab] at (1.925,1.475) {$4$};
\node[lab, anchor=east] at (-0.100,1.475) {$Q_2$};
\draw[cell frame] (0.000,0.600) rectangle (0.550,1.150);
\node[lab] at (0.275,0.875) {$1$};
\draw[cell frame] (0.550,0.600) rectangle (1.100,1.150);
\node[lab] at (0.825,0.875) {$2$};
\draw[cell frame] (1.100,0.600) rectangle (1.650,1.150);
\node[lab] at (1.375,0.875) {$3$};
\draw[cell frame] (1.650,0.600) rectangle (2.200,1.150);
\node[lab] at (1.925,0.875) {$4$};
\node[lab, anchor=east] at (-0.100,0.875) {$Q_3$};
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$1$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$2$};
\draw[cell frame] (1.100,0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$3$};
\draw[cell frame] (1.650,0.000) rectangle (2.200,0.550);
\node[lab] at (1.925,0.275) {$4$};
\node[lab, anchor=east] at (-0.100,0.275) {$Q_4$};
\node[lab] at (4.50,2.55) {after $Q_1=1$};
\draw[hl cell] (3.400,1.800) rectangle (3.950,2.350);
\node[lab] at (3.675,2.075) {$1$};
\draw[cell frame] (3.950,1.800) rectangle (4.500,2.350);
\draw[cell frame] (4.500,1.800) rectangle (5.050,2.350);
\draw[cell frame] (5.050,1.800) rectangle (5.600,2.350);
\node[lab, anchor=east] at (3.300,2.075) {$Q_1$};
\draw[cell frame] (3.400,1.200) rectangle (3.950,1.750);
\draw[cell frame] (3.950,1.200) rectangle (4.500,1.750);
\draw[cell frame] (4.500,1.200) rectangle (5.050,1.750);
\node[lab] at (4.775,1.475) {$3$};
\draw[cell frame] (5.050,1.200) rectangle (5.600,1.750);
\node[lab] at (5.325,1.475) {$4$};
\node[lab, anchor=east] at (3.300,1.475) {$Q_2$};
\draw[cell frame] (3.400,0.600) rectangle (3.950,1.150);
\draw[hl cell] (3.950,0.600) rectangle (4.500,1.150);
\node[lab] at (4.225,0.875) {$2$};
\draw[cell frame] (4.500,0.600) rectangle (5.050,1.150);
\draw[cell frame] (5.050,0.600) rectangle (5.600,1.150);
\node[lab, anchor=east] at (3.300,0.875) {$Q_3$};
\draw[cell frame] (3.400,0.000) rectangle (3.950,0.550);
\draw[cell frame] (3.950,0.000) rectangle (4.500,0.550);
\draw[cell frame] (4.500,0.000) rectangle (5.050,0.550);
\draw[cell frame] (5.050,0.000) rectangle (5.600,0.550);
\node[lab, anchor=east] at (3.300,0.275) {$Q_4$};
\node[lab] at (7.90,2.55) {after $Q_1=2$};
\draw[cell frame] (6.800,1.800) rectangle (7.350,2.350);
\draw[hl cell] (7.350,1.800) rectangle (7.900,2.350);
\node[lab] at (7.625,2.075) {$2$};
\draw[cell frame] (7.900,1.800) rectangle (8.450,2.350);
\draw[cell frame] (8.450,1.800) rectangle (9.000,2.350);
\node[lab, anchor=east] at (6.700,2.075) {$Q_1$};
\draw[cell frame] (6.800,1.200) rectangle (7.350,1.750);
\draw[cell frame] (7.350,1.200) rectangle (7.900,1.750);
\draw[cell frame] (7.900,1.200) rectangle (8.450,1.750);
\draw[hl cell] (8.450,1.200) rectangle (9.000,1.750);
\node[lab] at (8.725,1.475) {$4$};
\node[lab, anchor=east] at (6.700,1.475) {$Q_2$};
\draw[hl cell] (6.800,0.600) rectangle (7.350,1.150);
\node[lab] at (7.075,0.875) {$1$};
\draw[cell frame] (7.350,0.600) rectangle (7.900,1.150);
\draw[cell frame] (7.900,0.600) rectangle (8.450,1.150);
\draw[cell frame] (8.450,0.600) rectangle (9.000,1.150);
\node[lab, anchor=east] at (6.700,0.875) {$Q_3$};
\draw[cell frame] (6.800,0.000) rectangle (7.350,0.550);
\draw[cell frame] (7.350,0.000) rectangle (7.900,0.550);
\draw[hl cell] (7.900,0.000) rectangle (8.450,0.550);
\node[lab] at (8.175,0.275) {$3$};
\draw[cell frame] (8.450,0.000) rectangle (9.000,0.550);
\node[lab, anchor=east] at (6.700,0.275) {$Q_4$};
\end{tikzpicture}
\end{center}
```

Domains on 4-queens before and after AC-3 (@exm-arc-consistency-four-queens). At the start every value is supported; after $Q_1=1$ the domain of $Q_4$ becomes empty (AC-3 stops at the first empty domain, so $Q_2$ keeps two values); after $Q_1=2$ one value per variable remains, a solution.

:::

::: {#rmk-arc-consistency-limits .remark name="What arc consistency cannot see"}

An arc consistent CSP may have no solution, or many. Three mutually adjacent regions with two colours each, $\{r,g\}$, form an arc consistent CSP (every colour of one region has a different colour in each neighbour) with no solution; the 4-queens CSP before any assignment is arc consistent with two solutions. Arc consistency only looks at pairs of variables, and the contradiction in the triangle needs all three. So it is a filter inside search, not a replacement for it.

:::

::: {#def-k-consistency .definition name="k-consistency"}

A CSP is *$k$-consistent* if for every set of $k-1$ variables, every consistent assignment to them can be extended to any $k$-th variable consistently. It is *strongly $k$-consistent* if it is $j$-consistent for every $j\le k$.

:::

1-consistency is *node consistency* (every value in each domain satisfies the unary constraints), 2-consistency is arc consistency, and 3-consistency is also called *path consistency*. Enforcing $k$-consistency takes time and space exponential in $k$, so in practice $k\le3$.

::: {#thm-strong-n-consistency .theorem name="Strong n-consistency removes backtracking"}

If a CSP with $n$ variables is strongly $n$-consistent, then assigning the variables in any order, each to any value consistent with the earlier ones, never meets a dead end; such a value exists at every step, and the result is a solution.

:::

::: {.proof}

1. Choose the first variable and a value satisfying its unary constraints; 1-consistency guarantees the domain has one (every remaining value does).
2. Suppose $k-1$ variables have consistent values, $k\le n$. By $k$-consistency this assignment extends consistently to the next variable, so a consistent value exists for it.
3. After $n$ steps all variables are assigned consistently: a solution, reached without backtracking.

:::

The theorem trades search for preprocessing, and the preprocessing costs as much as the search in the worst case. Its value lies in the middle ground: low levels of consistency plus structure, as for tree-structured CSPs (@sec-ai-constraint-satisfaction-tree-structured-csps), already rule out backtracking.
