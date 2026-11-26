::: {.problem #prob-mit18433-3-q11 origin="external" source="mit18433-3-q11"}
Consider the set $X=\{(\sigma(1),\sigma(2),\cdots,\sigma(n)):\sigma\text{ is a permutation of }\{1,2\cdots,n\}\}$. Show that $\dim(\operatorname{conv}(X))=n-1$. (To show that $\dim(\operatorname{conv}(X))\ge n-1$, exhibit $n$ affinely independent permutations $\sigma$ (and prove that they are affinely independent).)
:::

::: {.problem #prob-mit18433-3-q12 origin="external" source="mit18433-3-q12"}
A stable set $S$ (sometimes, it is called also an independent set) in a graph $G=(V,E)$ is a set of vertices such that there are no edges between any two vertices in $S$. If we let $P$ denote the convex hull of all (incidence vectors of) stable sets of $G=(V,E)$, it is clear that $x_i+x_j\le1$ for any edge $(i,j)\in E$ is a valid inequality for $P$.

1. Give a graph $G$ for which $P$ is not equal to
$$\{x\in\mathbb R^{|V|}:x_i+x_j\le1\text{ for all }(i,j)\in E,\ x_i\ge0\text{ for all }i\in V\}$$
2. Show that if the graph $G$ is bipartite then $P$ equals
$$\{x\in\mathbb R^{|V|}:x_i+x_j\le1\text{ for all }(i,j)\in E,\ x_i\ge0\text{ for all }i\in V\}.$$
:::

::: {.problem #prob-mit18433-3-q13 origin="external" source="mit18433-3-q13"}
Let $e_k\in\mathbb R^n$ ($k=0,\ldots,n-1$) be a vector with the first $k$ entries being 1, and the following $n-k$ entries being $-1$. Let $S=\{e_0,e_1,\ldots,e_{n-1},-e_0,-e_1,\ldots,-e_{n-1}\}$, i.e. $S$ consists of all vectors consisting of $+1$ followed by $-1$ or vice versa. In this problem set, you will study $\operatorname{conv}(S)$.

1. Consider any vector $a\in\{-1,0,1\}^n$ such that (i) $\sum_{i=1}^na_i=1$ and (ii) for all $j=1,\ldots,n-1$, we have $0\le\sum_{i=1}^ja_i\le1$. (For example, for $n=5$, the vector $(1,0,-1,1,0)$ satisfies these conditions.) Show that $\sum_{i=1}^na_ix_i\le1$ and $\sum_{i=1}^na_ix_i\ge-1$ are valid inequalities for $\operatorname{conv}(S)$.
2. How many such inequalities are there?
3. Show that any such inequality defines a facet of $\operatorname{conv}(S)$.

   (This can be done in several ways. Here is one approach, but you are welcome to use any other one as well. First show that either $e_k$ or $-e_k$ satisfies this inequality at equality, for any $k$. Then show that the resulting set of vectors on the hyperplane are affinely independent (or uniquely identifies it).)
4. Show that the above inequalities define the entire convex hull of $S$.

   (Again this can be done in several ways. One possibility is to consider the 3rd technique described above.)
:::
