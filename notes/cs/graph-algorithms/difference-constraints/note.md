---
title: "Systems of Difference Constraints"
sources: [cs97si-7]
requires: [cs/graph-algorithms/bellman-ford]
status: draft
---

<!-- Added 2026-11-26 from Stanford CS 97SI (Winter 2011-12), Lecture 7, in our own wording; proofs written out in steps. The examples and figure are our own; values checked by computation. -->

Some systems of linear inequalities are shortest-path problems in disguise. Bellman–Ford (@thm-bellman-ford) then either solves them or proves them infeasible.

::: {#def-difference-constraints .definition name="System of difference constraints, constraint graph"}

A *system of difference constraints* on real variables $x_1,\dots,x_n$ is a finite set of inequalities

$$
x_j-x_i\le c_{ij}.
$$

Its *constraint graph* has vertices $0,1,\dots,n$, an edge $i\to j$ of weight $c_{ij}$ for every constraint, and an edge $0\to i$ of weight $0$ for every $i$.

:::

::: {#thm-difference-constraints .theorem name="Solving difference constraints"}

Let $\delta(v)$ be the shortest-path distance from $0$ in the constraint graph. If the graph has no negative cycle, then $x_i=\delta(i)$ is a solution of the system. If it has a negative cycle, the system has no solution. So one run of Bellman–Ford from $0$ decides the system in $O(nm)$ time for $m$ constraints.

:::

::: {.proof}

1. *Distances are finite.* Every vertex is reachable from $0$ by its edge of weight $0$, so without negative cycles every $\delta(i)$ is a real number with $\delta(i)\le0$.

2. *Solution.* For each edge $i\to j$ the triangle inequality of shortest paths gives $\delta(j)\le\delta(i)+c_{ij}$, which is exactly the constraint $x_j-x_i\le c_{ij}$ for $x=\delta$.

3. *Infeasible.* A negative cycle $v_1\to v_2\to\dots\to v_k\to v_1$ cannot pass through $0$, which has no incoming edges, so all its edges are constraints. Adding the inequalities $x_{v_{t+1}}-x_{v_t}\le c_{v_tv_{t+1}}$ around the cycle, the left sides cancel and give $0\le(\text{cycle weight})<0$, a contradiction. So no $x$ satisfies the system.

4. *Time.* The graph has $n+1$ vertices and $m+n$ edges; Bellman–Ford costs $O((n+1)(m+n))=O(nm)$ when every variable occurs in some constraint.

:::

::: {#exm-difference-constraints-1 .example name="Feasible and infeasible"}

The constraints $x_2-x_1\le3$, $x_3-x_2\le-2$, $x_3-x_1\le2$, $x_4-x_3\le1$, $x_1-x_4\le-1$, $x_4-x_2\le0$ give the distances $\delta=(-2,0,-2,-1)$ from $0$, a solution: for example $x_3-x_2=-2$ and $x_1-x_4=-1$ hold with equality. Adding $x_1-x_3\le-2$ makes $1\to2\to3\to1$ a cycle of weight $3-2-2=-1$: summing those three constraints gives $0\le-1$, so the larger system is infeasible.

:::

::: {#fig-difference-constraints-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.7cm,y=1.3cm,>=Stealth]
\node[small vertex] (0) at (0,0.75) {$0$};
\node[small vertex, fill=accentLight] (1) at (1.3,1.5) {$1$};
\node[small vertex, fill=accentLight] (2) at (2.8,1.5) {$2$};
\node[small vertex, fill=accentLight] (3) at (2.8,0) {$3$};
\node[small vertex] (4) at (1.3,0) {$4$};
\foreach \v in {1,2,3,4} \draw[->,faint] (0) -- (\v);
\draw[->,hl] (1) -- node[edge label] {$3$} (2);
\draw[->,hl] (2) -- node[edge label] {$-2$} (3);
\draw[->] (1) to[bend left=12] node[edge label,pos=0.35] {$2$} (3);
\draw[->] (3) -- node[edge label] {$1$} (4);
\draw[->] (4) -- node[edge label] {$-1$} (1);
\draw[->] (2) -- node[edge label,pos=0.7] {$0$} (4);
\draw[->,hl,dashed] (3) to[bend left=40] node[edge label,pos=0.6] {$-2$} (1);
\node[lab,tick,above left=5pt] at (1) {$\delta=-2$}; \node[lab,tick,above right=5pt] at (2) {$\delta=0$}; \node[lab,tick,below right=5pt] at (3) {$\delta=-2$}; \node[lab,tick,below left=5pt] at (4) {$\delta=-1$};
\end{tikzpicture}
\end{center}
```

The constraint graph of @exm-difference-constraints-1 (faint edges of weight $0$ from the source), labelled with the distances $\delta$. The dashed edge is the extra constraint $x_1-x_3\le-2$, which closes the negative cycle $1\to2\to3\to1$.

:::

::: {#rmk-difference-constraints-1 .remark name="Using the reduction"}

Constraints $x_j-x_i\ge c$ become $x_i-x_j\le-c$, and $x_j-x_i=c$ becomes two constraints. A solution stays a solution after adding a constant to every variable, so a problem asking for a particular value of one variable (or for $x_n-x_1$ as large as possible) is answered by the distances from that variable instead of from $0$. With integer $c_{ij}$ the solution is integral.

:::
