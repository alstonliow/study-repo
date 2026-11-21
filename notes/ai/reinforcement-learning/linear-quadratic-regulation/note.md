---
title: "Finite-Horizon MDPs and the Linear Quadratic Regulator"
sources: [cs229-20]
requires: [ai/reinforcement-learning/continuous-state-mdps, ai/reinforcement-learning/policy-iteration, math/linear-algebra/matrix-methods/matrix-derivatives]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS229 lecture notes (version of 23 August 2026), Chapter 20.1-20.2 (finite-horizon MDPs, non-stationary policies, dynamic programming backwards in time, the LQR model, the Riccati recursion, independence of the policy from the noise), in our own wording. We write LQR with costs to be minimized (CS229 uses negative rewards to be maximized; the two are the same up to sign). The derivation by completing the square and the scalar example with its golden-ratio limit are our own, checked in Python. Proofs written out in steps. -->

When the task has a fixed number of steps (land the aircraft within $T$ seconds), the best action depends on how much time is left, and the discount factor is no longer needed.

::: {#def-finite-horizon-mdp .definition name="Finite-horizon MDP"}

A *finite-horizon MDP* has states $S$, actions $A$, transition distributions $T_t(s,a,\cdot)$ and rewards $\text{Reward}_t(s,a)$ that may depend on the time $t$, and a *horizon* $T$. A *non-stationary policy* is a sequence $\pi_0,\dots,\pi_{T-1}$ with $a_t=\pi_t(s_t)$, and its utility is $\sum_{t=0}^{T-1}\text{Reward}_t(s_t,a_t)+\text{Reward}_T(s_T)$, with no discount.

:::

::: {#thm-finite-horizon-dp .theorem name="Dynamic programming backwards in time"}

Define $V_T^\star(s)=\text{Reward}_T(s)$ and, for $t=T-1,\dots,0$,

$$
V_t^\star(s)=\max_a\Bigl(\text{Reward}_t(s,a)+E_{s'\sim T_t(s,a,\cdot)}\bigl[V_{t+1}^\star(s')\bigr]\Bigr),
$$

with $\pi_t^\star(s)$ a maximizing action. Then $V_t^\star(s)$ is the largest expected utility of the remaining steps from state $s$ at time $t$, and the non-stationary policy $\pi^\star$ attains it.

:::

::: {.proof}

1. Induct backwards on $t$. At $t=T$ nothing remains but the final reward, so $V_T^\star$ is correct.

2. Suppose $V_{t+1}^\star$ is the best expected remaining utility from every state at time $t+1$. From state $s$ at time $t$, any policy takes some action $a$, collects $\text{Reward}_t(s,a)$ and moves to a random $s'$; by the Markov property, what it collects afterwards is at most $V_{t+1}^\star(s')$ in expectation, and $\pi^\star$ collects exactly that.

