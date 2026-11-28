---
title: "Local Martingales"
sources: [camiii-sc-2]
requires: [math/probability/stochastic-calculus/finite-variation-and-previsible-processes, math/probability/continuous-time/continuous-time-martingales]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part III Stochastic Calculus and Applications (lecture notes), Section 2.2, in our own wording; proofs written out in steps. -->

From now on the filtration satisfies the usual conditions (@def-usual-conditions). Martingales are not closed under the operations of stochastic calculus, but local martingales are.

::: {#def-local-martingale .definition name="Local martingale"}

A càdlàg adapted process $X$ is a *local martingale* if there are stopping times $T_n\to\infty$ almost surely such that each stopped process $X^{T_n}$ is a martingale. The sequence $(T_n)$ *reduces* $X$.

:::

Every martingale is a local martingale (take $T_n=n$ and use optional stopping, @thm-optional-stopping-continuous).

::: {#exm-inverse-bessel .example name="A strict local martingale: 1/|B| in three dimensions"}

Let $B$ be a standard Brownian motion in $\mathbb R^3$ and $X_t=1/|B_t|$ for $t\ge1$. Then $\sup_tE[X_t^2]<\infty$ and $E[X_t]\to0$, so the non-negative process $X$ is not a martingale (a martingale would have constant expectation). It is a local martingale:

1. For $f\in C_b^2$, $f(B_t)-f(B_1)-\frac12\int_1^t\Delta f(B_s)\,ds$ is a martingale (@sec-math-probability-brownian-motion-harmonic-functions-and-dirichlet-problem), and $\Delta(1/|x|)=0$ for $x\ne0$.

2. Let $T_n=\inf\{t\ge1:|B_t|<1/n\}$ and choose $f_n\in C_b^2$ with $f_n(x)=1/|x|$ for $|x|\ge1/n$. Then $X^{T_n}_t-X_1=f_n(B_{t\wedge T_n})-f_n(B_1)-\frac12\int_1^{t\wedge T_n}\Delta f_n(B_s)ds$ is a martingale increment.

3. $T_n\to\infty$ since $B$ never hits $0$ in $\mathbb R^3$ (@thm-brownian-recurrence).

:::

::: {#fig-local-martingales-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint, ->] (0,0) -- (5.5,0) node[right, lab] {$t$};
\draw[faint, ->] (0,0) -- (0,2.4);
\draw[emph] plot[domain=0.3:5.2,samples=25] (\x,{1.8/sqrt(\x+0.5)});
\draw[hl, dashed] (0,1.8) -- (5.2,1.8);
\node[lab, text=accent] at (3.6,2.2) {a martingale would stay here};
\node[lab] at (4.0,0.35) {$E[1/|B_t|]\to0$};
\end{tikzpicture}
\end{center}
```

The expectation of the non-negative local martingale $1/|B_t|$ decays to $0$, while a martingale has constant expectation; so it is a strict local martingale.

:::

::: {#prp-nonnegative-local-martingale .proposition name="Non-negative local martingales are super-martingales"}

If $X$ is a local martingale with $X_t\ge0$, then $X$ is a super-martingale.

:::

::: {.proof}

With $(T_n)$ reducing $X$ and $s<t$, Fatou's lemma for conditional expectations gives
$$E[X_t\mid\mathcal F_s]=E\big[\liminf_nX_{t\wedge T_n}\mid\mathcal F_s\big]\le\liminf_nE[X_{t\wedge T_n}\mid\mathcal F_s]=\liminf_nX_{s\wedge T_n}=X_s.$$

:::

::: {#prp-local-martingale-ui .proposition name="Martingale = local martingale with a uniformly integrable family"}

$X$ is a martingale if and only if it is a local martingale and, for every $t\ge0$, the family $\{X_T:T\text{ a stopping time},\,T\le t\}$ is uniformly integrable.

:::

::: {.proof}

(⇒) For a stopping time $T\le t$, optional stopping gives $X_T=E[X_t\mid\mathcal F_T]$, and conditional expectations of one integrable variable form a uniformly integrable family.

(⇐) Let $(T_n)$ reduce $X$ and $T\le t$ a stopping time.

1. $E[X_0]=E[X_0^{T_n}]=E[X^{T_n}_T]=E[X_{T\wedge T_n}]$.

2. $T\wedge T_n\le t$ and $T\wedge T_n\to T$ a.s., so $X_{T\wedge T_n}\to X_T$ a.s., hence in probability.

3. By uniform integrability and the equivalence of $L^1$-convergence with convergence in probability plus uniform integrability (@thm-l1-convergence-ui), $E[X_{T\wedge T_n}]\to E[X_T]$. So $E[X_T]=E[X_0]$ for all bounded stopping times, and $X$ is a martingale by @thm-optional-stopping-continuous.

:::

::: {#cor-dominated-local-martingale .corollary name="Domination gives a martingale"}

If $|X_t|\le Z\in L^1$ for all $t$, a local martingale $X$ is a martingale. In particular every bounded local martingale is a martingale.

:::

::: {#prp-localising-by-hitting-times .proposition name="A bounded reducing sequence"}

Let $X$ be a continuous local martingale with $X_0=0$ and $S_n=\inf\{t\ge0:|X_t|=n\}$. Then $S_n$ is a stopping time, $S_n\to\infty$, and $X^{S_n}$ is a bounded martingale; so $(S_n)$ reduces $X$.

:::

::: {.proof}

1. $\{S_n\le t\}=\bigcap_k\bigcup_{s<t,s\in\mathbb Q}\{|X_s|>n-1/k\}\in\mathcal F_t$, so $S_n$ is a stopping time.

2. By continuity $\sup_{s\le t}|X_s|<\infty$ for each $(\omega,t)$, and $\{\sup_{s\le t}|X_s|\le n\}=\{S_n\ge t\}$, hence $S_n\to\infty$.

3. $X^{S_n}$ is a local martingale (stopping a localised martingale again) bounded by $n$, hence a martingale by @cor-dominated-local-martingale.

:::

::: {#thm-fv-local-martingale-zero .theorem name="Continuous local martingales of finite variation are constant"}

If $X$ is a continuous local martingale with $X_0=0$ which is also a finite variation process, then $X_t=0$ for all $t$, almost surely.

:::

::: {.proof}

1. Let $V$ be the total variation process of $X$ and $S_n=\inf\{t:V_t\ge n\}$. Then $S_n\to\infty$, and $X^{S_n}$ is a local martingale bounded by $n$ (as $|X^{S_n}_t|\le V_{t\wedge S_n}\le n$), hence a martingale.

2. Fix $t$ and a subdivision $0=t_0<\dots<t_k=t$. Martingale increments are orthogonal, so
$$E\big[(X^{S_n}_t)^2\big]=\sum_iE\big[(X^{S_n}_{t_i}-X^{S_n}_{t_{i-1}})^2\big]\le E\Big[\max_i|X^{S_n}_{t_i}-X^{S_n}_{t_{i-1}}|\;V_{t\wedge S_n}\Big]\le n\,E\Big[\max_i|X^{S_n}_{t_i}-X^{S_n}_{t_{i-1}}|\Big].$$

3. Refine the subdivisions so the mesh tends to $0$. By continuity the maximum tends to $0$, and it is bounded by $n$, so dominated convergence gives $E[(X_t^{S_n})^2]=0$.

4. Hence $X_t^{S_n}=0$ a.s. for all $n$, and so $X_t=0$.

:::

This rules out reading $\int H\,dM$ as a Lebesgue–Stieltjes integral for a non-trivial continuous local martingale $M$ such as Brownian motion. It also makes the decomposition of a process into "continuous local martingale + finite variation" unique, which is what allows the integral against such a sum to be defined term by term (@def-semimartingale).
