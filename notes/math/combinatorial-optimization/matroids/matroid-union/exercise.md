::: {.problem #prob-mit18433ps-6-q1 origin="external" source="mit18433ps-6-q1"}
Given a matroid $M=(E,\mathcal I)$ with rank function $r$, define $\mathcal I^*=\{F\subset E\mid r(E\setminus F)=r(E)\}$, i.e. $F\in\mathcal I^*$ if the complement of $F$ still contains a base.

(a) Show that $M^*=(E,\mathcal I^*)$ is a matroid (it is called the dual matroid). What are the bases of $M^*$ (in terms of teh bases of $M$)?

(b) Let $r^*$ be the rank function of $M^*$. Give an expression for $r^*(U)$ (for any $U\subseteq E$) in terms of the rank function $r$ of $M$.
:::

::: {.problem #prob-mit18433-6-q2 origin="external" source="mit18433-6-q2"}
Derive from theorem 6.10 that the union of $k$ matroids $M_1,M_2,\cdots,M_k$ is a matroid with rank function
$$r_{M_1\cup M_2\cup\cdots\cup M_k}(S)=\min_{F\subseteq S}\{|S\setminus F|+r_{M_1}(F)+r_{M_2}(F)+\cdots+r_{M_k}(F)\}.$$

*Note (these notes):* Theorem 6.10 is @thm-matroid-union.
:::

::: {.problem #prob-mit18433-6-q3 origin="external" source="mit18433-6-q3"}
Derive Theorem 6.9 from Exercise 6-2.

*Note (these notes):* Theorem 6.9 is the statement after @thm-two-disjoint-spanning-trees: $G$ has $k$ edge-disjoint spanning trees iff $|\delta(V_1,\dots,V_p)|\ge k(p-1)$ for all partitions.
:::

::: {.problem #prob-mit18433-6-q4 origin="external" source="mit18433-6-q4"}
Assume that $G$ has 2 edge-disjoint spanning trees. Give a winning strategy for player 2 in the spanning tree game.
:::

::: {.problem #prob-mit18433-6-q5 origin="external" source="mit18433-6-q5"}
Find two edge-disjoint spanning trees in the following graph with 16 vertices and 30 edges or prove that no such trees exist.

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (v1) at (0.0,3.9) {1};
\node[small vertex] (v2) at (1.3,3.9) {2};
\node[small vertex] (v3) at (2.6,3.9) {3};
\node[small vertex] (v4) at (3.9,3.9) {4};
\node[small vertex] (v5) at (0.0,2.6) {5};
\node[small vertex] (v6) at (1.3,2.6) {6};
\node[small vertex] (v7) at (2.6,2.6) {7};
\node[small vertex] (v8) at (3.9,2.6) {8};
\node[small vertex] (v9) at (0.0,1.3) {9};
\node[small vertex] (v10) at (1.3,1.3) {10};
\node[small vertex] (v11) at (2.6,1.3) {11};
\node[small vertex] (v12) at (3.9,1.3) {12};
\node[small vertex] (v13) at (0.0,0.0) {13};
\node[small vertex] (v14) at (1.3,0.0) {14};
\node[small vertex] (v15) at (2.6,0.0) {15};
\node[small vertex] (v16) at (3.9,0.0) {16};
\draw (v1) -- (v2);
\draw (v2) -- (v3);
\draw (v3) -- (v4);
\draw (v4) -- (v8);
\draw (v8) -- (v12);
\draw (v12) -- (v16);
\draw (v13) -- (v14);
\draw (v14) -- (v15);
\draw (v15) -- (v16);
\draw (v1) -- (v5);
\draw (v5) -- (v9);
\draw (v9) -- (v13);
\draw (v5) -- (v6);
\draw (v6) -- (v7);
\draw (v7) -- (v8);
\draw (v9) -- (v10);
\draw (v10) -- (v11);
\draw (v11) -- (v12);
\draw (v2) -- (v6);
\draw (v6) -- (v10);
\draw (v10) -- (v14);
\draw (v3) -- (v7);
\draw (v7) -- (v11);
\draw (v11) -- (v15);
\draw (v1) -- (v6);
\draw (v6) -- (v11);
\draw (v11) -- (v16);
\draw (v4) -- (v7);
\draw (v7) -- (v10);
\draw (v10) -- (v13);
\end{tikzpicture}
\end{center}
```

*Note (these notes):* graph redrawn from the course notes.
:::
