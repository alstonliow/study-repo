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
