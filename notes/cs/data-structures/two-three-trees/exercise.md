::: {.problem #prob-mit6046s15-2-q2 origin="external" source="mit6046s15-2-q2"}
**Combining B-trees**

Consider a new B-tree operation COMBINE$(T_1,T_2,k)$. This operation takes as input two B-trees $T_1$ and $T_2$ with the same minimum degree parameter $t$, plus a new key $k$ that does not appear in either $T_1$ or $T_2$. We assume that all the keys in $T_1$ are strictly smaller than $k$ and all the keys in $T_2$ are strictly larger than $k$. The COMBINE operation produces a new B-tree $T$, with the same minimum degree $t$, whose keys are those in $T_1$, those in $T_2$, plus $k$. In the process, it destroys the original trees $T_1$ and $T_2$.

In this problem, you will design an algorithm to implement the COMBINE operation. Your algorithm should run in time $O(|h_1-h_2|+1)$, where $h_1$ and $h_2$ are the heights of trees $T_1$ and $T_2$ respectively. In analyzing the costs, you should regard $t$ as a constant.

(a) First consider the special case of the problem in which $h_1$ is assumed to be equal to $h_2$. Give an algorithm to combine the trees that runs in constant time.

(b) Consider another special case, in which $h_1$ is assumed to be exactly equal to $h_2+1$. Give a constant-time algorithm to combine the trees.

(c) Now consider the more general case in which $h_1$ and $h_2$ are arbitrary. Because the algorithm must work in such a small amount of time, and must work for arbitrary heights, a first step is to develop a new kind of augmented B-tree data structure in which each node $x$ always carries information about the height of the subtree below $x$. Describe how to augment the common B-tree insertion and deletion operations to maintain this information, while still maintaining the asymptotic time complexity of all operations.

(d) Now give an algorithm for combining two B-trees $T_1$ and $T_2$, in the general case where $h_1$ and $h_2$ are arbitrary. Your algorithm should run in time $O(|h_1-h_2|+1)$.
:::
