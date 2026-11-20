---
title: "Predictive Probabilities, Odds and Bayes Factors"
sources: [mit1805-12, mit1805-13]
requires: [math/statistics/bayesian/bayesian-updating]
status: draft
---

<!-- Added 2026-11-20 from MIT 18.05 (Spring 2022), Classes 12 and 13, in our own wording; proofs written out in steps. -->

The update table of @def-bayesian-update-table answers "which hypothesis is true?". Two further questions use the same numbers: how likely is the *next* outcome, and how strongly do the data favour one hypothesis over another?

::: {#def-predictive-probability .definition name="Prior and posterior predictive probabilities"}

Let $H_1,\dots,H_k$ be hypotheses as in @def-bayesian-update-table. The *prior predictive probability* of an outcome $D$ is its total probability before any data:
$$\Pr(D)=\sum_{i=1}^k\Pr(D\mid H_i)\Pr(H_i).$$
After data $D_1$ have been seen, the *posterior predictive probability* of a further outcome $D_2$ is $\Pr(D_2\mid D_1)$.

:::

::: {#prp-posterior-predictive .proposition name="Posterior predictive probability"}

If $D_1$ and $D_2$ are conditionally independent given each $H_i$, then
$$\Pr(D_2\mid D_1)=\sum_{i=1}^k\Pr(D_2\mid H_i)\Pr(H_i\mid D_1).$$
For a continuous parameter with posterior density $f(\theta\mid D_1)$ the sum becomes $\int\Pr(D_2\mid\theta)f(\theta\mid D_1)\,d\theta$.

:::

::: {.proof}

1. The events $D_2\cap H_i$ partition $D_2$, so $\Pr(D_2\mid D_1)=\sum_i\Pr(D_2\cap H_i\mid D_1)$.

2. By the multiplication rule for conditional probability, $\Pr(D_2\cap H_i\mid D_1)=\Pr(D_2\mid H_i\cap D_1)\Pr(H_i\mid D_1)$.

3. Conditional independence gives $\Pr(D_2\mid H_i\cap D_1)=\Pr(D_2\cap D_1\mid H_i)/\Pr(D_1\mid H_i)=\Pr(D_2\mid H_i)$. Substituting into step 2 and summing gives the formula.

:::

::: {#exm-coin-box-prediction .example name="Predicting the next toss"}

In @exm-coin-box-update the prior predictive probability of heads is the total of the Bayes numerators, $0.615$. After one heads the posterior is $(0.488,0.366,0.146)$, so the posterior predictive probability of a second heads is
$$0.488\cdot0.5+0.366\cdot0.75+0.146\cdot0.9=0.65 .$$
Seeing heads makes heads on the next toss more likely, although the tosses are independent given the coin.

:::

::: {#def-odds .definition name="Odds"}

The *odds* of an event $E$ (against its complement) are
$$O(E)=\frac{\Pr(E)}{\Pr(E^c)}\in[0,\infty],\qquad\text{so}\qquad\Pr(E)=\frac{O(E)}{1+O(E)}.$$
More generally the odds of $E$ against $F$ are $\Pr(E)/\Pr(F)$.

:::

::: {#def-bayes-factor .definition name="Bayes factor"}

For a hypothesis $H$ and data $D$, the *Bayes factor* is the ratio of likelihoods
$$\mathrm{BF}=\frac{\Pr(D\mid H)}{\Pr(D\mid H^c)} .$$

:::

::: {#thm-odds-form-of-bayes .theorem name="Bayes' theorem in odds form"}

$$O(H\mid D)=\mathrm{BF}\cdot O(H),\qquad\text{that is}\qquad\text{posterior odds}=\text{Bayes factor}\times\text{prior odds}.$$

:::

::: {.proof}

1. By Bayes' theorem $\Pr(H\mid D)=\Pr(D\mid H)\Pr(H)/\Pr(D)$ and $\Pr(H^c\mid D)=\Pr(D\mid H^c)\Pr(H^c)/\Pr(D)$.

2. Divide the first equation by the second. The factor $\Pr(D)$ cancels, leaving $\dfrac{\Pr(D\mid H)}{\Pr(D\mid H^c)}\cdot\dfrac{\Pr(H)}{\Pr(H^c)}$.

:::

A Bayes factor above $1$ is evidence for $H$, below $1$ evidence against it; the further from $1$, the stronger the evidence. The prior odds then decide what the evidence is worth.

::: {#exm-odds-disease-test .example name="The disease test in odds"}

In @exm-base-rate-fallacy the prior odds of disease are $0.005/0.995\approx0.00503$ and the Bayes factor of a positive test is $0.99/0.02=49.5$. The posterior odds are $49.5\cdot0.00503\approx0.249$, so $\Pr(\text{disease}\mid+)=0.249/1.249\approx0.199$, as before. Strong evidence still leaves the disease unlikely because the prior odds were small.

:::

::: {#cor-log-odds .corollary name="Independent data add log odds"}

If $D_1,\dots,D_m$ are conditionally independent given $H$ and given $H^c$, with Bayes factors $\mathrm{BF}_1,\dots,\mathrm{BF}_m$, then
$$\ln O(H\mid D_1\cap\dots\cap D_m)=\ln O(H)+\sum_{j=1}^m\ln\mathrm{BF}_j .$$

:::

::: {.proof}

1. By conditional independence, $\Pr(D_1\cap\dots\cap D_m\mid H)=\prod_j\Pr(D_j\mid H)$, and likewise given $H^c$. So the Bayes factor of all the data is $\prod_j\mathrm{BF}_j$.

2. Apply @thm-odds-form-of-bayes to all the data at once and take logarithms.

:::
