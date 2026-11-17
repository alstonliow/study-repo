---
title: "Integer Subproblems and Pseudopolynomial Time"
sources: [mit6006-18, mit6006r-18]
requires: [cs/dynamic-programming/subproblem-design]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 18 and Recitation 18, in our own wording; examples our own (checked by computation); proofs written out in steps. -->

Another source of subproblems is the integers below a given integer. Then the number of subproblems depends on the *values* in the input, not only on how many numbers there are.

## Rod cutting

::: {#exm-rod-cutting .example name="Rod cutting"}

A rod of integer length $L$ is to be cut into pieces of integer lengths; a piece of length $\ell$ sells for $v(\ell)$. Maximise the total value. For $L=5$ and values $v(1),\dots,v(5)=1,2,3,9,11$, the best is to sell the rod whole for $11$. Taking the piece with the best value per unit length first (length $4$, then $1$) gives only $10$, so the greedy idea fails.

1. *Subproblems:* $x(\ell)$, the most a rod of length $\ell$ yields, for $0\le\ell\le L$.
2. *Relation:* guess the length $p$ of the first piece: $x(\ell)=\max\{v(p)+x(\ell-p):1\le p\le\ell\}$.
3. *Order:* increasing $\ell$. 4. *Base:* $x(0)=0$.
5. *Original:* $x(L)$; storing the best $p$ for each $\ell$ recovers the cuts.
6. *Time:* $L+1$ subproblems with $O(L)$ work: $O(L^2)$.

:::

The input consists of $L+1$ numbers ($L$ and the $L$ values), so $O(L^2)$ is a polynomial in the input size: rod cutting is solved in polynomial time.

## Subset sum

::: {#exm-subset-sum .example name="Subset sum"}

Given positive integers $a_0,\dots,a_{n-1}$ and a target $T$, is there a subset with sum exactly $T$? This is a *decision problem*: the answer is yes or no. For $2,5,9,14$ the target $16=2+14$ is reachable, while $10$ is not.

1. *Subproblems:* $x(i,t)$: does some subset of $a_i,\dots,a_{n-1}$ sum to $t$? For $0\le i\le n$, $0\le t\le T$.
2. *Relation:* $a_i$ is used or not: $x(i,t)=x(i+1,t)\ \text{or}\ \bigl(t\ge a_i\ \text{and}\ x(i+1,t-a_i)\bigr)$.
3. *Order:* decreasing $i$. 4. *Base:* $x(i,0)=$ yes; $x(n,t)=$ no for $t\ge1$.
5. *Original:* $x(0,T)$. 6. *Time:* $O(nT)$ subproblems with $O(1)$ work: $O(nT)$.

Bottom up computes all $(n+1)(T+1)$ entries; top down computes only those reachable from $x(0,T)$, which can be far fewer.

:::

::: {#fig-pseudopolynomial-time-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab,tick] at (0.21,0.2) {0};
\node[lab,tick] at (0.63,0.2) {1};
\node[lab,tick] at (1.05,0.2) {2};
\node[lab,tick] at (1.47,0.2) {3};
\node[lab,tick] at (1.89,0.2) {4};
\node[lab,tick] at (2.31,0.2) {5};
\node[lab,tick] at (2.73,0.2) {6};
\node[lab,tick] at (3.15,0.2) {7};
\node[lab,tick] at (3.57,0.2) {8};
\node[lab,tick] at (3.99,0.2) {9};
\node[lab,tick] at (4.41,0.2) {10};
\node[lab,tick] at (4.83,0.2) {11};
\node[lab,tick] at (5.25,0.2) {12};
\node[lab,tick] at (5.67,0.2) {13};
\node[lab,tick] at (6.09,0.2) {14};
\node[lab,tick] at (6.51,0.2) {15};
\node[lab,tick] at (6.93,0.2) {16};
\node[lab,tick, anchor=east] at (-0.05,-0.21) {$i=0$ ($a_i=2$)};
\draw[hl cell] (0.00,0.00) rectangle (0.42,-0.42);
\draw[cell frame] (0.42,0.00) rectangle (0.84,-0.42);
\draw[hl cell] (0.84,0.00) rectangle (1.26,-0.42);
\draw[cell frame] (1.26,0.00) rectangle (1.68,-0.42);
\draw[cell frame] (1.68,0.00) rectangle (2.10,-0.42);
\draw[hl cell] (2.10,0.00) rectangle (2.52,-0.42);
\draw[cell frame] (2.52,0.00) rectangle (2.94,-0.42);
\draw[hl cell] (2.94,0.00) rectangle (3.36,-0.42);
\draw[cell frame] (3.36,0.00) rectangle (3.78,-0.42);
\draw[hl cell] (3.78,0.00) rectangle (4.20,-0.42);
\draw[cell frame] (4.20,0.00) rectangle (4.62,-0.42);
\draw[hl cell] (4.62,0.00) rectangle (5.04,-0.42);
\draw[cell frame] (5.04,0.00) rectangle (5.46,-0.42);
\draw[cell frame] (5.46,0.00) rectangle (5.88,-0.42);
\draw[hl cell] (5.88,0.00) rectangle (6.30,-0.42);
\draw[cell frame] (6.30,0.00) rectangle (6.72,-0.42);
\draw[hl cell] (6.72,0.00) rectangle (7.14,-0.42);
\node[lab,tick, anchor=east] at (-0.05,-0.63) {$i=1$ ($a_i=5$)};
\draw[hl cell] (0.00,-0.42) rectangle (0.42,-0.84);
\draw[cell frame] (0.42,-0.42) rectangle (0.84,-0.84);
\draw[cell frame] (0.84,-0.42) rectangle (1.26,-0.84);
\draw[cell frame] (1.26,-0.42) rectangle (1.68,-0.84);
\draw[cell frame] (1.68,-0.42) rectangle (2.10,-0.84);
\draw[hl cell] (2.10,-0.42) rectangle (2.52,-0.84);
\draw[cell frame] (2.52,-0.42) rectangle (2.94,-0.84);
\draw[cell frame] (2.94,-0.42) rectangle (3.36,-0.84);
\draw[cell frame] (3.36,-0.42) rectangle (3.78,-0.84);
\draw[hl cell] (3.78,-0.42) rectangle (4.20,-0.84);
\draw[cell frame] (4.20,-0.42) rectangle (4.62,-0.84);
\draw[cell frame] (4.62,-0.42) rectangle (5.04,-0.84);
\draw[cell frame] (5.04,-0.42) rectangle (5.46,-0.84);
\draw[cell frame] (5.46,-0.42) rectangle (5.88,-0.84);
\draw[hl cell] (5.88,-0.42) rectangle (6.30,-0.84);
\draw[cell frame] (6.30,-0.42) rectangle (6.72,-0.84);
\draw[cell frame] (6.72,-0.42) rectangle (7.14,-0.84);
\node[lab,tick, anchor=east] at (-0.05,-1.05) {$i=2$ ($a_i=9$)};
\draw[hl cell] (0.00,-0.84) rectangle (0.42,-1.26);
\draw[cell frame] (0.42,-0.84) rectangle (0.84,-1.26);
\draw[cell frame] (0.84,-0.84) rectangle (1.26,-1.26);
\draw[cell frame] (1.26,-0.84) rectangle (1.68,-1.26);
\draw[cell frame] (1.68,-0.84) rectangle (2.10,-1.26);
\draw[cell frame] (2.10,-0.84) rectangle (2.52,-1.26);
\draw[cell frame] (2.52,-0.84) rectangle (2.94,-1.26);
\draw[cell frame] (2.94,-0.84) rectangle (3.36,-1.26);
\draw[cell frame] (3.36,-0.84) rectangle (3.78,-1.26);
\draw[hl cell] (3.78,-0.84) rectangle (4.20,-1.26);
\draw[cell frame] (4.20,-0.84) rectangle (4.62,-1.26);
\draw[cell frame] (4.62,-0.84) rectangle (5.04,-1.26);
\draw[cell frame] (5.04,-0.84) rectangle (5.46,-1.26);
\draw[cell frame] (5.46,-0.84) rectangle (5.88,-1.26);
\draw[hl cell] (5.88,-0.84) rectangle (6.30,-1.26);
\draw[cell frame] (6.30,-0.84) rectangle (6.72,-1.26);
\draw[cell frame] (6.72,-0.84) rectangle (7.14,-1.26);
\node[lab,tick, anchor=east] at (-0.05,-1.47) {$i=3$ ($a_i=14$)};
\draw[hl cell] (0.00,-1.26) rectangle (0.42,-1.68);
\draw[cell frame] (0.42,-1.26) rectangle (0.84,-1.68);
\draw[cell frame] (0.84,-1.26) rectangle (1.26,-1.68);
\draw[cell frame] (1.26,-1.26) rectangle (1.68,-1.68);
\draw[cell frame] (1.68,-1.26) rectangle (2.10,-1.68);
\draw[cell frame] (2.10,-1.26) rectangle (2.52,-1.68);
\draw[cell frame] (2.52,-1.26) rectangle (2.94,-1.68);
\draw[cell frame] (2.94,-1.26) rectangle (3.36,-1.68);
\draw[cell frame] (3.36,-1.26) rectangle (3.78,-1.68);
\draw[cell frame] (3.78,-1.26) rectangle (4.20,-1.68);
\draw[cell frame] (4.20,-1.26) rectangle (4.62,-1.68);
\draw[cell frame] (4.62,-1.26) rectangle (5.04,-1.68);
\draw[cell frame] (5.04,-1.26) rectangle (5.46,-1.68);
\draw[cell frame] (5.46,-1.26) rectangle (5.88,-1.68);
\draw[hl cell] (5.88,-1.26) rectangle (6.30,-1.68);
\draw[cell frame] (6.30,-1.26) rectangle (6.72,-1.68);
\draw[cell frame] (6.72,-1.26) rectangle (7.14,-1.68);
\node[lab,tick, anchor=east] at (-0.05,-1.89) {$i=4$};
\draw[hl cell] (0.00,-1.68) rectangle (0.42,-2.10);
\draw[cell frame] (0.42,-1.68) rectangle (0.84,-2.10);
\draw[cell frame] (0.84,-1.68) rectangle (1.26,-2.10);
\draw[cell frame] (1.26,-1.68) rectangle (1.68,-2.10);
\draw[cell frame] (1.68,-1.68) rectangle (2.10,-2.10);
\draw[cell frame] (2.10,-1.68) rectangle (2.52,-2.10);
\draw[cell frame] (2.52,-1.68) rectangle (2.94,-2.10);
\draw[cell frame] (2.94,-1.68) rectangle (3.36,-2.10);
\draw[cell frame] (3.36,-1.68) rectangle (3.78,-2.10);
\draw[cell frame] (3.78,-1.68) rectangle (4.20,-2.10);
\draw[cell frame] (4.20,-1.68) rectangle (4.62,-2.10);
\draw[cell frame] (4.62,-1.68) rectangle (5.04,-2.10);
\draw[cell frame] (5.04,-1.68) rectangle (5.46,-2.10);
\draw[cell frame] (5.46,-1.68) rectangle (5.88,-2.10);
\draw[cell frame] (5.88,-1.68) rectangle (6.30,-2.10);
\draw[cell frame] (6.30,-1.68) rectangle (6.72,-2.10);
\draw[cell frame] (6.72,-1.68) rectangle (7.14,-2.10);
\draw[emph] (6.72,0) rectangle (7.14,-0.42);
\end{tikzpicture}
\end{center}
```

The subset sum table for $2,5,9,14$: row $i$, column $t$ is shaded when some subset of $a_i,\dots,a_{n-1}$ sums to $t$. Rows are filled from the bottom ($i=n$: only $t=0$). The framed cell $x(0,16)$ is shaded ($16=2+14$), while $x(0,10)$ is not. The table has $(n+1)(T+1)$ cells, which grows with the value $T$, not just with $n$.

:::

::: {#exm-knapsack .example name="0-1 knapsack"}

Items $i=0,\dots,n-1$ have integer sizes $s_i$ and values $v_i$, and a knapsack has capacity $S$. Choose items of total size at most $S$ and largest total value. With subproblems $x(i,c)$, the best value from items $i,\dots,n-1$ with capacity $c$:
$$x(i,c)=\max\bigl\{x(i+1,c),\ v_i+x(i+1,c-s_i)\ \text{(if }s_i\le c)\bigr\},\qquad x(n,c)=0,$$
and the answer $x(0,S)$, in $O(nS)$ time. Rod cutting is the *unbounded* version, where each piece length may be used any number of times (relation $x(c)=\max_i\{v_i+x(c-s_i)\}$), and subset sum is the case $v_i=s_i$ with the question whether the value $S$ is reached.

:::

## Polynomial or not?

Is $O(nT)$ polynomial? The input is $n+1$ numbers, each fitting in a word, but a word can have $w$ bits for large $w$, so $T$ can be as large as $2^w$. Taking $w=n$, the running time $O(n2^n)$ is exponential in the input size. The running time is polynomial in the *values*, not in the *size*.

::: {#def-pseudopolynomial .definition name="Strongly polynomial, pseudopolynomial, weakly polynomial"}

Measure the input size $N$ in words. An algorithm runs in

1. *(strongly) polynomial time* if its running time is $O(N^c)$ for a constant $c$;
2. *pseudopolynomial time* if its running time is bounded by a polynomial in $N$ and the largest integer $U$ in the input;
3. *weakly polynomial time* if its running time is bounded by a polynomial in $N$ and $\log U$, the number of bits of the input integers.

:::

A pseudopolynomial algorithm is polynomial when the integers are polynomially bounded, $U=N^{O(1)}$. Subset sum and knapsack ($O(nT)$, $O(nS)$), counting sort ($O(n+u)$), building a direct access array ($O(n+u)$), and computing $F_n$ with $O(n)$ additions are pseudopolynomial; radix sort, $O(n\log_nu)$, is weakly polynomial. Whether subset sum has a polynomial algorithm is the P versus NP question in disguise (@sec-cs-theory-complexity-classes): it is NP-complete, so a polynomial algorithm is not expected.

::: {#rmk-pseudopolynomial-time-features .remark name="Patterns in dynamic programs"}

Subproblems: prefixes or suffixes (bowling, LCS, LIS, subset sum), substrings (coin game, parenthesization), several sequences at once (LCS), integers (Fibonacci, rod cutting, subset sum), vertices (shortest paths). Expansion: by a constant factor (whose turn, min or max, which finger) or by a factor $n$ (number of edges in Bellman–Ford). Branching: constant (Fibonacci, LCS, Floyd–Warshall, subset sum), a vertex degree (shortest paths), or linear (LIS, parenthesization, rod cutting).

:::
