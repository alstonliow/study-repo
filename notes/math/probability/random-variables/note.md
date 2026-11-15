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

::: {#rmk-random-variables-1 .remark name="Notation"}

$X=k$ is shorthand for the event $\{u\in U : X(u)=k\}$, so $\Pr(X=k)$ means the probability of that event. Similarly for $X\le k$, etc.

:::

::: {#def-independent-random-variables .definition name="Independent random variables"}

$X,Y$ are *independent* if for all $r,s$,
$$\Pr(X=r \text{ and } Y=s) = \Pr(X=r)\cdot\Pr(Y=s).$$

:::

::: {#rmk-random-variables-2 .remark name="Compared with independent events"}

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

::: {#fig-random-variables-1}

```{=latex}
\begin{tikzpicture}[x=0.62cm, y=0.42cm]
  \foreach \y in {2,4,6} {\draw[rule] (1.4,\y) -- (12.6,\y); \node[left, tick] at (1.4,\y) {$\y/36$};}
  \draw (1.4,0) -- (12.6,0);
  \foreach \k/\c in {2/1,3/2,4/3,5/4,6/5,7/6,8/5,9/4,10/3,11/2,12/1} {
    \fill[primaryStrong] (\k-0.34,0) rectangle (\k+0.34,\c);
    \node[below, tick] at (\k,0) {$\k$};
  }
\end{tikzpicture}
```

The distribution of the total $Z$ of two fair dice: symmetric about $7$, the most likely total

:::
