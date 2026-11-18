---
title: "Weighted Shortest Paths and DAG Relaxation"
sources: [mit6006-11, mit6006r-11]
requires: [cs/graph-algorithms/depth-first-search]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 11 and Recitation 11, in our own wording; proofs written out in steps. -->

## Weighted graphs

::: {#def-weighted-graph .definition name="Weighted graph, shortest-path weight"}

A *weighted graph* is a graph $G=(V,E)$ with a *weight function* $w:E\to\mathbb Z$. The *weight* of a walk $\pi=(v_0,\dots,v_k)$ is $w(\pi)=\sum_{i=1}^kw(v_{i-1},v_i)$. The *shortest-path weight* from $s$ to $t$ is
$$\delta(s,t)=\inf\{w(\pi):\pi\text{ a walk from }s\text{ to }t\},$$
which is $\infty$ if there is no walk. A *negative-weight cycle* is a closed walk of negative weight. A walk of weight $\delta(s,t)$ is a *shortest path*.

:::

Weights model road lengths, network latencies or costs. We assume the weight of an edge can be looked up in $O(1)$ time (stored next to the neighbour in the adjacency list, or in a hash table keyed by edges). Lengths in @sec-cs-graph-algorithms-breadth-first-search are the special case of weight $1$ on every edge, and we keep the word *distance* for $\delta$.

The infimum is needed: if a walk from $s$ to $t$ can pass through a vertex of a negative-weight cycle, going round the cycle again and again makes the weight as small as we like, and $\delta(s,t)=-\infty$. In an undirected graph a single edge of negative weight already gives a negative-weight closed walk (go back and forth), so negative weights are interesting only for directed graphs.

::: {#lem-shortest-path-properties .lemma name="Subpaths and the triangle inequality"}

1. If $\pi$ is a shortest path from $s$ to $t$ and $x,y$ lie on $\pi$ in this order, the part of $\pi$ from $x$ to $y$ is a shortest path from $x$ to $y$.
2. *Triangle inequality:* $\delta(u,v)\le\delta(u,x)+\delta(x,v)$ for all vertices $u,x,v$, and $\delta(s,v)\le\delta(s,u)+w(u,v)$ for every edge $(u,v)$ (with the usual rules for $\pm\infty$ when the right side is defined).

:::

::: {.proof}

1. If a walk from $x$ to $y$ were lighter than that part, splicing it into $\pi$ would give a walk from $s$ to $t$ lighter than $\pi$.

2. Joining a walk from $u$ to $x$ and a walk from $x$ to $v$ gives a walk from $u$ to $v$ whose weight is the sum; take infima. The second form is the case $x=u$ and the walk consisting of the edge $(u,v)$.

:::

| graph | weights | algorithm | time $O(\cdot)$ |
|---|---|---|---|
| general | unweighted | BFS | $\lvert V\rvert+\lvert E\rvert$ |
| DAG | any | DAG relaxation | $\lvert V\rvert+\lvert E\rvert$ |
| general | non-negative | Dijkstra | $\lvert V\rvert\log\lvert V\rvert+\lvert E\rvert$ |
| general | any | Bellman–Ford | $\lvert V\rvert\cdot\lvert E\rvert$ |

## Relaxation

All of these algorithms keep an *estimate* $d(v)$ of $\delta(s,v)$ for each vertex, start with $d(s)=0$ and $d(v)=\infty$ otherwise, and lower estimates when an edge breaks the triangle inequality.

::: {#def-relaxation .definition name="Relaxing an edge"}

To *relax* the edge $(u,v)$: if $d(v)>d(u)+w(u,v)$, set $d(v)=d(u)+w(u,v)$.

:::

```{=latex}
\begin{algorithm}
\caption{Relax$(u,v)$}
\begin{algorithmic}
\INPUT Edge $(u,v)$, estimates $d$
\IF{$d(v)>d(u)+w(u,v)$}
    \STATE $d(v)\gets d(u)+w(u,v)$
\ENDIF
\end{algorithmic}
\end{algorithm}
```

::: {#fig-weighted-shortest-paths-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (u) at (0.00,0.00) {$u$};
\node[small vertex] (v) at (2.00,0.00) {$v$};
\draw[->] (u) -- node[edge label, pos=0.5] {$3$} (v);
\node[lab,tick] at (0.00,0.50) {$d(u)=2$};
\node[lab,tick] at (2.00,0.50) {$d(v)=7$};
\draw[emph,->] (3.0,0) -- (4.0,0);
\node[small vertex] (u2) at (5.00,0.00) {$u$};
\node[small vertex, fill=accentLight, draw=accent] (v2) at (7.00,0.00) {$v$};
\draw[->, hl] (u2) -- node[edge label, pos=0.5] {$3$} (v2);
\node[lab,tick] at (5.00,0.50) {$d(u)=2$};
\node[lab,tick] at (7.00,0.50) {$d(v)=5$};
\end{tikzpicture}
\end{center}
```

Relaxing $(u,v)$: the estimate $d(v)=7$ breaks the triangle inequality, since $d(u)+w(u,v)=2+3=5<7$, so $d(v)$ drops to $5$. If $d(v)$ were already at most $5$, nothing would change.

:::

::: {#lem-relaxation-safe .lemma name="Relaxation is safe"}

During any sequence of relaxations, each $d(v)$ is either $\infty$ or the weight of some walk from $s$ to $v$. In particular $d(v)\ge\delta(s,v)$ at all times.

:::

::: {.proof}

Initially $d(s)=0$ is the weight of the empty walk and every other estimate is $\infty$. If before relaxing $(u,v)$ the estimate $d(u)$ is the weight of a walk from $s$ to $u$, then the new $d(v)=d(u)+w(u,v)$ is the weight of that walk followed by the edge $(u,v)$. So the property holds after every step, by induction.

:::

## DAG relaxation

::: {#def-dag-relaxation .definition name="DAG relaxation"}

*DAG relaxation* from $s$ in a DAG: set $d(s)=0$ and $d(v)=\infty$ for $v\ne s$, then process the vertices $u$ in a topological order (@thm-dfs-topological-sort), relaxing every edge $(u,v)$ out of $u$.

:::

```{=latex}
\begin{algorithm}
\caption{DAG relaxation}
\begin{algorithmic}
\INPUT Weighted DAG $G=(V,E,w)$, source $s$
\OUTPUT $d(v)=\delta(s,v)$ for every $v\in V$
\STATE $d(s)\gets0$; $d(v)\gets\infty$ for every $v\ne s$
\FOR{$u\in V$ in topological order}
    \FOR{$v\in\operatorname{Adj}(u)$}
        \STATE relax $(u,v)$
    \ENDFOR
\ENDFOR
\RETURN $d$
\end{algorithmic}
\end{algorithm}
```

::: {#thm-dag-relaxation .theorem name="DAG relaxation"}

In a weighted DAG, DAG relaxation computes $d(v)=\delta(s,v)$ for every vertex $v$, in $O(|V|+|E|)$ time.

:::

::: {.proof}

1. A DAG has no cycles, so every $\delta(s,v)$ is finite or $\infty$, never $-\infty$. We show by induction along the topological order that $d(v)=\delta(s,v)$ once all vertices before $v$ have been processed.

2. Vertices before $s$ are not reachable from $s$ (every walk goes forward), so their estimates stay $\infty=\delta$, and $d(s)=0=\delta(s,s)$ (there is no cycle through $s$).

3. Let $v$ come after $s$ with $\delta(s,v)<\infty$, and let $u$ be the vertex before $v$ on a shortest path. Then $u$ comes before $v$ in the order, so $d(u)=\delta(s,u)$ by induction when $u$ is processed, and relaxing $(u,v)$ makes $d(v)\le\delta(s,u)+w(u,v)=\delta(s,v)$ by @lem-shortest-path-properties. Also $d(v)\ge\delta(s,v)$ by @lem-relaxation-safe. Unreachable $v$ keep $d(v)=\infty$, also by @lem-relaxation-safe.

4. *Time:* the topological sort takes $O(|V|+|E|)$, and each edge is relaxed once in $O(1)$.

:::

::: {#fig-weighted-shortest-paths-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (s) at (0.00,0.00) {$s$};
\node[small vertex] (a) at (1.50,0.70) {$a$};
\node[small vertex] (b) at (3.00,0.70) {$b$};
\node[small vertex] (c) at (1.50,-0.70) {$c$};
\node[small vertex] (d) at (3.00,-0.70) {$d$};
\node[small vertex] (t) at (4.50,0.00) {$t$};
\draw[->] (s) -- node[edge label, pos=0.5] {$3$} (a);
\draw[->] (s) -- node[edge label, pos=0.5] {$1$} (c);
\draw[->] (c) -- node[edge label, pos=0.5] {$1$} (a);
\draw[->] (a) -- node[edge label, pos=0.5] {$2$} (b);
\draw[->] (c) -- node[edge label, pos=0.5] {$6$} (d);
\draw[->] (a) -- node[edge label, pos=0.5] {$-2$} (d);
\draw[->] (b) -- node[edge label, pos=0.5] {$4$} (t);
\draw[->] (d) -- node[edge label, pos=0.5] {$1$} (t);
\draw[->] (b) -- node[edge label, pos=0.5] {$1$} (d);
\node[lab,tick] at (6.00,1.30) {after};
\node[lab,tick] at (6.75,1.30) {$d(s)$};
\node[lab,tick] at (7.50,1.30) {$d(c)$};
\node[lab,tick] at (8.25,1.30) {$d(a)$};
\node[lab,tick] at (9.00,1.30) {$d(b)$};
\node[lab,tick] at (9.75,1.30) {$d(d)$};
\node[lab,tick] at (10.50,1.30) {$d(t)$};
\node[lab,tick] at (6.00,0.88) {s};
\node[lab,tick] at (6.75,0.88) {0};
\node[lab,tick] at (7.50,0.88) {1};
\node[lab,tick] at (8.25,0.88) {3};
\node[lab,tick] at (9.00,0.88) {$\infty$};
\node[lab,tick] at (9.75,0.88) {$\infty$};
\node[lab,tick] at (10.50,0.88) {$\infty$};
\node[lab,tick] at (6.00,0.46) {c};
\node[lab,tick] at (6.75,0.46) {0};
\node[lab,tick] at (7.50,0.46) {1};
\node[lab,tick] at (8.25,0.46) {2};
\node[lab,tick] at (9.00,0.46) {$\infty$};
\node[lab,tick] at (9.75,0.46) {7};
\node[lab,tick] at (10.50,0.46) {$\infty$};
\node[lab,tick] at (6.00,0.04) {a};
\node[lab,tick] at (6.75,0.04) {0};
\node[lab,tick] at (7.50,0.04) {1};
\node[lab,tick] at (8.25,0.04) {2};
\node[lab,tick] at (9.00,0.04) {4};
\node[lab,tick] at (9.75,0.04) {0};
\node[lab,tick] at (10.50,0.04) {$\infty$};
\node[lab,tick] at (6.00,-0.38) {b};
\node[lab,tick] at (6.75,-0.38) {0};
\node[lab,tick] at (7.50,-0.38) {1};
\node[lab,tick] at (8.25,-0.38) {2};
\node[lab,tick] at (9.00,-0.38) {4};
\node[lab,tick] at (9.75,-0.38) {0};
\node[lab,tick] at (10.50,-0.38) {8};
\node[lab,tick] at (6.00,-0.80) {d};
\node[lab,tick] at (6.75,-0.80) {0};
\node[lab,tick] at (7.50,-0.80) {1};
\node[lab,tick] at (8.25,-0.80) {2};
\node[lab,tick] at (9.00,-0.80) {4};
\node[lab,tick] at (9.75,-0.80) {0};
\node[lab,tick] at (10.50,-0.80) {1};
\node[lab,tick] at (6.00,-1.22) {t};
\node[lab,tick] at (6.75,-1.22) {0};
\node[lab,tick] at (7.50,-1.22) {1};
\node[lab,tick] at (8.25,-1.22) {2};
\node[lab,tick] at (9.00,-1.22) {4};
\node[lab,tick] at (9.75,-1.22) {0};
\node[lab,tick] at (10.50,-1.22) {1};
\draw[faint] (5.60,1.09) -- (10.90,1.09);
\end{tikzpicture}
\end{center}
```

DAG relaxation from $s$ in the topological order $s,c,a,b,d,t$ (weights may be negative). Each row of the table shows the estimates after relaxing the edges out of one vertex; when a vertex is processed its estimate is already final, as the proof of @thm-dag-relaxation shows.

:::

## From distances to paths

::: {#prp-parents-from-distances .proposition name="Shortest-path tree from distances"}

Suppose $\delta(s,v)$ is known and finite for the vertices reachable from $s$, and $G$ has no cycle of weight $0$. For every edge $(u,v)$ with $\delta(s,v)=\delta(s,u)+w(u,v)$, $v\ne s$, and $P(v)$ not yet set, set $P(v)=u$. This takes $O(|V|+|E|)$ time and gives parent pointers along shortest paths.

:::

::: {.proof}

1. Every reachable $v\ne s$ gets a parent: the vertex before $v$ on a shortest path satisfies the equation.

2. Along parent pointers, each edge $(P(v),v)$ satisfies $\delta(s,v)=\delta(s,P(v))+w(P(v),v)$. If the pointers from some vertex went round a cycle, adding these equations around the cycle would give it weight $0$, which is excluded. So following parents from $v$ reaches $s$, and the edges used add up to $\delta(s,v)$: a shortest path.

:::

```{=latex}
\begin{algorithm}
\caption{Parents from distances}
\begin{algorithmic}
\INPUT Weighted graph $G=(V,E,w)$, source $s$, distances $\delta(s,\cdot)$
\OUTPUT Parent pointers $P$ along shortest paths
\STATE $P(v)\gets$ none for every $v\in V$
\FOR{$(u,v)\in E$}
    \IF{$v\ne s$ and $P(v)=$ none and $\delta(s,u)<\infty$ and $\delta(s,v)=\delta(s,u)+w(u,v)$}
        \STATE $P(v)\gets u$
    \ENDIF
\ENDFOR
\RETURN $P$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-weighted-shortest-paths-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (s) at (0.00,0.00) {$s$};
\node[small vertex] (a) at (1.50,0.70) {$a$};
\node[small vertex] (b) at (3.00,0.70) {$b$};
\node[small vertex] (c) at (1.50,-0.70) {$c$};
\node[small vertex] (d) at (3.00,-0.70) {$d$};
\node[small vertex] (t) at (4.50,0.00) {$t$};
\draw[->, faint] (s) -- node[edge label, pos=0.5] {$3$} (a);
\draw[->, hl] (s) -- node[edge label, pos=0.5] {$1$} (c);
\draw[->, hl] (c) -- node[edge label, pos=0.5] {$1$} (a);
\draw[->, hl] (a) -- node[edge label, pos=0.5] {$2$} (b);
\draw[->, faint] (c) -- node[edge label, pos=0.5] {$6$} (d);
\draw[->, hl] (a) -- node[edge label, pos=0.5] {$-2$} (d);
\draw[->, faint] (b) -- node[edge label, pos=0.5] {$4$} (t);
\draw[->, hl] (d) -- node[edge label, pos=0.5] {$1$} (t);
\draw[->, faint] (b) -- node[edge label, pos=0.5] {$1$} (d);
\node[lab,tick] at (0.00,0.45) {$0$};
\node[lab,tick] at (1.50,1.15) {$2$};
\node[lab,tick] at (3.00,1.15) {$4$};
\node[lab,tick] at (1.50,-1.15) {$1$};
\node[lab,tick] at (3.00,-1.15) {$0$};
\node[lab,tick] at (4.50,0.45) {$1$};
\end{tikzpicture}
\end{center}
```

Parent pointers from the distances of @fig-weighted-shortest-paths-1 (small numbers). The highlighted edges $(u,v)$ satisfy $\delta(s,v)=\delta(s,u)+w(u,v)$, and each is kept as $P(v)=u$; they form a shortest-path tree. The edge $s\to a$ fails the test: $0+3\ne2$.

:::

With zero-weight cycles the pointers may loop, and one must break such loops; the details are a known exercise. So from now on we only compute the weights $\delta(s,v)$.
