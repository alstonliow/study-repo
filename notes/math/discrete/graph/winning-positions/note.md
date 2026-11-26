---
title: "Winning and Losing Positions"
sources: [cs97si-5]
requires: [math/discrete/graph/directed-graphs]
status: draft
---

<!-- Added 2026-11-26 from Stanford CS 97SI (Winter 2011-12), Lecture 5 (simple games), in our own wording; proofs written out in steps. The example (moves 1, 3 or 4) and figure are our own; the table was checked by computation. -->

Many contest problems ask who wins a two-player game with perfect play. When both players have the same moves and the game cannot go on for ever, every position is either a win or a loss for the player to move, and a dynamic program over the positions decides which.

::: {#def-impartial-game .definition name="Impartial game, winning and losing positions"}

An *impartial game* is a finite directed acyclic graph (@def-dag) whose vertices are *positions* and whose edges are *moves*. Two players alternately move from the current position along an edge; the player who cannot move loses (*normal play*). A position is *winning* (W) if the player to move can force a win, and *losing* (L) otherwise.

:::

::: {#thm-winning-positions .theorem name="Labelling positions"}

In an impartial game every position is W or L, and

$$
x\text{ is L}\iff\text{every move from }x\text{ leads to a W position}.
$$

In particular a position with no moves is L. Processing the positions in reverse topological order labels them all in time proportional to the number of positions and moves.

:::

::: {.proof}

1. Induct along a reverse topological order (@thm-topological-sort), so that all positions reachable from $x$ are labelled before $x$.

2. If some move leads from $x$ to an L position $y$, the player to move goes to $y$; from $y$ the opponent is to move in a losing position, so whatever they do, the first player can keep winning. So $x$ is W.

3. If every move leads to a W position (or there are no moves), then whatever the player does, the opponent is to move in a winning position and can force a win. So $x$ is L.

4. The two cases are exclusive and exhaustive, and each position looks at each of its moves once.

:::

::: {#exm-winning-positions-1 .example name="Taking 1, 3 or 4 stones"}

A pile has $n$ stones; a move removes $1$, $3$ or $4$ of them, and the player who takes the last stone wins (the player facing $0$ cannot move and loses). The labels for $n=0,\dots,14$ are

$$
\mathrm{L\,W\,L\,W\,W\,W\,W\,L\,W\,L\,W\,W\,W\,W\,L},
$$

so the losing positions appear to be $n\equiv0,2\pmod 7$. Proof by induction on $n$: from $n\equiv1,3,4$ remove $1,3,4$ to reach a multiple of $7$; from $n\equiv5,6$ remove $3$ or $4$ to reach $\equiv2$. From $n\equiv0$ the moves reach $\equiv6,4,3$, and from $n\equiv2$ they reach $\equiv1,6,5$, all winning.

:::

::: {#fig-winning-positions-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.82cm]
\foreach \n/\w in {0/L,1/W,2/L,3/W,4/W,5/W,6/W,7/L,8/W,9/L,10/W,11/W,12/W,13/W,14/L} {
  \if\w L \draw[hl cell] (\n-0.31,-0.31) rectangle (\n+0.31,0.31); \else \draw[cell frame] (\n-0.31,-0.31) rectangle (\n+0.31,0.31); \fi
  \coordinate (c\n) at (\n,0.31); \node[lab] at (\n,0) {\w};
  \node[lab,tick] at (\n,-0.6) {$\n$};
}
\draw[->,hl] (c9) to[bend right=40] node[lab,tick,above] {$-1$} (c8);
\draw[->,faint] (c9) to[bend right=50] (c6);
\draw[->,faint] (c9) to[bend right=55] (c5);
\draw[->,hl] (c12) to[bend right=40] node[lab,tick,above] {$-3$} (c9);
\end{tikzpicture}
\end{center}
```

@exm-winning-positions-1. From the losing position $9$ every move ($-1,-3,-4$) reaches a winning position; from $12$ the winning move is to remove $3$ and leave $9$.

:::

::: {#rmk-winning-positions-1 .remark name="In practice"}

Compute the table for small $n$, guess a pattern (often periodic), and prove it by the same induction, or keep the table if $n$ is small enough. For games with scores rather than win/lose, the same recursion over positions is minimax (@def-game-recurrences), memoised over the positions; for sums of independent games, see @sec-math-discrete-graph-sprague-grundy.

:::
