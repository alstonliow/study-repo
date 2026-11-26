---
title: "Finding Eulerian Circuits"
sources: [cs97si-6]
requires: [math/discrete/graph/euler-and-hamilton, cs/graph-algorithms/depth-first-search]
status: draft
---

<!-- Added 2026-11-26 from Stanford CS 97SI (Winter 2011-12), Lecture 6 (Eulerian circuit and its constructive proof), in our own wording; proofs written out in steps. The example and figure are our own; the trace was checked by computation. -->

A connected graph has an Euler tour (a closed walk using every edge once) if and only if every vertex has even degree (@thm-euler-1736). The constructive proof becomes a linear-time algorithm: walk until stuck, then splice in further closed walks found from vertices on the way.

::: {#def-hierholzer .definition name="Hierholzer's algorithm"}

Keep a stack of vertices, starting with $s$, and mark edges as used. While the stack is non-empty, look at its top $v$: if $v$ has an unused edge $vu$, mark it used and push $u$; otherwise pop $v$ and append it to the output. The output, reversed, is the circuit.

:::

```{=latex}
\begin{algorithm}
\caption{Hierholzer's algorithm}
\begin{algorithmic}
\INPUT Connected multigraph $G$ with all degrees even, a start vertex $s$
\OUTPUT An Euler tour as a list of vertices
\STATE $S\gets(s)$; $C\gets()$
\WHILE{$S$ is not empty}
    \STATE $v\gets$ top of $S$
    \IF{$v$ has an unused edge $vu$}
        \STATE mark $vu$ used; push $u$ onto $S$
    \ELSE
        \STATE pop $v$ from $S$; append $v$ to $C$
    \ENDIF
\ENDWHILE
\RETURN $C$ reversed
\end{algorithmic}
\end{algorithm}
```

::: {#thm-hierholzer .theorem name="Hierholzer's algorithm"}

If $G$ is connected and every vertex has even degree, Hierholzer's algorithm returns an Euler tour starting and ending at $s$. With a pointer into each adjacency list that skips used edges, it runs in $O(|V|+|E|)$ time.

:::

::: {.proof}

1. *A greedy walk stops only at its start.* Let $H$ be a graph in which every vertex has even degree, and walk from $v$ along unused edges of $H$ until stuck. Each time the walk enters a vertex $x\ne v$, it has used an odd number of the edges at $x$ (one more in than out), so an unused one is left. Hence the walk stops only at $v$, and it is a closed walk.

2. *Claim.* Started with stack $(v)$ on a graph $H$ whose degrees are all even, the algorithm pops $v$ for the last time after using exactly the edges of the component of $v$ in $H$, and the vertices it output, reversed, form a closed walk from $v$ using each of those edges once. We prove this by strong induction on the number of edges of that component.

3. *First phase.* The pushes from $v$ follow a greedy walk $W=w_0w_1\cdots w_m$ with $w_0=w_m=v$ (step 1), and then $w_m$ is popped. Removing the edges of the closed walk $W$ leaves a graph $H_1$ whose degrees are still all even.

4. *Splicing.* Now $w_{m-1}$ is on top. Until $w_{m-1}$ is popped, the algorithm never looks below it, so it behaves exactly as if started with stack $(w_{m-1})$ on $H_1$: by induction it uses the component of $w_{m-1}$ in $H_1$ and outputs a closed walk $T_{m-1}$ through it, reversed. The graph that remains again has all degrees even, and the same holds in turn for $w_{m-2},\dots,w_0$.

5. *Result.* The reversed output is $w_0\,T_0\,w_1\,T_1\cdots$, the walk $W$ with a closed walk spliced in at each of its vertices, so it is a closed walk from $v$ using each consumed edge once. Every edge of $v$'s component is consumed: that component consists of $W$ and the components of $H_1$ that meet $W$, and each of those is consumed when the first of its vertices on $W$ comes to the top.

6. *Conclusion and time.* For connected $G$ with even degrees the claim gives an Euler tour from $s$. Each edge is pushed once, each push is popped once, and the adjacency pointers only move forward, so the work is $O(|V|+|E|)$.

:::

::: {#exm-eulerian-circuits-1 .example name="Two triangles sharing a vertex"}

Take edges $12,23,31,34,45,53$; vertex $3$ has degree $4$, all others degree $2$. From $s=1$ with lists in this order, the stack grows $1,2,3,1$; vertex $1$ is stuck and is output. The top is now $3$, which still has edges: the stack grows $3,4,5,3$, and then everything is output: $3,5,4,3,2,1$. Reversed, the output $1,3,5,4,3,2,1$ gives the circuit $1,2,3,4,5,3,1$.

:::

::: {#fig-eulerian-circuits-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.4cm,y=1.2cm]
\node[small vertex] (1) at (0,0) {$1$};
\node[small vertex] (2) at (0,1.6) {$2$};
\node[small vertex, fill=accentLight] (3) at (1.3,0.8) {$3$};
\node[small vertex] (4) at (2.6,1.6) {$4$};
\node[small vertex] (5) at (2.6,0) {$5$};
\draw[emph,->] (1) -- node[edge label] {$1$} (2);
\draw[emph,->] (2) -- node[edge label] {$2$} (3);
\draw[hl,->] (3) -- node[edge label] {$3$} (4);
\draw[hl,->] (4) -- node[edge label] {$4$} (5);
\draw[hl,->] (5) -- node[edge label] {$5$} (3);
\draw[emph,->] (3) -- node[edge label] {$6$} (1);
\end{tikzpicture}
\end{center}
```

The circuit of @exm-eulerian-circuits-1, edges numbered in tour order. The first walk $1,2,3,1$ missed the highlighted triangle; Hierholzer's algorithm splices it in at vertex $3$.

:::

::: {#rmk-eulerian-circuits-1 .remark name="Paths and directed graphs"}

If exactly two vertices have odd degree, start at one of them: the algorithm returns an Euler path ending at the other. In a directed graph the condition is $\deg^+(v)=\deg^-(v)$ for every $v$ (and the edges in one strongly connected component), and the same algorithm follows out-edges. Check connectivity separately, and use an explicit stack: recursion depth can reach $|E|$.

:::
