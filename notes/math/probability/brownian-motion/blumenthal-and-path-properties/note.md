---
title: "Blumenthal's Zero-One Law and Path Properties"
sources: [camiii-ap-5]
requires: [math/probability/brownian-motion/definition-and-construction, math/probability/continuous-time/continuous-time-stopping-times]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part III Advanced Probability (lecture notes), Section 5.1, in our own wording; proofs written out in steps. -->

Brownian motion forgets its past in a strong sense: it is independent of the *slightly enlarged* past $\mathcal F_{s+}=\bigcap_{u>s}\mathcal F_u$, and consequently every germ event at time $0$ is trivial.

::: {#thm-independent-of-f-plus .theorem name="Independence from $\mathcal F_{s+}$"}

For every $s\ge0$, $(B_{t+s}-B_s)_{t\ge0}$ is independent of $\mathcal F^B_{s+}$.

:::

::: {.proof}

1. Take $s_n\downarrow s$ with $s_n>s$. By continuity, $B_{t+s}-B_s=\lim_n(B_{t+s_n}-B_{s_n})$ almost surely.

2. Each $(B_{t+s_n}-B_{s_n})_t$ is independent of $\mathcal F^B_{s_n}\supseteq\mathcal F^B_{s+}$ (simple Markov property). Almost sure limits of independent variables stay independent of $\mathcal F^B_{s+}$.

:::

::: {#thm-blumenthal .theorem name="Blumenthal's zero-one law"}

The σ-algebra $\mathcal F^B_{0+}$ is trivial: every $A\in\mathcal F^B_{0+}$ has $\Pr(A)\in\{0,1\}$.

:::

::: {.proof}

Take $s=0$ in @thm-independent-of-f-plus: $(B_t)_{t\ge0}$ is independent of $\mathcal F^B_{0+}$. But $A\in\mathcal F^B_{0+}\subseteq\sigma(B_t:t\ge0)$, so $A$ is independent of itself and $\Pr(A)\in\{0,1\}$.

:::

::: {#prp-brownian-path-properties .proposition name="Path properties"}

Let $B$ be a standard Brownian motion.

1. ($d=1$) Almost surely $\inf\{t>0:B_t>0\}=0$, $\inf\{t>0:B_t<0\}=0$ and $\inf\{t>0:B_t=0\}=0$: the path takes both signs and returns to $0$ immediately after time $0$.
2. $B_t/t\to0$ almost surely as $t\to\infty$ (any $d$).
3. ($d=1$) With $S_t=\sup_{s\le t}B_s$ and $I_t=\inf_{s\le t}B_s$: $S_\infty=+\infty$ and $I_\infty=-\infty$ almost surely.
4. If $A\subseteq\mathbb R^d$ is open and $C_A=\{tx:x\in A,\ t>0\}$ its cone, then $\inf\{t\ge0:B_t\in C_A\}=0$ almost surely.

:::

::: {.proof}

1. The event $\{\inf\{t>0:B_t>0\}=0\}=\bigcap_n\{\exists\,t\in(0,1/n):B_t>0\}$ is in $\mathcal F^B_{0+}$, hence has probability $0$ or $1$. For $t_n\downarrow0$, $\Pr(B_{t_n}>0)=\frac12$, and by Fatou $\Pr(B_{t_n}>0\text{ i.o.})\ge\limsup\Pr(B_{t_n}>0)=\frac12>0$, so the probability is $1$. The case $<0$ follows by symmetry; as the path is continuous and takes both signs arbitrarily close to $0$, it hits $0$.

2. $X_t=tB_{1/t}$ is a Brownian motion (@prp-brownian-invariance), so $B_t/t=X_{1/t}\to X_0=0$ as $t\to\infty$.

3. $S_\infty=aS_\infty$ in law for every $a>0$ (scaling), and $S_\infty$ is a tail-measurable $[0,\infty]$-valued variable; so it equals $0$ or $\infty$ a.s., and by 1 it is not $0$. By symmetry $I_\infty=-\infty$.

4. The event $\{\inf\{t:B_t\in C_A\}=0\}$ lies in $\mathcal F^B_{0+}$, and has positive probability (by scaling, $\Pr(B_t\in C_A)=\Pr(B_1\in C_A)>0$ for all $t$, as in 1), so probability $1$.

:::

::: {#rmk-brownian-chaotic .remark name="A chaotic path"}

By 3 the path oscillates between arbitrarily large positive and negative values and, by 1 and scaling, crosses every level it has visited infinitely often. By @thm-wiener the path is $\alpha$-Hölder for $\alpha<\frac12$; it is in fact nowhere differentiable (not proved in these lectures).

:::

::: {#fig-blumenthal-and-path-properties-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-0.2,0) -- (8.4,0) node[lab, right] {$t$};
\draw[->] (0,-1.6) -- (0,1.8);
\draw[emph] (0,0) -- (0.3,0.35) -- (0.55,-0.3) -- (0.9,0.5) -- (1.3,-0.55) -- (1.9,0.8) -- (2.6,-0.7) -- (3.6,1.2) -- (4.8,-1.0) -- (6.2,1.5) -- (8,-0.5);
\draw[hl] (0,0) -- (0.3,0.35) -- (0.55,-0.3) -- (0.9,0.5);
\node[lab, text=accent] at (2.2,1.5) {oscillates right after $t=0$ (zero-one law)};
\end{tikzpicture}
\end{center}
```

Immediately after time $0$ the path crosses $0$ infinitely often (thick part): for events about arbitrarily short initial segments, there is no randomness left in the answer.

:::
