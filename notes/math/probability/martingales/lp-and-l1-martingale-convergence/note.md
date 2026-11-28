---
title: "Martingale Convergence in $L^p$ and $L^1$, Closed Martingales"
sources: [camiii-ap-2]
requires: [math/probability/martingales/martingale-convergence, math/probability/martingales/doob-inequalities]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part III Advanced Probability (lecture notes), Section 2.3, in our own wording; proofs written out in steps. -->

When does a martingale converge in $L^p$, and when is it of the form $E[Z\mid\mathcal F_n]$? For $p>1$, boundedness in $L^p$ is the exact condition; for $p=1$ one needs uniform integrability. In both cases martingales correspond one-to-one to their terminal values.

::: {#thm-lp-martingale-convergence .theorem name="$L^p$ martingale convergence ($p>1$)"}

For a martingale $(X_n)$ and $p>1$ the following are equivalent:

1. $(X_n)$ is bounded in $L^p$: $\sup_nE|X_n|^p<\infty$.
2. $X_n\to X_\infty$ almost surely and in $L^p$.
3. There is $Z\in L^p$ with $X_n=E[Z\mid\mathcal F_n]$ for all $n$.

Moreover in (3), $X_\infty=E[Z\mid\mathcal F_\infty]$. Hence $X\mapsto X_\infty$ is a bijection between $L^p$-bounded martingales and $L^p(\mathcal F_\infty)$.

:::

::: {.proof}

1. *(1)⇒(2).* Bounded in $L^p$ implies bounded in $L^1$, so $X_n\to X_\infty$ a.s. (@thm-martingale-convergence-as), and $X_\infty\in L^p$ by Fatou. By Doob's inequality and monotone convergence, $\|X^*\|_p\le\frac p{p-1}\sup_n\|X_n\|_p<\infty$ (@lem-doob-lp-inequality). Since $|X_n-X_\infty|\le2X^*$, dominated convergence gives $X_n\to X_\infty$ in $L^p$.

2. *(2)⇒(3).* Take $Z=X_\infty$. For $n\ge m$, $\|X_m-E[X_\infty\mid\mathcal F_m]\|_p=\|E[X_n-X_\infty\mid\mathcal F_m]\|_p\le\|X_n-X_\infty\|_p\to0$ (conditional expectation does not increase $L^p$ norms), and the left side does not depend on $n$, hence is $0$.

3. *(3)⇒(1)* since conditional expectation is an $L^p$ contraction.

4. *Moreover.* $\bigcup_n\mathcal F_n$ is a π-system generating $\mathcal F_\infty$. For $A\in\mathcal F_m$, $E[X_\infty\mathbf 1_A]=\lim_nE[X_n\mathbf 1_A]=E[Z\mathbf 1_A]=E[E[Z\mid\mathcal F_\infty]\mathbf 1_A]$. Two integrable variables with the same integrals over a generating π-system (and over $\Omega$) and both $\mathcal F_\infty$-measurable agree a.s.

:::

::: {#thm-l1-martingale-convergence .theorem name="$L^1$ martingale convergence"}

For a martingale $(X_n)$ the following are equivalent:

1. $(X_n)$ is uniformly integrable.
2. $X_n\to X_\infty$ almost surely and in $L^1$.
3. There is $Z\in L^1$ with $X_n=E[Z\mid\mathcal F_n]$ a.s.

Moreover $X_\infty=E[Z\mid\mathcal F_\infty]$; so uniformly integrable martingales correspond to $L^1(\mathcal F_\infty)$.

:::

::: {.proof}

1. *(1)⇒(2).* A UI family is bounded in $L^1$, so $X_n\to X_\infty$ a.s. by martingale convergence; almost sure convergence plus uniform integrability gives $L^1$ convergence (@thm-l1-convergence-ui).

2. *(2)⇒(3)* is the same argument as for $L^p$, with $Z=X_\infty$ and $L^1$ norms. 

3. *(3)⇒(1)* by @lem-conditional-expectations-ui: the conditional expectations of one integrable variable form a UI family. The identification of $X_\infty$ is as before.

:::

::: {#thm-optional-stopping-ui .theorem name="Optional stopping for uniformly integrable martingales"}

If $(X_n)$ is a uniformly integrable martingale and $S,T$ are arbitrary stopping times, then $E[X_T\mid\mathcal F_S]=X_{S\wedge T}$; in particular $E[X_T]=E[X_0]$. Here $X_T=X_\infty$ on $\{T=\infty\}$.

:::

::: {.proof}

1. By the bounded-time theorem, $E[X_{T\wedge n}\mid\mathcal F_S]=X_{S\wedge T\wedge n}$ for each $n$.

2. By optional stopping and the tower property, $X_{T\wedge n}=E[X_n\mid\mathcal F_{T\wedge n}]=E[E[X_\infty\mid\mathcal F_n]\mid\mathcal F_{T\wedge n}]=E[X_\infty\mid\mathcal F_{T\wedge n}]$, so $(X_{T\wedge n})_n$ is uniformly integrable, hence $X_{T\wedge n}\to X_T$ a.s. and in $L^1$.

3. Then $\|E[X_{T\wedge n}-X_T\mid\mathcal F_S]\|_1\le\|X_{T\wedge n}-X_T\|_1\to0$, so the left side of step 1 converges to $E[X_T\mid\mathcal F_S]$, while the right side converges a.s. to $X_{S\wedge T}$.

:::

::: {#fig-lp-and-l1-martingale-convergence-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (a) at (0,0) {$L^p(\mathcal F_\infty)$ ($p>1$)};
\node[box] (b) at (5.5,0) {$L^p$-bounded martingales};
\node[box] (c) at (0,-1.6) {$L^1(\mathcal F_\infty)$};
\node[box] (d) at (5.5,-1.6) {UI martingales};
\draw[->] (a) -- node[tick, above] {$Z\mapsto E[Z\mid\mathcal F_n]$} (b);
\draw[->] (c) -- node[tick, above] {$Z\mapsto E[Z\mid\mathcal F_n]$} (d);
\end{tikzpicture}
\end{center}
```

Closed martingales are exactly those that converge in the strong sense; the terminal value $X_\infty=Z$ determines the whole process.

:::
