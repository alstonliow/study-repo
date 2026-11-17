::: {.problem #prob-mit6006s20-6-q2 origin="external" source="mit6006s20-6-q2"}
**Short Circuits**

Given a weighted directed graph $G=(V,E,w)$ and vertex $s\in V$, with the property that, for every vertex $v\in V$, some minimum-weight path from $s$ to $v$ traverses at most $k$ edges, describe an algorithm to find the shortest-path weight from $s$ to each $v\in V$ in $O(|V|+k|E|)$ time.
:::

::: {.problem #prob-mit6006s20-6-q4 origin="external" source="mit6006s20-6-q4"}
**Conservative Cycles**

In Wentonian physics, a force field acts on the motion of a particle by requiring a certain positive or negative amount of work to move along any path. A force field is conservative if the total sum of work is zero along every closed loop. Given a discrete force field represented by $n$ possible particle locations $\ell_i$ and $O(n)$ possible particle transitions, where transition $(\ell_i,\ell_j,w_{ij})$ moves a particle along a directed path from location $\ell_i$ to location $\ell_j$ requiring (positive or negative) integer work $w_{ij}$, describe an $O(n^2)$-time algorithm to determine whether the force field is conservative.

(Footnote: Note that a transition from $\ell_i$ to $\ell_j$ does not imply the existence of a transition from $\ell_j$ to $\ell_i$.)
:::
