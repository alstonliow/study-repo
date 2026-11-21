---
title: "Poisson Distribution"
sources: [fit1058-cn-10.9, cs70-19.2.1, cs70-19.2.2]
requires: [math/probability/discrete/binomial-distribution]
aliases: [math/probability/poisson-distribution]   # old ids (moved)
status: draft
---

<!-- Split from math/probability/standard-distributions on 2026-11-16 (SPEC §2.6); block ids unchanged. -->
<!-- Migrated from 1058note notes/chapters/09-probability.tex: Poisson distribution. -->
<!-- Proof written out in steps; it follows CS70 Note 19 (cs70-19.2.1), in our own wording. -->

::: {#def-poisson-distribution .definition name="Poisson distribution"}

$X\sim\mathrm{Poisson}(\mu)$, for a parameter $\mu>0$, means
$$\Pr(X=k) = \frac{e^{-\mu}\mu^k}{k!}, \qquad k=0,1,2,\dots$$

:::

::: {#fig-poisson-distribution-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (7.0,0) node[lab, right] {$k$};
\draw[->] (0,0) -- (0,2.4) node[lab, above] {$\Pr(X=k)$};
\path[bar] (0.11,0) rectangle (0.29,2.023);
\path[bar] (0.66,0) rectangle (0.84,2.023);
\path[bar] (1.21,0) rectangle (1.39,1.012);
\path[bar] (1.76,0) rectangle (1.94,0.337);
\path[bar] (2.31,0) rectangle (2.49,0.084);
\path[bar] (2.86,0) rectangle (3.04,0.017);
\path[bar] (3.41,0) rectangle (3.59,0.003);
\path[bar] (3.96,0) rectangle (4.14,0.000);
\path[bar] (4.51,0) rectangle (4.69,0.000);
\path[bar] (5.06,0) rectangle (5.24,0.000);
\path[bar] (5.61,0) rectangle (5.79,0.000);
\path[bar] (6.16,0) rectangle (6.34,0.000);
\path[hl cell] (0.31,0) rectangle (0.49,0.101);
\path[hl cell] (0.86,0) rectangle (1.04,0.403);
\path[hl cell] (1.41,0) rectangle (1.59,0.806);
\path[hl cell] (1.96,0) rectangle (2.14,1.075);
\path[hl cell] (2.51,0) rectangle (2.69,1.075);
\path[hl cell] (3.06,0) rectangle (3.24,0.860);
\path[hl cell] (3.61,0) rectangle (3.79,0.573);
\path[hl cell] (4.16,0) rectangle (4.34,0.327);
\path[hl cell] (4.71,0) rectangle (4.89,0.164);
\path[hl cell] (5.26,0) rectangle (5.44,0.073);
\path[hl cell] (5.81,0) rectangle (5.99,0.029);
\path[hl cell] (6.36,0) rectangle (6.54,0.011);
\draw (0.3,0) -- (0.3,-0.08) node[tick, below] {$0$};
\draw (1.40,0) -- (1.40,-0.08) node[tick, below] {$2$};
\draw (2.5,0) -- (2.5,-0.08) node[tick, below] {$4$};
\draw (3.6,0) -- (3.6,-0.08) node[tick, below] {$6$};
\draw (4.7,0) -- (4.7,-0.08) node[tick, below] {$8$};
\draw (5.8,0) -- (5.8,-0.08) node[tick, below] {$10$};
\node[tick, right] at (0.8,2.05) {$\mu=1$};
\node[tick, right] at (2.6,1.25) {$\mu=4$};
\end{tikzpicture}
\end{center}
```

Poisson distributions with means $1$ (dark) and $4$ (light). As $\mu$ grows the mass moves right and spreads, since the variance is also $\mu$

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

::: {#fig-poisson-distribution-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-0.4,0) -- (6.6,0) node[lab, right] {$k$};
\draw[->] (-0.3,0) -- (-0.3,2.6) node[lab, above] {probability};
\fill[primaryStrong] (-0.225,0) rectangle (0.225,1.083);
\node[tick, below] at (0.000,0) {$0$};
\fill[primaryStrong] (0.525,0) rectangle (0.975,2.165);
\node[tick, below] at (0.750,0) {$1$};
\fill[primaryStrong] (1.275,0) rectangle (1.725,2.165);
\node[tick, below] at (1.500,0) {$2$};
\fill[primaryStrong] (2.025,0) rectangle (2.475,1.444);
\node[tick, below] at (2.250,0) {$3$};
\fill[primaryStrong] (2.775,0) rectangle (3.225,0.722);
\node[tick, below] at (3.000,0) {$4$};
\fill[primaryStrong] (3.525,0) rectangle (3.975,0.289);
\node[tick, below] at (3.750,0) {$5$};
\fill[primaryStrong] (4.275,0) rectangle (4.725,0.096);
\node[tick, below] at (4.500,0) {$6$};
\fill[primaryStrong] (5.025,0) rectangle (5.475,0.027);
\node[tick, below] at (5.250,0) {$7$};
\fill[primaryStrong] (5.775,0) rectangle (6.225,0.007);
\node[tick, below] at (6.000,0) {$8$};
\node[hl dot] at (0.000,0.973) {};
\node[hl dot] at (0.750,2.161) {};
\node[hl dot] at (1.500,2.281) {};
\node[hl dot] at (2.250,1.521) {};
\node[hl dot] at (3.000,0.718) {};
\node[hl dot] at (3.750,0.255) {};
\node[hl dot] at (4.500,0.071) {};
\node[hl dot] at (5.250,0.016) {};
\node[hl dot] at (6.000,0.003) {};
\draw (-0.24,0.800) -- (-0.36,0.800) node[tick, left] {$0.1$};
\draw (-0.24,1.600) -- (-0.36,1.600) node[tick, left] {$0.2$};
\fill[primaryStrong] (4.4,2.3) rectangle (4.6,2.5); \node[lab, right] at (4.6,2.4) {$\operatorname{Poisson}(2)$};
\node[hl dot] at (4.5,2.0) {}; \node[lab, right] at (4.6,2.0) {$\operatorname{Bin}(20,0.1)$};
\end{tikzpicture}
\end{center}
```

$\operatorname{Bin}(20,0.1)$ (dots) against its Poisson limit with the same mean $\mu=np=2$ (bars). Already for $n=20$ the two are close (@thm-poisson-as-a-limit-of).

:::

::: {#rmk-standard-distributions-3 .remark name="Approximating the binomial"}

So $\mathrm{Bin}(n,p)$ with $n$ large, $p$ small and $np$ moderate is well approximated by $\mathrm{Poisson}(np)$: think of many trials, each with a small chance of a rare event.

:::

::: {#thm-sum-of-poissons .theorem name="Sum of independent Poisson variables"}

If $X\sim\mathrm{Poisson}(\lambda)$ and $Y\sim\mathrm{Poisson}(\mu)$ are independent, then $X+Y\sim\mathrm{Poisson}(\lambda+\mu)$.

:::

::: {.proof}

1. Fix $k\ge0$. Both variables take values in $\{0,1,2,\dots\}$, so $X+Y=k$ is the disjoint union of the events $X=j,\ Y=k-j$ for $j=0,\dots,k$.

2. By independence (@def-independent-random-variables),
   $$\Pr(X+Y=k)=\sum_{j=0}^{k}\frac{e^{-\lambda}\lambda^j}{j!}\cdot\frac{e^{-\mu}\mu^{k-j}}{(k-j)!}=\frac{e^{-(\lambda+\mu)}}{k!}\sum_{j=0}^{k}\binom kj\lambda^j\mu^{k-j}.$$

3. By the binomial theorem (@thm-binomial-theorem) the sum is $(\lambda+\mu)^k$, so $\Pr(X+Y=k)=\dfrac{e^{-(\lambda+\mu)}(\lambda+\mu)^k}{k!}$.

:::

::: {#rmk-poisson-distribution-sum .remark name="Many summands"}

By induction, a sum of $n$ independent Poisson variables with parameters $\lambda_1,\dots,\lambda_n$ is $\mathrm{Poisson}(\lambda_1+\cdots+\lambda_n)$. For example, calls arriving independently at two exchanges at average rates $2$ and $3$ per minute add up to a Poisson stream at rate $5$.

:::
