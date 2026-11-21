---
title: "Nonlinear Control: Linearization and Differential Dynamic Programming"
sources: [cs229-20]
requires: [ai/reinforcement-learning/linear-quadratic-regulation]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS229 lecture notes (version of 23 August 2026), Chapter 20.3 (linearization of dynamics around a point and along a trajectory, differential dynamic programming), in our own wording. The time-varying LQR proposition and the pendulum-style example are our own; proof written out in steps. -->

Real dynamics are rarely linear. LQR still applies near a point or a trajectory where the dynamics are close to their first-order Taylor approximation.

::: {#def-linearized-dynamics .definition name="Linearized dynamics"}

Let $s_{t+1}=f(s_t,a_t)$ with $f$ differentiable. Around a reference state and action $(\bar s,\bar a)$,

$$
s_{t+1}\approx f(\bar s,\bar a)+\nabla_sf(\bar s,\bar a)\,(s_t-\bar s)+\nabla_af(\bar s,\bar a)\,(a_t-\bar a),
$$

where $\nabla_sf$ and $\nabla_af$ are the Jacobian matrices (@def-jacobian). Along a reference *trajectory* $(\bar s_t,\bar a_t)_{t=0}^{T}$ with $\bar s_{t+1}=f(\bar s_t,\bar a_t)$, the deviations $\delta s_t=s_t-\bar s_t$ and $\delta a_t=a_t-\bar a_t$ approximately satisfy the time-varying linear dynamics

$$
\delta s_{t+1}=A_t\,\delta s_t+B_t\,\delta a_t,\qquad A_t=\nabla_sf(\bar s_t,\bar a_t),\quad B_t=\nabla_af(\bar s_t,\bar a_t).
$$

:::

::: {#exm-linearized-pendulum .example name="Linearizing a swinging system"}

Let $s_{t+1}=s_t+0.1\sin s_t+a_t$ (one-dimensional, a crude pendulum-like system). Around $\bar s=0$ the linearization is $s_{t+1}\approx1.1\,s_t+a_t$: an unstable linear system that LQR can stabilize. Around $\bar s=\pi$ it is $s_{t+1}\approx\pi+0.9\,(s_t-\pi)+a_t$, stable on its own. The same non-linear system gives very different local models, so a controller designed at one point is trustworthy only near it.

:::

::: {#prp-time-varying-lqr .proposition name="Time-varying LQR"}

If the matrices of @def-lqr depend on time, $s_{t+1}=A_ts_t+B_ta_t+w_t$ with stage costs $s_t^{\mathsf T}U_ts_t+a_t^{\mathsf T}W_ta_t$, then the recursion of @thm-lqr-riccati with $A,B,U,W$ replaced by $A_t,B_t,U_t,W_t$ (using $P_{t+1}$ at step $t$) gives the optimal cost-to-go and the optimal policy $a_t^\star=-K_ts_t$.

:::

::: {.proof}

1. The proof of @thm-lqr-riccati treats each step $t$ separately: it uses only the dynamics and cost at step $t$ and the form of $J_{t+1}$.

2. Repeating its steps 2–6 with $A_t,B_t,U_t,W_t$ in place of $A,B,U,W$ gives the claim.

:::

Affine terms (a constant in the dynamics, or linear terms in the cost from a Taylor expansion) are handled by appending a constant coordinate $1$ to the state, which keeps the problem in LQR form.

::: {#def-ddp .definition name="Differential dynamic programming"}

*Differential dynamic programming* (DDP) improves a control sequence for non-linear dynamics $f$ and a smooth cost by repeating:

1. Start from a nominal trajectory $(\bar s_t,\bar a_t)$, for instance from a simple hand-designed controller run in the simulator.
2. Linearize the dynamics along it (@def-linearized-dynamics) and expand the cost to second order in $(\delta s_t,\delta a_t)$, giving a time-varying LQR problem in the deviations.
3. Solve it by @prp-time-varying-lqr, obtaining $\delta a_t=-K_t\,\delta s_t$ (plus a constant from the affine terms).
4. Run the new policy $a_t=\bar a_t+\delta a_t$ in the simulator from $s_0$ to get a new nominal trajectory.

:::

```{=latex}
\begin{algorithm}
\caption{Differential dynamic programming}
\begin{algorithmic}
\INPUT Dynamics $f$, cost, start state $s_0$, initial actions $\bar a_0,\dots,\bar a_{T-1}$
\REPEAT
    \STATE roll out $\bar s_{t+1}=f(\bar s_t,\bar a_t)$ from $\bar s_0=s_0$
    \FOR{$t=0,\dots,T-1$}
        \STATE $A_t\gets\nabla_sf(\bar s_t,\bar a_t)$, $B_t\gets\nabla_af(\bar s_t,\bar a_t)$
        \STATE expand the stage cost to second order at $(\bar s_t,\bar a_t)$
    \ENDFOR
    \STATE solve the time-varying LQR problem for gains $K_t$ and offsets
    \STATE $\bar a_t\gets\bar a_t+\delta a_t$ with $\delta a_t$ from the LQR policy along the new rollout
\UNTIL{the trajectory stops changing}
\RETURN the policy $a_t=\bar a_t-K_t(s_t-\bar s_t)$
\end{algorithmic}
\end{algorithm}
```

::: {#rmk-ddp-1 .remark name="A local method" editor="No figure: a candidate is the nominal trajectory of the example system before and after a few DDP iterations, which needs a numerical run."}

Each iteration of DDP is cheap and exact for its local model, and close to a good trajectory it converges quickly (it is closely related to Newton's method on the sequence of actions). Far from one, the linearization can mislead and the new trajectory can be worse, so practical versions limit the step (for example by mixing the old and new actions). The variant that ignores second derivatives of the dynamics is often called *iterative LQR*.

:::
