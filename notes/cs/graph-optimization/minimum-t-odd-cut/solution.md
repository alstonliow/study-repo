<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6854ps-4-q6" status="draft"}
*1.* Replace each edge $uv$ by the arcs $u\to v$ and $v\to u$, both of weight $w_{uv}$. For every $S$ with $s\in S$, $t\notin S$, the arcs leaving $S$ are exactly one orientation of each edge of $(S:\bar S)$, so directed and undirected cut weights agree.

*2.* Fix $t_0\in T$. A $T$–$T$ cut separates $t_0$ from some $t\in T\setminus\{t_0\}$, and every such $t_0$–$t$ cut is a $T$–$T$ cut. So the best of the $|T|-1$ minimum $t_0$–$t$ cuts is a minimum $T$–$T$ cut.

*3.* This is @lem-cut-submodular: count each edge by where its ends lie. Edges between $A\setminus B$ and $B\setminus A$ count twice on the left and not at all on the right; every other edge counts at least as often on the left as on the right.

*4.* If $|S\cap T|$ is odd, $S$ is a $T$-cut; and every $T$-cut is a $T$–$T$ cut (both sides meet $T$ in an odd, hence non-zero, number), so $S$ is a minimum $T$-cut.

Suppose $|S\cap T|$ is even. Let $T_1=S\cap T$ and $T_2=\bar S\cap T$, both even and non-empty, and let $C$ be a minimum $T$-cut.

1. Exactly one of $|C\cap T_1|$, $|C\cap T_2|$ is odd. Since $d(S)=d(\bar S)$, we may exchange the roles of $S$ and $\bar S$ and assume $|C\cap T_1|$ odd, $|C\cap T_2|$ even.

2. If $T_2\subseteq C$, replace $C$ by $\bar C$: it is also a minimum $T$-cut, $|\bar C\cap T_1|=|T_1|-|C\cap T_1|$ is odd and $\bar C\cap T_2=\varnothing$. So we may assume $T_2\not\subseteq C$.

3. Then $C\cup S$ contains $T_1\ne\varnothing$ and misses part of $T_2$, so it is a $T$–$T$ cut: $d(C\cup S)\ge d(S)$. By 3, $d(C\cap S)\le d(C)+d(S)-d(C\cup S)\le d(C)$.

4. $|(C\cap S)\cap T|=|C\cap T_1|$ is odd, so $C\cap S\subseteq S$ is a minimum $T$-cut.

*Algorithm.* If the minimum $T$–$T$ cut $S$ is odd, return it. Otherwise recurse on $G/\bar S$ (shrink $\bar S$ to one vertex, which is not a terminal since $|T_2|$ is even) with terminals $T_1$, and on $G/S$ with terminals $T_2$, and return the better answer. Shrinking preserves the weights of the cuts that do not split the shrunk set, which by the argument above include an optimal one. Each recursive call splits the current terminal set into two even parts of size at least $2$, so the recursion tree has at most $|T|/2$ leaves and at most $|T|$ calls of the $T$–$T$ cut algorithm, i.e. $O(|T|^2)$ minimum $s$–$t$ cuts. (Compare @def-t-odd-cut-algorithm.)
:::
