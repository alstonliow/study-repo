<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18650f16-10-q3" status="draft"}
1. $\Sigma=E[(X-\mu)(X-\mu)']$ with $\mu=E[X]$; it is $p\times p$, with entries $\operatorname{Cov}(X_j,X_k)$ (@def-covariance-matrix).

2. $\hat\Sigma=\frac1n\sum_{i=1}^n(X^i-\bar X)(X^i-\bar X)'$ with $\bar X=\frac1n\sum_iX^i$ (some texts divide by $n-1$; nothing below changes).

3. For $u\in\mathbb{R}^p$, $u'\Sigma u=E[(u'(X-\mu))^2]\ge0$; $\Sigma$ is symmetric by definition.

4. $u'\hat\Sigma u=\frac1n\sum_i\bigl(u'(X^i-\bar X)\bigr)^2\ge0$, and $\hat\Sigma$ is symmetric.

5. a) $E[AX]=A\mu$ and $(AX-A\mu)(AX-A\mu)'=A(X-\mu)(X-\mu)'A'$. Taking expectations, which commute with the fixed matrices $A$ and $A'$ by linearity, $\operatorname{Cov}(AX)=A\Sigma A'$.

   b) No. $\operatorname{rank}(A\Sigma A')\le\operatorname{rank}A\le p<q$, so the $q\times q$ matrix $A\Sigma A'$ is singular. (The vector $AX$ lies in the column space of $A$, of dimension at most $p$, so it is degenerate.)

   c) Take $A=u'$ ($q=1$): $\operatorname{Var}(u'X)=u'\Sigma u$.

6. a) The sample mean of the $BX^i$ is $B\bar X$, and $(BX^i-B\bar X)(BX^i-B\bar X)'=B(X^i-\bar X)(X^i-\bar X)'B'$; averaging gives $B\hat\Sigma B'$.

   b) $u'\hat\Sigma u$ (take $B=u'$), as in @prp-directional-variance.

7. Let $Z=AX$, with mean $A\mu$ and covariance $A\Sigma A'$ by 5(a). Then
$$E[X'A'AX]=E\|Z\|^2=\sum_{j=1}^kE[Z_j^2]=\sum_{j=1}^k\bigl(\operatorname{Var}(Z_j)+(E[Z_j])^2\bigr)=\operatorname{Tr}(A\Sigma A')+\|A\mu\|_2^2 .$$
:::
