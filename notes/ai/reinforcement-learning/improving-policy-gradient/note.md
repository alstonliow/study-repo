---
title: "Improving Policy Gradient"
sources: [cs221-12]
requires: [ai/reinforcement-learning/policy-gradient]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 12 (credit assignment, future utility, baselines, actor-critic, PPO, GRPO), in our own wording. The unbiasedness proof for the future-utility estimator is our own; proofs written out in steps. The training runs in the second figure are our own (NumPy code in code.md). -->

REINFORCE is unbiased, but its gradient estimates are very noisy. Rewards may come long after the actions that earned them (a robot drops the potato only at the end; a maths solution is marked only at the final answer), and REINFORCE gives every action of a rollout the same credit $u(\tau)$. Finding which actions deserve the credit is the *credit assignment problem*. The improvements below keep the estimate (nearly) unbiased and lower its variance: an estimate $f-g$ has the same mean as $f$ whenever $E[g]=0$, and much smaller variance when $g$ tracks $f$.

::: {#def-future-utility-estimator .definition name="Future utility"}

The *future-utility* (reward-to-go) estimator of the policy gradient replaces $u(\tau)$ for step $t$ by the utility from step $t$ on, $u_t=\sum_{j\ge t}\gamma^{j-t}r_j$:

$$
\sum_t\gamma^t\,u_t\,\nabla_\theta\log\pi_\theta(a_t\mid s_t).
$$

:::

(With $\gamma=1$, as in all examples here, the factor $\gamma^t$ is $1$.)

::: {#lem-baseline .lemma name="Baselines have zero mean"}

For every state $s$ and every number $b$ not depending on the action,

$$
E_{a\sim\pi_\theta(\cdot\mid s)}\bigl[\nabla_\theta\log\pi_\theta(a\mid s)\;b\bigr]=0 .
$$

:::

::: {.proof}

1. $E_{a}\bigl[\nabla_\theta\log\pi_\theta(a\mid s)\bigr]=\sum_a\pi_\theta(a\mid s)\dfrac{\nabla_\theta\pi_\theta(a\mid s)}{\pi_\theta(a\mid s)}=\sum_a\nabla_\theta\pi_\theta(a\mid s)$.

2. This is $\nabla_\theta\sum_a\pi_\theta(a\mid s)=\nabla_\theta1=0$.

3. Multiplying by the constant $b$ keeps it $0$.

:::

::: {#thm-future-utility-unbiased .theorem name="Future utility and baselines are unbiased"}

Let $b$ be any function of the state. Under the hypothesis of @thm-policy-gradient,

$$
\nabla_\theta V(\theta)=E_{\tau\sim p_\theta}\Bigl[\sum_t\gamma^t\bigl(u_t-b(s_t)\bigr)\nabla_\theta\log\pi_\theta(a_t\mid s_t)\Bigr].
$$

:::

::: {.proof}

1. Write $g_t=\nabla_\theta\log\pi_\theta(a_t\mid s_t)$. By @thm-policy-gradient, $\nabla_\theta V=E\bigl[\sum_t\sum_j\gamma^jr_j\,g_t\bigr]$.

2. Fix $t$ and $j<t$. Condition on the history $h_t=(s_0,a_0,r_0,\dots,s_t)$, which determines $r_j$. Given $h_t$, the action $a_t$ is drawn from $\pi_\theta(\cdot\mid s_t)$, so by @lem-baseline (with $b=\gamma^jr_j$) $E[\gamma^jr_j\,g_t\mid h_t]=0$, hence $E[\gamma^jr_jg_t]=0$: an action earns no credit for earlier rewards.

3. Dropping these terms leaves $E\bigl[\sum_t\sum_{j\ge t}\gamma^jr_jg_t\bigr]=E\bigl[\sum_t\gamma^tu_tg_t\bigr]$.

4. In the same way $E[\gamma^tb(s_t)g_t\mid h_t]=0$ by @lem-baseline, since $b(s_t)$ is fixed by $h_t$; subtracting these terms does not change the expectation.

:::

::: {#def-advantage .definition name="Advantage, baseline"}

The *advantage* of action $a$ in state $s$ under a policy is $A(s,a)=Q(s,a)-V(s)$: how much better $a$ is than the policy's average action. A *baseline* $b(s)$, usually an estimate $\hat V(s)$ of the policy's value, gives the Monte Carlo advantage estimate $\hat A_t=u_t-b(s_t)$, and the policy gradient with baseline uses $\sum_t\gamma^t\hat A_t\,\nabla_\theta\log\pi_\theta(a_t\mid s_t)$.

:::

```{=latex}
\begin{algorithm}
\caption{Policy gradient with future utility and a baseline}
\begin{algorithmic}
\INPUT Environment, policy $\pi_\theta$, baseline $b$, learning rate $\eta$, number of episodes $m$
\OUTPUT Parameters $\theta$
\FOR{$i=1$ \TO $m$}
    \STATE sample a rollout $s_0,a_0,r_0,\dots,s_L$ from $\pi_\theta$
    \STATE $u_L\gets0$; \textbf{for} $t=L-1$ \textbf{down to} $0$: $u_t\gets r_t+\gamma u_{t+1}$
    \STATE $\theta\gets\theta+\eta\sum_{t<L}\gamma^t\bigl(u_t-b(s_t)\bigr)\nabla_\theta\log\pi_\theta(a_t\mid s_t)$
\ENDFOR
\RETURN $\theta$
\end{algorithmic}
\end{algorithm}
```

::: {#exm-improving-policy-gradient-1 .example name="Two game shows"}

1. *First show.* Step 1: door left ($10$ points) or right ($1$); step 2: left ($2$) or right ($1$). The policy is $\pi_\theta(\text{left}\mid s)=\sigma(\theta_s)$ for $s\in\{S,A\}$ (step 1, step 2), starting at $\theta=0$. In the rollout left, right, REINFORCE gives step 2's choice `right` credit $11$, mostly for the $10$ earned before it; future utility gives it credit $1$. Once step 1 reliably picks left, every rollout has utility $11$ or $12$ and REINFORCE pushes up whichever door step 2 happens to choose, so it can lock onto `right`. In $10$ runs of $100$ episodes with $\eta=0.1$, REINFORCE ended with probability of `left` in step 2 below $0.1$ in $6$ runs; with future utility every run ended between $0.81$ and $0.93$ (@fig-improving-policy-gradient-2).

2. *Second show.* Step 1: room A (left) or room B (right), $0$ points; in room A, left pays $11$ and right $10$; in room B, left pays $2$ and right $1$. Left is better by $1$ everywhere. Under the uniform policy $V(A)=10.5$, $V(B)=1.5$, $V(S)=6$, and at $\theta=0$, $\partial\log\pi/\partial\theta_s=\tfrac12$ for left and $-\tfrac12$ for right. Future utility pushes up whatever is sampled (all rewards are positive); a constant baseline $6$ helps in room A but hurts in room B; the state baseline $V(s_t)$ pushes `left` up in every state in every rollout (@fig-improving-policy-gradient-1).

:::

::: {#fig-improving-policy-gradient-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.45cm,y=0.5cm]
\node[lab] at (0,0) {rollout};
\node[lab] at (1.5,0.6) {future utility};
\node[lab] at (3.5,0.6) {baseline $6$};
\node[lab] at (5.5,0.6) {baseline $V(s_t)$};
\foreach \c in {1,3,5} { \node[lab] at (\c,0) {$\theta_S$}; \node[lab] at ({\c+1},0) {room}; }
\foreach \r/\name/\a/\b/\c/\d/\e/\f in {1/{L, L (11)}/5.5/5.5/2.5/2.5/2.5/0.25, 2/{L, R (10)}/5/-5/2/-2/2/0.25, 3/{R, L (2)}/-1/1/2/-2/2/0.25, 4/{R, R (1)}/-0.5/-0.5/2.5/2.5/2.5/0.25} {
  \node[lab] at (0,-\r) {\name};
  \node[lab] at (1,-\r) {$\a$}; \node[lab] at (2,-\r) {$\b$};
  \node[lab] at (3,-\r) {$\c$}; \node[lab] at (4,-\r) {$\d$};
  \node[lab] at (5,-\r) {$\e$}; \node[lab] at (6,-\r) {$\f$};
}
\begin{scope}[on background layer]\draw[hl box] (4.6,-4.5) rectangle (6.4,-0.5);\end{scope}
\end{tikzpicture}
\end{center}
```

The second game show of @exm-improving-policy-gradient-1: for each of the four rollouts (doors and utility), the estimated gradient with respect to $\theta_S$ and to $\theta$ of the room visited, at $\theta=0$. Positive means `left` is pushed up. Only the state-dependent baseline (boxed) pushes `left` up everywhere.

:::

::: {#fig-improving-policy-gradient-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=5cm,y=0.6cm]
\draw[->] (0,0) -- (1.08,0) node[lab,anchor=north east] {$\pi_\theta(\text{left}\mid A)$ after training};
\foreach \x in {0,0.5,1} { \node[lab,tick] at (\x,-0.4) {\x}; }
\node[lab,anchor=east] at (-0.03,1) {REINFORCE};
\node[lab,anchor=east] at (-0.03,2) {future utility};
\foreach \p in {0.89,0.97,0.08,0.99,0.01,0.02,0.04,0.01,0.01,0.98} { \node[dot] at (\p,1) {}; }
\foreach \p in {0.81,0.89,0.89,0.86,0.9,0.86,0.84,0.88,0.93,0.81} { \node[hl dot] at (\p,2) {}; }
\end{tikzpicture}
\end{center}
```

Ten training runs on the first game show of @exm-improving-policy-gradient-1 ($100$ episodes, $\eta=0.1$): final probability of the better door in step 2. REINFORCE locks onto the wrong door in most runs; the future-utility estimator does not.

:::

::: {#def-actor-critic .definition name="Actor-critic"}

An *actor-critic* method learns two things at once: the *actor*, the policy $\pi_\theta$, and the *critic*, value estimates $\hat V$ (and $\hat Q$), for example by TD learning (@sec-ai-reinforcement-learning-td-learning). The actor is updated with the critic's advantage estimates in place of $u_t-b(s_t)$, such as $\hat A_t=\hat Q(s_t,a_t)-\hat V(s_t)$ or the bootstrapped $\hat A_t=r_t+\gamma\hat V(s_{t+1})-\hat V(s_t)$, so it can update after every step rather than at the end of a rollout.

:::

```{=latex}
\begin{algorithm}
\caption{One-step actor-critic}
\begin{algorithmic}
\INPUT Environment, policy $\pi_\theta$, value function $\hat V_w$, learning rates $\eta,\beta$, number of episodes $m$
\OUTPUT Parameters $\theta,w$
\FOR{$i=1$ \TO $m$}
    \STATE $s\gets s_{\text{start}}$
    \WHILE{not $\text{IsEnd}(s)$}
        \STATE sample $a\sim\pi_\theta(\cdot\mid s)$; take it; observe $r,s'$
        \STATE $\delta\gets r+\gamma\hat V_w(s')-\hat V_w(s)$ \COMMENT{with $\hat V_w(s')=0$ at an end state}
        \STATE $w\gets w+\beta\,\delta\,\nabla_w\hat V_w(s)$ \COMMENT{critic: TD learning}
        \STATE $\theta\gets\theta+\eta\,\delta\,\nabla_\theta\log\pi_\theta(a\mid s)$ \COMMENT{actor}
        \STATE $s\gets s'$
    \ENDWHILE
\ENDFOR
\RETURN $\theta,w$
\end{algorithmic}
\end{algorithm}
```

The critic removes the luck of later random events from the credit (in a game show with a door followed by a spin of a wheel, the door is judged by its average outcome over spins, not by the spin that happened), at the cost of bias while $\hat V$ and $\hat Q$ are inaccurate.

::: {#def-ppo .definition name="Proximal policy optimization"}

*Proximal policy optimization* (PPO) is an actor-critic method that reuses each batch of rollouts, collected with parameters $\theta_{\text{old}}$, for several gradient steps. Since the data then come from a different policy, each term is reweighted by the ratio $\rho_t(\theta)=\pi_\theta(a_t\mid s_t)/\pi_{\theta_{\text{old}}}(a_t\mid s_t)$, and the ratio is clipped so that the policy cannot move far from the one that generated the data. It maximizes

$$
\sum_t\min\Bigl(\rho_t(\theta)\hat A_t,\ \operatorname{clip}\bigl(\rho_t(\theta),1-\varepsilon,1+\varepsilon\bigr)\hat A_t\Bigr).
$$

:::

::: {#def-grpo .definition name="Group-relative advantages (GRPO)"}

When the environment can be reset to the same state, as for a language model answering a prompt $x$ (state: prompt and tokens so far; action: next token; reward only at the end, say $1$ if a verifier accepts the answer), advantages can be estimated without a critic. Sample $G$ responses with utilities $u_1,\dots,u_G$ and use the leave-one-out advantage $\hat A_i=u_i-\frac{1}{G-1}\sum_{j\ne i}u_j$, or the normalized $\hat A_i=(u_i-\operatorname{mean}(u))/\operatorname{std}(u)$ of *group relative policy optimization* (GRPO). Every token of response $i$ gets credit $\hat A_i$:

$$
\theta\gets\theta+\eta\,\frac1G\sum_{i=1}^{G}\hat A_i\sum_t\nabla_\theta\log\pi_\theta(y_{i,t}\mid x,y_{i,<t}).
$$

:::

```{=latex}
\begin{algorithm}
\caption{Policy gradient with group-relative advantages}
\begin{algorithmic}
\INPUT Prompts, policy $\pi_\theta$, reward function, group size $G$, learning rate $\eta$
\OUTPUT Parameters $\theta$
\FOR{each prompt $x$}
    \STATE sample responses $y_1,\dots,y_G\sim\pi_\theta(\cdot\mid x)$; $u_i\gets$ reward of $y_i$
    \STATE $\hat A_i\gets(u_i-\operatorname{mean}(u))/\operatorname{std}(u)$ for $i=1,\dots,G$
    \STATE $\theta\gets\theta+\eta\,\frac1G\sum_i\hat A_i\sum_t\nabla_\theta\log\pi_\theta(y_{i,t}\mid x,y_{i,<t})$
\ENDFOR
\RETURN $\theta$
\end{algorithmic}
\end{algorithm}
```

::: {#rmk-improving-policy-gradient-1 .remark editor="No separate figures for actor-critic and GRPO: both only change where the advantage comes from, and the first figure already compares credits with and without a state-dependent baseline; a run on a language model cannot be drawn on a page."}

The leave-one-out baseline does not depend on response $i$'s own actions, so it keeps the estimate unbiased (@lem-baseline); dividing by the group's standard deviation puts easy and hard prompts on the same scale but adds a small bias. Full GRPO also clips the update as in PPO and penalizes moving far from the original model.

:::
