---
title: "Random Variables and Distributions"
sources: [fit1058-cn-10.1, fit1058-cn-10.2]
requires: [math/probability/conditional-probability]
status: draft
---

<!-- Migrated from 1058note notes/chapters/09-probability.tex: Random variables; Probability distributions. -->

## Random variables

::: {#def-random-variable .definition name="Random variable"}

A *random variable* on a sample space $U$ is a function $X:U\to\mathbb{R}$.

:::

::: {#exm-random-variables-1 .example}

Throw two dice, so $U=\{1,\dots,6\}^2$. The total $Z(d_1,d_2)=d_1+d_2$ is a random variable with values in $\{2,\dots,12\}$; the event $Z=9$ is $\{(3,6),(4,5),(5,4),(6,3)\}$.

:::

::: {.remark name="Notation"}

$X=k$ is shorthand for the event $\{u\in U : X(u)=k\}$, so $\Pr(X=k)$ means the probability of that event. Similarly for $X\le k$, etc.

:::

::: {#def-independent-random-variables .definition name="Independent random variables"}

$X,Y$ are *independent* if for all $r,s$,
$$\Pr(X=r \text{ and } Y=s) = \Pr(X=r)\cdot\Pr(Y=s).$$

:::

::: {.remark name="Compared with independent events"}

This says that the events $X=r$ and $Y=s$ are independent (@sec-math-probability-conditional-probability) for *every* pair of values $r,s$. The numbers shown on two separate fair dice are independent random variables.

:::

## Probability distributions

::: {#def-probability-distribution .definition name="Probability distribution"}

The *probability distribution* of $X$ is the function $p(k) = \Pr(X=k)$, over the possible values $k$ of $X$. These probabilities add up to $1$.

:::

::: {#exm-random-variables-1-2 .example}

For the total $Z$ of two fair dice,
$$\begin{array}{c|ccccccccccc}
k & 2&3&4&5&6&7&8&9&10&11&12\\\hline
36\Pr(Z=k) & 1&2&3&4&5&6&5&4&3&2&1
\end{array}$$
The distribution is symmetric about $7$, the most likely total.

:::
