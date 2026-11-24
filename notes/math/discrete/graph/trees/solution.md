<!-- Draft solutions (status="draft") written by Claude. CN chapter 12 has no
     sample solutions, so these were not checked against one. Owner to review. -->

::: {.solution for="prob-graph-2-01"}
There are six trees with six vertices:

```{=latex}
\begin{tikzpicture}[scale=0.62, dotgraph]
  % 1 path
  \begin{scope}[shift={(0,0)}]
    \foreach \i in {0,...,5} \node (p\i) at (\i*0.8,0) {};
    \draw (p0)--(p1)--(p2)--(p3)--(p4)--(p5);
  \end{scope}
  % 2 star
  \begin{scope}[shift={(6,0)}]
    \node (c) at (0,0) {};
    \foreach \a in {90,162,234,306,18} \draw (c)--(\a:1) node {};
  \end{scope}
  % 3 degree 4 with one longer leg
  \begin{scope}[shift={(9.5,0)}]
    \node (c) at (0,0) {};
    \foreach \a in {90,180,270} \draw (c)--(\a:1) node {};
    \draw (c)--(1,0) node (x) {} -- (2,0) node {};
  \end{scope}
  % 4 double star (3,3)
  \begin{scope}[shift={(0,-3)}]
    \node (u) at (0,0) {}; \node (v) at (1.2,0) {};
    \draw (u)--(v);
    \draw (u)--(-0.8,0.8) node {}; \draw (u)--(-0.8,-0.8) node {};
    \draw (v)--(2,0.8) node {}; \draw (v)--(2,-0.8) node {};
  \end{scope}
  % 5 degree 3, legs 3,1,1
  \begin{scope}[shift={(4.2,-3)}]
    \node (c) at (0,0) {};
    \draw (c)--(-0.8,0.8) node {}; \draw (c)--(-0.8,-0.8) node {};
    \draw (c)--(0.8,0) node {} -- (1.6,0) node {} -- (2.4,0) node {};
  \end{scope}
  % 6 degree 3, legs 2,2,1
  \begin{scope}[shift={(9.5,-3)}]
    \node (c) at (0,0) {};
    \draw (c)--(0,0.8) node {};
    \draw (c)--(-0.8,0) node {} -- (-1.6,0) node {};
    \draw (c)--(0.8,0) node {} -- (1.6,0) node {};
  \end{scope}
\end{tikzpicture}
```

To see that the list is complete, sort by maximum degree $\Delta$:

- $\Delta = 2$: the path.
- $\Delta = 5$: the star.
- $\Delta = 4$: one vertex of degree $4$; the sixth vertex hangs off one of
  its neighbours. Only one way.
- $\Delta = 3$: if two vertices have degree $3$, the degree sum $10$ forces
  the rest to be leaves, and the two degree-3 vertices are adjacent (the
  "double star"). If only one vertex has degree $3$, the other $5$ vertices
  form three paths ("legs") hanging off it, with lengths $3,1,1$ or $2,2,1$.
:::

::: {.solution for="prob-graph-2-02"}
1. Diameter at least $3$ means there is a path $v_0v_1v_2v_3$ of length $3$.

2. $v_1$ is adjacent to $v_0$ and $v_2$, so $\deg(v_1)\ge 2$.

3. $v_1$ is not adjacent to $v_3$: otherwise $v_1v_2v_3v_1$ would be a cycle,
   which a tree does not have. And $v_1$ is not adjacent to itself.

4. So at least two of the $n$ vertices, $v_1$ and $v_3$, are not neighbours
   of $v_1$, and $\deg(v_1)\le n-2$. Take $v = v_1$.
:::

::: {.solution for="prob-graph-2-03"}
Let there be $\ell$ leaves, so $n = k + \ell$ vertices and $n-1$ edges.

1. By the Handshaking Lemma, $3k + \ell = 2(n-1) = 2(k+\ell-1)$.

2. Solving gives
   $$\ell = k + 2.$$

For example, $k = 1$ gives the star with $3$ leaves, and $k = 2$ gives two
adjacent degree-3 vertices with $4$ leaves.
:::

::: {.solution for="prob-graph-2-04"}
(a) 1. Let $T$ be a tree with $n\ge3$ vertices, so it has $n-1$ edges and
       degree sum $2(n-1)$.

    2. If every vertex had degree at most $1$, the degree sum would be at
       most $n$. But $2(n-1) > n$ when $n\ge3$.

    3. So some vertex has degree at least $2$.

(b) No. The path $P_n$ is a tree on $n$ vertices with maximum degree $2$,
    for every $n$.
:::

::: {.solution for="prob-graph-2-05"}
($\Rightarrow$) Let $G$ be a tree and $u,v$ vertices.

1. $G$ is connected, so there is a $u$–$v$ walk, and a shortest one is a path
   (Exercise 11.5).

2. Suppose there were two different $u$–$v$ paths $P$ and $Q$. Follow them
   from $u$ until they first differ, say after vertex $x$. Then follow $P$
   from $x$ until it first meets a vertex $y$ of $Q$ after $x$ (it must,
   since both end at $v$).

