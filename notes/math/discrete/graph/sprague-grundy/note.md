---
title: "The Sprague–Grundy Theorem"
sources: [cs97si-5]
requires: [math/discrete/graph/nim]
status: draft
---

<!-- Added 2026-11-26 from Stanford CS 97SI (Winter 2011-12), Lecture 5 (Grundy numbers), in our own wording; proofs written out in steps. The examples and figure are our own; values checked by computation. -->

Playing several impartial games at once (each turn, move in exactly one of them) is again an impartial game. The Grundy number turns each component into a Nim pile, so the sum is decided by a nim-sum (@thm-bouton).

::: {#def-grundy-number .definition name="mex, Grundy number, sum of games"}

For a finite set $A$ of non-negative integers, $\operatorname{mex}A$ is the smallest non-negative integer not in $A$. The *Grundy number* of a position $x$ of an impartial game (@def-impartial-game) is

$$
g(x)=\operatorname{mex}\{g(y):x\to y\text{ is a move}\}.
$$

The *sum* $G_1+\dots+G_k$ of impartial games has positions $(x_1,\dots,x_k)$; a move makes a move in exactly one component.

:::

::: {#thm-sprague-grundy .theorem name="Sprague–Grundy"}

1. A position $x$ is losing if and only if $g(x)=0$.
2. In a sum of games, $g(x_1,\dots,x_k)=g(x_1)\oplus\dots\oplus g(x_k)$.

Hence $(x_1,\dots,x_k)$ is losing exactly when $g(x_1)\oplus\dots\oplus g(x_k)=0$.

:::

::: {.proof}

1. *Part 1.* A position with no moves has $g=\operatorname{mex}\emptyset=0$. If $g(x)=0$, no move reaches a position of Grundy number $0$; if $g(x)>0$, some move reaches one (as $0$ is in the set). This is the labelling of @thm-winning-positions with "L" read as $g=0$, so by induction the two agree.

2. *Part 2, setup.* Let $s=g(x_1)\oplus\dots\oplus g(x_k)$. By the definition of $g$ it suffices to show, by induction along the game, that no move of the sum reaches a position whose value is $s$, and that for every $t<s$ some move reaches value $t$.

3. *No move keeps $s$.* A move changes one component $x_i$ to $y$ with $g(y)\ne g(x_i)$ (since $g(x_i)$ is the mex of a set containing $g(y)$). By induction the new value is $s\oplus g(x_i)\oplus g(y)\ne s$.

4. *Every $t<s$ is reached.* Let $d=s\oplus t$ and let $2^j$ be its highest set bit. Since $t<s$, bit $j$ is set in $s$ and not in $t$, so some $g(x_i)$ has bit $j$ set, and $g(x_i)\oplus d<g(x_i)$ as in @thm-bouton. By the definition of mex, some move $x_i\to y$ has $g(y)=g(x_i)\oplus d$. The new value is $s\oplus g(x_i)\oplus g(y)=s\oplus d=t$.

5. So the value of the sum is the mex of a set containing every $t<s$ but not $s$, which is $s$.

:::

::: {#exm-sprague-grundy-1 .example name="Two piles, removing 1, 3 or 4"}

In the game of @exm-winning-positions-1 the Grundy numbers for $n=0,\dots,14$ are

$$
0,1,0,1,2,3,2,0,1,0,1,2,3,2,0,
$$

with period $7$; the zeros are the losing positions found there. With two piles of $5$ and $6$ stones (a move removes $1$, $3$ or $4$ from one pile), the value is $g(5)\oplus g(6)=3\oplus2=1\ne0$, so the first player wins. A winning move must bring the first pile to Grundy number $2$: remove $1$ stone, leaving $(4,6)$ with $2\oplus2=0$.

:::

::: {#fig-sprague-grundy-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.82cm]
\foreach \n/\g in {0/0,1/1,2/0,3/1,4/2,5/3,6/2,7/0,8/1,9/0,10/1,11/2,12/3,13/2,14/0} {
  \if\g 0 \draw[hl cell] (\n-0.31,-0.31) rectangle (\n+0.31,0.31); \else \draw[cell frame] (\n-0.31,-0.31) rectangle (\n+0.31,0.31); \fi
  \coordinate (c\n) at (\n,0.31); \node[lab] at (\n,0) {$\g$};
  \node[lab,tick] at (\n,-0.6) {$\n$};
}
\draw[->,faint] (c5) to[bend right=50] node[lab,tick,above] {} (c4);
\draw[->,faint] (c5) to[bend right=55] (c2);
\draw[->,faint] (c5) to[bend right=60] (c1);
\node[lab,note] at (2.6,1.25) {$g(5)=\operatorname{mex}\{2,0,1\}=3$};
\end{tikzpicture}
\end{center}
```

Grundy numbers of @exm-sprague-grundy-1 (zeros shaded). From $5$ the moves reach $4$, $2$ and $1$, with Grundy numbers $2,0,1$, so $g(5)=3$.

:::

::: {#rmk-sprague-grundy-1 .remark name="Using it"}

Split the game into independent parts, compute each part's Grundy numbers by the mex recursion (memoised over positions), and combine with $\oplus$. A Nim pile of size $a$ has Grundy number $a$, so Bouton's theorem is the special case where every component is a single pile. Tables of Grundy numbers are often periodic or follow a simple pattern, which can be found by computing small cases.

:::
