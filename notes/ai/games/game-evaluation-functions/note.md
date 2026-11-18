---
title: "Evaluation Functions and Depth-Limited Search"
sources: [cs221-13, cs221-14]
requires: [ai/games/alpha-beta-pruning]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 13 (evaluation functions) and Lecture 14 (recap of the chess evaluation function), in our own wording. -->

Alpha-beta pruning is exact but can still take exponential time. To play real games, search stops at a fixed depth and *guesses* the value of the states it stops at.

::: {#def-evaluation-function .definition name="Evaluation function, depth-limited minimax"}

An *evaluation function* $\text{Eval}(s)$ estimates $V_{\text{minmax}}(s)$ from features of the state, using prior knowledge of the game. *Depth-limited minimax* with depth $d_{\max}$ computes $V_{\text{minmax}}(s_{\text{start}},d_{\max})$, where

$$
V_{\text{minmax}}(s,d)=\begin{cases}\text{Utility}(s)&\text{if }\text{IsEnd}(s),\\ \text{Eval}(s)&\text{if }d=0,\\ \max_aV_{\text{minmax}}(\text{Succ}(s,a),d-1)&\text{if }\text{Player}(s)=\text{agent},\\ \min_aV_{\text{minmax}}(\text{Succ}(s,a),d-1)&\text{if }\text{Player}(s)=\text{opp}.\end{cases}
$$

Here $d$ counts the remaining moves.

:::

```{=latex}
\begin{algorithm}
\caption{Depth-limited minimax}
\begin{algorithmic}
\INPUT State $s$, remaining depth $d$, evaluation function $\text{Eval}$
\OUTPUT $V_{\text{minmax}}(s,d)$
\FUNCTION{DepthLimited}{$s,d$}
    \IF{$\text{IsEnd}(s)$} \RETURN $\text{Utility}(s)$ \ENDIF
    \IF{$d=0$} \RETURN $\text{Eval}(s)$ \ENDIF
    \STATE $\mathcal V\gets\{\textsc{DepthLimited}(\text{Succ}(s,a),d-1):a\in\text{Actions}(s)\}$
    \IF{$\text{Player}(s)=\text{agent}$} \RETURN $\max\mathcal V$ \ELSE \RETURN $\min\mathcal V$ \ENDIF
\ENDFUNCTION
\end{algorithmic}
\end{algorithm}
```

::: {#exm-evaluation-function-chess .example name="A chess evaluation function"}

A classic hand-made evaluation function for chess is $\text{Eval}(s)=\text{material}+\text{mobility}+\text{king safety}+\text{centre control}$, with, for example,

$$
\text{material}=10^{100}(K-K')+9(Q-Q')+5(R-R')+3(B-B'+N-N')+(P-P'),\qquad
\text{mobility}=0.1\,(\text{legal moves}-\text{legal moves}'),
$$

where $K,Q,R,B,N,P$ count the agent's kings, queens, rooks, bishops, knights and pawns and primed letters the opponent's.

:::

::: {#rmk-game-evaluation-functions-1 .remark editor="No figure: running depth-limited minimax on a small tree looks exactly like the minimax figure with some subtrees replaced by guessed numbers, and a realistic example (chess) is too large to draw."}

Depth-limited search comes with no guarantee: a position that looks good at the cut-off may lose a few moves later. The evaluation function plays the role of the future-cost heuristic in A* search (@sec-ai-search-a-star-search), and depth-limited search is combined with alpha-beta pruning, using $\text{Eval}$ also to order moves. Instead of designing $\text{Eval}$ by hand it can be learned by self-play with TD learning (@sec-ai-reinforcement-learning-td-learning).

:::
