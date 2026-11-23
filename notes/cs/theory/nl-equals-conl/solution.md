<!-- Solutions marked status="draft" on Sipser problems were written by Claude in our own words;
     18.404J publishes no problem-set solutions and the book's Selected Solutions were not read.
     Owner to review, then remove status. -->

::: {.solution for="prob-sipser3e-8-q27" status="draft"}
1. *In NL.* Loop over all ordered pairs $(a,b)$ of nodes with two log-size counters. For each pair, guess a path from $a$ to $b$ of at most $n$ steps, node by node, and reject the branch if the guess fails. A branch survives all pairs iff every pair has a path, so some branch accepts iff $G$ is strongly connected.

2. *NL-hard: $\mathit{PATH}\le_{\mathrm L}\mathit{STRONGLY\text-CONNECTED}$.* Given $\langle G,s,t\rangle$, output $G'$: the graph $G$ plus an edge $t\to v$ and an edge $v\to s$ for every node $v$. This takes log space, since we only copy $G$ and loop over the nodes.

3. *A path gives strong connectivity.* If $G$ has a path from $s$ to $t$, then for any $u,v$ the walk $u\to s\leadsto t\to v$ lies in $G'$. So $G'$ is strongly connected.

4. *No path, no strong connectivity.* If $G$ has no path from $s$ to $t$, take a shortest path from $s$ to $t$ in $G'$, if one exists. It never uses an edge into $s$ (that would revisit $s$) or out of $t$ (that would revisit $t$). So it uses only edges of $G$, which is impossible. So $G'$ has no path from $s$ to $t$ and is not strongly connected.

5. $\mathit{PATH}$ is NL-complete, so $\mathit{STRONGLY\text-CONNECTED}$ is NL-complete.
:::
