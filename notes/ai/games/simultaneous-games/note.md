---
title: "Simultaneous Zero-Sum Games"
sources: [cs221-15]
requires: [ai/games/game-trees]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 15 (simultaneous zero-sum games, pure and mixed strategies, minimax theorem), in our own wording; proofs written out in steps. The minimax theorem is stated without proof (the lecture cites linear programming duality). -->

In rock-paper-scissors both players move at once, so there is no game tree: neither player sees the other's move before choosing.

::: {#def-matrix-game .definition name="Single-move simultaneous zero-sum game"}

Players A and B choose actions $a$ and $b$ at the same time from finite sets; A receives $V(a,b)$ and B receives $-V(a,b)$, where $V$ is the *payoff matrix*. A *pure strategy* is a single action; a *mixed strategy* is a probability distribution $\pi$ over actions. The value of a pair of mixed strategies is

$$
V(\pi_A,\pi_B)=\sum_a\sum_b\pi_A(a)\,\pi_B(b)\,V(a,b).
$$

:::

::: {#exm-two-finger-morra .example name="Two-finger Morra"}

Each player shows $1$ or $2$ fingers. If both show $1$, B pays A $2$; if both show $2$, B pays A $4$; otherwise A pays B $3$. So $V(1,1)=2$, $V(2,2)=4$ and $V(1,2)=V(2,1)=-3$. If both players mix uniformly, the value is $\tfrac14(2-3-3+4)=0$.

:::

A wants to maximize $V$ and B to minimize it, simultaneously. To break the deadlock, let one player commit first and reveal the strategy.

::: {#prp-going-second-no-worse .proposition name="Going second is no worse"}

For pure strategies, $\displaystyle\max_a\min_bV(a,b)\le\min_b\max_aV(a,b)$. In Morra the left side is $-3$ and the right side is $2$.

:::

::: {.proof}

1. For all $a$ and $b'$, $\min_bV(a,b)\le V(a,b')\le\max_{a'}V(a',b')$.

2. The left end does not depend on $b'$ and the right end does not depend on $a$, so maximizing over $a$ and minimizing over $b'$ keeps the inequality.

3. In Morra each row of $V$ has minimum $-3$ and the columns have maxima $2$ and $4$.

:::

::: {#prp-second-player-pure .proposition name="The second player can play a pure strategy"}

For every mixed strategy $\pi_A$, $\displaystyle\min_{\pi_B}V(\pi_A,\pi_B)=\min_bV(\pi_A,b)$, where $b$ ranges over pure strategies.

:::

::: {.proof}

1. $V(\pi_A,\pi_B)=\sum_b\pi_B(b)\,V(\pi_A,b)$ is an average of the numbers $V(\pi_A,b)$ with weights $\pi_B(b)$.

2. An average is at least the smallest of the numbers, and equals it when all the weight is on that $b$.

:::

::: {#exm-morra-mixed .example name="Optimal mixing in Morra"}

If A commits to $\pi_A=(p,1-p)$, B's two pure replies give $V(\pi_A,1)=2p-3(1-p)=5p-3$ and $V(\pi_A,2)=-3p+4(1-p)=-7p+4$. B takes the smaller, so A chooses $p$ to maximize $\min(5p-3,-7p+4)$. The first line increases and the second decreases, so the maximum is where they cross: $5p-3=-7p+4$, $p=\tfrac7{12}$, value $-\tfrac1{12}$. If instead B commits to $(q,1-q)$ first, A's replies give $5q-3$ and $-7q+4$, and B minimizes their maximum, again at $q=\tfrac7{12}$ with value $-\tfrac1{12}$.

:::

::: {#fig-simultaneous-games-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=4.5cm,y=0.45cm]
\draw[->] (0,0) -- (1.1,0) node[lab,anchor=north east] {$p=\pi_A(1)$};
\draw[->] (0,-3.5) -- (0,4.5) node[lab,anchor=north west] {value};
\foreach \x in {0.5,1} { \node[lab,tick] at (\x,-0.6) {\x}; }
\foreach \y in {-3,4} { \node[lab,tick] at (-0.05,\y) {\y}; }
\draw[faint] (0,-3) -- (1,2) node[lab,anchor=west] {B plays $1$: $5p-3$};
\draw[faint] (0,4) -- (1,-3) node[lab,anchor=west] {B plays $2$: $-7p+4$};
\draw[hl] (0,-3) -- ({7/12},{-1/12}) -- (1,-3);
\node[hl dot] at ({7/12},{-1/12}) {};
\node[lab,anchor=south] at ({7/12},0.3) {$(\frac7{12},-\frac1{12})$};
\end{tikzpicture}
\end{center}
```

Two-finger Morra when A commits to $(p,1-p)$: the value of each of B's pure replies, and their minimum (highlighted), which A maximizes at $p=\tfrac7{12}$.

:::

::: {#thm-von-neumann-minimax .theorem name="Minimax theorem (von Neumann)"}

For every simultaneous two-player zero-sum game with finitely many actions,

$$
\max_{\pi_A}\min_{\pi_B}V(\pi_A,\pi_B)=\min_{\pi_B}\max_{\pi_A}V(\pi_A,\pi_B),
$$

where $\pi_A,\pi_B$ range over mixed strategies.

:::

The common number is the *value of the game*. With mixed strategies the order of play does not matter: revealing an optimal mixed strategy costs nothing, and if both players use optimal strategies, a player who deviates can only do worse. The theorem follows from duality in linear programming, and the optimal strategies are found by linear programming.

::: {#def-matrix-game-lp .definition name="Optimal mixed strategy by linear programming"}

By @prp-second-player-pure, A's optimal mixed strategy solves the linear program

$$
\text{maximize } v\quad\text{subject to}\quad\sum_a\pi_A(a)\,V(a,b)\ge v\ \text{ for every action }b,\qquad\sum_a\pi_A(a)=1,\qquad\pi_A\ge0,
$$

in the variables $\pi_A(a)$ and $v$; its optimal $v$ is the value of the game. B's strategy solves the analogous program with the inequalities reversed and $v$ minimized.

:::

In Morra the constraints are $5p-3\ge v$ and $-7p+4\ge v$, and the optimum is the crossing point of @fig-simultaneous-games-1: both players' optimal strategies are $(\tfrac7{12},\tfrac5{12})$ and the value is $-\tfrac1{12}$, so the game slightly favours B.
