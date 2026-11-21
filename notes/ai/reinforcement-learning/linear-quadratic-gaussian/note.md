---
title: "Partial Observability and Linear Quadratic Gaussian Control"
sources: [cs229-20]
requires: [ai/reinforcement-learning/linear-quadratic-regulation, math/probability/estimation/kalman-filter]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS229 lecture notes (version of 23 August 2026), Chapter 20.4 (partially observable MDPs, belief states, the LQG model, the Kalman filter in vector form, the policy a = -K times the state estimate), in our own wording. The separation theorem is stated without proof, as in the source. The scalar Kalman filter and its derivation are in @sec-math-probability-estimation-kalman-filter; this note uses the vector form. -->

So far the controller saw the true state. Usually it sees only noisy sensor readings, and must act on a belief about the state.

::: {#def-pomdp .definition name="Partially observable MDP, belief"}

A *partially observable MDP* (POMDP) is an MDP together with an observation $y_t$ drawn from a distribution $O(\,\cdot\mid s_t)$ that depends on the hidden state $s_t$. The controller sees $y_0,\dots,y_t$ and its own actions but not the states. Its *belief* at time $t$ is the conditional distribution of $s_t$ given everything it has seen. The belief is a sufficient summary of the past, so a POMDP is an MDP whose states are beliefs.

:::

::: {#def-lqg .definition name="LQG model"}

The *linear quadratic Gaussian* (LQG) problem is LQR (@def-lqr) with observations

$$
y_t=Cs_t+v_t,\qquad v_t\sim N(\mathbf{0},\Sigma_v)\ \text{independent of everything else},
$$

and a Gaussian initial state $s_0\sim N(s_{0\mid-1},\Sigma_{0\mid-1})$. The controller chooses $a_t$ from $y_0,\dots,y_t$.

:::

::: {#def-kalman-filter-vector .definition name="Kalman filter, vector form" related="thm-kalman-filter"}

For the LQG model, write $s_{t\mid t}$ and $\Sigma_{t\mid t}$ for the mean and covariance of $s_t$ given $y_0,\dots,y_t$, and $s_{t+1\mid t}$, $\Sigma_{t+1\mid t}$ for those of $s_{t+1}$ given the same data. The *Kalman filter* computes them recursively:

1. *Update* with the new observation $y_t$:
   $$
   G_t=\Sigma_{t\mid t-1}C^{\mathsf T}\bigl(C\Sigma_{t\mid t-1}C^{\mathsf T}+\Sigma_v\bigr)^{-1},\qquad s_{t\mid t}=s_{t\mid t-1}+G_t\bigl(y_t-Cs_{t\mid t-1}\bigr),\qquad \Sigma_{t\mid t}=(I-G_tC)\Sigma_{t\mid t-1}.
   $$
2. *Predict* through the dynamics with the chosen action $a_t$:
   $$
   s_{t+1\mid t}=As_{t\mid t}+Ba_t,\qquad \Sigma_{t+1\mid t}=A\Sigma_{t\mid t}A^{\mathsf T}+\Sigma_w.
   $$

All conditional distributions are Gaussian, so the belief is exactly $N(s_{t\mid t},\Sigma_{t\mid t})$. The covariances do not depend on the observations or actions and can be computed in advance.

:::

::: {#thm-lqg-separation .theorem name="Separation of estimation and control"}

For the LQG problem the optimal policy is

$$
a_t^\star=-K_t\,s_{t\mid t},
$$

where $K_t$ is the LQR gain of @thm-lqr-riccati for the fully observed problem and $s_{t\mid t}$ is the Kalman filter estimate.

:::

<!-- Proof not given in the source and not written out here (it rests on the belief being Gaussian with an action-independent covariance, which reduces the expected cost to an LQR problem in s_{t|t}); TODO if a control or estimation course supplies it. -->

::: {#rmk-lqg-1 .remark name="Why the problem separates"}

The optimal controller is built from two independent pieces: the best estimator (the Kalman filter, which does not depend on the costs) and the best fully observed controller (LQR, which does not depend on the observation noise), joined by plugging the estimate in for the state. This is special to linear dynamics, quadratic costs and Gaussian noise; in general POMDPs the best action may deliberately gather information, and computing optimal policies is intractable.

:::
