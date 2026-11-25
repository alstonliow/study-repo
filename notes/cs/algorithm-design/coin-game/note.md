---
title: "Alternating Coin Game"
sources: [mit6006-16, mit6006r-16, mit6046-10]
requires: [cs/algorithm-design/subproblem-design]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 16 and Recitation 16, and MIT 6.046 (Spring 2015), Lecture 10, in our own wording; examples our own (checked by computation); proofs written out in steps. Split from cs/algorithm-design/subproblem-design on 2026-11-25 (one problem per note, SPEC §8.6). -->

A two-player game is solved by *expanding* the subproblems with whose turn it is, or by using that the game is zero-sum.

::: {#exm-coin-game .example name="Alternating coin game"}

Coins with values $v_0,\dots,v_{n-1}$ lie in a row. Two players alternately take the first or the last remaining coin; I move first. How much can I guarantee, if my opponent also plays as well as possible? For $5,10,100,25$ I can guarantee $105$ of the $140$: I take $5$, and whatever the opponent takes, I then get $100$.

*First solution*, using that the game is zero-sum (I get exactly what the opponent does not).

1. *Subproblems:* $x(i,j)$, the most that the player to move can guarantee from coins $i,\dots,j$, for $0\le i\le j<n$.
2. *Relation:* the player takes coin $i$ or coin $j$; the opponent then guarantees $x(i+1,j)$ or $x(i,j-1)$ of the rest:
   $$x(i,j)=\max\Bigl\{\sum_{k=i}^jv_k-x(i+1,j),\ \sum_{k=i}^jv_k-x(i,j-1)\Bigr\}.$$
3. *Order:* increasing $j-i$. 4. *Base:* $x(i,i)=v_i$. 5. *Original:* $x(0,n-1)$.
6. *Time:* $\Theta(n^2)$ subproblems; with all sums $\sum_{k=i}^jv_k$ precomputed from prefix sums, $O(1)$ work each, $\Theta(n^2)$ in total.

*Second solution*, by *expanding* the subproblems with whose turn it is.

1. *Subproblems:* $x(i,j,p)$, the most that *I* can guarantee from coins $i,\dots,j$ when player $p\in\{\text{me},\text{you}\}$ moves next.
2. *Relation:*
   $$x(i,j,\text{me})=\max\{v_i+x(i+1,j,\text{you}),\ v_j+x(i,j-1,\text{you})\},$$
   $$x(i,j,\text{you})=\min\{x(i+1,j,\text{me}),\ x(i,j-1,\text{me})\}.$$
3. *Order:* increasing $j-i$. 4. *Base:* $x(i,i,\text{me})=v_i$, $x(i,i,\text{you})=0$.
5. *Original:* $x(0,n-1,\text{me})$. 6. *Time:* $\Theta(n^2)$.

:::

```{=latex}
\begin{algorithm}
\caption{Alternating coin game}
\begin{algorithmic}
\INPUT Coin values $v_0,\dots,v_{n-1}$
\OUTPUT The most the first player can guarantee, $x(0,n-1)$
\STATE $P(0)\gets0$; $P(k+1)\gets P(k)+v_k$ for $k=0,\dots,n-1$ \COMMENT{prefix sums}
\FOR{$i=0$ to $n-1$}
    \STATE $x(i,i)\gets v_i$
\ENDFOR
\FOR{$\ell=1$ to $n-1$}
    \FOR{$i=0$ to $n-1-\ell$}
        \STATE $j\gets i+\ell$; $S\gets P(j+1)-P(i)$
        \STATE $x(i,j)\gets\max\{S-x(i+1,j),\ S-x(i,j-1)\}$
    \ENDFOR
\ENDFOR
\RETURN $x(0,n-1)$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-subproblem-design-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (0.750,0.750);
\node[lab] at (0.375,0.375) {$5$};
\draw[cell frame] (0.750,0.000) rectangle (1.500,0.750);
\node[lab] at (1.125,0.375) {$10$};
\draw[cell frame] (1.500,0.000) rectangle (2.250,0.750);
\node[lab] at (1.875,0.375) {$105$};
\draw[hl cell] (2.250,0.000) rectangle (3.000,0.750);
\node[lab] at (2.625,0.375) {$105$};
\node[lab,tick,anchor=east] at (-0.050,0.375) {$i=0$};
\draw[cell frame] (0.750,-0.750) rectangle (1.500,0.000);
\node[lab] at (1.125,-0.375) {$10$};
\draw[cell frame] (1.500,-0.750) rectangle (2.250,0.000);
\node[lab] at (1.875,-0.375) {$100$};
\draw[hl cell] (2.250,-0.750) rectangle (3.000,0.000);
\node[lab] at (2.625,-0.375) {$35$};
\node[lab,tick,anchor=east] at (-0.050,-0.375) {$i=1$};
\draw[cell frame] (1.500,-1.500) rectangle (2.250,-0.750);
\node[lab] at (1.875,-1.125) {$100$};
\draw[hl cell] (2.250,-1.500) rectangle (3.000,-0.750);
\node[lab] at (2.625,-1.125) {$100$};
\node[lab,tick,anchor=east] at (-0.050,-1.125) {$i=2$};
\draw[hl cell] (2.250,-2.250) rectangle (3.000,-1.500);
\node[lab] at (2.625,-1.875) {$25$};
\node[lab,tick,anchor=east] at (-0.050,-1.875) {$i=3$};
\node[lab,tick] at (0.375,0.930) {$j=0$};
\node[lab,tick] at (1.125,0.930) {$j=1$};
\node[lab,tick] at (1.875,0.930) {$j=2$};
\node[lab,tick] at (2.625,0.930) {$j=3$};
\draw[cell frame] (0.000,-3.300) rectangle (0.750,-2.550);
\node[lab] at (0.375,-2.925) {$5$};
\draw[cell frame] (0.750,-3.300) rectangle (1.500,-2.550);
\node[lab] at (1.125,-2.925) {$10$};
\draw[cell frame] (1.500,-3.300) rectangle (2.250,-2.550);
\node[lab] at (1.875,-2.925) {$100$};
\draw[cell frame] (2.250,-3.300) rectangle (3.000,-2.550);
\node[lab] at (2.625,-2.925) {$25$};
\node[lab, anchor=east] at (-0.100,-2.925) {coins};
\end{tikzpicture}
\end{center}
```

The table $x(i,j)$ of the first solution for the coins $5,10,100,25$, filled by increasing $j-i$ from the diagonal $x(i,i)=v_i$. The answer is $x(0,3)=105$. Highlighted cells follow optimal play: from $(0,3)$ the player to move takes coin $0$ (value $5$), leaving $x(1,3)=35$ to the opponent, and so on.

:::
