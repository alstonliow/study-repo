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
