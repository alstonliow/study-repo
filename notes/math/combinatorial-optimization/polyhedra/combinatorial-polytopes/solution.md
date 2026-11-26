<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18433-3-q11" status="draft"}
1. *Upper bound.* Every point of $X$ satisfies $\sum_ix_i=\binom{n+1}2$, so $\operatorname{conv}(X)$ lies in a hyperplane and has dimension at most $n-1$.

2. *Lower bound.* Let $\pi_1$ be the identity and $\pi_k$ ($k=2,\dots,n$) the permutation exchanging the values $1$ and $k$, so $\pi_k$ has $k$ in position $1$ and $1$ in position $k$. Then $\pi_k-\pi_1=(k-1)(e_1-e_k)$.

3. The vectors $e_1-e_k$, $k=2,\dots,n$, are linearly independent (each $e_k$ appears in only one of them). Hence $\pi_2-\pi_1,\dots,\pi_n-\pi_1$ are linearly independent, i.e. $\pi_1,\dots,\pi_n$ are affinely independent, and $\dim\operatorname{conv}(X)\ge n-1$.
:::

::: {.solution for="prob-mit18433-3-q12" status="draft"}
Call the displayed polyhedron $Q$; clearly $P\subseteq Q$.

1. For the triangle, $x=(\frac12,\frac12,\frac12)\in Q$, but a stable set of the triangle has at most one vertex, so $x_1+x_2+x_3\le1$ is valid for $P$ and violated by $x$. So $P\ne Q$.

2. We assume $G$ has no isolated vertex (an isolated vertex $v$ needs the extra row $x_v\le1$, after which the same argument works). Then $Q=\{x:Nx\le\mathbf1,\ x\ge0\}$, where $N$ is the edge–vertex incidence matrix, the transpose of the matrix of @thm-bipartite-incidence-tu; it is TU (transposition preserves TU). By @thm-tu-integral-polyhedron $Q$ is integral. Every vertex lies on an edge, so $0\le x\le1$ on $Q$: $Q$ is bounded, its vertices are $0$–$1$ vectors satisfying $x_i+x_j\le1$ on edges, i.e. incidence vectors of stable sets. Hence $Q=\operatorname{conv}(\text{vertices})\subseteq P$ (@thm-minkowski-polytope).
:::

::: {.solution for="prob-mit18433-3-q13" status="draft"}
Write $s_j=\sum_{i\le j}a_i$, so $s_0=0$, $s_n=1$ and $s_j\in\{0,1\}$.

1. $a^{\mathsf T}e_k=\sum_{i\le k}a_i-\sum_{i>k}a_i=s_k-(1-s_k)=2s_k-1\in\{-1,1\}$, and $a^{\mathsf T}(-e_k)=1-2s_k$. So $|a^{\mathsf T}x|\le1$ on $S$, hence on $\operatorname{conv}(S)$.

2. $a$ is determined by $(s_1,\dots,s_{n-1})\in\{0,1\}^{n-1}$, and every choice gives a valid $a$ (each $a_i=s_i-s_{i-1}\in\{-1,0,1\}$). So there are $2^{n-1}$ vectors $a$ and $2^n$ inequalities.

3. *Facets.* $e_k-e_{k-1}=2u_k$ ($u_k$ the $k$-th unit vector, $1\le k\le n-1$) and $e_0=-\mathbf 1$, so $e_0,\dots,e_{n-1}$ span $\mathbb R^n$ and are linearly independent. The $n+1$ points $e_0,\dots,e_{n-1},-e_0$ of $S$ are affinely independent, so $\dim\operatorname{conv}(S)=n$. For the inequality $a^{\mathsf T}x\le1$, by part 1 exactly one of $\pm e_k$ is tight for each $k$, namely $f_k=(2s_k-1)e_k$. The $f_k$ are $n$ linearly (hence affinely) independent points on the hyperplane, so the face has dimension $n-1$: a facet. The same holds for $a^{\mathsf T}x\ge-1$ with the points $-f_k$.

4. *Completeness* (facet technique). $\operatorname{conv}(S)$ is full-dimensional, so no equality is needed. Let $\alpha^{\mathsf T}x\le\beta$ define a facet with $\beta=\max_S\alpha^{\mathsf T}x$. As $S=-S$ spans $\mathbb R^n$ and $\alpha\ne0$, $\beta>0$, so the facet contains at most one of $\pm e_k$; it contains $n$ affinely independent points of $S$, hence exactly one $\sigma_ke_k$ ($\sigma_k=\pm1$) for each $k$, and these determine the hyperplane. Put $t_k=\sigma_k$ if $\sigma_0=-1$ and $t_k=-\sigma_k$ if $\sigma_0=1$, so $t_0=-1$; let $s_k=\frac{1+t_k}2\in\{0,1\}$, $s_n=1$, $a_i=s_i-s_{i-1}$. This $a$ is of the given type and $a^{\mathsf T}e_k=2s_k-1=t_k$. So the hyperplane $\alpha^{\mathsf T}x=\beta$ is $a^{\mathsf T}x=1$ (if $\sigma_0=-1$) or $a^{\mathsf T}x=-1$ (if $\sigma_0=1$), and since both halfspaces contain $0$, the facet inequality is one of ours. By @thm-facets-describe-polyhedra the listed inequalities describe $\operatorname{conv}(S)$.
:::
