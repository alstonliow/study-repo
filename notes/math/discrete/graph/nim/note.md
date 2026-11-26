---
title: "Nim"
sources: [cs97si-5]
requires: [math/discrete/graph/winning-positions]
status: draft
---

<!-- Added 2026-11-26 from Stanford CS 97SI (Winter 2011-12), Lecture 5 (Nim), in our own wording; proofs written out in steps. The example and figure are our own. -->

Nim is the impartial game (@def-impartial-game) that all others reduce to (@sec-math-discrete-graph-sprague-grundy). Its losing positions have a closed form in terms of the bitwise exclusive or, written $\oplus$: binary addition without carries.

::: {#def-nim .definition name="Nim, nim-sum"}

A position of *Nim* is a tuple $(a_1,\dots,a_k)$ of non-negative integers (pile sizes); a move decreases one $a_i$ to any smaller non-negative value. The player who cannot move (all piles empty) loses. The *nim-sum* of the position is $a_1\oplus a_2\oplus\dots\oplus a_k$.

:::

::: {#thm-bouton .theorem name="Bouton's theorem"}

A Nim position is losing if and only if its nim-sum is $0$. From a position with nim-sum $s\ne0$, a winning move is to replace a pile $a_i$ whose binary expansion has a $1$ in the highest bit of $s$ by $a_i\oplus s<a_i$.

:::

::: {.proof}

1. By @thm-winning-positions it suffices to show: (a) the empty position has nim-sum $0$; (b) every move from a position of nim-sum $0$ leads to a non-zero nim-sum; (c) from every position of non-zero nim-sum some move leads to nim-sum $0$. Then the positions of nim-sum $0$ are exactly the L positions, by induction on the total number of stones.

2. *(a)* The nim-sum of zeros is $0$.

3. *(b)* A move changes one pile from $a_i$ to $a_i'\ne a_i$, so the nim-sum changes from $s$ to $s\oplus a_i\oplus a_i'$. Since $a_i\oplus a_i'\ne0$, a nim-sum $s=0$ becomes non-zero.

4. *(c)* Let $s\ne0$ and let $2^j$ be its highest set bit. An odd number of piles have bit $j$ set, so some $a_i$ does. In $a_i\oplus s$, bit $j$ is cleared and the higher bits of $a_i$ are unchanged, so $a_i\oplus s<a_i$ and replacing $a_i$ by it is a legal move. The new nim-sum is $s\oplus a_i\oplus(a_i\oplus s)=0$.

:::

::: {#exm-nim-1 .example name="Piles 3, 4, 5"}

In binary $3=011$, $4=100$, $5=101$, so the nim-sum is $011\oplus100\oplus101=010=2$ and the first player wins. The highest bit of $2$ is bit $1$, set only in $3$; replace $3$ by $3\oplus2=1$. The position $(1,4,5)$ has nim-sum $001\oplus100\oplus101=0$.

:::

::: {#fig-nim-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.75cm,y=0.75cm]
\foreach \p/\n in {1/4,2/5} {
  \foreach \s in {1,...,\n} \node[ball] at (\p*3,\s) {};
  \node[lab,tick] at (\p*3,0) {$\n$};
}
\foreach \s in {2,3} \node[ball, opacity=0.25] at (0,\s) {};
\node[lab,tick] at (0,0) {$3$};
\node[hl ball] at (0,1) {};
\node[lab,note,anchor=west] at (9,4.5) {\texttt{3 = 011}};
\node[lab,note,anchor=west] at (9,3.7) {\texttt{4 = 100}};
\node[lab,note,anchor=west] at (9,2.9) {\texttt{5 = 101}};
\draw[faint] (9,2.4) -- (11.6,2.4);
\node[lab,note,anchor=west] at (9,1.9) {\texttt{\ \ \ \ 010}};
\node[lab,note,anchor=west] at (9,0.9) {take 2 from the first pile};
\end{tikzpicture}
\end{center}
```

@exm-nim-1: the nim-sum of $3,4,5$ is $2$; taking two stones from the first pile (hollow) leaves nim-sum $0$.

:::

::: {#rmk-nim-1 .remark name="Misère Nim"}

If instead the player who takes the last stone *loses*, the answer changes only at the end: play as in normal Nim unless the move would leave only piles of size $1$; then leave an odd number of them. Equivalently, a position is losing exactly when the nim-sum is $0$ and some pile exceeds $1$, or the nim-sum is $1$ and all piles are at most $1$.

:::
