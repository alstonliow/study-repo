<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18433-3-q7" status="draft"}
There is $y\ne0$ with $Ay=0$. For any $x\in P$, both $x+y$ and $x-y$ satisfy $A(x\pm y)=Ax\le b$, so they lie in $P$, and $x=\frac12(x+y)+\frac12(x-y)$ with $x+y\ne x-y$. So no point of $P$ is an extreme point.
:::

::: {.solution for="prob-mit18433-3-q8" status="draft"}
1. Let $v$ be a vertex of $Q$ and suppose $v=\lambda y+(1-\lambda)z$ with $y,z\in P$ and $0<\lambda<1$.

2. The inequality $\mathbf 1^{\mathsf T}Cx\le\mathbf 1^{\mathsf T}d$ (the sum of the rows $Cx\le d$) holds for $y$ and $z$, and with equality for $v\in Q$. Since $\mathbf 1^{\mathsf T}Cv$ is the weighted average of $\mathbf 1^{\mathsf T}Cy$ and $\mathbf 1^{\mathsf T}Cz$, both must equal $\mathbf 1^{\mathsf T}d$; together with $Cy\le d$ and $Cz\le d$ this gives $Cy=Cz=d$.

3. So $y,z\in Q$, and since $v$ is extreme in $Q$, $y=z=v$. Hence $v$ is extreme in $P$, i.e. a vertex of $P$.
:::

::: {.solution for="prob-mit18433-3-q9" status="draft"}
*Answer:* $M_1\ne M_2$ are adjacent if and only if $M_1\triangle M_2$ is a single cycle. Every vertex has degree $0$ or $2$ in $M_1\triangle M_2$ (both matchings are perfect), so it is a disjoint union of even cycles $C_1,\dots,C_r$ alternating between $M_1$ and $M_2$, with $r\ge1$.

1. *Sufficient ($r=1$).* Let $c_e=0$ for $e\in M_1\cup M_2$ and $c_e=1$ otherwise. A perfect matching of cost $0$ uses only edges of $M_1\cup M_2$. Outside $C_1$ every vertex has only its edge of $M_1\cap M_2$ there, so that edge is forced; on the even cycle $C_1$ the only perfect matchings are its two alternating halves. So $M_1$ and $M_2$ are the only minimisers.

2. *Necessary.* If $r\ge2$, let $N=M_1\triangle C_1$ and $N'=M_2\triangle C_1$, two perfect matchings different from $M_1$ and $M_2$ (they differ from $M_1$ on $C_1$ or on $C_2$). On each cycle one of $N,N'$ agrees with $M_1$ and the other with $M_2$, so $\chi_N+\chi_{N'}=\chi_{M_1}+\chi_{M_2}$. If some $c$ were minimised exactly by $M_1$ and $M_2$, then $c(N)+c(N')=c(M_1)+c(M_2)$ would force $N,N'$ to be minimisers too: a contradiction.
:::

::: {.solution for="prob-mit18433-3-q10" status="draft"}
We assume $P$ is bounded (a polytope), so every face is the convex hull of its vertices (@thm-minkowski-polytope). Let $m=\frac12(u+v)$ and use the description of adjacency by a cost $c$ from exercise 9.

1. *Adjacent $\Rightarrow$ unique.* Let $c$ be minimised over $P$ exactly at the vertices $u$, $v$, with value $z^*$. If $m=\sum_w\lambda_ww$ is a convex combination of vertices, then $z^*=c^{\mathsf T}m=\sum_w\lambda_wc^{\mathsf T}w$ with every $c^{\mathsf T}w\ge z^*$, so $\lambda_w>0$ only for $w\in\{u,v\}$. Then $m=\lambda_uu+(1-\lambda_u)v$ gives $(\lambda_u-\frac12)(u-v)=0$, so $\lambda_u=\frac12$: the representation is unique.

2. *Unique $\Rightarrow$ adjacent.* Let $I$ be the set of rows tight at $m$ and $F=F_I$ the face they define (@thm-faces-tight-rows). Since $m$ is the midpoint of $u,v\in P$, every row tight at $m$ is tight at $u$ and $v$; so $u,v\in F$. If $u$ and $v$ were the only vertices of $F$, then $F=\operatorname{conv}\{u,v\}$ would be a face of dimension $1$ and $u,v$ adjacent. Otherwise $F$ has another vertex $w$.

3. For small $\varepsilon>0$ the point $p=m-\varepsilon(w-m)$ lies in $F$: rows of $I$ stay tight (they are tight at $m$ and $w$) and the other rows are strict at $m$. Writing $p$ as a convex combination of vertices of $F$ gives $m=\frac{\varepsilon}{1+\varepsilon}w+\frac1{1+\varepsilon}p$, a representation of $m$ in which $w\notin\{u,v\}$ has positive weight, different from $\frac12u+\frac12v$.
:::
