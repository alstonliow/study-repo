---
title: "Bayesian Updating"
sources: [mit1805-11, mit1805-13]
requires: [math/probability/estimation/bayesian-inference]
status: draft
---

<!-- Added 2026-11-20 from MIT 18.05 (Spring 2022), Classes 11 and 13, in our own wording; proofs written out in steps. -->

Bayesian updating applies Bayes' theorem (@thm-bayes-theorem) to a list of competing explanations of the data. With finitely many hypotheses the whole computation fits in one table; with a continuous parameter the same steps are carried out with densities (@thm-bayes-rule-mixed).

::: {#def-bayesian-update-table .definition name="Bayesian update table"}

Let $H_1,\dots,H_k$ be mutually exclusive hypotheses, one of which is true, and let $D$ be the observed data. The *update table* has one row per hypothesis and the columns

1. *prior* $\Pr(H_i)$;
2. *likelihood* $\Pr(D\mid H_i)$;
3. *Bayes numerator* $\Pr(D\mid H_i)\Pr(H_i)$;
4. *posterior* $\Pr(H_i\mid D)=\dfrac{\Pr(D\mid H_i)\Pr(H_i)}{\Pr(D)}$.

The sum of column 3 is the *total probability of the data*
$$\Pr(D)=\sum_{i=1}^k\Pr(D\mid H_i)\Pr(H_i),$$
by the law of total probability (@thm-law-of-total-probability). The priors and the posteriors each sum to $1$; the likelihoods need not.

:::

In short, *posterior $\propto$ likelihood $\times$ prior*: the posterior is the Bayes numerator rescaled to total $1$.

::: {#exm-coin-box-update .example name="Which coin was drawn?"}

A box holds coins of three types: type $A$ lands heads with probability $0.5$, type $B$ with $0.75$, type $C$ with $0.9$. A coin is drawn with probabilities $0.6$, $0.3$, $0.1$ for the three types and tossed once; it lands heads.

| hypothesis | prior | likelihood | Bayes numerator | posterior |
|---|---|---|---|---|
| $A$ | $0.6$ | $0.5$ | $0.300$ | $0.488$ |
| $B$ | $0.3$ | $0.75$ | $0.225$ | $0.366$ |
| $C$ | $0.1$ | $0.9$ | $0.090$ | $0.146$ |
| total | $1$ | | $0.615$ | $1$ |

The data move probability towards the coins that favour heads, but $A$ is still the most probable because its prior was large.

:::

::: {#exm-base-rate-fallacy .example name="The base rate fallacy"}

A test for a disease with prevalence $0.5\%$ detects it $99\%$ of the time and gives a false positive $2\%$ of the time. The update table for a positive result has Bayes numerators $0.005\cdot0.99=0.00495$ (disease) and $0.995\cdot0.02=0.0199$ (no disease), so $\Pr(\text{disease}\mid+)\approx0.199$. Ignoring the small prior (the *base rate*) and reading the answer off the $99\%$ accuracy is the base rate fallacy.

:::

::: {#thm-sequential-updating .theorem name="Updating in stages"}

Suppose the data $D_1,D_2$ are conditionally independent given each hypothesis:
$$\Pr(D_1\cap D_2\mid H_i)=\Pr(D_1\mid H_i)\Pr(D_2\mid H_i)\qquad(i=1,\dots,k).$$
Updating the prior with $D_1$ and then updating the resulting posterior with $D_2$ gives the same result as one update with $D_1\cap D_2$:
$$\Pr(H_i\mid D_1\cap D_2)=\frac{\Pr(D_2\mid H_i)\Pr(H_i\mid D_1)}{\sum_j\Pr(D_2\mid H_j)\Pr(H_j\mid D_1)}.$$

:::

::: {.proof}

1. By Bayes' theorem and the conditional independence, $\Pr(H_i\mid D_1\cap D_2)$ is proportional, as a function of $i$, to $\Pr(D_1\mid H_i)\Pr(D_2\mid H_i)\Pr(H_i)$.

2. The first update gives $\Pr(H_i\mid D_1)$ proportional to $\Pr(D_1\mid H_i)\Pr(H_i)$. Multiplying by $\Pr(D_2\mid H_i)$ therefore gives a quantity proportional to the expression in step 1.

3. Two lists of non-negative numbers that are proportional and each sum to $1$ are equal. Dividing step 2 by its sum over $j$ gives the displayed formula, and it equals $\Pr(H_i\mid D_1\cap D_2)$.

:::

::: {#exm-coin-box-second-toss .example name="A second toss"}

The coin of @exm-coin-box-update is tossed again and lands tails. Using the posterior $(0.488,0.366,0.146)$ as the new prior and the likelihoods $(0.5,0.25,0.1)$ of tails gives Bayes numerators $(0.244,0.091,0.015)$ with total $0.350$, and the new posterior $(0.697,0.261,0.042)$. One update with the data "heads, then tails" and the original prior gives the same numbers.

:::

::: {#rmk-continuous-update-table .remark name="Continuous parameters" related="thm-bayes-rule-mixed"}

When the hypotheses are the values of a continuous parameter $\theta$ with prior density $f(\theta)$, the table has a row for every $\theta$: the prior column holds $f(\theta)\,d\theta$, the likelihood column $p(x\mid\theta)$ (or $f(x\mid\theta)$), and the total probability of the data is
$$p(x)=\int p(x\mid\theta)f(\theta)\,d\theta .$$
The posterior density is $f(\theta\mid x)=p(x\mid\theta)f(\theta)/p(x)$. With a *flat* (uniform) prior the posterior is the likelihood rescaled to integrate to $1$. @exm-coin-bias-uniform-prior is an example.

:::
