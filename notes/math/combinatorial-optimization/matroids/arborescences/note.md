---
title: "Minimum Cost Arborescences"
sources: [mit18433-6, mit18433-7]
requires: [math/combinatorial-optimization/matroids/matroid-intersection, math/combinatorial-optimization/polyhedra/ellipsoid-method]
status: draft
---

<!-- Added 2026-11-26 from MIT 18.433 (Spring 2015), lecture notes on matroid intersection (Section 6.4) and on the ellipsoid algorithm (the arborescence separation example), in our own wording; example our own (checked by brute force); proofs written out in steps. -->

Let $D=(V,A)$ be a digraph with a root $r$ (no arc enters $r$) and costs $c_a\ge0$. An $r$-arborescence (@exm-matroid-intersection-examples, item 2) is a set of $|V|-1$ arcs forming a spanning tree directed away from $r$. The *minimum cost arborescence problem* is a weighted matroid intersection problem, the directed analogue of the minimum spanning tree problem; but the greedy algorithm fails for it (exercise). A primal–dual algorithm in the style of the Hungarian method solves it.

For $S\subseteq V$, $\delta^-(S)$ is the set of arcs entering $S$. Every arborescence enters every $S\subseteq V\setminus\{r\}$, $S\ne\varnothing$, so consider the LP relaxation and its dual:
$$(P)\ \ \min\Big\{\sum_ac_ax_a:\ x(\delta^-(S))\ge1\ \ (\varnothing\ne S\subseteq V\setminus\{r\}),\ x\ge0\Big\},$$
$$(D)\ \ \max\Big\{\sum_Sy_S:\ \sum_{S:\,a\in\delta^-(S)}y_S\le c_a\ \ (a\in A),\ y\ge0\Big\}.$$
For an arborescence $T$ (with $x=\chi_T$) and a dual feasible $y$, complementary slackness (@thm-lp-complementary-slackness) asks for

1. $y_S>0\Rightarrow|T\cap\delta^-(S)|=1$, and
2. $a\in T\Rightarrow\sum_{S:\,a\in\delta^-(S)}y_S=c_a$ (the arc is *tight*).

