---
title: "Matroid Duality and Matroid Union"
sources: [mit18433-6]
requires: [math/combinatorial-optimization/matroids/matroid-intersection]
status: draft
---

<!-- Added 2026-11-26 from MIT 18.433 (Spring 2015), lecture notes on matroid intersection (Section 6.5), in our own wording; example our own (checked by computation); proofs written out in steps. The dual matroid's rank formula and the k-tree theorem are stated here; their proofs are exercises (prob-mit18433ps-6-q1, prob-mit18433-6-q3). -->

::: {#def-dual-matroid .definition name="Dual matroid"}

The *dual* of a matroid $M=(E,\mathcal I)$ is $M^*=(E,\mathcal I^*)$ with
$$\mathcal I^*=\{X\subseteq E:\ E\setminus X\ \text{contains a base of } M\}.$$

:::

::: {#thm-dual-matroid-rank .theorem name="The dual is a matroid"}

$M^*$ is a matroid, its bases are the complements of the bases of $M$, and its rank function is
$$r_{M^*}(X)=|X|+r_M(E\setminus X)-r_M(E).$$

:::

The proof is an exercise. For a connected plane graph, the dual of the graphic matroid is the graphic matroid of the planar dual graph: complements of spanning trees correspond to spanning trees of the dual.

::: {#thm-two-disjoint-spanning-trees .theorem name="Two edge-disjoint spanning trees"}

A graph $G=(V,E)$ has two edge-disjoint spanning trees if and only if every partition of $V$ into $p$ classes $V_1,\dots,V_p$ has at least $2(p-1)$ edges joining different classes:
$$|\delta(V_1,\dots,V_p)|\ge2(p-1).$$

:::

::: {.proof}

1. Necessity: each spanning tree has at least $p-1$ edges between the classes, since contracting the classes leaves a connected graph on $p$ vertices.

2. Sufficiency. If $G$ is disconnected, the partition into its $p\ge2$ components has no edges between classes, so the condition fails; hence assume $G$ connected. Let $M=M(G)$, with $r(F)=n-\kappa(F)$ and $n=|V|$. Two edge-disjoint spanning trees exist iff some spanning tree $S$ has a spanning tree inside $E\setminus S$, that is, iff $\max\{|S|:S\in\mathcal I\cap\mathcal I^*\}=n-1$.

3. By the matroid intersection theorem (@thm-matroid-intersection) and @thm-dual-matroid-rank (with $r(E)=n-1$),
$$\max_{S\in\mathcal I\cap\mathcal I^*}|S|=\min_{E_1\subseteq E}\big[(n-\kappa(E_1))+|E\setminus E_1|+(n-\kappa(E_1))-(n-1)\big]=\min_{E_1}\big[n+1+|E\setminus E_1|-2\kappa(E_1)\big].$$
So two disjoint spanning trees exist iff $|E\setminus E_1|\ge2(\kappa(E_1)-1)$ for every $E_1\subseteq E$.

4. This condition is equivalent to the partition condition. Given a partition, $E_1=E\setminus\delta(V_1,\dots,V_p)$ has $\kappa(E_1)\ge p$, so $|\delta(V_1,\dots,V_p)|=|E\setminus E_1|\ge2(\kappa(E_1)-1)\ge2(p-1)$. Conversely, given $E_1$, let $V_1,\dots,V_p$ be the components of $(V,E_1)$, so $p=\kappa(E_1)$; no edge of $E_1$ joins two components, so $|E\setminus E_1|\ge|\delta(V_1,\dots,V_p)|\ge2(p-1)$.

:::

More generally, $G$ has $k$ edge-disjoint spanning trees if and only if $|\delta(V_1,\dots,V_p)|\ge k(p-1)$ for every partition (Nash-Williams and Tutte); this follows from the union theorem below (exercise).

::: {#thm-matroid-union .theorem name="Matroid union"}

For matroids $M_1=(E,\mathcal I_1)$ and $M_2=(E,\mathcal I_2)$, the family $\mathcal I=\{S_1\cup S_2:S_1\in\mathcal I_1,\ S_2\in\mathcal I_2\}$ is the family of independent sets of a matroid $M_1\vee M_2$, whose rank function is
$$r_{M_1\vee M_2}(S)=\min_{F\subseteq S}\big(|S\setminus F|+r_1(F)+r_2(F)\big).$$

:::

::: {.proof}

*It is a matroid.* (I1) is clear.

1. Let $X,Y\in\mathcal I$, $|X|<|Y|$. Write $X=X_1\cup X_2$, $Y=Y_1\cup Y_2$ with $X_i,Y_i\in\mathcal I_i$, $X_1\cap X_2=\varnothing=Y_1\cap Y_2$, choosing these decompositions to maximise $|X_1\cap Y_1|+|X_2\cap Y_2|$.

2. As $|Y|>|X|$, we may assume $|Y_1|>|X_1|$, so some $e\in Y_1\setminus X_1$ has $X_1+e\in\mathcal I_1$.

3. If $e\in X_2$, the decomposition $X_1+e$, $X_2-e$ of $X$ has a larger value of $|X_1\cap Y_1|+|X_2\cap Y_2|$ (it gains $e$ in $X_1\cap Y_1$ and loses nothing, as $e\notin Y_2$): impossible. So $e\notin X$, and $X+e=(X_1+e)\cup X_2\in\mathcal I$.

*The rank formula.*

4. $\le$: for $S'\in\mathcal I$ with $S'\subseteq S$ and any $F\subseteq S$, $|S'|=|S'\setminus F|+|S'\cap F|\le|S\setminus F|+r_1(F)+r_2(F)$, since $S'\cap F$ is a union of a set independent in $M_1$ and one in $M_2$.

5. $\ge$: restricting both matroids to $S$, it suffices to treat $S=E$. Let $X=X_1\cup X_2$ be a base of $M_1\vee M_2$ with $X_1\cap X_2=\varnothing$; enlarging $X_2$ (and removing the added elements from $X_1$) we may assume $X_2$ is a base of $M_2$. Then $E\setminus X_1\supseteq X_2$ contains a base of $M_2$, so $X_1\in\mathcal I_1\cap\mathcal I_2^*$, and conversely any such $X_1$ gives the independent set $X_1\cup B_2$ of size $|X_1|+r_2(E)$ for a base $B_2\subseteq E\setminus X_1$.

6. Hence, by @thm-matroid-intersection and @thm-dual-matroid-rank,
$$r_{M_1\vee M_2}(E)=r_2(E)+\max_{X_1\in\mathcal I_1\cap\mathcal I_2^*}|X_1|=r_2(E)+\min_{F}\big(r_1(F)+|E\setminus F|+r_2(F)-r_2(E)\big),$$
which is the formula.

:::

The rank function of a union is submodular, as for any matroid, although the formula does not show it.

::: {#thm-spanning-tree-game .theorem name="The spanning tree game"}

Two players alternate on a graph $G$; player 1 starts. Player 1 deletes an edge not yet fixed; player 2 fixes an edge not yet deleted. Player 2 wins if the fixed edges eventually contain a spanning tree. Player 2 has a winning strategy if and only if $G$ has two edge-disjoint spanning trees; otherwise player 1 has one.

:::

::: {.proof}

1. If $G$ has no two edge-disjoint spanning trees, @thm-two-disjoint-spanning-trees gives a partition with $|\delta(V_1,\dots,V_p)|\le2(p-1)-1$. Player 1 always deletes an edge of $\delta(V_1,\dots,V_p)$. Player 1 moves first, so these edges run out before player 2 has fixed $p-1$ of them, and the fixed edges cannot connect the $p$ classes.

2. The strategy for player 2 when two disjoint spanning trees exist is an exercise.

:::

::: {#exm-two-spanning-trees-k4 .example name="$K_4$ and the triangle"}

$K_4$ has $6=2(4-1)$ edges and two edge-disjoint spanning trees, the paths $1$–$2$–$3$–$4$ and $3$–$1$–$4$–$2$. The triangle has only $3<2\cdot2$ edges; the partition into singletons gives $|\delta|=3<2(3-1)=4$, so player 1 wins the spanning tree game on it.

:::

::: {#fig-matroid-union-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (k1) at (0,1.5) {$1$};
\node[small vertex] (k2) at (1.5,1.5) {$2$};
\node[small vertex] (k3) at (1.5,0) {$3$};
\node[small vertex] (k4) at (0,0) {$4$};
\draw[hl] (k1) -- (k2);
\draw[hl] (k2) -- (k3);
\draw[hl] (k3) -- (k4);
\draw[emph, dashed] (k3) -- (k1);
\draw[emph, dashed] (k1) -- (k4);
\draw[emph, dashed] (k4) -- (k2);
\end{tikzpicture}
\end{center}
```

$K_4$ as the union of two edge-disjoint spanning trees: the path $1$–$2$–$3$–$4$ (highlighted) and the path $3$–$1$–$4$–$2$ (dashed).

:::
