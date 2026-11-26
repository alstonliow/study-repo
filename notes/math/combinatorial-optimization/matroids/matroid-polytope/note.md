---
title: "The Matroid Polytope"
sources: [mit18433-5]
requires: [math/combinatorial-optimization/matroids/matroid-greedy, math/combinatorial-optimization/matroids/matroid-rank, math/combinatorial-optimization/polyhedra/combinatorial-polytopes]
status: draft
---

<!-- Added 2026-11-26 from MIT 18.433 (Spring 2015), lecture notes on matroid optimization (Sections 5.4 and 5.5), in our own wording; example our own (checked by computation); proofs written out in steps. Of the course's three proofs of the description we keep the algorithmic one and the vertex one (its chain theorem is reused for matroid intersection); the facet proof is summarised in a remark. Sufficiency of "closed and inseparable" for facets is stated without proof, as in the course. -->

Let $M=(E,\mathcal I)$ be a matroid with rank function $r$. The *matroid polytope* is the convex hull of the incidence vectors $\chi_S$ of its independent sets, and $x(S)=\sum_{e\in S}x_e$.

::: {#thm-matroid-polytope .theorem name="Description of the matroid polytope (Edmonds)"}

$$\operatorname{conv}\{\chi_S:S\in\mathcal I\}=P:=\{x\in\mathbb R^E:\ x(S)\le r(S)\ \text{for all } S\subseteq E,\ \ x\ge0\}.$$

:::

::: {.proof}

We use the algorithmic method (the first technique of @sec-math-combinatorial-optimization-polyhedra-combinatorial-polytopes). Each $\chi_I$ with $I\in\mathcal I$ lies in $P$, since $|I\cap S|\le r(S)$; so it suffices to show, for every $c\in\mathbb R^E$, an independent set and a dual solution of equal value. The dual of $\max\{c^{\mathsf T}x:x\in P\}$ is
$$\min\Big\{\sum_Sr(S)y_S:\ \sum_{S\ni e}y_S\ge c(e)\ \text{for all } e,\ y\ge0\Big\}.$$

1. Run the greedy algorithm (@def-matroid-greedy) on the elements of nonnegative weight; it returns $S_k=\{s_1,\dots,s_k\}$ of maximum weight (@thm-matroid-greedy). In the sorted order $e_1,e_2,\dots$, let $U_j$ be the set of elements before $s_{j+1}$ (for $j=k$, all elements of nonnegative weight).

2. $r(U_j)=j$: indeed $S_j\subseteq U_j$ gives $r(U_j)\ge j$, and an element $e\in U_j\setminus S_j$ with $S_j+e$ independent would have been taken by greedy (its set at that moment was a subset of $S_j$, @def-matroid-greedy with (I1)).

3. Put $y_{U_j}=c(s_j)-c(s_{j+1})\ge0$ for $j=1,\dots,k$, with $c(s_{k+1})=0$, and $y_S=0$ for all other $S$.

4. *Feasibility.* For an element $e$, let $t$ be the least index with $e\in U_t$ (if any). Then $\sum_{S\ni e}y_S=\sum_{j\ge t}y_{U_j}=c(s_t)\ge c(e)$, because $e$ comes no earlier than $s_t$ in the order. An element in no $U_j$ has $c(e)<0$, and its constraint holds trivially.

5. *Value.* $\sum_jr(U_j)y_{U_j}=\sum_{j=1}^kj\,(c(s_j)-c(s_{j+1}))=\sum_{j=1}^kc(s_j)=c(S_k)$.

:::

The second proof shows directly that every vertex of $P$ is integral; its key step, the chain structure of faces, is used again for the intersection of two matroids (@thm-matroid-intersection-polytope). Call $S$ *tight* for $x\in P$ if $x(S)=r(S)$.

::: {#lem-tight-sets-lattice .lemma name="Tight sets are closed under union and intersection"}

If $x\in P$ and $S$, $T$ are tight for $x$, so are $S\cap T$ and $S\cup T$.

:::

::: {.proof}

1. $x(\cdot)$ is modular: $x(S)+x(T)=x(S\cap T)+x(S\cup T)$.

2. Hence $r(S)+r(T)=x(S)+x(T)=x(S\cap T)+x(S\cup T)\le r(S\cap T)+r(S\cup T)\le r(S)+r(T)$, using $x\in P$ and then submodularity (@lem-matroid-rank-submodular).

3. So equality holds throughout, and as $x(S\cap T)\le r(S\cap T)$, $x(S\cup T)\le r(S\cup T)$, both are equalities.

:::

A *chain* is a family of sets totally ordered by inclusion.

::: {#thm-matroid-face-chain .theorem name="Faces of the matroid polytope are given by chains"}

For every face $F$ of $P$ there are a chain $\mathcal C$ and a set $J\subseteq E$ with
$$F=\{x\in P:\ x(C)=r(C)\ (C\in\mathcal C),\ x_e=0\ (e\in J)\}.$$

:::

::: {.proof}

1. By @thm-faces-tight-rows, $F=\{x\in P:x(S)=r(S)\ (S\in\mathcal F),\ x_e=0\ (e\in J)\}$, where $\mathcal F$ is the family of sets tight for every $x\in F$. It suffices to find a chain $\mathcal C\subseteq\mathcal F$ whose incidence vectors span the same linear space as those of $\mathcal F$; then the equations of $\mathcal F$ follow from those of $\mathcal C$.

2. Take a maximal chain $\mathcal C\subseteq\mathcal F$ and let $H$ be the span of $\{\chi_C:C\in\mathcal C\}$. Suppose some $S\in\mathcal F$ has $\chi_S\notin H$, and among such sets choose one minimising $|V(S)|$, where $V(S)=\{C\in\mathcal C:C\not\subseteq S,\ S\not\subseteq C\}$. By maximality of $\mathcal C$, $V(S)\ne\varnothing$.

3. Fix $C\in V(S)$. By @lem-tight-sets-lattice (applied to every $x\in F$), $C\cap S$ and $C\cup S$ are in $\mathcal F$. Since $\chi_C+\chi_S=\chi_{C\cap S}+\chi_{C\cup S}$ with $\chi_C\in H$, $\chi_S\notin H$, one of $B=C\cap S$, $B=C\cup S$ has $\chi_B\notin H$.

4. Every chain member comparable with $S$ is comparable with $B$, and $C$ itself is comparable with $B$. So $V(B)\subsetneq V(S)$, contradicting the choice of $S$.

:::

::: {#cor-matroid-polytope-integral .corollary name="Vertices of the matroid polytope"}

Every vertex of $P$ is the incidence vector of an independent set. This gives a second proof of @thm-matroid-polytope, by the vertex method.

:::

::: {.proof}

1. By @thm-vertex-unique-solution and @thm-matroid-face-chain, a vertex $x$ is the unique solution of $x(C_i)=r(C_i)$ for a chain $C_1\subsetneq\dots\subsetneq C_p$ and $x_e=0$ for $e\in J$. With $C_0=\varnothing$ the system is equivalent to $x(C_i\setminus C_{i-1})=r(C_i)-r(C_{i-1})$, $x_e=0$ ($e\in J$).

2. Uniqueness forces every $C_i\setminus C_{i-1}$ to contain at most one element outside $J$, and every element outside $J$ to lie in some $C_i$. So each $x_e$ is an integer difference of ranks.

3. As $0\le x_e\le r(\{e\})\le1$, $x=\chi_S$ for some $S$, and $|S|=x(S)\le r(S)\le|S|$, so $S$ is independent.

4. $P$ is bounded ($0\le x\le1$), so $P=\operatorname{conv}(\text{vertices})$ (@thm-minkowski-polytope) $\subseteq\operatorname{conv}\{\chi_S:S\in\mathcal I\}$.

:::

::: {#rmk-matroid-polytope-facet-proof .remark name="A third proof through facets"}

If every singleton is independent, $\operatorname{conv}(X)$ is full-dimensional ($0$ and the unit vectors are affinely independent). For a facet-defining $\alpha$ with all $\alpha_e\ge0$, let $S$ be the set of elements of largest weight $\alpha_e>0$. Every maximiser $I$ has $|I\cap S|=r(S)$: otherwise an element $e\in S$ could be exchanged, by the unique circuit property (@thm-unique-circuit), for an element $f\notin S$ of the circuit in $I+e$, increasing the weight. So the facet lies in the face $x(S)=r(S)$; if some $\alpha_e<0$ it lies in $x_e=0$.

:::

## Facets

Not all the $2^{|E|}$ rank inequalities are needed. Assume $r(\{e\})=1$ for all $e$. Then each $x_e\ge0$ defines a facet. The inequality $x(S)\le r(S)$ is implied by others if $S$ is not closed (use $x(\operatorname{span}S)\le r(S)$ and $x\ge0$), or if $S$ is *separable*: $S=U\cup(S\setminus U)$ with $\varnothing\ne U\ne S$ and $r(S)=r(U)+r(S\setminus U)$.

::: {#prp-matroid-polytope-facets .proposition name="Facets of the matroid polytope"}

When all singletons are independent, $x(S)\le r(S)$ defines a facet of the matroid polytope if and only if $S$ is closed and inseparable.

:::

We have shown necessity; sufficiency is not proved here.

::: {#exm-forest-polytope .example name="Partition, forest and spanning tree polytopes"}

1. For a partition matroid with all $k_i\ge1$, the closed inseparable sets are the parts $E_i$ with $|E_i|>k_i$ and the singletons, so the polytope is $\{x:x(E_i)\le k_i\ (|E_i|>k_i),\ 0\le x\le1\}$.
2. For a graphic matroid, a closed inseparable set is a single edge or $E(S)$ for a vertex set $S$ with $(S,E(S))$ $2$-connected. So the *forest polytope* is
$$\{x\in\mathbb R^E:\ x(E(S))\le|S|-1\ \text{for } S\subseteq V \text{ with } E(S)\ 2\text{-connected or } |S|=2,\ \ 0\le x\le1\}.$$
3. The *spanning tree polytope* of a connected graph is its face $x(E)=|V|-1$. For the triangle, it is the triangle in $\mathbb R^3$ with vertices $(1,1,0)$, $(1,0,1)$, $(0,1,1)$: the conditions are $x_1+x_2+x_3=2$ and $0\le x_e\le1$.

:::

::: {#fig-matroid-polytope-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0,0) -- (1.6,0) -- (0,1.6) -- cycle; \draw[emph] (0,0) -- (1.6,0) -- (0,1.6) -- cycle;
\draw[->, faint] (0,0) -- (2.1,0) node[lab, right] {$x_1$}; \draw[->, faint] (0,0) -- (0,2.1) node[lab, above] {$x_2$};
\node[lab] at (0.8,-0.5) {two parallel edges};
\node[lab, right] at (0.9,1.0) {$x_1+x_2\le1$};
\fill[tintA] (4,0) rectangle (5.6,1.6); \draw[emph] (4,0) rectangle (5.6,1.6);
\draw[->, faint] (4,0) -- (6.1,0) node[lab, right] {$x_1$}; \draw[->, faint] (4,0) -- (4,2.1) node[lab, above] {$x_2$};
\node[lab] at (4.8,-0.5) {a path of two edges};
\end{tikzpicture}
\end{center}
```

Matroid polytopes of two graphic matroids with two edges. For parallel edges (a cycle of length $2$) the rank inequality $x_1+x_2\le r(\{1,2\})=1$ cuts the square to a triangle; for a path both edges together are independent and the polytope is the whole unit square.

:::
