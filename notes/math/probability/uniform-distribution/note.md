---
title: "Uniform Distribution"
sources: [fit1058-cn-10.7]
requires: [math/probability/expectation-and-variance]
status: draft
---

<!-- Split from math/probability/standard-distributions on 2026-11-16 (SPEC §2.6); block ids unchanged. -->
<!-- Migrated from 1058note notes/chapters/09-probability.tex: Uniform distribution. -->

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
