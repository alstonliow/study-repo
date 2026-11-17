---
title: "Binomial Distribution"
sources: [fit1058-cn-10.8, cs70-13.3.1, cs70-15.2]
requires: [math/probability/discrete/expectation-and-variance, math/discrete/counting/combinations]
aliases: [math/probability/binomial-distribution]   # old ids (moved)
status: draft
---

<!-- Split from math/probability/standard-distributions on 2026-11-16 (SPEC §2.6); block ids unchanged. -->
<!-- Migrated from 1058note notes/chapters/09-probability.tex: Binomial distribution. -->

::: {#def-bernoulli-trial .definition name="Bernoulli trial"}

A *Bernoulli trial* is a random experiment with two outcomes, “success” with probability $p$ and “failure” with probability $1-p$.

:::

::: {#def-bernoulli-distribution .definition name="Bernoulli distribution"}

$X\sim\mathrm{Bernoulli}(p)$, for $0\le p\le1$, means that $X$ takes only the values $0$ and $1$, with
$$\Pr(X=1)=p,\qquad \Pr(X=0)=1-p.$$
It records the outcome of one Bernoulli trial: $1$ for success, $0$ for failure.

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

::: {#rmk-binomial-distribution-2 .remark name="A probabilistic proof of the binomial theorem"}

The probabilities of a distribution add up to $1$, so $\sum_{k=0}^{n}\binom nk p^k(1-p)^{n-k}=1$. This is the binomial theorem (@thm-binomial-theorem) for $a=p$ and $b=1-p$.

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
