---
title: "Game Trees, Expectimax and Minimax"
sources: [cs221-13, cs188-6, cs188-7]
requires: [ai/reinforcement-learning/policy-evaluation]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 13 (game trees, game evaluation, expectimax, minimax, expectiminimax), in our own wording. The three properties of minimax are stated as a theorem with our own proof. -->

In an MDP the randomness of the environment is known. In a game the other player's strategy is unknown, and the other player may be working against us.

::: {#def-two-player-game .definition name="Two-player zero-sum game"}

A *two-player zero-sum game* (turn-based, with perfect information) consists of states with a start state $s_{\text{start}}$; actions $\text{Actions}(s)$; a successor function $\text{Succ}(s,a)$; a function $\text{Player}(s)\in\{\text{agent},\text{opp}\}$ saying who moves in $s$; end states marked by $\text{IsEnd}(s)$; and the agent's utility $\text{Utility}(s)$ at each end state, the opponent's being $-\text{Utility}(s)$. Its *game tree* has the start state at the root, one child per action, and the end states as leaves; each root-to-leaf path is a possible play.

:::

All the utility comes at the end, and the players take turns. A *policy* $\pi_p$ of player $p$ is deterministic ($\pi_p(s)$ is an action) or stochastic ($\pi_p(a\mid s)$ is a probability).

::: {#exm-game-bins .example name="Choosing a bin"}

There are three bins, A $=\{-50,50\}$, B $=\{1,3\}$ and C $=\{-5,15\}$. The agent chooses a bin, then the opponent chooses a number from it, which is the agent's utility. If the opponent picks uniformly at random, bin C is best (expected $5$, against $0$ and $2$). If the opponent picks the smallest number, bin B is best (guaranteed $1$, against $-50$ and $-5$).

:::

::: {#def-game-recurrences .definition name="Game evaluation, expectimax, minimax"}

For end states each of the following equals $\text{Utility}(s)$. Otherwise:

1. *Game evaluation*, for given policies of both players:
$$
V_{\text{eval}}(s)=\sum_{a}\pi_{\text{Player}(s)}(a\mid s)\,V_{\text{eval}}(\text{Succ}(s,a)).
$$
2. *Expectimax*, for a given opponent policy $\pi_{\text{opp}}$: $V_{\text{exptmax}}(s)=\max_aV_{\text{exptmax}}(\text{Succ}(s,a))$ if $\text{Player}(s)=\text{agent}$, and $\sum_a\pi_{\text{opp}}(a\mid s)V_{\text{exptmax}}(\text{Succ}(s,a))$ if $\text{Player}(s)=\text{opp}$.
3. *Minimax*, assuming the opponent plays as well as possible:
$$
V_{\text{minmax}}(s)=\begin{cases}\max_{a}V_{\text{minmax}}(\text{Succ}(s,a))&\text{if }\text{Player}(s)=\text{agent},\\ \min_{a}V_{\text{minmax}}(\text{Succ}(s,a))&\text{if }\text{Player}(s)=\text{opp}.\end{cases}
$$

The maximizing and minimizing actions define the *minimax policies* $\pi_{\max}$ and $\pi_{\min}$; the maximizing actions of expectimax define $\pi_{\text{exptmax}}$.

:::

Game evaluation is the analogue of policy evaluation and expectimax of value iteration in MDPs (@sec-ai-reinforcement-learning-value-iteration); minimax has no MDP analogue. The game tree is finite and acyclic, so each recurrence is computed by one depth-first traversal, but the tree can be exponentially large in its depth.

```{=latex}
\begin{algorithm}
\caption{Minimax}
\begin{algorithmic}
\INPUT A state $s$ of a two-player zero-sum game
\OUTPUT $V_{\text{minmax}}(s)$
\FUNCTION{Minimax}{$s$}
    \IF{$\text{IsEnd}(s)$}
        \RETURN $\text{Utility}(s)$
    \ENDIF
    \STATE $\mathcal V\gets\{\textsc{Minimax}(\text{Succ}(s,a)):a\in\text{Actions}(s)\}$
    \IF{$\text{Player}(s)=\text{agent}$}
        \RETURN $\max\mathcal V$
    \ELSE
        \RETURN $\min\mathcal V$
    \ENDIF
\ENDFUNCTION
\end{algorithmic}
\end{algorithm}
```

Expectimax and game evaluation are the same procedure with $\min$ (or $\max$) replaced by an expectation under the given policy.

::: {#fig-game-trees-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1.1cm]
\node[small vertex] (r) at (3,0) {$1$};
\node[small vertex] (A) at (0.75,-1) {$-50$};
\node[small vertex] (B) at (3,-1) {$1$};
\node[small vertex] (C) at (5.25,-1) {$-5$};
\foreach \n/\x/\v in {a1/0.25/-50,a2/1.25/50,b1/2.5/1,b2/3.5/3,c1/4.75/-5,c2/5.75/15} { \node[lab] (\n) at (\x,-2) {$\v$}; }
\draw (r) -- node[edge label,left] {A} (A); \draw[hl] (r) -- node[edge label,right] {B} (B); \draw (r) -- node[edge label,right] {C} (C);
\draw[hl] (A) -- (a1); \draw (A) -- (a2); \draw[hl] (B) -- (b1); \draw (B) -- (b2); \draw[hl] (C) -- (c1); \draw (C) -- (c2);
\node[lab,anchor=west] at (6.2,0) {max};
\node[lab,anchor=west] at (6.2,-1) {min};
\node[lab] at (0.4,-1.45) {$(0)$}; \node[lab] at (2.65,-1.45) {$(2)$}; \node[lab] at (4.9,-1.45) {$(5)$};
\end{tikzpicture}
\end{center}
```

Minimax on the bins game of @exm-game-bins: each min node takes its smaller leaf, the root the largest of these, so $V_{\text{minmax}}=1$ with $\pi_{\max}=\text{B}$ (highlighted). Numbers in parentheses are expectimax values for a uniform opponent; expectimax picks C, with value $5$.

:::

Write $V(\pi_{\text{agent}},\pi_{\text{opp}})$ for the value of the game when the two policies play each other. In the bins game,

$$
\begin{array}{r|cc}
&\pi_{\min}&\pi_{\text{uniform}}\\\hline
\pi_{\max}&1&2\\
\pi_{\text{exptmax}}&-5&5
\end{array}
$$

::: {#thm-minimax-properties .theorem name="What minimax guarantees"}

Let $\pi_{\max},\pi_{\min}$ be minimax policies and $\pi_{\text{exptmax}}$ the expectimax policy for an opponent policy $\pi_{\text{opp}}$. For all agent policies $\pi_{\text{agent}}$ and opponent policies $\pi$,

1. $V(\pi_{\text{agent}},\pi_{\min})\le V(\pi_{\max},\pi_{\min})$: $\pi_{\max}$ is best against $\pi_{\min}$;
2. $V(\pi_{\max},\pi_{\min})\le V(\pi_{\max},\pi)$: against any opponent, $\pi_{\max}$ earns at least the minimax value;
3. $V(\pi_{\text{agent}},\pi_{\text{opp}})\le V(\pi_{\text{exptmax}},\pi_{\text{opp}})$: expectimax is best against the opponent it assumes.

:::

::: {.proof}

1. All three are proved by induction on the height of the subtree at a state $s$, comparing the values of the two pairs of policies from $s$. At end states both sides equal $\text{Utility}(s)$.

2. For part 1, let $V_1(s)$ be the value from $s$ of $(\pi_{\text{agent}},\pi_{\min})$; we show $V_1(s)\le V_{\text{minmax}}(s)$, which is the value of $(\pi_{\max},\pi_{\min})$. At an opponent state both pairs play $\pi_{\min}$'s action $a^*$, so $V_1(s)=V_1(\text{Succ}(s,a^*))\le V_{\text{minmax}}(\text{Succ}(s,a^*))=V_{\text{minmax}}(s)$ by induction. At an agent state $V_1(s)$ is an average of $V_1(\text{Succ}(s,a))$ over $\pi_{\text{agent}}(\cdot\mid s)$, each at most $V_{\text{minmax}}(\text{Succ}(s,a))\le\max_aV_{\text{minmax}}(\text{Succ}(s,a))=V_{\text{minmax}}(s)$.

3. For part 2, let $V_2(s)$ be the value from $s$ of $(\pi_{\max},\pi)$; we show $V_2(s)\ge V_{\text{minmax}}(s)$. At an agent state both pairs play $\pi_{\max}$'s action, and induction applies. At an opponent state $V_2(s)$ is an average over $\pi(\cdot\mid s)$ of $V_2(\text{Succ}(s,a))\ge V_{\text{minmax}}(\text{Succ}(s,a))\ge\min_aV_{\text{minmax}}(\text{Succ}(s,a))=V_{\text{minmax}}(s)$.

4. For part 3, the value of $(\pi_{\text{exptmax}},\pi_{\text{opp}})$ is $V_{\text{exptmax}}$. At opponent states both pairs average over $\pi_{\text{opp}}$ and induction applies termwise; at agent states the value of $(\pi_{\text{agent}},\pi_{\text{opp}})$ is an average of children's values, each at most the corresponding $V_{\text{exptmax}}$, hence at most their maximum.

:::

Chaining the parts, $V(\pi_{\text{exptmax}},\pi_{\min})\le V(\pi_{\max},\pi_{\min})\le V(\pi_{\max},\pi_{\text{opp}})\le V(\pi_{\text{exptmax}},\pi_{\text{opp}})$, which in the bins game reads $-5\le1\le2\le5$. "Optimal" always means optimal against some assumed opponent. Minimax is safe, but against a known weak opponent expectimax does better.

::: {#def-expectiminimax .definition name="Expectiminimax"}

If some states belong to a *chance* player with a known policy $\pi_{\text{coin}}$ (dice, coin flips), *expectiminimax* takes $\max$ at agent states, $\min$ at opponent states and the expectation under $\pi_{\text{coin}}$ at chance states.

:::

For example, if after the agent picks a bin a fair coin decides whether to move one bin to the left (with wrap-around), the minimax opponent still picks the smaller number, and the expectiminimax value is $\max\bigl(\tfrac{-50-5}{2},\tfrac{1-50}{2},\tfrac{-5+1}{2}\bigr)=-2$, from choosing C. The same recipe handles more players or extra turns: write the recurrence for who controls each state. Games with hidden information (poker), with non-opposed utilities, or with simultaneous moves are not game trees of this kind (@sec-ai-games-simultaneous-games).

A game is *solved* when the outcome of perfect play (both players following minimax policies) is known: tic-tac-toe, Nim and Connect Four are solved from every position, checkers and Othello from the start, while chess and Go are not, even though programs play them better than people.

<!-- Added 2026-11-19 from UC Berkeley CS188 (Fall 2025), Lecture 6 (minimax as adversarial search) and Lecture 7 (expectimax, modelling assumptions, mixed layers, multi-agent utilities), in our own wording; the example values were checked by hand and by a short Python computation. -->

::: {#def-multi-agent-game-tree .definition name="Game trees with several utilities"}

In a turn-based game with players $1,\dots,k$ whose interests are not opposed, each end state carries a vector $(U_1(s),\dots,U_k(s))$ of utilities, one per player. The value of a state is a vector too: at an end state it is the utility vector, and at a state where player $p$ moves it is the value of the child whose $p$-th component is largest.

:::

Minimax is the special case $k=2$, $U_2=-U_1$: maximising $U_2$ is minimising $U_1$. With general utilities the players may cooperate or compete, depending only on the numbers.

::: {#exm-multi-agent-game-tree .example name="Cooperation without agreement"}

Player 1 chooses $L$ or $R$, then player 2 chooses one of two end states. Under $L$ the utility vectors are $(3,3)$ and $(1,2)$, under $R$ they are $(4,0)$ and $(2,1)$. Player 2 picks $(3,3)$ under $L$ and $(2,1)$ under $R$, so player 1 compares first components $3$ and $2$ and chooses $L$. The outcome $(3,3)$ is good for both, although neither player cares about the other; the state $(4,0)$, best for player 1, is never reached, because player 2 would not choose it.

:::

::: {#rmk-game-trees-modelling .remark name="Which model of the opponent?"}

Expectimax needs a probabilistic model of the other agents, and minimax assumes the worst. Each can fail: a minimax agent facing a random opponent plays too cautiously (in a game where it could win by taking a risk, it may hold back forever), and an expectimax agent facing an adversary walks into traps. The value of $(\pi_{\text{exptmax}},\pi_{\min})$ in the chain of inequalities above is the price of wrongly assuming randomness. Expectimax also prunes poorly: a chance node's value depends on every child, so without bounds on the utilities no child can be skipped; with known bounds, such as utilities in $[0,10]$, a partly evaluated chance node can sometimes be bounded well enough to prune.

:::
