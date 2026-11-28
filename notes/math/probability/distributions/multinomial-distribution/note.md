---
title: "Multinomial Distribution"
sources: [camib-st-1]
requires: [math/probability/distributions/binomial-distribution, math/probability/random-variables/covariance-and-correlation]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part IB Statistics (Lent 2025, lecturer's notes), Lecture 1 (review of important distributions), in our own wording; proofs written out in steps. -->

The binomial distribution counts the successes among $n$ trials with two outcomes. With $k$ possible outcomes per trial, the vector of counts is multinomial; it is the model behind contingency tables and goodness-of-fit tests.

::: {#def-multinomial-distribution .definition name="Multinomial distribution"}

Perform $n$ independent trials; in each trial outcome $i\in\{1,\dots,k\}$ occurs with probability $p_i$, where $p=(p_1,\dots,p_k)$ lies in the standard simplex ($p_i\ge0$, $\sum_ip_i=1$). Let $N_i$ be the number of trials with outcome $i$. Then $N=(N_1,\dots,N_k)$ has the *multinomial distribution* $\mathrm{Multinomial}(n;p)$,
$$
P(N_1=n_1,\dots,N_k=n_k)=\frac{n!}{n_1!\cdots n_k!}\,p_1^{n_1}\cdots p_k^{n_k},\qquad n_i\in\mathbb N_0,\ \sum_in_i=n .
$$

:::

::: {.proof}

A fixed sequence of outcomes with counts $n_1,\dots,n_k$ has probability $\prod_ip_i^{n_i}$ by independence, and there are $n!/(n_1!\cdots n_k!)$ such sequences (@thm-bookkeeper-rule).

:::

::: {#fig-multinomial-distribution-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[emph] (0,0) -- (4,0) -- (2,3.46) -- cycle;
\node[lab, below left] at (0,0) {$e_1$};
\node[lab, below right] at (4,0) {$e_2$};
\node[lab, above] at (2,3.46) {$e_3$};
\node[hl dot] at (2.2,1.2) {};
\node[lab, right] at (2.3,1.2) {$p$};
\draw[faint] (0,0) -- (2.2,1.2);
\end{tikzpicture}
\end{center}
```

For $k=3$ the probability vector $p$ is a point of the triangle with vertices $e_1,e_2,e_3$; the vertices are the degenerate cases in which one outcome has probability $1$.

:::

::: {#prp-multinomial-marginals .proposition name="Marginals and covariances"}

If $N\sim\mathrm{Multinomial}(n;p)$ then $N_i\sim\mathrm{Bin}(n,p_i)$, and for $i\ne j$
$$
\mathrm{Cov}(N_i,N_j)=-np_ip_j .
$$
In particular $N_1,\dots,N_k$ are not independent.

:::

::: {.proof}

1. Let $I_{t,i}$ be the indicator that trial $t$ gives outcome $i$, so $N_i=\sum_{t=1}^nI_{t,i}$. This is a sum of $n$ independent Bernoulli$(p_i)$ variables, hence $\mathrm{Bin}(n,p_i)$.

2. For $i\ne j$, indicators from different trials are independent, so $\mathrm{Cov}(I_{t,i},I_{s,j})=0$ for $t\ne s$. In the same trial $I_{t,i}I_{t,j}=0$, so $\mathrm{Cov}(I_{t,i},I_{t,j})=0-p_ip_j$.

3. Summing the $n$ nonzero covariances gives $\mathrm{Cov}(N_i,N_j)=-np_ip_j<0$ when $p_i,p_j>0$. (A larger count of one outcome leaves fewer trials for the others, as $\sum_iN_i=n$.)

:::

::: {#exm-multinomial-dice .example name="One of each face"}

Throw a fair die six times. The probability that every face appears exactly once is
$$\frac{6!}{1!\cdots1!}\Bigl(\frac16\Bigr)^6=\frac{720}{46656}\approx0.0154 .$$

:::
