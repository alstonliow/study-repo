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

::: {.solution for="prob-mit1805s22-9-q2" status="draft"}
$\theta$ is the probability of heads; small $\theta$ means bias toward tails.

(a) Under $H_0$ the number of heads $X$ is binomial$(12,0.5)$, and small $X$ favours $H_A$. $P(X\le2)=\frac{79}{4096}\approx0.019$ and $P(X\le3)=\frac{299}{4096}\approx0.073$, so the rejection region at $\alpha=0.05$ is $X\le2$. The p-value is $P(X\le3)\approx0.073>0.05$: Erika does not reject $H_0$. (Sketch: the symmetric binomial pmf on $0,\dots,12$ with the bars at $0,1,2$ marked.)

(b) Now the statistic is the number of tails $Y$ before the third head, negative binomial: $P(Y=y)=\binom{y+2}2(0.5)^{y+3}$ under $H_0$. Many tails favour $H_A$. $P(Y\ge y)$ is the probability that the first $y+2$ flips contain at most $2$ heads: $P(Y\ge8)=\frac{56}{1024}\approx0.055$ and $P(Y\ge9)=\frac{67}{2048}\approx0.033$. So the rejection region is $Y\ge9$, the p-value is $\approx0.033$, and Ruthi rejects $H_0$. (Sketch: a right-skewed pmf with its mode at $1$–$2$ and the tail $y\ge9$ marked.)

(c) No. A p-value is the probability of outcomes at least as extreme under the experiment that was actually run, which requires the stopping rule. "Stopped when bored" is not a specified random experiment, so the null distribution, and hence the p-value, is undefined.

(d) Experiment 1: $L_1(\theta)=\binom{12}3\theta^3(1-\theta)^9$. Experiment 2: $L_2(\theta)=\binom{11}2\theta^3(1-\theta)^9$ (the last flip must be the third head). They are proportional. With prior Beta$(n,m)$ both posteriors are Beta$(n+3,m+9)$ (@thm-beta-binomial-update): identical.

(e) The likelihood principle says that two experiments whose likelihood functions are proportional carry the same evidence about $\theta$. Bayesian inference obeys it automatically, as (d) shows. Frequentist significance tests do not: (a) and (b) reach opposite conclusions from the same data because p-values depend on the stopping rule, i.e. on outcomes that might have occurred but did not, and (c) shows that without a stopping rule no p-value exists. The voltmeter story makes the same point: a frequentist analysis can change because of what the instrument *would* have done in readings that were never taken.
:::
