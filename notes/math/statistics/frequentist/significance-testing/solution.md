<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1805s22-8-q1" status="draft"}
Under $H_0$ the number of heads $X$ is binomial$(250,0.5)$, symmetric about $125$.

(a) $140$ is $15$ above $125$. "At least this extreme" in both directions is $X\ge140$ or $X\le110$, of probability $2P(X\ge140)\approx0.066\approx7\%$. This is the two-sided p-value (@def-p-value); the one-sided value would be $3.3\%$.

(b) $p\approx0.066$: reject at $\alpha=0.1$ (since $p\le0.1$), do not reject at $\alpha=0.05$ (@prp-p-value-rule).

(c) The two-sided region at $\alpha=0.01$ is the smallest symmetric tail set of probability at most $0.01$: $X\ge146$ or $X\le104$. So at least $146$ heads (or at most $104$).

(d) (i) At $\alpha=0.05$ the region is $X\ge141$ or $X\le109$ (probability $\approx0.0497$). The power is $P(X\in R)$ under each alternative: $\approx0.35$ for $\theta=0.55$ and $\approx0.89$ for $\theta=0.6$.
(ii) The pmf under $\theta=0.55$ is centred at $137.5$, so less than half of it lies beyond $141$; under $\theta=0.6$ it is centred at $150$ and most of it lies in the right part of the region. Alternatives further from $H_0$ are easier to detect.

(e) (i) Computing the $\alpha=0.05$ region and the power at $\theta=0.55$ for increasing $n$, the first $n$ with power at least $0.9$ is $n=1055$ (power $\approx0.900$).
(ii) Both pmfs have standard deviation of order $\sqrt n$ while their centres $0.5n$ and $0.55n$ separate at rate $n$; for large $n$ they barely overlap, and the alternative's pmf lies mostly in the rejection region.

(f) The Bayes factor is $\dfrac{0.55^{140}0.45^{110}}{0.5^{250}}=1.1^{140}0.9^{110}\approx5.78$. With prior odds $1$, the posterior odds are $5.78$, so $P(H_A\mid\text{data})\approx0.85$.

(g) A personal judgement. Spinning coins on edge is known to be biased for some coins, which argues for a prior that is not concentrated at $\theta=0.5$; with the data's p-value of $0.066$ and Bayes factor around $6$ against the specific alternative $0.55$, a probability of roughly $0.7$–$0.85$ that the coin favours heads is reasonable.
:::

::: {.solution for="prob-mit1805s22-8-q3" status="draft"}
(a) The data are three readings, each $N(\mu,5^2)$, with $\mu$ the car's true speed; the statistic is $\bar x\sim N(\mu,25/3)$. $H_0$: $\mu\le40$ (not speeding), $H_A$: $\mu>40$. Both are composite. "Issue a ticket" means "reject $H_0$"; the test is one-sided (right).

(b) (i) The largest type I error occurs at $\mu=40$, so use the null distribution $N(40,25/3)$: reject when $\bar x\ge40+z_{0.04}\cdot\frac5{\sqrt3}\approx40+1.751\cdot2.887\approx45.05$ mph.
(ii) The sketch is the $N(40,25/3)$ density with the region $\bar x\ge45.05$ shaded; the shaded area is $0.04$.
(iii) It cannot be computed from the test alone: $P(\text{not speeding}\mid\text{ticket})$ needs a prior, the fraction of drivers who speed. The $4\%$ is $P(\text{ticket}\mid\text{not speeding})$ (at most), a different conditional probability.
(iv) $100\%$: every ticket then goes to a driver who was not speeding.

(c) Power at $\mu=45$: $P(\bar x\ge45.05\mid\mu=45)=P\bigl(Z\ge\frac{0.05}{2.887}\bigr)\approx0.49$. With $n$ guns the threshold is $40+1.751\cdot5/\sqrt n$ and the power at $45$ is $P\bigl(Z\ge1.751-\sqrt n\bigr)$. Power $0.9$ needs $\sqrt n-1.751\ge1.282$, i.e. $n\ge9.2$: ten radar guns.
:::

::: {.solution for="prob-mit1805s22-8-q4" status="draft"}
(a) Under $H_0$, $x\sim U[0,2]$: $P(x\le0.1)+P(x\ge1.9)=\frac{0.1}2+\frac{0.1}2=0.1$.

(b) A type II error is not rejecting when $\theta=2.5$: $P(0.1<x<1.9\mid\theta=2.5)=\frac{1.8}{2.5}=0.72$.
:::
