<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-graph-1-09" status="draft"}
Each vertex meets two sides of the square, each of them doubled, plus one
diagonal. So every vertex has degree $2\cdot2 + 1 = 5$, which is odd.

A trail through every edge requires $0$ or $2$ vertices of odd degree, because
each internal visit of the trail uses two edges at a vertex. This graph has
$4$ odd vertices, so there is no trail containing every edge, and hence no
Euler tour.
:::

::: {.solution for="prob-graph-1-10" status="draft"}
A connected graph is Eulerian if and only if every degree is even.

| solid | vertices | degree | Eulerian? |
|---|---|---|---|
| tetrahedron | 4 | 3 | no |
| cube | 8 | 3 | no |
| octahedron | 6 | 4 | **yes** |
| dodecahedron | 20 | 3 | no |
| icosahedron | 12 | 5 | no |

Hamiltonian cycles, using these labels:

- **Tetrahedron** ($K_4$, vertices $1,2,3,4$): $1\,2\,3\,4\,1$.
- **Cube** (vertices are 3-bit strings, see Exercise 11):
  $000,001,011,010,110,111,101,100,000$.
- **Octahedron**: top $T$, bottom $B$, and equator $1,2,3,4$ in order. $T$
  and $B$ are adjacent to all four equator vertices. Cycle:
  $T\,1\,2\,B\,3\,4\,T$.
- **Dodecahedron**: outer pentagon $a_0,\dots,a_4$, middle $10$-cycle
  $b_0,\dots,b_9$, inner pentagon $c_0,\dots,c_4$, with $a_i\sim b_{2i}$ and
  $c_i\sim b_{2i+1}$. Cycle:
  $$a_0a_1a_2a_3a_4\,b_8b_7b_6b_5b_4b_3b_2b_1\,c_0c_1c_2c_3c_4\,b_9b_0\,a_0.$$
- **Icosahedron**: top $t$, upper pentagon $u_0,\dots,u_4$, lower pentagon
  $l_0,\dots,l_4$, bottom $s$, with $u_i\sim l_i$ and $u_i\sim l_{i+1}$
  (indices mod $5$). Cycle:
  $$t\,u_0\,l_0l_1l_2l_3\,s\,l_4\,u_4u_3u_2u_1\,t.$$

Euler tour of the octahedron, through all $12$ edges:
$$T\,1\,2\,3\,4\,1\,B\,2\,T\,3\,B\,4\,T.$$
:::

::: {.solution for="prob-graph-1-11" status="draft"}
(a) The vertices are the corners of a cube. Each edge changes one bit, and
    the three directions correspond to the three bits:

```{=latex}
\begin{tikzpicture}[scale=1.6, every node/.style={font=\small, fill=white, inner sep=1.5pt}]
  \node (000) at (0,0) {000};   \node (100) at (2,0) {100};
  \node (010) at (0,2) {010};   \node (110) at (2,2) {110};
  \node (001) at (0.8,0.7) {001}; \node (101) at (2.8,0.7) {101};
  \node (011) at (0.8,2.7) {011}; \node (111) at (2.8,2.7) {111};
  \draw (000)--(100)--(110)--(010)--(000);
  \draw (001)--(101)--(111)--(011)--(001);
  \draw (000)--(001); \draw (100)--(101); \draw (010)--(011); \draw (110)--(111);
\end{tikzpicture}
```

(b) $000,001,011,010,110,111,101,100$, and back to $000$.

(c) Reflect and prefix (as for Gray codes in Exercise 1.5).

    1. $Q_2$: the cycle $00, 01, 11, 10$.

    2. Given a Hamiltonian cycle $L = x_1,\dots,x_N$ of $Q_{n-1}$, with
       $N = 2^{n-1}$, form
       $$0x_1, 0x_2, \dots, 0x_N,\ 1x_N, 1x_{N-1}, \dots, 1x_1.$$

    3. Consecutive strings differ in one bit: inside each half because $L$
       does, at the middle ($0x_N$ to $1x_N$) in the first bit, and at the
       wrap-around ($1x_1$ to $0x_1$) in the first bit. Every $n$-bit string
       appears exactly once, so this is a Hamiltonian cycle of $Q_n$
       (for $n\ge 2$). Starting from $Q_2$ and applying step 2 repeatedly
       covers every $n$.

(d) $Q_4$ is connected and every vertex has degree $4$, so it is Eulerian.
    One Euler tour, through all $32$ edges:

    0000 1000 1100 0100 0000 0010 1010 1110 0110 0010 0011 1011 1111 0111 0011 0001
    1001 1011 1010 1000 1001 1101 1111 1110 1100 1101 0101 0111 0110 0100 0101 0001 0000
:::

::: {.solution for="prob-graph-1-12" status="draft"}
Let $G$ be a connected multigraph (multiple edges and loops allowed).

1. *Construct $H$.* Replace every edge of $G$ by a path of length $3$: for
   an edge $e$ with ends $x,y$, add two new vertices $e_1,e_2$ and the edges
   $xe_1$, $e_1e_2$, $e_2y$. Do this for loops too ($x = y$). $H$ is a
   simple graph: no loops, and no two edges have the same ends.

2. *Degrees.* Each original vertex has the same degree in $H$ as in $G$
   (a loop contributes $2$ both times). Each new vertex has degree $2$.

3. *Connectivity.* $H$ is connected because $G$ is: every walk in $G$
   becomes a walk in $H$, and each new vertex is on such a path.

4. *Euler tours correspond.* An Euler tour of $G$ becomes one of $H$ by
   replacing each edge with its path of length $3$. Conversely, an Euler
   tour of $H$ must traverse each such path in one go, because its inner
   vertices have degree $2$; contracting the paths gives an Euler tour of
   $G$.

5. By Theorem 64 applied to $H$:
   $G$ is Eulerian $\iff$ $H$ is Eulerian $\iff$ every vertex of $H$ has
   even degree $\iff$ every vertex of $G$ has even degree, using step 2.
:::
