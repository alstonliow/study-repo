<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-8-q1" status="draft"}
(a) Always countable. Every disk contains a point with both coordinates rational (rationals are dense: inside the open disk there is a small square, which contains a point of $\mathbb Q\times\mathbb Q$). Choose one such point for each disk. Disjoint disks give different points, so this is an injection into $\mathbb Q\times\mathbb Q$, which is countable (@cor-rationals-countable); hence the set is countable (@prp-injection-into-countable).

(b) Potentially uncountable: the circles centred at the origin with radius $r\in(0,1)$ are pairwise disjoint, and there is one for each real $r\in(0,1)$, an uncountable set (@thm-reals-uncountable).

(c) Uncountable. For an infinite $0/1$ sequence $b=(b_0,b_1,\dots)$ let $f_b(n)=b_0+\dots+b_n$. Each $f_b$ is increasing, and $b$ can be read back from $f_b$ ($b_0=f_b(0)$, $b_n=f_b(n)-f_b(n-1)$), so $b\mapsto f_b$ is injective. Infinite $0/1$ sequences correspond to subsets of $\mathbb N$, which are uncountable (@thm-power-set-uncountable).

(d) Countable. A decreasing $f:\mathbb N\to\mathbb N$ can decrease at most $f(0)$ times, so it is eventually constant: there is a last position $N$ where it decreases, and $f$ is determined by the finite list $f(0),\dots,f(N)$. Encode this list as a finite string over the alphabet $\{0,\dots,9,\#\}$. Different functions get different strings, so this is an injection into the countable set of finite strings (@prp-finite-strings-countable).
:::

::: {.solution for="prob-cs70hw-8-q3" status="draft"}
Graphs are undirected; we may take the fixed vertex set to be $\mathbb N$.

(a) Countable. Write a finite graph as the finite string listing its vertices and then its edges, e.g. "$0,3,7\#\{0,3\},\{3,7\}$". Different graphs give different strings, so the set injects into the finite strings over a finite alphabet, which are countable (@prp-finite-strings-countable).

(b) Uncountable. For each subset $S\subseteq\mathbb N$ let $G_S$ have the edges $\{0,n\}$ for $n\in S\setminus\{0\}$. All $G_S$ are infinite graphs on $\mathbb N$ (the vertex set is infinite), and different subsets $S\setminus\{0\}$ give different graphs. Subsets of $\mathbb N\setminus\{0\}$ are uncountable (@thm-power-set-uncountable).

(c) Uncountable. Split $\mathbb N$ into blocks of $6$ consecutive numbers. For each infinite $0/1$ sequence $b$, let block $k$ carry two disjoint triangles if $b_k=0$ and one $6$-cycle if $b_k=1$. Every vertex has degree exactly $2$, and different sequences give different edge sets. Infinite $0/1$ sequences are uncountable.

(d) No: even up to isomorphism there are uncountably many trees.

1. An isomorphism $f$ maps the neighbours of $v$ bijectively onto the neighbours of $f(v)$, so $\deg f(v)=\deg v$; in particular it maps leaves to leaves and non-leaves to non-leaves.

2. For $S\subseteq\mathbb N$ build $T_S$: a ray $v_0,v_1,v_2,\dots$, and at each $v_i$ attach $1$ leaf if $i\in S$ and $2$ leaves if $i\notin S$. It is an infinite tree.

3. The non-leaves of $T_S$ are exactly the $v_i$, and they form a ray in which only $v_0$ has a single non-leaf neighbour. An isomorphism $T_S\to T_{S'}$ maps non-leaves to non-leaves and adjacency to adjacency, so it maps $v_0\mapsto v_0$ and then, step by step along the ray, $v_i\mapsto v_i$.

4. By step 1, $\deg v_i$ is the same in both trees, so $v_i$ has the same number of leaves: $i\in S\iff i\in S'$. So $T_S\cong T_{S'}$ only if $S=S'$, and the uncountably many subsets of $\mathbb N$ give pairwise non-isomorphic trees.
:::
