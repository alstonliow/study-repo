---
title: "The Stochastic Exponential and Girsanov's Theorem"
sources: [camiii-sc-3]
requires: [math/probability/stochastic-calculus/itos-formula]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part III Stochastic Calculus and Applications (lecture notes), Section 3.7, in our own wording; proofs written out in steps. -->

Girsanov's theorem describes what happens to martingales when the probability measure is changed by an exponential density.

::: {#exm-gaussian-shift .example name="Shifting a Gaussian by an exponential density"}

Let $X\sim N(0,C)$ in $\mathbb R^n$ with $C$ positive definite, $M=C^{-1}$, and $a\in\mathbb R^n$. Since the density of $N(a,C)$ is that of $N(0,C)$ times $\exp(-\tfrac12(a,Ma)+(x,Ma))$,
$$E[f(X+a)]=E[Z f(X)],\qquad Z=\exp\big(-\tfrac12(a,Ma)+(X,Ma)\big).$$
So the measure $\mathrm dQ=Z\,\mathrm dP$ makes $X$ a $N(a,C)$ variable. For Brownian motion and a deterministic drift $h$, applying this to $(B_{t_1},\dots,B_{t_n})$ and letting the partition refine gives the density $\exp\big(\int_0^th'\,dB-\frac12\int_0^th'^2\,ds\big)$ for the law of $B+h$ relative to that of $B$.

:::

::: {#def-stochastic-exponential .definition name="Stochastic exponential"}

For a continuous local martingale $M$, the *stochastic (Doléans–Dade) exponential* is
$$\mathcal E(M)_t=\exp\Big(M_t-\tfrac12\langle M\rangle_t\Big).$$

:::

::: {#prp-stochastic-exponential .proposition name="The stochastic exponential solves dZ = Z dM"}

For a continuous local martingale $M$ with $M_0=0$, $Z=\mathcal E(M)$ satisfies $Z_t=1+\int_0^tZ_s\,dM_s$; in particular it is a continuous local martingale. If $\langle M\rangle$ is uniformly bounded, $Z$ is a uniformly integrable martingale.

:::

::: {.proof}

1. Apply Itô's formula to $f(x,y)=e^{x-y/2}$ and the semi-martingale $(M,\langle M\rangle)$: $dZ=Z\,dM-\tfrac12Z\,d\langle M\rangle+\tfrac12Z\,d\langle M\rangle=Z\,dM$.

2. Hence $Z$ is a stochastic integral against a local martingale, hence a local martingale; it is non-negative, so a super-martingale.

3. If $\langle M\rangle\le c$, then $Z_t\le e^{M^*}$ with $M^*=\sup_t|M_t|$, and the exponential martingale inequality gives $\Pr(M^*\ge x)\le2e^{-x^2/2c}$. So $e^{M^*}\in L^1$, $Z$ is dominated by an integrable variable, and it is a uniformly integrable martingale by @cor-dominated-local-martingale.

:::

::: {#thm-girsanov .theorem name="Girsanov's theorem"}

Let $M$ be a continuous local martingale with $M_0=0$ such that $\mathcal E(M)$ is a uniformly integrable martingale, and define $\mathrm dQ/\mathrm dP=\mathcal E(M)_\infty$. If $X$ is a continuous local martingale under $P$, then $X-\langle X,M\rangle$ is a continuous local martingale under $Q$.

:::

::: {.proof}

Let $Z=\mathcal E(M)$ and $Y=X-\langle X,M\rangle$.

1. *$ZY$ is a $P$-local martingale.* By integration by parts, $d(ZY)=Z\,dY+Y\,dZ+d\langle Z,Y\rangle$. Here $dZ=Z\,dM$, $dY=dX-d\langle X,M\rangle$ and $d\langle Z,Y\rangle=Z\,d\langle M,X\rangle$. So $d(ZY)=Z\,dX-Z\,d\langle X,M\rangle+YZ\,dM+Z\,d\langle M,X\rangle=Z\,dX+YZ\,dM$, a stochastic integral against local martingales.

2. *Localise.* Let $T_n=\inf\{t:|Y_t|\ge n\}$ and let $(S_n)$ reduce $ZY$; put $R_n=T_n\wedge S_n$. Since $Q\ll P$, $R_n\to\infty$ $Q$-almost surely. The stopped process $Y^{R_n}$ is bounded and $Z^{R_n}Y^{R_n}=(ZY)^{R_n}$ is a $P$-martingale.

3. *$Y^{R_n}$ is a $Q$-martingale.* Let $T$ be a bounded stopping time. As $Z$ is uniformly integrable, $E_P[Z_\infty\mid\mathcal F_{T\wedge R_n}]=Z_{T\wedge R_n}$, so
$$E_Q[Y_{T\wedge R_n}]=E_P[Z_\infty Y_{T\wedge R_n}]=E_P[Z_{T\wedge R_n}Y_{T\wedge R_n}]=E_P[(ZY)^{R_n}_T]=E_P[Z_0Y_0]=0=E_Q[Y_0],$$
using optional stopping for the martingale $(ZY)^{R_n}$. By @thm-optional-stopping-continuous this shows $Y^{R_n}$ is a $Q$-martingale.

4. Hence $Y$ is a $Q$-local martingale.

:::

In particular, if $B$ is a $P$-Brownian motion and $M=\int h\,dB$ (with $\mathcal E(M)$ uniformly integrable), then $B-\int h\,ds$ is a $Q$-Brownian motion by Lévy's characterisation (@thm-levy-characterisation), because the bracket is unchanged by the change of measure: a drift can be added to or removed from a Brownian motion by changing the measure.

::: {#fig-girsanov-theorem-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0,0) -- (3,0);
\draw[faint] (4,0) -- (7,0);
\draw[emph] (0,0) -- (0.5,0.3) -- (1,-0.1) -- (1.5,0.2) -- (2,-0.2) -- (2.5,0.1) -- (3,-0.1);
\draw[emph] (4,0) -- (4.5,0.5) -- (5,0.3) -- (5.5,0.8) -- (6,0.7) -- (6.5,1.1) -- (7,1.0);
\draw[hl, dashed] (4,0) -- (7,1.1);
\node[lab] at (1.5,-0.7) {$B$ under $P$};
\node[lab] at (5.5,-0.7) {$B$ under $Q$: drift};
\draw[hl, ->] (3.2,0.4) -- (3.8,0.4);
\node[tick] at (3.5,0.7) {$\mathrm dQ=\mathcal E(M)\,\mathrm dP$};
\end{tikzpicture}
\end{center}
```

Weighting paths by the exponential density tilts the Brownian paths so that, under $Q$, $B$ acquires a drift $\langle B,M\rangle$ while $B-\langle B,M\rangle$ is again a Brownian motion.

:::
