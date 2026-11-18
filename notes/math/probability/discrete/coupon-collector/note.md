---
title: "The coupon collector's problem"
sources: [fit1058-cn-10.11, cs70-19.1.2]
requires: [math/probability/discrete/geometric-distribution]
aliases: [math/probability/coupon-collector]   # old ids (moved)
status: draft
---

<!-- Migrated from 1058note notes/chapters/09-probability.tex: The coupon collector's problem. -->

::: {#thm-coupon-collector .theorem name="Coupon collector"}

There are $n$ types of coupon, and each draw gives a type chosen uniformly at random, independently. Let $T$ be the number of draws needed to collect all $n$ types. Then
$$E[T] = n H_n = n\left(1+\frac12+\cdots+\frac1n\right).$$

:::

::: {.proof}

Let $T_i$ be the number of draws taken to go from $i-1$ to $i$ distinct types, so $T=\sum_{i=1}^n T_i$. When $i-1$ types have been collected, each draw is new with probability $\frac{n-i+1}{n}$, so $T_i$ is geometric with this $p$, and $E[T_i]=\frac{n}{n-i+1}$. By linearity,
$$E[T] = \sum_{i=1}^n \frac{n}{n-i+1} = n\sum_{j=1}^n\frac1j = nH_n,$$
substituting $j=n-i+1$.

:::

::: {#exm-coupon-collector-1 .example}

To see all six faces of a die takes on average $6H_6=6\bigl(1+\frac12+\frac13+\frac14+\frac15+\frac16\bigr)=14.7$ throws.

:::

::: {#fig-coupon-collector-1}

```{=latex}
\begin{tikzpicture}[x=0.9cm, y=0.5cm]
  \foreach \y in {2,4,6} {\draw[rule] (0.4,\y) -- (6.6,\y); \node[left, tick] at (0.4,\y) {$\y$};}
  \draw (0.4,0) -- (6.6,0);
  \foreach \k/\w/\t in {1/1/{\tfrac66}, 2/1.2/{\tfrac65}, 3/1.5/{\tfrac64}, 4/2/{\tfrac63}, 5/3/{\tfrac62}, 6/6/{\tfrac61}} {
    \fill[primaryStrong] (\k-0.32,0) rectangle (\k+0.32,\w);
    \node[above, tick] at (\k,\w) {$\t$};
    \node[below, tick] at (\k,0) {$\k$};
  }
  \node[tick, text=muted] at (3.5,-1.5) {new face number};
\end{tikzpicture}
```

Expected throws to see each new face of a die: $1, \tfrac65, \tfrac64, \tfrac63, \tfrac62, 6$. The last face alone takes $6$ throws on average, and the total is $14.7$

:::

::: {#rmk-coupon-collector-1 .remark name="The last few are expensive"}

Since $H_n\approx\ln n$ (@sec-math-calculus-single-variable-limits-sums-and-series), collecting all $n$ types takes about $n\ln n$ draws, not about $n$. The early types come quickly; the last one alone takes $n$ draws on average.

:::
