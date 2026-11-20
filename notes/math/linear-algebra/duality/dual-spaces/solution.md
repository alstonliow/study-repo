<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-las-2-q8" status="draft"}
1. $\tau_A$ is linear: $\operatorname{tr}(A(\lambda B+\mu B'))=\lambda\operatorname{tr}(AB)+\mu\operatorname{tr}(AB')$, since matrix multiplication and trace are linear.

2. $A\mapsto\tau_A$ is linear: $\tau_{\lambda A+\mu A'}(B)=\lambda\tau_A(B)+\mu\tau_{A'}(B)$ for every $B$.

3. Injective: let $E_{ji}\in\mathbb M_{m\times n}(\mathbb F)$ have a $1$ in position $(j,i)$ and $0$ elsewhere. Then $(AE_{ji})_{kl}=a_{kj}[l=i]$, so $\tau_A(E_{ji})=a_{ij}$. If $\tau_A=0$, every entry of $A$ is $0$.

4. Both spaces have dimension $nm$ (@thm-dual-basis), so the injective linear map is an isomorphism (@cor-injective-iff-surjective).
:::

::: {.solution for="prob-camib-las-2-q9" status="draft"}
(a) Let $E_{ij}$ be the matrix units, so $E_{ij}E_{kl}=[j=k]E_{il}$.

1. For $i\ne j$: $E_{ij}=E_{ij}E_{jj}$ and $E_{jj}E_{ij}=0$, so $f(E_{ij})=f(E_{jj}E_{ij})=f(0)=0$.

2. $E_{ii}=E_{ij}E_{ji}$ and $E_{jj}=E_{ji}E_{ij}$, so $f(E_{ii})=f(E_{jj})$ for all $i,j$; call the common value $c$.

3. $n=f(I)=\sum_if(E_{ii})=nc$, so $c=1$. By linearity $f(A)=\sum_{i,j}a_{ij}f(E_{ij})=\sum_ia_{ii}=\operatorname{tr}A$.

(b) $\operatorname{tr}(\alpha\beta-\beta\alpha)=0$ by @lem-trace-cyclic, while $\operatorname{tr}\mathrm{id}_V=\dim V\ne0$ in $\mathbb R$.

(c) $\alpha=d/dx$ and $\beta=$ multiplication by $x$: $(\alpha\beta-\beta\alpha)f=(xf)'-xf'=f$.
:::

::: {.solution for="prob-camib-las-2-q10" status="draft"}
(a) If $\det A=0$, the rows of $A$ are dependent (@thm-determinant-invertible with @lem-determinant-transpose): $\sum_kc_k(a_0^k,\dots,a_n^k)=0$ with $(c_0,\dots,c_n)\ne0$. Then $p(t)=\sum_kc_kt^k$ is a non-zero polynomial of degree $\le n$ with the $n+1$ distinct roots $a_0,\dots,a_n$, contradicting @thm-at-most-d-roots.

(b) Here $e_0,\dots,e_n$ are evaluation at $0,1,\dots,n$; take $a_i=i$ in (a). Let $\varepsilon_0,\dots,\varepsilon_n$ be the basis dual to $1,t,\dots,t^n$. By @thm-dual-basis, $e_{a_j}=\sum_ke_{a_j}(t^k)\varepsilon_k=\sum_ka_j^k\varepsilon_k$, so the coordinate column of $e_{a_j}$ is column $j$ of $A$. These columns are independent since $\det A\ne0$; $n+1$ independent vectors in the $(n+1)$-dimensional space $P_n^*$ form a basis.

(c) The Lagrange polynomials
$$p_j(t)=\prod_{i\ne j}\frac{t-i}{j-i}\qquad(j=0,\dots,n),$$
which have degree $n$ and satisfy $e_i(p_j)=p_j(i)=\delta_{ij}$. (They form a basis of $P_n$ by the duality: if $\sum c_jp_j=0$, applying $e_i$ gives $c_i=0$.)
:::
