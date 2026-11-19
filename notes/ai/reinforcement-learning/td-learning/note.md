---
title: "Temporal Difference Learning"
sources: [cs221-14, cs188-10]
requires: [ai/reinforcement-learning/function-approximation]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 14 (TD learning, self-play), in our own wording. The lecture applies TD learning to learn evaluation functions of games (@sec-ai-games-game-evaluation-functions); that part is a remark here. -->

SARSA estimates Q-values of the acting policy. If we know where each action leads, values of states are enough to act: in a game, $T$ and $\text{Reward}$ are the rules, so with $V_\pi$ known we can choose $\pi(s)=\operatorname{arg\,max}_aV_\pi(\text{Succ}(s,a))$. Value iteration is still out of reach there, not because the MDP is unknown but because it has exponentially many states. TD learning is to values what SARSA is to Q-values.

::: {#def-td-learning .definition name="TD learning"}

*Temporal difference* (TD) *learning* estimates the value $V_\pi$ of the acting policy with a parametrized $V_\theta(s)$ (a *value network* when it is a neural network). On each transition $(s_t,a_t,r_t,s_{t+1})$ it forms the target $y=r_t+\gamma V_\theta(s_{t+1})$ ($y=r_t$ if $s_{t+1}$ is an end state), treats it as a constant, and steps on the loss $\tfrac12(V_\theta(s_t)-y)^2$:

$$
\theta\ \gets\ \theta-\eta\,\bigl(V_\theta(s_t)-y\bigr)\,\nabla_\theta V_\theta(s_t).
$$

The difference $y-V_\theta(s_t)$ is the *TD error*. With indicator features ($V_\theta(s)=\theta_s$), the update is $\hat V(s_t)\gets\hat V(s_t)-\eta\bigl(\hat V(s_t)-(r_t+\gamma\hat V(s_{t+1}))\bigr)$.

:::

```{=latex}
\begin{algorithm}
\caption{TD learning}
\begin{algorithmic}
\INPUT Environment, policy $\pi$, value function $V_\theta$, learning rate $\eta$, number of episodes $m$
\OUTPUT Parameters $\theta$
\FOR{$i=1$ \TO $m$}
    \STATE $s\gets s_{\text{start}}$
    \WHILE{not $\text{IsEnd}(s)$}
        \STATE take $a=\pi(s)$; observe $r$ and $s'$
        \STATE $y\gets r$ \textbf{if} $\text{IsEnd}(s')$ \textbf{else} $r+\gamma V_\theta(s')$
        \STATE $\theta\gets\theta-\eta\,(V_\theta(s)-y)\,\nabla_\theta V_\theta(s)$; \quad $s\gets s'$
    \ENDWHILE
\ENDFOR
\RETURN $\theta$
\end{algorithmic}
\end{algorithm}
```

TD learning is on-policy and bootstraps, like SARSA. It needs a model of the transitions only for *acting* greedily on $V_\theta$, not for learning.

::: {#exm-td-learning-1 .example name="TD learning on the flaky tram"}

On the flaky tram (@exm-mdp-flaky-tram) with a table $\hat V$, initially $0$, $\eta=0.5$ and $\gamma=1$, suppose the agent walks from $1$ to $2$, walks to $3$, then takes the tram to $6$. The three updates are $\hat V(1)\gets0-0.5\bigl(0-(-1+0)\bigr)=-0.5$, then $\hat V(2)\gets-0.5$, then $\hat V(3)\gets0-0.5\bigl(0-(-2+0)\bigr)=-1$. Information travels backwards one step per visit: the next time the agent walks from $1$ to $2$, the target $-1+\hat V(2)=-1.5$ already includes what was learned at $2$.

:::

::: {#fig-td-learning-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.2cm,y=0.5cm]
\foreach \s in {1,2,3,6} { \node[lab] at (\s*0.8+1,0.9) {$\hat V(\s)$}; }
\node[lab,anchor=east] at (1.2,0) {start};
\node[lab,anchor=east] at (1.2,-1) {$1\xrightarrow{\text{walk},-1}2$};
\node[lab,anchor=east] at (1.2,-2) {$2\xrightarrow{\text{walk},-1}3$};
\node[lab,anchor=east] at (1.2,-3) {$3\xrightarrow{\text{tram},-2}6$};
\foreach \r/\a/\b/\c in {0/0/0/0, 1/\mathbf{-0.5}/0/0, 2/-0.5/\mathbf{-0.5}/0, 3/-0.5/-0.5/\mathbf{-1}} {
  \node[lab] at (1.8,-\r) {$\a$}; \node[lab] at (2.6,-\r) {$\b$}; \node[lab] at (3.4,-\r) {$\c$}; \node[lab] at (5.8,-\r) {$0$};
}
\end{tikzpicture}
\end{center}
```

The value table during the rollout of @exm-td-learning-1, after each transition; the entry just updated is in bold.

:::

::: {#rmk-td-learning-1 .remark name="Learning evaluation functions by self-play"}

In a two-player game (@sec-ai-games-game-trees) there are no rewards until the end, transitions are given by $\text{Succ}$, and the opponent minimizes what the agent maximizes. With one value function $V_\theta(s)=\theta\cdot\boldsymbol\phi(s)$ or $\text{MLP}_\theta(\boldsymbol\phi(s))$ shared by both players (*self-play*), the agent plays $\operatorname{arg\,max}_aV_\theta(\text{Succ}(s,a))$, the opponent $\operatorname{arg\,min}_a$, and TD learning on the resulting games learns an evaluation function. Samuel's checkers program (1959) did this with hand-made features and a linear function; TD-Gammon (1992) learned backgammon, a game with dice, with a neural network and simple features to expert level; AlphaGo Zero (2017) combined self-play with a value network and tree search.

:::

<!-- Added 2026-11-19 from UC Berkeley CS188 (Fall 2025), Lecture 10 (TD value learning for a fixed policy, exponential moving average), in our own wording; the numbers are our own. -->

::: {#exm-tabular-td-learning .example name="Tabular TD learning as a running average" related="def-model-free-monte-carlo"}

With indicator features, TD learning keeps a table $\hat V$ and on each transition moves $\hat V(s_t)$ a fraction $\eta$ of the way towards the sample $r_t+\gamma\hat V(s_{t+1})$: $\hat V(s_t)\gets(1-\eta)\hat V(s_t)+\eta\,(r_t+\gamma\hat V(s_{t+1}))$. After samples $x_1,\dots,x_n$ of the same state, this *exponential moving average* equals $(1-\eta)^{n}\hat V_0+\sum_{k=1}^{n}\eta(1-\eta)^{n-k}x_k$: recent samples weigh more, which suits targets that themselves improve over time, and decreasing $\eta$ makes the average converge.

For a fixed policy with $\gamma=1$, $\eta=\tfrac12$, all values initially $0$ except $\hat V(D)=8$, suppose the agent observes $B\xrightarrow{-2}C$ and then $C\xrightarrow{-2}D$. The first update gives $\hat V(B)=\tfrac12\cdot0+\tfrac12(-2+0)=-1$, the second $\hat V(C)=\tfrac12\cdot0+\tfrac12(-2+8)=3$. Unlike direct evaluation (model-free Monte Carlo, @def-model-free-monte-carlo), TD learns from each transition at once and uses the connection between states; but $B$ learns nothing about $D$ until $C$'s estimate has improved and $B$ is visited again. TD estimates values only, so turning them into a policy still needs the model (@def-policy-extraction), which is why Q-learning is used to act.

:::
