---
title: "Expectation, Median, Mode and Variance"
sources: [fit1058-cn-10.3, fit1058-cn-10.4, fit1058-cn-10.5, fit1058-cn-10.6]
requires: []
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/09-probability.tex: Expectation; Median; Mode; Variance. -->

## Expectation

::: {#def-expectation .definition name="Expectation"}

The *expectation* (or *expected value*, or *mean*) of $X$ is
$$E[X] = \sum_{u\in U} X(u)\Pr(u) = \sum_k k\cdot\Pr(X=k).$$

:::

::: {#exm-expectation-and-variance-1 .example}

For one fair die, $E[X]=(1+2+3+4+5+6)/6=21/6=3.5$. The expectation need not be a possible value of $X$.

:::

::: {#thm-linearity-of-expectation .theorem name="Linearity of expectation"}

For any random variables $X,Y$ and constants $a,b$,
$$E[aX+b] = aE[X]+b, \qquad E[X+Y] = E[X]+E[Y].$$

:::

::: {.proof}

$E[X+Y] = \sum_{u}(X(u)+Y(u))\Pr(u) = \sum_u X(u)\Pr(u) + \sum_u Y(u)\Pr(u) = E[X]+E[Y]$. The first identity is proved the same way.

:::

::: {.remark name="No independence required"}

Linearity holds for *any* $X,Y$: the proof never uses independence. For example, the expected total of two dice is $3.5+3.5=7$.

:::

## Median

::: {#def-median .definition name="Median"}

$m$ is a *median* of $X$ if $\Pr(X\le m)\ge\tfrac12$ and $\Pr(X\ge m)\ge\tfrac12$.

:::

::: {#exm-expectation-and-variance-1-2 .example}

For one die, every $m$ between $3$ and $4$ satisfies the definition; when the median falls in a gap like this we take the middle, $3.5$. For the points $X$ on a random Scrabble tile, $\Pr(X=0)=0.02$, $\Pr(X=1)=0.68$, $\Pr(X\ge2)=0.3$, so $\Pr(X\le1)=0.7$ and $\Pr(X\ge1)=0.98$, and the median is $1$.

:::

::: {.remark name="Median vs.\ mean"}

The median is less affected by rare extreme values. For a lottery ticket, the prize money has median $0$, even though a huge but very unlikely prize can make the mean much larger.

:::

## Mode

::: {#def-mode .definition name="Mode"}

A *mode* of $X$ is a value $k$ that maximises $\Pr(X=k)$.

:::

::: {#exm-expectation-and-variance-1-3 .example}

The total of two dice has mode $7$. A fair die has every value $1,\dots,6$ as a mode, so a mode need not be unique.

:::

## Variance

::: {#def-variance-standard-deviation .definition name="Variance, standard deviation"}

With $\mu=E[X]$, the *variance* of $X$ is $\mathrm{Var}(X) = E\big[(X-\mu)^2\big]$, and the *standard deviation* is $\sigma_X = \sqrt{\mathrm{Var}(X)}$.

:::

::: {.remark name="Units"}

The variance is in the square of the units of $X$; the standard deviation is back in the units of $X$, which makes it easier to interpret as a typical distance from the mean.

:::

::: {#prp-expectation-and-variance-1 .proposition}

$\mathrm{Var}(X) = E[X^2] - E[X]^2$.

:::

::: {.proof}

Let $\mu=E[X]$. By linearity, $E[(X-\mu)^2] = E[X^2]-2\mu E[X]+\mu^2 = E[X^2]-\mu^2$.

:::

::: {#exm-expectation-and-variance-1-4 .example}

For one die, $E[X^2]=(1+4+9+16+25+36)/6=91/6$, so $\mathrm{Var}(X)=\frac{91}6-3.5^2=\frac{35}{12}\approx2.92$ and $\sigma_X\approx1.71$.

:::

::: {#thm-variance-of-an-independent-sum .theorem name="Variance of an independent sum"}

If $X,Y$ are independent, then $\mathrm{Var}(X+Y) = \mathrm{Var}(X)+\mathrm{Var}(Y)$.

:::

::: {.proof}

First, independence gives $E[XY]=E[X]E[Y]$: in $E[XY]=\sum_{r,s}rs\Pr(X=r,Y=s)$, replace $\Pr(X=r,Y=s)$ by $\Pr(X=r)\Pr(Y=s)$ and factor the double sum. Then
$$\mathrm{Var}(X+Y) = E[X^2]+2E[XY]+E[Y^2] - (E[X]+E[Y])^2 = \big(E[X^2]-E[X]^2\big)+\big(E[Y^2]-E[Y]^2\big).$$

:::

::: {#exm-expectation-and-variance-2 .example}

The total of two dice has variance $\frac{35}{12}+\frac{35}{12}=\frac{35}6$.

:::

::: {#thm-chebyshev-s-inequality .theorem name="Chebyshev's inequality"}

For any $a>0$,  $\Pr\big(|X-E[X]|\ge a\big) \le \dfrac{\mathrm{Var}(X)}{a^2}$.

:::

::: {.proof}

Let $\mu=E[X]$. Dropping the terms with $|k-\mu|<a$, and then using $(k-\mu)^2\ge a^2$ in the rest,
$$\mathrm{Var}(X) = \sum_k (k-\mu)^2\Pr(X=k) \ge \sum_{k:\,|k-\mu|\ge a} (k-\mu)^2\Pr(X=k) \ge a^2\Pr(|X-\mu|\ge a).$$
Divide by $a^2$.

:::

::: {.remark name="Any distribution"}

Chebyshev’s inequality holds for every distribution, with no assumption about its shape. Taking $a=c\sigma$ gives $\Pr(|X-\mu|\ge c\sigma)\le1/c^2$: e.g. at most $\frac14$ of the probability lies two or more standard deviations from the mean.

:::
