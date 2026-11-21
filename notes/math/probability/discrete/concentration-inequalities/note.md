---
title: "Concentration Inequalities and the Law of Large Numbers"
sources: [cs70-17.1, cs70-17.2, cs70-17.3, cs70-17.4]
requires: [math/probability/discrete/indicator-variables, math/probability/discrete/binomial-distribution]
aliases: [math/probability/concentration-inequalities]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 17 (cs70-17.1 to cs70-17.4), in our own wording; proofs written out in steps. Chebyshev's inequality itself is in expectation-and-variance. -->

## Markov's inequality

::: {#thm-markov-inequality .theorem name="Markov's inequality"}

If $X\ge0$ (that is, $X(u)\ge0$ for every outcome $u$) and $E[X]$ is finite, then for every $c>0$,
$$\Pr(X\ge c)\le\frac{E[X]}{c}.$$

:::

::: {.proof}

1. Let $I$ indicate the event $X\ge c$ (@def-indicator-variable).

2. At every outcome, $X\ge c\,I$. Where $X\ge c$ this reads $X\ge c$; elsewhere it reads $X\ge0$, which holds because $X$ is non-negative.

3. Expectation preserves $\ge$ between random variables, because $E[X]-E[cI]=\sum_u\bigl(X(u)-cI(u)\bigr)\Pr(u)$ is a sum of non-negative terms. So $E[X]\ge c\,E[I]=c\Pr(X\ge c)$ by @prp-expectation-of-indicator.

4. Divide by $c>0$.

:::

::: {#fig-concentration-inequalities-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.6cm,y=10cm]
\draw[bar] (-0.32,0) rectangle (0.32,0.0282); \node[tick, below] at (0,0) {$0$};
\draw[bar] (0.6799999999999999,0) rectangle (1.32,0.1211); \node[tick, below] at (1,0) {$1$};
\draw[bar] (1.68,0) rectangle (2.32,0.2335); \node[tick, below] at (2,0) {$2$};
\draw[bar] (2.68,0) rectangle (3.32,0.2668); \node[tick, below] at (3,0) {$3$};
\draw[bar] (3.68,0) rectangle (4.32,0.2001); \node[tick, below] at (4,0) {$4$};
\draw[bar] (4.68,0) rectangle (5.32,0.1029); \node[tick, below] at (5,0) {$5$};
\draw[hl cell] (5.68,0) rectangle (6.32,0.0368); \node[tick, below] at (6,0) {$6$};
\draw[hl cell] (6.68,0) rectangle (7.32,0.0090); \node[tick, below] at (7,0) {$7$};
\draw[hl cell] (7.68,0) rectangle (8.32,0.0014); \node[tick, below] at (8,0) {$8$};
\draw[hl cell] (8.68,0) rectangle (9.32,0.0001); \node[tick, below] at (9,0) {$9$};
\draw[hl cell] (9.68,0) rectangle (10.32,0.0000); \node[tick, below] at (10,0) {$10$};
\draw[muted] (-0.6,0) -- (10.6,0);
\draw[accent, dashed] (3,0) -- (3,0.3) node[lab, above] {$E[X]=3$};
\node[lab, accent] at (8.3,0.15) {$\Pr(X\ge6)\approx0.047\le\frac36$};
\end{tikzpicture}
\end{center}
```

$X\sim\mathrm{Bin}(10,0.3)$ has mean $3$. Markov's inequality bounds the tail $\Pr(X\ge6)$ (shaded) by $\frac36$; the true value is about $0.047$, so the bound is valid but crude.

:::

::: {#thm-generalised-markov .theorem name="Generalised Markov inequality"}

For any random variable $Y$ and constants $c>0$ and $r>0$ with $E\bigl[|Y|^r\bigr]$ finite,
$$\Pr(|Y|\ge c)\le\frac{E\bigl[|Y|^r\bigr]}{c^r}.$$

:::

::: {.proof}

1. Since $r>0$, the function $t\mapsto t^r$ is increasing for $t\ge0$, so $|Y|\ge c$ exactly when $|Y|^r\ge c^r$.

2. Apply @thm-markov-inequality to the non-negative random variable $|Y|^r$ with the constant $c^r$.

:::

::: {#rmk-concentration-inequalities-1 .remark name="Chebyshev from Markov"}

With $Y=X-E[X]$ and $r=2$, the generalised inequality is Chebyshev's inequality (@thm-chebyshev-s-inequality), since $E[(X-E[X])^2]=\mathrm{Var}(X)$. Markov needs only the mean but applies only to non-negative variables; Chebyshev uses the variance as well and usually gives a much better bound.

:::

## Estimating a probability

::: {#prp-sample-mean .proposition name="Mean and variance of a sample mean"}

Let $X_1,\dots,X_n$ be independent with the same mean $\mu$ and the same variance $\sigma^2$, and let $\hat\mu=\frac1n(X_1+\cdots+X_n)$. Then
$$E[\hat\mu]=\mu,\qquad \mathrm{Var}(\hat\mu)=\frac{\sigma^2}n.$$

:::

::: {.proof}

1. By linearity, $E[\hat\mu]=\frac1n\cdot n\mu=\mu$.

2. By @thm-variance-of-an-independent-sum, applied $n-1$ times, $\mathrm{Var}(X_1+\cdots+X_n)=n\sigma^2$. (Each partial sum is a function of $X_1,\dots,X_{k}$ and so independent of $X_{k+1}$.)

3. For a constant $a$, $\mathrm{Var}(aX)=E[a^2X^2]-a^2E[X]^2=a^2\mathrm{Var}(X)$. With $a=\frac1n$, $\mathrm{Var}(\hat\mu)=\frac{n\sigma^2}{n^2}=\frac{\sigma^2}n$.

:::

::: {#fig-concentration-inequalities-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (6.4,0) node[lab, right] {$\overline X_n$};
\draw[emph, domain=0.2:6, samples=120, smooth, variable=\x] plot ({\x}, {0.4*exp(-((\x/6-0.5)^2)/(2*0.1581^2))/(0.1581*sqrt(2*pi))});
\draw[hl, domain=0.2:6, samples=120, smooth, variable=\x] plot ({\x}, {0.4*exp(-((\x/6-0.5)^2)/(2*0.0791^2))/(0.0791*sqrt(2*pi))});
\draw (3,0) -- (3,-0.08) node[tick, below] {$\tfrac12$};
\draw (0,0) -- (0,-0.08) node[tick, below] {$0$};
\draw (6,0) -- (6,-0.08) node[tick, below] {$1$};
\node[tick] at (4.6,0.75) {$n=10$};
\node[tick] at (3.7,2.0) {$n=40$};
\end{tikzpicture}
\end{center}
```

The sample mean of $n$ fair coin tosses has standard deviation $\tfrac1{2\sqrt n}$: quadrupling $n$ halves the spread around $\tfrac12$

:::

::: {#thm-coin-bias-sample-size .theorem name="How many tosses estimate a coin's bias"}

A coin shows heads with unknown probability $p$. Toss it $n$ times and let $\hat p$ be the fraction of heads. For $0<\varepsilon,\delta<1$, if
$$n\ge\frac1{4\varepsilon^2\delta},$$
then $\Pr(|\hat p-p|\ge\varepsilon)\le\delta$.

:::

::: {.proof}

1. Let $X_i$ indicate "toss $i$ is heads". The $X_i$ are independent with mean $p$ and variance $p(1-p)$ (@prp-standard-distributions-1-2 with $n=1$), and $\hat p$ is their sample mean.

2. By @prp-sample-mean and @thm-chebyshev-s-inequality,
   $$\Pr(|\hat p-p|\ge\varepsilon)\le\frac{\mathrm{Var}(\hat p)}{\varepsilon^2}=\frac{p(1-p)}{n\varepsilon^2}.$$

3. $p(1-p)\le\frac14$ for every $p$, because $\frac14-p(1-p)=\bigl(p-\frac12\bigr)^2\ge0$.

4. So the probability is at most $\frac1{4n\varepsilon^2}$, which is at most $\delta$ when $n\ge\frac1{4\varepsilon^2\delta}$.

:::

::: {#rmk-concentration-inequalities-2 .remark name="Estimating any expectation"}

The same argument estimates the mean $\mu$ of any distribution from independent samples. Asking for a *relative* error, $\Pr(|\hat\mu-\mu|\ge\varepsilon\mu)\le\delta$, it is enough that $n\ge\frac{\sigma^2}{\mu^2}\cdot\frac1{\varepsilon^2\delta}$. In practice one uses a lower bound for $\mu$ and an upper bound for $\sigma^2$. A very spread-out distribution, such as personal wealth, has a huge $\sigma^2/\mu^2$ and needs a huge sample.

:::

## The law of large numbers

::: {#thm-law-of-large-numbers .theorem name="Law of large numbers"}

Let $X_1,X_2,\dots$ be i.i.d. random variables with finite mean $\mu$ and finite variance $\sigma^2$, and let $S_n=X_1+\cdots+X_n$. Then for every $\varepsilon>0$,
$$\Pr\Bigl(\Bigl|\frac{S_n}n-\mu\Bigr|<\varepsilon\Bigr)\to1\qquad\text{as } n\to\infty.$$

:::

::: {.proof}

1. By @prp-sample-mean, $\frac{S_n}n$ has mean $\mu$ and variance $\frac{\sigma^2}n$.

2. By @thm-chebyshev-s-inequality, $\Pr\bigl(|\frac{S_n}n-\mu|\ge\varepsilon\bigr)\le\frac{\sigma^2}{n\varepsilon^2}$, which tends to $0$ as $n\to\infty$.

3. The event in the theorem is the complement, so its probability is at least $1-\frac{\sigma^2}{n\varepsilon^2}$ and tends to $1$ (@prp-complement).

:::

::: {#fig-concentration-inequalities-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (8.4,0) node[lab, right] {$n$};
\draw[->] (0,0) -- (0,2.6) node[lab, above] {$\overline X_n$};
\draw[emph] (0.02,2.40) -- (0.10,0.96) -- (0.18,0.80) -- (0.26,1.11) -- (0.34,0.99) -- (0.42,0.91) -- (0.50,1.06) -- (0.58,1.24) -- (0.66,1.16) -- (0.74,1.17) -- (0.82,1.11) -- (0.90,1.17) -- (0.98,1.18) -- (1.06,1.18) -- (1.14,1.22) -- (1.22,1.22) -- (1.30,1.22) -- (1.38,1.25) -- (1.46,1.28) -- (1.54,1.28) -- (1.62,1.30) -- (1.70,1.30) -- (1.78,1.29) -- (1.86,1.29) -- (1.94,1.34) -- (2.02,1.33) -- (2.10,1.33) -- (2.18,1.32) -- (2.26,1.32) -- (2.34,1.29) -- (2.42,1.31) -- (2.50,1.31) -- (2.58,1.30) -- (2.66,1.30) -- (2.74,1.28) -- (2.82,1.31) -- (2.90,1.32) -- (2.98,1.32) -- (3.06,1.30) -- (3.14,1.30) -- (3.22,1.30) -- (3.30,1.29) -- (3.38,1.26) -- (3.46,1.25) -- (3.54,1.23) -- (3.62,1.21) -- (3.70,1.21) -- (3.78,1.18) -- (3.86,1.18) -- (3.94,1.18) -- (4.02,1.18) -- (4.10,1.18) -- (4.18,1.19) -- (4.26,1.19) -- (4.34,1.19) -- (4.42,1.18) -- (4.50,1.19) -- (4.58,1.18) -- (4.66,1.19) -- (4.74,1.21) -- (4.82,1.20) -- (4.90,1.21) -- (4.98,1.21) -- (5.06,1.22) -- (5.14,1.23) -- (5.22,1.23) -- (5.30,1.21) -- (5.38,1.23) -- (5.46,1.24) -- (5.54,1.23) -- (5.62,1.22) -- (5.70,1.22) -- (5.78,1.22) -- (5.86,1.20) -- (5.94,1.20) -- (6.02,1.20) -- (6.10,1.18) -- (6.18,1.17) -- (6.26,1.18) -- (6.34,1.18) -- (6.42,1.19) -- (6.50,1.19) -- (6.58,1.17) -- (6.66,1.18) -- (6.74,1.18) -- (6.82,1.17) -- (6.90,1.17) -- (6.98,1.16) -- (7.06,1.15) -- (7.14,1.15) -- (7.22,1.14) -- (7.30,1.14) -- (7.38,1.15) -- (7.46,1.15) -- (7.54,1.15) -- (7.62,1.16) -- (7.70,1.17) -- (7.78,1.17) -- (7.86,1.17) -- (7.94,1.17);
\draw[hl] (0.02,0.00) -- (0.10,0.00) -- (0.18,0.27) -- (0.26,0.74) -- (0.34,0.85) -- (0.42,0.91) -- (0.50,1.06) -- (0.58,1.08) -- (0.66,1.02) -- (0.74,0.97) -- (0.82,1.05) -- (0.90,1.07) -- (0.98,1.03) -- (1.06,1.09) -- (1.14,1.09) -- (1.22,1.10) -- (1.30,1.11) -- (1.38,1.15) -- (1.46,1.12) -- (1.54,1.09) -- (1.62,1.07) -- (1.70,1.02) -- (1.78,1.00) -- (1.86,0.98) -- (1.94,1.04) -- (2.02,1.05) -- (2.10,1.03) -- (2.18,1.01) -- (2.26,0.98) -- (2.34,0.98) -- (2.42,1.03) -- (2.50,1.04) -- (2.58,1.00) -- (2.66,0.99) -- (2.74,1.00) -- (2.82,1.02) -- (2.90,1.03) -- (2.98,1.03) -- (3.06,1.04) -- (3.14,1.07) -- (3.22,1.06) -- (3.30,1.06) -- (3.38,1.07) -- (3.46,1.05) -- (3.54,1.04) -- (3.62,1.06) -- (3.70,1.08) -- (3.78,1.08) -- (3.86,1.07) -- (3.94,1.07) -- (4.02,1.06) -- (4.10,1.05) -- (4.18,1.06) -- (4.26,1.05) -- (4.34,1.06) -- (4.42,1.08) -- (4.50,1.07) -- (4.58,1.08) -- (4.66,1.08) -- (4.74,1.08) -- (4.82,1.09) -- (4.90,1.08) -- (4.98,1.09) -- (5.06,1.09) -- (5.14,1.09) -- (5.22,1.10) -- (5.30,1.10) -- (5.38,1.12) -- (5.46,1.11) -- (5.54,1.10) -- (5.62,1.11) -- (5.70,1.12) -- (5.78,1.14) -- (5.86,1.12) -- (5.94,1.12) -- (6.02,1.12) -- (6.10,1.10) -- (6.18,1.10) -- (6.26,1.10) -- (6.34,1.10) -- (6.42,1.10) -- (6.50,1.10) -- (6.58,1.09) -- (6.66,1.09) -- (6.74,1.08) -- (6.82,1.06) -- (6.90,1.06) -- (6.98,1.07) -- (7.06,1.08) -- (7.14,1.09) -- (7.22,1.09) -- (7.30,1.09) -- (7.38,1.11) -- (7.46,1.11) -- (7.54,1.11) -- (7.62,1.11) -- (7.70,1.11) -- (7.78,1.12) -- (7.86,1.11) -- (7.94,1.11);
\draw[faint, dashed] (0,1.2) -- (8.1,1.2);
\draw (0,1.2) -- (-0.08,1.2) node[tick, left] {$\tfrac12$};
\draw (0,2.4) -- (-0.08,2.4) node[tick, left] {$1$};
\draw (8,0) -- (8,-0.08) node[tick, below] {$400$};
\end{tikzpicture}
\end{center}
```

Running proportions of heads in two sequences of $400$ fair tosses. Both settle near $\tfrac12$, as the weak law of large numbers predicts

:::

::: {#rmk-concentration-inequalities-3 .remark name="What it says"}

Averaging many independent observations smooths out their fluctuations: the probability of any fixed deviation of the average from the mean, however small, tends to $0$. The theorem also holds without a finite variance, but that proof needs more advanced tools.

:::
