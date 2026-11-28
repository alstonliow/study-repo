::: {.problem #prob-eecs126hw-9-q4 origin="external" source="eecs126hw-9-q4"}
**Poisson Process MAP.** Customers arrive to a store according to a Poisson process of rate $1$. The store manager learns of a rumor that one of the employees is sending $1/2$ of the customers to the rival store. Refer to hypothesis $X=1$ as the rumor being true, that one of the employees is sending every other customer arrival to the rival store and hypothesis $X=0$ as the rumor being false, where each hypothesis is equally likely. Assume that at time $0$, there is a successful sale. After that, the manager observes $S_1,S_2,\dots,S_n$ where $n$ is a positive integer and $S_i$ is the time of the $i$th subsequent sale for $i=1,\dots,n$. Derive the MAP rule to determine whether the rumor was true or not.
:::

::: {.problem #prob-eecs126hw-9-q5 origin="external" source="eecs126hw-9-q5"}
**Statistical Estimation.** Given $X\in\{0,1\}$, the random variable $Y$ is exponentially distributed with rate $3X+1$.

(a) Assume $P(X=1)=p\in(0,1)$ and $P(X=0)=1-p$. Find the MAP estimate of $X$ given $Y$.

(b) Find the MLE of X given Y.
:::

::: {.problem #prob-eecs126hw-12-q1 origin="external" source="eecs126hw-12-q1"}
**Flipping Coins and Hypothesizing.** You flip a coin until you see heads. Let
$$X=\begin{cases}1&\text{if the bias of the coin is }q>p.\\0&\text{if the bias of the coin is }p.\end{cases}$$
Find a decision rule $\hat X(Y)$ that maximizes $P[\hat X=1\mid X=1]$ subject to $P[\hat X=1\mid X=0]\le\beta$ for $\beta\in[0,1]$. Remember to calculate the randomization constant $\gamma$.
:::

::: {.problem #prob-eecs126hw-12-q2 origin="external" source="eecs126hw-12-q2"}
**Gaussian Hypothesis Testing.** Consider a hypothesis testing problem that if $X=0$, you observe a sample of $N(\mu_0,\sigma^2)$, and if $X=1$, you observe a sample of $N(\mu_1,\sigma^2)$, where $\mu_0,\mu_1\in\mathbb R$, $\sigma^2>0$. Find the Neyman-Pearson test for false alarm $\alpha\in(0,1)$, that is, $P(\hat X=1\mid X=0)\le\alpha$.
:::

::: {.problem #prob-eecs126hw-12-q3 origin="external" source="eecs126hw-12-q3"}
**BSC Hypothesis Testing.** Consider a BSC with some error probability $\epsilon\in[0.1,0.5)$. Given $n$ inputs and outputs $(x_i,y_i)$ of the BSC, solve a hypothesis problem to detect that $\epsilon>0.1$ with a probability of false alarm at most equal to $0.05$. Assume that $n$ is very large and use the CLT.

Hint: The null hypothesis is $\epsilon=0.1$. The alternate hypothesis is $\epsilon>0.1$, which is a composite hypothesis (this means that under the alternate hypothesis, the probability distribution of the observation is not completely determined; compare this to a simple hypothesis such as $\epsilon=0.3$, which does completely determine the probability distribution of the observation). The Neyman-Pearson Lemma we learned in class applies for the case of a simple null hypothesis and a simple alternate hypothesis, so it does not directly apply here.

To fix this, fix some specific $\epsilon_0>0.1$ and use the Neyman-Pearson Lemma to find the optimal hypothesis test for the hypotheses $\epsilon=0.1$ vs. $\epsilon=\epsilon_0$. Then, argue that the optimal decision rule does not depend on the specific choice of $\epsilon_0$; thus, the decision rule you derive will be simultaneously optimal for testing $\epsilon=0.1$ vs. $\epsilon=\epsilon_0$ for all $\epsilon_0>0.1$.
:::

::: {.problem #prob-eecs126d-11-q2 origin="external" source="eecs126d-11-q2"}
**Hypothesis Testing for Uniform Distribution.** Assume that

- If $X=0$, then $Y\sim\text{Uniform}[-1,1]$.
- If $X=1$, then $Y\sim\text{Uniform}[0,2]$.

Using the Neyman-Pearson formulation of hypothesis testing, find the optimal randomized decision rule $r:[-1,2]\to\{0,1\}$ with respect to the criterion
$$\min_{\text{randomized }r:[-1,2]\to\{0,1\}}P\bigl(r(Y)=0\mid X=1\bigr)\quad\text{s.t.}\quad P\bigl(r(Y)=1\mid X=0\bigr)\le\beta,$$
where $\beta\in[0,1]$ is a given upper bound on the false positive probability.
:::

::: {#prob-neyman-pearson-code .problem .coding origin="adapted" source="res-ucb-eecs126-labs-hypothesis-testing"}
An observation $Y\in\{0,\dots,m-1\}$ has PMF $p_0$ under hypothesis $0$ and $p_1$ under hypothesis $1$. Write `neyman_pearson(p0, p1, beta)`, which returns the most powerful test with $\mathrm{PFA}\le\beta$ (@def-neyman-pearson-problem, @thm-neyman-pearson). The result is a list `r` of rejection probabilities: on observing $y$, decide $1$ with probability `r[y]`.

Build it greedily. Take the outcomes in decreasing order of the likelihood ratio, where $p_1(y)/p_0(y)=\infty$ when $p_0(y)=0<p_1(y)$, and reject each one fully while the false-alarm budget allows. Randomise at the first outcome that does not fit. Outcomes with $p_1(y)=0$ are never rejected. The tests compare with every deterministic test on a small example and include a case where the best rejection region is not a threshold in $y$.

```{.python .starter}
def neyman_pearson(p0, p1, beta):
    """Most powerful test of level beta for an observation y in 0..len(p0)-1 with
    PMF p0 under hypothesis 0 and p1 under hypothesis 1. Return the list r of
    rejection probabilities: on observing y, decide 1 with probability r[y]."""
    ...
```

```{.python .tests}
from itertools import product
from math import comb


def binom(n, p):
    return [comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(n + 1)]


def pfa(r, p0):
    return sum(a * b for a, b in zip(r, p0))


def test_binomial_threshold():
    p0, p1 = binom(10, 0.4), binom(10, 0.6)
    r = neyman_pearson(p0, p1, 0.1)
    assert abs(pfa(r, p0) - 0.1) < 1e-12
    # increasing likelihood ratio: reject large y, randomise at one y only
    assert r[:6] == [0] * 6 and r[7:] == [1] * 4 and 0 < r[6] < 1
    assert abs(pfa(r, p1) - 0.4841) < 1e-4


def test_beats_every_deterministic_test():
    p0 = [0.3, 0.1, 0.25, 0.05, 0.2, 0.1]
    p1 = [0.05, 0.3, 0.1, 0.2, 0.05, 0.3]
    for beta in [0.05, 0.15, 0.3, 0.5]:
        r = neyman_pearson(p0, p1, beta)
        assert pfa(r, p0) <= beta + 1e-12
        best = max(pfa(s, p1) for s in product([0, 1], repeat=6) if pfa(s, p0) <= beta + 1e-12)
        assert pfa(r, p1) >= best - 1e-12


def test_two_peaks_need_no_threshold():
    # mixtures: the rejection region is not of the form {y >= c}
    p0 = [(a + b) / 2 for a, b in zip(binom(10, 0.1), binom(10, 0.7))]
    p1 = [(a + b) / 2 for a, b in zip(binom(10, 0.3), binom(10, 0.9))]
    r = neyman_pearson(p0, p1, 0.1)
    assert abs(pfa(r, p0) - 0.1) < 1e-12
    assert r[3] == 1 and r[5] == 0 and r[10] == 1


def test_extreme_levels():
    p0, p1 = [0.5, 0.5, 0.0], [0.2, 0.3, 0.5]
    assert neyman_pearson(p0, p1, 0.0) == [0, 0, 1]   # free detection where p0 = 0
    r = neyman_pearson(p0, p1, 1.0)
    assert pfa(r, p1) == 1
```
:::

::: {.problem #prob-camib-sts-2-q1 origin="external" source="camib-sts-2-q1"}
Let $X$ have density function
$$f(x\mid\theta)=\frac{\theta}{(x+\theta)^2},\qquad x>0,$$
where $\theta\in(0,\infty)$ is an unknown parameter. Find the likelihood ratio test of size $0.05$ of $H_0:\theta=1$ against $H_1:\theta=2$ and show that the probability of Type II error is $19/21$.
:::

::: {.problem #prob-camib-sts-2-q2 origin="external" source="camib-sts-2-q2"}
Let $X\sim N(\mu,1)$ where $\mu$ is unknown. Find the most powerful tests of sizes $0.05$ and $0.01$ for the following hypotheses:

(a) $H_0:\mu=0$ vs $H_1:\mu=4$.

(b) $H_0:\mu=4$ vs $H_1:\mu=0$.

Explain how to interpret your results when the realised value is $X(\omega)=2.1$.
:::

::: {.problem #prob-camib-sts-2-q5 origin="external" source="camib-sts-2-q5"}
Let $f_0$ and $f_1$ be probability mass functions on a countable set $\mathcal X$. State and prove a version of the Neyman–Pearson lemma for a size $\alpha$ test of $H_0:f=f_0$ against $H_1:f=f_1$ assuming that $\alpha$ is such that there exists a likelihood ratio test of exact size $\alpha$.
:::

::: {.problem #prob-camib-sts-2-q12 origin="external" source="camib-sts-2-q12"}
(Harder) In Question 5, does there exist a version of the Neyman–Pearson lemma when a likelihood ratio test of exact size $\alpha$ does not exist?
:::
