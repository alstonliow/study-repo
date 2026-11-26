---
title: "Matroids"
sources: [mit18433-5]
requires: [math/discrete/graph/forests-and-spanning-trees, math/combinatorial-optimization/matching/augmenting-paths]
status: draft
---

<!-- Added 2026-11-26 from MIT 18.433 (Spring 2015), lecture notes on matroid optimization (Section 5.1), in our own wording; example our own (checked by computation); proofs written out in steps. -->

Matroids abstract the notion of linear independence of vectors. They are exactly the structures on which the greedy algorithm works (@sec-math-combinatorial-optimization-matroids-matroid-greedy), and intersections of two of them describe matchings, arborescences and much more.

::: {#def-matroid .definition name="Matroid"}

A *matroid* $M=(E,\mathcal I)$ consists of a finite *ground set* $E$ and a family $\mathcal I$ of subsets of $E$, the *independent sets*, such that $\varnothing\in\mathcal I$ and

- (I1) if $X\subseteq Y$ and $Y\in\mathcal I$, then $X\in\mathcal I$;
- (I2) if $X,Y\in\mathcal I$ and $|Y|>|X|$, then $X+e\in\mathcal I$ for some $e\in Y\setminus X$.

A family satisfying (I1) alone is an *independence system*. A maximal independent set is a *base*. By (I2), all bases have the same size: a smaller base could be extended by an element of a larger one.

:::

::: {#exm-matroid-examples .example name="Standard matroids"}

1. *Uniform matroid* $U_{k,n}$: $|E|=n$ and $\mathcal I=\{X:|X|\le k\}$. The *free matroid* $U_{n,n}$ has every set independent.
2. *Partition matroid*: $E=E_1\cup\dots\cup E_l$ disjointly, integers $k_i\ge0$, and $\mathcal I=\{X:|X\cap E_i|\le k_i\ \text{for all } i\}$. For (I2), if $|Y|>|X|$ then $|Y\cap E_i|>|X\cap E_i|$ for some $i$, and any $e\in(Y\setminus X)\cap E_i$ can be added to $X$.
3. *Linear matroid*: $E$ indexes the columns of a matrix $A$ over a field $\mathbb F$, and $X\in\mathcal I$ iff the columns $A_X$ are linearly independent. (I2) holds because $|Y|$ independent columns span a space of dimension $|Y|>|X|$, so some column of $Y$ lies outside the span of $A_X$. A matroid of this form is *representable* over $\mathbb F$; over $\mathbb F_2$ it is *binary*.
4. *Graphic matroid* $M(G)$ of a graph $G=(V,E)$: the independent sets are the forests (@def-forest). A forest $F$ has $\kappa(F)=|V|-|F|$ components, so if $|Y|>|X|$ for forests $X,Y$, then $Y$ has fewer components and some edge of $Y$ joins two components of $X$; adding it to $X$ keeps a forest. For connected $G$ the bases are the spanning trees.
5. *Matching matroid* of a graph $G=(V,E)$: the ground set is $V$, and $S\subseteq V$ is independent if some matching covers all of $S$ (it may cover more) (exercise).

:::

A graphic matroid is linear over every field: give the edge $ij$ the column with $1$ in row $i$, $-1$ in row $j$ and $0$ elsewhere (over $\mathbb F_2$, $-1=1$); a set of columns is dependent exactly when the edges contain a cycle. Matroids representable over every field are called *regular*.

::: {#exm-non-matroids .example name="Two independence systems that are not matroids"}

1. *Matchings.* In the path $1$–$2$–$3$–$4$, the matchings $X=\{23\}$ and $Y=\{12,34\}$ violate (I2): neither edge of $Y$ can be added to $X$.
2. *Overlapping parts.* With $E_1=\{1,2\}$, $E_2=\{2,3\}$, $k_1=k_2=1$ the family $\{X:|X\cap E_i|\le1\}$ contains $X=\{2\}$ and $Y=\{1,3\}$, but neither $1$ nor $3$ can be added to $X$; the parts of a partition matroid must be disjoint.

:::

Matchings are, however, the common independent sets of *two* partition matroids (@sec-math-combinatorial-optimization-matroids-matroid-intersection).

::: {#def-matroid-circuit .definition name="Circuit"}

A *circuit* of a matroid is an inclusion-wise minimal dependent set. In a graphic matroid the circuits are the cycles of the graph; in a partition matroid they are the sets $C\subseteq E_i$ with $|C|=k_i+1$.

:::

::: {#thm-unique-circuit .theorem name="Unique circuit property"}

If $S\in\mathcal I$ and $S+e\notin\mathcal I$, then $S+e$ contains exactly one circuit $C$, and $C\ni e$. Moreover $S+e-f\in\mathcal I$ for every $f\in C$.

:::

::: {.proof}

1. $S+e$ is dependent, so it contains a circuit; every circuit in it contains $e$, since $S$ is independent.

2. Suppose $S+e$ contains two circuits $C_1\ne C_2$. By minimality neither contains the other, so there is $f\in C_1\setminus C_2$, and $C_1-f\in\mathcal I$.

3. Extend $C_1-f$ to a maximal independent subset $X$ of $S+e$. By (I2) all maximal independent subsets of $S+e$ have the same size; $S$ is one of them (as $S+e$ is dependent), so $|X|=|S|=|S+e|-1$ and $X=S+e-g$ for a single element $g$. If $g\ne f$, then $X\supseteq(C_1-f)+f=C_1$, which is impossible. So $X=S+e-f$.

4. But $C_2\subseteq S+e-f=X$, because $f\notin C_2$; this contradicts the independence of $X$.

5. For $f\in C$: if $S+e-f$ were dependent, it would contain a circuit, which lies in $S+e$ and avoids $f$, so differs from $C$; this contradicts uniqueness.

:::

For a forest $S$ and an edge $e$ closing a cycle, the theorem says the cycle is unique and removing any of its edges gives a forest again.

::: {#exm-matroid-circuit-small .example name="Circuits of a small linear matroid"}

Over $\mathbb R$ let the columns be $a_1=(1,0)$, $a_2=(0,1)$, $a_3=(1,1)$, $a_4=(2,0)$. The bases are all pairs except $\{1,4\}$ (parallel columns), so the matroid has rank $2$. Its circuits are $\{1,4\}$, $\{1,2,3\}$ and $\{2,3,4\}$. For the base $S=\{1,2\}$ and $e=4$, the unique circuit in $S+e$ is $\{1,4\}$, and $S+4-1=\{2,4\}$ is again a base.

:::

::: {#fig-matroids-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.3,0) -- (3.0,0); \draw[->, faint] (0,-0.3) -- (0,1.8);
\draw[->, emph] (0,0) -- (1.2,0) node[lab, below] {$a_1$};
\draw[->, hl] (0,0) -- (2.4,0) node[lab, above] {$a_4$};
\draw[->, emph] (0,0) -- (0,1.2) node[lab, left] {$a_2$};
\draw[->, emph] (0,0) -- (1.2,1.2) node[lab, right] {$a_3$};
\end{tikzpicture}
\end{center}
```

The columns of the example: $a_1$ and $a_4$ are parallel, so $\{1,4\}$ is a circuit; any three columns with no parallel pair, such as $\{1,2,3\}$, form a circuit too, since the rank is $2$.

:::
