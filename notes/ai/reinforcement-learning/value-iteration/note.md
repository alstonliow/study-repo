---
title: "Value Iteration"
sources: [cs221-8]
requires: [ai/reinforcement-learning/policy-evaluation]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 8 (value iteration), in our own wording. The convergence and optimality theorem for gamma < 1 is our own addition; proof written out in steps. -->

There are exponentially many policies, so evaluating each one is hopeless. Value iteration finds the best value directly: it is policy evaluation with the policy's action replaced by a maximum over actions.

::: {#def-optimal-value .definition name="Optimal value, optimal policy"}

The *optimal value* of a state is $V_{\text{opt}}(s)=\max_\pi V_\pi(s)$, and a policy $\pi_{\text{opt}}$ is *optimal* if $V_{\pi_{\text{opt}}}(s)=V_{\text{opt}}(s)$ for every $s$. The *optimal Q-value* is $Q_{\text{opt}}(s,a)=\sum_{s'}T(s,a,s')\bigl[\text{Reward}(s,a,s')+\gamma V_{\text{opt}}(s')\bigr]$.

:::

::: {#def-value-iteration .definition name="Value iteration"}

*Value iteration* sets $V^{(0)}(s)=0$ for all $s$ and, for $t=1,2,\dots$, $V^{(t)}(s)=0$ for end states and

$$
V^{(t)}(s)=\max_{a\in\text{Actions}(s)}\sum_{s'}T(s,a,s')\bigl[\text{Reward}(s,a,s')+\gamma V^{(t-1)}(s')\bigr]
$$

otherwise, until the largest change is below a tolerance. It returns the values $V$ and the *greedy policy* $\pi(s)=\operatorname{arg\,max}_a\sum_{s'}T(s,a,s')[\text{Reward}(s,a,s')+\gamma V(s')]$.

:::

```{=latex}
\begin{algorithm}
\caption{Value iteration}
\begin{algorithmic}
\INPUT MDP, tolerance $\varepsilon$
\OUTPUT $V\approx V_{\text{opt}}$ and a policy $\pi$
\STATE $V(s)\gets0$ for all states $s$
\REPEAT
    \FOR{each non-end state $s$}
        \FOR{each $a\in\text{Actions}(s)$}
            \STATE $Q(s,a)\gets\sum_{s'}T(s,a,s')\bigl[\text{Reward}(s,a,s')+\gamma V(s')\bigr]$
        \ENDFOR
        \STATE $V'(s)\gets\max_aQ(s,a)$; \quad $\pi(s)\gets\operatorname{arg\,max}_aQ(s,a)$
    \ENDFOR
    \STATE $V'(s)\gets0$ for end states $s$
    \STATE $\delta\gets\max_s\lvert V'(s)-V(s)\rvert$; $V\gets V'$
\UNTIL{$\delta<\varepsilon$}
\RETURN $V,\pi$
\end{algorithmic}
\end{algorithm}
```

::: {#thm-value-iteration .theorem name="Value iteration converges to the optimal value"}

Let $\gamma<1$. The equation

$$
V(s)=\max_{a}\sum_{s'}T(s,a,s')\bigl[\text{Reward}(s,a,s')+\gamma V(s')\bigr]\quad(\text{and }V(s)=0\text{ at end states})
$$

(the *Bellman optimality equation*) has exactly one solution $V^*$; the iterates of value iteration converge to it, with $\max_s\lvert V^{(t)}(s)-V^*(s)\rvert\le\gamma^t\max_s\lvert V^*(s)\rvert$. Moreover $V^*=V_{\text{opt}}$, and the greedy policy with respect to $V^*$ is optimal.

:::

::: {.proof}

1. Let $B^*$ map $V$ to the right-hand side, and $B_\pi$ be the update of policy evaluation for a policy $\pi$. Since $\lvert\max_af(a)-\max_ag(a)\rvert\le\max_a\lvert f(a)-g(a)\rvert$, the computation of step 2 in the proof of @thm-policy-evaluation-converges shows $\max_s\lvert(B^*U)(s)-(B^*V)(s)\rvert\le\gamma\max_s\lvert U(s)-V(s)\rvert$.

2. A map with this property has at most one fixed point: two fixed points $U,V$ would satisfy $\max\lvert U-V\rvert\le\gamma\max\lvert U-V\rvert$, so $U=V$. The iterates $V^{(t)}=B^*V^{(t-1)}$ satisfy $\max\lvert V^{(t+1)}-V^{(t)}\rvert\le\gamma^t\max\lvert V^{(1)}-V^{(0)}\rvert$, so they form a Cauchy sequence in the finite-dimensional space of value functions and converge to some $V^*$; by continuity of $B^*$, $B^*V^*=V^*$. The error bound follows as in @thm-policy-evaluation-converges.

3. For every policy $\pi$ and every $V$, $B_\pi V\le B^*V$ entrywise (a maximum is at least any one term), and both maps are monotone: $U\le V$ implies $B_\pi U\le B_\pi V$ and $B^*U\le B^*V$, since the weights $T$ are non-negative. By induction $B_\pi^t\mathbf{0}\le(B^*)^t\mathbf{0}$ for all $t$; letting $t\to\infty$ (@thm-policy-evaluation-converges) gives $V_\pi\le V^*$.

4. Let $\pi^*$ be greedy with respect to $V^*$. Then $B_{\pi^*}V^*=B^*V^*=V^*$, so $V^*$ is the fixed point of $B_{\pi^*}$, which is $V_{\pi^*}$ by @thm-bellman-policy and the uniqueness argument of step 2.

5. So $V^*=V_{\pi^*}\le V_{\text{opt}}=\max_\pi V_\pi\le V^*$, hence $V^*=V_{\text{opt}}$ and $\pi^*$ is optimal.

:::

As with policy evaluation, the result also holds for $\gamma=1$ when every policy reaches an end state with probability $1$, which is the case in both running examples.

::: {#exm-value-iteration-1 .example name="Value iteration on the dice game and the flaky tram"}

In the dice game the update is $V^{(t)}(\text{in})=\max\bigl(10,\ 4+\tfrac23V^{(t-1)}(\text{in})\bigr)$, giving $10,\ 10.67,\ 11.11,\ 11.41,\dots\to12$; the greedy policy switches from quit to stay at iteration $2$. On the flaky tram with $n=10$, $p=0.4$, value iteration converges after $15$ iterations (tolerance $10^{-3}$) to $V_{\text{opt}}(i)=-(10-i)$ for $i\ge6$ and $V_{\text{opt}}(i)=-\tfrac{10}{3}-(5-i)$ for $i\le5$: the optimal policy walks to $5$, takes the tram to $10$ (expected time $2/0.6=\tfrac{10}{3}$) and walks everywhere else, with expected time $7\tfrac13$ from the start instead of $9$.

:::

::: {#fig-value-iteration-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \i in {1,...,10} { \node[lab,tick] at ({0.95*\i},0.45) {\i}; }
\node[lab,anchor=east] at (0.4,0.45) {state};
\node[lab,anchor=east] at (0.4,0) {$t=1$};
\node[lab,anchor=east] at (0.4,-0.45) {$t=2$};
\node[lab,anchor=east] at (0.4,-0.9) {$t=3$};
\node[lab,anchor=east] at (0.4,-1.35) {$t=15$};
\node[lab,anchor=east] at (0.4,-1.8) {$\pi$};
\foreach \i/\v in {1/-1,2/-1,3/-1,4/-1,5/-1,6/-1,7/-1,8/-1,9/-1,10/0} { \node[lab] at ({0.95*\i},0) {$\v$}; }
\foreach \i/\v in {1/-2,2/-2,3/-2,4/-2,5/-2,6/-2,7/-2,8/-2,9/-1,10/0} { \node[lab] at ({0.95*\i},-0.45) {$\v$}; }
\foreach \i/\v in {1/-3,2/-3,3/-3,4/-3,5/-2.8,6/-3,7/-3,8/-2,9/-1,10/0} { \node[lab] at ({0.95*\i},-0.9) {$\v$}; }
\foreach \i/\v in {1/-7.33,2/-6.33,3/-5.33,4/-4.33,5/-3.33,6/-4,7/-3,8/-2,9/-1,10/0} { \node[lab] at ({0.95*\i},-1.35) {$\v$}; }
\foreach \i/\v in {1/W,2/W,3/W,4/W,6/W,7/W,8/W,9/W} { \node[lab] at ({0.95*\i},-1.8) {\v}; }
\node[lab] at (4.75,-1.8) {\textbf{T}};
\begin{scope}[on background layer]\draw[hl box] (4.45,-1.6) rectangle (5.05,-2.0);\end{scope}
\end{tikzpicture}
\end{center}
```

Value iteration on the flaky tram ($n=10$, $p=0.4$): values $V^{(t)}$ after iterations $1$, $2$, $3$ and $15$ (converged), and the greedy policy (W walk, T tram). After $t$ iterations a state's value counts at most $t$ steps, so values first fall by $1$ per iteration until the end is within reach.

:::
