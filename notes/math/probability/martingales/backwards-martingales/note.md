---
title: "Backwards Martingales, the Zero-One Law and the Strong Law"
sources: [camiii-ap-2]
requires: [math/probability/martingales/lp-and-l1-martingale-convergence, math/probability/measure-theoretic/tail-events]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part III Advanced Probability (lecture notes), Section 2.4, in our own wording; proofs written out in steps. -->

If the σ-algebras *decrease* with time, conditional expectations of one integrable variable still converge, and always in $L^1$. This gives short martingale proofs of Kolmogorov's zero-one law and of the strong law of large numbers.

::: {#def-backwards-filtration .definition name="Backwards filtration"}

A *backwards filtration* is a sequence of σ-algebras $\hat{\mathcal F}_0\supseteq\hat{\mathcal F}_1\supseteq\dots$; put $\hat{\mathcal F}_\infty=\bigcap_n\hat{\mathcal F}_n$.

:::

::: {#thm-backwards-martingale-convergence .theorem name="Backwards martingale convergence"}

Let $Y\in L^1$ and $(\hat{\mathcal F}_n)$ a backwards filtration. Then $X_n=E[Y\mid\hat{\mathcal F}_n]\to E[Y\mid\hat{\mathcal F}_\infty]$ almost surely and in $L^1$. The process $(X_n)$ is called a *backwards martingale*.

:::

::: {.proof}

1. Fix $n$. By the tower property, $(X_{n-k})_{0\le k\le n}$ is a martingale for the increasing filtration $\hat{\mathcal F}_n\subseteq\hat{\mathcal F}_{n-1}\subseteq\dots\subseteq\hat{\mathcal F}_0$; so is $(-X_{n-k})_k$.

2. The number of upcrossings of $[a,b]$ by $(X_k)_{0\le k\le n}$ read backwards from $n$ equals the number of upcrossings of $[-b,-a]$ by $(-X_{n-k})_k$, to which @lem-doob-upcrossing applies; as in @thm-martingale-convergence-as (the family is bounded in $L^1$ since $E|X_n|\le E|Y|$), $X_n\to X_\infty$ almost surely. The family is uniformly integrable (@lem-conditional-expectations-ui), so the convergence also holds in $L^1$.

3. $X_\infty$ is $\hat{\mathcal F}_m$-measurable for every $m$ (it is the limit of $X_n$, $n\ge m$), hence $\hat{\mathcal F}_\infty$-measurable. For $A\in\hat{\mathcal F}_\infty\subseteq\hat{\mathcal F}_n$, $E[X_\infty\mathbf 1_A]=\lim_nE[X_n\mathbf 1_A]=E[Y\mathbf 1_A]$. So $X_\infty=E[Y\mid\hat{\mathcal F}_\infty]$.

:::

::: {#thm-zero-one-martingale .theorem name="Kolmogorov's zero-one law, by martingales"}

If $X_1,X_2,\dots$ are independent and $\hat{\mathcal F}_n=\sigma(X_{n+1},X_{n+2},\dots)$, then every event of the tail σ-algebra $\hat{\mathcal F}_\infty$ has probability $0$ or $1$.

:::

::: {.proof}

1. Let $\mathcal F_n=\sigma(X_1,\dots,X_n)$ and $A\in\hat{\mathcal F}_\infty$. Then $A$ is independent of $\mathcal F_n$, so $E[\mathbf 1_A\mid\mathcal F_n]=\Pr(A)$ for all $n$.

2. The left side is a UI martingale converging a.s. to $E[\mathbf 1_A\mid\mathcal F_\infty]=\mathbf 1_A$, because $A\in\mathcal F_\infty$. Hence $\mathbf 1_A=\Pr(A)$ a.s., so $\Pr(A)\in\{0,1\}$.

:::

This is an alternative proof of @thm-kolmogorov-zero-one.

::: {#thm-slln-martingale .theorem name="Strong law of large numbers, by backwards martingales"}

Let $X_1,X_2,\dots$ be i.i.d. in $L^1$ with mean $\mu$ and $S_n=X_1+\dots+X_n$. Then $S_n/n\to\mu$ almost surely and in $L^1$.

:::

::: {.proof}

1. By symmetry (the $X_i$ are exchangeable given $S_n$), $E[X_i\mid S_n]$ does not depend on $i$, so $S_n=E[S_n\mid S_n]=nE[X_1\mid S_n]$ and $S_n/n=E[X_1\mid S_n]$.

2. The σ-algebras $\sigma(S_n)$ do not decrease, so use $\hat{\mathcal F}_n=\sigma(S_n,S_{n+1},\dots)=\sigma(S_n,X_{n+1},X_{n+2},\dots)$, a backwards filtration.

3. $\sigma(X_{n+1},X_{n+2},\dots)$ is independent of $\sigma(X_1,S_n)$, so by property 9 of @prp-conditional-expectation-properties, $E[X_1\mid\hat{\mathcal F}_n]=E[X_1\mid S_n]=S_n/n$.

4. By @thm-backwards-martingale-convergence, $S_n/n\to E[X_1\mid\hat{\mathcal F}_\infty]$ a.s. and in $L^1$. The σ-algebra $\hat{\mathcal F}_\infty$ lies in the tail σ-algebra of $(X_n)$ (since $S_n$ is determined by the $X$'s, and $\hat{\mathcal F}_\infty\subseteq\bigcap_n\sigma(S_n,X_{n+1},\dots)$ is, up to null sets, tail), which is trivial by @thm-zero-one-martingale. So the limit is a.s. constant, equal to its expectation $E[X_1]=\mu$.

:::

::: {#fig-backwards-martingales-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[box] (0,0) rectangle (7,2.4);
\draw[box] (0.4,0.3) rectangle (6.6,2.0);
\draw[box] (0.9,0.55) rectangle (6.1,1.65);
\draw[box] (1.4,0.8) rectangle (5.6,1.3);
\node[tick] at (0.5,2.2) {$\hat{\mathcal F}_0$};
\node[tick] at (1.0,1.85) {$\hat{\mathcal F}_1$};
\node[tick] at (1.5,1.5) {$\hat{\mathcal F}_2$};
\node[lab, text=accent] at (3.5,1.05) {$\hat{\mathcal F}_\infty=\bigcap_n\hat{\mathcal F}_n$};
\draw[hl, ->] (-0.6,2.2) -- (-0.6,0.9);
\node[tick] at (-1.4,1.5) {$n\uparrow$};
\end{tikzpicture}
\end{center}
```

A backwards filtration shrinks: information is forgotten as $n$ grows, and $E[Y\mid\hat{\mathcal F}_n]$ converges to the conditional expectation on what is never forgotten.

:::

::: {#rmk-backwards-martingales-1 .remark name="Relation to earlier proofs"}

@sec-math-probability-measure-theoretic-tail-events and @sec-math-probability-measure-theoretic-strong-law-of-large-numbers contain direct proofs of the same two theorems (the strong law there is proved under $L^4$ and then in general). The martingale proofs are alternatives, not extra content; see the merge proposals in the integration report.

:::
