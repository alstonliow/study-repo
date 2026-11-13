---
title: "Walks, paths and cycles"
sources: [fit1058-cn-11.8]
requires: []
status: draft
---

<!-- Migrated from 1058note notes/chapters/10-graph-theory.tex: Walks, paths and cycles. -->

::: {#def-walk-closed .definition name="Walk, closed walk"}

A *walk* from $v$ to $w$ is a sequence $v_0,e_1,v_1,e_2,\dots,e_k,v_k$ of vertices and edges with $v_0=v$, $v_k=w$, and $e_i=\{v_{i-1},v_i\}$ for each $i$. Its *length* is $k$, the number of edges. The walk is *closed* if $v_0=v_k$.

:::

::: {.remark name="Two freedoms"}

A walk may visit a vertex more than once, and may use an edge more than once, in either direction. The shortest walk has length $0$: a single vertex and no edges. In a simple graph a walk is determined by its vertices alone, so we usually write just $v_0,v_1,\dots,v_k$.

:::

```{=latex}
\begin{center}
\begin{tikzpicture}[every node/.style={circle,draw,fill=white,inner sep=1.5pt,minimum size=6mm}]
\node (a) at (0,1) {$a$};
\node (b) at (1.3,1.6) {$b$};
\node (c) at (0,-0.3) {$c$};
\node (d) at (1.3,-0.9) {$d$};
\node (e) at (2.8,0.5) {$e$};
\node (f) at (4.3,0.5) {$f$};
\draw (a)--(b) (a)--(c) (b)--(c) (b)--(d) (c)--(d) (b)--(e) (d)--(e) (e)--(f);
\end{tikzpicture}
\end{center}
```

::: {#exm-walks-paths-cycles-1 .example}

In the graph above:

- $a,b,d,e,f$ is a walk of length $4$ from $a$ to $f$;

- $a,b,d,c,b,e$ is a walk of length $5$ (it revisits $b$);

- $b,e,f,e,d$ is a walk of length $4$ (it uses $\{e,f\}$ twice);

- $a,b,c,a$ is a closed walk of length $3$, and $a,b,c,b,c,a$ is one of length $5$;

- $c$ alone is a walk of length $0$.

:::

::: {#def-trail-path-cycle .definition name="Trail, path, cycle"}

A walk is a *trail* if no edge is used more than once; a *closed trail* is a trail with $v_0=v_k$. A *path* is a trail with no repeated vertex. A *cycle* is a closed trail with no repeated vertex other than $v_0=v_k$.

:::

::: {#exm-walks-paths-cycles-2 .example}

In the graph above, $a,b,c,a$ and $a,c,b,d,e,b,a$ are closed trails (the second revisits $b$, so it is not a cycle). $a,b,d,e,f$ is a path, but not a shortest one: the shortest path from $a$ to $f$ is $a,b,e,f$, of length $3$. Shortest paths need not be unique: $a,b,d$ and $a,c,d$ are both shortest paths from $a$ to $d$.

:::

::: {.remark name="Each notion restricts the last"}

Walk $\supseteq$ trail $\supseteq$ path: a trail gives up reusing edges, and a path also gives up reusing vertices. A cycle is *not* a “closed path”, since a path of length $\ge1$ cannot be closed. In a simple graph a cycle has length at least $3$: there are no loops, and $u,v,u$ uses the edge $\{u,v\}$ twice.

:::

::: {#lem-shortest-path .lemma name="Shortest walk is a path"}

If there is a walk from $v$ to $w$, then every shortest walk from $v$ to $w$ is a path. Hence $v$ and $w$ are joined by a walk iff they are joined by a path.

:::

::: {.proof}

Let $v_0,\dots,v_k$ be a shortest walk from $v$ to $w$, and suppose, for contradiction, that $v_i=v_j$ for some $i<j$. Cutting out the part between them gives $v_0,\dots,v_i,v_{j+1},\dots,v_k$, which is still a walk from $v$ to $w$ (as $v_i=v_j\sim v_{j+1}$) but is shorter, by $j-i$. This contradicts minimality. So no vertex repeats, hence no edge repeats, and the walk is a path.

:::

::: {#def-distance .definition name="Distance"}

If $v$ and $w$ are joined by a walk, the *distance* $d(v,w)$ is the length of a shortest path between them (equivalently, of a shortest walk, by @lem-shortest-path). Otherwise $d(v,w)=\infty$.

:::

::: {#thm-odd-closed-walk .theorem name="CN Thm 60"}

A graph has a closed walk of odd length if and only if it has a cycle of odd length.

:::

::: {.proof}

($\Leftarrow$) Every cycle is a closed walk of the same length.

($\Rightarrow$) Let $W=v_0,\dots,v_k$ be a *shortest* closed walk of odd length $k$. Since there are no loops, $k\ge3$. We claim that no vertex repeats in $W$ apart from $v_0=v_k$.

Suppose, for contradiction, that $v_i=v_j$ with $0\le i<j\le k-1$. Splitting $W$ at this vertex gives two closed walks, $v_i,\dots,v_j$ of length $j-i$, and $v_j,\dots,v_{k-1},v_0,\dots,v_i$ of length $k-(j-i)$. Both lengths are between $1$ and $k-1$, and they add up to the odd number $k$, so one of them is odd. That is an odd closed walk shorter than $W$, a contradiction.

So $W$ repeats no vertex except $v_0=v_k$. Then it repeats no edge either (as $k\ge3$), so $W$ is a cycle of odd length.

:::

::: {.remark name="The “even” version fails"}

$K_2$ has the closed walk $v,w,v$ of even length $2$ but no cycle at all. The proof breaks because an even length can split as odd $+$ odd, so no shorter *even* closed walk need appear.

:::

### Counting walks with the adjacency matrix

::: {#thm-walks .theorem name="Counting walks via matrix powers (extra)"}

Let $A$ be the adjacency matrix of $G$. For every $r\ge1$, $(A^r)_{ij}$ is the number of walks of length $r$ from $v_i$ to $v_j$.

:::

::: {.proof}

We use induction on $r$.

**Base case** ($r=1$): A walk of length $1$ from $v_i$ to $v_j$ is a single edge, so there is one if $v_i\sim v_j$ and none otherwise. That count is $A_{ij}$.

**Inductive step**: Assume $(A^r)_{ik}$ counts the walks of length $r$ from $v_i$ to $v_k$, for all $i,k$. Classify the walks of length $r+1$ from $v_i$ to $v_j$ by their second-to-last vertex $v_k$. Such a walk is a walk of length $r$ from $v_i$ to $v_k$, which can be chosen in $(A^r)_{ik}$ ways by the inductive hypothesis, followed by a final step $v_k\to v_j$, which exists ($1$ way) iff $A_{kj}=1$. So there are $(A^r)_{ik}A_{kj}$ walks with second-to-last vertex $v_k$. Every walk has exactly one second-to-last vertex, so adding over $k$ gives $\sum_{k}(A^r)_{ik}A_{kj}$, which is the $(i,j)$ entry of $A^rA=A^{r+1}$.

By the Principle of Mathematical Induction, the claim holds for all $r\ge1$.

:::

::: {.remark name="Walks, not paths"}

The theorem counts walks, which may repeat vertices. It also holds for $r=0$: $A^0=I$, and the only walk of length $0$ from $v_i$ ends at $v_i$.

:::

::: {#exm-walks-paths-cycles-3 .example}

For the triangle on $\{a,b,c\}$,
$$A=\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix},\qquad
A^2=\begin{pmatrix}2&1&1\\1&2&1\\1&1&2\end{pmatrix}.$$
$(A^2)_{aa}=2$ counts the walks $a,b,a$ and $a,c,a$, and $(A^2)_{ab}=1$ counts the walk $a,c,b$.

:::
