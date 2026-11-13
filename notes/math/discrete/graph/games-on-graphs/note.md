---
title: "Games on graphs"
sources: [fit1058-cn-12.6]
requires: []
status: draft
---

<!-- Migrated from 1058note notes/chapters/10-graph-theory.tex: Games on graphs. -->

### Shannon’s Switching Game

::: {#def-shannon-s-switching-game .definition name="Shannon's Switching Game"}

The game is played on a connected graph $G$ with two *terminals* $s,t$. Two players, *Join* and *Cut*, take turns. Join thickens an edge that is not yet crossed out; Cut crosses out an edge that is not yet thickened. Join wins as soon as the thickened edges contain a path from $s$ to $t$. Cut wins as soon as $s$ and $t$ are in different components of the graph of edges not crossed out.

:::

```{=latex}
\begin{center}
\begin{tikzpicture}[every node/.style={circle,draw,fill=white,inner sep=1.5pt,minimum size=6mm}]
\node (s) at (0,0) {$s$};
\node (a) at (1.5,1) {$a$};
\node (b) at (1.5,-1) {$b$};
\node (t) at (3,0) {$t$};
\draw (s)--(a) (s)--(b) (a)--(t) (b)--(t) (a)--(b);
\end{tikzpicture}
\end{center}
```

::: {#exm-games-on-graphs-1 .example}

On the graph above, with Join first: Join thickens $\{s,a\}$; Cut crosses out $\{a,t\}$; Join thickens $\{a,b\}$; Cut crosses out $\{b,t\}$. Now $s$ and $t$ are separated, so Cut wins. Join’s second move was a blunder: thickening $\{b,t\}$ instead would have threatened both $s,b,t$ and $s,a,b,t$, and Cut cannot block both.

:::

::: {#prp-no-draws .proposition name="No draws"}

Every play of Shannon’s Switching Game ends with a winner.

:::

::: {.proof}

If play continued until every edge were thickened or crossed out, then the thickened edges would either contain a path from $s$ to $t$, so Join wins, or not, in which case $s$ and $t$ are separated in the graph of remaining edges, so Cut wins. So the game always ends with a winner, possibly earlier.

:::

::: {.remark name="Four possible cases"}

Since there are no draws, on each graph exactly one of these holds: Join has a winning strategy whoever starts; Cut has a winning strategy whoever starts; the first player has a winning strategy; or the second player has a winning strategy. In fact the last case never happens.

:::

::: {#thm-the-second-player-never-has .theorem name="The second player never has the advantage"}

There is no graph on which the second player has a winning strategy whichever role they play.

:::

::: {.proof}

We use strategy stealing. Suppose, for contradiction, that on some graph the second player has a winning strategy $\sigma$, whichever role they play. The first player makes an arbitrary first move, and then plays as if they were the second player following $\sigma$, ignoring their extra move. In this game an extra thickened (or crossed-out) edge never hurts its owner, so the first player still wins, as $\sigma$ guarantees. But then the second player’s $\sigma$ is not a winning strategy, a contradiction.

:::

::: {.remark name="Bridg-It"}

A commercial version of this game, Bridg-It, was invented by David Gale and sold from 1960.

:::

### Slither

::: {#def-slither .definition name="Slither"}

Two players take turns choosing edges so that the chosen edges always form a path. The first move is any edge. Each later edge must have one endpoint at either end of the current path and its other endpoint not yet on the path. The first player who cannot move loses.

:::

::: {.remark name="Impartial vs.\ partisan"}

In Slither both players make the same kind of move, so the game is *impartial*; Shannon’s Switching Game, where one player thickens and the other crosses out, is *partisan*. Unlike Shannon’s game, Slither has graphs where the first player has a winning strategy and also graphs where the second player does.

:::
