---
title: "Modes of Convergence"
sources: [eecs126-2]
requires: [math/probability/continuous/central-limit-theorem]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley EECS126 (Fall 2021), note "Modes of Convergence", in our own wording; proofs written out in steps. -->

A sequence of random variables $X_1,X_2,\dots$ can approach a limit $X$ in several non-equivalent senses.

::: {#def-almost-sure-convergence .definition name="Almost sure convergence"}

$X_n\to X$ *almost surely* (a.s.) if
$$\Pr\Bigl(\lim_{n\to\infty}X_n=X\Bigr)=1.$$

:::

::: {#def-convergence-in-probability .definition name="Convergence in probability"}

$X_n\to X$ *in probability* if for every $\varepsilon>0$
$$\lim_{n\to\infty}\Pr\bigl(|X_n-X|>\varepsilon\bigr)=0.$$

:::

::: {#def-convergence-in-distribution .definition name="Convergence in distribution"}

$X_n\to X$ *in distribution* if
$$\lim_{n\to\infty}\Pr(X_n\le x)=\Pr(X\le x)$$
at every $x$ where the CDF of $X$ is continuous.

:::

The weak law of large numbers (@thm-law-of-large-numbers) is convergence in probability of sample means; the strong law says they converge almost surely; the central limit theorem (@thm-central-limit-theorem) is convergence in distribution of the standardised sums.

::: {#thm-convergence-implications .theorem name="Almost sure ⇒ in probability ⇒ in distribution"}

1. If $X_n\to X$ almost surely, then $X_n\to X$ in probability.
2. If $X_n\to X$ in probability, then $X_n\to X$ in distribution.
3. If $X_n\to c$ in distribution for a constant $c$, then $X_n\to c$ in probability.

:::

::: {.proof}

1. Fix $\varepsilon>0$ and let $A_n=\{|X_m-X|>\varepsilon\text{ for some }m\ge n\}$. The $A_n$ decrease, and their intersection is contained in the event that $X_n\not\to X$, which has probability $0$. By continuity of probability $\Pr(A_n)\to0$, and $\Pr(|X_n-X|>\varepsilon)\le\Pr(A_n)$.

2. Fix a continuity point $x$ of $F_X$ and $\varepsilon>0$. If $X_n\le x$ then either $X\le x+\varepsilon$ or $|X_n-X|>\varepsilon$, so $F_{X_n}(x)\le F_X(x+\varepsilon)+\Pr(|X_n-X|>\varepsilon)$.

3. Likewise $F_X(x-\varepsilon)\le F_{X_n}(x)+\Pr(|X_n-X|>\varepsilon)$.

4. Letting $n\to\infty$, $F_X(x-\varepsilon)\le\liminf F_{X_n}(x)\le\limsup F_{X_n}(x)\le F_X(x+\varepsilon)$. Letting $\varepsilon\to0$ and using continuity of $F_X$ at $x$ gives $F_{X_n}(x)\to F_X(x)$.

5. For part 3, $\Pr(|X_n-c|>\varepsilon)\le F_{X_n}(c-\varepsilon)+1-F_{X_n}(c+\varepsilon/2)$; both $c\pm$ points are continuity points of the constant's CDF, so this tends to $0+1-1=0$.

:::

::: {#exm-convergence-counterexamples .example name="The converses fail"}

1. *In probability, not almost surely.* Let $X_n$ be independent with $\Pr(X_n=1)=1/n$ and $X_n=0$ otherwise. Then $\Pr(|X_n|>\varepsilon)=1/n\to0$. But $\sum_n1/n=\infty$, so by the second Borel–Cantelli lemma (@lem-borel-cantelli) $X_n=1$ infinitely often with probability $1$, and $X_n\not\to0$ almost surely.

2. *In distribution, not in probability.* Let $X\sim N(0,1)$ and $X_n=-X$ for all $n$. Every $X_n$ has the distribution of $X$, but $|X_n-X|=2|X|$ does not become small.

:::

::: {#lem-borel-cantelli .lemma name="Borel–Cantelli"}

Let $A_1,A_2,\dots$ be events.

1. If $\sum_n\Pr(A_n)<\infty$, then with probability $1$ only finitely many $A_n$ occur.
2. If the $A_n$ are independent and $\sum_n\Pr(A_n)=\infty$, then with probability $1$ infinitely many $A_n$ occur.

:::

::: {.proof}

1. Let $N=\sum_n\mathbf 1_{A_n}$, the number of events that occur. By linearity (monotone convergence) $E[N]=\sum_n\Pr(A_n)<\infty$, so $N<\infty$ with probability $1$.

2. For each $m$, by independence and $1-p\le e^{-p}$,
   $$\Pr\Bigl(\bigcap_{n=m}^{M}A_n^c\Bigr)=\prod_{n=m}^{M}(1-\Pr(A_n))\le\exp\Bigl(-\sum_{n=m}^{M}\Pr(A_n)\Bigr)\xrightarrow[M\to\infty]{}0.$$

3. So with probability $1$ some $A_n$ with $n\ge m$ occurs, for every $m$; a countable intersection of probability-one events has probability one.

:::

Part 1 gives a practical test for almost sure convergence: if $\sum_n\Pr(|X_n-X|>\varepsilon)<\infty$ for every $\varepsilon>0$, then $X_n\to X$ almost surely.

::: {#thm-continuous-mapping .theorem name="Continuous mapping"}

Let $f$ be continuous. If $X_n\to X$ almost surely, in probability, or in distribution, then $f(X_n)\to f(X)$ in the same sense.

:::

::: {.proof}

1. Almost surely: on the event $X_n\to X$, continuity gives $f(X_n)\to f(X)$.

2. In probability: fix $\varepsilon,\delta>0$ and choose $K$ with $\Pr(|X|>K)<\delta$. On $[-K-1,K+1]$, $f$ is uniformly continuous, so there is $\eta\in(0,1)$ with $|f(x)-f(y)|\le\varepsilon$ when $|x|\le K$ and $|x-y|\le\eta$. Then $\Pr(|f(X_n)-f(X)|>\varepsilon)\le\Pr(|X|>K)+\Pr(|X_n-X|>\eta)<2\delta$ for large $n$.

3. In distribution: we state this case without proof (it follows from the characterisation by bounded continuous functions, $E[h(X_n)]\to E[h(X)]$).

:::

::: {#rmk-convergence-expectation .remark name="Expectations need not converge"}

Convergence of $X_n$ does not give $E[X_n]\to E[X]$: with $\Pr(X_n=n)=1/n$ and $X_n=0$ otherwise, $X_n\to0$ in probability but $E[X_n]=1$. Expectations do converge when the $X_n$ are monotone and non-negative (monotone convergence) or bounded by one integrable variable (dominated convergence).

:::
