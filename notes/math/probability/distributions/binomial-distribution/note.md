---
title: "Binomial Distribution"
sources: [fit1058-cn-10.8, cs70-13.3.1, cs70-15.2]
requires: [math/probability/random-variables/expectation-and-variance, math/discrete/counting/combinations]
aliases: [math/probability/binomial-distribution, math/probability/discrete/binomial-distribution]   # old ids (moved)
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

::: {#fig-binomial-distribution-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (2.0,0) node[lab, right] {$k$};
\draw[->] (0,0) -- (0,2.4) node[lab, above] {$\Pr(X=k)$};
\path[bar] (0.275,0) rectangle (0.725,1.750);
\node[tick, below] at (0.500,0) {$0$};
\path[hl cell] (1.075,0) rectangle (1.525,0.750);
\node[tick, below] at (1.300,0) {$1$};
\node[tick, above] at (0.5,1.75) {$1-p$};
\node[tick, above] at (1.3,0.75) {$p$};
\end{tikzpicture}
\end{center}
```

A Bernoulli distribution with $p=0.3$: the value $1$ (success) has probability $p$ and $0$ has $1-p$

:::

::: {#def-binomial-distribution .definition name="Binomial distribution"}

$X\sim\mathrm{Bin}(n,p)$ is the number of successes in $n$ independent Bernoulli trials, each with success probability $p$:
$$\Pr(X=k) = \binom{n}{k}p^k(1-p)^{n-k}, \qquad k=0,1,\dots,n.$$

:::

::: {#fig-binomial-distribution-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1]
\draw[->] (-0.4,0) -- (8.3,0) node[lab, right] {$k$};
\draw[->] (-0.3,0) -- (-0.3,2.4) node[lab, above] {$\Pr(X=k)$};
\fill[primaryStrong] (-0.225,0) rectangle (0.225,0.226);
\node[tick, below] at (0.000,0) {$0$};
\fill[primaryStrong] (0.525,0) rectangle (0.975,0.968);
\node[tick, below] at (0.750,0) {$1$};
\fill[primaryStrong] (1.275,0) rectangle (1.725,1.868);
\node[tick, below] at (1.500,0) {$2$};
\fill[primaryStrong] (2.025,0) rectangle (2.475,2.135);
\node[tick, below] at (2.250,0) {$3$};
\fill[primaryStrong] (2.775,0) rectangle (3.225,1.601);
\node[tick, below] at (3.000,0) {$4$};
\fill[primaryStrong] (3.525,0) rectangle (3.975,0.823);
\node[tick, below] at (3.750,0) {$5$};
\fill[primaryStrong] (4.275,0) rectangle (4.725,0.294);
\node[tick, below] at (4.500,0) {$6$};
\fill[primaryStrong] (5.025,0) rectangle (5.475,0.072);
\node[tick, below] at (5.250,0) {$7$};
\fill[primaryStrong] (5.775,0) rectangle (6.225,0.012);
\node[tick, below] at (6.000,0) {$8$};
\fill[primaryStrong] (6.525,0) rectangle (6.975,0.001);
\node[tick, below] at (6.750,0) {$9$};
\fill[primaryStrong] (7.275,0) rectangle (7.725,0.000);
\node[tick, below] at (7.500,0) {$10$};
\draw (-0.24,0.800) -- (-0.36,0.800) node[tick, left] {$0.1$};
\draw (-0.24,1.600) -- (-0.36,1.600) node[tick, left] {$0.2$};
\end{tikzpicture}
\end{center}
```

The probabilities of $\operatorname{Bin}(10,0.3)$. They peak near the mean $np=3$; the largest is $\Pr(X=3)\approx0.27$.

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
