---
title: "Catalan Numbers"
sources: []
requires: [math/discrete/counting/combinations]
status: draft
---

<!-- Added 2026-11-26 for the CSES problems Bracket Sequences I and II, in our own wording. TODO: add a source. -->

How many ways are there to write $n$ pairs of brackets so that they match? The answer is a *Catalan number*, and the same numbers count many other structures.

::: {#def-balanced-brackets .definition name="Balanced bracket sequence"}

A sequence of $n$ opening and $n$ closing brackets is *balanced* if every prefix has at least as many opening as closing brackets. Equivalently, it is a lattice path with steps $(1,+1)$ for "(" and $(1,-1)$ for ")" from $(0,0)$ to $(2n,0)$ that never goes below the $x$-axis. Write $C_n$ for the number of balanced sequences.

:::

::: {#thm-catalan .theorem name="Catalan numbers"}

$$
C_n=\binom{2n}{n}-\binom{2n}{n+1}=\frac1{n+1}\binom{2n}{n},
$$

and $C_0=1$, $C_{n+1}=\sum_{i=0}^{n}C_iC_{n-i}$. More generally, the number of paths from $(0,0)$ to $(m,h)$ with $m\equiv h \pmod 2$ and $h\ge0$ that never go below the axis is $\binom{m}{(m+h)/2}-\binom{m}{(m+h)/2+1}$.

:::

::: {.proof}

1. *All paths.* A path with $n$ up steps and $n$ down steps is determined by the positions of the up steps, so there are $\binom{2n}{n}$ of them.

2. *Reflection.* Call a path *bad* if it touches the line $y=-1$. Reflect the part of a bad path up to its first touch of $y=-1$ in that line. This maps a bad path from $(0,0)$ to $(2n,0)$ to a path from $(0,-2)$ to $(2n,0)$, and the map is a bijection: reflecting again recovers the original, since the first touch point is unchanged.

3. *Counting bad paths.* A path from $(0,-2)$ to $(2n,0)$ has $n+1$ up steps and $n-1$ down steps, so there are $\binom{2n}{n+1}$ of them. Hence $C_n=\binom{2n}{n}-\binom{2n}{n+1}$.

4. *Closed form.* $\binom{2n}{n+1}=\binom{2n}{n}\frac{n}{n+1}$, so the difference is $\binom{2n}{n}\frac1{n+1}$.

5. *Recurrence.* Split a nonempty balanced sequence at the bracket closing the first "(": it has the form $(A)B$ with $A$ balanced of $i$ pairs and $B$ balanced of $n-i$ pairs. This is a bijection onto pairs $(A,B)$, so $C_{n+1}=\sum_i C_iC_{n-i}$.

6. *General case.* The same reflection argument applied to paths ending at height $h$ gives the stated difference of binomial coefficients.

:::

::: {#exm-catalan-numbers-1 .example name="Three pairs"}

$C_3=\binom63-\binom64=20-15=5$: the balanced sequences are $((()))$, $(()())$, $(())()$, $()(())$ and $()()()$. The first terms are $1,1,2,5,14,42,132$.

:::

::: {#fig-catalan-numbers-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.5cm,y=0.5cm]
\draw[gridline] (0,0) -- (6,0);
\draw[faint] (0,-1) -- (6,-1);
\draw[emph] (0,0) -- (1,1) -- (2,2) -- (3,1) -- (4,2) -- (5,1) -- (6,0);
\draw[hl] (0,0) -- (1,-1) -- (2,0) -- (3,1) -- (4,0) -- (5,-1) -- (6,0);
\foreach \x/\y in {0/0,6/0} {\node[dot] at (\x,\y) {};}
\node[lab,tick,anchor=west] at (6.2,-1) {$y=-1$};
\end{tikzpicture}
\end{center}
```

@exm-catalan-numbers-1: a balanced path (solid) and a bad one (highlighted) that touches $y=-1$. Reflecting the bad path up to its first touch gives the bijection of the proof.

:::

::: {#rmk-catalan-numbers-1 .remark name="Counting modulo a prime"}

For large $n$ compute $\binom{2n}{n}-\binom{2n}{n+1}$ modulo a prime $p>2n$ from factorial tables and modular inverses. If the first $k$ brackets are already fixed and leave balance $h\ge0$ (never negative so far), the remaining $m=2n-k$ steps form a path from height $h$ to $0$ that stays $\ge0$. Reflecting at $y=-1$ as in the proof gives $\binom{m}{(m-h)/2}-\binom{m}{(m-h)/2-1}$ such completions. Other objects counted by $C_n$: binary trees with $n$ nodes, triangulations of a convex $(n+2)$-gon, and monotone lattice paths below the diagonal.

:::
