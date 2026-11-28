---
title: "Lévy's Characterisation and the Dubins–Schwarz Theorem"
sources: [camiii-sc-3]
requires: [math/probability/stochastic-calculus/itos-formula, math/probability/brownian-motion/definition-and-construction]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part III Stochastic Calculus and Applications (lecture notes), Section 3.6, in our own wording; proofs written out in steps where given. -->

::: {#thm-levy-characterisation .theorem name="Lévy's characterisation of Brownian motion"}

Let $X^1,\dots,X^d$ be continuous local martingales with $X_0=0$ and $\langle X^i,X^j\rangle_t=\delta_{ij}t$. Then $(X^1,\dots,X^d)$ is a standard $d$-dimensional Brownian motion.

:::

::: {.proof}

It suffices to show that for $s<t$ the increment $X_t-X_s$ is independent of $\mathcal F_s$ and $N(0,(t-s)I)$-distributed, i.e. that $E[e^{i\langle\theta,X_t-X_s\rangle}\mid\mathcal F_s]=e^{-|\theta|^2(t-s)/2}$ for $\theta\in\mathbb R^d$.

1. Apply Itô's formula (complex-valued version, real and imaginary parts separately) to $F(X)=e^{i\langle\theta,X\rangle}$: since $d\langle X^j,X^k\rangle=\delta_{jk}dt$,
$$F(X_t)-F(X_s)=i\sum_j\theta_j\int_s^tF(X_r)\,dX^j_r-\frac{|\theta|^2}2\int_s^tF(X_r)\,dr .$$

2. The stochastic integrals are martingales because $|F|=1$ is bounded. So for $A\in\mathcal F_s$, $\varphi(t)=E[F(X_t)\overline{F(X_s)}\mathbf 1_A]$ satisfies $\varphi(t)=\Pr(A)-\frac{|\theta|^2}2\int_s^t\varphi(r)\,dr$.

3. This linear integral equation has the unique solution $\varphi(t)=\Pr(A)e^{-|\theta|^2(t-s)/2}$. Hence $E[e^{i\langle\theta,X_t-X_s\rangle}\mathbf 1_A]=\Pr(A)e^{-|\theta|^2(t-s)/2}$ for all $A\in\mathcal F_s$, which is the claim.

:::

This is useful because for a stochastic integral $\langle H\cdot B\rangle=H^2\cdot\langle B\rangle$, so quadratic variations of integrals against Brownian motion are explicit.

::: {#thm-dubins-schwarz .theorem name="Dubins–Schwarz"}

Let $M$ be a continuous local martingale with $M_0=0$ and $\langle M\rangle_\infty=\infty$. Put $T_s=\inf\{t\ge0:\langle M\rangle_t>s\}$, $B_s=M_{T_s}$ and $\mathcal G_s=\mathcal F_{T_s}$. Then each $T_s$ is a stopping time, $\langle M\rangle_{T_s}=s$, $B$ is a $(\mathcal G_s)$-Brownian motion, and $M_t=B_{\langle M\rangle_t}$.

:::

*Proof omitted.* The argument shows that $B$ is a continuous local martingale with $\langle B\rangle_s=s$, so Lévy's characterisation applies; continuity of $B$ uses the lemma that $M$ is constant on an interval exactly when $\langle M\rangle$ is.

<!-- TODO: write out the proof (time change, constancy lemma for M and <M>, continuity of B, Lévy). -->

Every continuous local martingale is therefore a Brownian motion run on the clock $\langle M\rangle$.

::: {#fig-levy-and-dubins-schwarz-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0,0) -- (3,0);
\draw[faint] (4,0) -- (7,0);
\draw[emph] (0,0.5) -- (0.4,0.2) -- (0.8,0.9) -- (1.4,0.7) -- (1.9,1.4) -- (2.4,0.8) -- (3,1.1);
\draw[emph] (4,0.5) -- (5.0,0.2) -- (5.5,0.9) -- (6.0,0.7) -- (7,1.4);
\node[lab] at (1.5,-0.5) {$M_t$ in real time $t$};
\node[lab] at (5.5,-0.5) {$B_s$, $s=\langle M\rangle_t$};
\draw[hl, ->] (3.2,0.7) -- (3.8,0.7);
\node[tick] at (3.5,1.0) {clock};
\end{tikzpicture}
\end{center}
```

Rescaling time by the quadratic variation turns a continuous local martingale into a standard Brownian motion.

:::
