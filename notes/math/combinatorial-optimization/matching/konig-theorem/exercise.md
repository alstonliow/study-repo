::: {.problem #prob-mit18433-1-q2 origin="external" source="mit18433-1-q2"}
An *edge cover* of a graph $G=(V,E)$ is a subset of $R$ of $E$ such that every vertex of $V$ is incident to at least one edge in $R$. Let $G$ be a bipartite graph with no isolated vertex. Show that the cardinality of the minimum edge cover $R^*$ of $G$ is equal to $|V|$ minus the cardinality of the maximum matching $M^*$ of $G$. Give an efficient algorithm for finding the minimum edge cover of $G$. Is this true also for non-bipartite graphs?
:::

::: {.problem #prob-mit18433-1-q4 origin="external" source="mit18433-1-q4"}
Consider the problem of perfectly tiling a subset of a checkerboard (i.e. a collection of unit squares, see example below) with dominoes (a domino being 2 adjacent squares).

1. Show that this problem can be formulated as the problem of deciding whether a bipartite graph has a perfect matching.
2. Can the following figure be tiled by dominoes? Give a tiling or a short proof that no tiling exists.

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.90,3.15) rectangle (1.35,3.60);
\draw[cell frame] (1.35,3.15) rectangle (1.80,3.60);
\draw[cell frame] (0.45,2.70) rectangle (0.90,3.15);
\draw[cell frame] (0.90,2.70) rectangle (1.35,3.15);
\draw[cell frame] (1.35,2.70) rectangle (1.80,3.15);
\draw[cell frame] (0.00,2.25) rectangle (0.45,2.70);
\draw[cell frame] (0.45,2.25) rectangle (0.90,2.70);
\draw[cell frame] (0.90,2.25) rectangle (1.35,2.70);
\draw[cell frame] (1.35,2.25) rectangle (1.80,2.70);
\draw[cell frame] (1.80,2.25) rectangle (2.25,2.70);
\draw[cell frame] (2.70,2.25) rectangle (3.15,2.70);
\draw[cell frame] (3.15,2.25) rectangle (3.60,2.70);
\draw[cell frame] (0.00,1.80) rectangle (0.45,2.25);
\draw[cell frame] (0.45,1.80) rectangle (0.90,2.25);
\draw[cell frame] (0.90,1.80) rectangle (1.35,2.25);
\draw[cell frame] (1.35,1.80) rectangle (1.80,2.25);
\draw[cell frame] (1.80,1.80) rectangle (2.25,2.25);
\draw[cell frame] (2.70,1.80) rectangle (3.15,2.25);
\draw[cell frame] (3.15,1.80) rectangle (3.60,2.25);
\draw[cell frame] (0.00,1.35) rectangle (0.45,1.80);
\draw[cell frame] (0.45,1.35) rectangle (0.90,1.80);
\draw[cell frame] (0.90,1.35) rectangle (1.35,1.80);
\draw[cell frame] (1.35,1.35) rectangle (1.80,1.80);
\draw[cell frame] (1.80,1.35) rectangle (2.25,1.80);
\draw[cell frame] (2.25,1.35) rectangle (2.70,1.80);
\draw[cell frame] (2.70,1.35) rectangle (3.15,1.80);
\draw[cell frame] (3.15,1.35) rectangle (3.60,1.80);
\draw[cell frame] (0.45,0.90) rectangle (0.90,1.35);
\draw[cell frame] (0.90,0.90) rectangle (1.35,1.35);
\draw[cell frame] (1.35,0.90) rectangle (1.80,1.35);
\draw[cell frame] (1.80,0.90) rectangle (2.25,1.35);
\draw[cell frame] (2.25,0.90) rectangle (2.70,1.35);
\draw[cell frame] (2.70,0.90) rectangle (3.15,1.35);
\draw[cell frame] (3.15,0.90) rectangle (3.60,1.35);
\draw[cell frame] (1.35,0.45) rectangle (1.80,0.90);
\draw[cell frame] (1.80,0.45) rectangle (2.25,0.90);
\draw[cell frame] (2.25,0.45) rectangle (2.70,0.90);
\draw[cell frame] (2.70,0.45) rectangle (3.15,0.90);
\draw[cell frame] (3.15,0.45) rectangle (3.60,0.90);
\draw[cell frame] (1.80,0.00) rectangle (2.25,0.45);
\draw[cell frame] (2.25,0.00) rectangle (2.70,0.45);
\draw[cell frame] (2.70,0.00) rectangle (3.15,0.45);
\end{tikzpicture}
\end{center}
```

*Note (these notes):* figure redrawn from the course notes; rows are numbered $1$–$8$ from the top and columns $1$–$8$ from the left.
:::

::: {.problem #prob-mit18433-1-q7 origin="external" source="mit18433-1-q7"}
Deduce Hall's theorem from König's theorem.
:::

::: {.problem #prob-mit18433-1-q8 origin="external" source="mit18433-1-q8"}
Consider a bipartite graph $G=(V,E)$ with bipartition $(A,B)$. For $X\subseteq A$, define $\operatorname{def}(X)=|X|-|N(X)|$ where $N(X)=\{b\in B:\exists a\in X\text{ with }(a,b)\in E\}$. Let
$$\operatorname{def}_{\max}=\max_{X\subseteq A}\operatorname{def}(X).$$
Since $\operatorname{def}(\emptyset)=0$, we have $\operatorname{def}_{\max}\ge0$.

1. Generalize Hall's theorem by showing that the maximum size of a matching in a bipartite graph $G$ equals $|A|-\operatorname{def}_{\max}$.
2. For any 2 subsets $X,Y\subseteq A$, show that
$$\operatorname{def}(X\cup Y)+\operatorname{def}(X\cap Y)\ge\operatorname{def}(X)+\operatorname{def}(Y).$$
:::

::: {.problem #prob-mit18433-1-q12 origin="external" source="mit18433-1-q12"}
Consider a bipartite graph $G=(V,E)$ in which every vertex has degree $k$ (a so-called $k$-regular bipartite graph). Prove that such a graph always has a perfect matching in two different ways:

1. by using König's theorem,
2. by using the linear programming formulation we have derived in this section.

(Optional: Is this result also true for non-bipartite graphs?)
:::

::: {.problem #prob-mit18433-1-q13 origin="external" source="mit18433-1-q13"}
Using the previous exercise 12, show that the edges of a $k$-regular bipartite graph $G$ can be partitioned into $k$ matchings (i.e. the number of colors needed to color the edges of a $k$-regular bipartite graph such that no two edges with a common endpoint have the same color — the edge chromatic number — is precisely $k$).

(Optional: Is this result also true also for non-bipartite graphs?)
:::

::: {.problem #prob-mit18433-1-q14 origin="external" source="mit18433-1-q14"}
Given a graph $G=(V,E)$, its edge coloring number is the smallest number of colors needed to color the edges in $E$ so that any two edges having a common endpoint have a different color.

1. Show that the edge coloring number of a bipartite graph $G$ is always equal to its maximum degree $\Delta$ (i.e. the maximum over all vertices $v$ of the number of edges incident to $v$). (Use the previous problem.)
2. Give an example of a non-bipartite graph for which the edge coloring number is (strictly) greater than $\Delta$.
:::

::: {.problem #prob-mit18433ps-1-q4 origin="external" source="mit18433ps-1-q4"}
(More difficult.) Let $S=\{1,2,\cdots,n\}$. Let $A_k$ be the set of all subsets of $S$ of cardinality $k$ (thus $|A_k|=\binom nk$). Let $k<\frac n2$. Consider the graph $G_k$ with bipartition $A_k$ and $A_{k+1}$, and with $E=\{(a,b)\mid a\in A_k,b\in A_{k+1}\text{ and }a\subset b\}$.

(a) Prove that the maximum matching in $G_k$ has size $A_k$ (remember $k<n/2$).

(b) Prove *Sperner's lemma*. The maximum number of subsets of $S$ such that no subset is contained into another is $\binom n{\lfloor n/2\rfloor}$.
:::
