---
title: "Coin Change"
sources: []
requires: [cs/algorithm-design/subproblem-design]
status: draft
---

<!-- Added 2026-11-26 for the CSES dynamic-programming problems, in our own wording. TODO: add a source. -->

Given coin values $c_1,\dots,c_k$ (positive integers, unlimited supply of each) and a target $x$, three questions have almost the same dynamic program: the fewest coins, the number of ordered sequences, and the number of unordered combinations that sum to $x$.

::: {#def-coin-change .definition name="Coin-change subproblems"}

For $0\le s\le x$ define

$$
m(s)=\min\{\text{number of coins with sum } s\},\qquad
o(s)=\#\{\text{ordered sequences with sum } s\},
$$

with $m(0)=0$ and $o(0)=1$ (the empty sequence), and $m(s)=\infty$ if no multiset has sum $s$. For *combinations* let $u_j(s)$ be the number of multisets with sum $s$ that use only the coins $c_1,\dots,c_j$.

:::

::: {#thm-coin-change .theorem name="Coin-change recurrences"}

For $s\ge1$,

$$
m(s)=1+\min_{c_i\le s} m(s-c_i),\qquad o(s)=\sum_{c_i\le s}o(s-c_i),
$$

and $u_0(0)=1$, $u_0(s)=0$ for $s>0$, $u_j(s)=u_{j-1}(s)+u_j(s-c_j)$ for $c_j\le s$ (and $u_j(s)=u_{j-1}(s)$ otherwise). Each table is filled in $O(kx)$ time.

:::

::: {.proof}

1. *Minimum.* In an optimal sequence for sum $s$ look at the last coin $c_i$. Removing it leaves a sequence for $s-c_i$ that must itself be optimal, otherwise replacing it would improve the whole. Conversely adding any coin $c_i\le s$ to an optimal solution for $s-c_i$ gives a solution for $s$.

2. *Ordered sequences.* Classify the nonempty ordered sequences with sum $s$ by their last element $c_i$. Deleting it is a bijection with the sequences of sum $s-c_i$.

3. *Combinations.* A multiset over $c_1,\dots,c_j$ with sum $s$ either contains no coin $c_j$ (counted by $u_{j-1}(s)$), or contains at least one: removing one copy is a bijection with the multisets over $c_1,\dots,c_j$ with sum $s-c_j$.

4. *Time.* Each of the $x+1$ entries (times $k$ coin values in the combination table) takes $O(k)$, resp. $O(1)$, work.

:::

::: {#exm-coin-change-1 .example name="Coins 1, 3, 4 and target 6"}

The minimum is $m(6)=2$ (as $3+3$). The ordered counts are $o=(1,1,1,2,4,6,9)$ for $s=0..6$: for instance $o(4)=o(3)+o(1)+o(0)=2+1+1=4$. Unordered, the sum $6$ can be formed as $1^6$, $1^3 3$, $3^2$, $1^2 4$, so $u_3(6)=4$.

:::

::: {#fig-coin-change-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.9cm,y=0.9cm]
\foreach \s/\m/\o in {0/0/1,1/1/1,2/2/1,3/1/2,4/1/4,5/2/6,6/2/9} {
  \draw[cell frame] (\s,0) rectangle +(0.9,0.6); \node[lab] at (\s+0.45,0.3) {$\m$};
  \draw[cell frame] (\s,-0.8) rectangle +(0.9,0.6); \node[lab] at (\s+0.45,-0.5) {$\o$};
  \node[lab,tick] at (\s+0.45,0.9) {$\s$};
}
\node[lab,anchor=east] at (-0.1,0.3) {$m(s)$};
\node[lab,anchor=east] at (-0.1,-0.5) {$o(s)$};
\draw[hl cell] (6,0) rectangle +(0.9,0.6);
\end{tikzpicture}
\end{center}
```

@exm-coin-change-1: the tables for coins $1,3,4$ up to $s=6$.

:::

::: {#rmk-coin-change-1 .remark name="Order of the loops"}

The ordered count and the combination count differ only in the loop order. Looping over $s$ outside and coins inside counts sequences (every order of the same coins is counted); looping over coins outside and sums inside counts multisets, because each coin value is introduced once, in a fixed order. This is the same pattern as unbounded knapsack (@sec-cs-algorithm-design-knapsack) with all values equal to $1$.

:::
