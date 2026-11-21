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

::: {#fig-coupon-collector-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (4.8,0) node[lab, right] {throws};
\draw[->] (0,0) -- (0,3.0) node[lab, above] {distinct faces};
\draw[emph] (0.00,0.00) -- (0.30,0.00) -- (0.30,0.45);
\node[hl dot] at (0.30,0.45) {};
\draw[emph] (0.30,0.45) -- (0.60,0.45) -- (0.60,0.90);
\node[hl dot] at (0.60,0.90) {};
\draw[emph] (0.60,0.90) -- (0.90,0.90) -- (0.90,1.35);
\node[hl dot] at (0.90,1.35) {};
\draw[emph] (0.90,1.35) -- (1.20,1.35) -- (1.20,1.35);
\draw[emph] (1.20,1.35) -- (1.50,1.35) -- (1.50,1.35);
\draw[emph] (1.50,1.35) -- (1.80,1.35) -- (1.80,1.80);
\node[hl dot] at (1.80,1.80) {};
\draw[emph] (1.80,1.80) -- (2.10,1.80) -- (2.10,2.25);
\node[hl dot] at (2.10,2.25) {};
\draw[emph] (2.10,2.25) -- (2.40,2.25) -- (2.40,2.25);
\draw[emph] (2.40,2.25) -- (2.70,2.25) -- (2.70,2.25);
\draw[emph] (2.70,2.25) -- (3.00,2.25) -- (3.00,2.25);
\draw[emph] (3.00,2.25) -- (3.30,2.25) -- (3.30,2.25);
\draw[emph] (3.30,2.25) -- (3.60,2.25) -- (3.60,2.25);
\draw[emph] (3.60,2.25) -- (3.90,2.25) -- (3.90,2.25);
\draw[emph] (3.90,2.25) -- (4.20,2.25) -- (4.20,2.70);
\node[hl dot] at (4.20,2.70) {};
\draw (0,0.45) -- (-0.08,0.45) node[tick, left] {$1$};
\draw (0,0.9) -- (-0.08,0.9) node[tick, left] {$2$};
\draw (0,1.35) -- (-0.08,1.35) node[tick, left] {$3$};
\draw (0,1.8) -- (-0.08,1.8) node[tick, left] {$4$};
\draw (0,2.25) -- (-0.08,2.25) node[tick, left] {$5$};
\draw (0,2.7) -- (-0.08,2.7) node[tick, left] {$6$};
\draw (4.2,0) -- (4.2,-0.08) node[tick, below] {$14$};
\end{tikzpicture}
\end{center}
```

One run of collecting all faces of a die, which took 14 throws. New faces (dots) come fast at first and slowly at the end; the expected total is $6H_6=14.7$

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
