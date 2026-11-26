---
title: "Stacks, Queues and Monotonic Stacks"
sources: []
requires: [cs/data-structures/linked-lists, cs/data-structures/dynamic-arrays]
status: draft
---

<!-- Added 2026-11-26 in our own words (owner decision 2026-11-26: new notes for the LeetCode Hot 100 problems without a fitting note). No single source; TODO: add a source if one is integrated later. The examples and figures are our own. -->

A stack, a queue and a deque are restricted sequences (@def-sequence-interface): they allow changes only at the ends. The restriction is what makes them fast and what makes them useful as invariants.

::: {#def-stack-queue-deque .definition name="Stack, queue, deque"}

A *stack* supports `push` (insert at the top), `pop` (remove the top) and `top`: last in, first out. A *queue* supports `enqueue` (insert at the back), `dequeue` (remove the front) and `front`: first in, first out. A *deque* (double-ended queue) supports insertion and deletion at both ends.

:::

All three can be stored in a dynamic array used as a circular buffer, with indices $\mathit{head}$ and $\mathit{tail}$ taken modulo the capacity, or in a doubly linked list. Either way each operation takes $O(1)$ time (amortized for the array, because of resizing).

::: {#fig-stacks-and-queues-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.6cm,y=0.6cm]
\foreach \c [count=\i] in {a,b,c} { \draw[cell frame] (0,\i-1) rectangle (1.4,\i); \node[lab] at (0.7,\i-0.5) {$\c$}; }
\draw[->] (2.6,3.4) -- (1.6,2.6); \node[lab,tick] at (3.2,3.6) {push / pop};
\node[lab] at (0.7,-0.6) {stack};
\begin{scope}[xshift=4.5cm]
\foreach \c [count=\i] in {a,b,c,d} { \draw[cell frame] (\i-1,1) rectangle (\i,2); \node[lab] at (\i-0.5,1.5) {$\c$}; }
\draw[->] (-1.2,1.5) -- (-0.1,1.5); \node[lab,tick] at (-1.4,2.2) {dequeue};
\draw[<-] (4.1,1.5) -- (5.2,1.5); \node[lab,tick] at (5.2,2.2) {enqueue};
\node[lab] at (2,-0.6) {queue};
\end{scope}
\begin{scope}[xshift=10cm]
\foreach \c [count=\i] in {a,b,c,d} { \draw[cell frame] (\i-1,1) rectangle (\i,2); \node[lab] at (\i-0.5,1.5) {$\c$}; }
\draw[<->] (-1.2,1.5) -- (-0.1,1.5); \draw[<->] (4.1,1.5) -- (5.2,1.5);
\node[lab] at (2,-0.6) {deque};
\end{scope}
\end{tikzpicture}
\end{center}
```

The three restricted sequences. A stack changes only at its top; a queue inserts at the back and removes at the front; a deque does both at both ends.

:::

::: {#rmk-stacks-and-queues-1 .remark name="Nesting"}

A stack is the natural memory for nested structure. To check that a string of brackets is balanced, push each opening bracket and, at each closing bracket, pop and check that the two match; the string is balanced exactly when no check fails and the stack ends empty. The same idea decodes nested repetitions such as $3[a2[c]]$: on `[` push the current string and count, on `]` pop them and append the repeated inner string.

:::

## Monotonic stacks

::: {#def-monotonic-stack .definition name="Monotonic stack"}

A *monotonic stack* over an array $A[1..n]$ is a stack of indices, processed left to right, whose values are kept strictly decreasing from bottom to top (or increasing, symmetrically). Before pushing $i$, pop every index $j$ on top with $A[j]\le A[i]$.

:::

When $j$ is popped by $i$, the index $i$ is the *next greater-or-equal element* of $j$: the first $i>j$ with $A[i]\ge A[j]$. Indices still on the stack at the end have none.

::: {#thm-monotonic-stack .theorem name="Next greater elements in linear time"}

The monotonic stack computes the next greater-or-equal element of every index of $A[1..n]$ in $O(n)$ time.

:::

::: {.proof}

1. *Invariant.* Popping every top value $\le A[i]$ before pushing $i$ keeps the stack values strictly decreasing from bottom to top.

2. *Correctness.* Let $j$ be popped at step $i$; then $A[i]\ge A[j]$. For each $k$ with $j<k<i$, the index $j$ was still on the stack after step $k$ and $k$ lay above it, so $A[k]<A[j]$ by the invariant. Hence $i$ is the first index after $j$ with value $\ge A[j]$.

3. *An index never popped has no answer.* If $j$ remains at the end, then after each step $i>j$ both $j$ and $i$ are on the stack with $j$ below, so $A[i]<A[j]$.

4. *Time.* Each index is pushed once and popped at most once, so there are at most $2n$ stack operations in total.

:::

::: {#fig-stacks-and-queues-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.75cm,y=0.12cm]
\foreach \v [count=\i] in {73,74,75,71,69,72,76,73} {
  \draw[bar] (\i-0.8,0) rectangle (\i-0.2,\v-60);
  \node[lab,tick] at (\i-0.5,\v-57) {$\v$};
  \node[lab,tick] at (\i-0.5,-2.5) {\i};
}
\draw[->,hl] (4.5,10) to[bend left=40] (5.35,12.5);
\draw[->,hl] (3.5,12) to[bend left=30] (5.25,12.8);
\node[lab,note,anchor=west] at (8.2,14) {at $i=6$: pop $5$ and $4$};
\node[lab,note,anchor=west] at (8.2,8) {stack after: $3,6$};
\end{tikzpicture}
\end{center}
```

A monotonic stack on daily temperatures. When index $6$ (value $72$) arrives, the stack holds $3,4,5$ with values $75,71,69$. It pops $5$ and $4$, whose next warmer day is therefore day $6$, and stops at $3$, since $75>72$.

:::

::: {#exm-stacks-and-queues-histogram .example name="Largest rectangle in a histogram"}

For bars of heights $h[1..n]$, the largest rectangle that uses bar $j$ at full height spans from just after the previous lower bar to just before the next lower bar. One pass of an increasing monotonic stack finds both: when $j$ is popped by $i$ (so $h[i]<h[j]$), the right limit is $i-1$ and the left limit is one more than the index below $j$ on the stack. With equal heights only the last of them gets its full width, which is enough for the maximum. So the largest rectangle is found in $O(n)$ time. A decreasing stack counts trapped rain water the same way: each pop of $j$ fills the layer above $h[j]$ between its two neighbours on the stack.

:::

::: {#fig-stacks-and-queues-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.7cm,y=0.5cm]
\foreach \v [count=\i] in {2,1,5,6,2,3} { \draw[bar] (\i-1,0) rectangle (\i,\v); \node[lab,tick] at (\i-0.5,-0.5) {\i}; }
\fill[tintA] (2,0) rectangle (4,5); \draw[hl] (2,0) rectangle (4,5);
\draw[<->] (2,6.8) -- (4,6.8); \node[lab,tick] at (3,7.4) {bars higher than $h[3]$};
\end{tikzpicture}
\end{center}
```

Heights $2,1,5,6,2,3$. Bar $3$ extends right until bar $5$ (lower) and left until bar $2$ (lower), giving the rectangle of area $2\cdot5=10$, which is the largest.

:::

## Monotonic queues

::: {#def-monotonic-queue .definition name="Monotonic queue"}

A *monotonic queue* for windows of width $k$ over $A[1..n]$ is a deque of indices whose values decrease from front to back. To add $i$: pop indices from the back while their value is $\le A[i]$, push $i$ at the back, and pop the front if it is $\le i-k$. The front is then the index of the maximum of $A[i-k+1..i]$.

:::

::: {#prp-monotonic-queue .proposition name="Sliding window maximum"}

The maxima of all $n-k+1$ windows of width $k$ are found in $O(n)$ time.

:::

::: {.proof}

1. *Invariant.* The deque holds, in order, exactly the indices $j$ of the current window that have no later index $j'\le i$ with $A[j']\ge A[j]$. An index removed from the back has such a $j'$ (namely $i$), so it can never be a window maximum again.

2. So the values decrease along the deque, and its front is the largest value in the window.

3. *Time.* Each index enters and leaves the deque at most once.

:::

Another stack trick: to support `getMin` in $O(1)$, store with each stack entry the minimum of the entries below and including it.
