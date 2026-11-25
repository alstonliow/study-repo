---
title: "Shortest Paths, Parenthesization and Fingering by Dynamic Programming"
sources: [mit6006-17, mit6006r-17]
requires: [cs/algorithm-design/subproblem-design, cs/graph-algorithms/all-pairs-shortest-paths]
aliases: [cs/dynamic-programming/more-dynamic-programs]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 17 and Recitation 17, in our own wording; examples our own (checked by computation); proofs written out in steps. -->

## Shortest paths as dynamic programs

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

## Parenthesization

::: {#exm-arithmetic-parenthesization .example name="Arithmetic parenthesization"}

Given an expression $a_0\ast_1a_1\ast_2\cdots\ast_{n-1}a_{n-1}$ with integers $a_i$ (possibly negative) and operations $\ast_i\in\{+,\times\}$, place parentheses to make its value as large as possible. For $2\times(-3)+1\times(-4)$ the best is $\bigl(2\times(-3)+1\bigr)\times(-4)=20$.

Maximising each part is not enough: $(-3)\times(-3)>(-2)\times(-2)$, so a large product may need two very *negative* factors. So we expand the subproblems with both goals.

1. *Subproblems:* $x(i,j,\mathrm{opt})$, the minimum ($\mathrm{opt}=\min$) or maximum ($\mathrm{opt}=\max$) value of $a_i\ast_{i+1}\cdots\ast_{j-1}a_{j-1}$ over all parenthesizations, for $0\le i<j\le n$.
2. *Relation:* guess the operation $\ast_k$ evaluated last, and the extreme of each side:
   $$x(i,j,\mathrm{opt})=\mathrm{opt}\bigl\{x(i,k,\mathrm{opt}')\ast_kx(k,j,\mathrm{opt}''):i<k<j;\ \mathrm{opt}',\mathrm{opt}''\in\{\min,\max\}\bigr\}.$$
   This is right because the left side ranges over values in $[x(i,k,\min),x(i,k,\max)]$ and the right side over $[x(k,j,\min),x(k,j,\max)]$, and $l+r$ and $l\times r$ are linear in each argument separately, so their extremes over such a rectangle are reached at its corners.
3. *Order:* increasing $j-i$. 4. *Base:* $x(i,i+1,\mathrm{opt})=a_i$.
5. *Original:* $x(0,n,\max)$; parent pointers (two per subproblem) give the parenthesization as a binary tree.
6. *Time:* $O(n^2)$ subproblems with $O(n)$ work each: $O(n^3)$.

In the example, $x(0,4,\min)=-14$, from $2\times\bigl(-3+1\times(-4)\bigr)$.

:::

```{=latex}
\begin{algorithm}
\caption{Arithmetic parenthesization}
\begin{algorithmic}
\INPUT Integers $a_0,\dots,a_{n-1}$ and operations $\ast_1,\dots,\ast_{n-1}\in\{+,\times\}$
\OUTPUT The largest value $x(0,n,\max)$
\FOR{$i=0$ to $n-1$}
    \STATE $x(i,i+1,\min)\gets a_i$; $x(i,i+1,\max)\gets a_i$
\ENDFOR
\FOR{$\ell=2$ to $n$}
    \FOR{$i=0$ to $n-\ell$}
        \STATE $j\gets i+\ell$
        \STATE $C\gets\{x(i,k,o')\ast_kx(k,j,o''):i<k<j;\ o',o''\in\{\min,\max\}\}$
        \STATE $x(i,j,\min)\gets\min C$; $x(i,j,\max)\gets\max C$
    \ENDFOR
\ENDFOR
\RETURN $x(0,n,\max)$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-more-dynamic-programs-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (1.050,1.050);
\node[lab] at (0.525,0.525) {$2,2$};
\draw[cell frame] (1.050,0.000) rectangle (2.100,1.050);
\node[lab] at (1.575,0.525) {$-6,-6$};
\draw[cell frame] (2.100,0.000) rectangle (3.150,1.050);
\node[lab] at (2.625,0.525) {$-5,-4$};
\draw[hl cell] (3.150,0.000) rectangle (4.200,1.050);
\node[lab] at (3.675,0.525) {$-14,20$};
\node[lab,tick,anchor=east] at (-0.050,0.525) {$i=0$};
\draw[cell frame] (1.050,-1.050) rectangle (2.100,0.000);
\node[lab] at (1.575,-0.525) {$-3,-3$};
\draw[cell frame] (2.100,-1.050) rectangle (3.150,0.000);
\node[lab] at (2.625,-0.525) {$-2,-2$};
\draw[cell frame] (3.150,-1.050) rectangle (4.200,0.000);
\node[lab] at (3.675,-0.525) {$-7,8$};
\node[lab,tick,anchor=east] at (-0.050,-0.525) {$i=1$};
\draw[cell frame] (2.100,-2.100) rectangle (3.150,-1.050);
\node[lab] at (2.625,-1.575) {$1,1$};
\draw[cell frame] (3.150,-2.100) rectangle (4.200,-1.050);
\node[lab] at (3.675,-1.575) {$-4,-4$};
\node[lab,tick,anchor=east] at (-0.050,-1.575) {$i=2$};
\draw[cell frame] (3.150,-3.150) rectangle (4.200,-2.100);
\node[lab] at (3.675,-2.625) {$-4,-4$};
\node[lab,tick,anchor=east] at (-0.050,-2.625) {$i=3$};
\node[lab,tick] at (0.525,1.230) {$j=1$};
\node[lab,tick] at (1.575,1.230) {$j=2$};
\node[lab,tick] at (2.625,1.230) {$j=3$};
\node[lab,tick] at (3.675,1.230) {$j=4$};
\end{tikzpicture}
\end{center}
```

The table for $2\times(-3)+1\times(-4)$: the cell $(i,j)$ holds $x(i,j,\min),x(i,j,\max)$ for $a_i\ast\cdots a_{j-1}$, filled by increasing $j-i$ from the diagonal $x(i,i+1,\cdot)=a_i$. The answer is $x(0,4,\max)=20$. It needs the *minimum* $-5$ of $2\times(-3)+1$ (cell $(0,3)$) times $-4$; the maximum of that part, $-4$, would give only $16$.

:::

## Fingering

::: {#exm-piano-fingering .example name="Piano fingering"}

A pianist plays single notes $t_0,\dots,t_{n-1}$ with the right hand, using fingers $1,\dots,F$. A given function $d(t,f,t',f')$ measures the difficulty of moving from note $t$ played with finger $f$ to note $t'$ played with finger $f'$ (a sum of penalties for awkward crossings, weak fingers and so on). Assign fingers to minimise the total difficulty.

The suffix subproblem "best difficulty for $t_i,\dots,t_{n-1}$" is not enough: the cost of the next transition depends on which finger the rest starts with. So expand with that finger.

1. *Subproblems:* $x(i,f)$, the least total difficulty for $t_i,\dots,t_{n-1}$ when $t_i$ is played with finger $f$.
2. *Relation:* guess the finger for $t_{i+1}$: $x(i,f)=\min_{1\le f'\le F}\bigl\{d(t_i,f,t_{i+1},f')+x(i+1,f')\bigr\}$.
3. *Order:* decreasing $i$. 4. *Base:* $x(n-1,f)=0$. 5. *Original:* $\min_fx(0,f)$.
6. *Time:* $nF$ subproblems with $O(F)$ work: $O(nF^2)$, independent of how many different notes there are.

For a guitar, a "finger" becomes a pair (finger, string), replacing $F$ by $FS$ for $S$ strings. If several notes sound at once, each step chooses an assignment of fingers to at most $T$ notes, at most $F^T$ choices, so $O(nF^{2T})$ time, which is linear in $n$ for fixed small $F$ and $T$.

:::

```{=latex}
\begin{algorithm}
\caption{Piano fingering}
\begin{algorithmic}
\INPUT Notes $t_0,\dots,t_{n-1}$, fingers $1,\dots,F$, difficulty function $d$
\OUTPUT The least total difficulty
\FOR{$f=1$ to $F$}
    \STATE $x(n-1,f)\gets0$
\ENDFOR
\FOR{$i=n-2$ down to $0$}
    \FOR{$f=1$ to $F$}
        \STATE $x(i,f)\gets\min_{1\le f'\le F}\{d(t_i,f,t_{i+1},f')+x(i+1,f')\}$
    \ENDFOR
\ENDFOR
\RETURN $\min_fx(0,f)$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-more-dynamic-programs-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (x01) at (0.00,0.00) {$x(0,1)$};
\node[box] (x02) at (0.00,-0.90) {$x(0,2)$};
\node[box] (x03) at (0.00,-1.80) {$x(0,3)$};
\node[lab,tick] at (0.00,0.70) {$t_0$};
\node[box] (x11) at (2.00,0.00) {$x(1,1)$};
\node[box] (x12) at (2.00,-0.90) {$x(1,2)$};
\node[box] (x13) at (2.00,-1.80) {$x(1,3)$};
\node[lab,tick] at (2.00,0.70) {$t_1$};
\node[box] (x21) at (4.00,0.00) {$x(2,1)$};
\node[box] (x22) at (4.00,-0.90) {$x(2,2)$};
\node[box] (x23) at (4.00,-1.80) {$x(2,3)$};
\node[lab,tick] at (4.00,0.70) {$t_2$};
\node[box] (x31) at (6.00,0.00) {$x(3,1)$};
\node[box] (x32) at (6.00,-0.90) {$x(3,2)$};
\node[box] (x33) at (6.00,-1.80) {$x(3,3)$};
\node[lab,tick] at (6.00,0.70) {$t_3$};
\draw[->, faint] (x01.east) -- (x11.west);
\draw[->, faint] (x01.east) -- (x12.west);
\draw[->, faint] (x01.east) -- (x13.west);
\draw[->, hl] (x02.east) -- (x11.west);
\draw[->, faint] (x02.east) -- (x12.west);
\draw[->, faint] (x02.east) -- (x13.west);
\draw[->, faint] (x03.east) -- (x11.west);
\draw[->, faint] (x03.east) -- (x12.west);
\draw[->, faint] (x03.east) -- (x13.west);
\draw[->, faint] (x11.east) -- (x21.west);
\draw[->, faint] (x11.east) -- (x22.west);
\draw[->, hl] (x11.east) -- (x23.west);
\draw[->, faint] (x12.east) -- (x21.west);
\draw[->, faint] (x12.east) -- (x22.west);
\draw[->, faint] (x12.east) -- (x23.west);
\draw[->, faint] (x13.east) -- (x21.west);
\draw[->, faint] (x13.east) -- (x22.west);
\draw[->, faint] (x13.east) -- (x23.west);
\draw[->, faint] (x21.east) -- (x31.west);
\draw[->, faint] (x21.east) -- (x32.west);
\draw[->, faint] (x21.east) -- (x33.west);
\draw[->, faint] (x22.east) -- (x31.west);
\draw[->, faint] (x22.east) -- (x32.west);
\draw[->, faint] (x22.east) -- (x33.west);
\draw[->, faint] (x23.east) -- (x31.west);
\draw[->, hl] (x23.east) -- (x32.west);
\draw[->, faint] (x23.east) -- (x33.west);
\end{tikzpicture}
\end{center}
```

The subproblem DAG of piano fingering for $n=4$ notes and $F=3$ fingers. The edge from $x(i,f)$ to $x(i+1,f')$ costs $d(t_i,f,t_{i+1},f')$, and $x(i,f)$ is the lightest path from it to the last column, where $x(n-1,f)=0$. A fingering is a path from the first column to the last (one is highlighted); the program finds a lightest one with $F^2$ edges per pair of neighbouring notes, so $O(nF^2)$ time. The note gives no particular $d$, so the edge costs are left out.

:::
