---
title: "Rank and Span in a Matroid"
sources: [mit18433-5]
requires: [math/combinatorial-optimization/matroids/matroids]
status: draft
---

<!-- Added 2026-11-26 from MIT 18.433 (Spring 2015), lecture notes on matroid optimization (Section 5.3), in our own wording; example our own (checked by computation); proofs written out in steps. -->

::: {#def-matroid-rank .definition name="Rank function"}

The *rank function* of a matroid $M=(E,\mathcal I)$ is
$$r(X)=\max\{|Y|:Y\subseteq X,\ Y\in\mathcal I\}\qquad(X\subseteq E).$$
By (I2), every maximal independent subset of $X$ has exactly $r(X)$ elements. The rank of the matroid is $r(E)$, the size of its bases.

:::

::: {#exm-matroid-rank-functions .example name="Rank functions"}

1. For a linear matroid, $r(X)=\operatorname{rank}A_X$, the usual rank of the columns in $X$.
2. For a partition matroid with parts $E_i$ and bounds $k_i$, $r(X)=\sum_i\min(|X\cap E_i|,k_i)$.
3. For a graphic matroid $M(G)$ with $G=(V,E)$, $r(F)=|V|-\kappa(F)$, where $\kappa(F)$ counts the components of $(V,F)$, isolated vertices included: a maximal forest in $F$ is a spanning tree of each component.

:::

Every rank function satisfies

- (R1) $0\le r(X)\le|X|$, and $r$ is integer-valued;
- (R2) $X\subseteq Y\Rightarrow r(X)\le r(Y)$;
- (R3) $r(X)+r(Y)\ge r(X\cap Y)+r(X\cup Y)$ for all $X,Y\subseteq E$.

(R1) and (R2) are immediate. Property (R3), *submodularity*, needs a proof; it is one of the central notions of combinatorial optimisation.

::: {#lem-matroid-rank-submodular .lemma name="Rank is submodular"}

The rank function of every matroid satisfies (R3).

:::

::: {.proof}

1. Let $J$ be a maximal independent subset of $X\cap Y$, so $|J|=r(X\cap Y)$. Extend it to a maximal independent subset $J_X$ of $X$, so $|J_X|=r(X)$, and then $J_X$ to a maximal independent subset $J_{XY}$ of $X\cup Y$, so $|J_{XY}|=r(X\cup Y)$.

2. By maximality of $J$ in $X\cap Y$, the set $J_X$ has no further elements in $Y$: $J_X\cap Y=J$, so $J_X\setminus Y=J_X\setminus J$.

3. By maximality of $J_X$ in $X$, $J_{XY}$ has no further elements in $X$, so $J_{XY}\cap X=J_X$. Hence the elements of $J_{XY}$ outside $Y$ are exactly those of $J_X\setminus Y$, and
$$J_{XY}\cap Y=J_{XY}\setminus(J_X\setminus J).$$

4. $J_{XY}\cap Y$ is an independent subset of $Y$, so
$$r(Y)\ge|J_{XY}|-|J_X|+|J|=r(X\cup Y)-r(X)+r(X\cap Y),$$
which is (R3).

:::

::: {#def-matroid-span .definition name="Span, closed set"}

The *span* (or *closure*) of $S\subseteq E$ is
$$\operatorname{span}(S)=\{e\in E:r(S+e)=r(S)\}.$$
A set $S$ is *closed* (a *flat*) if $\operatorname{span}(S)=S$.

:::

::: {#prp-span-same-rank .proposition name="The span has the same rank"}

$S\subseteq\operatorname{span}(S)$ and $r(\operatorname{span}(S))=r(S)$.

:::

::: {.proof}

1. $S\subseteq\operatorname{span}(S)$ since $S+e=S$ for $e\in S$.

2. Let $J$ be a maximal independent subset of $S$. If $r(\operatorname{span}(S))>|J|$, then by (I2) some $e\in\operatorname{span}(S)\setminus J$ has $J+e\in\mathcal I$.

3. Then $r(S+e)\ge|J+e|=|J|+1>r(S)$, contradicting $e\in\operatorname{span}(S)$.

:::

In a linear matroid, the span of $S$ is the set of columns in the linear span of $A_S$. In a graphic matroid, the span of an edge set $F$ consists of all edges whose two ends lie in the same component of $(V,F)$.

::: {#exm-matroid-rank-small .example name="Submodularity in a graphic matroid"}

Let $G$ be the $4$-cycle $1$–$2$–$3$–$4$–$1$ with edges $a=12$, $b=23$, $c=34$, $d=41$, and take $X=\{a,b,c\}$, $Y=\{b,c,d\}$. Then $r(X)=r(Y)=3$ (paths), $r(X\cap Y)=r(\{b,c\})=2$ and $r(X\cup Y)=r(E)=3$, so (R3) reads $3+3\ge2+3$. The span of $\{a,b\}$ is $\{a,b\}$ (vertex $4$ is not reached), while the span of $X$ is all of $E$.

:::

::: {#fig-matroid-rank-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (w1) at (0,1.4) {$1$};
\node[small vertex] (w2) at (1.4,1.4) {$2$};
\node[small vertex] (w3) at (1.4,0) {$3$};
\node[small vertex] (w4) at (0,0) {$4$};

\draw[hl] (w1) -- node[edge label] {$a$} (w2);
\draw[hl] (w2) -- node[edge label] {$b$} (w3);
\draw[emph] (w3) -- node[edge label] {$c$} (w4);
\draw[emph] (w4) -- node[edge label] {$d$} (w1);
\end{tikzpicture}
\end{center}
```

The $4$-cycle of the example. The highlighted set $\{a,b\}$ has rank $2$ and is closed: $c$ and $d$ reach vertex $4$, outside its component. Any three edges have rank $3$ and span all four.

:::
