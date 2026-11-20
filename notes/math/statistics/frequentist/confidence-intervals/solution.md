<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1805s22-10-q2" status="draft"}
$n=9$, $\bar x=356$, $s\approx3.937$. Use @thm-normal-confidence-intervals.

(a) z-interval: $356\pm1.960\cdot\frac33=[354.04,\ 357.96]$.

(b) $z_{0.01}\approx2.326$: $356\pm2.326=[353.67,\ 358.33]$.

(c) t-intervals with $8$ degrees of freedom: $t_{8,0.025}\approx2.306$ gives $356\pm2.306\cdot\frac{3.937}3=[352.97,\ 359.03]$ at $95\%$, and $t_{8,0.01}\approx2.896$ gives $[352.20,\ 359.80]$ at $98\%$. They are wider for two reasons: $s\approx3.94$ is larger than the assumed $\sigma=3$, and $t$ critical values exceed $z$ ones to pay for estimating $\sigma$.
:::

::: {.solution for="prob-mit1805s22-10-q3" status="draft"}
(a) $n=12$, $s^2\approx0.1536$. With the $\chi^2_{11}$ critical values $c_{0.025}\approx21.92$ and $c_{0.975}\approx3.816$, the chi-square interval of @thm-normal-confidence-intervals is
$$\Bigl[\frac{11\cdot0.1536}{21.92},\ \frac{11\cdot0.1536}{3.816}\Bigr]\approx[0.077,\ 0.443]\ (\text{mmol/L})^2 .$$

(b) That the $12$ levels are independent draws from one normal distribution. The chi-square interval is sensitive to non-normality, unlike intervals for a mean.
:::

::: {.solution for="prob-mit1805s22-10-q4" status="draft"}
(a) With $\chi^2_9$ critical values $c_{0.025}\approx19.02$ and $c_{0.975}\approx2.700$, the $95\%$ interval for $\sigma^2$ is $\bigl[\frac{9\cdot4.2}{19.02},\frac{9\cdot4.2}{2.700}\bigr]\approx[1.99,\ 14.0]$. The square root is increasing, so $\sigma$ lies in $[\sqrt{1.99},\sqrt{14.0}]\approx[1.41,\ 3.74]$ grams exactly when $\sigma^2$ lies in that interval: this is a $95\%$ interval for $\sigma$.

(b) That the $10$ weights are independent and normally distributed with a common mean and variance.
:::

::: {.solution for="prob-mit1805s22-10-q5" status="draft"}
(a) $95\%$: whatever $\mu$ is, $\Pr(\mu\in\text{interval})=0.95$ over repetitions of sampling (@def-confidence-interval).

(b) (i) The interval $[0.375,2.825]$ contains $\mu=1$ and $\mu=2$, of prior probability $0.04$.
(ii) Given $\mu$, $\bar x\sim N(\mu,(5/8)^2)$, so the likelihoods are the $N(\mu,0.390625)$ density at $1.6$. The posterior is approximately $0.537,0.191,0.247,0.025$ for $\mu=0,1,2,3$, and the posterior probability of the interval is $0.191+0.247\approx0.44$.
Neither is close to $0.95$. That is expected: the $95\%$ is a property of the procedure averaged over samples, not a probability for $\mu$ given this sample. A probability for $\mu$ requires a prior, and here the strong prior on $\mu=0$ dominates.

(c) (i) False: it gives a probability to the parameter, which a confidence interval never does. (ii) False, for the same reason. (iii) True: the interval (and its midpoint $15$) estimates the true increase. (iv) False as stated: "likely to be incorrect" is a probability statement about a hypothesis; the result does show the data are inconsistent with "no change" at level $0.05$. (v) True: this is what the confidence level means (approximately, since the count is random). (vi) True: $0$ lies outside the $95\%$ interval, so the two-sided level-$0.05$ test rejects (@thm-interval-test-duality); a one-sided test would also reject.
:::

::: {.solution for="prob-mit1805s22-11-q1" status="draft"}
(a) $t_{19,0.05}\approx1.729$ and $s/\sqrt{20}\approx0.844$, so the interval is $69.55\pm1.460=[68.09,\ 71.01]$ inches.

(b) $z_{0.05}\approx1.645$ and $\sigma/\sqrt{20}\approx0.843$: $69.55\pm1.387=[68.16,\ 70.94]$ inches.

(c) The width is $2\cdot1.645\cdot3.77/\sqrt n$. It is at most $1$ when $\sqrt n\ge12.40$, i.e. $n\ge153.8$: $154$ people.
:::

::: {.solution for="prob-mit1805s22-11-q2" status="draft"}
1. $y_2/a$ is a pivot: its distribution Beta$(2,n-1)$ does not depend on $a$. Let $q_{0.025}$ and $q_{0.975}$ be its quantiles (`qbeta(0.025, 2, n-1)` and `qbeta(0.975, 2, n-1)`). Then $\Pr(q_{0.025}\le Y_2/a\le q_{0.975})=0.95$.

2. Solving for $a>0$, the inequality is equivalent to $\dfrac{Y_2}{q_{0.975}}\le a\le\dfrac{Y_2}{q_{0.025}}$, so $\Bigl[\dfrac{y_2}{q_{0.975}},\ \dfrac{y_2}{q_{0.025}}\Bigr]$ is a $95\%$ confidence interval for $a$.

3. For $n=9$: Beta$(2,8)$ has $q_{0.025}\approx0.0281$ and $q_{0.975}\approx0.4825$, so with $y_2=1.5$ the interval is $\approx[3.1,\ 53.3]$. It is very wide and skewed because the second smallest of nine points says little about the right end.
:::

::: {.solution for="prob-mit1805s22-11-q3" status="draft"}
(a) All three plots are centred at $250\theta$. The true standard deviation $\sqrt{250\theta(1-\theta)}$ is $7.91$, $7.25$, $4.74$ for $\theta=0.5,0.3,0.1$; the conservative one is always $\sqrt{250/4}\approx7.91$.
(i) $\theta=0.5$: the two normal curves coincide and sit on top of the binomial points.
(ii) $\theta=0.3$: the true-variance normal still fits the binomial closely; the conservative curve is slightly lower and wider ($7.91$ against $7.25$).
(iii) $\theta=0.1$: the true-variance normal still fits well (the binomial is only slightly skewed), but the conservative curve is far too wide and low ($7.91$ against $4.74$).
So the conservative normal is a reasonable approximation for $\theta$ roughly between $0.3$ and $0.7$, where $\theta(1-\theta)\ge0.21$ is close to $\frac14$.

(b) $\bar x=0.56$ and the conservative standard error is $\frac1{2\sqrt{250}}\approx0.0316$ (@prp-conservative-proportion-interval). At $80\%$, $z_{0.1}\approx1.2816$: $0.56\pm0.0405=[0.520,\ 0.601]$. At $95\%$ with $z_{0.025}=2$: $0.56\pm0.0632=[0.497,\ 0.623]$.

(c) The posterior is Beta$(141,111)$ (@thm-beta-binomial-update), whose $0.1$ and $0.9$ quantiles give the $80\%$ probability interval $\approx[0.519,\ 0.599]$. It is almost the same as the $80\%$ confidence interval: with a flat prior and much data the posterior is close to $N(\bar x,\bar x(1-\bar x)/n)$, and $\bar x(1-\bar x)=0.246$ is close to $\frac14$. The interpretations still differ: one is a probability for $\theta$, the other a property of the procedure.
:::
