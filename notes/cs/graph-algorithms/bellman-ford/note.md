---
title: "Bellman–Ford: Shortest Paths with Negative Weights"
sources: [mit6006-12, mit6006r-12]
requires: [cs/graph-algorithms/dag-shortest-paths]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 12 and Recitation 12, in our own wording; proofs written out in steps. -->

Goal: in a directed graph with arbitrary integer weights, compute $\delta(s,v)$ for every $v$, including $-\infty$ for vertices reached through a negative-weight cycle, in $O(|V|\cdot|E|)$ time.

## Bounded-length shortest paths

::: {#lem-simple-shortest-paths .lemma name="Finite shortest paths can be taken simple"}

If $\delta(s,v)$ is finite, some shortest path from $s$ to $v$ repeats no vertex, and so has at most $|V|-1$ edges.

:::

::: {.proof}

1. Since $\delta(s,v)$ is finite, no walk from $s$ to $v$ passes through a vertex of a negative-weight cycle (going round it would make the weight arbitrarily small). So every closed walk contained in a walk from $s$ to $v$ has weight $\ge0$.

2. If a walk from $s$ to $v$ repeats a vertex, it contains a closed walk $C$ between the two occurrences. Cutting $C$ out gives a walk from $s$ to $v$ with fewer edges and weight at most the original, by step 1. Repeating this turns every walk from $s$ to $v$ into a path (no repeated vertex) that is no heavier.

3. So $\delta(s,v)$, the infimum over all walks, equals the minimum over the finitely many paths from $s$ to $v$, and a lightest path attains it. A path has at most $|V|$ vertices, so at most $|V|-1$ edges.

:::

::: {#def-k-edge-distance .definition name="$k$-edge distance, witness"}

The *$k$-edge distance* $\delta_k(s,v)$ is the least weight of a walk from $s$ to $v$ with at most $k$ edges ($\infty$ if there is none). A vertex $v$ with $\delta_{|V|}(s,v)<\delta_{|V|-1}(s,v)$ is a *(negative cycle) witness*.

:::

By @lem-simple-shortest-paths, $\delta(s,v)=\delta_{|V|-1}(s,v)$ whenever $\delta(s,v)>-\infty$. A witness has a walk with $|V|$ edges lighter than every walk with fewer edges, which (as shown below) is impossible unless $\delta(s,v)=-\infty$.

::: {#lem-witnesses .lemma name="Witnesses find all $-\infty$ vertices"}

1. Every witness $v$ has $\delta(s,v)=-\infty$.
2. If $\delta(s,v)=-\infty$, then $v$ is reachable from a witness.

:::

::: {.proof}

1. If $\delta(s,v)$ were finite, then $\delta_{|V|}(s,v)\ge\delta(s,v)=\delta_{|V|-1}(s,v)$, so $v$ would not be a witness. And $\delta_{|V|}(s,v)<\infty$ means $v$ is reachable, so $\delta(s,v)\ne\infty$.

2. If $\delta(s,v)=-\infty$, some walk from $s$ to $v$ passes through a negative-weight cycle $C$ reachable from $s$. It suffices to show that $C$ contains a witness. For each $x$ on $C$, let $x'$ be its predecessor on $C$, so $\sum_{x\in C}w(x',x)=w(C)<0$. Each $x$ on $C$ is reachable, so $\delta_{|V|-1}(s,x)$ is finite (a reachable vertex has a path with at most $|V|-1$ edges).

3. A walk with at most $|V|-1$ edges to $x'$, followed by the edge $(x',x)$, has at most $|V|$ edges, so $\delta_{|V|}(s,x)\le\delta_{|V|-1}(s,x')+w(x',x)$. Summing over $x\in C$ (each vertex of $C$ appears once as $x$ and once as $x'$):
   $$\sum_{x\in C}\delta_{|V|}(s,x)\le\sum_{x\in C}\delta_{|V|-1}(s,x)+w(C)<\sum_{x\in C}\delta_{|V|-1}(s,x).$$

4. So $\delta_{|V|}(s,x)<\delta_{|V|-1}(s,x)$ for at least one $x$ on $C$: a witness.

:::

## The algorithm

::: {#def-bellman-ford .definition name="Bellman–Ford by graph duplication"}

Build a DAG $G'$ with $|V|+1$ *levels*: a copy $v_k$ of every vertex $v$ for $k=0,\dots,|V|$, and for $k=1,\dots,|V|$ the edges $(v_{k-1},v_k)$ of weight $0$ for every vertex $v$ and $(u_{k-1},v_k)$ of weight $w(u,v)$ for every edge $(u,v)\in E$. Run DAG relaxation (@def-dag-relaxation) from $s_0$. Set $d(v)=\delta'(s_0,v_{|V|-1})$; then, for every witness $u$ (a vertex with $\delta'(s_0,u_{|V|})<\delta'(s_0,u_{|V|-1})$), set $d(v)=-\infty$ for every $v$ reachable from $u$ in $G$.

:::

```{=latex}
\begin{algorithm}
\caption{Bellman–Ford by graph duplication}
\begin{algorithmic}
\INPUT Weighted digraph $G=(V,E,w)$, source $s$
\OUTPUT $d(v)=\delta(s,v)$ for every $v\in V$
\STATE build $G'$ with vertices $v_k$ ($v\in V$, $0\le k\le|V|$), edges $(v_{k-1},v_k)$ of weight $0$ and $(u_{k-1},v_k)$ of weight $w(u,v)$
\STATE run DAG relaxation on $G'$ from $s_0$, giving $\delta'$
\FOR{$v\in V$}
    \STATE $d(v)\gets\delta'(s_0,v_{|V|-1})$
\ENDFOR
\FOR{$u\in V$}
    \IF{$\delta'(s_0,u_{|V|})<\delta'(s_0,u_{|V|-1})$}
        \STATE $d(v)\gets-\infty$ for every $v$ reachable from $u$ in $G$ \COMMENT{$u$ is a witness}
    \ENDIF
\ENDFOR
\RETURN $d$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-bellman-ford-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (a0) at (0.0,0.0) {$a_0$};
\node[small vertex] (b0) at (1.8,0.0) {$b_0$};
\node[small vertex] (c0) at (3.6,0.0) {$c_0$};
\node[lab,tick] at (-0.9,0.0) {level 0};
\node[small vertex] (a1) at (0.0,-1.1) {$a_1$};
\node[small vertex] (b1) at (1.8,-1.1) {$b_1$};
\node[small vertex] (c1) at (3.6,-1.1) {$c_1$};
\node[lab,tick] at (-0.9,-1.1) {level 1};
\node[small vertex] (a2) at (0.0,-2.2) {$a_2$};
\node[small vertex] (b2) at (1.8,-2.2) {$b_2$};
\node[small vertex] (c2) at (3.6,-2.2) {$c_2$};
\node[lab,tick] at (-0.9,-2.2) {level 2};
\node[small vertex] (a3) at (0.0,-3.30) {$a_3$};
\node[small vertex] (b3) at (1.8,-3.30) {$b_3$};
\node[small vertex] (c3) at (3.6,-3.30) {$c_3$};
\node[lab,tick] at (-0.9,-3.30) {level 3};
\draw[->, faint] (a0) -- (a1);
\draw[->, faint] (b0) -- (b1);
\draw[->, faint] (c0) -- (c1);
\draw[->] (a0) -- node[edge label, pos=0.3] {$4$} (b1);
\draw[->] (a0) -- node[edge label, pos=0.3] {$2$} (c1);
\draw[->] (c0) -- node[edge label, pos=0.3] {$-1$} (b1);
\draw[->] (b0) -- node[edge label, pos=0.3] {$3$} (c1);
\draw[->, faint] (a1) -- (a2);
\draw[->, faint] (b1) -- (b2);
\draw[->, faint] (c1) -- (c2);
\draw[->] (a1) -- node[edge label, pos=0.3] {$4$} (b2);
\draw[->] (a1) -- node[edge label, pos=0.3] {$2$} (c2);
\draw[->] (c1) -- node[edge label, pos=0.3] {$-1$} (b2);
\draw[->] (b1) -- node[edge label, pos=0.3] {$3$} (c2);
\draw[->, faint] (a2) -- (a3);
\draw[->, faint] (b2) -- (b3);
\draw[->, faint] (c2) -- (c3);
\draw[->] (a2) -- node[edge label, pos=0.3] {$4$} (b3);
\draw[->] (a2) -- node[edge label, pos=0.3] {$2$} (c3);
\draw[->] (c2) -- node[edge label, pos=0.3] {$-1$} (b3);
\draw[->] (b2) -- node[edge label, pos=0.3] {$3$} (c3);
\node[lab,tick] at (5.60,0.30) {$k$};
\node[lab,tick] at (6.70,0.30) {$\delta_k(a,a)$};
\node[lab,tick] at (7.80,0.30) {$\delta_k(a,b)$};
\node[lab,tick] at (8.90,0.30) {$\delta_k(a,c)$};
\node[lab,tick] at (5.60,-0.12) {0};
\node[lab,tick] at (6.70,-0.12) {0};
\node[lab,tick] at (7.80,-0.12) {$\infty$};
\node[lab,tick] at (8.90,-0.12) {$\infty$};
\node[lab,tick] at (5.60,-0.54) {1};
\node[lab,tick] at (6.70,-0.54) {0};
\node[lab,tick] at (7.80,-0.54) {4};
\node[lab,tick] at (8.90,-0.54) {2};
\node[lab,tick] at (5.60,-0.96) {2};
\node[lab,tick] at (6.70,-0.96) {0};
\node[lab,tick] at (7.80,-0.96) {1};
\node[lab,tick] at (8.90,-0.96) {2};
\node[lab,tick] at (5.60,-1.38) {3};
\node[lab,tick] at (6.70,-1.38) {0};
\node[lab,tick] at (7.80,-1.38) {1};
\node[lab,tick] at (8.90,-1.38) {2};
\draw[faint] (5.20,0.09) -- (9.30,0.09);
\end{tikzpicture}
\end{center}
```

Graph duplication for a graph with edges $a\to b$ ($4$), $a\to c$ ($2$), $c\to b$ ($-1$), $b\to c$ ($3$). Level $k$ has a copy of every vertex; grey edges (weight $0$) mean "wait" and black edges copy the edges of $G$ one level down. Shortest paths from $a_0$ give the $k$-edge distances in the table. Here $|V|=3$ and $\delta_3=\delta_2$, so there is no witness and $\delta(a,\cdot)=\delta_2(a,\cdot)$.

:::

::: {#thm-bellman-ford .theorem name="Bellman–Ford"}

1. $\delta'(s_0,v_k)=\delta_k(s,v)$ for all $v$ and $k$.
2. Bellman–Ford computes $d(v)=\delta(s,v)$ for every vertex $v$, in $O(|V|\cdot|E|)$ time.

:::

::: {.proof}

1. Every edge of $G'$ goes up one level, so $G'$ is a DAG, and a walk from $s_0$ to $v_k$ corresponds to a walk from $s$ to $v$ in $G$ with at most $k$ edges (the weight-$0$ edges are "waiting" steps), of the same weight. Conversely, every such walk in $G$ lifts to $G'$ by waiting at $s$ first. So $\delta'(s_0,v_k)=\delta_k(s,v)$.

2. By part 1, DAG relaxation (@thm-dag-relaxation) gives $\delta_{|V|-1}$ and $\delta_{|V|}$ exactly. If $\delta(s,v)>-\infty$ then $d(v)=\delta_{|V|-1}(s,v)=\delta(s,v)$ by @lem-simple-shortest-paths, and $v$ is not reachable from a witness by @lem-witnesses part 1 (a vertex reachable from a vertex with weight $-\infty$ also has weight $-\infty$). If $\delta(s,v)=-\infty$, $v$ is reachable from a witness by @lem-witnesses part 2 and is set to $-\infty$.

3. *Time.* First discard the vertices not reachable from $s$ (their $\delta$ is $\infty$), using BFS in $O(|V|+|E|)$; what remains is connected from $s$, so $|V|=O(|E|+1)$. $G'$ has $O(|V|^2)$ vertices and $O(|V|(|V|+|E|))=O(|V|\cdot|E|)$ edges, and DAG relaxation is linear in its size. Marking everything reachable from the witnesses takes one search from an extra vertex joined to all witnesses, $O(|V|+|E|)$.

:::

::: {#rmk-bellman-ford-practice .remark name="The usual implementation"}

Only two levels of $G'$ are needed at a time, so $O(|V|)$ space suffices. The traditional form keeps one estimate per vertex and relaxes every edge of $G$ in each of $|V|-1$ rounds; a further round that still lowers some estimate reveals a negative-weight cycle. Its estimates are no longer exactly the $k$-edge distances, so its proof is less direct, but it has the same $O(|V|\cdot|E|)$ time. A shortest walk from $s_0$ to $v_{|V|}$ for a witness $v$ has $|V|+1$ vertices, so it repeats a vertex of $G$, and the repeated part is a negative-weight cycle that can be returned.

:::

```{=latex}
\begin{algorithm}
\caption{Bellman–Ford, the usual implementation}
\begin{algorithmic}
\INPUT Weighted digraph $G=(V,E,w)$, source $s$
\OUTPUT $d(v)=\delta(s,v)$, or a report of a negative-weight cycle
\STATE $d(s)\gets0$; $d(v)\gets\infty$ for every $v\ne s$
\FOR{$i=1$ to $|V|-1$}
    \FOR{$(u,v)\in E$}
        \STATE relax $(u,v)$
    \ENDFOR
\ENDFOR
\FOR{$(u,v)\in E$}
    \IF{$d(v)>d(u)+w(u,v)$}
        \RETURN "negative-weight cycle reachable from $s$"
    \ENDIF
\ENDFOR
\RETURN $d$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-bellman-ford-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (a) at (0.00,0.00) {$a$};
\node[small vertex] (b) at (1.80,0.80) {$b$};
\node[small vertex] (c) at (1.80,-0.80) {$c$};
\draw[->] (a) -- node[edge label, pos=0.5] {$4$} (b);
\draw[->] (a) -- node[edge label, pos=0.5] {$2$} (c);
\draw[->] (b) to[bend left=40] node[edge label, pos=0.5] {$3$} (c);
\draw[->] (c) to[bend left=40] node[edge label, pos=0.5] {$-1$} (b);
\node[lab,tick] at (3.60,1.00) {after};
\node[lab,tick] at (4.70,1.00) {$d(a)$};
\node[lab,tick] at (5.40,1.00) {$d(b)$};
\node[lab,tick] at (6.10,1.00) {$d(c)$};
\draw[faint] (3.1,0.8) -- (6.5,0.8);
\node[lab,tick] at (3.60,0.55) {start};
\node[lab,tick] at (4.70,0.55) {$0$};
\node[lab,tick] at (5.40,0.55) {$\infty$};
\node[lab,tick] at (6.10,0.55) {$\infty$};
\node[lab,tick] at (3.60,0.10) {round 1};
\node[lab,tick] at (4.70,0.10) {$0$};
\node[lab,tick] at (5.40,0.10) {$\mathbf{1}$};
\node[lab,tick] at (6.10,0.10) {$\mathbf{2}$};
\node[lab,tick] at (3.60,-0.35) {round 2};
\node[lab,tick] at (4.70,-0.35) {$0$};
\node[lab,tick] at (5.40,-0.35) {$1$};
\node[lab,tick] at (6.10,-0.35) {$2$};
\end{tikzpicture}
\end{center}
```

The usual Bellman–Ford on the graph of @fig-bellman-ford-1 from $a$, relaxing the edges in the order $a\to b$, $a\to c$, $b\to c$, $c\to b$ in each of the $|V|-1=2$ rounds (bold: changed). Round $1$ already reaches $d(b)=1$, a two-edge walk, so the estimates run ahead of the $k$-edge distances. Round $2$ changes nothing, and the final check finds no edge to relax, so there is no negative-weight cycle.

:::
