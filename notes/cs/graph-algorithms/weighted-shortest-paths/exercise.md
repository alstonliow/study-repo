::: {.problem #prob-mit6006-11-q1 origin="external" source="mit6006-11-q1"}
Prove this algorithm correctly computes parent pointers in linear time

*Note (these notes):* "This algorithm" extends @prp-parents-from-distances to graphs that may have cycles of weight $0$. Given $\delta(s,v)$ for all $v$ (no negative-weight cycle reachable from $s$): (i) set $P(s)=$ None; for each $u$ with $\delta(s,u)$ finite and each edge $(u,v)$, if $P(v)$ is unset and $\delta(s,v)=\delta(s,u)+w(u,v)$, set $P(v)=u$. (ii) Parent pointers may now run around cycles of weight $0$; mark every vertex on such a cycle. (iii) For each unmarked vertex $u$ (including vertices unmarked later in this step) and each edge $(u,v)$ with $v$ marked and $\delta(s,v)=\delta(s,u)+w(u,v)$: unmark the vertices of the cycle through $v$ by following parent pointers from $v$, and set $P(v)=u$.
:::
