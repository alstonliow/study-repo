<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18433-3-q14" status="draft"}
1. The map $\varphi(x)=(x,b-Ax)$ is an affine bijection from $P$ onto $Q$, with inverse $(x,s)\mapsto x$: indeed $(x,s)\in Q$ forces $s=b-Ax$, and $s\ge0$ iff $Ax\le b$.

2. Affine maps preserve convex combinations: $\varphi(\lambda y+(1-\lambda)z)=\lambda\varphi(y)+(1-\lambda)\varphi(z)$. So $x$ is a non-trivial convex combination of points of $P$ iff $\varphi(x)$ is one of points of $Q$; hence $x$ is extreme in $P$ iff $\varphi(x)$ is extreme in $Q$.

3. If $A,b$ are integral, $x$ is integral iff $(x,b-Ax)$ is. With step 2, all vertices of $P$ are integral iff all vertices of $Q$ are.
:::

::: {.solution for="prob-mit18433-3-q15" status="draft"}
Every square submatrix of $A^{\mathsf T}$ is the transpose of a square submatrix of $A$, and $\det B^{\mathsf T}=\det B\in\{-1,0,1\}$.
:::

::: {.solution for="prob-mit18433-3-q16" status="draft"}
Let $A$ be the vertex–edge incidence matrix of the bipartite graph; it is TU (@thm-bipartite-incidence-tu), and so is $A^{\mathsf T}$.

1. Consider $\max\{\mathbf 1^{\mathsf T}x:Ax\le\mathbf 1,\ x\ge0\}$ and its dual $\min\{\mathbf 1^{\mathsf T}y:A^{\mathsf T}y\ge\mathbf 1,\ y\ge0\}$. Both are feasible ($x=0$, $y=\mathbf 1$) and bounded, so by strong duality (@thm-strong-duality) their optima are equal, and both are attained at vertices (@cor-minimal-faces-are-vertices; the constraint matrices contain $\pm I$, so have full column rank).

2. By @thm-tu-integral-polyhedron both polyhedra are integral. An integral primal vertex has $x_e\le1$ (from the degree constraint at an end of $e$), so it is the incidence vector of a matching.

3. An integral optimal dual $y$ can be taken $0$–$1$ (lowering any $y_v\ge2$ to $1$ keeps feasibility and does not increase the cost). Then $\{v:y_v=1\}$ meets every edge, i.e. it is a vertex cover.

4. So the maximum matching size equals the minimum vertex cover size.
:::

::: {.solution for="prob-mit18433-3-q17" status="draft"}
1. Activity $i$ occupies $[t_i,u_i)$. Two such intervals overlap iff one contains the start time of the other. So for each start time $\tau\in\{t_1,\dots,t_n\}$ impose
$$\sum_{i:\ t_i\le\tau<u_i}x_i\le1 .$$
With $b=\mathbf 1$ and $x\in\{0,1\}^n$ the feasible $x$ are exactly the sets of pairwise non-overlapping activities, and we maximise $p^{\mathsf T}x$.

2. Order the rows by increasing $\tau$. Column $i$ has its $1$s in the rows with $\tau\in[t_i,u_i)$, which are consecutive in this order. So $A$ is an interval matrix and is TU (@exm-interval-matrix-tu). Appending the rows $x_i\le1$ (rows of $I$) keeps it TU, so by @thm-tu-integral-polyhedron the polytope $\{x:Ax\le\mathbf 1,\ 0\le x\le\mathbf 1\}$ is integral. An optimal vertex of the LP is a $0$–$1$ solution of the integer program, hence optimal for it.
:::

::: {.solution for="prob-mit18433-3-q18" status="draft"}
1. *Yes, it is TU.* Use Ghouila-Houri (@thm-ghouila-houri). Let $R$ be a set of rows. If $R$ does not contain the all-ones row, put the rows of $A$-vertices in $R_1$ and those of $B$-vertices in $R_2$; each column (an edge $ij$) gets $[i\in R]-[j\in R]\in\{-1,0,1\}$. If $R$ contains the all-ones row, put it alone in $R_1$ and all other rows of $R$ in $R_2$; column $ij$ gets $1-[i\in R]-[j\in R]\in\{-1,0,1\}$.

2. $S_k\subseteq P_k$ is clear. By part 1 and @thm-tu-integral-polyhedron, $P_k$ is integral, and it is bounded ($x_{ij}\le1$). Its vertices are $0$–$1$ vectors with degrees at most $1$ and at most $k$ ones, i.e. elements of $S_k$. So $P_k=\operatorname{conv}(\text{vertices})\subseteq\operatorname{conv}(S_k)$ (@thm-minkowski-polytope).

3. *No.* Take the $4$-cycle $a_1b_1a_2b_2a_1$ with edges $e_1=a_1b_1$, $e_2=b_1a_2$, $e_3=a_2b_2$, $e_4=b_2a_1$, $E_1=\{e_1,e_3\}$ and $k=1$. The point $x=(\frac12,\frac12,\frac12,\frac12)$ satisfies all degree constraints and $x(E_1)=1$. But every allowed matching has at most $2$ edges, and the only allowed one with $2$ edges is $\{e_2,e_4\}$. Since $x$ has total $2$, a convex combination equal to $x$ would have to put all its weight on $\{e_2,e_4\}$, giving $x(E_1)=0\ne1$. So $x$ is not in the convex hull.
:::
