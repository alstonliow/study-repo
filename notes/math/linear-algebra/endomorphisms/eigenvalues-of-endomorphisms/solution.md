<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-las-2-q5" status="draft"}
(i) First part.

1. Suppose $v,\alpha v$ are dependent for every $v$. Then each $v\ne0$ is an eigenvector: $\alpha v=\lambda_vv$.

2. For independent $u,w$: $\lambda_{u+w}(u+w)=\alpha(u+w)=\lambda_uu+\lambda_ww$, so $\lambda_u=\lambda_{u+w}=\lambda_w$. For dependent non-zero $u,w=cu$, $\alpha w=c\lambda_uu=\lambda_uw$. So $\alpha=\lambda\iota$ for one $\lambda$.

3. Then $0=\operatorname{tr}\alpha=n\lambda$ with $n=\dim V\ge1$, so $\lambda=0$ and $\alpha=0$. Hence if $\alpha\ne0$ some $v,\alpha v$ are independent.

(i) Second part, by induction on $n$. For $n=1$, $\operatorname{tr}\alpha=0$ means $\alpha=0$. If $\alpha=0$ any basis works.

1. Otherwise take $v$ as above and extend $v_1=v$, $v_2=\alpha v$ to a basis $v_1,\dots,v_n$. Since $\alpha v_1=v_2$, the $(1,1)$ entry of the matrix is $0$.

2. Let $W=\langle v_2,\dots,v_n\rangle$, $\pi:V\to W$ the projection along $\langle v_1\rangle$, and $\alpha'=\pi\alpha|_W\in\operatorname{End}(W)$. Its matrix in $v_2,\dots,v_n$ is the bottom-right $(n-1)\times(n-1)$ block, so $\operatorname{tr}\alpha'=\operatorname{tr}\alpha-0=0$.

3. By induction $W$ has a basis $w_2,\dots,w_n$ in which $\alpha'$ has zero diagonal. In the basis $v_1,w_2,\dots,w_n$ of $V$: the $(1,1)$ entry is still $0$ since $\alpha v_1=v_2\in W$; and for $i\ge2$, the $w_i$-coordinate of $\alpha w_i$ equals that of $\pi\alpha w_i=\alpha'w_i$, which is $0$.

(ii)

1. Take a basis in which $\alpha$ has a matrix $A$ with zero diagonal, by (i).

2. Let $D=\operatorname{diag}(d_1,\dots,d_n)$ with distinct real $d_i$. For any $X$, $(DX-XD)_{ij}=(d_i-d_j)x_{ij}$.

3. Put $x_{ij}=a_{ij}/(d_i-d_j)$ for $i\ne j$ and $x_{ii}=0$. Then $DX-XD=A$, the diagonal entries agreeing because both are $0$. Let $\beta,\gamma$ be the endomorphisms with matrices $D,X$.
:::

::: {.solution for="prob-camib-las-3-q4" status="draft"}
1. If $\alpha v=\lambda v$ with $v\ne0$, then $\alpha^2v=\lambda^2v$.

2. Let $\mu$ be an eigenvalue of $\alpha^2$ and $\nu\in\mathbb C$ with $\nu^2=\mu$. Then $\alpha^2-\mu\iota=(\alpha-\nu\iota)(\alpha+\nu\iota)$ is not injective, so one of the two factors is not injective: $\nu$ or $-\nu$ is an eigenvalue of $\alpha$, and its square is $\mu$.

3. The eigenspaces can differ. For $\alpha=\operatorname{diag}(1,-1)$ on $\mathbb C^2$ and $\lambda=1$: $\ker(\alpha-\iota)=\langle e_1\rangle$, but $\alpha^2=\iota$ and $\ker(\alpha^2-\iota)=\mathbb C^2$. (Also $\alpha=\begin{pmatrix}0&1\\0&0\end{pmatrix}$, $\lambda=0$: $\ker\alpha=\langle e_1\rangle$, $\ker\alpha^2=\mathbb C^2$.) Always $\ker(\alpha-\lambda\iota)\subseteq\ker(\alpha^2-\lambda^2\iota)$.
:::

::: {.solution for="prob-camib-las-3-q12" status="draft"}
1. $p(\lambda)=\det(A+\lambda B)$ is a polynomial in $\lambda$ (expand the determinant, @def-determinant-leibniz) with real coefficients. $p(i)=\det C\ne0$, so $p$ is not the zero polynomial and has finitely many roots (@thm-at-most-d-roots). Any real $\lambda$ that is not a root makes $A+\lambda B$ invertible.

2. Let $Q=X^{-1}PX$ with $X\in\operatorname{GL}_n(\mathbb C)$, so $XQ=PX$. Write $X=A+iB$ with $A,B$ real. Taking real and imaginary parts (as $P,Q$ are real), $AQ=PA$ and $BQ=PB$.

3. Hence $(A+\lambda B)Q=P(A+\lambda B)$ for every real $\lambda$. By step 1 choose $\lambda$ with $Y=A+\lambda B$ invertible; then $Q=Y^{-1}PY$ with $Y$ real.
:::

::: {.solution for="prob-camib-las-3-q13" status="draft"}
Let $N=n+1$ and index rows and columns by $0,\dots,n$. Then $C_{rs}=a_{(s-r)\bmod N}$.

1. Let $S$ be the circulant with $a_1=1$ and all other $a_k=0$: $S_{rs}=1$ iff $s\equiv r+1\pmod N$. Then $(S^k)_{rs}=1$ iff $s\equiv r+k$, so $C=\sum_ka_kS^k=f(S)$.

2. For $j=0,\dots,n$ let $v_j=(1,\zeta^j,\zeta^{2j},\dots,\zeta^{nj})^{\mathsf T}$. Then $(Sv_j)_r=(v_j)_{r+1}=\zeta^j(v_j)_r$, using $\zeta^{jN}=1$ for the last row. So $Sv_j=\zeta^jv_j$.

3. The $\zeta^j$ are $N$ distinct numbers, so the $v_j$ form a basis of eigenvectors (@lem-eigenspaces-independent), and $Cv_j=f(S)v_j=f(\zeta^j)v_j$ (@prp-eigenvalue-root-of-minimal-polynomial).

4. With $V=[v_0\ \cdots\ v_n]$, $V^{-1}CV=\operatorname{diag}(f(1),f(\zeta),\dots,f(\zeta^n))$, and $\det C=\det(V^{-1}CV)=\prod_{j=0}^nf(\zeta^j)$.
:::
