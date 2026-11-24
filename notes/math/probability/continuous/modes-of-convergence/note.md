---
title: "Modes of Convergence"
sources: [eecs126-2, mit18650-1]
requires: [math/probability/continuous/central-limit-theorem]
relations:
  related: [math/analysis/measure-theory/convergence-in-measure]
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

::: {#fig-modes-of-convergence-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (4.6,0) node[lab, right] {$x$};
\draw[->] (0,0) -- (0,2.4) node[lab, above] {};
\draw[faint] (0.000,0.000) -- (1.333,0.000) -- (1.333,0.667);
\draw[faint] (1.333,0.667) -- (2.667,0.667) -- (2.667,1.333);
\draw[faint] (2.667,1.333) -- (4.000,1.333) -- (4.000,2.000);
\draw[emph] (0.000,0.000) -- (0.667,0.000) -- (0.667,0.333);
\draw[emph] (0.667,0.333) -- (1.333,0.333) -- (1.333,0.667);
\draw[emph] (1.333,0.667) -- (2.000,0.667) -- (2.000,1.000);
\draw[emph] (2.000,1.000) -- (2.667,1.000) -- (2.667,1.333);
\draw[emph] (2.667,1.333) -- (3.333,1.333) -- (3.333,1.667);
\draw[emph] (3.333,1.667) -- (4.000,1.667) -- (4.000,2.000);
\draw[hl] (0,0) -- (4,2) -- (4.4,2);
\draw (4,0) -- (4,-0.08) node[tick, below] {$1$};
\draw (0,2) -- (-0.08,2) node[tick, left] {$1$};
\end{tikzpicture}
\end{center}
```

Distribution functions of the uniform distribution on $\{\tfrac1n,\dots,1\}$ for $n=3,6$: the staircases approach the line $F(x)=x$ of the uniform distribution on $[0,1]$, so the variables converge in distribution

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

::: {#fig-modes-of-convergence-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0,-0.00) -- (4,-0.00);
\draw[hl] (0.00,-0.00) -- (4.00,-0.00);
\node[tick, left] at (0,-0.00) {$X_1$};
\draw[faint] (0,-0.45) -- (4,-0.45);
\draw[hl] (0.00,-0.45) -- (2.00,-0.45);
\node[tick, left] at (0,-0.45) {$X_2$};
\draw[faint] (0,-0.90) -- (4,-0.90);
\draw[hl] (2.00,-0.90) -- (4.00,-0.90);
\node[tick, left] at (0,-0.90) {$X_3$};
\draw[faint] (0,-1.35) -- (4,-1.35);
\draw[hl] (0.00,-1.35) -- (1.00,-1.35);
\node[tick, left] at (0,-1.35) {$X_4$};
\draw[faint] (0,-1.80) -- (4,-1.80);
\draw[hl] (1.00,-1.80) -- (2.00,-1.80);
\node[tick, left] at (0,-1.80) {$X_5$};
\draw[faint] (0,-2.25) -- (4,-2.25);
\draw[hl] (2.00,-2.25) -- (3.00,-2.25);
\node[tick, left] at (0,-2.25) {$X_6$};
\draw[faint] (0,-2.70) -- (4,-2.70);
\draw[hl] (3.00,-2.70) -- (4.00,-2.70);
\node[tick, left] at (0,-2.70) {$X_7$};
\node[tick, below] at (0,-3.0) {$0$};
\node[tick, below] at (4,-3.0) {$1$};
\end{tikzpicture}
\end{center}
```

The sliding indicators on $[0,1]$: $X_n$ is $1$ on the highlighted interval. The intervals shrink, so $X_n\to0$ in probability, but they sweep across $[0,1]$ again and again, so $X_n(\omega)\to0$ for no $\omega$

:::

::: {#fig-modes-of-convergence-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (as) at (0,0) {almost surely};
\node[box] (pr) at (4.2,0) {in probability};
\node[box] (di) at (8.4,0) {in distribution};
\draw[-{Implies}, double, double distance=1.6pt, emph] (as) -- (pr);
\draw[-{Implies}, double, double distance=1.6pt, emph] (pr) -- (di);
\draw[->, dashed, accent] (pr) to[bend left=30] node[edge label, below=2pt] {fails: example 1} (as);
\draw[->, dashed, accent] (di) to[bend left=30] node[edge label, below=2pt] {fails: example 2} (pr);
\end{tikzpicture}
\end{center}
```

The modes of convergence: each implies the next (@thm-convergence-implications), and the two parts of @exm-convergence-counterexamples show that neither implication can be reversed.

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

<!-- Added 2026-11-21 from MIT 18.650 (Fall 2016), Chapter 1 (review of convergence: convergence in L^p, characterisations of convergence in distribution, sums and products of limits), in our own wording; proofs written out in steps. -->

::: {#def-lp-convergence .definition name="Convergence in mean of order p"}

Let $p\ge1$. $X_n\to X$ *in $L^p$* (in mean of order $p$) if $E[|X_n|^p]$ and $E[|X|^p]$ are finite and
$$\lim_{n\to\infty}E\bigl[|X_n-X|^p\bigr]=0 .$$
For $p=2$ this is *convergence in mean square*.

:::

::: {#prp-lp-convergence .proposition name="Convergence in $L^p$ is stronger than in probability"}

1. If $X_n\to X$ in $L^p$, then $X_n\to X$ in $L^q$ for every $1\le q\le p$.
2. If $X_n\to X$ in $L^p$ for some $p\ge1$, then $X_n\to X$ in probability.

:::

::: {.proof}

1. Let $Y=|X_n-X|$. The function $y\mapsto y^{p/q}$ is convex on $[0,\infty)$ because $p/q\ge1$, so Jensen's inequality gives $\bigl(E[Y^q]\bigr)^{p/q}\le E[Y^p]$.

2. Hence $E[|X_n-X|^q]\le\bigl(E[|X_n-X|^p]\bigr)^{q/p}\to0$, which is part 1.

3. For part 2 fix $\varepsilon>0$. By the generalised Markov inequality (@thm-generalised-markov) applied to $|X_n-X|^p$,
   $$\Pr\bigl(|X_n-X|>\varepsilon\bigr)\le\frac{E[|X_n-X|^p]}{\varepsilon^p}\to0 .$$

:::

The converse of part 2 fails, for the reason given in the remark on expectations above: with $\Pr(X_n=n)=1/n$, $X_n\to0$ in probability but $E[|X_n|]=1$ for every $n$.

::: {#prp-limits-of-sums-products .proposition name="Sums and products of limits"}

Suppose $U_n\to U$ and $V_n\to V$, both almost surely or both in probability. Then, in the same sense,
$$U_n+V_n\to U+V,\qquad U_nV_n\to UV,$$
and $U_n/V_n\to U/V$ if moreover $\Pr(V=0)=0$.

:::

::: {.proof}

1. *Almost surely.* The two events $\{U_n\to U\}$ and $\{V_n\to V\}$ have probability $1$, so their intersection does. On it the ordinary limit rules for real sequences give all three statements (the quotient where $V\ne0$, which also has probability $1$).

2. *In probability.* The pair $(U_n,V_n)$ converges in probability to $(U,V)$ in the plane: $\Pr(\|(U_n,V_n)-(U,V)\|>\varepsilon)\le\Pr(|U_n-U|>\varepsilon/2)+\Pr(|V_n-V|>\varepsilon/2)\to0$.

3. The maps $(u,v)\mapsto u+v$ and $(u,v)\mapsto uv$ are continuous on $\mathbb{R}^2$, and $(u,v)\mapsto u/v$ is continuous where $v\ne0$. The proof of @thm-continuous-mapping, part 2, works word for word for random vectors (choose $K$ with $\Pr(\|(U,V)\|>K)<\delta$; for the quotient, also choose $\kappa>0$ with $\Pr(|V|<\kappa)<\delta$ and work on the compact set $\{\|(u,v)\|\le K+1,\ |v|\ge\kappa/2\}$), which proves the claim.

:::

::: {#rmk-limits-in-distribution .remark name="Convergence in distribution does not add"}

The rules of @prp-limits-of-sums-products fail for convergence in distribution. Take $X\sim N(0,1)$, $U_n=X$ and $V_n=-X$. Then $U_n\to X$ and $V_n\to X$ in distribution (since $-X$ has the law of $X$), but $U_n+V_n=0$ does not converge in distribution to $X+X\sim N(0,4)$. Convergence in distribution concerns each law separately and says nothing about the joint law; the rules hold when the pair $(U_n,V_n)$ converges in distribution to $(U,V)$, and in the important case where one limit is a constant (Slutsky's theorem, @thm-slutsky).

:::

::: {#prp-convergence-in-distribution-tests .proposition name="Other ways to check convergence in distribution"}

Each of the following is equivalent to $X_n\to X$ in distribution (stated without proof).

1. $E[h(X_n)]\to E[h(X)]$ for every bounded continuous function $h$; it is even enough to check this for bounded uniformly continuous $h$.
2. The characteristic functions converge: $E[e^{itX_n}]\to E[e^{itX}]$ for every $t\in\mathbb{R}$ (Lévy's continuity theorem).

Both carry over to random vectors in $\mathbb{R}^d$, with $t\in\mathbb{R}^d$ and $e^{i\,t^{\mathsf T}X_n}$; the definition by CDFs does too, with $\Pr(X_n\le x)$ read componentwise.

:::

