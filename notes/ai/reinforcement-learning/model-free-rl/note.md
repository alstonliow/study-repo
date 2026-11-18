---
title: "Model-Free Monte Carlo, SARSA and Q-Learning"
sources: [cs221-9]
requires: [ai/reinforcement-learning/model-based-rl]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 9 (model-free Monte Carlo, SARSA, Q-learning), in our own wording. The incremental-mean proposition is our own addition; proof written out in steps. -->

Model-free methods skip the estimated MDP and estimate Q-values directly; the policy is then $\epsilon$-greedy with respect to them (@def-epsilon-greedy). All three methods below have the same shape: a *model* $\hat Q(s_t,a_t)$, a *target* computed from experience, and an update that nudges the model towards the target,

$$
\hat Q(s_t,a_t)\ \gets\ \hat Q(s_t,a_t)-\eta\bigl(\hat Q(s_t,a_t)-\text{target}\bigr),
$$

with a learning rate $\eta\in(0,1]$. This is one step of gradient descent on the squared error $\tfrac12(\hat Q(s_t,a_t)-\text{target})^2$.

::: {#prp-incremental-mean .proposition name="Running average"}

If the $k$-th update of a value $\hat Q$ uses learning rate $\eta=1/k$ and targets $u_1,u_2,\dots$, starting from any $\hat Q$, then after $k$ updates $\hat Q=\frac1k\sum_{i=1}^ku_i$.

:::

::: {.proof}

1. The first update has $\eta=1$, so $\hat Q=u_1$, whatever the start.

2. If $\hat Q=\frac1{k-1}\sum_{i<k}u_i$ before update $k$, then afterwards $\hat Q=\bigl(1-\frac1k\bigr)\frac{1}{k-1}\sum_{i<k}u_i+\frac1ku_k=\frac1k\sum_{i\le k}u_i$.

:::

In a rollout $s_0,a_0,r_0,s_1,\dots$ let $u_t=\sum_{j\ge t}\gamma^{j-t}r_j$ be the utility from step $t$ on. Then $u_t=r_t+\gamma u_{t+1}$.

::: {#def-model-free-monte-carlo .definition name="Model-free Monte Carlo"}

*Model-free Monte Carlo* waits until a rollout ends, and then, for each step $t$, updates $\hat Q(s_t,a_t)$ with target $u_t$. With $\eta=1/(\text{number of updates of }\hat Q(s,a))$ it keeps $\hat Q(s,a)$ equal to the average utility observed after taking $a$ in $s$ (@prp-incremental-mean), an unbiased estimate of the Q-value of the policy the agent acts with.

:::

It is *on-policy*: it estimates the Q-values $Q_{\text{act}}$ of the acting policy, which improves as those estimates improve and $\epsilon$ decreases. Its drawback is that it learns nothing until the end of a rollout, and real life offers one long rollout.

::: {#def-sarsa .definition name="SARSA"}

*SARSA* updates after each step, on the tuple $(s_t,a_t,r_t,s_{t+1},a_{t+1})$, where $a_{t+1}$ is the action the agent actually takes next, with the *bootstrapped* target

$$
r_t+\gamma\,\hat Q(s_{t+1},a_{t+1})
$$

(just $r_t$ if $s_{t+1}$ is an end state). It replaces the unknown remainder $u_{t+1}$ of the utility by the current estimate of its expectation.

:::

The bootstrapped target has lower variance than $u_t$, since it depends on one random transition rather than a whole rollout, but it is biased while $\hat Q$ is wrong. SARSA is also on-policy.

::: {#def-q-learning .definition name="Q-learning"}

*Q-learning* updates on each transition $(s_t,a_t,r_t,s_{t+1})$ with the target

$$
r_t+\gamma\max_{a'\in\text{Actions}(s_{t+1})}\hat Q(s_{t+1},a')
$$

(just $r_t$ if $s_{t+1}$ is an end state). It estimates the optimal Q-values $Q_{\text{opt}}$, whatever policy generates the data.

:::

Q-learning is *off-policy*: its target is a sample of the right-hand side of the Bellman optimality equation for $Q_{\text{opt}}$ (@thm-value-iteration), with the expectation over $s'$ replaced by the observed next state. Under standard conditions (every state–action pair is updated infinitely often and the learning rates decrease suitably) $\hat Q$ converges to $Q_{\text{opt}}$.

```{=latex}
\begin{algorithm}
\caption{Q-learning with an $\epsilon$-greedy policy (SARSA and Monte Carlo differ only in the target)}
\begin{algorithmic}
\INPUT Environment, learning rate $\eta$, exploration rate $\epsilon$, number of episodes $m$
\OUTPUT Estimates $\hat Q$
\STATE $\hat Q(s,a)\gets0$ for all $s,a$
\FOR{$i=1$ \TO $m$}
    \STATE $s\gets s_{\text{start}}$
    \WHILE{not $\text{IsEnd}(s)$}
        \STATE $a\gets$ $\epsilon$-greedy action for $\hat Q$ in $s$
        \STATE take $a$; observe reward $r$ and next state $s'$
        \STATE $y\gets r$ \textbf{if} $\text{IsEnd}(s')$ \textbf{else} $r+\gamma\max_{a'}\hat Q(s',a')$ \COMMENT{SARSA: $r+\gamma\hat Q(s',a_{\text{next}})$}
        \STATE $\hat Q(s,a)\gets\hat Q(s,a)-\eta\bigl(\hat Q(s,a)-y\bigr)$
        \STATE $s\gets s'$
    \ENDWHILE
\ENDFOR
\RETURN $\hat Q$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-model-free-rl-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.15cm]
\foreach \i/\t in {0/{s_t},1/{a_t},2/{r_t},3/{s_{t+1}},4/{a_{t+1}},5/{r_{t+1}},6/{s_{t+2}},7/{\cdots}} { \node[lab] at (\i,0.55) {$\t$}; }
\node[lab,anchor=east] at (-0.4,0) {Monte Carlo};
\begin{scope}[on background layer]\draw[hl box] (-0.3,-0.2) rectangle (1.3,0.2);\end{scope} \draw[box] (1.7,-0.2) rectangle (7.3,0.2);
\node[lab] at (4.5,0) {$u_t=r_t+\gamma r_{t+1}+\gamma^2r_{t+2}+\cdots$ (whole rollout)};
\node[lab,anchor=east] at (-0.4,-0.6) {SARSA};
\begin{scope}[on background layer]\draw[hl box] (-0.3,-0.8) rectangle (1.3,-0.4);\end{scope} \draw[box] (1.7,-0.8) rectangle (4.3,-0.4);
\node[lab] at (3.0,-0.6) {$r_t+\gamma\hat Q(s_{t+1},a_{t+1})$};
\node[lab,anchor=east] at (-0.4,-1.2) {Q-learning};
\begin{scope}[on background layer]\draw[hl box] (-0.3,-1.4) rectangle (1.3,-1.0);\end{scope} \draw[box] (1.7,-1.4) rectangle (4.3,-1.0);
\node[lab] at (3.0,-1.2) {$r_t+\gamma\max_{a'}\hat Q(s_{t+1},a')$};
\end{tikzpicture}
\end{center}
```

What each method uses to update $\hat Q(s_t,a_t)$ (highlighted): Monte Carlo waits for the whole rest of the rollout; SARSA uses one reward and the next action actually taken; Q-learning uses one reward and the best next action according to $\hat Q$, whichever action is taken.

:::

::: {#exm-model-free-rl-1 .example name="On-policy and off-policy in the dice game"}

In the dice game (@exm-mdp-dice-game) let the agent act $\epsilon$-greedily with $\epsilon=0.3$, exploring uniformly, so once it prefers staying it stays with probability $0.85$ and quits with probability $0.15$. The value of this acting policy satisfies $V=0.15\cdot10+0.85\bigl(4+\tfrac23V\bigr)$, so $V\approx11.31$ and $Q_{\text{act}}(\text{in},\text{stay})=4+\tfrac23V\approx11.54$. SARSA and model-free Monte Carlo estimate these values, while Q-learning estimates $Q_{\text{opt}}(\text{in},\text{stay})=12$: the value of staying if every later choice were optimal.

:::
