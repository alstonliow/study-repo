<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-probability-2-09"}
(a) Geometric with $p = 0.0125$: the number of balls up to and including
    the dismissal ball, $\Pr(X = k) = (1-p)^{k-1}p$ for $k\ge1$.

(b) $\Pr(X = 1) = p = 0.0125$.

(c) $E(X) = 1/p = 80$ balls.

(d) The geometric distribution is memoryless:
    $$\Pr(X > 200 + k\mid X > 200) = (1-p)^k = \Pr(X > k).$$
    So the remaining number of balls has the same distribution as at the
    start, and we expect $80$ more. (Under this model the batter does not
    "get their eye in".)
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-13-q2" status="draft"}
For $y\ge0$, $\Pr(X>y)=(1-p)^y$ (the first $y$ trials fail). Conditioning on $Y$ and using independence,
$$\Pr(X>Y)=\sum_{y\ge0}\frac{e^{-\lambda}\lambda^y}{y!}(1-p)^y=e^{-\lambda}e^{\lambda(1-p)}=e^{-\lambda p}.$$
:::

::: {.solution for="prob-cs70hw-13-q3" status="draft"}
For $k\ge0$, by independence,
$$\Pr(\min\{X,Y\}>k)=\Pr(X>k)\Pr(Y>k)=(1-p)^k(1-q)^k=\bigl((1-p)(1-q)\bigr)^k.$$
This is the tail of $\mathrm{Geom}(r)$ with $1-r=(1-p)(1-q)$, and the tails determine the distribution ($\Pr(Z=k)=\Pr(Z>k-1)-\Pr(Z>k)$). So $\min\{X,Y\}\sim\mathrm{Geom}(p+q-pq)$: running both experiments in parallel, a round succeeds unless both fail.
:::

::: {.solution for="prob-mit6041f10-4-q3" status="draft"}
1. For $1\le i\le n-1$, independence gives $\Pr(X=i,X+Y=n)=\Pr(X=i)\Pr(Y=n-i)=(1-p)^{i-1}p\,(1-p)^{n-i-1}p=p^2(1-p)^{n-2}$, which does not depend on $i$.

2. $X+Y=n$ forces $X\in\{1,\dots,n-1\}$, so $\Pr(X+Y=n)=(n-1)p^2(1-p)^{n-2}$.

3. Dividing, $\Pr(X=i\mid X+Y=n)=\frac1{n-1}$.
:::
