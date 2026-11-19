---
title: "Policy Extraction and Policy Iteration"
sources: [cs188-8, cs188-9]
requires: [ai/reinforcement-learning/value-iteration]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley CS188 (Fall 2025), Lecture 8 (time-limited values, discounting) and Lecture 9 (Bellman equations, policy extraction from values and Q-values, policy iteration, comparison of MDP algorithms, offline and online planning), in our own wording; proofs written out in steps; the flaky-tram run was computed exactly in Python. -->

Value iteration (@def-value-iteration) updates values and reads off a policy at the end. Policy iteration does the opposite: it keeps a policy, evaluates it exactly, and improves it. Both rest on the same two operations, evaluating and acting greedily.

::: {#prp-time-limited-values .proposition name="Value iteration computes time-limited values"}

For every state $s$ and $t\ge0$, the iterate $V^{(t)}(s)$ of value iteration is the largest expected discounted reward obtainable from $s$ when the process is stopped after $t$ steps, over all ways of choosing actions (which may depend on the step).

:::

::: {.proof}

1. For $t=0$ no reward is collected, and $V^{(0)}=0$. At end states nothing more is collected, matching $V^{(t)}=0$ there.
2. Suppose the claim holds for $t-1$. With $t$ steps left at a non-end state $s$, choosing $a$ first yields $\text{Reward}(s,a,s')$ and moves to $s'$ with probability $T(s,a,s')$; from $s'$, with $t-1$ steps left, the best obtainable is $V^{(t-1)}(s')$ by induction, discounted by $\gamma$.
3. The best first action maximises the expectation of the total, $\sum_{s'}T(s,a,s')[\text{Reward}(s,a,s')+\gamma V^{(t-1)}(s')]$, which is the update defining $V^{(t)}(s)$.

:::

So $V^{(t)}$ is a depth-$t$ expectimax (@def-game-recurrences) computed bottom-up for all states at once, without repeating the work for states that recur in the tree; with $\gamma<1$ the far levels matter little, which is why the iterates converge (@thm-value-iteration).

::: {#rmk-discounting .remark name="Why discount?"}

Discounting with $\gamma<1$ prefers rewards sooner, keeps utilities of infinite rollouts finite (at most $R_{\max}/(1-\gamma)$ when rewards are bounded by $R_{\max}$), and helps the algorithms converge. It is also forced by a natural assumption: if preferences between reward sequences are *stationary* — $[a,b_1,b_2,\dots]\succ[a,c_1,c_2,\dots]$ exactly when $[b_1,b_2,\dots]\succ[c_1,c_2,\dots]$ — then the utility of a sequence must be additive, $\sum_tr_t$, or discounted, $\sum_t\gamma^tr_t$. Other ways to avoid infinite utilities are a finite horizon (stopping after $T$ steps, which makes the optimal policy depend on the time left) and absorbing end states reached with probability $1$.

:::

::: {#def-policy-extraction .definition name="Policy extraction"}

*Policy extraction* turns values into a policy by one step of lookahead: given values $V$,
$$
\pi_V(s)=\operatorname*{arg\,max}_{a}\sum_{s'}T(s,a,s')\bigl[\text{Reward}(s,a,s')+\gamma V(s')\bigr],
$$
and given Q-values $Q$, simply $\pi_Q(s)=\operatorname{arg\,max}_aQ(s,a)$.

:::

Extracting from values needs the model ($T$ and Reward); extracting from Q-values does not. This is why the reinforcement learning methods that do without a model learn Q-values (@def-q-learning). Q-values can also be computed directly by *Q-value iteration*, $Q^{(t)}(s,a)=\sum_{s'}T(s,a,s')[\text{Reward}(s,a,s')+\gamma\max_{a'}Q^{(t-1)}(s',a')]$, which is value iteration with $V^{(t-1)}(s')=\max_{a'}Q^{(t-1)}(s',a')$ substituted.

::: {#def-policy-iteration .definition name="Policy iteration"}

*Policy iteration* starts from any policy $\pi_0$ and for $i=0,1,2,\dots$:

1. (*evaluation*) computes $V_{\pi_i}$, by solving the Bellman equations of @thm-bellman-policy (a linear system) or by policy evaluation (@def-policy-evaluation);
2. (*improvement*) sets $\pi_{i+1}=\pi_{V_{\pi_i}}$ by policy extraction, keeping $\pi_{i+1}(s)=\pi_i(s)$ when $\pi_i(s)$ is among the maximisers;

and stops when $\pi_{i+1}=\pi_i$.

:::

```{=latex}
\begin{algorithm}
\caption{Policy iteration}
\begin{algorithmic}
\INPUT MDP with $\gamma<1$
\OUTPUT An optimal policy and its values
\STATE $\pi\gets$ any policy
\REPEAT
    \STATE $V\gets V_\pi$ \COMMENT{solve $V(s)=\sum_{s'}T(s,\pi(s),s')[\text{Reward}(s,\pi(s),s')+\gamma V(s')]$}
    \STATE $\mathit{stable}\gets$ true
    \FOR{each non-end state $s$}
        \STATE $Q(s,a)\gets\sum_{s'}T(s,a,s')[\text{Reward}(s,a,s')+\gamma V(s')]$ for all $a$
        \IF{$Q(s,a)>Q(s,\pi(s))$ for some $a$}
            \STATE $\pi(s)\gets\operatorname{arg\,max}_aQ(s,a)$; $\mathit{stable}\gets$ false
        \ENDIF
    \ENDFOR
\UNTIL{$\mathit{stable}$}
\RETURN $\pi,V$
\end{algorithmic}
\end{algorithm}
```

::: {#thm-policy-improvement .theorem name="Policy improvement"}

Let $\gamma<1$, let $\pi$ be a policy and $\pi'$ a policy with $Q_\pi(s,\pi'(s))\ge V_\pi(s)$ for every non-end state $s$ (for example $\pi'=\pi_{V_\pi}$). Then $V_{\pi'}(s)\ge V_\pi(s)$ for every $s$. If moreover the inequality is strict at some state $s_0$, then $V_{\pi'}(s_0)>V_\pi(s_0)$.

:::

::: {.proof}

1. Define the operator $(B'V)(s)=\sum_{s'}T(s,\pi'(s),s')[\text{Reward}(s,\pi'(s),s')+\gamma V(s')]$ (and $0$ at end states). It is monotone ($V\le W$ pointwise implies $B'V\le B'W$, since the weights $T$ are non-negative), and by @thm-bellman-policy $V_{\pi'}$ is its fixed point.
2. The hypothesis says $B'V_\pi=Q_\pi(\cdot,\pi'(\cdot))\ge V_\pi$.
3. Applying $B'$ repeatedly and using monotonicity, $V_\pi\le B'V_\pi\le(B')^{2}V_\pi\le\cdots$.
4. As in the proof of @thm-value-iteration, $B'$ is a $\gamma$-contraction in the maximum norm, so $(B')^{k}V_\pi\to V_{\pi'}$. Hence $V_\pi\le B'V_\pi\le V_{\pi'}$.
5. If $(B'V_\pi)(s_0)>V_\pi(s_0)$, then $V_{\pi'}(s_0)\ge(B'V_\pi)(s_0)>V_\pi(s_0)$ by step 4.

:::

::: {#thm-policy-iteration .theorem name="Policy iteration finds an optimal policy"}

For a finite MDP with $\gamma<1$, policy iteration stops after finitely many iterations, and the final policy is optimal.

:::

::: {.proof}

1. If $\pi_{i+1}\ne\pi_i$, then at some state the new action has $Q_{\pi_i}(s,\pi_{i+1}(s))>Q_{\pi_i}(s,\pi_i(s))=V_{\pi_i}(s)$ (ties keep the old action), while at all states $Q_{\pi_i}(s,\pi_{i+1}(s))\ge V_{\pi_i}(s)$. By @thm-policy-improvement, $V_{\pi_{i+1}}\ge V_{\pi_i}$ with strict inequality somewhere.
2. So no policy occurs twice. There are finitely many policies ($\prod_s|\text{Actions}(s)|$), so the iteration stops.
3. When it stops, $\pi=\pi_i$ satisfies $V_\pi(s)=\max_aQ_\pi(s,a)=\max_a\sum_{s'}T(s,a,s')[\text{Reward}(s,a,s')+\gamma V_\pi(s')]$: $V_\pi$ solves the Bellman optimality equation. By @thm-value-iteration its solution is unique and equals $V_{\text{opt}}$, so $\pi$ is optimal.

:::

::: {#exm-policy-iteration-tram .example name="Policy iteration on the flaky tram"}

On the flaky tram (@exm-mdp-flaky-tram, $n=10$, $p=0.4$; here $\gamma=1$, but every policy reaches the end with probability $1$, which is all the proofs need) start with "always walk", whose values are $V(i)=-(10-i)$. Improvement compares walking, $-1+V(i+1)$, with the tram, $0.6(-2+V(2i))+0.4(-2+V(i))$: at $i=5$ the tram gives $-4>-5$ and at $i=4$ it gives $-5.6>-6$, so the new policy takes the tram at $4$ and $5$. Its values are $V(5)=-\tfrac{10}{3}$, $V(4)=-\tfrac{16}{3}$, $V(1)=-\tfrac{25}{3}$. The next improvement switches $4$ back to walking ($-1+V(5)=-\tfrac{13}{3}$ beats the tram's $-\tfrac{16}{3}$), giving $V(1)=-\tfrac{22}{3}\approx-7.33$, and the third round changes nothing: the optimal policy takes the tram only from $5$.

:::

::: {#fig-policy-iteration-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$W$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$W$};
\draw[cell frame] (1.100,0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$W$};
\draw[cell frame] (1.650,0.000) rectangle (2.200,0.550);
\node[lab] at (1.925,0.275) {$W$};
\draw[cell frame] (2.200,0.000) rectangle (2.750,0.550);
\node[lab] at (2.475,0.275) {$W$};
\draw[cell frame] (2.750,0.000) rectangle (3.300,0.550);
\node[lab] at (3.025,0.275) {$W$};
\draw[cell frame] (3.300,0.000) rectangle (3.850,0.550);
\node[lab] at (3.575,0.275) {$W$};
\draw[cell frame] (3.850,0.000) rectangle (4.400,0.550);
\node[lab] at (4.125,0.275) {$W$};
\draw[cell frame] (4.400,0.000) rectangle (4.950,0.550);
\node[lab] at (4.675,0.275) {$W$};
\node[lab, anchor=east] at (-0.100,0.275) {$\pi_0$};
\node[lab, anchor=west] at (5.15,0.27) {$V(1)=-9$};
\draw[cell frame] (0.000,-0.750) rectangle (0.550,-0.200);
\node[lab] at (0.275,-0.475) {$W$};
\draw[cell frame] (0.550,-0.750) rectangle (1.100,-0.200);
\node[lab] at (0.825,-0.475) {$W$};
\draw[cell frame] (1.100,-0.750) rectangle (1.650,-0.200);
\node[lab] at (1.375,-0.475) {$W$};
\draw[hl cell] (1.650,-0.750) rectangle (2.200,-0.200);
\node[lab] at (1.925,-0.475) {$T$};
\draw[hl cell] (2.200,-0.750) rectangle (2.750,-0.200);
\node[lab] at (2.475,-0.475) {$T$};
\draw[cell frame] (2.750,-0.750) rectangle (3.300,-0.200);
\node[lab] at (3.025,-0.475) {$W$};
\draw[cell frame] (3.300,-0.750) rectangle (3.850,-0.200);
\node[lab] at (3.575,-0.475) {$W$};
\draw[cell frame] (3.850,-0.750) rectangle (4.400,-0.200);
\node[lab] at (4.125,-0.475) {$W$};
\draw[cell frame] (4.400,-0.750) rectangle (4.950,-0.200);
\node[lab] at (4.675,-0.475) {$W$};
\node[lab, anchor=east] at (-0.100,-0.475) {$\pi_1$};
\node[lab, anchor=west] at (5.15,-0.48) {$V(1)=-25/3$};
\draw[cell frame] (0.000,-1.500) rectangle (0.550,-0.950);
\node[lab] at (0.275,-1.225) {$W$};
\draw[cell frame] (0.550,-1.500) rectangle (1.100,-0.950);
\node[lab] at (0.825,-1.225) {$W$};
\draw[cell frame] (1.100,-1.500) rectangle (1.650,-0.950);
\node[lab] at (1.375,-1.225) {$W$};
\draw[cell frame] (1.650,-1.500) rectangle (2.200,-0.950);
\node[lab] at (1.925,-1.225) {$W$};
\draw[hl cell] (2.200,-1.500) rectangle (2.750,-0.950);
\node[lab] at (2.475,-1.225) {$T$};
\draw[cell frame] (2.750,-1.500) rectangle (3.300,-0.950);
\node[lab] at (3.025,-1.225) {$W$};
\draw[cell frame] (3.300,-1.500) rectangle (3.850,-0.950);
\node[lab] at (3.575,-1.225) {$W$};
\draw[cell frame] (3.850,-1.500) rectangle (4.400,-0.950);
\node[lab] at (4.125,-1.225) {$W$};
\draw[cell frame] (4.400,-1.500) rectangle (4.950,-0.950);
\node[lab] at (4.675,-1.225) {$W$};
\node[lab, anchor=east] at (-0.100,-1.225) {$\pi_2$};
\node[lab, anchor=west] at (5.15,-1.23) {$V(1)=-22/3$};
\node[lab, tick] at (0.28,0.75) {1};
\node[lab, tick] at (0.83,0.75) {2};
\node[lab, tick] at (1.38,0.75) {3};
\node[lab, tick] at (1.93,0.75) {4};
\node[lab, tick] at (2.48,0.75) {5};
\node[lab, tick] at (3.03,0.75) {6};
\node[lab, tick] at (3.58,0.75) {7};
\node[lab, tick] at (4.12,0.75) {8};
\node[lab, tick] at (4.68,0.75) {9};
\end{tikzpicture}
\end{center}
```

Policy iteration on the flaky tram (@exm-policy-iteration-tram): the action at each location $1,\dots,9$ (W walk, T tram, highlighted) in each round, and the value of the start. The third round reproduces $\pi_2$, which is optimal.

:::

::: {#rmk-mdp-algorithms .remark name="Comparing the algorithms"}

Value iteration does a cheap sweep, $O(|S|^{2}|A|)$, many times, and its policy often stops changing long before its values do. Policy iteration does an expensive evaluation per round, a linear system or many sweeps with one fixed action per state ($O(|S|^{2})$ each), but usually needs very few rounds. Both are *offline planning*: the agent knows $T$ and Reward and computes before acting. If the model is unknown, the agent must learn from experience while acting (*online*), which is reinforcement learning (@sec-ai-reinforcement-learning-model-based-rl).

:::