::: {#def-arborescence-algorithm .definition name="Primal–dual arborescence algorithm"}

*Phase 1.* Start with $F=\varnothing$, $y=0$, $k=0$. While some vertex is not reachable from $r$ in $(V,F)$, choose a set $S\subseteq V\setminus\{r\}$ such that $F$ is strongly connected inside $S$ and no arc of $F$ enters $S$. Raise $y_S$ until some arc $a\in\delta^-(S)$ becomes tight; put $a_{k+1}=a$, add it to $F$ and increase $k$.

*Phase 2 (reverse delete).* For $i=k,k-1,\dots,1$: if $F-a_i$ still reaches every vertex from $r$, delete $a_i$ from $F$. Return $T=F$.

:::

A set $S$ as in Phase 1 exists: shrink the strong components of $(V,F)$; the resulting digraph is acyclic, and following entering arcs backwards from a component not reachable from $r$ ends at a component with no entering arc, which is not the one of $r$.

```{=latex}
\begin{algorithm}
\caption{Minimum cost arborescence (primal--dual)}
\begin{algorithmic}
\INPUT digraph $D=(V,A)$, root $r$, costs $c\ge0$
\OUTPUT a minimum cost $r$-arborescence $T$
\STATE $F\gets\varnothing$; $y\gets0$; $k\gets0$
\WHILE{some vertex is unreachable from $r$ in $(V,F)$}
\STATE $S\gets$ a strong component of $(V,F)$, not containing $r$, with $F\cap\delta^-(S)=\varnothing$
\STATE raise $y_S$ until an arc $a\in\delta^-(S)$ is tight; $k\gets k+1$; $a_k\gets a$; $F\gets F+a_k$
\ENDWHILE
\FOR{$i=k$ \TO $1$ \textbf{step} $-1$}
\IF{$F-a_i$ reaches every vertex from $r$} \STATE $F\gets F-a_i$ \ENDIF
\ENDFOR
\RETURN $T=F$
\end{algorithmic}
\end{algorithm}
```

::: {#thm-arborescence-algorithm .theorem name="The algorithm finds a minimum cost arborescence"}

The set $T$ returned is an $r$-arborescence, and $T$ and $y$ satisfy both complementary slackness conditions. Hence $T$ is optimal, and the LP (P) has an integral optimum.

:::

::: {.proof}

1. Phase 1 keeps $y$ dual feasible and every arc of $F$ tight, since $y_S$ is raised only until the first arc of $\delta^-(S)$ becomes tight, and that arc then joins $F$. So condition 2 holds for $T\subseteq F$.

2. *A rerouting fact.* When an arc $a_m$ is tested in Phase 2, the current $F$ contains $T$ (arcs are only deleted) and every $a_i$ with $i<m$ (not yet tested). So if $F-a_m$ reaches every vertex from $r$ at that moment, $a_m$ is deleted and $a_m\notin T$.

3. *$T$ is an arborescence.* Every vertex is reachable from $r$ in $T$. Suppose two arcs $a_i\ne a_m$ of $T$ enter the same vertex $v$. In $T$, the tail of one of them, say $a_i$, is reachable from $r$ by a path $Q$ avoiding $v$ (otherwise neither tail, and so not $v$, could be reached). When $a_m$ was tested, $F-a_m$ still contained $Q$ and $a_i$, so it reached $v$, and every path through $a_m$ could be rerouted through $Q$ and $a_i$. By step 2, $a_m\notin T$: a contradiction. So each $v\ne r$ has exactly one entering arc in $T$, $|T|=|V|-1$, and $T$ is an $r$-arborescence.

4. *Condition 1.* Let $y_S>0$ and let $a_k$ be the arc added when $S$ was processed. No arc of $F$ entered $S$ before, so every arc of $\delta^-(S)$ in $F$ has index $\ge k$; and $S$ is strongly connected using arcs $a_i$ with $i<k$. Let $s$ be the vertex of $S$ closest to $r$ in $T$; its tree path consists of a path $Q$ outside $S$ and one arc $e_0\in T\cap\delta^-(S)$. Suppose $T$ has another arc $a_m\in\delta^-(S)$, so $m\ge k$. When $a_m$ was tested, $F-a_m$ contained $Q$, $e_0$ and all $a_i$ with $i<k$, so it reached all of $S$; and any vertex reached by a path through $a_m$ is reached from the last vertex of $S$ on that path. By step 2, $a_m\notin T$: a contradiction. Thus $|T\cap\delta^-(S)|=1$.

5. By complementary slackness $\chi_T$ is optimal for (P) and $y$ for (D); since every arborescence is feasible for (P), $T$ is a minimum cost arborescence.

:::

::: {#exm-arborescence-small .example name="Three vertices"}

Let $V=\{r,a,b\}$ with arcs $ra$ (cost $4$), $rb$ ($5$), $ab$ ($1$), $ba$ ($1$).

1. $S=\{a\}$: raise $y_{\{a\}}$ to $1$, when $ba$ becomes tight; $a_1=ba$.
2. $S=\{b\}$: raise $y_{\{b\}}$ to $1$; $a_2=ab$.
3. Now $\{a,b\}$ is strongly connected with no entering arc of $F$: raise $y_{\{a,b\}}$ to $3$, when $ra$ becomes tight ($1+3=4$; $rb$ would need $4$ more); $a_3=ra$.
4. Reverse delete: $ra$ and $ab$ are needed; $ba$ is not, and is deleted.

So $T=\{ra,ab\}$ of cost $5$, equal to the dual value $1+1+3$. The other two arborescences, $\{ra,rb\}$ and $\{rb,ba\}$, cost $9$ and $6$.

:::

::: {#fig-arborescences-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA, rounded corners] (1.0,-0.45) rectangle (3.6,2.25);
\node[small vertex] (r) at (0,0.7) {$r$};
\node[small vertex] (a) at (1.6,1.4) {$a$};
\node[small vertex] (b) at (3.0,0) {$b$};
\draw[->, hl] (r) -- node[edge label] {$4$} (a);
\draw[->, faint] (r) -- node[edge label] {$5$} (b);
\draw[->, hl] (a) to[bend left=15] node[edge label] {$1$} (b);
\draw[->, faint] (b) to[bend left=15] node[edge label] {$1$} (a);
\node[lab, right] at (3.6,1.6) {$y_{\{a,b\}}=3$};
\node[lab, above] at (a.north) {$y_{\{a\}}=1$};
\node[lab, below] at (b.south) {$y_{\{b\}}=1$};
\end{tikzpicture}
\end{center}
```

The example: the dual values $y_{\{a\}}=y_{\{b\}}=1$ and $y_{\{a,b\}}=3$ (the shaded set) make the highlighted arborescence $\{ra,ab\}$ tight, and its cost $5$ equals the dual value.

:::

::: {#exm-arborescence-separation .example name="Solving (P) by the ellipsoid method"}

(P) has exponentially many constraints, but it has a fast separation oracle (@def-separation-oracle). Given $x^*$, return a violated $x_a\ge0$ if there is one. Otherwise, for each $t\ne r$ compute a minimum $r$–$t$ cut with capacities $x^*$ by a maximum flow (@thm-max-flow-min-cut). If some cut $\delta^-(S)$, $t\in S\subseteq V\setminus\{r\}$, has capacity less than $1$, it is a violated constraint; if none does, $x^*$ is feasible. So $|V|-1$ flow computations separate, and by @thm-optimization-from-separation the LP can be solved in polynomial time even without the combinatorial algorithm.

:::
