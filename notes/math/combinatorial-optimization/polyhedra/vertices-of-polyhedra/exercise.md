::: {.problem #prob-mit18433-3-q7 origin="external" source="mit18433-3-q7"}
Show that if $\operatorname{rank}(A)<n$ then $P=\{x\in\mathbb R^n:Ax\le b\}$ has no vertices.
:::

::: {.problem #prob-mit18433-3-q8 origin="external" source="mit18433-3-q8"}
Suppose $P=\{x\in\mathbb R^n:Ax\le b,Cx\le d\}$. Show that the set of vertices of $Q=\{x\in\mathbb R^n:Ax\le b,Cx=d\}$ is a subset of the set of vertices of $P$.

(In particular, this means that if the vertices of $P$ all belong to $\{0,1\}^n$, then so do the vertices of $Q$.)
:::

::: {.problem #prob-mit18433-3-q9 origin="external" source="mit18433-3-q9"}
Given two extreme points $a$ and $b$ of a polyhedron $P$, we say that they are adjacent if the line segment between them forms an edge (i.e. a face of dimension 1) of the polyhedron $P$. This can be rephrased by saying that $a$ and $b$ are adjacent on $P$ if and only if there exists a cost function $c$ such that $a$ and $b$ are the only two extreme points of $P$ minimizing $c^{\mathsf T}x$ over $P$.

Consider the polyhedron (polytope) $P$ defined as the convex hull of all perfect matchings in a (not necessarily bipartite) graph $G$. Give a necessary and sufficient condition for two matchings $M_1$ and $M_2$ to be adjacent on this polyhedron (hint: think about $M_1\triangle M_2=(M_1\setminus M_2)\cup(M_2\setminus M_1)$) and prove that your condition is necessary and sufficient.)
:::

::: {.problem #prob-mit18433-3-q10 origin="external" source="mit18433-3-q10"}
Show that two vertices $u$ and $v$ of a polyhedron $P$ are adjacent if and only there is a unique way to express their midpoint ($\frac12(u+v)$) as a convex combination of vertices of $P$.
:::
