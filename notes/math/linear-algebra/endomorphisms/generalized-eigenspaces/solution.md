<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-las-3-q8" status="draft"}
We prove slightly more: if $p(\alpha)=0$ for some $p=\prod_{i=1}^k(t-\lambda_i)^{c_i}$ with distinct $\lambda_i$ (any exponents), then $V=\bigoplus_i\ker(\alpha-\lambda_i\iota)^{c_i}$; the theorem is the case $p=m_\alpha$. Induction on $k$, splitting off one eigenvalue at a time; $k=1$ is clear since then $V=\ker(\alpha-\lambda_1\iota)^{c_1}$. Let $N=\dim V$.

1. For any $\beta\in\operatorname{End}(V)$, the kernels $\ker\beta^j$ increase with $j$ and their dimensions are at most $N$, so by the rank argument of Sheet 1 Q6 they stop growing by $j=N$: $\ker\beta^N=\ker\beta^{2N}$.

2. Then $V=\ker\beta^N\oplus\operatorname{im}\beta^N$. If $v=\beta^Nw$ lies in both, then $\beta^{2N}w=0$, so $w\in\ker\beta^N$ and $v=0$; the dimensions add up to $N$ by @thm-rank-nullity.

3. Take $\beta=\alpha-\lambda_1\iota$, $K=\ker\beta^N$, $I=\operatorname{im}\beta^N$. Both are $\alpha$-invariant, since $\alpha$ commutes with $\beta$. On $K$, the only eigenvalue of $\alpha$ is $\lambda_1$: if $\alpha v=\mu v$ with $0\ne v\in K$, then $0=\beta^Nv=(\mu-\lambda_1)^Nv$. On $I$, $\lambda_1$ is not an eigenvalue: $\ker\beta\cap I\subseteq K\cap I=\{0\}$.

4. $K=\ker(\alpha-\lambda_1\iota)^{c_1}$. "$\supseteq$": if $c_1>N$ the kernels have stabilised, and otherwise $\ker\beta^{c_1}\subseteq\ker\beta^N$. "$\subseteq$": $p=(t-\lambda_1)^{c_1}q$ with $q=\prod_{i\ge2}(t-\lambda_i)^{c_i}$; each factor $\alpha-\lambda_i\iota$ ($i\ge2$) is injective on $K$ by step 3, so $q(\alpha)|_K$ is invertible, and $0=p(\alpha)|_K=q(\alpha)|_K(\alpha-\lambda_1\iota)^{c_1}|_K$ forces $(\alpha-\lambda_1\iota)^{c_1}K=0$.

5. For $i\ge2$, $V_i=\ker(\alpha-\lambda_i\iota)^{c_i}\subseteq I$: write $v\in V_i$ as $k+x$ with $k\in K$, $x\in I$; both parts lie in $V_i$ by invariance, and $(\alpha-\lambda_i\iota)$ is injective on $K$, so $k=0$.

6. $\alpha|_I$ is killed by $q$: $0=p(\alpha)|_I=(\alpha-\lambda_1\iota)^{c_1}q(\alpha)|_I$, and $(\alpha-\lambda_1\iota)^{c_1}$ is injective on $I$. By induction applied to $\alpha|_I$ and $q$ (with $k-1$ factors), $I=\bigoplus_{i\ge2}\big(\ker(\alpha-\lambda_i\iota)^{c_i}\cap I\big)=\bigoplus_{i\ge2}V_i$, using step 5. With step 2, $V=V_1\oplus V_2\oplus\dots\oplus V_k$.
:::

::: {.solution for="prob-camib-las-3-q10" status="draft"}
1. Choose $y$ with $\alpha^{n-1}y\ne0$. Suppose $\sum_{i=0}^{n-1}c_i\alpha^iy=0$ with not all $c_i=0$, and let $i_0$ be the least index with $c_{i_0}\ne0$. Applying $\alpha^{n-1-i_0}$ kills every term with $i>i_0$ (as $\alpha^n=0$) and leaves $c_{i_0}\alpha^{n-1}y=0$, a contradiction. So the $n$ vectors are independent, hence a basis.

2. In the basis $(y,\alpha y,\dots,\alpha^{n-1}y)$, $\alpha$ sends each vector to the next and the last to $0$: its matrix has $1$s on the subdiagonal (entries $(i+1,i)$) and $0$ elsewhere. $\alpha^k$ sends $\alpha^iy\mapsto\alpha^{i+k}y$, so its matrix has $1$s in positions $(i+k,i)$, the $k$-th subdiagonal, and is $0$ for $k\ge n$.

3. Let $\beta\alpha=\alpha\beta$. Write $\beta(y)=\sum_{i=0}^{n-1}c_i\alpha^iy=p(\alpha)y$ with $p(t)=\sum_ic_it^i$. Then for each $j$,
$$\beta(\alpha^jy)=\alpha^j\beta(y)=\alpha^jp(\alpha)y=p(\alpha)(\alpha^jy).$$
So $\beta$ and $p(\alpha)$ agree on a basis, and $\beta=p(\alpha)$.

4. By step 2 the matrix of $\beta=\sum c_i\alpha^i$ is lower triangular and constant along diagonals (Toeplitz): $c_0$ on the diagonal, $c_1$ on the first subdiagonal, ..., $c_{n-1}$ in the bottom-left corner.
:::
