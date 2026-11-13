---
title: "Sums and Series"
sources: [fit1058-cn-6.10, fit1058-cn-6.11, fit1058-cn-6.12, fit1058-cn-6.13, fit1058-cn-6.14, fit1058-cn-6.15]
requires: [math/discrete/proof/induction-examples, math/discrete/sequences/limits]
status: draft
---

<!-- Migrated from 1058note notes/chapters/06-sequences-series.tex: Sums and summation; Finite series; Finite arithmetic series; Finite geometric series; Infinite geometric series; Harmonic numbers. -->

## Sums and summation

::: {#def-summation-notation .definition name="Summation notation"}

$\displaystyle\sum_{k=1}^n a_k = a_1+a_2+\cdots+a_n$. The variable $k$ is a dummy variable: renaming it does not change the sum.

:::

::: {#exm-swapping-the-order-of-a .example name="Swapping the order of a double sum"}

Consider $\sum_{i=1}^{n}\sum_{j=1}^{i} j$, the sum of the triangular array whose row $i$ is $1,2,\dots,i$:
$$\begin{array}{c|ccccc}
i \backslash j & 1 & 2 & 3 & \cdots & n \\\hline
1 & 1 & & & & \\
2 & 1 & 2 & & & \\
3 & 1 & 2 & 3 & & \\
\vdots & \vdots & \vdots & & \ddots & \\
n & 1 & 2 & 3 & \cdots & n
\end{array}$$
Summing row by row gives $1+(1+2)+(1+2+3)+\cdots+(1+\cdots+n)$. Summing column by column instead, column $j$ contains the value $j$ once for each row $i=j,\dots,n$, i.e. $n-j+1$ times. So
$$\sum_{i=1}^{n}\sum_{j=1}^{i} j = \sum_{j=1}^{n}\sum_{i=j}^{n} j = \sum_{j=1}^n j(n-j+1).$$
Both describe the same region $1\le j\le i\le n$, once “by rows” and once “by columns”.

:::

## Finite series

::: {#def-series-partial-sum .definition name="Series, partial sum"}

A *finite series* is the sum of the terms of a finite sequence. For an infinite sequence $(a_k)$, the $n$-th *partial sum* is $S_n=\sum_{k=1}^n a_k$.

:::

## Finite arithmetic series

::: {#thm-sums-and-series-1 .theorem}

$$\sum_{k=1}^n \bigl(a+(k-1)d\bigr) = n\cdot\frac{2a+(n-1)d}{2} = n\cdot\frac{\text{first}+\text{last}}{2}.$$
In particular, $1+2+\cdots+n=\dfrac{n(n+1)}{2}$.

:::

::: {.proof}

Write the sum $S$ forwards and backwards and add term by term. Each of the $n$ pairs adds to $a+\bigl(a+(n-1)d\bigr)=2a+(n-1)d$, so $2S=n\bigl(2a+(n-1)d\bigr)$.

:::

::: {#exm-sums-and-series-1 .example}

$1+3+5+\cdots+99$ has $50$ terms, so it equals $50\cdot\frac{1+99}{2}=2500=50^2$.

:::

## Finite geometric series

::: {#thm-sums-and-series-1-2 .theorem}

For $r\neq1$,
$$\sum_{k=0}^n ar^k = a\cdot\frac{r^{n+1}-1}{r-1}.$$

:::

::: {.proof}

Let $S=a+ar+\cdots+ar^n$. Then $rS=ar+ar^2+\cdots+ar^{n+1}$, and subtracting, all but two terms cancel: $rS-S=ar^{n+1}-a$. Divide by $r-1\ne0$.

:::

::: {#exm-sums-and-series-1-2 .example}

$1+2+4+\cdots+2^n=2^{n+1}-1$ (with $a=1$, $r=2$), as in Exercise 3.7.

:::

## Infinite geometric series

::: {#thm-convergence-condition .theorem name="Convergence condition"}

The infinite geometric series $\sum_{k=0}^\infty ar^k$ (with $a\ne0$) converges if and only if $|r|<1$, and then its sum is $\dfrac{a}{1-r}$.

:::

::: {.proof}

The partial sums are $S_n = a\dfrac{1-r^{n+1}}{1-r}$. If $|r|<1$ then $r^{n+1}\to0$ (@sec-math-discrete-sequences-limits), so $S_n \to \dfrac{a}{1-r}$. If $|r|\ge1$, the terms $ar^k$ do not tend to $0$, so the partial sums cannot settle down to a limit.

:::

::: {#exm-sums-and-series-1-3 .example}

$\frac12+\frac14+\frac18+\cdots=\dfrac{1/2}{1-1/2}=1$, and $0.999\ldots=\dfrac{9/10}{1-1/10}=1$.

:::

## Harmonic numbers

::: {#def-harmonic-numbers .definition name="Harmonic numbers"}

The $n$-th *harmonic number* is $H_n = 1+\frac12+\frac13+\cdots+\frac1n$.

:::

::: {#thm-the-harmonic-series-diverges .theorem name="The harmonic series diverges"}

$H_n\to\infty$ as $n\to\infty$, even though $1/n\to0$.

:::

::: {.proof}

Group the terms of $H_{2^k}$ in blocks:
$$H_{2^k} = 1 + \frac12 + \left(\frac13+\frac14\right) + \left(\frac15+\cdots+\frac18\right) + \cdots + \left(\frac{1}{2^{k-1}+1}+\cdots+\frac{1}{2^k}\right).$$
The $j$-th block has $2^{j-1}$ terms, each at least $1/2^j$, so it adds up to at least $\frac12$. There are $k$ blocks after the first term, so $H_{2^k} \ge 1+\frac{k}{2}$. This tends to $\infty$, and $H_n$ is increasing, so $H_n\to\infty$.

:::

::: {.remark name="Same bound, two proofs"}

This is the bound $H_{2^n}\ge1+n/2$ proved by induction in @sec-math-discrete-proof-induction-examples; here it comes directly from grouping.

:::

::: {.remark name="Growth rate"}

$H_n$ grows like $\log_e n$: in fact $H_n - \log_e n \to \gamma = 0.5772\ldots$ (Euler’s constant), so $H_n\approx\log_e n+\gamma$ for large $n$. It is unknown whether $\gamma$ is rational.

:::

::: {.remark name="A borderline case"}

$(1/2^n)$ and $(1/n^2)$ tend to $0$ and have finite sums, but $(1/n)$ also tends to $0$ yet has an infinite sum: it decays just too slowly.

:::
