<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-las-1-q8" status="draft"}
1. (i)⇒(ii): if $v\in U_j\cap\sum_{i\ne j}U_i$, write $v=\sum_{i\ne j}u_i$. Then $v$ has two expressions, $v$ in slot $j$ and $0$ elsewhere, or $u_i$ in the slots $i\ne j$ and $0$ in slot $j$. By uniqueness $v=0$.

2. (ii)⇒(iii), independence: suppose a finite combination of vectors from the $B_i$ is $0$, and let $u_i\in U_i$ collect the terms from $B_i$. Then $\sum_iu_i=0$, so $u_j=-\sum_{i\ne j}u_i\in U_j\cap\sum_{i\ne j}U_i=\{0\}$ for every $j$. As $B_j$ is independent, the coefficients of its vectors vanish. (If a vector $b$ lay in $B_i\cap B_j$ with $i\ne j$, then $b\in U_j\cap\sum_{i\ne j}U_i$, so $b=0$, impossible for a basis vector; so the $B_i$ are disjoint and the union has no repeated vector.)

3. (ii)⇒(iii), spanning: every $\sum u_i$ is a combination of the $B_i$.

4. (iii)⇒(i): existence of an expression is $U=\sum U_i$. If $\sum u_i=\sum u_i'$, expand each $u_i-u_i'$ in $B_i$; this gives a combination of the union equal to $0$, and because the $B_i$ are disjoint, the coefficient of each basis vector of the union comes from one $B_i$ only. So all coefficients are $0$ and $u_i=u_i'$.

Example: in $\mathbb R^2$, $U_1=\langle e_1\rangle$, $U_2=\langle e_2\rangle$, $U_3=\langle e_1+e_2\rangle$ meet pairwise in $\{0\}$, but $e_1+e_2$ has two expressions, $e_1+e_2+0$ and $0+0+(e_1+e_2)$.
:::

::: {.solution for="prob-camib-las-1-q9" status="draft"}
Let $U,W\le V$ with $\dim U=\dim W=k$ and $\dim V=n$. Induction on $n-k$.

1. If $k=n$, then $U=W=V$ and $\{0\}$ is a common complement.

2. If $k<n$, then $U$ and $W$ are proper subspaces, and $U\cup W\ne V$: otherwise $U\cup W$ would be a subspace, so $U\le W$ or $W\le U$ (Q2(i) of this sheet), and $V=U\cup W$ would equal $U$ or $W$.

3. Pick $v\notin U\cup W$. Then $U'=U+\langle v\rangle$ and $W'=W+\langle v\rangle$ have dimension $k+1$. By induction they have a common complement $X'$.

4. Let $X=\langle v\rangle+X'$. Then $U+X=U'+X'=V$, and $\dim U+\dim X\le k+1+(n-k-1)=n$. By @prp-direct-sum-criteria (dimension count) $V=U\oplus X$, and $\dim X=n-k$. The same holds for $W$.
:::
