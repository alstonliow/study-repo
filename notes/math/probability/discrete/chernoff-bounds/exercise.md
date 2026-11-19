::: {.problem #prob-eecs126hw-6-q2 origin="external" source="eecs126hw-6-q2"}
**Confidence Intervals: Chebyshev vs. Chernoff vs. CLT.** Let $X_1,\dots,X_n$ be i.i.d. $\text{Bernoulli}(q)$ random variables, with common mean $\mu=E[X_1]=q$ and variance $\sigma^2=\operatorname{var}(X_1)=q(1-q)$. We want to estimate the mean $\mu$, and towards this goal we use the sample mean estimator
$$\bar X_n\overset{\Delta}{=}\frac{X_1+\dots+X_n}{n}.$$
Given some confidence level $a\in(0,1)$ we want to construct a confidence interval around $\bar X_n$ such that $\mu$ lies in this interval with probability at least $1-a$.

(a) Use Chebyshev's inequality in order to show that $\mu$ lies in the interval
$$\Bigl[\bar X_n-\frac{\sigma}{\sqrt n\sqrt a},\ \bar X_n+\frac{\sigma}{\sqrt n\sqrt a}\Bigr]$$
with probability at least $1-a$.

(b) A Chernoff bound for this setting can be computed to be:
$$P(|\bar X_n-q|\ge\epsilon)\le2e^{-2n\epsilon^2},\quad\text{for any }\epsilon>0.$$
Use this inequality in order to show that $\mu$ lies in the interval
$$\Bigl[\bar X_n-\frac{1}{2\sqrt n}\sqrt{2\ln\frac2a},\ \bar X_n+\frac{1}{2\sqrt n}\sqrt{2\ln\frac2a}\Bigr]$$
with probability at least $1-a$.

(c) Show that if $Z\sim N(0,1)$, then
$$P(|Z|\ge\epsilon)\le2e^{-\frac{\epsilon^2}{2}},\quad\text{for any }\epsilon>0.$$

(d) Use the Central Limit Theorem, and Part (c) in order to heuristically argue that $\mu$ lies in the interval
$$\Bigl[\bar X_n-\frac{\sigma}{\sqrt n}\sqrt{2\ln\frac2a},\ \bar X_n+\frac{\sigma}{\sqrt n}\sqrt{2\ln\frac2a}\Bigr]$$
with probability at least $1-a$.

(e) Compare the three confidence intervals.
:::
