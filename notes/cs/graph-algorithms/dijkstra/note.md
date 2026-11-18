---
title: "Dijkstra's Algorithm"
sources: [mit6006-13, mit6006r-13]
requires: [cs/graph-algorithms/weighted-shortest-paths, cs/data-structures/binary-heaps]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 13 and Recitation 13, in our own wording; proofs written out in steps. -->

When all weights are non-negative, shortest paths can be found much faster than by Bellman–Ford, by growing a "ball" around the source as BFS does.

Two observations drive the algorithm. First, with non-negative weights, distances never decrease along a shortest path: if $u$ lies on a shortest path from $s$ to $v$, then $\delta(s,u)\le\delta(s,v)$. Second, if we knew the order of the vertices by distance from $s$, every edge of a shortest path would go forward in that order, and one pass of relaxations in that order would compute all distances, as in DAG relaxation. Dijkstra's algorithm discovers this order on the fly.

::: {#def-changeable-priority-queue .definition name="Changeable priority queue"}

A *changeable priority queue* stores items with keys and distinct ids, and supports `build(X)`, `delete_min()`, and `decrease_key(id, k)` (lower the key of the item with this id to $k$). It can be built from a priority queue together with a dictionary that maps each id to the item's current position in the queue, updated whenever items move.

:::

::: {#def-dijkstra .definition name="Dijkstra's algorithm"}

*Dijkstra's algorithm* from $s$, for non-negative weights: set $d(s)=0$ and $d(v)=\infty$ for $v\ne s$, and build a changeable priority queue $Q$ holding every vertex $v$ with key $d(v)$. While $Q$ is not empty, delete a vertex $u$ with minimum $d(u)$ from $Q$ and relax every edge $(u,v)$ out of $u$, decreasing the key of $v$ in $Q$ whenever $d(v)$ drops.

:::

```{=latex}
\begin{algorithm}
\caption{Dijkstra's algorithm}
\begin{algorithmic}
\INPUT Graph $G=(V,E,w)$ with $w\ge0$, source $s$
\OUTPUT $d(v)=\delta(s,v)$ for every $v\in V$
\STATE $d(s)\gets0$; $d(v)\gets\infty$ for every $v\ne s$
\STATE $Q\gets$ changeable priority queue of $V$ keyed by $d$
\WHILE{$Q$ is not empty}
    \STATE $u\gets Q.\mathrm{delete\_min}()$
    \FOR{$v\in\operatorname{Adj}(u)$}
        \IF{$d(v)>d(u)+w(u,v)$}
            \STATE $d(v)\gets d(u)+w(u,v)$
            \STATE $Q.\mathrm{decrease\_key}(v,d(v))$
        \ENDIF
    \ENDFOR
\ENDWHILE
\RETURN $d$
\end{algorithmic}
\end{algorithm}
```

::: {#thm-dijkstra .theorem name="Dijkstra's algorithm"}

If all weights are non-negative, Dijkstra's algorithm ends with $d(v)=\delta(s,v)$ for every vertex $v$.

:::

::: {.proof}

1. Estimates only decrease, and they never drop below $\delta(s,v)$ (@lem-relaxation-safe). So it suffices to show that $d(v)=\delta(s,v)$ at the moment $v$ is removed from $Q$.

2. We use induction on the order of removal. The first vertex removed is $s$, with $d(s)=0=\delta(s,s)$ (no negative weights, so no negative cycle). Unreachable vertices keep $d=\infty=\delta$. Now let $v$ be removed, reachable from $s$, and assume the claim for all vertices removed before it. Let $\pi$ be a shortest path from $s$ to $v$.

3. Let $(x,y)$ be the first edge of $\pi$ whose head $y$ had not been removed before $v$ (possibly $y=v$); such an edge exists because $s$ has been removed and $v$ has not. When $x$ was removed, $d(x)=\delta(s,x)$ by induction, and the edge $(x,y)$ was relaxed. So, at the moment $v$ is removed,
   $$d(y)\le\delta(s,x)+w(x,y)=\delta(s,y)\le\delta(s,v)\le d(v)\le d(y).$$
   The equality holds because the part of $\pi$ up to $y$ is a shortest path (@lem-shortest-path-properties); the next inequality because the rest of $\pi$ has non-negative weight; the next by @lem-relaxation-safe; and the last because $v$ has the minimum key in $Q$ while $y$ is still in $Q$ (or $y=v$).

4. So equality holds throughout, and $d(v)=\delta(s,v)$.

:::

::: {#fig-dijkstra-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (s) at (0.00,0.00) {$s$};
\node[small vertex] (a) at (1.60,0.80) {$a$};
\node[small vertex] (b) at (3.20,0.80) {$b$};
\node[small vertex] (c) at (1.60,-0.80) {$c$};
\node[small vertex] (d) at (3.20,-0.80) {$d$};
\draw[->] (s) -- node[edge label, pos=0.5] {$7$} (a);
\draw[->] (s) -- node[edge label, pos=0.5] {$2$} (c);
\draw[->] (c) -- node[edge label, pos=0.5] {$3$} (a);
\draw[->] (a) -- node[edge label, pos=0.5] {$1$} (b);
\draw[->] (c) -- node[edge label, pos=0.5] {$8$} (d);
\draw[->] (a) -- node[edge label, pos=0.5] {$4$} (d);
\draw[->] (b) to[bend left=25] node[edge label, pos=0.5] {$1$} (d);
\draw[->] (d) to[bend left=25] node[edge label, pos=0.5] {$2$} (b);
\node[lab,tick] at (5.00,1.30) {remove};
\node[lab,tick] at (5.75,1.30) {$d(s)$};
\node[lab,tick] at (6.50,1.30) {$d(a)$};
\node[lab,tick] at (7.25,1.30) {$d(b)$};
\node[lab,tick] at (8.00,1.30) {$d(c)$};
\node[lab,tick] at (8.75,1.30) {$d(d)$};
\node[lab,tick] at (5.00,0.88) {s};
\node[lab,tick] at (5.75,0.88) {\textbf{0}};
\node[lab,tick] at (6.50,0.88) {7};
\node[lab,tick] at (7.25,0.88) {$\infty$};
\node[lab,tick] at (8.00,0.88) {2};
\node[lab,tick] at (8.75,0.88) {$\infty$};
\node[lab,tick] at (5.00,0.46) {c};
\node[lab,tick] at (5.75,0.46) {0};
\node[lab,tick] at (6.50,0.46) {5};
\node[lab,tick] at (7.25,0.46) {$\infty$};
\node[lab,tick] at (8.00,0.46) {\textbf{2}};
\node[lab,tick] at (8.75,0.46) {10};
\node[lab,tick] at (5.00,0.04) {a};
\node[lab,tick] at (5.75,0.04) {0};
\node[lab,tick] at (6.50,0.04) {\textbf{5}};
\node[lab,tick] at (7.25,0.04) {6};
\node[lab,tick] at (8.00,0.04) {2};
\node[lab,tick] at (8.75,0.04) {9};
\node[lab,tick] at (5.00,-0.38) {b};
\node[lab,tick] at (5.75,-0.38) {0};
\node[lab,tick] at (6.50,-0.38) {5};
\node[lab,tick] at (7.25,-0.38) {\textbf{6}};
\node[lab,tick] at (8.00,-0.38) {2};
\node[lab,tick] at (8.75,-0.38) {7};
\node[lab,tick] at (5.00,-0.80) {d};
\node[lab,tick] at (5.75,-0.80) {0};
\node[lab,tick] at (6.50,-0.80) {5};
\node[lab,tick] at (7.25,-0.80) {6};
\node[lab,tick] at (8.00,-0.80) {2};
\node[lab,tick] at (8.75,-0.80) {\textbf{7}};
\draw[faint] (4.60,1.09) -- (9.15,1.09);
\end{tikzpicture}
\end{center}
```

Dijkstra's algorithm from $s$. Each row removes the vertex with the smallest estimate (its value, in bold, is final from then on) and relaxes its outgoing edges. The vertices leave the queue in the order s,c,a,b,d, in increasing distance.

:::

::: {#prp-dijkstra-time .proposition name="Running time of Dijkstra"}

With a changeable priority queue on $n$ items whose `build`, `delete_min` and `decrease_key` cost $B_n$, $M_n$ and $D_n$, Dijkstra's algorithm runs in $O\bigl(B_{|V|}+|V|\,M_{|V|}+|E|\,D_{|V|}\bigr)$ time. In particular:

| priority queue | `build` | `delete_min` | `decrease_key` | Dijkstra |
|---|---|---|---|---|
| array (keys indexed by vertex) | $n$ | $n$ | $1$ | $\lvert V\rvert^2$ |
| binary heap | $n$ | $\log n$ | $\log n$ | $\lvert E\rvert\log\lvert V\rvert$ |
| Fibonacci heap | $n$ | $\log n$ (a) | $1$ (a) | $\lvert E\rvert+\lvert V\rvert\log\lvert V\rvert$ |

(after discarding vertices not reachable from $s$, so that $|V|=O(|E|+1)$).

:::

::: {.proof}

`build` is called once, `delete_min` once per vertex, and `decrease_key` at most once per relaxation, that is, at most once per edge. With an array, `delete_min` scans for the minimum in $O(|V|)$. With a binary heap (@sec-cs-data-structures-binary-heaps), `decrease_key` is a heapify up from the item's position, $O(\log n)$. Fibonacci heaps achieve the last row; we do not describe them.

:::

::: {#rmk-dijkstra-choice .remark name="Which version to use"}

For dense graphs ($|E|=\Theta(|V|^2)$) the array version, $O(|V|^2)$, is optimal; for sparse graphs ($|E|=O(|V|)$) the heap version, $O(|V|\log|V|)$, is better. In theory one quotes $O(|E|+|V|\log|V|)$. With a negative weight the algorithm can fail: take edges $s\to a$ of weight $1$, $s\to b$ of weight $2$, $b\to a$ of weight $-2$ and $a\to c$ of weight $1$. It removes $a$ (with $d(a)=1$) before $b$ and sets $d(c)=2$; when $b$ is removed later, $d(a)$ drops to $0$, but $a$ is not processed again, so $d(c)$ stays $2$ although $\delta(s,c)=1$.

:::

| graph | weights | single-source algorithm | time $O(\cdot)$ |
|---|---|---|---|
| general | unweighted | BFS | $\lvert V\rvert+\lvert E\rvert$ |
| DAG | any | DAG relaxation | $\lvert V\rvert+\lvert E\rvert$ |
| general | non-negative | Dijkstra | $\lvert V\rvert\log\lvert V\rvert+\lvert E\rvert$ |
| general | any | Bellman–Ford | $\lvert V\rvert\cdot\lvert E\rvert$ |
