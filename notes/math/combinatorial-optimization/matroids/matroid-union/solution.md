<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18433ps-6-q1" status="draft"}
Write $r=r(E)$ for short where no confusion arises. This proves @thm-dual-matroid-rank.

1. *(I1).* If $F'\subseteq F\in\mathcal I^*$, then $E\setminus F'\supseteq E\setminus F$ contains a base.

2. *(I2).* Let $X,Y\in\mathcal I^*$ with $|Y|>|X|$ and suppose no $e\in Y\setminus X$ has $X+e\in\mathcal I^*$, i.e. $r(E\setminus X-e)<r(E)$: every $e\in Y\setminus X$ lies in every base inside $E\setminus X$. Let $Z=E\setminus(X\cup Y)$ and fix a base $B_X\subseteq E\setminus X=(Y\setminus X)\cup Z$; then $Y\setminus X\subseteq B_X$ and $|B_X\cap Z|=r(E)-|Y\setminus X|$. A base $B_Y\subseteq E\setminus Y=(X\setminus Y)\cup Z$ shows $r(Z)\ge r(E)-|X\setminus Y|>r(E)-|Y\setminus X|$. So the independent set $B_X\cap Z$ can be extended by some $z\in Z$ (by (I2) inside $Z$). The unique circuit of $B_X+z$ (@thm-unique-circuit) is not inside $(B_X\cap Z)+z$, so it contains some $e\in Y\setminus X$, and $B_X+z-e$ is a base inside $E\setminus X-e$: a contradiction.

3. *Bases.* A maximal $F$ with $E\setminus F$ containing a base $B$ is $F=E\setminus B$. So the bases of $M^*$ are the complements of the bases of $M$.

4. *(b)* $r^*(U)=|U|+r(E\setminus U)-r(E)$. Upper bound: if $F\subseteq U$ and $E\setminus F\supseteq B$ (a base), then $B\cap U\subseteq U\setminus F$, so $|F|\le|U|-|B\cap U|$, and $|B\cap U|=r(E)-|B\setminus U|\ge r(E)-r(E\setminus U)$. Lower bound: take a maximal independent $J\subseteq E\setminus U$ and extend it to a base $B$; then $B\setminus U=J$, and $F=U\setminus B$ has $E\setminus F\supseteq B$ and $|F|=|U|-(r(E)-r(E\setminus U))$.
:::

::: {.solution for="prob-mit18433-6-q2" status="draft"}
Induct on $k$. For $k=1$ the formula gives $r_1(S)$: $F=S$ attains it, and $|S\setminus F|+r_1(F)\ge r_1(S)$ for every $F$. For $k=2$ it is the theorem.

1. The union of $k$ matroids is $N\vee M_k$ with $N=M_1\vee\dots\vee M_{k-1}$, since $S_1\cup\dots\cup S_k=(S_1\cup\dots\cup S_{k-1})\cup S_k$. By induction $N$ is a matroid, so by @thm-matroid-union so is $N\vee M_k$.

2. Its rank is $\min_{F\subseteq S}\big(|S\setminus F|+r_N(F)+r_k(F)\big)$ with $r_N(F)=\min_{F'\subseteq F}\big(|F\setminus F'|+\sum_{i<k}r_i(F')\big)$. So
$$r(S)=\min_{F'\subseteq F\subseteq S}\Big(|S\setminus F'|+\sum_{i<k}r_i(F')+r_k(F)\Big),$$
using $|S\setminus F|+|F\setminus F'|=|S\setminus F'|$.

3. Since $r_k(F)\ge r_k(F')$, the minimum is attained with $F=F'$, which gives the formula.
:::

::: {.solution for="prob-mit18433-6-q3" status="draft"}
Let $n=|V|$, $M=M(G)$ with $r(F)=n-\kappa(F)$. If $G$ is disconnected, both sides fail (take the partition into components), so assume $G$ connected.

1. $G$ has $k$ edge-disjoint spanning trees iff the union of $k$ copies of $M$ has rank $k(n-1)$: such trees give an independent set of that size; conversely a union of $k$ forests of total size $k(n-1)$, made disjoint by dropping repeated elements, consists of $k$ disjoint forests with $n-1$ edges each, i.e. spanning trees.

2. By exercise 6-2 the rank is $\min_F\big(|E\setminus F|+k(n-\kappa(F))\big)$. It equals $k(n-1)$ (it is at most that, with $F=E$) iff $|E\setminus F|\ge k(\kappa(F)-1)$ for every $F\subseteq E$.

3. As in the proof of @thm-two-disjoint-spanning-trees, this is equivalent to the partition condition: for a partition, take $F=E\setminus\delta(V_1,\dots,V_p)$, which has $\kappa(F)\ge p$; for an $F$, take the partition into the components of $(V,F)$, for which $\delta(V_1,\dots,V_p)\subseteq E\setminus F$.
:::

::: {.solution for="prob-mit18433-6-q4" status="draft"}
Player 2 keeps the following invariant after each of its moves: in the graph $G'$ obtained from $G$ by deleting the deleted edges and contracting the fixed edges, there are two edge-disjoint spanning trees $T_1,T_2$ (loops are ignored). It holds at the start.

1. Player 1 deletes an edge $e$. If $e\notin T_1\cup T_2$, player 2 fixes any edge $f\in T_1$. If $e\in T_1$ (or symmetrically $T_2$), $T_1-e$ has two components, and the spanning tree $T_2$ has an edge $f$ joining them; player 2 fixes $f$, and $T_1-e+f$ is a spanning tree.

2. After contracting $f$: the tree containing $f$ becomes a spanning tree of $G'/f$. The other tree, which does not contain $f$, becomes a connected spanning subgraph of $G'/f$ with one edge too many; dropping an edge of the cycle formed gives a spanning tree. The two remain edge-disjoint, so the invariant holds.

3. Each move of player 2 contracts an edge of a spanning tree, reducing the number of vertices of $G'$ by one. After $|V|-1$ such moves $G'$ is a single vertex, i.e. the fixed edges connect all of $V$ and contain a spanning tree: player 2 wins.
:::

::: {.solution for="prob-mit18433-6-q5" status="draft"}
Two edge-disjoint spanning trees exist; since $30=2\cdot15$, together they use every edge. One choice:

- $T_1=\{12,\ 23,\ 34,\ 16,\ 6\,10,\ 7\,10,\ 78,\ 7\,11,\ 8\,12,\ 59,\ 9\,13,\ 10\,13,\ 11\,16,\ 14\,15,\ 15\,16\}$,
- $T_2=\{15,\ 26,\ 37,\ 47,\ 48,\ 56,\ 67,\ 6\,11,\ 9\,10,\ 10\,11,\ 10\,14,\ 11\,12,\ 11\,15,\ 12\,16,\ 13\,14\}$.

Each has $15$ edges and connects all $16$ vertices, so each is a spanning tree (checked by a union–find computation). For instance in $T_1$ the path $5$–$9$–$13$–$10$–$6$–$1$–$2$–$3$–$4$ and the branches $10$–$7$–$8$–$12$, $7$–$11$–$16$–$15$–$14$ reach every vertex.
:::
