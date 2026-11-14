<!-- Draft solutions (status="draft") written by Claude. CN chapter 12 has no
     sample solutions, so these were not checked against one. Owner to review. -->

::: {.solution for="prob-graph-2-01" status="draft"}
There are six trees with six vertices:

```{=latex}
\begin{tikzpicture}[scale=0.62, every node/.style={circle, fill, inner sep=1.6pt}]
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

::: {.solution for="prob-graph-2-02" status="draft"}
1. Diameter at least $3$ means there is a path $v_0v_1v_2v_3$ of length $3$.

2. $v_1$ is adjacent to $v_0$ and $v_2$, so $\deg(v_1)\ge 2$.

3. $v_1$ is not adjacent to $v_3$: otherwise $v_1v_2v_3v_1$ would be a cycle,
   which a tree does not have. And $v_1$ is not adjacent to itself.

4. So at least two of the $n$ vertices, $v_1$ and $v_3$, are not neighbours
   of $v_1$, and $\deg(v_1)\le n-2$. Take $v = v_1$.
:::

::: {.solution for="prob-graph-2-03" status="draft"}
Let there be $\ell$ leaves, so $n = k + \ell$ vertices and $n-1$ edges.

1. By the Handshaking Lemma, $3k + \ell = 2(n-1) = 2(k+\ell-1)$.

2. Solving gives
   $$\ell = k + 2.$$

For example, $k = 1$ gives the star with $3$ leaves, and $k = 2$ gives two
adjacent degree-3 vertices with $4$ leaves.
:::

::: {.solution for="prob-graph-2-04" status="draft"}
(a) 1. Let $T$ be a tree with $n\ge3$ vertices, so it has $n-1$ edges and
       degree sum $2(n-1)$.

    2. If every vertex had degree at most $1$, the degree sum would be at
       most $n$. But $2(n-1) > n$ when $n\ge3$.

    3. So some vertex has degree at least $2$.

(b) No. The path $P_n$ is a tree on $n$ vertices with maximum degree $2$,
    for every $n$.
:::

::: {.solution for="prob-graph-2-05" status="draft"}
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

::: {.solution for="prob-graph-2-06" status="draft"}
A tree with $n$ vertices has $n-1$ edges, so its average degree is
$$\frac{2(n-1)}{n} = 2 - \frac2n < 2.$$
:::
