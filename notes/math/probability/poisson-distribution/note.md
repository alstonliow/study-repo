---
title: "Poisson Distribution"
sources: [fit1058-cn-10.9, cs70-19.2.1]
requires: [math/probability/binomial-distribution]
status: draft
---

<!-- Split from math/probability/standard-distributions on 2026-11-16 (SPEC §2.6); block ids unchanged. -->
<!-- Migrated from 1058note notes/chapters/09-probability.tex: Poisson distribution. -->
<!-- Proof written out in steps; it follows CS70 Note 19 (cs70-19.2.1), in our own wording. -->

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
