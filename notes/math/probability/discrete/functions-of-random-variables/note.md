---
title: "Functions of a Random Variable and Spread"
sources: [cs70-16.1]
requires: [math/probability/discrete/indicator-variables]
status: draft
---

<!-- Split from math/probability/discrete/covariance-and-correlation on 2026-11-17 (block ids unchanged). Added from CS70 Note 16 (cs70-16.1), in our own wording; proofs written out in steps. -->

## Functions of a random variable

::: {#prp-expectation-of-function .proposition name="Expectation of a function of X"}

For any function $f$ on the values of $X$,
$$E[f(X)]=\sum_x f(x)\Pr(X=x).$$
This is sometimes called the *law of the unconscious statistician*.

:::

::: {.proof}

1. Let $Y=f(X)$. The event $Y=y$ is the disjoint union of the events $X=x$ with $f(x)=y$, so $\Pr(Y=y)=\sum_{x:\,f(x)=y}\Pr(X=x)$.

2. By @def-expectation,
   $$E[Y]=\sum_y y\Pr(Y=y)=\sum_y\ \sum_{x:\,f(x)=y} f(x)\Pr(X=x).$$

3. Every value $x$ appears in exactly one inner sum, the one with $y=f(x)$, so the double sum is $\sum_x f(x)\Pr(X=x)$.

:::

## Spread: the random walk

::: {#prp-random-walk-square .proposition name="Squared distance of a random walk"}

A particle starts at $0$ and makes $n$ independent moves, each $+1$ or $-1$ with probability $\frac12$. Its position is $S_n=X_1+\cdots+X_n$. Then $E[S_n]=0$ and $E[S_n^2]=n$.

:::

::: {.proof}

1. $E[X_i]=\frac12\cdot1+\frac12\cdot(-1)=0$, so $E[S_n]=0$ by linearity.

2. Expanding the square, $S_n^2=\sum_i X_i^2+\sum_{i\ne j}X_iX_j$.

3. $X_i^2=1$ always, so $E[X_i^2]=1$.

4. For $i\ne j$, $X_i$ and $X_j$ are independent, so $E[X_iX_j]=E[X_i]E[X_j]=0$ (@thm-expectation-of-product).

5. By linearity, $E[S_n^2]=n\cdot1+0=n$.

:::

::: {#rmk-covariance-and-correlation-1 .remark name="Typical distance"}

$E[S_n]=0$ says nothing about how far the particle wanders, because moves to the left and right cancel. The squared distance has mean $n$, which suggests a typical distance of about $\sqrt n$. This is the idea behind the variance, $E[(X-\mu)^2]$ (@def-variance-standard-deviation).

:::

::: {#prp-fixed-points-variance .proposition name="Variance of the number of fixed points"}

For the number $X_n$ of fixed points of a random permutation of $n\ge2$ elements, $\mathrm{Var}(X_n)=1$.

:::

::: {.proof}

1. Write $X_n=I_1+\cdots+I_n$ as in @thm-expected-fixed-points, so $E[X_n]=1$.

2. $E[X_n^2]=\sum_i E[I_i^2]+\sum_{i\ne j}E[I_iI_j]$ by expanding the square and linearity.

3. $I_i^2=I_i$, so $E[I_i^2]=\frac1n$.

4. For $i\ne j$, $I_iI_j$ indicates "both $i$ and $j$ are fixed". There are $(n-2)!$ such permutations, so $E[I_iI_j]=\frac{(n-2)!}{n!}=\frac1{n(n-1)}$.

5. The second sum has $n(n-1)$ terms, so $E[X_n^2]=n\cdot\frac1n+n(n-1)\cdot\frac1{n(n-1)}=2$.

6. By @prp-expectation-and-variance-1, $\mathrm{Var}(X_n)=2-1^2=1$.

:::
