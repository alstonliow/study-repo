<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18433-5-q1" status="draft"}
1. For a part $E_i$ with bound $k_i$, choose $|E_i|$ vectors in $\mathbb R^{k_i}$ in general position, so that any $k_i$ of them are linearly independent; for instance the Vandermonde columns $(1,\alpha,\alpha^2,\dots,\alpha^{k_i-1})$ for distinct reals $\alpha$ (a $k_i\times k_i$ Vandermonde determinant is non-zero). If $k_i=0$, use zero columns.

2. Let $A$ be block diagonal with these blocks. A set of columns is independent iff its columns within each block are independent. Within block $i$, any $\le k_i$ columns are independent and any $>k_i$ columns, lying in $\mathbb R^{k_i}$, are dependent.

3. So $X$ is independent in the linear matroid of $A$ iff $|X\cap E_i|\le k_i$ for all $i$, which is the partition matroid.
:::

::: {.solution for="prob-mit18433-5-q2" status="draft"}
(I1) holds: a matching covering $Y$ covers every subset of $Y$. For (I2), let $X,Y$ be independent with $|Y|>|X|$, covered by matchings $M_X$ and $M_Y$.

1. If some $y\in Y\setminus X$ is covered by $M_X$, then $M_X$ covers $X+y$. So assume no vertex of $Y\setminus X$ is covered by $M_X$.

2. In $H=M_X\triangle M_Y$ every vertex has degree at most $2$, so its components are alternating paths and cycles. Each $y\in Y\setminus X$ is covered by $M_Y$ but not by $M_X$, so it has degree $1$ in $H$: it is an end of a path component $P_y$, whose first edge is in $M_Y$.

3. Let $z$ be the other end of $P_y$. In $M'=M_X\triangle P_y$ all inner vertices of $P_y$ stay covered and $y$ becomes covered; $z$ stays covered unless its edge on $P_y$ belongs to $M_X$. In that case $z$ is not covered by $M_Y$ (it has degree $1$ in $H$), so $z\notin Y$; if moreover $z\in X$, call $P_y$ *bad*. If $P_y$ is not bad, $M'$ covers $X+y$, and we are done.

4. Distinct $y$ lie on distinct paths or at the two ends of one path; a bad path has only one end in $Y\setminus X$ (its other end is in $X\setminus Y$). So bad paths give an injection from their ends in $Y\setminus X$ into $X\setminus Y$. As $|Y\setminus X|>|X\setminus Y|$, some $y\in Y\setminus X$ has a path that is not bad.
:::

::: {.solution for="prob-mit18433-5-q3" status="draft"}
Over $\mathbb F_3$ take the four columns $(1,0)$, $(0,1)$, $(1,1)$, $(1,2)$. Each pair is linearly independent: the determinants are $1$, $1$, $2$, $1$, $1$ and $1\cdot2-1\cdot1=1$, all non-zero in $\mathbb F_3$ (for the pairs $\{1,2\},\{1,3\},\{1,4\},\{2,3\},\{2,4\},\{3,4\}$ up to sign). Any three vectors in $\mathbb F_3^2$ are dependent. So the independent sets are exactly the sets of size at most $2$: this is $U_{2,4}$.
:::

::: {.solution for="prob-mit18433-5-q4" status="draft"}
Write $a_1,\dots,a_5$ for the columns. The last two rows are equal, so $\operatorname{rank}A=2$; $a_2=2a_1$, $a_1=a_3+a_4$ and $a_5=a_3-a_4$.

1. *Bases:* all pairs except the parallel pair $\{1,2\}$: $\{1,3\},\{1,4\},\{1,5\},\{2,3\},\{2,4\},\{2,5\},\{3,4\},\{3,5\},\{4,5\}$ (nine bases).

2. *Circuits:* $\{1,2\}$, and every $3$-set not containing both $1$ and $2$ (rank $2$, while all its pairs are bases): $\{1,3,4\},\{1,3,5\},\{1,4,5\},\{2,3,4\},\{2,3,5\},\{2,4,5\},\{3,4,5\}$. Eight circuits in all (checked by computing ranks).

3. Take $B=\{3,4\}$ and $e=5$. The circuits inside $B+e=\{3,4,5\}$: $\{1,2\}$ is not inside, and the only $3$-circuit inside is $\{3,4,5\}$ itself, so the circuit is unique, as @thm-unique-circuit says. Removing any of its elements gives a base: $\{4,5\}$, $\{3,5\}$, $\{3,4\}$.
:::

::: {.solution for="prob-mit18433-5-q5" status="draft"}
1. Form the bipartite graph with the indices $1,\dots,n$ on one side, the elements of $E$ on the other, and an edge $\{i,a\}$ whenever $a\in A_i$.

2. $T\subseteq E$ is a partial transversal iff some matching covers $T$: a matching covering $T$ assigns distinct indices $i$ to the elements $a\in T$ with $a\in A_i$; keep only these edges. Conversely a partial transversal gives such a matching.

3. So the partial transversals are the independent sets of the matching matroid of this graph (exercise 2) restricted to the vertex set $E$. A restriction of a matroid to a subset of its ground set is a matroid (the axioms only refer to subsets), so they form a matroid.
:::

::: {.solution for="prob-mit18433-5-q6" status="draft"}
(I1): a subset of an independent set of size at most $k$ is independent and has size at most $k$. (I2): if $X,Y\in\mathcal I_k$ with $|Y|>|X|$, then by (I2) for $M$ some $e\in Y\setminus X$ has $X+e\in\mathcal I$, and $|X+e|=|X|+1\le|Y|\le k$, so $X+e\in\mathcal I_k$.
:::

::: {.solution for="prob-mit18433-5-q7" status="draft"}
(I1) is clear (assuming all $k(A)\ge0$, so $\varnothing\in\mathcal I$). For (I2), let $X,Y\in\mathcal I$ with $|Y|>|X|$, and suppose no $e\in Y\setminus X$ has $X+e\in\mathcal I$.

1. Then every $e\in Y\setminus X$ lies in a set $A\in\mathcal F$ that is *tight* for $X$: $|X\cap A|=k(A)$.

2. Let $A_1,\dots,A_m$ be the inclusion-wise maximal tight sets containing elements of $Y\setminus X$. Two of them that intersect are nested (laminarity), hence equal by maximality; so they are pairwise disjoint, and $U=A_1\cup\dots\cup A_m\supseteq Y\setminus X$.

3. For each $l$, $|Y\cap A_l|\le k(A_l)=|X\cap A_l|$, so $|Y\cap U|\le|X\cap U|$. Outside $U$, $Y\setminus U\subseteq X\setminus U$. Adding, $|Y|\le|X|$: a contradiction.
:::
