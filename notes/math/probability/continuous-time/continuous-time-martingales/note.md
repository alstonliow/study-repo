---
title: "Continuous-Time Martingales: Optional Stopping, Convergence and Regularisation"
sources: [camiii-ap-3]
requires: [math/probability/continuous-time/continuous-time-stopping-times, math/probability/martingales/lp-and-l1-martingale-convergence]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part III Advanced Probability (lecture notes), Section 3, in our own wording; proofs written out in steps. -->

A continuous-time martingale is sampled along any increasing sequence of times to give a discrete martingale, and along a decreasing sequence to give a backwards martingale. With cadlag paths, almost every discrete result carries over by approximating along dyadic times.

::: {#def-continuous-time-martingale .definition name="Continuous-time martingale"}

An adapted integrable process $(X_t)_{t\ge0}$ is a *martingale* if $E[X_t\mid\mathcal F_s]=X_s$ for $t\ge s$; super- and sub-martingales have $\le$, resp. $\ge$.

:::

::: {#thm-optional-stopping-continuous .theorem name="Optional stopping (continuous time)"}

For an adapted cadlag integrable process $X$ the following are equivalent:

1. For every bounded stopping time $T$ and every stopping time $S$, $X_T\in L^1$ and $E[X_T\mid\mathcal F_S]=X_{T\wedge S}$.
2. For every stopping time $T$, $X^T=(X_{T\wedge t})_t$ is a martingale.
3. For every bounded stopping time $T$, $X_T\in L^1$ and $E[X_T]=E[X_0]$.

:::

::: {.proof}

We show (1)⇒(2); the other implications follow from the discrete case as before.

1. Assume $T\le t$, with $t\in\mathbb N$ by enlarging. Let $T_n=2^{-n}\lceil2^nT\rceil$ and $S_n=2^{-n}\lceil2^nS\rceil$; $T_n\downarrow T$ and $X_{T_n}\to X_T$ by right-continuity.

2. $T_n\le t+1$ takes values in $D_n$, so discrete optional stopping gives $E[X_{t+1}\mid\mathcal F_{T_n}]=X_{T_n}$. Hence $(X_{T_n})_n$ is uniformly integrable, converges in $L^1$, and $X_T\in L^1$.

3. Let $A\in\mathcal F_S\subseteq\mathcal F_{S_n}$. Discrete optional stopping for the bounded times $S_n\wedge T_n\le T_n$ gives $E[X_{T_n}\mathbf 1_A]=E[X_{S_n\wedge T_n}\mathbf 1_A]$. Both sides converge in $L^1$ as $n\to\infty$ (the families are uniformly integrable by step 2), so $E[X_T\mathbf 1_A]=E[X_{S\wedge T}\mathbf 1_A]$. Together with the $\mathcal F_S$-measurability of $X_{S\wedge T}$ this is (1).

:::

::: {#thm-continuous-martingale-convergence .theorem name="Convergence for super-martingales bounded in $L^1$"}

A cadlag super-martingale bounded in $L^1$ converges almost surely as $t\to\infty$ to some $X_\infty\in L^1$.

:::

::: {.proof}

1. Let $U_s[a,b]$ be the number of upcrossings of $[a,b]$ up to time $s$. By right-continuity, $U_s[a,b,(X_t)_{t\ge0}]=\lim_nU_s[a,b,(X_t)_{t\in D_n}]$ (monotone in $n$).

2. By monotone convergence and Doob's upcrossing lemma applied to each discrete skeleton, $E[U_s[a,b]]\le\sup_nE(X_s-a)^-/(b-a)\le(E|X_s|+|a|)/(b-a)$. Taking $s\to\infty$ shows $U_\infty[a,b]<\infty$ a.s.

3. As in discrete time, convergence in $[-\infty,\infty]$ follows; $E|X_\infty|\le\liminf E|X_{t_n}|<\infty$ by Fatou, so $X_\infty$ is finite a.s.

:::

For cadlag martingales or non-negative sub-martingales, Doob's maximal and $L^p$ inequalities hold with $X^*_t=\sup_{s\le t}|X_s|$, by approximating with dyadic times and monotone convergence: $\lambda\Pr(X^*_t\ge\lambda)\le E|X_t|$ and $\|X^*_t\|_p\le\frac p{p-1}\|X_t\|_p$.

::: {#thm-martingale-regularisation .theorem name="Regularisation of martingales"}

Let $(X_t)$ be a martingale for a filtration satisfying the usual conditions. Then $X$ has a cadlag version.

:::

::: {.proof}

1. For $M>0$ let $\Omega^M_0=\{\sup_{q\in D\cap[0,M]}|X_q|<\infty\}\cap\bigcap_{a<b\in\mathbb Q}\{U_M[a,b,(X_t)_{t\in D\cap[0,M]}]<\infty\}$. By the maximal and upcrossing inequalities $\Pr(\Omega^M_0)=1$.

2. Define $\tilde X_t=\lim_{s\downarrow t,\,s\in D}X_s\mathbf 1_{\Omega^t_0}$. This is $\mathcal F_t$-measurable by the usual conditions, and the path is cadlag on $\Omega_0^M$ because the dyadic skeleton has finitely many upcrossings (a function with finitely many upcrossings and bounded on every compact interval has one-sided limits).

3. For $t_n\downarrow t$, $(X_{t_n})$ is a backwards martingale, so it converges a.s. and in $L^1$ to $\tilde X_t$. Since $X_t=E[X_{t_n}\mid\mathcal F_t]$ and $\tilde X_t$ is $\mathcal F_t$-measurable, $X_t=\tilde X_t$ a.s.: $\tilde X$ is a version of $X$.

:::

::: {#thm-continuous-martingale-lp-l1 .theorem name="$L^p$ and $L^1$ convergence, closed martingales (continuous time)"}

For a cadlag martingale $(X_t)$:

1. for $p>1$: bounded in $L^p$ $\iff$ $X_t\to X_\infty$ a.s. and in $L^p$ $\iff$ $X_t=E[Z\mid\mathcal F_t]$ for some $Z\in L^p$;
2. uniformly integrable $\iff$ $X_t\to X_\infty$ a.s. and in $L^1$ $\iff$ $X_t=E[Z\mid\mathcal F_t]$ for some $Z\in L^1$;
3. if $X$ is uniformly integrable and $S,T$ are arbitrary stopping times, $E[X_T\mid\mathcal F_S]=X_{S\wedge T}$.

:::

The proofs reduce to @thm-lp-martingale-convergence, @thm-l1-martingale-convergence and @thm-optional-stopping-ui along integer times and dyadic approximations.

::: {#fig-continuous-time-martingales-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-0.2,0) -- (8.2,0) node[lab, right] {$t$};
\draw[emph] (0,1.2) -- (1.5,1.2) -- (1.5,1.8) -- (3.0,1.8) -- (3.0,1.1) -- (5.0,1.1) -- (5.0,1.5) -- (8,1.5);
\foreach \x in {0,1,2,3,4,5,6,7,8} {\draw[faint] (\x,0) -- (\x,0.12);}
\draw[hl] (0,1.2) -- (1,1.2) -- (2,1.8) -- (3,1.8) -- (4,1.1) -- (5,1.1) -- (6,1.5) -- (7,1.5) -- (8,1.5);
\node[lab, text=accent] at (4,2.5) {a cadlag path (jumps) and its dyadic skeleton (highlighted)};
\end{tikzpicture}
\end{center}
```

A cadlag path is determined by its values on dyadic times; discrete martingale theory applied to the skeletons passes to the limit.

:::
