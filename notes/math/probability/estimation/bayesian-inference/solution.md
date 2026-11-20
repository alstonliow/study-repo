<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6041f10-5-q6" status="draft"}
Let $H_i$ be "toss $i$ is heads"; given $P=p$ the tosses are independent with $\Pr(H_i\mid P=p)=p$.

(a) By total probability, with $\int_0^1p\sin(2\pi p)\,dp=-\frac1{2\pi}$ (integrate by parts),
$$\Pr(H_1)=\int_0^1p(1+\sin2\pi p)\,dp=\frac12-\frac1{2\pi}\approx0.341.$$

(b) By Bayes' rule (@thm-bayes-rule-mixed),
$$f_{P\mid H_1}(p)=\frac{p(1+\sin2\pi p)}{\frac12-\frac1{2\pi}},\qquad0\le p\le1.$$

(c) $\Pr(H_2\mid H_1)=\int_0^1p\,f_{P\mid H_1}(p)\,dp$. With $\int_0^1p^2\sin(2\pi p)\,dp=-\frac1{2\pi}$,
$$\Pr(H_2\mid H_1)=\frac{\frac13-\frac1{2\pi}}{\frac12-\frac1{2\pi}}=\frac{2\pi-3}{3(\pi-1)}\approx0.511.$$
Seeing a head raises the probability of the next head, although the tosses are independent given $P$.
:::

::: {.solution for="prob-mit6041f10-10-q4" status="draft"}
Let $\Theta=1$ or $2$ be the coin. $\Pr(Y=k\mid\Theta=1)=\binom3k\frac{2^{3-k}}{27}$ and $\Pr(Y=k\mid\Theta=2)=\binom3k\frac{2^k}{27}$.

(a) By Bayes' rule,
$$\Pr(\Theta=1\mid Y=k)=\frac{p\,2^{3-k}}{p\,2^{3-k}+(1-p)\,2^k}.$$

(b) This exceeds $p$ exactly when the likelihood ratio $2^{3-k}/2^k=2^{3-2k}$ exceeds $1$, that is $k\in\{0,1\}$ (for $0<p<1$). The set does not depend on $p$.

(c) The MAP rule (@thm-map-minimises-error): guess the first coin when $p\,2^{3-k}>(1-p)\,2^k$, that is when
$$\frac p{1-p}>2^{2k-3},$$
and the second coin when the inequality is reversed (either guess on equality).

(d) i. With $p=\frac23$ the condition is $2>2^{2k-3}$, i.e. $k\le1$; at $k=2$ both guesses are equally good. Summing $\max\{p\Pr(Y=k\mid1),(1-p)\Pr(Y=k\mid2)\}$ over $k$: $\frac{16}{81}+\frac8{27}+\frac4{27}+\frac8{81}=\frac{20}{27}\approx0.741$.
  ii. Without tossing, the best guess is the first coin, correct with probability $\frac23\approx0.667$; the tosses help a little.

(e) A larger $p$ raises the left side, so the threshold on $k$ moves up: Bob guesses the first coin for more values of $k$.

(f) He never guesses the first coin when even $k=0$ fails: $\frac p{1-p}\le2^{-3}$, i.e. $p\le\frac19$ (strictly below $\frac19$ if ties are broken towards the first coin).

(g) He always guesses the first coin when even $k=3$ passes: $\frac p{1-p}\ge2^3$, i.e. $p\ge\frac89$ (strictly above if ties go to the second coin).
:::

::: {.solution for="prob-mit6041f10-10-q5" status="draft"}
Given $Q=q$, the $T_i$ are independent $\mathrm{Geom}(q)$ (@thm-bernoulli-interarrivals).

(a) $p_{T_1}(t)=\int_0^1q(1-q)^{t-1}\,dq=\frac{1!\,(t-1)!}{(t+1)!}=\frac1{t(t+1)}$, $t=1,2,\dots$

(b) The LSE is the posterior mean:
$$E[Q\mid T_1=t]=\frac{\int_0^1q^2(1-q)^{t-1}\,dq}{p_{T_1}(t)}=\frac{2\,(t-1)!}{(t+2)!}\,t(t+1)=\frac2{t+2}.$$

(c) The posterior is proportional to $\prod_iq(1-q)^{t_i-1}=q^k(1-q)^{s-k}$ with $s=t_1+\dots+t_k$. Setting the derivative of $k\ln q+(s-k)\ln(1-q)$ to zero gives $\hat q=\frac ks$.

(d) Now $Q$ is uniform on $[\frac12,1]$ with density $2$. Using $E[T\mid Q]=\frac1Q$ and $E[T^2\mid Q]=\frac{2-Q}{Q^2}$:

1. $E[T_1]=E[T_2]=E[1/Q]=2\ln2\approx1.386$.
2. $E[1/Q^2]=2$, so $\mathrm{Var}(T_1)=E\bigl[\tfrac2{Q^2}-\tfrac1Q\bigr]-(2\ln2)^2=4-2\ln2-4(\ln2)^2\approx0.692$.
3. Given $Q$, $T_1$ and $T_2$ are independent, so $\mathrm{Cov}(T_1,T_2)=E[1/Q^2]-(E[1/Q])^2=2-4(\ln2)^2\approx0.078$.
4. By @thm-llse,
$$\hat T_2=2\ln2+\frac{2-4(\ln2)^2}{4-2\ln2-4(\ln2)^2}\,(t_1-2\ln2)\approx1.386+0.113\,(t_1-1.386).$$
:::

::: {.solution for="prob-mit6041f10-10-q6" status="draft"}
(a) $\int_0^1\int_0^1xy\,dx\,dy=\frac14$, so $c=4$.

(b) $f_{X,Y}(x,y)=2x\cdot2y$ is a product, so $X$ and $Y$ are independent with $f_X(x)=2x$ on $(0,1]$. Hence $E[X\mid Y=y]=E[X]=\int_0^12x^2\,dx=\frac23$ for every $y$.

(c) No: by independence, $Y$ carries no information about $X$, and the estimate equals the prior mean $\frac23$.

(d) The posterior is $f_X(x)=2x$, maximised at $x=1$. The MAP estimate is $1$ for every $y$, again the same as before observing $Y$.
:::

::: {.solution for="prob-mit6041f10-11-q2" status="draft"}
By Bayes' rule (@thm-bayes-rule-mixed) the posterior is proportional to $\mu e^{-\mu x}\cdot e^{-x}x^y/y!\propto x^ye^{-(\mu+1)x}$ for $x\ge0$.

(a) The logarithm $y\ln x-(\mu+1)x$ has derivative $\frac yx-(\mu+1)$, so the MAP estimate is $\hat x=\frac y{\mu+1}$ (for $y=0$ the posterior is decreasing and the maximum is at $0$, which the formula gives).

(b) i. Normalising with the given integral, $f_{X\mid Y}(x\mid y)=\frac{\lambda^{y+1}}{y!}x^ye^{-\lambda x}$ with $\lambda=\mu+1$.
  ii. $xf_{X\mid Y}(x\mid y)=\frac{y+1}\lambda f_{X\mid Y}(x\mid y+1)$, which integrates to $\frac{y+1}\lambda$. So $E[X\mid Y=y]=\frac{y+1}{\mu+1}$.

(c) Both are linear in $y$ with slope $\frac1{\mu+1}$; the LMS estimate is larger by $\frac1{\mu+1}$, because the posterior is skewed to the right and its mean lies beyond its mode.
:::
