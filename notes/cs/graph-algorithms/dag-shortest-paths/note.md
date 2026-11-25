---
title: "Shortest Paths in DAGs: DAG Relaxation"
sources: [mit6006-11, mit6006r-11]
requires: [cs/graph-algorithms/weighted-shortest-paths, cs/graph-algorithms/topological-sort]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 11 and Recitation 11, in our own wording; proofs written out in steps. Split from cs/graph-algorithms/weighted-shortest-paths on 2026-11-25 (one algorithm per note, SPEC §8.6). -->

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
