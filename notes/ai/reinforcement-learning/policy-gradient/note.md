---
title: "Policy Gradient"
sources: [cs221-11]
requires: [ai/reinforcement-learning/model-free-rl, ai/machine-learning/softmax-regression]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 11 (imitation learning, policy gradient theorem, REINFORCE), in our own wording; proof written out in steps. -->

Model-based methods estimate the MDP and value-based methods estimate Q-values; both derive a policy at the end. *Policy-based* methods learn the policy directly. A policy is a classifier from states to actions, and as in classification (@prp-zero-one-loss-gradient) a hard choice gives no useful gradient, so the policy is made probabilistic.

::: {#def-stochastic-policy .definition name="Stochastic policy, imitation learning"}

A *stochastic policy* $\pi_\theta(a\mid s)$ is a probability distribution over $\text{Actions}(s)$ for each state, depending differentiably on parameters $\theta$ (for example a softmax of linear scores of features). Given an expert demonstration $s_0,a_0,s_1,a_1,\dots$, *imitation learning* maximizes the log-likelihood $\sum_t\log\pi_\theta(a_t\mid s_t)$, which is training a classifier on the examples $(s_t,a_t)$.

:::

Imitation learning needs demonstrations, such as teleoperated robot motions or worked solutions to maths problems. Reinforcement learning has only rewards. For a rollout $\tau=(s_0,a_0,r_0,s_1,\dots)$ with utility $u(\tau)$, following $\pi_\theta$ gives it probability

$$
p_\theta(\tau)=\prod_t\pi_\theta(a_t\mid s_t)\,T(s_t,a_t,s_{t+1}),
$$

and the goal is to maximize the expected utility $V(\theta)=E_{\tau\sim p_\theta}[u(\tau)]=\sum_\tau p_\theta(\tau)\,u(\tau)$.

::: {#thm-policy-gradient .theorem name="Policy gradient theorem"}

If every rollout ends after at most a fixed number of steps, then

$$
\nabla_\theta V(\theta)=E_{\tau\sim p_\theta}\Bigl[u(\tau)\sum_t\nabla_\theta\log\pi_\theta(a_t\mid s_t)\Bigr].
$$

:::

::: {.proof}

1. There are finitely many rollouts, so the gradient passes through the sum: $\nabla_\theta V(\theta)=\sum_\tau u(\tau)\,\nabla_\theta p_\theta(\tau)$, since $u(\tau)$ does not depend on $\theta$.

2. Wherever $p_\theta(\tau)>0$, $\nabla_\theta p_\theta(\tau)=p_\theta(\tau)\,\nabla_\theta\log p_\theta(\tau)$ (the *log-derivative trick*), so $\nabla_\theta V(\theta)=\sum_\tau p_\theta(\tau)\,u(\tau)\,\nabla_\theta\log p_\theta(\tau)=E_{\tau\sim p_\theta}\bigl[u(\tau)\nabla_\theta\log p_\theta(\tau)\bigr]$. Rollouts with $p_\theta(\tau)=0$ contribute nothing to either side, since a smooth non-negative function has zero gradient where it is $0$.

3. $\log p_\theta(\tau)=\sum_t\log\pi_\theta(a_t\mid s_t)+\sum_t\log T(s_t,a_t,s_{t+1})$, and the second sum does not depend on $\theta$, so $\nabla_\theta\log p_\theta(\tau)=\sum_t\nabla_\theta\log\pi_\theta(a_t\mid s_t)$.

:::

The transitions dropped out: the gradient can be estimated from rollouts without knowing the MDP. Sampling one rollout $\tau\sim p_\theta$ gives an unbiased estimate $u(\tau)\sum_t\nabla_\theta\log\pi_\theta(a_t\mid s_t)$ of $\nabla_\theta V(\theta)$ (but $u(\tau)\log p_\theta(\tau)$ is not an estimate of $V(\theta)$ itself).

::: {#def-reinforce .definition name="REINFORCE"}

*REINFORCE* repeatedly samples a rollout $\tau$ from the current policy $\pi_\theta$ and takes a gradient *ascent* step

$$
\theta\ \gets\ \theta+\eta\,u(\tau)\sum_t\nabla_\theta\log\pi_\theta(a_t\mid s_t).
$$

:::

```{=latex}
\begin{algorithm}
\caption{REINFORCE}
\begin{algorithmic}
\INPUT Environment, differentiable policy $\pi_\theta$, learning rate $\eta$, number of episodes $m$
\OUTPUT Parameters $\theta$
\FOR{$i=1$ \TO $m$}
    \STATE sample a rollout $s_0,a_0,r_0,s_1,\dots$ with $a_t\sim\pi_\theta(\cdot\mid s_t)$
    \STATE $u\gets\sum_t\gamma^tr_t$
    \STATE $\theta\gets\theta+\eta\,u\sum_t\nabla_\theta\log\pi_\theta(a_t\mid s_t)$
\ENDFOR
\RETURN $\theta$
\end{algorithmic}
\end{algorithm}
```

REINFORCE is imitation learning on the agent's own rollouts, each weighted by its utility; if utilities are $1$ for success and $0$ for failure, it imitates exactly its own successful rollouts. No separate exploration policy is needed, because a stochastic policy already explores.

::: {#exm-policy-gradient-1 .example name="One REINFORCE step on the flaky tram"}

On a flaky tram with $n=6$ and $\gamma=1$, suppose the rollout walks from $1$ to $2$ and from $2$ to $3$, then takes the tram from $3$ to $6$: rewards $-1,-1,-2$ and $u(\tau)=-4$. The REINFORCE step is

$$
\theta\gets\theta-4\eta\bigl(\nabla_\theta\log\pi_\theta(\text{walk}\mid1)+\nabla_\theta\log\pi_\theta(\text{walk}\mid2)+\nabla_\theta\log\pi_\theta(\text{tram}\mid3)\bigr),
$$

which makes all three actions less likely. A rollout with a less negative utility pushes its actions down less, so on average the better actions win (@thm-policy-gradient).

:::

::: {#fig-policy-gradient-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.6cm]
\foreach \i/\s in {0/1,1/2,2/3,3/6} { \node[small vertex] (s\i) at (\i,0) {$\s$}; }
\draw[->] (s0) -- node[edge label,above] {walk, $-1$} (s1);
\draw[->] (s1) -- node[edge label,above] {walk, $-1$} (s2);
\draw[->] (s2) -- node[edge label,above] {tram, $-2$} (s3);
\foreach \i in {0,1,2} { \node[lab] at ({\i+0.5},-0.55) {credit $-4$}; }
\begin{scope}[on background layer]\draw[hl box] (0.1,-0.8) rectangle (2.9,-0.3);\end{scope}
\end{tikzpicture}
\end{center}
```

The rollout of @exm-policy-gradient-1. REINFORCE gives every action the same credit, the utility $u(\tau)=-4$ of the whole rollout.

:::
