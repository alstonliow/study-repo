<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-las-3-q6" status="draft"}
1. If $N=P^{-1}MP$, then $N-I=P^{-1}(M-I)P$, so $M-I$ and $N-I$ have the same rank. For the three matrices, $M-I$ has rank $2$, $1$ and $0$. So no two are similar.

2. Let $N$ be the fourth matrix. $\chi_N(t)=(t-1)^3$ and
$$N-I=\begin{pmatrix}-3&-2&-1\\3&2&1\\3&2&1\end{pmatrix}$$
has rank $1$ (all rows are multiples of $(3,2,1)$), and $(N-I)^2=0$. By step 1 it can only be similar to the second matrix, and it is, by the basis below.

3. Jordan basis: $w=e_1$ has $(N-I)w=(-3,3,3)^{\mathsf T}=:v_1\ne0$; put $v_2=e_1$, and choose $v_3=(-2,3,0)^{\mathsf T}\in\ker(N-I)$ (it satisfies $3x+2y+z=0$), independent of $v_1$. Then $Nv_1=v_1$ (as $(N-I)^2=0$), $Nv_2=v_2+v_1$, $Nv_3=v_3$, so with $P=[v_1\ v_2\ v_3]$ (determinant $9$),
$$P^{-1}NP=\begin{pmatrix}1&1&0\\0&1&0\\0&0&1\end{pmatrix}.$$
:::

::: {.solution for="prob-camib-las-3-q7" status="draft"}
$A=J_2(0)\oplus J_2(0)$ and $B=J_2(0)\oplus J_1(0)\oplus J_1(0)$. Both have $\chi=t^4$ and, since $A^2=B^2=0\ne A,B$, $m=t^2$. But $\operatorname{rk}A=2$ and $\operatorname{rk}B=1$, so they are not similar (similar matrices have equal rank), and they are different Jordan normal forms.
:::

::: {.solution for="prob-camib-las-3-q9" status="draft"}
Write $J=J_n(\lambda)=\lambda I+N$, where $Ne_1=0$ and $Ne_i=e_{i-1}$.

Case $\lambda\ne0$: the Jordan normal form is $J_n(\lambda^k)$.

1. By the binomial theorem ($N$ commutes with $I$), $J^k-\lambda^kI=\sum_{j\ge1}\binom kj\lambda^{k-j}N^j=NU$ with $U=k\lambda^{k-1}I+\binom k2\lambda^{k-2}N+\dots$, which is upper triangular with non-zero diagonal $k\lambda^{k-1}$, hence invertible, and commutes with $N$.

2. So $(J^k-\lambda^kI)^r=N^rU^r$ has the rank of $N^r$, namely $n-r$ for $r\le n$. By @thm-jordan-block-count the number of blocks of size $\ge r$ is $(r)-(r-1)=1$ for $1\le r\le n$: a single block $J_n(\lambda^k)$.

Case $\lambda=0$: $J^k=N^k$ sends $e_i\mapsto e_{i-k}$ (and to $0$ if $i\le k$).

1. The basis splits into chains by residue mod $k$: for $c=1,\dots,\min(k,n)$, the vectors $e_c,e_{c+k},e_{c+2k},\dots$ (up to $n$) form a chain $e_{c+jk}\mapsto e_{c+(j-1)k}\mapsto\dots\mapsto e_c\mapsto0$, giving a block $J_\ell(0)$ with $\ell$ the length of the chain.

2. Write $n=qk+r$ with $0\le r<k$. The residues $c\le r$ give chains of length $q+1$, the others length $q$. So the Jordan normal form of $J_n(0)^k$ is $r$ blocks $J_{q+1}(0)$ and $k-r$ blocks $J_q(0)$ (omitting blocks of size $0$; if $k\ge n$ this is $N^k=0$, $n$ blocks of size $1$). For example $J_7(0)^2\sim J_4(0)\oplus J_3(0)$ and $J_7(0)^3\sim J_3(0)\oplus J_2(0)\oplus J_2(0)$.
:::

::: {.solution for="prob-camib-las-3-q11" status="draft"}
(a) Let $A$ be $n\times n$.

1. $Av=\lambda v$ iff $A^{-1}v=\lambda^{-1}v$ (all eigenvalues of $A$ are non-zero), so the eigenvalues of $A^{-1}$ are the inverses of those of $A$, with the same eigenvectors.

2. $\chi_{A^{-1}}(t)=\det(tI-A^{-1})=\det(A^{-1})\det(tA-I)=\det(A^{-1})(-t)^n\det(t^{-1}I-A)$ for $t\ne0$. Since $\chi_A(0)=(-1)^n\det A$,
$$\chi_{A^{-1}}(t)=\frac{t^n\chi_A(1/t)}{\chi_A(0)},$$
the reversed polynomial, made monic (an identity of polynomials, as both sides agree for all $t\ne0$).

3. If $m_A$ has degree $d$, then $m_A(0)\ne0$ (@cor-minimal-and-characteristic-same-roots) and $q(t)=t^dm_A(1/t)/m_A(0)$ is monic of degree $d$ with $q(A^{-1})=A^{-d}m_A(A)/m_A(0)=0$. So $\deg m_{A^{-1}}\le\deg m_A$, and by symmetry they are equal; as $q$ is monic of the minimal degree, $m_{A^{-1}}=q$, the monic reversal of $m_A$.

(b)

1. Let $J=J_m(\lambda)=\lambda I+N$. Then $J^{-1}$ has only the eigenvalue $\lambda^{-1}$, and
$$J^{-1}-\lambda^{-1}I=J^{-1}\lambda^{-1}(\lambda I-J)=-\lambda^{-1}J^{-1}N.$$

2. $J^{-1}$ commutes with $N$, so $(J^{-1}-\lambda^{-1}I)^r=(-\lambda)^{-r}J^{-r}N^r$ has the rank of $N^r$, which is $m-r$ for $r\le m$. By @thm-jordan-block-count there is exactly one block, of size $m$: $J^{-1}\sim J_m(\lambda^{-1})$.

3. If $A=PJP^{-1}$ with $J=\bigoplus_iJ_{m_i}(\lambda_i)$, then $A^{-1}=P\big(\bigoplus_iJ_{m_i}(\lambda_i)^{-1}\big)P^{-1}$, and each block is similar to $J_{m_i}(\lambda_i^{-1})$. So the Jordan normal form of $A^{-1}$ is $\bigoplus_iJ_{m_i}(\lambda_i^{-1})$: same block sizes, inverted eigenvalues.

(c)

1. Let $R$ be the $m\times m$ reversal permutation, $Re_i=e_{m+1-i}$, so $R=R^{-1}$. Then $RJ_m(\lambda)R=J_m(\lambda)^{\mathsf T}$: conjugating by $R$ reverses the order of rows and columns, moving the superdiagonal to the subdiagonal.

2. If $A=PJP^{-1}$ with $J$ in Jordan normal form, let $R'$ be the block diagonal matrix of reversals. Then $J^{\mathsf T}=R'JR'$ and $A^{\mathsf T}=(P^{-1})^{\mathsf T}J^{\mathsf T}P^{\mathsf T}=(P^{\mathsf T})^{-1}R'P^{-1}\,A\,PR'P^{\mathsf T}$, which is similar to $A$.
:::
