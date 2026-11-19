<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-eecs126hw-10-q2" status="draft"}
Write $h(q)=-q\log q-(1-q)\log(1-q)$.

(a) $0<p(x)\le1$ gives $-\log p(x)\ge0$, so every term $-p(x)\log p(x)$ is non-negative.

(b) A fair bit is the most uncertain, so $p=\frac12$ should give more: $h(\frac12)=1$ bit and $h(\frac13)=\log3-\frac23\approx0.918$ bit.

(c) $Y$ takes values $0,1,?$ with probabilities $\frac{1-p_e}2,\frac{1-p_e}2,p_e$, so
$$H(Y)=p_e\log\frac1{p_e}+(1-p_e)\log\frac2{1-p_e}=h(p_e)+(1-p_e).$$

(d) By the chain rule (@thm-entropy-properties), $H(X,Y)=H(X)+H(Y\mid X)$. Given $X=x$, $Y$ is $x$ or $?$ with probabilities $1-p_e,p_e$, so $H(Y\mid X)=h(p_e)$ and $H(X,Y)=1+h(p_e)$.
:::

::: {.solution for="prob-eecs126hw-10-q3" status="draft"}
(a) For every affine $l\le f$, linearity gives $E[f(Z)]\ge E[l(Z)]=l(E[Z])$. Taking the supremum over such $l$, $E[f(Z)]\ge f(E[Z])$.

(b) $\log$ is concave, so by Jensen
$$H(X)=E\Bigl[\log\frac1{p(X)}\Bigr]\le\log E\Bigl[\frac1{p(X)}\Bigr]=\log\#\{x:p(x)>0\}\le\log|\mathcal X|.$$
The uniform distribution on $[n]$ has $H=\log n$, so it attains the maximum. (Equality in Jensen for strictly concave $\log$ needs $1/p(X)$ constant, so it is the only maximiser.)

(c) By Jensen again, summing over pairs with $p(x,y)>0$,
$$-I(X;Y)=E\Bigl[\log\frac{p(X)p(Y)}{p(X,Y)}\Bigr]\le\log\sum_{x,y:p(x,y)>0}p(x)p(y)\le\log1=0.$$
(Compare @thm-entropy-properties.)
:::

::: {.solution for="prob-eecs126hw-10-q4" status="draft"}
(a) With $X\sim p$, by Jensen for the strictly concave $\log$,
$$-D(p\|q)=E\Bigl[\log\frac{q(X)}{p(X)}\Bigr]\le\log E\Bigl[\frac{q(X)}{p(X)}\Bigr]=\log\sum_{x:p(x)>0}q(x)\le0.$$
Equality needs $q/p$ constant on the support of $p$ and $\sum_{p(x)>0}q(x)=1$, which together force $q=p$. (This is @thm-relative-entropy-nonnegative.)

(b) We take the state space finite. Irreducibility gives $\pi(i)>0$ for all $i$. Let $h=\mu/\pi$ and $\hat P(j,i)=\pi(i)P(i,j)/\pi(j)$, a transition matrix (rows sum to $1$ because $\pi P=\pi$) which is irreducible because $P$ is.

1. $\mu P=\mu$ reads $\pi(j)h(j)=\sum_i\pi(i)h(i)P(i,j)$, i.e. $h(j)=\sum_i\hat P(j,i)h(i)$: each $h(j)$ is an average of the values of $h$ at the states $\hat P$ can move to.
2. Let $j^*$ maximise $h$. The average equals the maximum only if $h(i)=h(j^*)$ for every $i$ with $\hat P(j^*,i)>0$; repeating from those states and using irreducibility, $h$ is constant.
3. So $\mu=c\pi$, and both sum to $1$, so $\mu=\pi$.

In terms of the hint: Jensen applied to $D(\pi\|\mu P)=\sum_j\pi(j)\log\frac{1}{\sum_i\hat P(j,i)h(i)}$ gives $D(\pi\|\mu P)\le D(\pi\|\mu)$, with equality only when $h$ is constant over the possible predecessors of each state, which is step 2 in another form.
:::
