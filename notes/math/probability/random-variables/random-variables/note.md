---
title: "Random Variables and Distributions"
sources: [fit1058-cn-10.1, fit1058-cn-10.2, cs70-15.3]
requires: [math/probability/foundations/conditional-probability]
aliases: [math/probability/random-variables, math/probability/discrete/random-variables]   # old ids (moved)
status: draft
---

<!-- Migrated from 1058note notes/chapters/09-probability.tex: Random variables; Probability distributions. -->

## Random variables

::: {#def-random-variable .definition name="Random variable"}

A *random variable* on a sample space $U$ is a function $X:U\to\mathbb{R}$.

:::

::: {#fig-random-variables-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[set] at (0,0) {};
\node[lab] at (0,1.9) {$S$};
\node[lab] (o0) at (0,1.05) {HH};
\node[lab] (o1) at (0,0.35) {HT};
\node[lab] (o2) at (0,-0.35) {TH};
\node[lab] (o3) at (0,-1.05) {TT};
\draw[->] (2.5,-1.6) -- (2.5,1.6) node[lab, above] {$\mathbb R$};
\node[dot] (v0) at (2.5,-1) {};
\node[tick, right] at (v0.east) {$0$};
\node[dot] (v1) at (2.5,0) {};
\node[tick, right] at (v1.east) {$1$};
\node[dot] (v2) at (2.5,1) {};
\node[tick, right] at (v2.east) {$2$};
\draw[map] (o0.east) -- (v2);
\draw[map] (o1.east) -- (v1);
\draw[map] (o2.east) -- (v1);
\draw[map] (o3.east) -- (v0);
\node[lab] at (1.3,1.6) {$X$};
\end{tikzpicture}
\end{center}
```

A random variable is a function on the sample space: $X$ sends each outcome of two coin tosses to its number of heads

:::

::: {#exm-random-variables-1 .example}

Throw two dice, so $U=\{1,\dots,6\}^2$. The total $Z(d_1,d_2)=d_1+d_2$ is a random variable with values in $\{2,\dots,12\}$; the event $Z=9$ is $\{(3,6),(4,5),(5,4),(6,3)\}$.

:::

::: {#rmk-random-variables-1 .remark name="Notation"}

$X=k$ is shorthand for the event $\{u\in U : X(u)=k\}$, so $\Pr(X=k)$ means the probability of that event. Similarly for $X\le k$, etc.

:::

::: {#def-independent-random-variables .definition name="Independent random variables"}

$X,Y$ are *independent* if for all $r,s$,
$$\Pr(X=r \text{ and } Y=s) = \Pr(X=r)\cdot\Pr(Y=s).$$

:::

::: {#rmk-random-variables-2 .remark name="Compared with independent events"}

This says that the events $X=r$ and $Y=s$ are independent (@sec-math-probability-foundations-conditional-probability) for *every* pair of values $r,s$. The numbers shown on two separate fair dice are independent random variables.

:::

## Probability distributions

::: {#def-probability-distribution .definition name="Probability distribution"}

The *probability distribution* of $X$ is the function $p(k) = \Pr(X=k)$, over the possible values $k$ of $X$. These probabilities add up to $1$.

:::

::: {#exm-random-variables-1-2 .example}

For the total $Z$ of two fair dice,
$$\begin{array}{c|ccccccccccc}
k & 2&3&4&5&6&7&8&9&10&11&12\\\hline
36\Pr(Z=k) & 1&2&3&4&5&6&5&4&3&2&1
\end{array}$$
The distribution is symmetric about $7$, the most likely total.

:::

::: {#fig-random-variables-1}

```{=latex}
\begin{tikzpicture}[x=0.62cm, y=0.42cm]
  \foreach \y in {2,4,6} {\draw[rule] (1.4,\y) -- (12.6,\y); \node[left, tick] at (1.4,\y) {$\y/36$};}
  \draw (1.4,0) -- (12.6,0);
  \foreach \k/\c in {2/1,3/2,4/3,5/4,6/5,7/6,8/5,9/4,10/3,11/2,12/1} {
    \fill[primaryStrong] (\k-0.34,0) rectangle (\k+0.34,\c);
    \node[below, tick] at (\k,0) {$\k$};
  }
\end{tikzpicture}
```

The distribution of the total $Z$ of two fair dice: symmetric about $7$, the most likely total

:::

## Joint distributions

::: {#def-joint-distribution .definition name="Joint and marginal distributions"}

The *joint distribution* of random variables $X$ and $Y$ on the same sample space gives, for every pair of values $(a,b)$, the probability
$$\Pr(X=a,\ Y=b).$$
The distribution of $X$ alone is then called its *marginal distribution*. It is found by adding over the values of $Y$:
$$\Pr(X=a)=\sum_b \Pr(X=a,\ Y=b).$$
The same applies to any finite number of random variables.

:::

::: {.proof name="Why the marginal formula holds"}

1. The events $Y=b$, over all values $b$ of $Y$, are pairwise mutually exclusive and together cover the sample space.

2. So the event $X=a$ is the disjoint union of the events $X=a,\ Y=b$, and its probability is the sum of theirs.

:::

::: {#fig-random-variables-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.0,0.0) rectangle (1.26,-0.9);
\node[tick] at (0.63,-0.45) {$1/4$};
\draw[hl cell] (1.26,0.0) rectangle (2.52,-0.9);
\node[tick] at (1.89,-0.45) {$1/4$};
\draw[cell frame] (2.52,0.0) rectangle (3.78,-0.9);
\node[tick] at (3.15,-0.45) {$0$};
\node[lab, left] at (0,-0.45) {$X=0$};
\node[tick, right] at (3.88,-0.45) {$1/2$};
\draw[cell frame] (0.0,-0.9) rectangle (1.26,-1.8);
\node[tick] at (0.63,-1.35) {$0$};
\draw[hl cell] (1.26,-0.9) rectangle (2.52,-1.8);
\node[tick] at (1.89,-1.35) {$1/4$};
\draw[hl cell] (2.52,-0.9) rectangle (3.78,-1.8);
\node[tick] at (3.15,-1.35) {$1/4$};
\node[lab, left] at (0,-1.35) {$X=1$};
\node[tick, right] at (3.88,-1.35) {$1/2$};
\node[lab, above] at (0.63,0) {$Y=0$};
\node[tick, below] at (0.63,-1.85) {$1/4$};
\node[lab, above] at (1.89,0) {$Y=1$};
\node[tick, below] at (1.89,-1.85) {$1/2$};
\node[lab, above] at (3.15,0) {$Y=2$};
\node[tick, below] at (3.15,-1.85) {$1/4$};
\end{tikzpicture}
\end{center}
```

The joint distribution of $X$, the number of heads on the first of two tosses, and $Y$, the total number of heads. Row sums (right) and column sums (below) give the distributions of $X$ and $Y$

:::

::: {#rmk-random-variables-3 .remark name="Independence in these terms"}

$X$ and $Y$ are independent (@def-independent-random-variables) exactly when the joint distribution is the product of the marginals. Random variables that are mutually independent and have the same distribution are called *i.i.d.* (independent and identically distributed); the results of repeated tosses of one coin are an example.

:::
