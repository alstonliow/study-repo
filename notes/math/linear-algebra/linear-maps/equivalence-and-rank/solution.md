<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-las-1-q11" status="draft"}
Linearity: $\beta(\lambda\theta_1+\mu\theta_2)\alpha=\lambda\beta\theta_1\alpha+\mu\beta\theta_2\alpha$, since composition with linear maps distributes over sums and scalars (check on each $t\in T$).

The rank of $\Phi$ is $rs$.

1. By @thm-rank-normal-form choose bases $t_1,\dots$ of $T$ and $u_1,\dots$ of $U$ with $\alpha(t_j)=u_j$ for $j\le r$ and $\alpha(t_j)=0$ for $j>r$; and bases $v_1,\dots$ of $V$ and $w_1,\dots$ of $W$ with $\beta(v_i)=w_i$ for $i\le s$ and $\beta(v_i)=0$ for $i>s$.

2. Let $\theta$ have matrix $X=(x_{ij})$ in the bases $(u_j)$, $(v_i)$. For $j\le r$, $\beta\theta\alpha(t_j)=\beta\big(\sum_ix_{ij}v_i\big)=\sum_{i\le s}x_{ij}w_i$; for $j>r$ it is $0$.

3. So the matrix of $\Phi(\theta)$ keeps the entries $x_{ij}$ with $i\le s$, $j\le r$ and has zeros elsewhere. The image of $\Phi$ is the space of maps whose matrix vanishes outside the top-left $s\times r$ block, of dimension $rs$.
:::

::: {.solution for="prob-camib-las-2-q2" status="draft"}
Write $B=(b_1,\dots,b_n)$, and read $[\mathrm{id}_V]^C_B$ as the matrix of the identity from basis $C$ to basis $B$: its column $j$ holds the $B$-coordinates of $c_j$ (@def-matrix-of-linear-map).

1. Let $c_j=\sum_ip_{ij}b_i$. The coordinate map $V\to\mathbb F^n$ is an isomorphism sending $c_j$ to column $j$ of $P$; these columns form a basis of $\mathbb F^n$ because $P$ is invertible, so $C=(c_1,\dots,c_n)$ is a basis of $V$ (@thm-isomorphic-iff-same-dimension). By construction $[\mathrm{id}_V]^C_B=P$.

2. Apply step 1 to $P^{-1}$: there is a basis $D$ with $[\mathrm{id}_V]^D_B=P^{-1}$, namely $d_j=\sum_i(P^{-1})_{ij}b_i$.

3. By @thm-matrix-of-linear-map item 3, $[\mathrm{id}_V]^B_D\,[\mathrm{id}_V]^D_B=[\mathrm{id}_V]^D_D=I$, so $[\mathrm{id}_V]^B_D=(P^{-1})^{-1}=P$.
:::

::: {.solution for="prob-camib-las-2-q3" status="draft"}
1. Factorisations with $r'<r$ do not exist: if $A=BC$ with $B$ of size $m\times r'$, every column $A\mathbf e_j=B(C\mathbf e_j)$ lies in the column space of $B$, which has dimension $\le r'$. So $r\le r'$.

2. One exists with $r'=r$: let the columns of $B$ ($m\times r$) be a basis of the column space of $A$. Each column of $A$ is $B\mathbf c_j$ for some $\mathbf c_j\in\mathbb F^r$; let $C=[\mathbf c_1\ \cdots\ \mathbf c_n]$. Then $A=BC$.

3. Transposing, $A^{\mathsf T}=C^{\mathsf T}B^{\mathsf T}$ with $C^{\mathsf T}$ of size $n\times r$, so by step 1 applied to $A^{\mathsf T}$, $\operatorname{rk}A^{\mathsf T}\le r=\operatorname{rk}A$.

4. Applying step 3 to $A^{\mathsf T}$ gives $\operatorname{rk}A\le\operatorname{rk}A^{\mathsf T}$. So they are equal.
:::
