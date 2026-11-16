---
title: "Standard Distributions"
sources: [fit1058-cn-10.7, fit1058-cn-10.8, fit1058-cn-10.9, fit1058-cn-10.10, cs70-13.3.1, cs70-19.1.1, cs70-19.2.1]
requires: [math/probability/expectation-and-variance, math/discrete/counting/combinations]
status: draft
---

<!-- Migrated from 1058note notes/chapters/09-probability.tex: Uniform distribution; Binomial distribution; Poisson distribution; Geometric distribution. -->
<!-- Proofs written out in steps; the Poisson moments and the tail sum method for the Geometric moments follow CS70 Note 19 (cs70-19.1.1, cs70-19.2.1), in our own wording. -->

## Uniform distribution

::: {#def-discrete-uniform-distribution .definition name="Discrete uniform distribution"}

$X\sim\mathrm{Unif}(a,b)$ means $X$ takes each integer value in $[a,b]$ with the same probability $1/(b-a+1)$.

:::

```{=latex}
\begin{tikzpicture}[x=0.75cm, y=11cm, every node/.style={note}]
  \foreach \y in {0.1,0.2,0.3} {\draw[rule] (-0.6,\y) -- (10.6,\y); \node[left] at (-0.6,\y) {\y};}
  \draw (-0.6,0) -- (10.6,0);
  \foreach \k/\p in {1/0.167, 2/0.167, 3/0.167, 4/0.167, 5/0.167, 6/0.167} \fill[primaryStrong] (\k-0.32,0) rectangle (\k+0.32,\p);
  \foreach \k in {0,...,10} \node[below] at (\k,0) {\k};
  \draw[accent, dashed] (3.5,0) -- (3.5,0.31) node[above] {$E[X]=3.5$};
  \node[anchor=south, heading] at (5,0.36) {$\mathrm{Unif}(1,6)$ (a fair die)};
\end{tikzpicture}
```

::: {#exm-standard-distributions-1 .example}

A fair coin with Tails $=0$ and Heads $=1$ is $\mathrm{Unif}(0,1)$; a fair die is $\mathrm{Unif}(1,6)$. The uniform distribution is also used to model ignorance: with no other information, the age of an adult learner driver might be modelled as $\mathrm{Unif}(18,21)$.

:::

::: {#prp-standard-distributions-1 .proposition}

If $X\sim\mathrm{Unif}(1,n)$, then $E[X] = \dfrac{n+1}{2}$ and $\mathrm{Var}(X) = \dfrac{n^2-1}{12}$.

:::

::: {.proof}

1. Each value $k\in\{1,\dots,n\}$ has probability $\frac1n$. By @def-expectation and @thm-sums-and-series-1,
   $$E[X]=\sum_{k=1}^n k\cdot\frac1n=\frac1n\cdot\frac{n(n+1)}2=\frac{n+1}2.$$

2. The sum of squares is $\sum_{k=1}^n k^2=\frac{n(n+1)(2n+1)}6$. This holds for $n=1$, and if it holds for $n$, then
   $$\frac{n(n+1)(2n+1)}6+(n+1)^2=\frac{(n+1)\bigl(2n^2+7n+6\bigr)}6=\frac{(n+1)(n+2)(2n+3)}6,$$
   which is the formula for $n+1$. So it holds for all $n\ge1$ by induction.

3. Hence
   $$E[X^2]=\sum_{k=1}^n k^2\cdot\frac1n=\frac{(n+1)(2n+1)}6.$$

4. By @prp-expectation-and-variance-1,
   $$\mathrm{Var}(X)=E[X^2]-E[X]^2=\frac{(n+1)(2n+1)}6-\frac{(n+1)^2}4=\frac{(n+1)\bigl(2(2n+1)-3(n+1)\bigr)}{12}=\frac{(n+1)(n-1)}{12}=\frac{n^2-1}{12}.$$

:::

## Binomial distribution

::: {#def-bernoulli-trial .definition name="Bernoulli trial"}

A *Bernoulli trial* is a random experiment with two outcomes, “success” with probability $p$ and “failure” with probability $1-p$.

:::

::: {#def-binomial-distribution .definition name="Binomial distribution"}

$X\sim\mathrm{Bin}(n,p)$ is the number of successes in $n$ independent Bernoulli trials, each with success probability $p$:
$$\Pr(X=k) = \binom{n}{k}p^k(1-p)^{n-k}, \qquad k=0,1,\dots,n.$$

:::

```{=latex}
\begin{tikzpicture}[x=0.75cm, y=11cm, every node/.style={note}]
  \foreach \y in {0.1,0.2,0.3} {\draw[rule] (-0.6,\y) -- (10.6,\y); \node[left] at (-0.6,\y) {\y};}
  \draw (-0.6,0) -- (10.6,0);
  \foreach \k/\p in {0/0.028, 1/0.121, 2/0.233, 3/0.267, 4/0.200, 5/0.103, 6/0.037, 7/0.009, 8/0.001} \fill[primaryStrong] (\k-0.32,0) rectangle (\k+0.32,\p);
  \foreach \k in {0,...,10} \node[below] at (\k,0) {\k};
  \draw[accent, dashed] (3,0) -- (3,0.31) node[above] {$E[X]=3$};
  \node[anchor=south, heading] at (5,0.36) {$\mathrm{Bin}(10,\,0.3)$};
\end{tikzpicture}
```

::: {#rmk-standard-distributions-1 .remark name="Where the formula comes from"}

$\binom nk$ counts the ways to choose which $k$ of the $n$ trials succeed (@sec-math-discrete-counting-combinations), and each such outcome has probability $p^k(1-p)^{n-k}$ by independence.

:::

::: {#exm-standard-distributions-1-2 .example}

For $n=10$, $p=0.3$:  $\Pr(X=6)=\binom{10}6(0.3)^6(0.7)^4=210\cdot0.000729\cdot0.2401\approx0.037$.

:::

::: {#prp-standard-distributions-1-2 .proposition}

If $X\sim\mathrm{Bin}(n,p)$, then $E[X] = np$ and $\mathrm{Var}(X) = np(1-p)$.

:::

::: {.proof}

1. For $i=1,\dots,n$ let $X_i=1$ if trial $i$ succeeds and $X_i=0$ otherwise. Then $X$ counts the successes, so
   $$X=X_1+X_2+\cdots+X_n.$$

2. Each $X_i$ takes the value $1$ with probability $p$ and $0$ with probability $1-p$, so $E[X_i]=1\cdot p+0\cdot(1-p)=p$.

3. By @thm-linearity-of-expectation, applied $n-1$ times,
   $$E[X]=E[X_1]+\cdots+E[X_n]=np.$$

4. For the variance, expand the square:
   $$X^2=\sum_{i=1}^n X_i^2+\sum_{i\ne j}X_iX_j.$$
   The second sum has $n(n-1)$ ordered pairs $(i,j)$ with $i\ne j$.

5. Since $X_i\in\{0,1\}$, we have $X_i^2=X_i$, so $E[X_i^2]=p$.

6. For $i\ne j$, trials $i$ and $j$ are independent, so $X_i$ and $X_j$ are independent random variables. By @thm-expectation-of-product, $E[X_iX_j]=E[X_i]\,E[X_j]=p^2$.

7. By linearity, steps 4–6 give
   $$E[X^2]=np+n(n-1)p^2.$$

8. By @prp-expectation-and-variance-1,
   $$\mathrm{Var}(X)=E[X^2]-E[X]^2=np+n(n-1)p^2-n^2p^2=np-np^2=np(1-p).$$

:::

## Poisson distribution

::: {#def-poisson-distribution .definition name="Poisson distribution"}

$X\sim\mathrm{Poisson}(\mu)$, for a parameter $\mu>0$, means
$$\Pr(X=k) = \frac{e^{-\mu}\mu^k}{k!}, \qquad k=0,1,2,\dots$$

:::

```{=latex}
\begin{tikzpicture}[x=0.75cm, y=11cm, every node/.style={note}]
  \foreach \y in {0.1,0.2,0.3} {\draw[rule] (-0.6,\y) -- (10.6,\y); \node[left] at (-0.6,\y) {\y};}
  \draw (-0.6,0) -- (10.6,0);
  \foreach \k/\p in {0/0.050, 1/0.149, 2/0.224, 3/0.224, 4/0.168, 5/0.101, 6/0.050, 7/0.022, 8/0.008, 9/0.003, 10/0.001} \fill[primaryStrong] (\k-0.32,0) rectangle (\k+0.32,\p);
  \foreach \k in {0,...,10} \node[below] at (\k,0) {\k};
  \draw[accent, dashed] (3,0) -- (3,0.31) node[above] {$E[X]=3$};
  \node[anchor=south, heading] at (5,0.36) {$\mathrm{Poisson}(3)$ (continues past $10$)};
\end{tikzpicture}
```

::: {#rmk-standard-distributions-2 .remark name="When it applies"}

The Poisson distribution counts events that happen independently at random times, at a steady average rate, during a fixed time interval: phone calls to a call centre, visits to a website, coins tossed into a busker’s cap, alpha particles emitted by radioactive material. The parameter $\mu$ is the average number of events in the interval.

:::

::: {#exm-standard-distributions-1-3 .example}

For $\mu=3$:  $\Pr(X\le2)=e^{-3}\bigl(1+3+\tfrac92\bigr)\approx0.0498+0.1494+0.2240\approx0.423$.

:::

::: {#prp-standard-distributions-1-3 .proposition}

If $X\sim\mathrm{Poisson}(\mu)$, then $E[X]=\mu$ and $\mathrm{Var}(X)=\mu$.

:::

::: {.proof}

1. We use the exponential series from calculus: for every real $x$,
   $$e^{x}=\sum_{j=0}^{\infty}\frac{x^j}{j!}.$$
   With $x=\mu$ it shows that the probabilities in @def-poisson-distribution add up to $e^{-\mu}e^{\mu}=1$.

2. By @def-expectation,
   $$E[X]=\sum_{k=0}^{\infty}k\,\frac{e^{-\mu}\mu^k}{k!}.$$
   The term $k=0$ is $0$, and for $k\ge1$ we have $\frac{k}{k!}=\frac1{(k-1)!}$.

3. Substituting $j=k-1$,
   $$E[X]=\mu e^{-\mu}\sum_{k=1}^{\infty}\frac{\mu^{k-1}}{(k-1)!}=\mu e^{-\mu}\sum_{j=0}^{\infty}\frac{\mu^{j}}{j!}=\mu e^{-\mu}e^{\mu}=\mu.$$

4. In the same way, the terms $k=0,1$ of $E[X(X-1)]$ are $0$, and for $k\ge2$ we have $\frac{k(k-1)}{k!}=\frac1{(k-2)!}$. With $j=k-2$,
   $$E[X(X-1)]=\sum_{k=2}^{\infty}k(k-1)\frac{e^{-\mu}\mu^k}{k!}=\mu^2e^{-\mu}\sum_{j=0}^{\infty}\frac{\mu^j}{j!}=\mu^2.$$

5. All terms in these series are non-negative and the series converge, so they may be added term by term. Since $X^2=X(X-1)+X$, this gives
   $$E[X^2]=E[X(X-1)]+E[X]=\mu^2+\mu.$$

6. By @prp-expectation-and-variance-1,
   $$\mathrm{Var}(X)=E[X^2]-E[X]^2=\mu^2+\mu-\mu^2=\mu.$$

:::

::: {#thm-poisson-as-a-limit-of .theorem name="Poisson as a limit of binomial"}

Fix $\mu>0$. As $n\to\infty$ with $p=\mu/n$,
$$\binom{n}{k}p^k(1-p)^{n-k} \to \frac{e^{-\mu}\mu^k}{k!}.$$

:::

::: {.proof}

1. Fix $k\ge0$ and take $n>\max(k,\mu)$, so that $0<p=\mu/n<1$. Since $\binom nk=\frac{n(n-1)\cdots(n-k+1)}{k!}$ and $p^k=\frac{\mu^k}{n^k}$,
   $$\binom{n}{k}p^k(1-p)^{n-k}=\frac{\mu^k}{k!}\cdot\frac{n(n-1)\cdots(n-k+1)}{n^k}\cdot\Bigl(1-\frac\mu n\Bigr)^{n}\cdot\Bigl(1-\frac\mu n\Bigr)^{-k}.$$

2. The second factor is a product of the $k$ factors $1-\frac in$ for $i=0,\dots,k-1$:
   $$\frac{n(n-1)\cdots(n-k+1)}{n^k}=\prod_{i=0}^{k-1}\Bigl(1-\frac in\Bigr).$$
   Each factor tends to $1$ as $n\to\infty$. There are $k$ of them and $k$ does not depend on $n$, so the product tends to $1$.

3. Since $1-\frac\mu n\to1$ and the exponent $-k$ is fixed, $\bigl(1-\frac\mu n\bigr)^{-k}\to1$.

4. By the standard limit $\bigl(1+\frac xn\bigr)^n\to e^{x}$ with $x=-\mu$, we get $\bigl(1-\frac\mu n\bigr)^n\to e^{-\mu}$.

5. The limit of a product of finitely many convergent factors is the product of their limits. So the left side tends to
   $$\frac{\mu^k}{k!}\cdot1\cdot e^{-\mu}\cdot1=\frac{e^{-\mu}\mu^k}{k!}.$$

:::

::: {#rmk-standard-distributions-3 .remark name="Approximating the binomial"}

So $\mathrm{Bin}(n,p)$ with $n$ large, $p$ small and $np$ moderate is well approximated by $\mathrm{Poisson}(np)$: think of many trials, each with a small chance of a rare event.

:::

## Geometric distribution

::: {#def-geometric-distribution .definition name="Geometric distribution"}

$X\sim\mathrm{Geom}(p)$ is the number of independent Bernoulli trials, each with success probability $p$, up to and including the first success:
$$\Pr(X=k) = (1-p)^{k-1}p, \qquad k=1,2,3,\dots$$

:::

```{=latex}
\begin{tikzpicture}[x=0.75cm, y=11cm, every node/.style={note}]
  \foreach \y in {0.1,0.2,0.3} {\draw[rule] (-0.6,\y) -- (10.6,\y); \node[left] at (-0.6,\y) {\y};}
  \draw (-0.6,0) -- (10.6,0);
  \foreach \k/\p in {1/0.300, 2/0.210, 3/0.147, 4/0.103, 5/0.072, 6/0.050, 7/0.035, 8/0.025, 9/0.017, 10/0.012} \fill[primaryStrong] (\k-0.32,0) rectangle (\k+0.32,\p);
  \foreach \k in {0,...,10} \node[below] at (\k,0) {\k};
  \draw[accent, dashed] (3.333,0) -- (3.333,0.31) node[above] {$E[X]=\tfrac{10}{3}$};
  \node[anchor=south, heading] at (5,0.36) {$\mathrm{Geom}(0.3)$ (continues past $10$)};
\end{tikzpicture}
```

::: {#rmk-standard-distributions-4 .remark name="Two conventions"}

Some books instead count the failures *before* the first success, which is $X-1$. Check which one is meant.

:::

::: {#exm-standard-distributions-1-4 .example}

For $p=0.3$:  $\Pr(X=6)=(0.7)^5\cdot0.3\approx0.050$.

:::

::: {#prp-standard-distributions-1-4 .proposition}

If $X\sim\mathrm{Geom}(p)$, then $E[X] = \dfrac1p$ and $\mathrm{Var}(X)=\dfrac{1-p}{p^2}$.

:::

::: {.proof}

Write $q=1-p$, so $0\le q<1$.

1. **Tails.** For $i\ge1$, the event $X\ge i$ means that the first $i-1$ trials all fail. The trials are independent, so
   $$\Pr(X\ge i)=q^{\,i-1}.$$

2. **Tail sum formula.** If $X$ takes values in $\{1,2,3,\dots\}$, then $E[X]=\sum_{i\ge1}\Pr(X\ge i)$. Indeed, write $j=\sum_{i=1}^{j}1$ and swap the order of summation (@exm-swapping-the-order-of-a):
   $$E[X]=\sum_{j\ge1}j\Pr(X=j)=\sum_{j\ge1}\sum_{i=1}^{j}\Pr(X=j)=\sum_{i\ge1}\sum_{j\ge i}\Pr(X=j)=\sum_{i\ge1}\Pr(X\ge i).$$
   All terms are non-negative, so swapping the order of an infinite double sum does not change its value.

3. **Expectation.** By steps 1–2 and @thm-convergence-condition (with ratio $q$, $|q|<1$),
   $$E[X]=\sum_{i\ge1}q^{\,i-1}=\frac1{1-q}=\frac1p.$$

4. **Second moment.** In the same way, write $j^2=\sum_{i=1}^{j}(2i-1)$ (the sum of the first $j$ odd numbers) and swap the order of summation:
   $$E[X^2]=\sum_{j\ge1}j^2\Pr(X=j)=\sum_{i\ge1}(2i-1)\Pr(X\ge i)=2\sum_{i\ge1}i\,q^{\,i-1}-\sum_{i\ge1}q^{\,i-1}.$$

5. **The remaining series.** By @def-geometric-distribution,
   $$E[X]=\sum_{i\ge1}i\,q^{\,i-1}p,$$
   so $\sum_{i\ge1}i\,q^{\,i-1}=\frac{E[X]}p=\frac1{p^2}$. In particular this series converges. Together with $\sum_{i\ge1}q^{\,i-1}=\frac1p$ from step 3,
   $$E[X^2]=\frac2{p^2}-\frac1p.$$

6. **Variance.** By @prp-expectation-and-variance-1,
   $$\mathrm{Var}(X)=E[X^2]-E[X]^2=\frac2{p^2}-\frac1p-\frac1{p^2}=\frac{1-p}{p^2}.$$

:::

::: {#rmk-standard-distributions-5 .remark name="Memoryless property"}

Given that the first $t$ trials have all failed, the number of further trials needed is again $\mathrm{Geom}(p)$: past failures do not make success “due”. Examples include the number of loop iterations until a random stopping condition holds, the number of time intervals until a component fails, and the number of balls a cricket batter faces.

:::

## Comparing the four

All four plots above use the same axes and have mean about $3$, so the shapes can be compared directly.

| | $X$ is | $E[X]$ | $\mathrm{Var}(X)$ | use when |
|---|---|---|---|---|
| $\mathrm{Unif}(a,b)$ | one of $a,\dots,b$ | $\frac{a+b}2$ | $\frac{(b-a+1)^2-1}{12}$ | all outcomes equally likely |
| $\mathrm{Bin}(n,p)$ | successes in $n$ trials | $np$ | $np(1-p)$ | a fixed number of trials |
| $\mathrm{Poisson}(\mu)$ | events in an interval | $\mu$ | $\mu$ | a steady rate, no fixed number of trials |
| $\mathrm{Geom}(p)$ | trials to first success | $\frac1p$ | $\frac{1-p}{p^2}$ | repeat until the first success |

Binomial and Poisson count *how many* successes; Geometric counts *how long* until one. Binomial is bounded by $n$, while Poisson and Geometric have no upper limit. For large $n$ and small $p$, $\mathrm{Bin}(n,p)\approx\mathrm{Poisson}(np)$ (@thm-poisson-as-a-limit-of). Only Geometric is memoryless.
