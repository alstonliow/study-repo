<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18650f16-3-q1" status="draft"}
Write $\ell_n(\theta)=\sum_i\log f_\theta(X_i)$. In cases 1, 3, 4, 5 the support does not depend on $\theta$, $\ell_n$ has a single critical point, and $\ell_n\to-\infty$ at both ends of $(0,\infty)$, so the critical point is the maximum.

1. $\ell_n(\theta)=n\log\theta+n\theta\log\tau-(\theta+1)\sum_i\log X_i$, so $\ell_n'(\theta)=\frac n\theta-\sum_i\log(X_i/\tau)$ and
$$\hat\theta=\frac n{\sum_{i=1}^n\log(X_i/\tau)} .$$

2. The likelihood is $\tau^n\theta^{n\tau}\prod_iX_i^{-(\tau+1)}$ when $\theta\le\min_iX_i$ and $0$ otherwise. It increases in $\theta$ on $(0,\min_iX_i]$, so $\hat\theta=\min_iX_i$.

3. With $s=\sqrt\theta$, $\ell_n=n\log s+(s-1)\sum_i\log X_i$, maximised at $s=-n/\sum_i\log X_i$ (positive, since $\log X_i<0$). So $\hat\theta=\Bigl(\dfrac n{\sum_i\log X_i}\Bigr)^2$.

4. $\ell_n=\sum_i\log X_i-2n\log\theta-\frac1{2\theta^2}\sum_iX_i^2$, $\ell_n'=-\frac{2n}\theta+\frac1{\theta^3}\sum_iX_i^2$, so $\hat\theta=\sqrt{\dfrac1{2n}\sum_{i=1}^nX_i^2}$.

5. $\ell_n=n\log\theta+n\log\tau+(\tau-1)\sum_i\log X_i-\theta\sum_iX_i^\tau$, $\ell_n'=\frac n\theta-\sum_iX_i^\tau$, so $\hat\theta=\dfrac n{\sum_iX_i^\tau}$.
:::

::: {.solution for="prob-mit18650f16-3-q2" status="draft"}
1. $\ell_n(\theta)=-\frac n2\log(2\pi\theta)-\frac1{2\theta}\sum_i(X_i-\theta)^2=-\frac n2\log(2\pi\theta)-\frac{S_2}{2\theta}+S_1-\frac{n\theta}2$, with $S_1=\sum_iX_i$ and $S_2=\sum_iX_i^2$.

2. $\ell_n'(\theta)=-\frac n{2\theta}+\frac{S_2}{2\theta^2}-\frac n2$. Setting it to $0$ and multiplying by $2\theta^2/n$ gives $\theta^2+\theta-\hat m_2=0$ with $\hat m_2=S_2/n$.

3. The positive root is
$$\hat\theta_n=\frac{-1+\sqrt{1+4\hat m_2}}2 .$$
$\ell_n'>0$ for small $\theta$ and $<0$ for large $\theta$, with this single zero in between, so it is the maximiser.

4. *Consistency.* By the strong law, $\hat m_2\to E[X^2]=\theta+\theta^2$ almost surely. The map $m\mapsto(-1+\sqrt{1+4m})/2$ is continuous, so $\hat\theta_n\to(-1+\sqrt{1+4\theta+4\theta^2})/2=(-1+(1+2\theta))/2=\theta$ almost surely.
:::

::: {.solution for="prob-mit18650f16-3-q3" status="draft"}
1. $\log\frac{p(x)}{q(x)}=\frac{(x-b)^2-(x-a)^2}{2\sigma^2}=\frac{(a-b)(2x-a-b)}{2\sigma^2}$. Under $P$, $E[2X-a-b]=a-b$, so
$$\operatorname{KL}(P,Q)=\frac{(a-b)^2}{2\sigma^2},$$
which here happens to be symmetric in $a,b$.

2. Summing over $x\in\{0,1\}$:
$$\operatorname{KL}(P,Q)=a\log\frac ab+(1-a)\log\frac{1-a}{1-b},$$
which is not symmetric in general (@prp-kl-properties).
:::

::: {.solution for="prob-mit18650f16-3-q4" status="draft"}
We use $\operatorname{TV}=\frac12\sum|p-q|$ or $\frac12\int|p-q|$ (@prp-total-variation-formula).

1. The densities are $1/s$ on $[0,s]$ and $1/t$ on $[0,t]$. So
$$\operatorname{TV}=\frac12\Bigl[s\Bigl(\frac1s-\frac1t\Bigr)+(t-s)\frac1t\Bigr]=1-\frac st .$$
(Equivalently, the supremum is attained at $A=[0,s]$.)

2. $\frac12\bigl(|p-q|+|(1-p)-(1-q)|\bigr)=|p-q|$.

3. By part 2, $\operatorname{TV}(\operatorname{Ber}(\bar X_n),\operatorname{Ber}(p))=|\bar X_n-p|$, which tends to $0$ in probability by the law of large numbers.

4. With $p_k=e^{-1/n}n^{-k}/k!$ and the Dirac mass $\delta_0$,
$$\operatorname{TV}=\frac12\Bigl(|p_0-1|+\sum_{k\ge1}p_k\Bigr)=\frac12\bigl((1-e^{-1/n})+(1-e^{-1/n})\bigr)=1-e^{-1/n}\to0 .$$
:::
