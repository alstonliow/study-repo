::: {.problem #prob-eecs126hw-10-q1 origin="external" source="eecs126hw-10-q1"}
**Random Graph Estimation.** Consider a random graph on $n$ vertices in which each edge appears independently with probability $p$. Let $D$ be the average degree of a vertex in the graph. Compute the maximum likelihood estimator of $p$ given $D$. You may approximate $\text{Binomial}(n,p)=\text{Poisson}(np)$.
:::

::: {.problem #prob-eecs126d-2-q3 origin="external" source="eecs126d-2-q3"}
**Clustering Coefficient.** This problem will explore an important probabilistic concept of clustering that is widely used in machine learning applications today. Consider $n$ students, where $n$ is a positive integer. For each pair of students $i,j\in\{1,\dots,n\}$, $i\ne j$, they are friends with probability $p$, independently of other pairs. We assume that friendship is mutual. We can see that the friendship among the $n$ students can be represented by an undirected graph $G$. Let $N(i)$ be the number of friends of student $i$ and $T(i)$ be the number of triangles attached to student $i$. We define the clustering coefficient $C(i)$ for student $i$ as follows:
$$C(i)=\frac{T(i)}{\binom{N(i)}{2}}.$$
```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (1) at (0,1.2) {$1$};
\node[small vertex] (2) at (1.3,1.6) {$2$};
\node[small vertex] (3) at (1.3,0.3) {$3$};
\node[small vertex] (4) at (2.6,1.2) {$4$};
\node[small vertex] (5) at (1.3,-1.0) {$5$};
\draw (3)--(1);
\draw (3)--(2);
\draw (3)--(4);
\draw (3)--(5);
\draw (1)--(2);
\draw (2)--(4);
\end{tikzpicture}
\end{center}
```

The clustering coefficient is not defined for the students who have no friends. An example is shown in Figure ??. Student 3 has 4 friends (1, 2, 4, 5) and there are two triangles attached to student 3, i.e., triangle 1-2-3 and triangle 2-3-4. Therefore $C(3)=2/\binom42=1/3$.

Find $E[C(i)\mid N(i)\ge2]$.

:::