3. So every policy collects at most $\text{Reward}_t(s,a)+E[V_{t+1}^\star(s')]$ for its action $a$, which is at most $V_t^\star(s)$, and $\pi^\star$ attains the maximum.

:::

This is the time-limited value of @prp-time-limited-values computed for each remaining time separately; the optimal policy is generally non-stationary.

::: {#def-lqr .definition name="Linear quadratic regulator"}

The *linear quadratic regulator* (LQR) problem has states $s_t\in\mathbb{R}^n$, actions $a_t\in\mathbb{R}^m$, *linear dynamics*

$$
s_{t+1}=As_t+Ba_t+w_t,\qquad w_t\sim N(\mathbf{0},\Sigma_w)\ \text{independent},
$$

and *quadratic costs* to be minimized,

$$
\sum_{t=0}^{T-1}\bigl(s_t^{\mathsf T}Us_t+a_t^{\mathsf T}Wa_t\bigr)+s_T^{\mathsf T}Us_T,
$$

with $U$ positive semidefinite and $W$ positive definite. (This is a finite-horizon MDP with $\text{Reward}=-\text{cost}$.) For example $U=I$, $W=I$ asks to drive the state to $\mathbf{0}$ without large actions.

:::

::: {#thm-lqr-riccati .theorem name="The LQR solution: the Riccati recursion"}

Let $P_T=U$, $q_T=0$ and, for $t=T-1,\dots,0$,

$$
\begin{aligned}
K_t&=(W+B^{\mathsf T}P_{t+1}B)^{-1}B^{\mathsf T}P_{t+1}A,\\
P_t&=U+A^{\mathsf T}P_{t+1}A-A^{\mathsf T}P_{t+1}B\,(W+B^{\mathsf T}P_{t+1}B)^{-1}B^{\mathsf T}P_{t+1}A,\\
q_t&=q_{t+1}+\operatorname{tr}(\Sigma_wP_{t+1}).
\end{aligned}
$$

Then the optimal expected cost-to-go is $J_t(s)=s^{\mathsf T}P_ts+q_t$, with each $P_t$ positive semidefinite, and the optimal action is linear in the state: $a_t^\star=-K_ts_t$.

:::

::: {.proof}

1. Apply @thm-finite-horizon-dp with costs: $J_T(s)=s^{\mathsf T}Us$ and $J_t(s)=\min_a\bigl(s^{\mathsf T}Us+a^{\mathsf T}Wa+E[J_{t+1}(As+Ba+w)]\bigr)$. Induct backwards on $t$; the claim holds at $t=T$.

2. Suppose $J_{t+1}(s)=s^{\mathsf T}P_{t+1}s+q_{t+1}$ with $P=P_{t+1}$ positive semidefinite. Since $w$ has mean $\mathbf{0}$ and covariance $\Sigma_w$, for $\mathbf{m}=As+Ba$,

   $$
   E\bigl[(\mathbf{m}+w)^{\mathsf T}P(\mathbf{m}+w)\bigr]=\mathbf{m}^{\mathsf T}P\mathbf{m}+E[w^{\mathsf T}Pw]=\mathbf{m}^{\mathsf T}P\mathbf{m}+\operatorname{tr}(\Sigma_wP).
   $$

3. So the quantity to minimize over $a$ is $a^{\mathsf T}Ma+2a^{\mathsf T}\mathbf{g}+s^{\mathsf T}(U+A^{\mathsf T}PA)s+\operatorname{tr}(\Sigma_wP)+q_{t+1}$ with $M=W+B^{\mathsf T}PB$ and $\mathbf{g}=B^{\mathsf T}PAs$.

4. $M$ is positive definite because $W$ is and $B^{\mathsf T}PB$ is positive semidefinite. Completing the square, $a^{\mathsf T}Ma+2a^{\mathsf T}\mathbf{g}=(a+M^{-1}\mathbf{g})^{\mathsf T}M(a+M^{-1}\mathbf{g})-\mathbf{g}^{\mathsf T}M^{-1}\mathbf{g}$, minimized exactly at $a=-M^{-1}\mathbf{g}=-K_ts$.

5. The minimum value is $s^{\mathsf T}\bigl(U+A^{\mathsf T}PA-A^{\mathsf T}PBM^{-1}B^{\mathsf T}PA\bigr)s+q_{t+1}+\operatorname{tr}(\Sigma_wP)=s^{\mathsf T}P_ts+q_t$.

6. $P_t$ is positive semidefinite because $J_t(s)-q_t=s^{\mathsf T}P_ts$ is a minimum of non-negative costs.

:::

::: {#exm-lqr-scalar .example name="A scalar regulator and the golden ratio"}

Take $n=m=1$ and $A=B=U=W=1$: $s_{t+1}=s_t+a_t+w_t$ with cost $s_t^2+a_t^2$ per step. The recursion is $P_t=1+P_{t+1}-P_{t+1}^2/(1+P_{t+1})$ and $K_t=P_{t+1}/(1+P_{t+1})$. Starting from $P_T=1$:

| steps to go | $1$ | $2$ | $3$ | $4$ | $5$ |
|---|---|---|---|---|---|
| $P$ | $3/2$ | $8/5$ | $21/13$ | $55/34$ | $144/89$ |
| gain $K$ | $1/2$ | $3/5$ | $8/13$ | $21/34$ | $55/89$ |

The entries are ratios of Fibonacci numbers, and as the horizon grows $P$ tends to the fixed point of $P=1+P-P^2/(1+P)$, that is $P^2=P+1$, the golden ratio $\varphi\approx1.618$, while the gain tends to $\varphi/(1+\varphi)=1/\varphi\approx0.618$. With one step to go the regulator cancels half of the state; with a long horizon it cancels about $62\%$ of it each step.

:::

::: {#fig-linear-quadratic-regulation-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.9cm,y=0.8cm]
\draw[->] (0,0) -- (6.5,0) node[lab,anchor=west] {steps to go};
\draw[->] (0,0) -- (0,3.6) node[lab,anchor=south] {$P$};
\draw[faint] (0,3.236) -- (6.2,3.236) node[lab,anchor=south east] {$\varphi\approx1.618$};
\node[dot] at (0,2.000) {};
\draw[tick] (0,0) -- (0,-0.1) node[lab,anchor=north] {$0$};
\node[dot] at (1,3.000) {};
\draw[tick] (1,0) -- (1,-0.1) node[lab,anchor=north] {$1$};
\node[dot] at (2,3.200) {};
\draw[tick] (2,0) -- (2,-0.1) node[lab,anchor=north] {$2$};
\node[dot] at (3,3.231) {};
\draw[tick] (3,0) -- (3,-0.1) node[lab,anchor=north] {$3$};
\node[dot] at (4,3.235) {};
\draw[tick] (4,0) -- (4,-0.1) node[lab,anchor=north] {$4$};
\node[dot] at (5,3.236) {};
\draw[tick] (5,0) -- (5,-0.1) node[lab,anchor=north] {$5$};
\node[dot] at (6,3.236) {};
\draw[tick] (6,0) -- (6,-0.1) node[lab,anchor=north] {$6$};
\draw[tick] (0,2) -- (-0.1,2) node[lab,anchor=east] {$1$};
\draw[tick] (0,3.0) -- (-0.1,3.0) node[lab,anchor=east] {$1.5$};
\end{tikzpicture}
\end{center}
```

The Riccati recursion of @exm-lqr-scalar: the cost-to-go coefficient $P$ with $0,1,\dots,6$ steps to go, converging to the golden ratio.

:::

::: {#rmk-lqr-1 .remark name="Noise and the steady state"}

The noise covariance $\Sigma_w$ enters only the constants $q_t$, never $K_t$: the optimal LQR policy is the same as for the deterministic system $s_{t+1}=As_t+Ba_t$ (*certainty equivalence*). For long horizons $P_t$ usually converges to a fixed point of the recursion (the *discrete algebraic Riccati equation*), and the constant gain it gives is used as a stationary policy. Each backward step costs $O(n^3+m^3)$ operations, independent of any discretization, so LQR handles state dimensions far beyond the reach of @def-discretization.

:::
