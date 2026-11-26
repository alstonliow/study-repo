::: {.problem #prob-mit6854ps-3-q3 origin="external" source="mit6854ps-3-q3"}
In the blocking flow problem (which arises in the blocking flow algorithm for the maximum flow problem), we are given a directed acyclic graph $G=(V,E)$, 2 vertices $s$ and $t$ and capacities on the edges. The goal is to find a flow $f$ such that for every path $P$ in $E$ from $s$ to $t$ at least one of the edges of $P$ is saturated (i.e. $f(v,w)=u(v,w)$).

1. Is the following argument correct?

   > A blocking flow $f$ is maximum since, if we take $S$ to be the set of vertices reachable from $s$ in $(V,E)$ by non-saturated edges, we get a cut $(S:\bar S)$ whose value equals the blocking flow, and hence the blocking flow must be optimal.

   If the argument is fallacious, show a blocking flow which is not maximum.

2. Show how to find a blocking flow in a graph $G=(V,E)$ with $n$ vertices and $m$ edges in $O(m\log n)$ time. (Your solution can be quite short.)

(FYI, Dinitz showed that one can solve a maximum flow problem in a general directed graph by solving at most $n$ blocking flow problems in directed acyclic graphs.)
:::
