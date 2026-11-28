<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-12-q1" status="draft"}
Write $X=\sum_iX_i$ with $X_i$ the indicator that $i$ is isolated, and $q=1-p$. Then $\mathrm{Var}(X_i)=q^{n-1}(1-q^{n-1})$, and for $i\ne j$, $\mathrm{Cov}(X_i,X_j)=E[X_iX_j]-E[X_i]E[X_j]=q^{2n-3}-q^{2n-2}$ (both are isolated when the $2n-3$ edges at $i$ or $j$ are absent). By @prp-covariance-properties,
$$\mathrm{Var}(X)=nq^{n-1}(1-q^{n-1})+n(n-1)\bigl(q^{2n-3}-q^{2n-2}\bigr).$$
This agrees with HW 11 Q4(b).
:::

::: {.solution for="prob-cs70hw-12-q2" status="draft"}
Take $c=0$, $d=1$ (so $\tilde Y=Y$), $a=1$ and $b=-\frac{\mathrm{Cov}(X,Y)}{\mathrm{Var}(Y)}$. Then $ad-bc=1\ne0$, and by bilinearity (@prp-covariance-properties)
$$\mathrm{Cov}(\tilde X,Y)=\mathrm{Cov}(X,Y)+b\,\mathrm{Var}(Y)=0.$$
:::

::: {.solution for="prob-mit6041f10-4-q5" status="draft"}
Let $I_t$ indicate a head at time $t-1$ and a tail at time $t$, so $R=I_1+\dots+I_n$, and let $q=p(1-p)=E[I_t]$.

1. Linearity: $E[R]=nq=np(1-p)$.

2. $\mathrm{Var}(I_t)=q(1-q)$.

3. $I_t$ and $I_{t+1}$ cannot both be $1$ (toss $t$ would be a tail and a head), so $\mathrm{Cov}(I_t,I_{t+1})=0-q^2$. Indicators two or more apart use disjoint tosses and are independent.

4. Hence
$$\mathrm{Var}(R)=nq(1-q)-2(n-1)q^2,\qquad q=p(1-p).$$
:::

::: {.solution for="prob-mit6041f10-6-q3" status="draft"}
(a) Negatively correlated: the counts add up to $n$, so more 1's leave fewer tosses for 2's.

(b) Write $X_1=\sum_tA_t$ and $X_2=\sum_tB_t$ with $A_t,B_t$ indicating that toss $t$ shows $1$, respectively $2$.

1. For $s\ne t$, $A_s$ and $B_t$ are independent, so $\mathrm{Cov}(A_s,B_t)=0$.

2. For $s=t$, $A_tB_t=0$, so $\mathrm{Cov}(A_t,B_t)=0-\frac1k\cdot\frac1k$.

3. By bilinearity, $\mathrm{Cov}(X_1,X_2)=-\frac n{k^2}$.
:::

::: {.solution for="prob-mit1805s22-5-q3" status="draft"}
(a) The marginals force $P(X=1,Y=-1)=\frac12-c$, $P(X=-1,Y=1)=\frac12-c$ and then $P(X=-1,Y=-1)=c$, with $0\le c\le\frac12$. Both means are $0$ and both variances $1$, so
$$\mathrm{Cov}(X,Y)=E[XY]=c-\bigl(\tfrac12-c\bigr)-\bigl(\tfrac12-c\bigr)+c=4c-1=\mathrm{Cor}(X,Y).$$

(b) Independence needs $P(X=1,Y=1)=\frac14$, i.e. $c=\frac14$; then all four cells are $\frac14$, which is the product of the marginals. The correlation is $1$ when $c=\frac12$ (then $Y=X$); it is $-1$ when $c=0$ (then $Y=-X$).
:::

::: {.solution for="prob-mit1805s22-5-q5" status="draft"}
1. $X=\sum_{i=1}^nX_i$ and $Y=\sum_{j=n-7}^{2n-8}X_j$; each is a sum of $n$ terms, so $\mathrm{Var}(X)=\mathrm{Var}(Y)=n/4$.

2. By bilinearity, $\mathrm{Cov}(X,Y)=\sum_i\sum_j\mathrm{Cov}(X_i,X_j)$. Independent terms contribute $0$ and $\mathrm{Cov}(X_i,X_i)=\frac14$, so only the shared indices $n-7,\dots,n$ count; there are $8$ of them. Hence $\mathrm{Cov}(X,Y)=\frac84=2$.

3. $\mathrm{Cor}(X,Y)=\dfrac2{\sqrt{(n/4)(n/4)}}=\dfrac8n$.
:::
