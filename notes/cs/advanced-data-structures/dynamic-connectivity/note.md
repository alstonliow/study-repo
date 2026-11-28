---
title: "Dynamic Connectivity"
sources: [mit6851-20]
requires: [cs/advanced-data-structures/euler-tour-trees, cs/data-structures/union-find]
status: draft
---

<!-- Added 2026-11-26 from MIT 6.851 (Spring 2012), Lecture 20, in our own wording; proofs written out in steps. Decremental trees and the survey of other dynamic graph problems are only summarised. The offline divide-and-conquer remark is our own addition, not from the lecture. -->

Maintain an undirected graph under edge insertions, edge deletions and queries "are $u$ and $v$ connected?". Insertions alone are union-find; deletions are the difficulty, because deleting an edge of a spanning forest may or may not disconnect the graph.

::: {#def-dynamic-connectivity .definition name="Dynamic connectivity"}

Maintain a graph on $n$ vertices under $\operatorname{insert}(u,v)$, $\operatorname{delete}(u,v)$ and $\operatorname{connected}(u,v)$. The problem is *incremental* if only insertions are allowed, *decremental* if only deletions, and *fully dynamic* otherwise.

:::

::: {#prp-incremental-connectivity .proposition name="Incremental and trees"}

Incremental connectivity is solved by union-find in $O(\alpha(m,n))$ amortised time per operation. For a dynamic *forest* (edge insertion linking two trees, deletion of a tree edge), Euler-tour trees (@thm-euler-tour-tree) or link-cut trees give $O(\log n)$ per operation.

:::

For a general graph, keep a spanning forest $F$ in an Euler-tour tree: a query is $\operatorname{findroot}(u)=\operatorname{findroot}(v)$, and an insertion that joins two trees adds the edge to $F$. When a tree edge $e$ is deleted, a *replacement edge* of the graph (a non-tree edge reconnecting the two halves) must be found, and the problem is to find it without scanning many edges repeatedly.

::: {#def-hdt-levels .definition name="Level structure (Holm–de Lichtenberg–Thorup)"}

Give every edge a *level* in $\{0,\dots,\lfloor\log_2n\rfloor\}$ that only decreases over time; new edges get the top level $L=\lfloor\log_2n\rfloor$. Let $G_i$ be the graph of edges of level $\le i$, and $F_i$ a spanning forest of $G_i$ kept in Euler-tour trees, augmented to report a vertex incident to a non-tree edge of level exactly $i$. The structure maintains

1. every connected component of $G_i$ has at most $2^i$ vertices;
2. $F_0\subseteq F_1\subseteq\dots\subseteq F_L$ (so $F_L$ is a minimum spanning forest of $G=G_L$ for the weights "level").

:::

```{=latex}
\begin{algorithm}
\caption{Delete an edge $e=(u,v)$}
\begin{algorithmic}
\STATE remove $e$ from the adjacency lists
\IF{$e\notin F_L$}
    \RETURN
\ENDIF
\STATE remove $e$ from $F_i$ for all $i\ge\mathrm{level}(e)$
\FOR{$i=\mathrm{level}(e)$ \TO $L$}
    \STATE let $T_u,T_v$ be the trees of $F_i$ containing $u,v$; assume $|T_v|\le|T_u|$
    \STATE push every level-$i$ tree edge of $T_v$ down to level $i-1$
    \FOR{each non-tree edge $(x,y)$ of level $i$ with $x\in T_v$}
        \IF{$y\in T_u$}
            \STATE add $(x,y)$ to $F_i,F_{i+1},\dots,F_L$; \RETURN
        \ELSE
            \STATE $\mathrm{level}(x,y)\gets i-1$
        \ENDIF
    \ENDFOR
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

The insertion of an edge $e$ sets its level to $L$, adds it to the adjacency lists, and adds it to $F_L$ if its ends lie in different trees.

::: {#thm-dynamic-connectivity .theorem name="Dynamic connectivity in $O(\log^2n)$"}

The structure above supports $\operatorname{insert}$ and $\operatorname{delete}$ in $O(\log^2n)$ amortised time and $\operatorname{connected}$ in $O(\log n)$ time (with $B$-tree based Euler-tour trees $O(\log n/\log\log n)$).

:::

::: {.proof}

1. *Query.* $u,v$ are connected iff they are in the same tree of $F_L$: two $\operatorname{findroot}$ calls.

2. *Where to search.* A replacement edge $f$ for $e$ has level $\ge\mathrm{level}(e)$. Suppose $\mathrm{level}(f)=j<\mathrm{level}(e)$. Its ends are joined in $F_j\subseteq F_L$ by a path; they lie on different sides of $e$ in $F_L$, so that path is the $F_L$-path through $e$, and then $e\in F_j$, which means $\mathrm{level}(e)\le j$, a contradiction. So the search starts at $i=\mathrm{level}(e)$ and moves up.

3. *Why the smaller side can be pushed down.* At level $i$ the trees $T_u,T_v$ lie in one component of $G_i$ before the deletion, so $|T_u|+|T_v|\le2^i$ by property 1 and $|T_v|\le2^{i-1}$. After moving the level-$i$ edges inside $T_v$ to level $i-1$, the component $T_v$ of $G_{i-1}$ has at most $2^{i-1}$ vertices, so property 1 is kept. Each non-tree edge of level $i$ at $T_v$ has both ends in $T_u\cup T_v$ (the component of $G_i$); either it joins $T_v$ to $T_u$ (a replacement) or both ends are in $T_v$ and it is demoted.

4. *Cost of the search.* Each scanned edge that is not a replacement has its level decreased; each level is decreased at most $L=O(\log n)$ times per edge, and each decrease costs $O(\log n)$ (finding the next candidate in the augmented tree and moving an edge between forests). Charge those scans to the decreases: $O(\log n)\cdot O(\log n)$ per edge over its life, which is $O(\log^2n)$ amortised per *insertion* of the edge.

5. *Rest of a deletion.* Removing $e$ from the forests and, per level, one split and one successful or failed search step costs $O(\log n)$ per level, $O(\log^2n)$ in total. Adding the replacement edge to $F_i,\dots,F_L$ is $O(\log^2n)$ as well.

:::

::: {#rmk-dynamic-connectivity-1 .remark name="Other bounds and an offline variant"}

If all edges are eventually deleted and only deletions occur on a tree, connectivity queries are answered in $O(1)$ amortised time by trimming the tree below vertices with $\ge\log n$ descendants and using bit vectors for the pieces. Thorup reaches $O(\log n(\log\log n)^3)$ updates; a worst-case $O(\sqrt n)$ update with $O(1)$ query is known; and lower bounds of Pătrașcu and Demaine show that the above trade-offs between update and query time are essentially optimal. Whether $O(\log n)$ is possible for both operations is open. When all operations are known in advance (offline), a simpler method suffices in contests: put each edge on the $O(\log m)$ nodes of a segment tree over its lifetime, traverse the tree depth-first, and use a union-find with rollback; this takes $O(m\log m\log n)$ time overall.

:::
