---
title: "Uniform Distribution"
sources: [fit1058-cn-10.7]
requires: [math/probability/random-variables/expectation-and-variance]
aliases: [math/probability/uniform-distribution, math/probability/discrete/uniform-distribution]   # old ids (moved)
status: draft
---

<!-- Split from math/probability/standard-distributions on 2026-11-16 (SPEC §2.6); block ids unchanged. -->
<!-- Migrated from 1058note notes/chapters/09-probability.tex: Uniform distribution. -->

::: {#def-discrete-uniform-distribution .definition name="Discrete uniform distribution"}

$X\sim\mathrm{Unif}(a,b)$ means $X$ takes each integer value in $[a,b]$ with the same probability $1/(b-a+1)$.

:::

::: {#fig-uniform-distribution-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (5.4,0) node[lab, right] {$k$};
\draw[->] (0.15,0) -- (0.15,2.0) node[lab, above] {$\Pr(X=k)$};
\fill[primaryStrong] (0.525,0) rectangle (0.975,1.333);
\node[tick, below] at (0.750,0) {$1$};
\fill[primaryStrong] (1.275,0) rectangle (1.725,1.333);
\node[tick, below] at (1.500,0) {$2$};
\fill[primaryStrong] (2.025,0) rectangle (2.475,1.333);
\node[tick, below] at (2.250,0) {$3$};
\fill[primaryStrong] (2.775,0) rectangle (3.225,1.333);
\node[tick, below] at (3.000,0) {$4$};
\fill[primaryStrong] (3.525,0) rectangle (3.975,1.333);
\node[tick, below] at (3.750,0) {$5$};
\fill[primaryStrong] (4.275,0) rectangle (4.725,1.333);
\node[tick, below] at (4.500,0) {$6$};
\draw (0.21,1.333) -- (0.09,1.333) node[tick, left] {$\frac16$};
\end{tikzpicture}
\end{center}
```

A fair die roll is $\operatorname{Unif}(1,6)$: each of the $b-a+1=6$ values has probability $\frac16$.

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

::: {#fig-uniform-distribution-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (4.6,0) node[lab, right] {$x$};
\draw[->] (0,0) -- (0,2.4) node[lab, above] {$F(x)$};
\draw[emph] (0.6,0.333) -- (1.2,0.333);
\node[dot] at (0.6,0.333) {};
\node[hollow dot] at (0.6,0.000) {};
\draw[emph] (1.2,0.667) -- (1.80,0.667);
\node[dot] at (1.2,0.667) {};
\node[hollow dot] at (1.2,0.333) {};
\draw[emph] (1.80,1.000) -- (2.4,1.000);
\node[dot] at (1.80,1.000) {};
\node[hollow dot] at (1.80,0.667) {};
\draw[emph] (2.4,1.333) -- (3.0,1.333);
\node[dot] at (2.4,1.333) {};
\node[hollow dot] at (2.4,1.000) {};
\draw[emph] (3.0,1.667) -- (3.6,1.667);
\node[dot] at (3.0,1.667) {};
\node[hollow dot] at (3.0,1.333) {};
\draw[emph] (3.60,2.000) -- (4.20,2.000);
\node[dot] at (3.60,2.000) {};
\node[hollow dot] at (3.60,1.667) {};
\draw[emph] (0,0) -- (0.6,0);
\draw (0.6,0) -- (0.6,-0.08) node[tick, below] {$1$};
\draw (1.2,0) -- (1.2,-0.08) node[tick, below] {$2$};
\draw (1.80,0) -- (1.80,-0.08) node[tick, below] {$3$};
\draw (2.4,0) -- (2.4,-0.08) node[tick, below] {$4$};
\draw (3.0,0) -- (3.0,-0.08) node[tick, below] {$5$};
\draw (3.60,0) -- (3.60,-0.08) node[tick, below] {$6$};
\draw (0,2) -- (-0.08,2) node[tick, left] {$1$};
\end{tikzpicture}
\end{center}
```

The distribution function of a fair die is a staircase with six equal steps of $\tfrac16$, one at each value

:::
