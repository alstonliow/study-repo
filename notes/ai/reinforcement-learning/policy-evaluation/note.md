---
title: "Policy Evaluation"
sources: [cs221-8]
requires: [ai/reinforcement-learning/markov-decision-processes]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 8 (policy evaluation by bootstrapping), in our own wording. The convergence theorem for gamma < 1 is our own addition; proof written out in steps. -->

The Bellman equations (@thm-bellman-policy) determine $V_\pi$, but they are recursive and the MDP may have cycles (in the dice game, staying can return to the same state), so they cannot be solved by one pass of dynamic programming. Instead we *bootstrap*: start from a guess and repeatedly substitute the current values into the right-hand side.

::: {#def-policy-evaluation .definition name="Policy evaluation"}

*Policy evaluation* sets $V^{(0)}_\pi(s)=0$ for all $s$ and, for $t=1,2,\dots$, $V^{(t)}_\pi(s)=0$ for end states and

$$
V^{(t)}_\pi(s)=\sum_{s'}T(s,\pi(s),s')\bigl[\text{Reward}(s,\pi(s),s')+\gamma V^{(t-1)}_\pi(s')\bigr]
$$

otherwise. It stops when $\max_s\lvert V^{(t)}_\pi(s)-V^{(t-1)}_\pi(s)\rvert$ falls below a tolerance $\varepsilon$ (such as $10^{-3}$).

:::

$V^{(t)}_\pi(s)$ is the expected utility of following $\pi$ from $s$ for at most $t$ steps and then stopping. Each iteration costs $O(\lvert S\rvert\,K)$, where $K$ bounds the number of successors of a state.

```{=latex}
\begin{algorithm}
\caption{Policy evaluation}
\begin{algorithmic}
\INPUT MDP, policy $\pi$, tolerance $\varepsilon$
\OUTPUT $V\approx V_\pi$
\STATE $V(s)\gets0$ for all states $s$
\REPEAT
    \FOR{each state $s$}
        \STATE $V'(s)\gets0$ \textbf{if} $\text{IsEnd}(s)$ \textbf{else} $\sum_{s'}T(s,\pi(s),s')\bigl[\text{Reward}(s,\pi(s),s')+\gamma V(s')\bigr]$
    \ENDFOR
    \STATE $\delta\gets\max_s\lvert V'(s)-V(s)\rvert$; $V\gets V'$
\UNTIL{$\delta<\varepsilon$}
\RETURN $V$
\end{algorithmic}
\end{algorithm}
```

::: {#thm-policy-evaluation-converges .theorem name="Policy evaluation converges"}

If $\gamma<1$, the iterates of policy evaluation converge to $V_\pi$, and

$$
\max_s\bigl\lvert V^{(t)}_\pi(s)-V_\pi(s)\bigr\rvert\ \le\ \gamma^t\max_s\lvert V_\pi(s)\rvert .
$$

:::

::: {.proof}

1. Write the update as $V^{(t)}=B(V^{(t-1)})$, where $(BV)(s)$ is the right-hand side above (and $0$ at end states). By @thm-bellman-policy, $B(V_\pi)=V_\pi$.

2. For any two functions $U,V$ on the states and any non-end $s$,
$$
\lvert(BU)(s)-(BV)(s)\rvert=\gamma\Bigl\lvert\sum_{s'}T(s,\pi(s),s')\bigl(U(s')-V(s')\bigr)\Bigr\rvert\le\gamma\max_{s'}\lvert U(s')-V(s')\rvert,
$$
because the rewards cancel and the weights $T(s,\pi(s),s')$ are non-negative and sum to $1$. At end states both sides are $0$.

3. So $\max_s\lvert V^{(t)}(s)-V_\pi(s)\rvert=\max_s\lvert(BV^{(t-1)})(s)-(BV_\pi)(s)\rvert\le\gamma\max_s\lvert V^{(t-1)}(s)-V_\pi(s)\rvert$.

4. Applying step 3 $t$ times and using $V^{(0)}=0$ gives the bound, which tends to $0$ since $\gamma<1$.

:::

With $\gamma=1$ the same argument works whenever every rollout of $\pi$ ends with probability $1$, though the error then shrinks at a rate set by the MDP rather than by $\gamma$. In the dice game with $\gamma=1$, the chance of continuing, $\tfrac23$, plays the role of $\gamma$.

::: {#exm-policy-evaluation-1 .example name="Evaluating the policy that stays"}

In the dice game (@exm-mdp-dice-game) with $\pi(\text{in})=\text{stay}$, the update is $V^{(t)}(\text{in})=4+\tfrac23V^{(t-1)}(\text{in})$, giving $0,\,4,\,6.67,\,8.44,\,9.63,\dots$ In closed form $V^{(t)}(\text{in})=12\bigl(1-(\tfrac23)^t\bigr)$, which converges to $V_\pi(\text{in})=12$ with error shrinking by the factor $\tfrac23$ each iteration.

:::

::: {#fig-policy-evaluation-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (5.2,0) node[lab,anchor=north east] {iteration $t$};
\draw[->] (0,0) -- (0,2.9) node[lab,anchor=north west] {$V^{(t)}_\pi(\text{in})$};
\foreach \t in {2,4,6,8,10,12} { \node[lab,tick] at ({\t*0.4},-0.25) {\t}; }
\foreach \v in {4,8,12} { \node[lab,tick] at (-0.3,{\v*0.2}) {\v}; }
\draw[faint,dashed] (0,2.4) -- (5,2.4);
\draw[hl] plot coordinates {(0.0,0.00) (0.4,0.80) (0.8,1.33) (1.2,1.69) (1.6,1.93) (2.0,2.08) (2.4,2.19) (2.8,2.26) (3.2,2.31) (3.6,2.34) (4.0,2.36) (4.4,2.37) (4.8,2.38)};
\node[dot] at (0.0,0.00) {}; \node[dot] at (0.4,0.80) {}; \node[dot] at (0.8,1.33) {}; \node[dot] at (1.2,1.69) {}; \node[dot] at (1.6,1.93) {}; \node[dot] at (2.0,2.08) {}; \node[dot] at (2.4,2.19) {}; \node[dot] at (2.8,2.26) {}; \node[dot] at (3.2,2.31) {}; \node[dot] at (3.6,2.34) {}; \node[dot] at (4.0,2.36) {}; \node[dot] at (4.4,2.37) {}; \node[dot] at (4.8,2.38) {};
\end{tikzpicture}
\end{center}
```

Policy evaluation for "always stay" in the dice game: the iterates approach the value $12$ (dashed) geometrically.

:::
