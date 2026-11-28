---
title: "Continuous-Time Stopping Times and Hitting Times"
sources: [camiii-ap-3]
requires: [math/probability/continuous-time/continuous-time-processes, math/probability/martingales/martingales-and-stopping-times]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part III Advanced Probability (lecture notes), Section 3, in our own wording; proofs written out in steps. -->

The discrete theory transfers to continuous time once we choose the filtration and the paths well. A new subtlety: whether a hitting time is a stopping time depends on whether the target set is closed or open.

::: {#def-continuous-filtration .definition name="Filtration and stopping time in continuous time"}

A *filtration* is a family $(\mathcal F_t)_{t\ge0}$ with $\mathcal F_s\subseteq\mathcal F_t\subseteq\mathcal F$ for $s\le t$; $\mathcal F_\infty=\sigma(\mathcal F_t:t\ge0)$. A random variable $T:\Omega\to[0,\infty]$ is a *stopping time* if $\{T\le t\}\in\mathcal F_t$ for all $t$. As before, $\mathcal F_T=\{A\in\mathcal F_\infty:A\cap\{T\le t\}\in\mathcal F_t\ \forall t\}$ and $X^T_t=X_{T\wedge t}$.

:::

::: {#prp-continuous-stopping-properties .proposition name="Properties of stopped cadlag processes"}

Let $X$ be cadlag and adapted and $S,T$ stopping times. Then

1. $S\wedge T$ is a stopping time;
2. $S\le T$ implies $\mathcal F_S\subseteq\mathcal F_T$;
3. $X_T\mathbf 1_{\{T<\infty\}}$ is $\mathcal F_T$-measurable;
4. the stopped process $X^T$ is adapted.

:::

::: {.proof}

Parts 1 and 2 are as in discrete time. For 3 we use the fact that $Z$ is $\mathcal F_T$-measurable iff $Z\mathbf 1_{\{T\le t\}}$ is $\mathcal F_t$-measurable for all $t$.

1. $X_T\mathbf 1_{\{T\le t\}}=X_T\mathbf 1_{\{T<t\}}+X_t\mathbf 1_{\{T=t\}}$ and the second term is $\mathcal F_t$-measurable, so it suffices to treat $X_T\mathbf 1_{\{T<t\}}$.

2. Let $T_n=2^{-n}\lceil2^nT\rceil\downarrow T$, a stopping time taking values in the dyadics. Since $X$ is cadlag (right-continuous), $X_T\mathbf 1_{\{T<t\}}=\lim_nX_{T_n\wedge t}\mathbf 1_{\{T<t\}}$.

3. $X_{T_n\wedge t}=\sum_{q\in D_n,\,q<t}X_q\mathbf 1_{\{T_n=q\}}+X_t\mathbf 1_{\{T<t<T_n\}}$ is $\mathcal F_t$-measurable, being a countable sum of measurable pieces; hence so is the limit. Part 4 is similar.

:::

::: {#def-continuous-hitting-time .definition name="Hitting time"}

For $A\in\mathcal B(\mathbb R)$ the *hitting time* of $A$ is $T_A=\inf\{t\ge0:X_t\in A\}$.

:::

::: {#exm-hitting-time-not-stopping .example name="A hitting time that is not a stopping time"}

Let $X_t=t$ with probability $\frac12$, and with probability $\frac12$ let $X_t=t$ for $t\le1$ and $X_t=2-t$ for $t>1$. Take $A=(1,\infty)$ (open). Then $T_A=1$ in the first case (the path enters $A$ immediately after time $1$) and $T_A=\infty$ in the second. At time $1$ the two paths are identical, so $\{T_A\le1\}\notin\mathcal F_1$ (natural filtration).

:::

::: {#prp-hitting-closed .proposition name="Closed sets"}

If $A$ is closed and $X$ is continuous and adapted, then $T_A$ is a stopping time.

:::

Indeed $d(X_q,A)$ is continuous in $q$, so $\{T_A\le t\}=\{\inf_{q\in\mathbb Q\cap[0,t]}d(X_q,A)=0\}$ (with $q=t$ included), which is $\mathcal F_t$-measurable.

::: {#def-usual-conditions .definition name="Right-continuous filtration, usual conditions"}

Put $\mathcal F_{t+}=\bigcap_{s>t}\mathcal F_s\supseteq\mathcal F_t$; the filtration is *right-continuous* if $\mathcal F_t=\mathcal F_{t+}$. Let $\mathcal N=\{A\in\mathcal F_\infty:\Pr(A)\in\{0,1\}\}$ (the null sets and their complements). The filtration satisfies the *usual conditions* if it is right-continuous and $\mathcal N\subseteq\mathcal F_0$.

:::

::: {#prp-hitting-open .proposition name="Open sets"}

If $X$ is cadlag and adapted and $A$ is open, then $T_A$ is a stopping time with respect to $(\mathcal F_{t+})$.

:::

::: {.proof}

1. By right-continuity of paths and openness of $A$, $\{T_A<t\}=\bigcup_{q<t,\,q\in\mathbb Q}\{X_q\in A\}\in\mathcal F_t$.

2. Then $\{T_A\le t\}=\bigcap_{n\ge1}\{T_A<t+1/n\}\in\bigcap_n\mathcal F_{t+1/n}=\mathcal F_{t+}$.

:::

::: {#fig-continuous-time-stopping-times-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-0.2,0) -- (7,0) node[lab, right] {$t$};
\draw[faint] (0,2) -- (7,2);
\node[tick, left] at (0,2) {$1$};
\draw[emph] (0,0) -- (2,2);
\draw[emph] (2,2) -- (4,2.0+2.0);
\draw[emph, dashed] (2,2) -- (4,0);
\draw[faint] (2,0) -- (2,2);
\node[tick] at (2,-0.3) {$1$};
\node[lab, text=accent] at (4.9,3.9) {goes on up: $T_A=1$};
\node[lab, text=accent] at (5.0,0.3) {turns back: $T_A=\infty$};
\end{tikzpicture}
\end{center}
```

For $A=(1,\infty)$ the two paths coincide up to time $1$, so whether $T_A\le1$ cannot be decided at time $1$: it needs $\mathcal F_{1+}$. For closed $A$ the hitting is visible at the moment it happens.

:::
