---
title: "Graph Search: Breadth-First Search"
sources: [mit6006-9, mit6006r-9]
requires: [math/discrete/graph/directed-graphs, math/discrete/graph/representing-graphs, cs/data-structures/hashing]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 9 and Recitation 9, in our own wording; proofs written out in steps. 6.006 says "path" for what these notes call a walk, and "simple path" for a path. -->

## Graphs as data

Graphs model road and computer networks, social networks, and the state spaces of puzzles and games (a vertex per position, an edge per move). We use the definitions of @def-graph and @def-digraph and assume graphs are *simple*: no loops and no repeated edges. Then $|E|=O(|V|^2)$. For a vertex $u$ we write
$$\operatorname{Adj}^+(u)=\{v:(u,v)\in E\},\qquad\operatorname{Adj}^-(u)=\{v:(v,u)\in E\},$$
the out- and in-neighbours, with $\deg^\pm(u)=|\operatorname{Adj}^\pm(u)|$; without a sign we mean $\operatorname{Adj}^+$ and $\deg^+$. In an undirected graph both are the set of neighbours.

::: {#def-graph-representation .definition name="Adjacency-list representation"}

An *adjacency-list representation* of $G=(V,E)$ is a set data structure that maps each vertex $u$ to a sequence holding $\operatorname{Adj}(u)$ (@def-adjacency-list). The map is usually a direct access array (when $V=\{0,\dots,|V|-1\}$) or a hash table, and each $\operatorname{Adj}(u)$ an array or linked list. It uses $\Theta\bigl(|V|+\sum_u\deg(u)\bigr)=\Theta(|V|+|E|)$ space, by the handshaking lemma (@thm-handshake) or its directed version (@prp-digraph-degree-sum).

:::

Accordingly, a graph algorithm is *linear time* if it runs in $O(|V|+|E|)$ time. Storing each $\operatorname{Adj}(u)$ in a hash table instead also allows testing whether $(u,v)\in E$ in $O(1)$ expected time.

## Path problems

The *length* of a walk is its number of edges, and the *distance* $\delta(u,v)$ is the length of a shortest walk from $u$ to $v$, or $\infty$ if there is none (@def-distance; a shortest walk is a path by @lem-shortest-path, which holds for digraphs with the same proof). Natural problems, each at least as hard as the one before:

1. *single-pair reachability* $(G,s,t)$: is there a walk from $s$ to $t$?
2. *single-pair shortest path* $(G,s,t)$: return $\delta(s,t)$ and a shortest path from $s$ to $t$;
3. *single-source shortest paths* $(G,s)$: return $\delta(s,v)$ for every $v$ and a shortest-path tree.

::: {#def-shortest-path-tree .definition name="Parent pointers, shortest-path tree"}

For a source $s$, a *parent* function $P$ assigns to each vertex $v\ne s$ reachable from $s$ a vertex $P(v)$ with $(P(v),v)\in E$ and $\delta(s,P(v))=\delta(s,v)-1$; let $P(s)$ be empty. Following parents from $v$ gives a shortest path back to $s$, in reverse. The parent edges form a *shortest-path tree* of size $O(|V|)$, which describes a shortest path to every vertex even though the paths together may have total length $\Theta(|V|^2)$.

:::

## Breadth-first search

::: {#def-bfs .definition name="Breadth-first search"}

*Breadth-first search* (BFS) from $s$ computes *level sets* $L_0,L_1,\dots$: let $L_0=\{s\}$, $d(s)=0$, $P(s)$ empty. For $i=1,2,\dots$, for every $u\in L_{i-1}$ and every $v\in\operatorname{Adj}(u)$ that has not been reached yet, add $v$ to $L_i$ and set $d(v)=i$, $P(v)=u$. Stop when a level is empty, and set $d(v)=\infty$ for every vertex not reached.

:::

::: {#thm-bfs .theorem name="Breadth-first search"}

BFS computes $d(v)=\delta(s,v)$ for every vertex $v$ and a parent function $P$ as in @def-shortest-path-tree. It runs in $O(|V|+|E|)$ time.

:::

::: {.proof}

1. *Claim:* $L_i=\{v:\delta(s,v)=i\}$ for every $i$. By strong induction on $i$; $L_0=\{s\}$ is right. Assume the claim for all levels below $i$.

2. If $\delta(s,v)=i\ge1$, take a shortest walk from $s$ to $v$ and let $u$ be its second-to-last vertex. Its first part is a walk of length $i-1$ to $u$, and no shorter walk to $u$ exists (it would give a shorter walk to $v$), so $\delta(s,u)=i-1$ and $u\in L_{i-1}$ by induction. Since $\delta(s,v)=i$, $v$ is in no earlier level, so it is still unreached when $u$ is scanned, and it is added to $L_i$ (if not already added from another vertex of $L_{i-1}$).

3. Conversely, if $v$ is added to $L_i$ from $u\in L_{i-1}$, there is a walk of length $(i-1)+1=i$ to $v$, so $\delta(s,v)\le i$; and $v$ was in no earlier level, which by induction means $\delta(s,v)\ne j$ for all $j<i$. So $\delta(s,v)=i$, and $P(v)=u$ satisfies $\delta(s,u)=i-1$.

4. Vertices never reached have no walk from $s$ (by the claim, a vertex at finite distance is in some level), so $d(v)=\infty$ is right.

5. *Time.* Store each level in a dynamic array and $d$, $P$ in a direct access array or hash table, so that "reached yet?" takes $O(1)$ time. Each vertex enters at most one level and is scanned once, with $O(1)$ work per out-neighbour, so the scans cost $O\bigl(|V|+\sum_u\deg(u)\bigr)=O(|V|+|E|)$. Setting $d(v)=\infty$ for unreached vertices costs $O(|V|)$.

:::

::: {#fig-breadth-first-search-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-0.55,-1.5) rectangle (0.55,1.5);
\node[lab,tick] at (0.00,1.75) {$L_0$};
\draw[faint] (1.05,-1.5) rectangle (2.15,1.5);
\node[lab,tick] at (1.60,1.75) {$L_1$};
\draw[faint] (2.65,-1.5) rectangle (3.75,1.5);
\node[lab,tick] at (3.20,1.75) {$L_2$};
\draw[faint] (4.25,-1.5) rectangle (5.35,1.5);
\node[lab,tick] at (4.80,1.75) {$L_3$};
\node[small vertex] (s) at (0.00,0.00) {$s$};
\node[small vertex] (a) at (1.60,0.80) {$a$};
\node[small vertex] (b) at (1.60,-0.80) {$b$};
\node[small vertex] (c) at (3.20,0.80) {$c$};
\node[small vertex] (d) at (3.20,-0.80) {$d$};
\node[small vertex] (e) at (4.80,0.80) {$e$};
\node[small vertex] (f) at (4.80,-0.80) {$f$};
\draw[emph] (s) -- (a);
\draw[emph] (s) -- (b);
\draw[faint] (a) -- (b);
\draw[emph] (a) -- (c);
\draw[faint] (b) -- (c);
\draw[emph] (b) -- (d);
\draw[emph] (c) -- (e);
\draw[faint] (d) -- (e);
\draw[emph] (d) -- (f);
\draw[faint] (e) -- (f);
\end{tikzpicture}
\end{center}
```

Breadth-first search from $s$ (neighbours taken in alphabetical order). Each box is a level set $L_i=\{v:\delta(s,v)=i\}$; bold edges are the parent edges $P(v)\to v$, which form a shortest-path tree. Every other edge joins the same or neighbouring levels.

:::

::: {#rmk-breadth-first-search-queue .remark name="BFS with a queue"}

BFS is usually written with one queue instead of separate levels: start with $s$ in the queue, and repeatedly remove the first vertex $u$ and append each unreached $v\in\operatorname{Adj}(u)$, setting $d(v)=d(u)+1$ and $P(v)=u$. The queue always holds the rest of one level followed by the start of the next, so vertices leave it in the order $L_0,L_1,\dots$, and the algorithm is the same.

:::
