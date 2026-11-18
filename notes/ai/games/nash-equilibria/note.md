---
title: "Non-Zero-Sum Games and Nash Equilibria"
sources: [cs221-15]
requires: [ai/games/simultaneous-games]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 15 (non-zero-sum games, Nash equilibria), in our own wording. Nash's existence theorem is stated without proof, as in the lecture. -->

Zero-sum games are purely competitive; in *cooperative* games all players share one utility and the problem is plain maximization. Most real interactions lie in between: each player has their own payoff matrix, $V_A(a,b)$ and $V_B(a,b)$, extended to mixed strategies as in @def-matrix-game. The minimax theorem no longer applies, but a weaker notion survives.

::: {#def-nash-equilibrium .definition name="Nash equilibrium"}

A pair of mixed strategies $(\pi_A^*,\pi_B^*)$ is a *Nash equilibrium* if neither player gains by changing strategy alone:

$$
V_A(\pi_A^*,\pi_B^*)\ge V_A(\pi_A,\pi_B^*)\quad\text{for all }\pi_A,\qquad V_B(\pi_A^*,\pi_B^*)\ge V_B(\pi_A^*,\pi_B)\quad\text{for all }\pi_B .
$$

:::

::: {#thm-nash-existence .theorem name="Nash's existence theorem"}

Every game with finitely many players and finitely many actions has at least one Nash equilibrium, possibly in mixed strategies.

:::

::: {#exm-nash-equilibria .example name="Three games"}

1. *Prisoner's dilemma.* Two suspects are separately asked to testify against each other. If both testify, each gets $5$ years; if both refuse, each gets $1$; if only one testifies, that one goes free and the other gets $10$. With utility $-(\text{years})$, testifying is better for each player whatever the other does ($-5>-10$ and $0>-1$), so the only Nash equilibrium is that both testify, with utilities $(-5,-5)$, although both refusing would give $(-1,-1)$ to each.

2. *Two-finger Morra* (@exm-two-finger-morra) as a game with $V_A=V$, $V_B=-V$: the minimax strategies, both $(\tfrac7{12},\tfrac5{12})$, form a Nash equilibrium.

3. *Collaborative Morra*, in which both players receive $V(a,b)$: both showing $1$, both showing $2$, and both playing $(\tfrac7{12},\tfrac5{12})$ are all Nash equilibria, with utilities $2$, $4$ and $-\tfrac1{12}$ for each player.

:::

::: {#fig-nash-equilibria-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=2.1cm,y=0.75cm]
\node[lab] at (1,0) {B testifies}; \node[lab] at (2,0) {B refuses};
\node[lab,anchor=east] at (0.5,-1) {A testifies}; \node[lab,anchor=east] at (0.5,-2) {A refuses};
\begin{scope}[on background layer]\draw[hl box] (0.6,-1.4) rectangle (1.4,-0.6);\end{scope}
\node[lab] at (1,-1) {$(-5,-5)$}; \node[lab] at (2,-1) {$(0,-10)$};
\node[lab] at (1,-2) {$(-10,0)$}; \node[lab] at (2,-2) {$(-1,-1)$};
\draw[->,faint] (2,-1.6) -- (2,-1.3);
\draw[->,faint] (1.6,-2) -- (1.4,-2);
\draw[->,faint] (1.6,-1) -- (1.4,-1);
\draw[->,faint] (1,-1.6) -- (1,-1.3);
\end{tikzpicture}
\end{center}
```

The prisoner's dilemma, each entry (A's utility, B's utility). Arrows show a player improving by changing their own action alone; every arrow leads towards the boxed Nash equilibrium.

:::

::: {#rmk-nash-equilibria-1 .remark name="Stability is not optimality"}

A Nash equilibrium is a notion of stability: it considers one player deviating at a time, and says nothing about whether the outcome is good for anyone, as the prisoner's dilemma shows. In zero-sum games all equilibria share one value (the value of the game); in general games there can be several equilibria with different values, as in collaborative Morra.

:::
