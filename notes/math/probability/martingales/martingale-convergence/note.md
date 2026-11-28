---
title: "Doob's Upcrossing Lemma and Almost Sure Martingale Convergence"
sources: [camiii-ap-2]
requires: [math/probability/martingales/martingales-and-stopping-times]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part III Advanced Probability (lecture notes), Section 2.3, in our own wording; proofs written out in steps. -->

A real sequence converges iff it is bounded in the right way and does not oscillate between two rational levels infinitely often. For a super-martingale the number of oscillations can be controlled in expectation, because a player who buys at $a$ and sells at $b$ cannot gain on average.

::: {#def-upcrossing .definition name="Upcrossings"}

For a sequence $(x_n)$ and $a<b$, an *upcrossing* of $[a,b]$ is a run $j,j+1,\dots,k$ with $x_j\le a$ and $x_k\ge b$. Let $U_n[a,b]$ be the number of disjoint upcrossings inside $\{0,\dots,n\}$ and $U[a,b]=\lim_nU_n[a,b]$.

:::

::: {#lem-convergence-criterion .lemma name="Convergence criterion"}

A real sequence $(x_n)$ converges in $\mathbb R$ iff (i) $\liminf|x_n|<\infty$ and (ii) $U[a,b]<\infty$ for all rationals $a<b$.

:::

If $\liminf x_n<\limsup x_n$, pick rationals $a<b$ strictly between them: the sequence is below $a$ and above $b$ infinitely often, so $U[a,b]=\infty$. Conversely (i) and (ii) rule out $\pm\infty$ limits and oscillation.

::: {#fig-martingale-convergence-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0,0.5) -- (9,0.5);
\draw[faint] (0,2) -- (9,2);
\node[tick, left] at (0,0.5) {$a$};
\node[tick, left] at (0,2) {$b$};
\draw[emph] (0,1.2) -- (1,0.5) -- (2,1.0) -- (3,2.2) -- (4,1.5) -- (5,0.3) -- (6,0.9) -- (7,2.1) -- (8,1.4) -- (9,1.7);
\draw[hl] (1,0.5) -- (2,1.0) -- (3,2.2);
\draw[hl] (5,0.3) -- (6,0.9) -- (7,2.1);
\node[lab, text=accent] at (2,2.8) {up 1};
\node[lab, text=accent] at (6,2.8) {up 2};
\end{tikzpicture}
\end{center}
```

Two upcrossings of $[a,b]$ (highlighted): runs from at or below $a$ to at or above $b$.

:::

::: {#lem-doob-upcrossing .lemma name="Doob's upcrossing lemma"}

If $(X_n)$ is a super-martingale, then

$$
(b-a)\,E[U_n[a,b]]\le E[(X_n-a)^-].
$$

:::

::: {.proof}

1. Define stopping times $T_0=0$, $S_{k+1}=\inf\{n\ge T_k:X_n\le a\}$, $T_{k+1}=\inf\{n\ge S_{k+1}:X_n\ge b\}$. Consider $\sum_{k\ge1}\big(X_{T_k\wedge n}-X_{S_k\wedge n}\big)$ (a finite sum, at most $n$ nonzero terms).

2. Each completed upcrossing contributes $X_{T_k}-X_{S_k}\ge b-a$. If the path is in the middle of an upcrossing at time $n$ (so $S_{U+1}\le n<T_{U+1}$, $U=U_n$), that unfinished stretch contributes $X_n-X_{S_{U+1}}\ge-(X_n-a)^-$; all later terms are $0$. Hence the sum is at least $(b-a)U_n-(X_n-a)^-$.

3. Since $S_k\wedge n\le T_k\wedge n$ are bounded stopping times, $E[X_{T_k\wedge n}]\le E[X_{S_k\wedge n}]$ by optional stopping, so the expected sum is $\le0$. Therefore $0\ge(b-a)E[U_n]-E[(X_n-a)^-]$.

:::

::: {#thm-martingale-convergence-as .theorem name="Almost sure martingale convergence"}

Let $(X_n)$ be a super-martingale bounded in $L^1$, $\sup_nE|X_n|<\infty$. Then there is an $\mathcal F_\infty$-measurable $X_\infty\in L^1$ with $X_n\to X_\infty$ almost surely.

:::

::: {.proof}

1. By Fatou, $E[\liminf|X_n|]\le\liminf E|X_n|<\infty$, so $\liminf|X_n|<\infty$ a.s.

2. For rationals $a<b$, the upcrossing lemma and $E(X_n-a)^-\le E|X_n|+|a|\le C$ give $E[U_n[a,b]]\le C/(b-a)$ uniformly in $n$. By monotone convergence $E[U[a,b]]<\infty$, so $U[a,b]<\infty$ a.s.

3. There are countably many rational pairs, so almost surely both conditions of @lem-convergence-criterion hold, and $X_n$ converges; the limit $X_\infty$ is $\mathcal F_\infty$-measurable and in $L^1$ by Fatou.

:::

::: {#exm-product-martingale-no-l1 .example name="Convergence without $L^1$ convergence"}

For the product martingale $X_n=\rho_1\cdots\rho_n$ with $\rho_k\in\{0,2\}$ equally likely, $E X_n=1$ and $\sup E|X_n|=1$. Almost surely some $\rho_k=0$, so $X_n\to0$ a.s., yet $\|X_n-0\|_1=1\not\to0$. Bounded in $L^1$ gives pointwise convergence but not convergence of expectations: uniform integrability is needed (@sec-math-probability-martingales-lp-and-l1-martingale-convergence).

:::
