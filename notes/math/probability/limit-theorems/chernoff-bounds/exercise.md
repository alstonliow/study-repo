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

::: {.problem #prob-eecs126-1-q2 origin="external" source="eecs126-1-q2"}
By letting $t$ take values in some larger interval than $[0,1]$, show that the term $e^{-c\lambda\sigma/K}$ in the Chernoff bound can be replaced with $(\lambda K/\sigma)^{-c\lambda\sigma/K}$, which is better for when $\lambda K\gg\sigma$.

*Note (these notes):* The notes' Chernoff bound (6), a different form from @thm-chernoff-bound: if $X_1,\dots,X_n$ are independent with $|X_i|\le K$ almost surely, means $\mu_i$ and variances $\sigma_i^2$, then for every $\lambda>0$, $P(|S_n-\mu|\ge\lambda\sigma)\le C\max\bigl(e^{-c\lambda^2},e^{-c\lambda\sigma/K}\bigr)$, where $\mu=\sum\mu_i$, $\sigma^2=\sum\sigma_i^2$ and $C,c>0$ are constants. The proof reduces to $\mu_i=0$, $K=1$, bounds $Ee^{tX_i}\le e^{O(t^2\sigma_i^2)}$ for $t\in[0,1]$, applies Markov's inequality to $e^{tS_n}$, and optimizes over $t\in[0,1]$.
:::
