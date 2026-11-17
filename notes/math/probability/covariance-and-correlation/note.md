---
title: "Covariance and Correlation"
sources: [cs70-16.1, cs70-16.4]
requires: [math/probability/indicator-variables]
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 16 (cs70-16.1, cs70-16.4), in our own wording; proofs written out in steps. -->

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

## Covariance

::: {#def-covariance .definition name="Covariance"}

With $\mu_X=E[X]$ and $\mu_Y=E[Y]$, the *covariance* of $X$ and $Y$ is
$$\mathrm{Cov}(X,Y)=E[(X-\mu_X)(Y-\mu_Y)].$$

:::

::: {#prp-covariance-properties .proposition name="Properties of covariance"}

1. $\mathrm{Cov}(X,Y)=E[XY]-E[X]E[Y]$.

2. If $X$ and $Y$ are independent, then $\mathrm{Cov}(X,Y)=0$.

3. $\mathrm{Cov}(X,X)=\mathrm{Var}(X)$.

4. Covariance is bilinear: for constants $a_i,b_j$,
   $$\mathrm{Cov}\Bigl(\sum_i a_iX_i,\ \sum_j b_jY_j\Bigr)=\sum_i\sum_j a_ib_j\,\mathrm{Cov}(X_i,Y_j).$$

5. $\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)+2\,\mathrm{Cov}(X,Y)$.

:::

::: {.proof}

1. Expand and use linearity: $E[(X-\mu_X)(Y-\mu_Y)]=E[XY]-\mu_XE[Y]-\mu_YE[X]+\mu_X\mu_Y=E[XY]-\mu_X\mu_Y$.

2. By @thm-expectation-of-product, $E[XY]=E[X]E[Y]$ for independent $X,Y$; use part 1.

3. Put $Y=X$ in @def-covariance and compare with @def-variance-standard-deviation.

4. By part 1 it is enough to expand $E\bigl[\sum_i a_iX_i\sum_j b_jY_j\bigr]$ and $E\bigl[\sum_i a_iX_i\bigr]E\bigl[\sum_j b_jY_j\bigr]$ as double sums by linearity, and subtract term by term.

5. By parts 3 and 4, $\mathrm{Var}(X+Y)=\mathrm{Cov}(X+Y,X+Y)=\mathrm{Cov}(X,X)+\mathrm{Cov}(Y,Y)+2\,\mathrm{Cov}(X,Y)$, using $\mathrm{Cov}(X,Y)=\mathrm{Cov}(Y,X)$.

:::

::: {#rmk-covariance-and-correlation-2 .remark name="The converse fails"}

Zero covariance does not imply independence. For example, let $X$ be $-1$, $0$ or $1$ with probability $\frac13$ each, and $Y=X^2$. Then $E[XY]=E[X^3]=0=E[X]E[Y]$, so $\mathrm{Cov}(X,Y)=0$, but $Y$ is determined by $X$. Part 5 shows that the variance of a sum is the sum of the variances exactly when the covariance is $0$ (@thm-variance-of-an-independent-sum is the independent case).

:::

## Correlation

::: {#def-correlation .definition name="Correlation"}

If $\sigma_X>0$ and $\sigma_Y>0$, the *correlation* of $X$ and $Y$ is
$$\mathrm{Corr}(X,Y)=\frac{\mathrm{Cov}(X,Y)}{\sigma_X\,\sigma_Y}.$$

:::

::: {#thm-correlation-bound .theorem name="Correlation lies between -1 and 1"}

If $\sigma_X>0$ and $\sigma_Y>0$, then $-1\le\mathrm{Corr}(X,Y)\le1$.

:::

::: {.proof}

1. Standardise: let $\tilde X=(X-\mu_X)/\sigma_X$ and $\tilde Y=(Y-\mu_Y)/\sigma_Y$. Then $E[\tilde X]=E[\tilde Y]=0$ and $E[\tilde X^2]=E[\tilde Y^2]=1$.

2. By part 1 of @prp-covariance-properties and linearity, $E[\tilde X\tilde Y]=\dfrac{E[(X-\mu_X)(Y-\mu_Y)]}{\sigma_X\sigma_Y}=\mathrm{Corr}(X,Y)$.

3. A square is never negative, so
   $$0\le E[(\tilde X-\tilde Y)^2]=2-2E[\tilde X\tilde Y],\qquad 0\le E[(\tilde X+\tilde Y)^2]=2+2E[\tilde X\tilde Y].$$

4. Hence $-1\le E[\tilde X\tilde Y]\le1$, and by step 2 this is the claim.

:::

::: {#rmk-covariance-and-correlation-3 .remark name="When the bound is reached"}

The proof shows that $\mathrm{Corr}(X,Y)=1$ exactly when $E[(\tilde X-\tilde Y)^2]=0$, that is when $\tilde X=\tilde Y$ with probability $1$. Then $Y=aX+b$ with $a>0$. Likewise $\mathrm{Corr}(X,Y)=-1$ gives $Y=aX+b$ with $a<0$. The sign of the covariance shows the direction of the association; the correlation also measures its strength on a fixed scale.

:::
