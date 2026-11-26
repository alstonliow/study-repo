---
title: "2-Satisfiability"
sources: []
requires: [cs/graph-algorithms/strongly-connected-components]
status: draft
---

<!-- Added 2026-11-26 for the CSES problem Giant Pizza, in our own wording. TODO: add a source. -->

A boolean formula in conjunctive normal form is a *2-CNF* if every clause has at most two literals. Deciding satisfiability of such a formula is easy, in contrast with 3-CNF.

::: {#def-implication-graph .definition name="Implication graph"}

For a 2-CNF $\varphi$ on variables $x_1,\dots,x_n$, the implication graph has the $2n$ literals $x_i,\lnot x_i$ as vertices, and for each clause $(a\lor b)$ two edges $\lnot a\to b$ and $\lnot b\to a$. A one-literal clause $(a)$ is treated as $(a\lor a)$ and gives the edge $\lnot a\to a$.

:::

::: {#thm-two-sat .theorem name="2-SAT by strongly connected components"}

$\varphi$ is unsatisfiable if and only if some $x_i$ and $\lnot x_i$ lie in the same strongly connected component of the implication graph. Otherwise a satisfying assignment is obtained by setting a literal $\ell$ true when its component comes later than the component of $\lnot\ell$ in a topological order of the component graph. Everything takes $O(n+m)$ time for $m$ clauses.

:::

::: {.proof}

1. *Implications are sound.* Under any satisfying assignment, if a literal is true and $u\to v$ is an edge, then $v$ is true: the edge comes from a clause $(\lnot u\lor v)$ whose first literal is false. So truth propagates along paths, and the literals of one strongly connected component all have the same value.

2. *Necessity.* If $x_i$ and $\lnot x_i$ are in one component, they get the same value, which is impossible, so $\varphi$ is unsatisfiable.

3. *The graph is skew-symmetric.* An edge $u\to v$ exists iff $\lnot v\to\lnot u$ exists, so a path $u\leadsto v$ gives a path $\lnot v\leadsto\lnot u$, and components come in complementary pairs, with the order of the pair reversed in the topological order.

4. *Sufficiency.* Assume no variable shares a component with its negation, and set $\ell$ true iff its component is later than that of $\lnot\ell$. By step 3 exactly one of $x_i,\lnot x_i$ is true. Suppose a clause $(a\lor b)$ were false: then $\lnot a$ and $\lnot b$ are true, so $\operatorname{comp}(\lnot a)$ is later than $\operatorname{comp}(a)$ and $\operatorname{comp}(\lnot b)$ is later than $\operatorname{comp}(b)$. The edge $\lnot a\to b$ gives $\operatorname{comp}(\lnot a)\le\operatorname{comp}(b)$, and $\lnot b\to a$ gives $\operatorname{comp}(\lnot b)\le\operatorname{comp}(a)$. Chaining, $\operatorname{comp}(a)<\operatorname{comp}(\lnot a)\le\operatorname{comp}(b)<\operatorname{comp}(\lnot b)\le\operatorname{comp}(a)$, a contradiction.

5. *Time.* The graph has $2n$ vertices and $2m$ edges, and the components are found in linear time.

:::

::: {#exm-two-satisfiability-1 .example name="A small formula"}

For $\varphi=(x\lor y)\land(\lnot x\lor y)\land(\lnot y\lor z)$ the edges are $\lnot x\to y$, $\lnot y\to x$, $x\to y$, $\lnot y\to\lnot x$, $y\to z$, $\lnot z\to\lnot y$. From $\lnot y$ we reach both $x$ and $\lnot x$, but $y$ does not reach $\lnot y$, so the formula is satisfiable, with $y=z=1$ forced and $x$ free.

:::

::: {#fig-two-satisfiability-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[graph, x=1.6cm, y=1.1cm]
\node (x) at (0,1) {$x$}; \node (nx) at (0,-1) {$\bar x$};
\node (y) at (2,1) {$y$}; \node (ny) at (2,-1) {$\bar y$};
\node (z) at (4,1) {$z$}; \node (nz) at (4,-1) {$\bar z$};
\draw[->] (nx)--(y); \draw[->] (ny)--(x); \draw[->] (x)--(y); \draw[->] (ny)--(nx);
\draw[->] (y)--(z); \draw[->] (nz)--(ny);
\end{tikzpicture}
\end{center}
```

@exm-two-satisfiability-1: the implication graph; no literal shares a component with its negation.

:::
