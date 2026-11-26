---
title: "Minimum T-Odd Cuts"
sources: [mit18433-4, mit18433-7]
requires: [cs/graph-optimization/global-minimum-cut, math/combinatorial-optimization/polyhedra/ellipsoid-method]
status: draft
---

<!-- Added 2026-11-26 from MIT 18.433 (Spring 2015), lecture notes on flows and cuts (Section 4.5) and on the ellipsoid algorithm (the matching separation example), in our own wording; example our own (checked by brute force over all cuts); proofs written out in steps. Edmonds' description of the matching polytope is stated without proof, as in the course. -->

Let $G=(V,E)$ be undirected with capacities $u\ge0$, and let $T\subseteq V$ have even size. A set $S\subseteq V$ is *$T$-odd* if $|S\cap T|$ is odd; then $V\setminus S$ is $T$-odd too. The *minimum $T$-odd cut problem* asks for a $T$-odd $S$ minimising $u(\delta(S))$. It is the separation problem for the matching polytope (@exm-matching-polytope-separation).

::: {#lem-cut-submodular .lemma name="The cut function is submodular"}

For all $A,B\subseteq V$,
$$u(\delta(A))+u(\delta(B))\ge u(\delta(A\cap B))+u(\delta(A\cup B)).$$

:::

::: {.proof}

1. Compare the contribution of one edge $e=xy$ to both sides. Each side counts $e$ once for each set (of the two on that side) that separates $x$ from $y$.

2. If $e$ is counted on the right for $A\cap B$, say $x\in A\cap B$ and $y\notin A\cap B$, then $y\notin A$ or $y\notin B$, so $e\in\delta(A)$ or $e\in\delta(B)$. Similarly an edge of $\delta(A\cup B)$ lies in $\delta(A)$ or $\delta(B)$.

3. If $e$ is counted twice on the right, then (up to swapping $x,y$) $x\in A\cap B$ and $y\notin A\cup B$, so $e$ lies in both $\delta(A)$ and $\delta(B)$ and is counted twice on the left as well. With $u\ge0$ the inequality follows.

:::

::: {#lem-t-odd-uncrossing .lemma name="Uncrossing"}

Let $S$ minimise $u(\delta(S))$ among the sets with $\varnothing\ne S\cap T\ne T$, and suppose $|S\cap T|$ is even. Then some minimum $T$-odd cut $A$ satisfies $A\subseteq S$ or $A\subseteq V\setminus S$.

:::

::: {.proof}

1. Let $B$ be a minimum $T$-odd cut and split $T$ into $T_1=T\setminus(B\cup S)$, $T_2=(T\cap S)\setminus B$, $T_3=T\cap B\cap S$, $T_4=(T\cap B)\setminus S$.

2. Since $S$ and $B$ both separate $T$, the sets $T_1\cup T_2$, $T_2\cup T_3$, $T_3\cup T_4$, $T_4\cup T_1$ are non-empty. Hence $T_1,T_3\ne\varnothing$ or $T_2,T_4\ne\varnothing$; replacing $B$ by $V\setminus B$ swaps these cases, so assume $T_1,T_3\ne\varnothing$.

3. Then $S\cap B$ (containing $T_3$, missing $T_1$) and $S\cup B$ (missing $T_1$) both separate $T$. Also $|(S\cap B)\cap T|+|(S\cup B)\cap T|=|S\cap T|+|B\cap T|$ is odd, so exactly one of them is $T$-odd and the other separates $T$.

4. By @lem-cut-submodular, $u(\delta(S))+u(\delta(B))\ge u(\delta(S\cap B))+u(\delta(S\cup B))$. The $T$-separating one of the two has cut value at least $u(\delta(S))$ by the choice of $S$, so the $T$-odd one has cut value at most $u(\delta(B))$, and is a minimum $T$-odd cut.

5. $S\cap B\subseteq S$, and $S\cup B$ has complement $V\setminus(S\cup B)\subseteq V\setminus S$, also a minimum $T$-odd cut.

:::

::: {#def-t-odd-cut-algorithm .definition name="Algorithm for minimum $T$-odd cuts"}

$\mathrm{ALG}(G,T)$: fix $s\in T$ and compute a minimum $s$–$t$ cut for every $t\in T-s$; let $S$ be the best of these $|T|-1$ cuts (a minimum cut separating $T$). If $S$ is $T$-odd, return it. Otherwise return the better of $\mathrm{ALG}(G/S,\,T\setminus S)$ and $\mathrm{ALG}(G/(V\setminus S),\,T\cap S)$, where $G/X$ shrinks $X$ to a single vertex (not in $T$).

:::

```{=latex}
\begin{algorithm}
\caption{Minimum $T$-odd cut}
\begin{algorithmic}
\INPUT undirected $G$ with capacities $u\ge0$, $T\subseteq V$ with $|T|\ge2$ even
\OUTPUT a minimum $T$-odd cut
\STATE fix $s\in T$; $S\gets$ the smallest minimum $s$--$t$ cut over $t\in T-s$
\IF{$|S\cap T|$ is odd} \RETURN $S$ \ENDIF
\STATE $A_1\gets\mathrm{ALG}(G/S,\ T\setminus S)$; $A_2\gets\mathrm{ALG}(G/(V\setminus S),\ T\cap S)$
\RETURN the better of $A_1$, $A_2$ (expanded to $G$)
\end{algorithmic}
\end{algorithm}
```

::: {#thm-t-odd-cut-algorithm .theorem name="Correctness and running time"}

$\mathrm{ALG}(G,T)$ returns a minimum $T$-odd cut using at most $|T|^2$ minimum $s$–$t$ cut computations.

:::

::: {.proof}

1. *Correctness.* If $S$ is $T$-odd it is optimal, since every $T$-odd cut separates $T$. Otherwise, by @lem-t-odd-uncrossing some minimum $T$-odd cut lies inside $V\setminus S$ or inside $S$, so it survives as a $T\setminus S$-odd cut of $G/S$ or a $T\cap S$-odd cut of $G/(V\setminus S)$, with the same value. Both parts of $T$ are even and non-empty (so of size at least $2$), and the cuts of the shrunk graphs are cuts of $G$; by induction the better recursive answer is optimal.

2. *Count.* Let $R(k)$ bound the number of $s$–$t$ cut computations when $|T|=k$. Then $R(2)=1$ and $R(k)\le(k-1)+\max\{R(k_1)+R(k_2):k_1+k_2=k,\ k_1,k_2\ge2\}$. If $R(j)\le j^2$ for smaller $j$, then $R(k)\le(k-1)+4+(k-2)^2=k^2-3k+7\le k^2$ for $k\ge4$ (the sum of squares is largest at $k_1=2$).

:::

::: {#exm-t-odd-cut-cycle .example name="A $4$-cycle"}

Take the cycle $1$–$2$–$3$–$4$–$1$ with $u_{12}=u_{34}=1$, $u_{23}=u_{41}=3$, and $T=V$. The minimum cut separating $T$ is $S=\{1,4\}$ of value $2$, but $|S\cap T|=2$ is even. Shrinking $\{1,4\}$ to $x$ gives the triangle $x,2,3$ with $u_{x2}=u_{x3}=1$, $u_{23}=3$ and $T=\{2,3\}$, whose minimum cut separating $2$ and $3$ has value $4$ (for instance $\{2\}$); the other branch is symmetric. So the minimum $T$-odd cut has value $4$, attained by every single vertex, as checking all $T$-odd sets confirms.

:::

::: {#fig-minimum-t-odd-cut-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA, rounded corners] (-0.4,-0.4) rectangle (0.4,1.8);
\node[small vertex] (o1) at (0,1.4) {$1$};
\node[small vertex] (o2) at (1.6,1.4) {$2$};
\node[small vertex] (o3) at (1.6,0) {$3$};
\node[small vertex] (o4) at (0,0) {$4$};
\draw[emph] (o1) -- node[edge label] {$1$} (o2);
\draw[emph] (o2) -- node[edge label] {$3$} (o3);
\draw[emph] (o3) -- node[edge label] {$1$} (o4);
\draw[emph] (o4) -- node[edge label] {$3$} (o1);
\node[lab] at (0,2.05) {$S$};
\node[small vertex] (px) at (3.4,0.7) {$x$};
\node[small vertex] (p2) at (5,1.4) {$2$};
\node[small vertex] (p3) at (5,0) {$3$};
\draw[emph] (px) -- node[edge label] {$1$} (p2);
\draw[emph] (p2) -- node[edge label] {$3$} (p3);
\draw[emph] (px) -- node[edge label] {$1$} (p3);
\node[lab] at (4.2,-0.6) {$G/S$, $T=\{2,3\}$};
\end{tikzpicture}
\end{center}
```

The example: the cheapest cut separating $T$ is $S=\{1,4\}$ (shaded, capacity $2$), but it is $T$-even. Shrinking $S$ to $x$ leaves the triangle on the right, where the minimum cut separating $2$ from $3$ has capacity $4$.

:::

::: {#thm-edmonds-matching-polytope .theorem name="The matching polytope (Edmonds)"}

The convex hull of the incidence vectors of the matchings of a graph $G=(V,E)$ is
$$\Big\{x\in\mathbb R^E:\ x(\delta(v))\le1\ (v\in V),\ \ x(E(S))\le\tfrac{|S|-1}2\ (S\subseteq V,\ |S|\text{ odd}),\ \ x\ge0\Big\}.$$

:::

This is not proved here. The odd-set inequalities are needed: for the triangle, $x=(\frac12,\frac12,\frac12)$ satisfies the degree constraints but has $x(E)=\frac32>1$.

::: {#exm-matching-polytope-separation .example name="Separating over the matching polytope"}

Given $x\ge0$ with $x(\delta(v))\le1$ for all $v$ (otherwise a violated constraint is found directly), we must find an odd $S$ with $x(E(S))>\frac{|S|-1}2$ or show there is none. Assume $|V|$ even (add an isolated vertex), and put $s_v=1-x(\delta(v))\ge0$.

1. For odd $|S|$, summing $x(\delta(v))=1-s_v$ over $v\in S$ gives $2x(E(S))+x(\delta(S))=|S|-\sum_{v\in S}s_v$, so $x(E(S))\le\frac{|S|-1}2$ is equivalent to $\sum_{v\in S}s_v+x(\delta(S))\ge1$.

2. Add a new vertex $w$ joined to every $v\in V$ with capacity $s_v$, and give each edge $e\in E$ capacity $x_e$; call the graph $H$ and let $T=V$ (even). For $S\subseteq V$ the cut $\delta_H(S)$ has capacity exactly $\sum_{v\in S}s_v+x(\delta(S))$, and a $T$-odd set of $H$ or its complement is an odd $S\subseteq V$.

3. So a minimum $T$-odd cut of $H$ (@thm-t-odd-cut-algorithm) of value less than $1$ gives a violated inequality, and value at least $1$ proves $x$ in the polytope. With @thm-optimization-from-separation, maximum weight matchings can be found in polynomial time by the ellipsoid method.

:::
