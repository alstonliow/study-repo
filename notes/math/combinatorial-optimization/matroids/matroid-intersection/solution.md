<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18433-6-q1" status="draft"}
1. Use the partition matroids $M_A$, $M_B$ of @exm-matroid-intersection-examples, whose common independent sets are the matchings. For $U\subseteq E$, $r_A(U)$ is the number of vertices of $A$ incident to $U$, and $r_B(E\setminus U)$ the number of vertices of $B$ incident to $E\setminus U$.

2. Let $C$ be the set of these vertices. Every edge of $U$ is covered by its end in $A$, every edge of $E\setminus U$ by its end in $B$, so $C$ is a vertex cover with $|C|\le r_A(U)+r_B(E\setminus U)$.

3. By @thm-matroid-intersection, for a minimising $U$ the maximum matching size equals $r_A(U)+r_B(E\setminus U)\ge|C|$, while $|C|\ge$ the maximum matching size by weak duality (@prp-matching-cover-weak-duality). So a maximum matching and a minimum vertex cover have the same size.
:::

::: {.solution for="prob-mit18433ps-5-q5" status="draft"}
Arcs follow @def-exchange-graph: $(y,x)$ if $S-y+x$ is a forest in $G_1$, $(x,y)$ if it is a forest in $G_2$ ($y\in S$, $x\notin S$).

1. *Sources* $X_1=\{x:S+x \text{ acyclic in } G_1\}=\{f,i\}$ ($e,h,g$ close cycles with $a,b,c,d$ in $G_1$). *Sinks* $X_2=\{x:S+x\text{ acyclic in }G_2\}=\{e,h\}$.

2. *Arcs* $(y,x)$ (from $M_1$): $a\to f,g,h,i$; $b\to f,g,i$; $c\to e,f,g,h,i$; $d\to e,f,g,h,i$. *Arcs* $(x,y)$ (from $M_2$): $e\to a,b,c,d$; $f\to a,b$; $g\to a,b,c,d$; $h\to a,b,c,d$; $i\to c,d$. (Computed by checking each exchange for a cycle.)

3. A shortest source–sink path is $f\to a\to h$: $S-a+f$ is a forest in $G_2$ and $S-a+h$ a forest in $G_1$. Augmenting gives $S\triangle\{f,a,h\}=\{b,c,d,f,h\}$.

4. Check: in $G_1$ the edges $b,c,d,f,h$ form a spanning tree of its $6$ vertices, and in $G_2$ as well. With $5=|V|-1$ elements this common independent set is maximum.
:::

::: {.solution for="prob-mit18433ps-6-q4" status="draft"}
1. *Matroids on the rows.* $M_1$: $I$ independent iff the rows of $A_{I,Y_1}$ are independent (a linear matroid), rank $r_1(U)=\operatorname{rank}A_{U,Y_1}$. $N$: the same with $Y_2$, rank $r_N(U)=\operatorname{rank}A_{U,Y_2}$; $r_N([n])=|Y_2|$ because $A_{[n],Y_2}$ has independent columns. Let $M_2=N^*$, with rank $r_2(U)=|U|+r_N([n]\setminus U)-|Y_2|$ (@thm-dual-matroid-rank).

2. *What we need.* If $X_1\in\mathcal I_1\cap\mathcal I_2$ with $|X_1|=|Y_1|$, then $A_{X_1,Y_1}$ is square with independent rows, so invertible; and $X_1\in\mathcal I(N^*)$ means $X_2=[n]\setminus X_1$ contains a base of $N$, of size $|Y_2|=|X_2|$, so $X_2$ is that base and $A_{X_2,Y_2}$ is invertible.

3. *Min-max.* Every common independent set has at most $r_1([n])=|Y_1|$ elements. By @thm-matroid-intersection it suffices that $r_1(U)+r_2([n]\setminus U)\ge|Y_1|$ for all $U$. Now $r_2([n]\setminus U)=n-|U|+\operatorname{rank}A_{U,Y_2}-|Y_2|=|Y_1|-|U|+\operatorname{rank}A_{U,Y_2}$, so the condition is
$$\operatorname{rank}A_{U,Y_1}+\operatorname{rank}A_{U,Y_2}\ge|U| .$$

4. This holds: the column space of $A_{U,[n]}$ is the sum of those of $A_{U,Y_1}$ and $A_{U,Y_2}$, so the two ranks add up to at least $\operatorname{rank}A_{U,[n]}=|U|$ (the rows of the invertible $A$ are independent).
:::
