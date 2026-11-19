---
title: "Tree-Structured CSPs and Cutset Conditioning"
sources: [cs188-5]
requires: [ai/constraint-satisfaction/arc-consistency]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley CS188 (Fall 2025), Lecture 5 (problem structure, independent subproblems, tree-structured CSPs, cutset conditioning, tree decomposition), in our own wording; proofs written out in steps. -->

Search on a CSP is exponential in the number of variables in the worst case, but the shape of the constraint graph (@def-constraint-graph) can make it easy. If the graph splits into components, each is a separate CSP: a problem of $n$ variables with domain size $d$ split into pieces of $c$ variables costs $O\bigl(\tfrac nc\,d^{c}\bigr)$ instead of $O(d^{n})$, linear in $n$. Trees are the next best case.

::: {#def-tree-csp-algorithm .definition name="Tree CSP algorithm"}

Let the constraint graph of a binary CSP be a tree. Choose a root and order the variables $X_1,\dots,X_n$ so that each variable comes after its parent. The *tree CSP algorithm* then

1. (*backward pass*) for $i=n,n-1,\dots,2$, revises the arc $\text{Parent}(X_i)\to X_i$ (@def-arc-consistency), failing if a domain becomes empty;
2. (*forward pass*) for $i=1,\dots,n$, assigns $X_i$ any value in its domain consistent with the value of its parent.

:::

```{=latex}
\begin{algorithm}
\caption{Tree CSP algorithm}
\begin{algorithmic}
\INPUT Binary CSP whose constraint graph is a tree, variables ordered parents first
\OUTPUT A solution, or failure
\FOR{$i=n$ \textbf{downto} $2$}
    \STATE revise $\text{Parent}(X_i)\to X_i$; \textbf{if} $D_{\text{Parent}(X_i)}=\emptyset$ \textbf{return} failure
\ENDFOR
\STATE $X_1\gets$ any value in $D_{X_1}$
\FOR{$i=2$ \textbf{to} $n$}
    \STATE $X_i\gets$ a value in $D_{X_i}$ compatible with the value of $\text{Parent}(X_i)$
\ENDFOR
\RETURN the assignment
\end{algorithmic}
\end{algorithm}
```

::: {#thm-tree-csp .theorem name="Tree-structured CSPs take linear time"}

The tree CSP algorithm returns a solution if one exists and failure otherwise, in time $O(nd^{2})$.

:::

::: {.proof}

1. The backward pass deletes only values in no solution (as in @thm-ac3, step 1), so if it fails there is no solution.
2. Let $P=\text{Parent}(X_i)$. The arc $P\to X_i$ is revised at step $i$, which makes it consistent. Afterwards only arcs $\text{Parent}(X_j)\to X_j$ with $j<i$ are revised, and these delete values only from $\text{Parent}(X_j)$, which comes before $X_j$ and hence before $X_i$. So $D_{X_i}$ never changes again, and deleting values from $D_P$ cannot make $P\to X_i$ inconsistent. Hence after the backward pass every arc $\text{Parent}(X_i)\to X_i$ is consistent.
3. Forward pass. $D_{X_1}$ is not empty. If $X_i$'s parent has been given a value $p$ from its domain, consistency of $\text{Parent}(X_i)\to X_i$ gives a compatible value in $D_{X_i}$. So each step succeeds.
4. The result satisfies every constraint: in a tree every constraint is between a variable and its parent, and each such pair was chosen compatible. So it is a solution.
5. Cost: each of the $n-1$ revisions compares $O(d^{2})$ pairs of values, and each forward step scans at most $d$ values; total $O(nd^{2})$.

:::

The same idea, ordering the variables so that each constraint is checked once against an arc consistent domain, fails for graphs with cycles: a variable may have two earlier neighbours whose values need not share a compatible value. That is why the next two methods reduce a general graph to a tree.

::: {#exm-tree-csp .example name="A small tree CSP"}

Variables $A,B,C,D$ with constraints $A\ne B$, $A\ne C$, $C\ne D$ form a tree with root $A$, children $B,C$, and $D$ below $C$; let the domains be $D_A=\{r,g,b\}$, $D_B=\{r\}$, $D_C=\{r,g\}$, $D_D=\{g\}$. The backward pass in the order $A,B,C,D$ revises $C\to D$ (deleting $g$ from $C$, leaving $\{r\}$), then $A\to C$ (deleting $r$ from $A$), then $A\to B$ (nothing more to delete), leaving $D_A=\{g,b\}$. The forward pass assigns $A=g$, $B=r$, $C=r$, $D=g$, a solution, without any backtracking.

:::

::: {#fig-tree-structured-csps-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\node[small vertex] (A) at (1.5,0) {$A$};
\node[lab, tick, anchor=west] at (1.85,0) {$\{r,g,b\}\to\{g,b\}$};
\node[small vertex] (B) at (0,-1.2) {$B$};
\node[lab, tick, anchor=west] at (0.35,-1.2) {$\{r\}\to\{r\}$};
\node[small vertex] (C) at (3,-1.2) {$C$};
\node[lab, tick, anchor=west] at (3.35,-1.2) {$\{r,g\}\to\{r\}$};
\node[small vertex] (D) at (3,-2.4) {$D$};
\node[lab, tick, anchor=west] at (3.35,-2.4) {$\{g\}\to\{g\}$};
\draw (A) -- (B);
\draw (A) -- (C);
\draw (C) -- (D);
\end{tikzpicture}
\end{center}
```

The tree CSP of @exm-tree-csp with each domain before and after the backward pass, which revises $C\to D$, $A\to C$ and $A\to B$ in that order. The forward pass then picks $A=g$, $B=r$, $C=r$, $D=g$ without backtracking.

:::

::: {#def-cutset-conditioning .definition name="Cutset conditioning"}

A *cycle cutset* is a set $S$ of variables whose removal leaves the constraint graph a forest. *Cutset conditioning* tries every consistent assignment of the variables in $S$; for each, it removes from the domains of the other variables the values incompatible with it and solves the remaining forest-structured CSP with the tree CSP algorithm, stopping at the first solution.

:::

::: {#prp-cutset-conditioning .proposition name="Cost of cutset conditioning"}

With a cycle cutset of size $c$, cutset conditioning is complete and runs in time $O\bigl(d^{c}(n-c)d^{2}\bigr)$.

:::

::: {.proof}

1. Every solution restricts to a consistent assignment of $S$, which is tried; given it, the remaining constraints involve the other variables, unary ones (with a cutset variable) and binary ones forming a forest, and after the unary pruning the tree CSP algorithm finds a solution if one exists (@thm-tree-csp, applied to each tree of the forest).
2. There are at most $d^{c}$ assignments of $S$, and for each the pruning and tree algorithm on $n-c$ variables take $O((n-c)d^{2})$.

:::

So a CSP that is "nearly a tree" (small $c$) is easy. Finding a smallest cycle cutset is NP-hard, but cutsets found greedily are often small.

::: {#exm-cutset-conditioning .example name="Cutset for the map"}

In the map of @exm-map-colouring-csp, removing $C$ leaves the edges $AB$, $BD$, $DE$, a path; so $\{C\}$ is a cycle cutset with $c=1$. For $C=r$ the other domains lose $r$ wherever $C$ is a neighbour ($A,B,D,E$ all are), and the path $A,B,D,E$ with domains $\{g,b\}$ is solved by the tree algorithm: $A=g$, $B=b$, $D=g$, $E=b$.

:::

::: {#fig-tree-structured-csps-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\node[small vertex] (A) at (0,1) {$A$};
\node[small vertex] (B) at (0,-0.2) {$B$};
\node[small vertex, fill=accentLight, draw=accent] (C) at (1.4,0.4) {$C$};
\node[small vertex] (D) at (1.4,-1.1) {$D$};
\node[small vertex] (E) at (2.8,-0.5) {$E$};
\draw[emph] (A) -- (B);
\draw[emph] (B) -- (D);
\draw[emph] (D) -- (E);
\draw[faint, dashed] (A) -- (C);
\draw[faint, dashed] (B) -- (C);
\draw[faint, dashed] (C) -- (D);
\draw[faint, dashed] (C) -- (E);
\end{tikzpicture}
\end{center}
```

The map of @exm-map-colouring-csp with the cycle cutset $\{C\}$ highlighted. Once $C$ is assigned, its edges (dashed) only prune the neighbours' domains, and what remains, the path $A,B,D,E$, is a tree.

:::

::: {#rmk-tree-decomposition .remark name="Tree decomposition"}

Another reduction groups the variables into overlapping subsets $M_1,\dots,M_k$ so that every constraint lies inside some $M_j$ and the subsets themselves form a tree. Each subset becomes a *mega-variable* whose values are the consistent assignments of its variables, and adjacent mega-variables must agree on their shared variables. The result is a tree-structured CSP, solved in time exponential only in the size of the largest subset (the *treewidth* plus one).

:::
