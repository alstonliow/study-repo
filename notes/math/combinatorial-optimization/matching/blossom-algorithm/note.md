---
title: "Edmonds' Blossom Algorithm"
sources: [mit18433-2]
requires: [math/combinatorial-optimization/matching/konig-theorem]
status: draft
---

<!-- Added 2026-11-26 from MIT 18.433 (Spring 2015), lecture notes on non-bipartite matching (Section 2, the upper bound, flowers and blossoms, the algorithm and its analysis), in our own wording; example our own (checked by computation); proofs written out in steps. -->

In a general graph $G=(V,E)$ a matching is still maximum exactly when there is no augmenting path (@thm-berge-augmenting-path), but finding one is harder: an alternating walk from an exposed vertex can run into an odd cycle and come back to itself. Edmonds' algorithm (1965) shrinks such cycles.

::: {#lem-tutte-berge-bound .lemma name="An upper bound from deleting vertices"}

For every matching $M$ and every $U\subseteq V$,
$$|M|\le\frac12\big(|V|+|U|-o(G-U)\big),$$
where $o(G-U)$ is the number of connected components of $G-U$ with an odd number of vertices.

:::

::: {.proof}

1. At most $|U|$ edges of $M$ have an end in $U$.

2. Every other edge of $M$ lies inside a component $K_i$ of $G-U$, and $K_i$ holds at most $\lfloor|K_i|/2\rfloor$ of them. So $|M|\le|U|+\sum_i\lfloor|K_i|/2\rfloor$.

3. $\sum_i\lfloor|K_i|/2\rfloor=\frac12\big(\sum_i|K_i|-o(G-U)\big)=\frac12\big(|V|-|U|-o(G-U)\big)$. Adding $|U|$ gives the bound.

:::

The Tutte–Berge formula (@thm-tutte-berge) says that some $U$ attains the bound; the algorithm below finds such a $U$.

::: {#def-flower-blossom .definition name="Flower, blossom, shrinking"}

Let $M$ be a matching. A *flower* consists of a *stem*, an even-length alternating path from an exposed vertex $u$ to a vertex $v$ (possibly $u=v$), and a *blossom* $B$: an odd cycle through $v$ whose edges alternate between $M$ and $E\setminus M$ except that the two edges at $v$ are both outside $M$. The *shrunk graph* $G/B$ replaces $B$ by one new vertex $b$, joins $b$ to every vertex outside $B$ that had a neighbour in $B$, and deletes the edges inside $B$. The matching $M/B$ is $M$ without its $\frac12(|B|-1)$ edges inside $B$.

:::

::: {#thm-blossom-shrinking .theorem name="Shrinking a blossom"}

If $B$ is a blossom with respect to $M$, then $M$ is a maximum matching of $G$ if and only if $M/B$ is a maximum matching of $G/B$.

:::

::: {.proof}

1. *Reduction to an empty stem.* If the stem $P$ is non-empty, replace $M$ by $M\triangle P$: it has the same size, $(M\triangle P)/B=(M/B)\triangle P$ has the same size as $M/B$, and now the flower has an empty stem. So assume $v=u$ is exposed; then $b$ is exposed in $G/B$.

2. *If $M/B$ is not maximum, neither is $M$.* Let $N$ be a larger matching of $G/B$. In $G$, the edges of $N$ meet $B$ in at most one vertex (the one replacing $b$, if $b$ is covered). Add $\frac12(|B|-1)$ edges of the odd cycle $B$ that cover all its other vertices. The result is a matching of $G$ of size $|N|+\frac12(|B|-1)>|M/B|+\frac12(|B|-1)=|M|$.

3. *If $M$ is not maximum, neither is $M/B$.* Take an augmenting path $P$ for $M$ in $G$. Only one vertex of $B$ is exposed, so one end of $P$, say $x$, lies outside $B$. If $P$ avoids $B$, it is augmenting in $G/B$. Otherwise let $w$ be the first vertex of $P$ in $B$; the part of $P$ from $x$ to $w$ becomes, after shrinking, an alternating path from $x$ to the exposed vertex $b$, an augmenting path for $M/B$.

:::

The proof is constructive: a larger matching of $G/B$ lifts to a larger matching of $G$. But a *maximum* matching of $G/B$ does not always lift to a maximum matching of $G$ by just adding edges inside $B$ (exercise); the algorithm therefore restarts its search after each augmentation.

::: {#def-blossom-algorithm .definition name="Edmonds' blossom algorithm"}

Label every exposed vertex *Even* and grow an *alternating forest* with these vertices as roots. Repeatedly take an Even vertex $u$ and an edge $uv$:

1. If $v$ is unlabelled, it is matched (exposed vertices are already Even); label $v$ *Odd* and its partner $w$ *Even*, and add $uv$, $vw$ to the tree of $u$.
2. If $v$ is Even and in another tree, the tree paths from $u$ and from $v$ to their roots, joined by $uv$, form an augmenting path. Augment, expand all shrunk blossoms (@thm-blossom-shrinking), and restart with the new matching.
3. If $v$ is Even and in the same tree, the tree paths from $u$ and $v$ together with $uv$ form a flower. Shrink its blossom into a vertex labelled Even and continue in the shrunk graph.

If no Even vertex has an edge of type 1, 2 or 3, stop: the current matching is maximum.

:::

```{=latex}
\begin{algorithm}
\caption{Edmonds' blossom algorithm}
\begin{algorithmic}
\INPUT graph $G$
\OUTPUT a maximum matching $M$
\STATE $M\gets\varnothing$
\LOOP
\STATE label exposed vertices Even, others unlabelled; $G'\gets G$
\WHILE{some Even $u$ has an edge $uv$ of type 1, 2 or 3 in $G'$}
\IF{$v$ unlabelled} \STATE label $v$ Odd and its partner Even
\ELSIF{$v$ Even, other tree} \STATE augment along the path; expand blossoms; \textbf{goto} next round
\ELSE \STATE shrink the blossom of $uv$ into one Even vertex of $G'$
\ENDIF
\ENDWHILE
\RETURN $M$ (expanded to $G$)
\ENDLOOP
\end{algorithmic}
\end{algorithm}
```

::: {#thm-blossom-algorithm .theorem name="Correctness and running time"}

Edmonds' algorithm returns a maximum matching in $O(|V|^2|E|)$ time. When it stops, the set $U$ of Odd vertices of the final shrunk graph $G'=(V',E')$ satisfies $|M'|=\frac12\big(|V'|+|U|-o(G'-U)\big)$.

:::

::: {.proof}

1. At the end, no edge joins two Even vertices (types 2 and 3) or an Even vertex to an unlabelled one (type 1). So in $G'-U$ every Even vertex is a component by itself, and $o(G'-U)\ge|\text{Even}|$; the remaining components consist of unlabelled vertices.

2. Each Odd vertex is matched to an Even one, every Even vertex other than a root is matched to an Odd one, and unlabelled vertices are matched among themselves. So $|M'|=|\text{Odd}|+\frac12(|V'|-|\text{Odd}|-|\text{Even}|)$.

3. Hence $\frac12(|V'|+|U|-o(G'-U))\le\frac12(|V'|+|\text{Odd}|-|\text{Even}|)=|M'|$, and by @lem-tutte-berge-bound equality holds and $M'$ is maximum in $G'$. Applying @thm-blossom-shrinking once per shrunk blossom, the expanded matching is maximum in $G$.

4. There are at most $|V|/2$ augmentations. Between two of them at most $|V|/2$ blossoms are shrunk, each removing at least $2$ vertices, and growing the forest between shrinkings takes $O(|E|)$ time. This gives $O(|V|^2|E|)$.

:::

::: {#exm-blossom-small .example name="Shrinking one blossom"}

Let $V=\{1,\dots,6\}$, $E=\{12,23,34,45,35,46\}$ and $M=\{23,45\}$, so $1$ and $6$ are exposed. Processing $1$: $2$ becomes Odd and $3$ Even. Processing $3$: $4$ becomes Odd and $5$ Even. Processing $5$: its neighbour $3$ is Even in the same tree, so $B=\{3,4,5\}$ is a blossom (stem $1$–$2$–$3$). In $G/B$ the edge $46$ becomes $b6$, and $1$–$2$–$b$–$6$ is augmenting. Lifted to $G$, the path enters $B$ at $4$ and goes round the even side to the base: $1$–$2$–$3$–$5$–$4$–$6$, and augmenting gives the perfect matching $\{12,35,46\}$.

:::

::: {#fig-blossom-algorithm-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (1.75,0) -- (3.25,0.85) -- (3.25,-0.85) -- cycle;
\node[small vertex, fill=accentLight, draw=accent] (b1) at (0,0) {$1$};
\node[small vertex] (b2) at (1,0) {$2$};
\node[small vertex] (b3) at (2,0) {$3$};
\node[small vertex] (b4) at (3,0.6) {$4$};
\node[small vertex] (b5) at (3,-0.6) {$5$};
\node[small vertex, fill=accentLight, draw=accent] (b6) at (4.2,0.6) {$6$};
\draw[faint] (b1) -- (b2);
\draw[bold] (b2) -- (b3);
\draw[faint] (b3) -- (b4);
\draw[bold] (b4) -- (b5);
\draw[faint] (b3) -- (b5);
\draw[faint] (b4) -- (b6);
\node[lab] at (2.75,-1.05) {blossom $B$};
\node[small vertex, fill=accentLight, draw=accent] (c1) at (6,0) {$1$};
\node[small vertex] (c2) at (7,0) {$2$};
\node[small vertex] (cb) at (8.1,0) {$b$};
\node[small vertex, fill=accentLight, draw=accent] (c6) at (9.2,0) {$6$};
\draw[hl] (c1) -- (c2);
\draw[hl] (c2) -- (cb);
\draw[hl] (cb) -- (c6);
\node[lab] at (7.6,-1.05) {$G/B$: augmenting path};
\end{tikzpicture}
\end{center}
```

The example: matching edges thick, exposed vertices $1$ and $6$ highlighted. The search from $1$ finds the blossom $B=\{3,4,5\}$; in $G/B$ the path $1$–$2$–$b$–$6$ is augmenting, and it lifts to $1$–$2$–$3$–$5$–$4$–$6$ in $G$.

:::

::: {#rmk-blossom-algorithm-1 .remark name="Faster versions and weights"}

The Micali–Vazirani algorithm finds a maximum matching in $O(\sqrt{|V|}\,|E|)$ time. A primal–dual version of the blossom algorithm, with duals on odd sets, solves the minimum weight perfect matching problem in general graphs; it rests on Edmonds' description of the matching polytope (@sec-cs-graph-optimization-minimum-t-odd-cut).

:::
