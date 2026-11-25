---
title: "Floyd–Warshall Algorithm"
sources: [mit6006-17, mit6006r-17]
requires: [cs/algorithm-design/more-dynamic-programs, cs/graph-algorithms/all-pairs-shortest-paths, cs/graph-algorithms/bellman-ford]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 17 and Recitation 17, in our own wording; examples our own (checked by computation); proofs written out in steps. Split from cs/algorithm-design/more-dynamic-programs on 2026-11-25 (one problem per note, SPEC §8.6). -->

Shortest paths in general graphs, single-source (Bellman–Ford) and all-pairs (Floyd–Warshall), as dynamic programs. Bellman–Ford (@sec-cs-graph-algorithms-bellman-ford) and the other all-pairs algorithms (@sec-cs-graph-algorithms-all-pairs-shortest-paths) have their own notes.

Shortest paths in a graph with cycles do not form an acyclic family of subproblems: $\delta(s,v)$ may depend on $\delta(s,u)$ and the other way round. *Expanding* the subproblems with the number of edges makes them acyclic.

::: {#exm-bellman-ford-dp .example name="Bellman–Ford as a dynamic program"}

1. *Subproblems:* $\delta_k(s,v)$, the least weight of a walk from $s$ to $v$ with at most $k$ edges (@def-k-edge-distance), for $v\in V$ and $0\le k\le|V|$.
2. *Relation:* guess the last edge: $\delta_k(s,v)=\min\bigl(\{\delta_{k-1}(s,u)+w(u,v):(u,v)\in E\}\cup\{\delta_{k-1}(s,v)\}\bigr)$.
3. *Order:* increasing $k$. 4. *Base:* $\delta_0(s,s)=0$, $\delta_0(s,v)=\infty$ for $v\ne s$.
5. *Original:* $\delta(s,v)=\delta_{|V|-1}(s,v)$ unless some witness shows $-\infty$ (@lem-witnesses).
6. *Time:* $\sum_{k=0}^{|V|}\sum_vO(1+\deg^-(v))=O(|V|(|V|+|E|))$.

This is exactly Bellman–Ford (@thm-bellman-ford), computed in a different order.

:::

```{=latex}
\begin{algorithm}
\caption{Bellman–Ford as a dynamic program}
\begin{algorithmic}
\INPUT Weighted digraph $G=(V,E,w)$, source $s$
\OUTPUT $\delta_k(s,v)$ for all $v\in V$ and $0\le k\le|V|$
\STATE $\delta_0(s,s)\gets0$; $\delta_0(s,v)\gets\infty$ for every $v\ne s$
\FOR{$k=1$ to $|V|$}
    \FOR{$v\in V$}
        \STATE $\delta_k(s,v)\gets\delta_{k-1}(s,v)$
        \FOR{$u\in\operatorname{Adj}^-(v)$}
            \STATE $\delta_k(s,v)\gets\min\{\delta_k(s,v),\ \delta_{k-1}(s,u)+w(u,v)\}$
        \ENDFOR
    \ENDFOR
\ENDFOR
\RETURN all $\delta_k(s,v)$ \COMMENT{witnesses then give the vertices with $\delta(s,v)=-\infty$}
\end{algorithmic}
\end{algorithm}
```

For all pairs, the same idea costs $|V|$ times as much, $O(|V|^2|E|)$. A cleverer choice of subproblems has constant branching.

::: {#thm-floyd-warshall .theorem name="Floyd–Warshall"}

Let $G$ have vertices $1,\dots,|V|$ and no negative-weight cycle. Let $d(u,v,k)$ be the least weight of a path from $u$ to $v$ all of whose *intermediate* vertices (other than $u$ and $v$) lie in $\{1,\dots,k\}$. Then $d(u,u,0)=0$, $d(u,v,0)=w(u,v)$ if $(u,v)\in E$ and $\infty$ otherwise, and for $k\ge1$
$$d(u,v,k)=\min\bigl\{d(u,v,k-1),\ d(u,k,k-1)+d(k,v,k-1)\bigr\}.$$
Computing all $d(u,v,k)$ in order of increasing $k$ gives $\delta(u,v)=d(u,v,|V|)$ in $\Theta(|V|^3)$ time.

:::

::: {.proof}

1. Without negative-weight cycles, a lightest walk can be taken to be a path (as in @lem-simple-shortest-paths), so $\delta(u,v)=d(u,v,|V|)$, and minimising over walks or over paths with the same intermediate vertices gives the same value.

2. *Base:* with no intermediate vertex allowed, a path from $u$ to $v$ is empty ($u=v$) or a single edge.

3. *Relation.* Take a lightest path $\pi$ from $u$ to $v$ with intermediate vertices in $\{1,\dots,k\}$. If $k$ is not on $\pi$ as an intermediate vertex, its weight is $d(u,v,k-1)$. Otherwise $k$ appears once, and splits $\pi$ into a path from $u$ to $k$ and a path from $k$ to $v$, both with intermediate vertices in $\{1,\dots,k-1\}$, so its weight is at least $d(u,k,k-1)+d(k,v,k-1)$. Conversely, both options in the minimum are weights of walks with intermediate vertices in $\{1,\dots,k\}$, so they are at least $d(u,v,k)$ by step 1.

4. *Time:* $|V|^2(|V|+1)$ subproblems with $O(1)$ work each.

:::

```{=latex}
\begin{algorithm}
\caption{Floyd–Warshall}
\begin{algorithmic}
\INPUT Weighted digraph on vertices $1,\dots,n$ with no negative-weight cycle
\OUTPUT $d(u,v)=\delta(u,v)$ for all $u,v$
\FOR{$u=1$ to $n$}
    \FOR{$v=1$ to $n$}
        \STATE $d(u,v)\gets0$ if $u=v$; $w(u,v)$ if $(u,v)\in E$; $\infty$ otherwise
    \ENDFOR
\ENDFOR
\FOR{$k=1$ to $n$}
    \FOR{$u=1$ to $n$}
        \FOR{$v=1$ to $n$}
            \STATE $d(u,v)\gets\min\{d(u,v),\ d(u,k)+d(k,v)\}$
        \ENDFOR
    \ENDFOR
\ENDFOR
\RETURN $d$ \COMMENT{one table suffices: row and column $k$ do not change in round $k$}
\end{algorithmic}
\end{algorithm}
```

::: {#fig-more-dynamic-programs-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (0.500,0.500);
\node[lab] at (0.250,0.250) {$0$};
\draw[cell frame] (0.500,0.000) rectangle (1.000,0.500);
\node[lab] at (0.750,0.250) {$2$};
\draw[cell frame] (1.000,0.000) rectangle (1.500,0.500);
\node[lab] at (1.250,0.250) {$\infty$};
\draw[cell frame] (1.500,0.000) rectangle (2.000,0.500);
\node[lab] at (1.750,0.250) {$4$};
\node[lab,tick,anchor=east] at (-0.050,0.250) {a};
\draw[cell frame] (0.000,-0.500) rectangle (0.500,0.000);
\node[lab] at (0.250,-0.250) {$\infty$};
\draw[cell frame] (0.500,-0.500) rectangle (1.000,0.000);
\node[lab] at (0.750,-0.250) {$0$};
\draw[cell frame] (1.000,-0.500) rectangle (1.500,0.000);
\node[lab] at (1.250,-0.250) {$-3$};
\draw[cell frame] (1.500,-0.500) rectangle (2.000,0.000);
\node[lab] at (1.750,-0.250) {$\infty$};
\node[lab,tick,anchor=east] at (-0.050,-0.250) {b};
\draw[cell frame] (0.000,-1.000) rectangle (0.500,-0.500);
\node[lab] at (0.250,-0.750) {$2$};
\draw[cell frame] (0.500,-1.000) rectangle (1.000,-0.500);
\node[lab] at (0.750,-0.750) {$\infty$};
\draw[cell frame] (1.000,-1.000) rectangle (1.500,-0.500);
\node[lab] at (1.250,-0.750) {$0$};
\draw[cell frame] (1.500,-1.000) rectangle (2.000,-0.500);
\node[lab] at (1.750,-0.750) {$\infty$};
\node[lab,tick,anchor=east] at (-0.050,-0.750) {c};
\draw[cell frame] (0.000,-1.500) rectangle (0.500,-1.000);
\node[lab] at (0.250,-1.250) {$\infty$};
\draw[cell frame] (0.500,-1.500) rectangle (1.000,-1.000);
\node[lab] at (0.750,-1.250) {$\infty$};
\draw[cell frame] (1.000,-1.500) rectangle (1.500,-1.000);
\node[lab] at (1.250,-1.250) {$1$};
\draw[cell frame] (1.500,-1.500) rectangle (2.000,-1.000);
\node[lab] at (1.750,-1.250) {$0$};
\node[lab,tick,anchor=east] at (-0.050,-1.250) {d};
\node[lab,tick] at (0.250,0.680) {a};
\node[lab,tick] at (0.750,0.680) {b};
\node[lab,tick] at (1.250,0.680) {c};
\node[lab,tick] at (1.750,0.680) {d};
\node[lab,tick] at (1.00,1.05) {$k=0$};
\draw[cell frame] (2.750,0.000) rectangle (3.250,0.500);
\node[lab] at (3.000,0.250) {$0$};
\draw[cell frame] (3.250,0.000) rectangle (3.750,0.500);
\node[lab] at (3.500,0.250) {$2$};
\draw[cell frame] (3.750,0.000) rectangle (4.250,0.500);
\node[lab] at (4.000,0.250) {$\infty$};
\draw[cell frame] (4.250,0.000) rectangle (4.750,0.500);
\node[lab] at (4.500,0.250) {$4$};
\draw[cell frame] (2.750,-0.500) rectangle (3.250,0.000);
\node[lab] at (3.000,-0.250) {$\infty$};
\draw[cell frame] (3.250,-0.500) rectangle (3.750,0.000);
\node[lab] at (3.500,-0.250) {$0$};
\draw[cell frame] (3.750,-0.500) rectangle (4.250,0.000);
\node[lab] at (4.000,-0.250) {$-3$};
\draw[cell frame] (4.250,-0.500) rectangle (4.750,0.000);
\node[lab] at (4.500,-0.250) {$\infty$};
\draw[cell frame] (2.750,-1.000) rectangle (3.250,-0.500);
\node[lab] at (3.000,-0.750) {$2$};
\draw[hl cell] (3.250,-1.000) rectangle (3.750,-0.500);
\node[lab] at (3.500,-0.750) {$4$};
\draw[cell frame] (3.750,-1.000) rectangle (4.250,-0.500);
\node[lab] at (4.000,-0.750) {$0$};
\draw[hl cell] (4.250,-1.000) rectangle (4.750,-0.500);
\node[lab] at (4.500,-0.750) {$6$};
\draw[cell frame] (2.750,-1.500) rectangle (3.250,-1.000);
\node[lab] at (3.000,-1.250) {$\infty$};
\draw[cell frame] (3.250,-1.500) rectangle (3.750,-1.000);
\node[lab] at (3.500,-1.250) {$\infty$};
\draw[cell frame] (3.750,-1.500) rectangle (4.250,-1.000);
\node[lab] at (4.000,-1.250) {$1$};
\draw[cell frame] (4.250,-1.500) rectangle (4.750,-1.000);
\node[lab] at (4.500,-1.250) {$0$};
\node[lab,tick] at (3.000,0.680) {a};
\node[lab,tick] at (3.500,0.680) {b};
\node[lab,tick] at (4.000,0.680) {c};
\node[lab,tick] at (4.500,0.680) {d};
\node[lab,tick] at (3.75,1.05) {$k=1$ (via $a$)};
\draw[cell frame] (5.500,0.000) rectangle (6.000,0.500);
\node[lab] at (5.750,0.250) {$0$};
\draw[cell frame] (6.000,0.000) rectangle (6.500,0.500);
\node[lab] at (6.250,0.250) {$2$};
\draw[hl cell] (6.500,0.000) rectangle (7.000,0.500);
\node[lab] at (6.750,0.250) {$-1$};
\draw[cell frame] (7.000,0.000) rectangle (7.500,0.500);
\node[lab] at (7.250,0.250) {$4$};
\draw[cell frame] (5.500,-0.500) rectangle (6.000,0.000);
\node[lab] at (5.750,-0.250) {$\infty$};
\draw[cell frame] (6.000,-0.500) rectangle (6.500,0.000);
\node[lab] at (6.250,-0.250) {$0$};
\draw[cell frame] (6.500,-0.500) rectangle (7.000,0.000);
\node[lab] at (6.750,-0.250) {$-3$};
\draw[cell frame] (7.000,-0.500) rectangle (7.500,0.000);
\node[lab] at (7.250,-0.250) {$\infty$};
\draw[cell frame] (5.500,-1.000) rectangle (6.000,-0.500);
\node[lab] at (5.750,-0.750) {$2$};
\draw[cell frame] (6.000,-1.000) rectangle (6.500,-0.500);
\node[lab] at (6.250,-0.750) {$4$};
\draw[cell frame] (6.500,-1.000) rectangle (7.000,-0.500);
\node[lab] at (6.750,-0.750) {$0$};
\draw[cell frame] (7.000,-1.000) rectangle (7.500,-0.500);
\node[lab] at (7.250,-0.750) {$6$};
\draw[cell frame] (5.500,-1.500) rectangle (6.000,-1.000);
\node[lab] at (5.750,-1.250) {$\infty$};
\draw[cell frame] (6.000,-1.500) rectangle (6.500,-1.000);
\node[lab] at (6.250,-1.250) {$\infty$};
\draw[cell frame] (6.500,-1.500) rectangle (7.000,-1.000);
\node[lab] at (6.750,-1.250) {$1$};
\draw[cell frame] (7.000,-1.500) rectangle (7.500,-1.000);
\node[lab] at (7.250,-1.250) {$0$};
\node[lab,tick] at (5.750,0.680) {a};
\node[lab,tick] at (6.250,0.680) {b};
\node[lab,tick] at (6.750,0.680) {c};
\node[lab,tick] at (7.250,0.680) {d};
\node[lab,tick] at (6.50,1.05) {$k=2$ (via $b$)};
\draw[cell frame] (8.250,0.000) rectangle (8.750,0.500);
\node[lab] at (8.500,0.250) {$0$};
\draw[cell frame] (8.750,0.000) rectangle (9.250,0.500);
\node[lab] at (9.000,0.250) {$2$};
\draw[cell frame] (9.250,0.000) rectangle (9.750,0.500);
\node[lab] at (9.500,0.250) {$-1$};
\draw[cell frame] (9.750,0.000) rectangle (10.250,0.500);
\node[lab] at (10.000,0.250) {$4$};
\draw[hl cell] (8.250,-0.500) rectangle (8.750,0.000);
\node[lab] at (8.500,-0.250) {$-1$};
\draw[cell frame] (8.750,-0.500) rectangle (9.250,0.000);
\node[lab] at (9.000,-0.250) {$0$};
\draw[cell frame] (9.250,-0.500) rectangle (9.750,0.000);
\node[lab] at (9.500,-0.250) {$-3$};
\draw[hl cell] (9.750,-0.500) rectangle (10.250,0.000);
\node[lab] at (10.000,-0.250) {$3$};
\draw[cell frame] (8.250,-1.000) rectangle (8.750,-0.500);
\node[lab] at (8.500,-0.750) {$2$};
\draw[cell frame] (8.750,-1.000) rectangle (9.250,-0.500);
\node[lab] at (9.000,-0.750) {$4$};
\draw[cell frame] (9.250,-1.000) rectangle (9.750,-0.500);
\node[lab] at (9.500,-0.750) {$0$};
\draw[cell frame] (9.750,-1.000) rectangle (10.250,-0.500);
\node[lab] at (10.000,-0.750) {$6$};
\draw[hl cell] (8.250,-1.500) rectangle (8.750,-1.000);
\node[lab] at (8.500,-1.250) {$3$};
\draw[hl cell] (8.750,-1.500) rectangle (9.250,-1.000);
\node[lab] at (9.000,-1.250) {$5$};
\draw[cell frame] (9.250,-1.500) rectangle (9.750,-1.000);
\node[lab] at (9.500,-1.250) {$1$};
\draw[cell frame] (9.750,-1.500) rectangle (10.250,-1.000);
\node[lab] at (10.000,-1.250) {$0$};
\node[lab,tick] at (8.500,0.680) {a};
\node[lab,tick] at (9.000,0.680) {b};
\node[lab,tick] at (9.500,0.680) {c};
\node[lab,tick] at (10.000,0.680) {d};
\node[lab,tick] at (9.25,1.05) {$k=3$ (via $c$)};
\draw[cell frame] (11.000,0.000) rectangle (11.500,0.500);
\node[lab] at (11.250,0.250) {$0$};
\draw[cell frame] (11.500,0.000) rectangle (12.000,0.500);
\node[lab] at (11.750,0.250) {$2$};
\draw[cell frame] (12.000,0.000) rectangle (12.500,0.500);
\node[lab] at (12.250,0.250) {$-1$};
\draw[cell frame] (12.500,0.000) rectangle (13.000,0.500);
\node[lab] at (12.750,0.250) {$4$};
\draw[cell frame] (11.000,-0.500) rectangle (11.500,0.000);
\node[lab] at (11.250,-0.250) {$-1$};
\draw[cell frame] (11.500,-0.500) rectangle (12.000,0.000);
\node[lab] at (11.750,-0.250) {$0$};
\draw[cell frame] (12.000,-0.500) rectangle (12.500,0.000);
\node[lab] at (12.250,-0.250) {$-3$};
\draw[cell frame] (12.500,-0.500) rectangle (13.000,0.000);
\node[lab] at (12.750,-0.250) {$3$};
\draw[cell frame] (11.000,-1.000) rectangle (11.500,-0.500);
\node[lab] at (11.250,-0.750) {$2$};
\draw[cell frame] (11.500,-1.000) rectangle (12.000,-0.500);
\node[lab] at (11.750,-0.750) {$4$};
\draw[cell frame] (12.000,-1.000) rectangle (12.500,-0.500);
\node[lab] at (12.250,-0.750) {$0$};
\draw[cell frame] (12.500,-1.000) rectangle (13.000,-0.500);
\node[lab] at (12.750,-0.750) {$6$};
\draw[cell frame] (11.000,-1.500) rectangle (11.500,-1.000);
\node[lab] at (11.250,-1.250) {$3$};
\draw[cell frame] (11.500,-1.500) rectangle (12.000,-1.000);
\node[lab] at (11.750,-1.250) {$5$};
\draw[cell frame] (12.000,-1.500) rectangle (12.500,-1.000);
\node[lab] at (12.250,-1.250) {$1$};
\draw[cell frame] (12.500,-1.500) rectangle (13.000,-1.000);
\node[lab] at (12.750,-1.250) {$0$};
\node[lab,tick] at (11.250,0.680) {a};
\node[lab,tick] at (11.750,0.680) {b};
\node[lab,tick] at (12.250,0.680) {c};
\node[lab,tick] at (12.750,0.680) {d};
\node[lab,tick] at (12.00,1.05) {$k=4$ (via $d$)};
\end{tikzpicture}
\end{center}
```

Floyd–Warshall on the graph of @fig-all-pairs-shortest-paths-1, numbering the vertices $a,b,c,d$ as $1,2,3,4$ (row $u$, column $v$). Round $k$ allows vertex $k$ as an intermediate vertex; highlighted entries improved in that round. After round $4$ the table holds all $\delta(u,v)$, the same as the last matrix of @fig-all-pairs-shortest-paths-2.

:::

::: {#fig-more-dynamic-programs-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (u) at (0,0) {$u$};
\node[small vertex, fill=accentLight, draw=accent] (k) at (2.5,1.1) {$k$};
\node[small vertex] (v) at (5,0) {$v$};
\draw[->, emph] (u) to[bend left=10] node[edge label] {$d(u,k,k-1)$} (k);
\draw[->, emph] (k) to[bend left=10] node[edge label] {$d(k,v,k-1)$} (v);
\draw[->] (u) to[bend right=15] node[edge label] {$d(u,v,k-1)$} (v);
\node[lab,tick] at (2.5,-1.1) {intermediate vertices in $\{1,\dots,k-1\}$ on every path drawn};
\end{tikzpicture}
\end{center}
```

The Floyd–Warshall relation. A lightest path from $u$ to $v$ with intermediate vertices in $\{1,\dots,k\}$ either avoids $k$ (lower path) or passes through $k$ once, splitting into two paths that use only $\{1,\dots,k-1\}$ (upper path).

:::

This matches Johnson's algorithm (@thm-johnson) on dense graphs and is much simpler to implement. A negative entry $d(u,u,|V|)<0$ reveals a negative-weight cycle.
