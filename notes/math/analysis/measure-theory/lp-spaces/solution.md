<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camii-pms-4-q5" status="draft"}
1. Write $f=f^+-f^-$; by Minkowski it suffices to approximate $f\ge0$. Let $f_n=\min(2^{-n}\lfloor2^nf\rfloor,n)\mathbf 1_{[-n,n]}$. These are simple, vanish outside $[-n,n]$, take finitely many values, and $f_n\uparrow f$ a.e. Since $|f-f_n|^p\le f^p$, dominated convergence gives $\|f-f_n\|_p\to0$.

2. Each $f_n$ is a finite combination $\sum_ka_k\mathbf 1_{B_k}$ with $B_k$ Borel of finite measure. By Minkowski it suffices to approximate one $\mathbf 1_B$.

3. By problem 1.8, there is a finite disjoint union of intervals $A$ with $\lambda(A\triangle B)<\delta$; then $\|\mathbf 1_A-\mathbf 1_B\|_p=\lambda(A\triangle B)^{1/p}<\delta^{1/p}$, and $\mathbf 1_A\in\mathcal I$. This proves density of $\mathcal I$.

4. For the second claim it suffices to approximate $\mathbf 1_{(a,b]}$ (Minkowski again; the type of end points does not matter, single points being null). The continuous function $h_k$ equal to $1$ on $[a,b]$, $0$ outside $(a-\frac1k,b+\frac1k)$ and linear in between satisfies $\|h_k-\mathbf 1_{(a,b]}\|_p^p\le\frac2k\to0$.
:::

::: {.solution for="prob-camii-pms-5-q1" status="draft"}
1. Let $V$ be the closure of $\bigcup_nV_n$, a closed subspace (closures of subspaces are subspaces), and $g$ the projection of $f$ on $V$ (@thm-l2-orthogonal-projection).

2. $f_n$ is also the projection of $g$ on $V_n$: indeed $g-f_n=(f-f_n)-(f-g)$, where $f-f_n\perp V_n$ and $f-g\perp V\supseteq V_n$; so $g=f_n+(g-f_n)$ is the decomposition of $g$ along $V_n$. Hence $\|g-f_n\|_2=\inf_{w\in V_n}\|g-w\|_2$.

3. Given $\varepsilon>0$, pick $h\in\bigcup_nV_n$ with $\|g-h\|_2<\varepsilon$, say $h\in V_N$. For $n\ge N$, $h\in V_n$, so $\|g-f_n\|_2\le\|g-h\|_2<\varepsilon$.

4. Hence $f_n\to g$ in $L^2$.
:::

::: {.solution for="prob-camii-pms-5-q2" status="draft"}
1. The entries are finite: $|\operatorname{cov}(X_i,X_j)|\le\|X_i-E X_i\|_2\|X_j-EX_j\|_2$ by Cauchy–Schwarz. The matrix is symmetric.

2. For $a\in\mathbb R^n$, bilinearity of covariance gives
$$a^{\mathsf T}\operatorname{var}(X)\,a=\sum_{i,j}a_ia_j\operatorname{cov}(X_i,X_j)=\operatorname{Var}\Big(\sum_ia_iX_i\Big)=E\Big[\Big(\sum_ia_i(X_i-EX_i)\Big)^2\Big]\ge0 .$$
:::