3. The section of $P$ from $x$ to $y$ and the section of $Q$ from $y$ back
   to $x$ share only $x$ and $y$. Together they form a cycle. A tree has no
   cycles, so the path is unique.

($\Leftarrow$) Suppose every pair of vertices is joined by a unique path.

4. Every pair is joined by a path, so $G$ is connected.

5. If $G$ had a cycle, take two vertices $x\ne y$ on it. The two arcs of the
   cycle are two different $x$–$y$ paths, which contradicts uniqueness. So
   $G$ has no cycle.

6. Connected and acyclic, so $G$ is a tree.
:::

::: {.solution for="prob-graph-2-06"}
A tree with $n$ vertices has $n-1$ edges, so its average degree is
$$\frac{2(n-1)}{n} = 2 - \frac2n < 2.$$
:::

::: {.solution for="prob-cs70-5-q2"}
<!-- TODO: solution -->
:::

::: {.solution for="prob-cs70-5-q3"}
<!-- TODO: solution -->
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-3-q2" status="draft"}
(a)

1. Removing a vertex of degree $2$ from a tree leaves exactly two components (each edge of a tree is a bridge): $L\ni u$ and $R\ni v$. Each is connected and acyclic, so a tree.

2. In $L$, only $u$ lost an edge. If $\deg_Tu=1$, then $L$ is the single vertex $u$, a binary tree of height $0$ with root $u$. If $\deg_Tu=3$, then $u$ has degree $2$ in $L$ and every other vertex of $L$ keeps degree $1$ or $3$, so $L$ is a binary tree with root $u$. The same holds for $R$.

3. In a tree the path from $r$ to a leaf $\ell\ne r$ is unique; it starts with the edge to $u$ or to $v$, and then stays in $L$ or in $R$. So its length is $1$ plus the length of the path from $u$ (or $v$) to $\ell$ in $L$ (or $R$). The leaves of $T$ are exactly the leaves of $L$ and of $R$ (a root of height $0$ is a leaf of degree $1$ in $T$). Taking the maximum, $h(T)=1+\max(h(L),h(R))$.

(b) Strong induction on $h$. For $h=0$ there is $1=2^1-1$ vertex. For $h>0$, by (a), $T$ is the root plus $L$ and $R$ of heights at most $h-1$, so it has at most $1+2(2^h-1)=2^{h+1}-1$ vertices.

(c) Strong induction on $n$. A binary tree with one leaf is the single vertex (a tree of height $>0$ has at least two leaves, one in each of $L$, $R$), with $1=2\cdot1-1$ vertices. If $n>1$, the root is not a leaf, so by (a) the $n$ leaves split as $a$ in $L$ and $b$ in $R$ with $a+b=n$, $a,b\ge1$. By the hypothesis $T$ has $1+(2a-1)+(2b-1)=2n-1$ vertices.
:::

::: {.solution for="prob-mit6042f10-5-q1" status="draft"}
(a) Let $r$ be the root, with neighbours $u$ and $v$, and let $L$ be the component containing $u$. $L$ is a tree (a connected subgraph of a tree has no cycles). Only $u$ lost an edge. If $u$ had degree $1$, then $L=\{u\}$, a lone vertex, which is an SBTree. If $u$ had degree $3$, it now has degree $2$ and is the only vertex of $L$ of degree $2$; all other vertices of $L$ keep degree $3$ or $1$. So $L$ is an SBTree with root $u$, and the same holds for the component of $v$.

(b) Claim: an SBTree with $l$ leaves has $2l-1$ vertices. Strong induction on $l$.

1. An SBTree with more than one vertex has at least two leaves: by (a) it splits into two SBTrees, each with at least one leaf, and these are leaves of the whole tree (the root, of degree $2$, is not a leaf). So $l=1$ means the lone vertex: $1=2\cdot1-1$.

2. If $l\ge2$, removing the root gives SBTrees with $l_1,l_2\ge1$ leaves, $l_1+l_2=l$. By the hypothesis they have $2l_1-1$ and $2l_2-1$ vertices, so the tree has $1+(2l_1-1)+(2l_2-1)=2l-1$.

This is the same result as @prob-cs70hw-3-q2 (c), for the same kind of tree.
:::

::: {.solution for="prob-mit6006s20-0-q5" status="draft"}
Induction on $n=|V|\ge1$.

1. *Base case* $n=1$: there are no edges, so no cycle.

2. *Inductive step.* Let $G$ be connected with $n+1\ge2$ vertices and $n$ edges, and assume the claim for $n$ vertices. The degrees sum to $2n<2(n+1)$ (@thm-handshake), so some vertex $v$ has degree at most $1$; since $G$ is connected with at least two vertices, $\deg v=1$.

3. Removing $v$ and its edge leaves a graph $G'$ with $n$ vertices and $n-1$ edges. $G'$ is connected: a path between two vertices of $G'$ in $G$ cannot pass through $v$, which has only one neighbour. By the hypothesis $G'$ is acyclic.

4. A cycle of $G$ cannot use $v$ (a vertex on a cycle has degree at least $2$), so it would be a cycle of $G'$. Hence $G$ is acyclic.
:::
