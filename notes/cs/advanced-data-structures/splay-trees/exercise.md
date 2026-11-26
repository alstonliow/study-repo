::: {.problem #prob-mit6854ps-3-q1 origin="external" source="mit6854ps-3-q1"}
Consider the symmetric traveling salesman path problem. We are given a set $V$ of vertices, a (symmetric) distance $d(i,j)=d(j,i)\ge0$ for every pair $i,j$ of vertices, 2 special vertices $s$ and $t$, and we would like to find a path from $s$ to $t$ passing through all vertices (a *Hamiltonian* path) and of minimum total length. This problem is NP-hard, and so we will not try to solve it exactly in polynomial time.

One simple heuristic is known as 2-OPT. Start from any ordering $v_1=s,v_2,\cdots,v_n=t$ and remove 2 non-consecutive edges of the Hamiltonian path, say $(v_i,v_{i+1})$ and $(v_j,v_{j+1})$ where $i+1<j$. Now, there is a unique way to form a new Hamilonian path by adding 2 other edges, namely $(v_i,v_j)$ and $(v_{i+1},v_{j+1})$. If this results in a path of shorter length, this so-called 2-swap is performed, and this is repeated until no more improvements are possible.

Now suppose we would like to create a data structure to maintain the ordering of the vertices on the path. For any vertex $v$, we would like to be able to find $\textsc{Next}(v)$, the vertex following $v$ on the way to it, and similarly $\textsc{Previous}(v)$, the vertex preceding $v$ (i.e. closer to $s$). The tricky thing is that when we perform a 2-swap, the vertices $v_{i+1}$ to $v_j$ are now visited in the *reverse* order (from $v_i$ we go to $v_j$, then to $v_{j-1}$ and continue all the way to $v_{i+1}$, and then continue at $v_{j+1}$). This means we would also like to have an operation $\textsc{Reverse}(v,w)$ that reverses the ordering from $v$ to $w$; in our case above we would perform $\textsc{Reverse}(v_{i+1},v_j)$. If we were maintaining the ordering as a doubly-linked list (with pointers *next* and *previous*), a $\textsc{Reverse}$ operation would require $\Theta(n)$ time in the worst-case. Show how to use splay trees to maintain the ordering and perform any sequence of $m$ operations ($\textsc{Next}$, $\textsc{Previous}$, or $\textsc{Reverse}$) in $O((m+n)\log n)$ time.

(If you augment the splay tree with additional information at every node, you must indicate how this information is maintained while performing operations.)
:::

::: {.problem #prob-mit6854ps-3-q2 origin="external" source="mit6854ps-3-q2"}
In lecture, we argued the static optimality property of splay trees by showing that the time $T$ required for a splay tree to access element $i$ $m_i\ge1$ times for $i=1,\cdots,n$ is within a constant of the time required by any static BST. In this problem, you need to argue that this time $T$ for splay trees is
$$O\left(\sum_im_i\left(1+\log\frac m{m_i}\right)\right),$$
where $m=\sum_im_i$ is the total number of accesses.
:::
