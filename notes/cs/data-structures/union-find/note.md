---
title: "Union-Find"
sources: [mit6046r-3]
requires: [cs/data-structures/amortized-analysis]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Recitation 3, in our own wording; proofs written out in steps. -->

::: {#def-union-find .definition name="Union-find (disjoint sets)"}

A *union-find* structure maintains a collection of pairwise disjoint sets, each with a *representative* element, under the operations

1. `make_set(x)`: add the set $\{x\}$;
2. `find(x)`: return the representative of the set containing $x$;
3. `union(x, y)`: replace the sets containing $x$ and $y$ by their union.

:::

It keeps track of connected components while edges are added, and it is the core of Kruskal's algorithm (@sec-cs-graph-algorithms-minimum-spanning-trees).

## Linked lists with union by size

Store each set as a linked list in which every element points to the head (the representative), and keep the size of each list. `find` follows one pointer, $O(1)$. `union` appends the *smaller* list to the larger one and updates the head pointers of the smaller list.

::: {#prp-union-by-size-lists .proposition name="Smaller into larger"}

With linked lists and union by size, any sequence of $m$ operations including $n$ `make_set`s takes $O(m+n\log n)$ time.

:::

::: {.proof}

1. Apart from updating head pointers, each operation costs $O(1)$.

2. When the head pointer of an element $x$ is updated, $x$ was in the smaller of the two sets, so the size of $x$'s set at least doubles. A set has at most $n$ elements, so $x$'s pointer is updated at most $\log_2n$ times.

3. Summing over the $n$ elements gives $O(n\log n)$ pointer updates in total.

:::

## Forests with union by rank and path compression

::: {#def-disjoint-set-forest .definition name="Disjoint-set forest"}

Store each set as a rooted tree whose root is the representative; each element points to its parent. Every root carries a *rank*, an upper bound on the height of its tree.

1. `find(x)` follows parent pointers to the root and then (*path compression*) makes every node on that path point directly to the root.
2. `union(x, y)` finds both roots and (*union by rank*) makes the root of smaller rank a child of the other; if the ranks are equal, either becomes the child and the new root's rank grows by $1$.

:::

::: {#fig-union-find-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.9cm,y=0.9cm]
\node[small vertex] (r) at (1,0) {$r$}; \node[small vertex] (a) at (0.4,-1) {$a$}; \node[small vertex] (e) at (1.6,-1) {$e$};
\node[small vertex] (b) at (0.4,-2) {$b$}; \node[small vertex, fill=accentLight, draw=accent] (c) at (0.4,-3) {$c$};
\draw[->] (a)--(r); \draw[->] (e)--(r); \draw[->] (b)--(a); \draw[->] (c)--(b);
\draw[emph,->] (2.6,-1.5) -- (3.8,-1.5); \node[lab,tick] at (3.2,-1.15) {\texttt{find(c)}};
\node[small vertex] (r2) at (6,0) {$r$}; \node[small vertex] (a2) at (4.8,-1) {$a$}; \node[small vertex] (b2) at (5.6,-1) {$b$};
\node[small vertex, fill=accentLight, draw=accent] (c2) at (6.4,-1) {$c$}; \node[small vertex] (e2) at (7.2,-1) {$e$};
\draw[->] (a2)--(r2); \draw[->] (b2)--(r2); \draw[->] (c2)--(r2); \draw[->] (e2)--(r2);
\end{tikzpicture}
\end{center}
```

Path compression: `find(c)` walks $c\to b\to a\to r$ and then points every node on the path straight at the root $r$, so later finds from these nodes take one step.

:::

::: {#lem-rank-size .lemma name="Rank and size"}

With union by rank (with or without path compression), a root of rank $r$ has at least $2^r$ elements in its tree. Hence every rank is at most $\log_2n$, and without path compression every tree has height at most $\log_2n$.

:::

::: {.proof}

1. By induction on the operations. A new set has rank $0$ and one element.

2. A root's rank grows only when two roots of equal rank $r$ are joined; the new tree has at least $2^r+2^r=2^{r+1}$ elements.

3. Path compression changes no rank and no tree's set of elements. Without compression, the height of a tree grows only when ranks are equal, and then by $1$ together with the rank.

:::

So union by rank alone gives $O(\log n)$ per operation. With path compression as well the amortized cost is far smaller.

::: {#thm-union-find-ackermann .theorem name="Tarjan's bound"}

With union by rank and path compression, any sequence of $m$ operations on $n$ elements takes $O(m\,\alpha(n))$ time, where $\alpha$ is the inverse Ackermann function, which is at most $4$ for any $n$ that could occur in practice.

:::

We do not prove this; the proof is a careful potential-function argument (@def-potential-method). A weaker bound, $O(m\log^*n)$ with $\log^*n$ the number of times $\log_2$ must be applied to reach $1$, has a simpler proof.
