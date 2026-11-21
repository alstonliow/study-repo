---
title: "Continuous State MDPs and Fitted Value Iteration"
sources: [cs229-19]
requires: [ai/reinforcement-learning/function-approximation]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS229 lecture notes (version of 23 August 2026), Chapter 19.3-19.4 (learning a model, simulators, discretization and the curse of dimensionality, value function approximation, fitted value iteration), in our own wording. The cell count example is our own. -->

A car, a helicopter or an inverted pendulum has a state made of real numbers (positions, angles, velocities). Value iteration (@def-value-iteration) needs a table with one entry per state, which no longer exists.

::: {#def-discretization .definition name="Discretization"}

To *discretize* a continuous state space $S\subseteq\mathbb{R}^d$, cover it by a grid of cells, treat each cell as one state of a finite MDP (estimating its transition probabilities from where the system goes from points in the cell), solve that MDP by value or policy iteration, and act in a continuous state $s$ by the policy of the cell that contains $s$.

:::

::: {#rmk-curse-of-dimensionality .remark name="The curse of dimensionality"}

Discretization approximates $V^\star$ by a function that is constant on each cell, which is crude unless the cells are small, and the number of cells grows exponentially with the dimension: $k$ cells per coordinate give $k^d$ states. With $k=100$, a $2$-dimensional state needs $10^4$ cells, but the $12$-dimensional state of a helicopter (position, orientation and their velocities) would need $10^{24}$. Discretization works well for $d\le2$ or $3$, and with care up to about $6$.

:::

::: {#def-mdp-simulator .definition name="Simulator, learned model"}

A *model* or *simulator* of an MDP is a procedure that takes a state $s_t$ and an action $a_t$ and returns a next state $s_{t+1}$ drawn from (an approximation of) the true transition distribution $T(s_t,a_t,\cdot)$. It may come from physics, from off-the-shelf simulation software, or be *learned* from logged trajectories: for example, fit a linear model

$$
s_{t+1}=As_t+Ba_t+\varepsilon_t
$$

by choosing $A,B$ to minimize $\sum_t\lVert s_{t+1}-(As_t+Ba_t)\rVert^2$ over the recorded transitions (least squares, @sec-ai-machine-learning-linear-regression), and model $\varepsilon_t$ as Gaussian noise with the covariance of the residuals. Setting $\varepsilon_t=0$ gives a *deterministic* model. Non-linear features $\phi(s_t,a_t)$ can replace $(s_t,a_t)$.

:::

::: {#def-fitted-value-iteration .definition name="Fitted value iteration"}

Choose a feature map $\phi(s)$ and approximate $V(s)\approx\boldsymbol\theta^{\mathsf T}\phi(s)$. Sample states $s^{(1)},\dots,s^{(m)}$, set $\boldsymbol\theta=\mathbf{0}$, and repeat:

1. For each $i$ and each action $a$, draw $k$ next states $s'_1,\dots,s'_k$ from the simulator at $(s^{(i)},a)$ and estimate
   $$
   q(a)=\frac1k\sum_{l=1}^k\bigl[\text{Reward}(s^{(i)},a)+\gamma\,\boldsymbol\theta^{\mathsf T}\phi(s'_l)\bigr].
   $$
2. Set the targets $y^{(i)}=\max_aq(a)$, an estimate of the value-iteration update at $s^{(i)}$.
3. Fit $\boldsymbol\theta=\operatorname{arg\,min}_{\boldsymbol\theta}\tfrac12\sum_i\bigl(\boldsymbol\theta^{\mathsf T}\phi(s^{(i)})-y^{(i)}\bigr)^2$ (or with any other regression method).

Act with the greedy policy $\pi(s)=\operatorname{arg\,max}_aE_{s'}\bigl[\text{Reward}(s,a)+\gamma\boldsymbol\theta^{\mathsf T}\phi(s')\bigr]$, estimating the expectation with samples from the simulator.

:::

```{=latex}
\begin{algorithm}
\caption{Fitted value iteration}
\begin{algorithmic}
\INPUT Sampled states $s^{(1)},\dots,s^{(m)}$, simulator, features $\phi$, samples per action $k$
\STATE $\boldsymbol\theta\gets\mathbf{0}$
\REPEAT
    \FOR{$i=1,\dots,m$}
        \FOR{each action $a$}
            \STATE draw $s'_1,\dots,s'_k$ from the simulator at $(s^{(i)},a)$
            \STATE $q(a)\gets\frac1k\sum_l\bigl[\text{Reward}(s^{(i)},a)+\gamma\,\boldsymbol\theta^{\mathsf T}\phi(s'_l)\bigr]$
        \ENDFOR
        \STATE $y^{(i)}\gets\max_aq(a)$
    \ENDFOR
    \STATE $\boldsymbol\theta\gets\operatorname{arg\,min}_{\boldsymbol\theta}\sum_i\bigl(\boldsymbol\theta^{\mathsf T}\phi(s^{(i)})-y^{(i)}\bigr)^2$
\UNTIL{$\boldsymbol\theta$ stops changing much}
\RETURN $\boldsymbol\theta$
\end{algorithmic}
\end{algorithm}
```

::: {#rmk-fitted-value-iteration-1 .remark name="What fitted value iteration does and does not guarantee" editor="No figure: fitted value iteration needs a simulator and features; a candidate is a one-dimensional value function after a few iterations on a toy system."}

Fitted value iteration is value iteration in which each update is evaluated only at sampled states and then generalized by supervised learning; with a deterministic simulator one sample, $k=1$, is enough. Exact value iteration converges because its update is a contraction (@thm-value-iteration), but composing that update with a regression step need not be one, so fitted value iteration has no general convergence guarantee, although it often works well in practice. Q-learning with function approximation (@def-q-function-approximation) is the model-free relative: it replaces the simulator by observed transitions.

:::
