---
title: "Matroid Intersection"
sources: [mit18433-6]
requires: [math/combinatorial-optimization/matroids/matroid-rank]
status: draft
---

<!-- Added 2026-11-26 from MIT 18.433 (Spring 2015), lecture notes on matroid intersection (Sections 6.1 and 6.2), in our own wording; example our own (checked by computation); proofs written out in steps. The exchange-graph matching lemma and the two corollaries for orientations and colourful trees are stated without proof, as in the course. -->

The greedy algorithm solves optimisation over one matroid, but most problems are not of that form. Many are, however, problems over the sets independent in *two* matroids $M_1=(E,\mathcal I_1)$ and $M_2=(E,\mathcal I_2)$ on the same ground set: the *matroid intersection* $\mathcal I_1\cap\mathcal I_2$ (which is usually not a matroid).

::: {#exm-matroid-intersection-examples .example name="Problems that are matroid intersections"}

1. *Bipartite matchings.* For a bipartite graph with sides $A$, $B$, let $M_A$ be the partition matroid with parts $\delta(v)$, $v\in A$, each with bound $1$, and $M_B$ the same for $B$. The common independent sets are exactly the matchings.
2. *Arborescences.* In a digraph $D=(V,A)$ with root $r$ (and no arc into $r$), an *$r$-arborescence* is a spanning tree of the underlying graph directed away from $r$. Take $M_1$ the graphic matroid of the underlying graph and $M_2$ the partition matroid allowing at most one arc into each $v\ne r$. The common independent sets of size $|V|-1$ are exactly the $r$-arborescences: in such a spanning tree the path from $r$ to any $v$ must be directed away from $r$, since otherwise some vertex would have two entering arcs or $r$ one.
3. *Orientations with indegree bounds.* Replace each edge $\{u,v\}$ of $G$ by the two arcs $(u,v)$, $(v,u)$. With $M_1$ allowing at most one arc of each pair and $M_2$ at most $k(v)$ arcs into each $v$, an orientation with indegrees at most $k$ is a common independent set of size $|E|$.
4. *Colourful spanning trees.* If the edges of $G$ are coloured, a spanning tree with all colours distinct is a base of $M(G)$ independent in the partition matroid with parts the colour classes and bounds $1$.

:::

::: {#prp-matroid-intersection-weak .proposition name="Weak duality for matroid intersection"}

If $r_1,r_2$ are the rank functions, then for every $S\in\mathcal I_1\cap\mathcal I_2$ and every $U\subseteq E$,
$$|S|\le r_1(U)+r_2(E\setminus U).$$

:::

::: {.proof}

$S\cap U$ is independent in $M_1$ and $S\setminus U$ in $M_2$ (by (I1)), so $|S|=|S\cap U|+|S\setminus U|\le r_1(U)+r_2(E\setminus U)$.

:::

::: {#thm-matroid-intersection .theorem name="Matroid intersection theorem (Edmonds)"}

$$\max_{S\in\mathcal I_1\cap\mathcal I_2}|S|=\min_{U\subseteq E}\big(r_1(U)+r_2(E\setminus U)\big).$$

:::

The minimum may be taken over sets $U$ closed in $M_1$ (replacing $U$ by $\operatorname{span}_1(U)$ keeps $r_1$ and does not increase $r_2(E\setminus U)$). Specialised to the examples, the theorem gives:

::: {#cor-orientation-indegree .corollary name="Orientations with bounded indegree"}

A graph $G=(V,E)$ has an orientation in which every $v$ has indegree at most $k(v)$ if and only if $|E(P)|\le\sum_{v\in P}k(v)$ for every $P\subseteq V$.

:::

::: {#cor-colourful-spanning-tree .corollary name="Colourful spanning trees"}

A connected graph whose edges are coloured with colours $1,\dots,k$ has a spanning tree with all edges of different colours if and only if, for every $c$, deleting the edges of any $c$ colours leaves at most $c+1$ components.

:::

The proof of the theorem is an augmenting path algorithm on the following graph.

::: {#def-exchange-graph .definition name="Exchange graph"}

For a matroid $M$ and $S\in\mathcal I$, the *exchange graph* $G_M(S)$ is the bipartite graph on $S$ and $E\setminus S$ with an edge $yx$ ($y\in S$, $x\notin S$) whenever $S-y+x\in\mathcal I$. For two matroids and $S\in\mathcal I_1\cap\mathcal I_2$, the directed exchange graph $D(S)$ has an arc $(y,x)$ if $S-y+x\in\mathcal I_1$ and an arc $(x,y)$ if $S-y+x\in\mathcal I_2$. Its *sources* are $X_1=\{x\notin S:S+x\in\mathcal I_1\}$ and its *sinks* $X_2=\{x\notin S:S+x\in\mathcal I_2\}$.

:::

If $|S|=|T|$ and both are independent, $G_M(S)$ has a perfect matching between $S\setminus T$ and $T\setminus S$; this is not proved here. We need a partial converse.

::: {#prp-unique-matching-independent .proposition name="A unique exchange matching gives an independent set"}

Let $S\in\mathcal I$ and $|T|=|S|$. If $G_M(S)$ has exactly one perfect matching between $S\setminus T$ and $T\setminus S$, then $T\in\mathcal I$.

:::

::: {.proof}

1. Let $N$ be the unique matching. Orient its edges from $T\setminus S$ to $S\setminus T$ and all other edges between these sets the other way. A directed cycle would alternate between $N$ and non-$N$ edges and give a second perfect matching, so the graph is acyclic.

2. A topological order lets us number $N=\{y_1x_1,\dots,y_tx_t\}$ so that $y_ix_j$ is never an edge for $i<j$.

3. Suppose $T$ is dependent and let $C\subseteq T$ be a circuit. It meets $T\setminus S$, as $S$ is independent; let $i$ be least with $x_i\in C$.

4. For every $x\in C-x_i$, either $x\in S\cap T$, or $x=x_j$ with $j>i$ and then $y_ix$ is not an edge, meaning $S-y_i+x\notin\mathcal I$, so $x\in\operatorname{span}(S-y_i)$. Either way $C-x_i\subseteq\operatorname{span}(S-y_i)$.

5. As $C$ is a circuit, $x_i\in\operatorname{span}(C-x_i)\subseteq\operatorname{span}(S-y_i)$ (spans are monotone and $\operatorname{span}\operatorname{span}=\operatorname{span}$, @prp-span-same-rank). So $S-y_i+x_i\notin\mathcal I$, contradicting the edge $y_ix_i$.

:::

::: {#def-matroid-intersection-algorithm .definition name="Matroid intersection algorithm"}

Start with $S=\varnothing$. Repeat: build $D(S)$. If it has a path from $X_1$ to $X_2$, take a shortest one $P$ (it has no *shortcuts*, arcs from a vertex of $P$ to a later non-consecutive vertex of $P$) and replace $S$ by $S\triangle P$, where $P$ is read as its vertex set. Otherwise stop, and return $S$ together with $U$, the set of elements of $E$ from which $X_2$ can be reached in $D(S)$.

:::

```{=latex}
\begin{algorithm}
\caption{Matroid intersection}
\begin{algorithmic}
\INPUT matroids $M_1,M_2$ on $E$ with independence tests
\OUTPUT $S\in\mathcal I_1\cap\mathcal I_2$ of maximum size and $U$ with $|S|=r_1(U)+r_2(E\setminus U)$
\STATE $S\gets\varnothing$
\LOOP
\STATE build $D(S)$, $X_1$, $X_2$
\IF{there is no path from $X_1$ to $X_2$}
\STATE $U\gets\{z\in E: z \text{ reaches } X_2\}$; \RETURN $S,U$
\ENDIF
\STATE $P\gets$ a shortest path from $X_1$ to $X_2$; $S\gets S\triangle P$
\ENDLOOP
\end{algorithmic}
\end{algorithm}
```

::: {#thm-matroid-intersection-algorithm .theorem name="Correctness of the algorithm"}

Each step keeps $S\in\mathcal I_1\cap\mathcal I_2$ and increases $|S|$ by one, and at the end $|S|=r_1(U)+r_2(E\setminus U)$. This proves @thm-matroid-intersection; the algorithm makes at most $r_1(E)$ augmentations, each with $O(|S|\,|E|)$ independence tests.

:::

::: {.proof}

*Optimality at the end.*

1. $X_2\subseteq U$ by definition, and $X_1\cap U=\varnothing$ since no path from $X_1$ to $X_2$ exists. We show $r_1(U)=|S\cap U|$ and $r_2(E\setminus U)=|S\setminus U|$; adding gives the equality.

2. If $|S\cap U|<r_1(U)$, some $x\in U\setminus S$ has $(S\cap U)+x\in\mathcal I_1$. Extend $(S\cap U)+x$ by elements of $S$ to an independent set of size $|S|$ (possible as $S\in\mathcal I_1$, by (I2)). If this uses all of $S$ then $S+x\in\mathcal I_1$, so $x\in X_1\cap U$, impossible. Otherwise it is $S-y+x$ for some $y\in S\setminus U$, giving the arc $(y,x)$; since $x$ reaches $X_2$, so does $y$, contradicting $y\notin U$.

3. Symmetrically, if $|S\setminus U|<r_2(E\setminus U)$, some $x\in(E\setminus U)\setminus S$ has $(S\setminus U)+x\in\mathcal I_2$. As before either $S+x\in\mathcal I_2$, so $x\in X_2\subseteq U$, impossible; or $S-y+x\in\mathcal I_2$ for some $y\in S\cap U$, giving the arc $(x,y)$, so $x$ reaches $X_2$ through $y$ and $x\in U$: a contradiction.

*Each augmentation stays independent.* Let $P=x_0,y_1,x_1,\dots,y_t,x_t$ be a shortest path, $x_0\in X_1$, $x_t\in X_2$.

4. Add a new element $t_0$ to $M_1$ that is independent of everything (a coloop): $M_1'$ has independent sets $\{J:J-t_0\in\mathcal I_1\}$. Then $S+t_0\in\mathcal I(M_1')$, and in $G_{M_1'}(S+t_0)$ the pairs $t_0x_0$, $y_1x_1$, …, $y_tx_t$ are edges: $t_0x_0$ because $S+x_0\in\mathcal I_1$, and the others are arcs of $P$.

5. Since $P$ is shortest, no $y_i$ is joined to an $x_j$ with $j>i$ (that arc would shorten $P$), and $t_0$ is joined to no $x_j$ with $j>0$ (that would give a shorter path from $X_1$). So this is the unique perfect matching between $\{t_0,y_1,\dots,y_t\}$ and $\{x_0,\dots,x_t\}$, and by @prp-unique-matching-independent $(S+t_0)\triangle\{t_0,x_0,y_1,\dots,x_t\}=S\triangle P$ is independent in $M_1$.

6. The same argument with a coloop added to $M_2$, matched to the last vertex $x_t$, shows $S\triangle P\in\mathcal I_2$. As $P$ has one more element outside $S$ than inside, $|S\triangle P|=|S|+1$.

:::

::: {#exm-matroid-intersection-run .example name="The algorithm on a bipartite matching instance"}

Use the two partition matroids of a bipartite graph with $A=\{1,2,3\}$, $B=\{4,5,6\}$ and edges $14,24,34,35,36$ (example 1 above).

1. From $S=\{34\}$: the sources are the edges at the free vertices $1,2$ of $A$, so $X_1=\{14,24\}$; the sinks are the edges at the free vertices $5,6$ of $B$, $X_2=\{35,36\}$. The arcs $(14,34)$ (as $S-34+14=\{14\}\in\mathcal I_2$) and $(34,35)$ (as $\{35\}\in\mathcal I_1$) give the path $14,34,35$, and $S\triangle P=\{14,35\}$.
2. From $S=\{14,35\}$: $X_1=\{24\}$ and $X_2=\{36\}$. The only arcs out of $24$ and $14$ lead to each other, so no path exists. The elements reaching $X_2$ are $U=\{35,36\}$ (via the arc $(35,36)$), and $r_1(U)+r_2(E\setminus U)=1+1=2=|S|$: here $r_1(U)$ counts the $A$-vertices of $U$ (only $3$) and $r_2(\{14,24,34\})$ the $B$-vertices (only $4$). This is König's cover $\{3,4\}$ of @exm-konig-cover.

:::

::: {#fig-matroid-intersection-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (y) at (1.6,0.9) {$34$};
\node[small vertex, fill=accentLight, draw=accent] (x14) at (0,-0.6) {$14$};
\node[small vertex] (x24) at (1.07,-0.6) {$24$};
\node[small vertex, fill=accentLight, draw=accent] (x35) at (2.13,-0.6) {$35$};
\node[small vertex] (x36) at (3.2,-0.6) {$36$};
\draw[->, hl] (x14) to[bend left=12] (y);
\draw[->, hl] (y) to[bend left=12] (x35);
\draw[->, faint] (y) to[bend left=12] (x14); \draw[->, faint] (y) to[bend left=12] (x24); \draw[->, faint] (x24) to[bend left=12] (y);
\draw[->, faint] (x35) to[bend left=12] (y); \draw[->, faint] (y) to[bend left=12] (x36); \draw[->, faint] (x36) to[bend left=12] (y);
\node[lab] at (-0.2,-1.15) {source}; \node[lab] at (2.13,-1.15) {sink};
\node[lab] at (3.2,-1.15) {sink}; \node[lab] at (1.07,-1.15) {source};
\end{tikzpicture}
\end{center}
```

The exchange graph $D(S)$ for $S=\{34\}$ in the example: sources $14,24$, sinks $35,36$. The shortest path $14\to34\to35$ (highlighted) gives the larger common independent set $\{14,35\}$.

:::
