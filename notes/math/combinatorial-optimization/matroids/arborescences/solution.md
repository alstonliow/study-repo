<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18433ps-6-q2" status="draft"}
Take $V=\{r,a,b\}$ with arcs $ab$ (cost $1$), $ba$ ($3$), $rb$ ($2$), $ra$ ($10$).

1. With $S=\{a,b\}$, the cheapest admissible arc is $ab$ (cost $1$); add it and remove $b$ from $S$.
2. With $S=\{a\}$, the arcs into $a$ are $ba$, which would close the directed circuit $a\to b\to a$, and $ra$. So $ra$ (cost $10$) is added.

Greedy returns $\{ab,ra\}$ of cost $11$, while $\{rb,ba\}$ is an $r$-arborescence of cost $5$. (The primal–dual algorithm of @def-arborescence-algorithm finds the latter.)
:::

::: {.solution for="prob-mit18433ps-6-q3" status="draft"}
Assume $D$ is strongly connected (otherwise some $r$ has no arborescence) and allow arcs into every vertex.

1. *Rootless phase 1.* Start with $F=\varnothing$, $y=0$. While $F$ is not strongly connected, pick a strong component $S\ne V$ of $(V,F)$ with no arc of $F$ entering it (a source of the acyclic component graph), raise $y_S$ until an arc $a_k\in\delta^-(S)$ is tight, and add it to $F$. At the end $F=\{a_1,\dots,a_k\}$ is strongly connected, $y$ is feasible for every dual, and every arc of $F$ is tight: $c_a=\sum_{S:\,a\in\delta^-(S)}y_S$.

2. *For each root $r$:* run reverse delete on $F$ with root $r$ (test $a_k,\dots,a_1$, delete an arc if all vertices stay reachable from $r$), obtaining $T_r$.

3. *Correctness for a fixed $r$.* Exactly as in the proof of @thm-arborescence-algorithm: $T_r$ is an $r$-arborescence, and $|T_r\cap\delta^-(S)|=1$ for every chosen $S$ with $r\notin S$. For a chosen $S\ni r$, no arc of $T_r$ enters $S$: when such an arc $a_m$ ($m\ge k$, where $a_k$ was added for $S$) was tested, the arcs $a_i$, $i<k$, were present and made $S$ strongly connected, so all of $S$ was reachable from $r\in S$ without $a_m$, and any path through $a_m$ could continue from the last vertex of $S$ on it; so $a_m$ was deleted.

4. Restricting $y$ to the sets $S\not\ni r$ gives a feasible dual for root $r$, and
$$c(T_r)=\sum_{a\in T_r}\sum_{S:\,a\in\delta^-(S)}y_S=\sum_Sy_S\,|T_r\cap\delta^-(S)|=\sum_{S\not\ni r}y_S,$$
its value. By weak duality $T_r$ is optimal.

5. *Cost.* Phase 1, the expensive part, runs once; each root then needs only a reverse delete pass ($|F|\le2|V|$ reachability tests).
:::
