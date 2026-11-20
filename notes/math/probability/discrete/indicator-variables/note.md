---
title: "Indicator Variables and Linearity"
sources: [cs70-15.4.2, cs70-15.4.3]
requires: [math/probability/discrete/expectation-and-variance, math/discrete/counting/derangements]
aliases: [math/probability/indicator-variables]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 15 §4.2-4.3 (cs70-15.4.2, cs70-15.4.3), in our own wording. -->

## Indicator random variables

::: {#def-indicator-variable .definition name="Indicator random variable"}

The *indicator* of an event $A$ is the random variable
$$I_A(u)=\begin{cases}1, & u\in A,\\ 0, & u\notin A.\end{cases}$$
It is a Bernoulli random variable (@def-bernoulli-distribution) with parameter $\Pr(A)$.

:::

::: {#prp-expectation-of-indicator .proposition name="Expectation of an indicator"}

$E[I_A]=\Pr(A)$.

:::

::: {.proof}

By @def-expectation, $E[I_A]=0\cdot\Pr(I_A=0)+1\cdot\Pr(I_A=1)=\Pr(A)$.

:::

::: {#rmk-indicator-variables-1 .remark name="The method"}

To find the expectation of a count $X$, write $X=I_1+\cdots+I_n$, where $I_i$ indicates the $i$th thing that might be counted. By linearity (@thm-linearity-of-expectation) and @prp-expectation-of-indicator,
$$E[X]=\Pr(A_1)+\cdots+\Pr(A_n).$$
The distribution of $X$ may be hard to find, but no independence is needed for this sum.

:::

## Fixed points of a random permutation

::: {#thm-expected-fixed-points .theorem name="Expected number of fixed points"}

Let $X_n$ be the number of fixed points (@def-fixed-point) of a permutation of $\{1,\dots,n\}$ chosen uniformly at random. Then $E[X_n]=1$ for every $n\ge1$.

:::

::: {.proof}

1. Let $I_i$ indicate the event "$i$ is a fixed point". Then $X_n=I_1+\cdots+I_n$, since both sides count the fixed points at every outcome.

2. The permutations with $i$ fixed correspond to the permutations of the other $n-1$ elements, so there are $(n-1)!$ of them out of $n!$. Hence $\Pr(I_i=1)=\frac1n$.

3. By linearity (@thm-linearity-of-expectation) and @prp-expectation-of-indicator, $E[X_n]=n\cdot\frac1n=1$.

:::

::: {#fig-indicator-variables-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \i in {1,...,5} { \node[small vertex] (a\i) at (1.3*\i,1.6) {$\i$}; \node[small vertex] (b\i) at (1.3*\i,0) {$\i$}; }
\foreach \i/\j in {1/2,2/1,4/5,5/4} \draw[map] (a\i) -- (b\j);
\draw[map, hl] (a3) -- (b3);
\node[small vertex, fill=accentLight, draw=accent] at (b3) {$3$};
\node[lab, left] at (0.7,1.6) {student}; \node[lab, left] at (0.7,0) {homework};
\end{tikzpicture}
\end{center}
```

A permutation of $5$ items with one fixed point (highlighted). The indicator $I_i$ is $1$ when item $i$ is sent to itself, which happens with probability $\frac1n$; adding the $n$ indicators gives an expected number of fixed points of $1$.

:::

::: {#rmk-indicator-variables-2 .remark name="Handing back homework"}

If $n$ students' homework is handed back at random, on average exactly one student gets their own, whatever the size of the class. Compare @sec-math-discrete-counting-derangements, which counts the permutations with no fixed point.

:::
