---
title: "Integer Subproblems and Pseudopolynomial Time"
sources: [mit6006-18, mit6006r-18]
requires: [cs/algorithm-design/subproblem-design]
aliases: [cs/dynamic-programming/pseudopolynomial-time]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 18 and Recitation 18, in our own wording; examples our own (checked by computation); proofs written out in steps. On 2026-11-25 rod cutting, subset sum and 0-1 knapsack moved to their own notes (one problem per note, SPEC §8.6); this note is their overview. -->

Another source of subproblems is the integers below a given integer. Then the number of subproblems depends on the *values* in the input, not only on how many numbers there are.

## The problems

| problem | subproblems | time | polynomial? |
|---|---|---|---|
| rod cutting (@sec-cs-algorithm-design-rod-cutting) | lengths $\ell\le L$ | $O(L^2)$ | yes: the input has $L+1$ numbers |
| subset sum (@sec-cs-algorithm-design-subset-sum) | suffixes and targets $t\le T$ | $O(nT)$ | pseudopolynomial |
| 0-1 knapsack (@sec-cs-algorithm-design-knapsack) | suffixes and capacities $c\le S$ | $O(nS)$ | pseudopolynomial |

## Polynomial or not?

Is the $O(nT)$ of subset sum (@exm-subset-sum) polynomial? The input is $n+1$ numbers, each fitting in a word, but a word can have $w$ bits for large $w$, so $T$ can be as large as $2^w$. Taking $w=n$, the running time $O(n2^n)$ is exponential in the input size. The running time is polynomial in the *values*, not in the *size*.

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
