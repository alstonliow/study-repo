---
title: "Filtrations, Martingales and Optional Stopping"
sources: [camiii-ap-2]
requires: [math/probability/measure-theoretic/general-conditional-expectation]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part III Advanced Probability (lecture notes), Sections 2.1-2.2, in our own wording; proofs written out in steps. -->

A *filtration* records the information available at each time. A *martingale* is a process that cannot be predicted to go up or down given that information: a fair game. Stopping times are the strategies that decide when to quit using only the information so far. Throughout, $(\Omega,\mathcal F,\Pr)$ carries a filtration $(\mathcal F_n)_{n\ge0}$.

::: {#def-filtration .definition name="Filtration, adapted process"}

A *filtration* is a sequence of σ-algebras $\mathcal F_0\subseteq\mathcal F_1\subseteq\dots\subseteq\mathcal F$; put $\mathcal F_\infty=\sigma(\mathcal F_0,\mathcal F_1,\dots)$. A process $(X_n)_{n\ge0}$ is *adapted* if $X_n$ is $\mathcal F_n$-measurable for all $n$, and *integrable* if $X_n\in L^1$. The *natural filtration* of $(X_n)$ is $\mathcal F^X_n=\sigma(X_0,\dots,X_n)$; $X$ is adapted exactly when $\mathcal F^X_n\subseteq\mathcal F_n$.

:::

::: {#def-martingale .definition name="Martingale, super- and sub-martingale"}

An integrable adapted process $(X_n)_{n\ge0}$ is a *martingale* if

$$
E[X_n\mid\mathcal F_m]=X_m\qquad(n\ge m),
$$

a *super-martingale* if $E[X_n\mid\mathcal F_m]\le X_m$, and a *sub-martingale* if $E[X_n\mid\mathcal F_m]\ge X_m$.

:::

By the tower property it suffices to take $n=m+1$. $X$ is a super-martingale iff $-X$ is a sub-martingale, and a martingale is both; so results are proved for super-martingales and applied to $\pm X$.

::: {#exm-martingales-examples .example name="Basic examples"}

1. *Random walk.* If $\xi_k$ are independent with $E\xi_k=0$, then $S_n=\xi_1+\dots+\xi_n$ is a martingale for $\mathcal F_n=\sigma(\xi_1,\dots,\xi_n)$ (property 3 and linearity of @prp-conditional-expectation-properties).
2. *Product martingale.* If $\rho_k$ are i.i.d. with $\Pr(\rho_k=0)=\Pr(\rho_k=2)=\tfrac12$, then $X_n=\rho_1\cdots\rho_n$ is a martingale with $E[X_n]=1$ for all $n$.
3. *Harmonic functions.* If $(X_n)$ is a Markov chain with transition matrix $P$ on a countable set and $f$ is bounded with $Pf=f$, then $f(X_n)$ is a martingale: $E[f(X_{n+1})\mid\mathcal F_n]=(Pf)(X_n)=f(X_n)$.
4. *Closed martingale.* For $Z\in L^1$, $X_n=E[Z\mid\mathcal F_n]$ is a martingale, by the tower property.
5. A martingale need not be Markov: with $S_n$ as in 1, a bounded random variable $Z$ independent of the $\xi_k$ and $\mathcal F'_n=\sigma(\mathcal F_n,Z)$, the process $ZS_n$ is a martingale (take $Z$ out, @prp-conditional-expectation-properties), but in general not a Markov chain, since the hidden factor $Z$ affects the future increments.

:::

::: {#def-stopping-time .definition name="Stopping time"}

A *stopping time* is a map $T:\Omega\to\{0,1,2,\dots\}\cup\{\infty\}$ with $\{T\le n\}\in\mathcal F_n$ for all $n$. Equivalently $\{T=n\}\in\mathcal F_n$ for all $n$, because $\{T=n\}=\{T\le n\}\setminus\{T\le n-1\}$ and $\{T\le n\}=\bigcup_{k\le n}\{T=k\}$.

:::

For $B$ Borel, $T=\inf\{n:X_n\in B\}$ is a stopping time for an adapted $X$, while $\sup\{n:X_n\in B\}$ generally is not (it needs the future).

::: {#def-stopped-process .definition name="$X_T$, stopped process, $\mathcal F_T$"}

For a stopping time $T$ set $X_T(\omega)=X_{T(\omega)}(\omega)$ on $\{T<\infty\}$ (and $0$ there otherwise unless a limit $X_\infty$ is available). The *stopped process* is $X^T_n=X_{T\wedge n}$. The σ-algebra of events determined by time $T$ is

$$
\mathcal F_T=\{A\in\mathcal F_\infty:\ A\cap\{T\le n\}\in\mathcal F_n\ \text{for all }n\}.
$$

:::

::: {#prp-stopping-time-properties .proposition name="Elementary properties"}

1. If $S,T,T_n$ are stopping times, so are $S\vee T$, $S\wedge T$, $\sup_nT_n$, $\inf_nT_n$, $\limsup_nT_n$, $\liminf_nT_n$.
2. $\mathcal F_T$ is a σ-algebra, and $S\le T$ implies $\mathcal F_S\subseteq\mathcal F_T$; for constant $T\equiv n$, $\mathcal F_T=\mathcal F_n$.
3. $X_T\mathbf 1_{\{T<\infty\}}$ is $\mathcal F_T$-measurable.
4. If $X$ is adapted (resp. integrable), so is the stopped process $X^T$.

:::

These are routine checks from the definitions (for instance $\{\inf T_n<k\}=\bigcup_n\{T_n<k\}$ and $\{\sup T_n\le k\}=\bigcap_n\{T_n\le k\}$).

::: {#fig-martingales-and-stopping-times-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-0.2,0) -- (8.2,0) node[lab, right] {$n$};
\draw[faint] (0,2) -- (8,2);
\node[tick, left] at (0,2) {$b$};
\draw[emph] (0,0) -- (1,0.5) -- (2,1.0) -- (3,0.5) -- (4,1.0) -- (5,1.5) -- (6,2.0) -- (7,1.5) -- (8,2.0);
\draw[hl] (0,0) -- (1,0.5) -- (2,1.0) -- (3,0.5) -- (4,1.0) -- (5,1.5) -- (6,2.0) -- (8,2.0);
\draw[faint] (6,0) -- (6,2);
\node[tick] at (6,-0.3) {$T$};
\node[lab, text=accent] at (3.0,2.45) {$X^T_n$ (highlighted) freezes at $T=\inf\{n:X_n\ge b\}$};
\end{tikzpicture}
\end{center}
```

A stopping time decides by looking at the path so far: $T$ is the first time the walk reaches level $b$. The stopped process follows the walk up to $T$ and is constant afterwards.

:::

::: {#thm-optional-stopping-discrete .theorem name="Optional stopping theorem (bounded times)"}

Let $(X_n)$ be a super-martingale and $S\le T$ bounded stopping times. Then $E[X_T]\le E[X_S]$. For a martingale, $E[X_T]=E[X_S]$, and in particular $E[X_T]=E[X_0]$ for every bounded stopping time $T$.

:::

This is the special case (iv) of the following theorem. Boundedness cannot be dropped: for a walk with $X_0=0$ and $T=\inf\{n:X_n=1\}$ we have $E[X_T]=1\ne0=E[X_0]$, so $T$ is not bounded.

::: {#thm-optional-stopping-equivalences .theorem name="Characterisations of super-martingales"}

For an adapted integrable process $(X_n)$ the following are equivalent:

1. $X$ is a super-martingale.
2. For every bounded stopping time $T$ and every stopping time $S$, $E[X_T\mid\mathcal F_S]\le X_{S\wedge T}$.
3. For every stopping time $T$, the stopped process $X^T$ is a super-martingale.
4. $E[X_T]\le E[X_S]$ for all bounded stopping times $S\le T$.

:::

::: {.proof}

1. *(1)⇒(2).* Let $T\le n$. Then $X_T=X_{S\wedge T}+\sum_{k=0}^{n}(X_{k+1}-X_k)\mathbf 1_{\{S\le k<T\}}$. The event $\{S\le k<T\}=\{S\le k\}\cap\{T\le k\}^c$ lies in $\mathcal F_k$, and for $A\in\mathcal F_S$ also $A\cap\{S\le k<T\}\in\mathcal F_k$. Multiply by $\mathbf 1_A$ and take expectations: each term $E[(X_{k+1}-X_k)\mathbf 1_{A\cap\{S\le k<T\}}]\le0$ by the super-martingale property, so $E[X_T\mathbf 1_A]\le E[X_{S\wedge T}\mathbf 1_A]$ for all $A\in\mathcal F_S$.

2. Since $X_{S\wedge T}$ is $\mathcal F_{S\wedge T}\subseteq\mathcal F_S$-measurable, this gives $E[E[X_T\mid\mathcal F_S]\mathbf 1_A]\le E[X_{S\wedge T}\mathbf 1_A]$ for all $A\in\mathcal F_S$, which is (2).

3. *(2)⇒(3).* For $m\le n$ apply (2) with $S=m$ and the bounded time $T'\wedge n$: $E[X_{T'\wedge n}\mid\mathcal F_m]\le X_{m\wedge T'}$, which is the super-martingale property of $X^{T'}$.

4. *(3)⇒(1)* by taking $T=\infty$. *(2)⇒(4)* by taking expectations. 

5. *(4)⇒(1).* Fix $m\le n$ and $A\in\mathcal F_m$. Then $T=m\mathbf 1_A+n\mathbf 1_{A^c}$ is a stopping time bounded by $n$, with $X_T=X_m\mathbf 1_A+X_n\mathbf 1_{A^c}$. By (4) with $S=n$, $0\ge E[X_n]-E[X_T]=E[X_n\mathbf 1_A]-E[X_m\mathbf 1_A]$. Hence $E[E[X_n\mid\mathcal F_m]\mathbf 1_A]\le E[X_m\mathbf 1_A]$ for all $A\in\mathcal F_m$, i.e. $E[X_n\mid\mathcal F_m]\le X_m$.

:::

::: {#rmk-martingales-fair-game .remark name="Fair games"}

If $X_n$ is a gambler's wealth, the theorem says that no rule for quitting, as long as it is bounded and uses only the past, changes the expected final wealth of a fair game. Unbounded rules can fail (the example above); the uniformly integrable case is in @sec-math-probability-martingales-lp-and-l1-martingale-convergence.

:::
