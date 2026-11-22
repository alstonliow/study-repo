---
title: "Time Complexity and the Class P"
sources: [mit18404j-12, mit18404j-14]
requires: [cs/theory/logical-theories, math/discrete/sequences/big-o]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lecture 12 and the first part of Lecture 14, in our own wording; proofs written out in steps. The informal program version of P is @def-p-exp-r. -->

Computability asks *whether* a problem can be solved; complexity asks how many resources it needs. We measure time as a function of the input length, in the worst case.

## Running time

::: {#def-time-class .definition name="Running time and TIME"}

A deterministic TM $M$ that halts on all inputs *runs in time* $t(n)$, for $t:\mathbb N\to\mathbb N$, if on every input of length $n$ it halts within $t(n)$ steps. The *time complexity class*

$$
\mathrm{TIME}(t(n))=\{A: \text{some deterministic 1-tape TM decides } A \text{ in time } O(t(n))\}.
$$

:::

::: {#exm-anbn-time .example name="Deciding $a^kb^k$ on one tape"}

Let $A=\{a^kb^k: k\ge0\}$ and $n$ the input length.

1. *Crossing off pairs.* Check $w\in a^*b^*$; then repeatedly cross off one $a$ and one $b$ in a sweep across the tape. Each sweep costs $O(n)$ and there are at most $n/2$ sweeps, so $A\in\mathrm{TIME}(n^2)$.
2. *Halving.* Check $w\in a^*b^*$; then repeatedly check that the numbers of remaining $a$'s and $b$'s have the same parity (reject if not) and cross off every other $a$ and every other $b$. Each sweep costs $O(n)$ and halves both counts, so there are $O(\log n)$ sweeps and $A\in\mathrm{TIME}(n\log n)$. The parities read off the binary digits of the two counts, from the lowest digit up, so they are compared digit by digit.
3. *Two tapes.* Copy the $a$'s to a second tape, then match them against the $b$'s: $O(n)$ steps.

One can show that a 1-tape TM cannot do better than $O(n\log n)$: every language in $\mathrm{TIME}(o(n\log n))$ is regular.

:::

::: {#fig-time-complexity-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.42cm, y=0.42cm]
\foreach \r/\row in {0/{a,a,a,a,a,a,b,b,b,b,b,b},1/{\times,a,\times,a,\times,a,\times,b,\times,b,\times,b},2/{\times,\times,\times,a,\times,\times,\times,\times,\times,b,\times,\times},3/{\times,\times,\times,\times,\times,\times,\times,\times,\times,\times,\times,\times}} {
  \foreach \s [count=\i from 0] in \row {
    \draw[cell frame] (\i,-1.6*\r) rectangle (\i+1,-1.6*\r+1);
    \node[lab, note] at (\i+0.5,-1.6*\r+0.5) {$\s$};
  }
}
\node[lab, note, anchor=west] at (12.5,0.5) {6 and 6: parity even, even};
\node[lab, note, anchor=west] at (12.5,-1.1) {3 and 3: odd, odd};
\node[lab, note, anchor=west] at (12.5,-2.7) {1 and 1: odd, odd};
\node[lab, note, anchor=west] at (12.5,-4.3) {0 and 0: accept};
\end{tikzpicture}
\end{center}
```

The halving decider of @exm-anbn-time on $a^6b^6$: each sweep crosses off every other remaining symbol, so the counts $6,3,1,0$ are their binary expansions read from the right.

:::

## Changing the model

::: {#thm-multitape-quadratic .theorem name="Multitape simulation costs a square"}

Let $t(n)\ge n$. Every multitape TM running in time $t(n)$ has an equivalent 1-tape TM running in time $O(t(n)^2)$.

:::

::: {.proof}

1. Use the simulation of @thm-multitape-equivalent.

2. In $t(n)$ steps each tape of the multitape machine uses at most $t(n)$ cells, so the single tape holds $O(t(n))$ cells (the number of tapes is a constant).

3. Simulating one step takes a constant number of sweeps over this tape, plus at most a constant number of right shifts, each $O(t(n))$. So each step costs $O(t(n))$.

4. Over $t(n)$ steps the total is $O(t(n)^2)$.

:::

So reasonable deterministic models differ in time by at most a polynomial factor, and a class closed under polynomial changes does not depend on the model.

## The class P

::: {#def-class-p .definition name="The class P" related="def-p-exp-r"}

$$
\mathrm P=\bigcup_{k}\mathrm{TIME}(n^k),
$$

the languages decidable in polynomial time on a deterministic 1-tape TM (equivalently, on any reasonable deterministic model).

:::

P is robust (the same for all reasonable deterministic models) and roughly matches the problems that are solvable in practice. Inputs must be encoded reasonably: numbers in binary, not unary, and graphs by lists of nodes and edges.

::: {#prp-path-in-p .proposition name="Reachability is in P"}

$\mathit{PATH}=\{\langle G,s,t\rangle: G \text{ is a directed graph with a path from } s \text{ to } t\}$ is in $\mathrm P$.

:::

::: {.proof}

1. Mark $s$. Repeat: for every edge $(a,b)$ with $a$ marked, mark $b$. Stop when a round marks nothing new; accept iff $t$ is marked (this is breadth-first search, @def-bfs).

2. Each round marks a new node or is the last, so there are at most $m+1$ rounds for $m$ nodes, and each round scans the edges in polynomial time.

3. Trying all paths instead would take exponential time, as there can be $m^m$ of them.

:::

::: {#exm-relprime-in-p .example name="Relatively prime numbers"}

$\mathit{RELPRIME}=\{\langle x,y\rangle: \gcd(x,y)=1\}$ is in $\mathrm P$: the Euclidean algorithm takes $O(n)$ division steps on $n$-bit inputs, because the larger number at least halves every two steps (@sec-math-discrete-number-theory-gcd-and-euclidean-algorithm). Trying all divisors up to $x$ would take time exponential in the number of bits.

:::

::: {#fig-time-complexity-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex, fill=accentLight, draw=accent] (s) at (0,0) {$s$};
\node[small vertex, fill=accentLight, draw=accent] (a) at (1.6,0.9) {};
\node[small vertex, fill=accentLight, draw=accent] (b) at (1.6,-0.9) {};
\node[small vertex, fill=accentLight, draw=accent] (c) at (3.2,0.9) {};
\node[small vertex] (d) at (3.2,-0.9) {};
\node[small vertex, fill=accentLight, draw=accent] (t) at (4.8,0) {$t$};
\draw[trans] (s) -- (a); \draw[trans] (s) -- (b); \draw[trans] (a) -- (c); \draw[trans] (c) -- (t);
\draw[trans] (d) -- (b); \draw[trans] (d) -- (t);
\node[lab, tick] at (0,0.55) {0};
\node[lab, tick] at (1.6,1.45) {1}; \node[lab, tick] at (1.6,-1.45) {1};
\node[lab, tick] at (3.2,1.45) {2}; \node[lab, tick] at (4.8,0.55) {3};
\end{tikzpicture}
\end{center}
```

The marking algorithm of @prp-path-in-p; numbers give the round in which a node is marked. The unshaded node is never marked (no edge leads into it), and $t$ is reached in round 3.

:::
