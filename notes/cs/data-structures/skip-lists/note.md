---
title: "Skip Lists"
sources: [mit6046-7]
requires: [cs/data-structures/linked-lists-and-dynamic-arrays, math/probability/discrete/chernoff-bounds, math/probability/discrete/geometric-distribution]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 7, in our own wording; proofs written out in steps. -->

A sorted linked list is easy to update but takes $\Theta(n)$ time to search. A *skip list* adds "express lanes" chosen at random, which gives $O(\log n)$ search with high probability and keeps updates simple.

::: {#def-skip-list .definition name="Skip list"}

A *skip list* consists of sorted linked lists $L_0\supseteq L_1\supseteq L_2\supseteq\cdots$. The bottom list $L_0$ holds all $n$ keys; each list starts with a sentinel $-\infty$, and every node also points to the copy of its key in the list below. When a key is inserted into $L_0$, a fair coin is tossed repeatedly: for each head the key is also inserted into the next list up, and the first tail stops the promotion.

:::

::: {#def-skip-list-search .definition name="Search"}

To search for $x$, start at the sentinel of the top list. Move right while the next key is at most $x$; when the next key exceeds $x$ (or the list ends), move down one list. At the bottom list, the current key is $x$ or the predecessor of $x$.

:::

::: {#fig-skip-lists-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.95cm,y=0.75cm]
\foreach \lev/\keys in {0/{1,3,4,6,8,9,12}, 1/{3,6,9,12}, 2/{6,12}, 3/{6}} {
  \node[lab,tick] at (-1.3,\lev) {$L_{\lev}$};
  \node[box] (s\lev) at (0,\lev) {$-\infty$};
}
\foreach \k/\x in {1/1,3/2,4/3,6/4,8/5,9/6,12/7} \node[box] (a\k) at (\x*1.5,0) {$\k$};
\foreach \k/\x in {3/2,6/4,9/6,12/7} \node[box] (b\k) at (\x*1.5,1) {$\k$};
\foreach \k/\x in {6/4,12/7} \node[box] (c\k) at (\x*1.5,2) {$\k$};
\node[box] (d6) at (4*1.5,3) {$6$};
\draw[->] (s0)--(a1); \draw[->] (a1)--(a3); \draw[->] (a3)--(a4); \draw[->] (a4)--(a6); \draw[->] (a6)--(a8); \draw[->] (a8)--(a9); \draw[->] (a9)--(a12);
\draw[->] (s1)--(b3); \draw[->] (b3)--(b6); \draw[->] (b6)--(b9); \draw[->] (b9)--(b12);
\draw[->] (s2)--(c6); \draw[->] (c6)--(c12);
\draw[->] (s3)--(d6);
\draw[hl,->] (s3) -- (d6); \draw[hl,->] (d6) -- (c6); \draw[hl,->] (c6) -- (b6); \draw[hl,->] (b6) -- (a6); \draw[hl,->] (a6) -- (a8);
\end{tikzpicture}
\end{center}
```

A skip list on $1,3,4,6,8,9,12$. Searching for $8$ (highlighted) moves right on the top list to $6$, then down, because the next keys ($12$, $9$) are too large, and finally right to $8$ at the bottom.

:::

Inserting $x$ is a search followed by splicing $x$ into $L_0$ and, after each head of the coin, into the next list up, in $O(1)$ per list. Deleting removes $x$ from every list that holds it. So all operations cost about as much as a search.

::: {#lem-skip-list-levels .lemma name="Few levels"}

For every constant $c\ge1$, a skip list with $n$ keys has at most $(c+1)\log_2n$ non-empty lists above $L_0$ with probability at least $1-1/n^c$.

:::

::: {.proof}

1. A given key reaches $L_k$ only if its first $k$ coin tosses are heads, with probability $2^{-k}$.

2. By the union bound (@thm-union-bound) over the $n$ keys, $L_k$ is non-empty with probability at most $n2^{-k}$. For $k=(c+1)\log_2n$ this is $n\cdot n^{-(c+1)}=n^{-c}$.

:::

::: {#thm-skip-list-search .theorem name="Search in $O(\log n)$ with high probability"}

For every constant $c\ge1$ there is a constant $a$ such that a search in a skip list with $n$ keys takes at most $a\log_2n$ steps with probability at least $1-2/n^c$.

:::

::: {.proof}

1. Trace the search path *backwards*, from the bottom node up to the top-left sentinel. At each node the backward path goes *up* if the node was promoted, and *left* otherwise. Whether a node was promoted is a coin toss independent of everything seen before on the backward path, so each backward step is up with probability $\frac12$.

2. The path has as many up-steps as there are levels. By @lem-skip-list-levels, with probability at least $1-1/n^c$ there are at most $L=(c+1)\log_2n$ of them.

3. So the path length is at most the number of tosses of a fair coin needed to see $L$ heads. Among $a\log_2n$ tosses, the expected number of heads is $\frac a2\log_2n$; a Chernoff bound (@thm-chernoff-bound, applied to the tails) shows that fewer than $L$ heads occur with probability at most $1/n^c$ once $a$ is a large enough constant (depending on $c$).

4. Both bad events together have probability at most $2/n^c$.

:::

The expected search time is also $O(\log n)$. Unlike a balanced tree, a skip list needs no rebalancing: its shape depends only on coin tosses, not on the order of insertions.
