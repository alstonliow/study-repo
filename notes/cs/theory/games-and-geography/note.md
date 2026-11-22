---
title: "Games and PSPACE"
sources: [mit18404j-19]
requires: [cs/theory/savitch-theorem]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lecture 19, in our own wording; proofs written out in steps. -->

Alternating quantifiers are a game: the $\exists$ player wants the formula true, the $\forall$ player wants it false. Deciding who wins a natural game is therefore often PSPACE-complete.

## The formula game

::: {#def-formula-game .definition name="Formula game"}

Let $\phi=\exists x_1\,\forall x_2\,\exists x_3\cdots Q x_m\,[\psi]$ be a quantified Boolean formula with alternating quantifiers. In the *formula game*, players E and A choose values of $x_1,x_2,\dots$ in order, E choosing the variables under $\exists$ and A those under $\forall$. E wins if $\psi$ is true at the end. $\mathit{FORMULAGAME}=\{\langle\phi\rangle: \text{E has a winning strategy}\}$.

:::

::: {#thm-formula-game-pspace-complete .theorem name="The formula game is PSPACE-complete"}

:::

::: {.proof}

1. E has a winning strategy iff $\phi$ is true: "E can choose $x_1$ so that, whatever A chooses for $x_2$, E can choose $x_3$ so that …" is word for word the meaning of the quantifiers.

2. So $\mathit{FORMULAGAME}=\mathit{TQBF}$ restricted to alternating quantifiers. Any quantified formula can be put in that form by inserting dummy quantified variables that do not occur in $\psi$, so the restricted problem is still PSPACE-complete (@thm-tqbf-pspace-complete).

:::

## Generalized geography

::: {#def-generalized-geography .definition name="Generalized geography"}

Given a directed graph $G$ and a start node $b$, player I takes $b$; then players II and I alternately choose a node that extends the path chosen so far along an edge and has not been used before. A player who cannot move loses. $\mathit{GG}=\{\langle G,b\rangle: \text{player I has a winning strategy}\}$.

:::

::: {#exm-geography .example name="A small game"}

Take nodes $1,2,3,4,6$ with edges $1\to2$, $1\to4$, $2\to3$, $2\to4$, $3\to1$, $3\to6$, $4\to2$, $4\to3$, and $b=1$. Player I wins by never entering node $3$ while $6$ is still free: if II goes to $2$, I goes to $4$; II is forced to $3$, and I takes $6$, after which II is stuck. If II goes to $4$, I goes to $2$, and again II must take $3$ and I takes $6$. Entering $3$ himself would lose, since II then takes $6$.

:::

::: {#fig-games-and-geography-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[hl state] (1) at (0,0) {$1$};
\node[state] (2) at (2.2,1.1) {$2$};
\node[hl state] (4) at (2.2,-1.1) {$4$};
\node[state] (3) at (4.4,0) {$3$};
\node[hl state] (6) at (6.4,0) {$6$};
\draw[start] (1.west) -- ++(-0.6,0);
\draw[trans, hl] (1) -- (2);
\draw[trans] (1) -- (4);
\draw (2) edge[trans, hl, bend left=12] (4);
\draw (4) edge[trans, bend left=12] (2);
\draw[trans] (2) -- (3);
\draw[trans, hl] (4) -- (3);
\draw[trans, hl] (3) -- (6);
\draw (3) edge[trans, bend right=40] (1);
\node[lab, note] at (3.2,-2.2) {play: I $1$, II $2$, I $4$, II $3$, I $6$; II cannot move};
\end{tikzpicture}
\end{center}
```

The game of @exm-geography. The highlighted path is a play in which player I (shaded nodes) follows the winning strategy.

:::

::: {#thm-gg-pspace-complete .theorem name="Generalized geography is PSPACE-complete"}

:::

::: {.proof}

1. $\mathit{GG}\in\mathrm{PSPACE}$: recursively, player I wins from $b$ iff for every move of II to some $c$, I wins the game on $G-b$ starting from $c$ (with the roles exchanged one more time). The recursion depth is at most the number of nodes and each level stores one node, so the space is polynomial.

2. Reduce $\mathit{FORMULAGAME}$ to $\mathit{GG}$; we may assume $\phi$ starts and ends with $\exists$ and that $\psi$ is in conjunctive normal form (as in the proof of @thm-tqbf-pspace-complete). Player I plays E and player II plays A.

3. For each variable $x_i$ build a *diamond*: from its top node the path can go left (meaning $x_i$ true) or right ($x_i$ false), and the two sides meet at its bottom node, which is the top of the next diamond. The player who chooses at the top of diamond $i$ is E for odd $i$ and A for even $i$, by the alternation of moves.

4. After the last diamond, A moves to a node of his choice $c_j$ for a clause he claims is false. From $c_j$, E chooses a literal of $c_j$; the literal node for $x_i$ has an edge into the left side of diamond $i$, and for $\bar x_i$ into the right side.

5. If the chosen side of diamond $i$ was taken earlier (the literal is true), that node is used, so A cannot move and loses. If not (the literal is false), A moves to it and E is stuck. So E wins iff every clause A can pick has a true literal, iff the assignment satisfies $\psi$; and player I has a winning strategy in $G$ iff E has one in the formula game.

6. The graph has polynomial size and is built in polynomial time.

:::

::: {#fig-games-and-geography-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.9cm, y=0.8cm]
\foreach \i/\y in {1/0,2/-2,3/-4} {
  \node[small vertex] (t\i) at (0,\y) {};
  \node[small vertex] (l\i) at (-1,\y-1) {};
  \node[small vertex] (r\i) at (1,\y-1) {};
  \draw[trans] (t\i) -- (l\i); \draw[trans] (t\i) -- (r\i);
  \node[lab, note] at (-1.7,\y-1) {$x_\i$};
  \node[lab, note] at (1.55,\y-0.6) {$\bar x_\i$};
}
\node[small vertex] (end) at (0,-6) {};
\foreach \i/\j in {1/t2,2/t3,3/end} {\draw[trans] (l\i) -- (\j); \draw[trans] (r\i) -- (\j);}
\node[lab, note, anchor=west] at (0.35,0) {E};
\node[lab, note, anchor=west] at (0.35,-2) {A};
\node[lab, note, anchor=west] at (0.35,-4) {E};
\node[small vertex] (c1) at (2.6,-7.2) {$c_1$};
\node[small vertex] (c2) at (4.2,-7.2) {$c_2$};
\draw[trans] (end) -- (c1); \draw[trans] (end) -- (c2);
\node[small vertex] (p) at (4.4,-4.2) {};
\node[small vertex] (q) at (2.6,-5.4) {};
\draw[trans] (c1) -- (p); \draw[trans] (c1) -- (q);
\draw[trans, hl] (p) -- (r1);
\draw[trans, hl] (q) -- (r2);
\node[lab, note, anchor=west] at (4.65,-4.2) {$\bar x_1$};
\node[lab, note, anchor=west] at (2.85,-5.4) {$\bar x_2$};
\end{tikzpicture}
\end{center}
```

The reduction of @thm-gg-pspace-complete for a clause $c_1=(\bar x_1\vee\bar x_2\vee\cdots)$. Diamonds record the assignment; A then picks a clause, E picks a literal, and the literal's edge returns to a diamond side, which is already used exactly when the literal is true.

:::
