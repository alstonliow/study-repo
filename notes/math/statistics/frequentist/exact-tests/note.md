---
title: "Permutation Tests and Fisher's Exact Test"
sources: [camib-st-10]
requires: [math/statistics/frequentist/contingency-tables, math/probability/distributions/hypergeometric-distribution]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part IB Statistics (Lent 2025, lecturer's notes), Lecture 10 (permutation tests; the lady tasting tea; Fisher's exact test), in our own wording; proofs written out in steps. -->

The chi-squared test of independence uses an approximate null distribution. When the two classifications are independent, the data have a symmetry that gives the null distribution exactly, by relabelling.

::: {#thm-permutation-null .theorem name="The permutation null distribution"}

Let $(X_1,Y_1),\dots,(X_n,Y_n)$ be iid pairs. If $X_1$ and $Y_1$ are independent, then for every permutation $\pi$ of $\{1,\dots,n\}$
$$(X_1,Y_1,\dots,X_n,Y_n)\overset d=(X_1,Y_{\pi(1)},\dots,X_n,Y_{\pi(n)}).$$

:::

::: {.proof}

By independence the pairs have the joint law $P_X\otimes P_Y$, and the vector $(X_1,\dots,X_n,Y_1,\dots,Y_n)$ has independent coordinates, the $X_i$ with law $P_X$ and the $Y_i$ with law $P_Y$. Permuting the $Y$'s among themselves leaves this product law unchanged.

:::

::: {#def-permutation-test .definition name="Permutation test"}

Let $S(x,y)$ be a statistic that is large when the data are far from independence. The *permutation $p$-value* of the observed data is
$$P=\frac1{n!}\#\bigl\{\pi:\ S\bigl(x,(y_{\pi(1)},\dots,y_{\pi(n)})\bigr)\ge S(x,y)\bigr\},$$
the fraction of relabellings whose statistic is at least as extreme. By @thm-permutation-null, if $H_0$ holds then $P$ is exactly (not approximately) a valid $p$-value (it satisfies $P(P\le\alpha)\le\alpha$), whatever the sample size. It is computed by enumeration or by random permutations; for $2$-way tables this amounts to generating random tables with the observed row and column totals (R's `chisq.test` with `simulate.p.value=TRUE`).

:::

::: {#thm-fisher-exact .theorem name="Fisher's exact test"}

For a $2\times2$ table $(N_{ij})$ with all margins $N_{1+},N_{2+},N_{+1},N_{+2}$ fixed and total $n$, suppose the $n$ units are randomly relabelled as in a permutation test, that is $H_0$ holds. Then $N_{11}$ has the hypergeometric distribution
$$P(N_{11}=k)=\frac{\binom{N_{1+}}{k}\binom{N_{2+}}{N_{+1}-k}}{\binom{n}{N_{+1}}},$$
and the exact test of $H_0$ against an alternative of positive association rejects for large $N_{11}$, with $p$-value $\sum_{j\ge N_{11}^{\mathrm{obs}}}P(N_{11}=j)$.

:::

::: {.proof}

1. Mark the $N_{1+}$ units in row $1$. Under random relabelling, the set of $N_{+1}$ units that fall in column $1$ is a uniformly random subset of size $N_{+1}$ of the $n$ units, as each subset arises from the same number of permutations.

2. $N_{11}=k$ means that exactly $k$ of the chosen units lie in row $1$ and $N_{+1}-k$ in row $2$; the number of such subsets is $\binom{N_{1+}}{k}\binom{N_{2+}}{N_{+1}-k}$ out of $\binom{n}{N_{+1}}$.

3. This is the hypergeometric distribution (@def-hypergeometric-distribution). The table has a single degree of freedom given its margins, so $N_{11}$ determines it.

:::

::: {#exm-lady-tasting-tea .example name="The lady tasting tea"}

Eight cups of tea are prepared, four with the milk added first and four with the tea first, and a lady, told this in advance, classifies each cup. The margins are all $4$, and $N_{11}$, the number of milk-first cups she identifies correctly, is hypergeometric with $P(N_{11}=k)=\binom4k\binom4{4-k}/\binom84$:
$$P(4)=\frac1{70}\approx1.4\%,\qquad P(3)=\frac{16}{70},\qquad P(N_{11}\ge3)=\frac{17}{70}\approx24.3\% .$$
Getting all four right gives $p=1.4\%$, evidence against guessing at the $5\%$ level; getting three right ($p=24.3\%$) does not.

:::

::: {#fig-exact-tests-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=8cm]
\draw[->, muted] (-0.7,0) -- (4.9,0) node[lab, right] {$k$};
\draw[->, muted] (-0.7,0) -- (-0.7,0.58);
\foreach \x in {0,1,2,3,4} \node[tick, below] at (\x,0) {$\x$};
\foreach \x/\v in {0/0.0143,1/0.2286,2/0.5143,3/0.2286,4/0.0143}
  \fill[primary] (\x-0.3,0) rectangle (\x+0.3,\v);
\foreach \y in {0.1,0.2,0.3,0.4,0.5} \node[tick, left] at (-0.7,\y) {$\y$};
\fill[hl] (3-0.3,0) rectangle (3+0.3,0.2286);
\fill[hl] (4-0.3,0) rectangle (4+0.3,0.0143);
\node[lab] at (3.5,0.42) {$P(N_{11}\ge3)=\tfrac{17}{70}$};
\end{tikzpicture}
\end{center}
```

The null distribution of $N_{11}$ in the tea-tasting experiment, the hypergeometric law with margins $4,4,4,4$. The highlighted bars add up to the $p$-value $17/70$ for an observed $N_{11}=3$.

:::
