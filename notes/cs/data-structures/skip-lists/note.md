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

```{=latex}
\begin{algorithm}
\caption{Search in a skip list}
\begin{algorithmic}
\INPUT Skip list, key $x$
\OUTPUT The node of $L_0$ holding $x$ or its predecessor
\STATE $p\gets$ the sentinel of the top list
\WHILE{true}
    \WHILE{$p.\mathrm{next}$ is not none and $p.\mathrm{next}.\mathrm{key}\le x$}
        \STATE $p\gets p.\mathrm{next}$
    \ENDWHILE
    \IF{$p$ is in $L_0$}
        \RETURN $p$
    \ENDIF
    \STATE $p\gets p.\mathrm{down}$
\ENDWHILE
\end{algorithmic}
\end{algorithm}
```

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

```{=latex}
\begin{algorithm}
\caption{Insert in a skip list}
\begin{algorithmic}
\INPUT Skip list, new key $x$
\STATE search for $x$, remembering in each list $L_i$ the last node $p_i$ visited
\STATE splice $x$ into $L_0$ after $p_0$; $i\gets0$
\WHILE{a fair coin comes up heads}
    \STATE $i\gets i+1$
    \IF{$L_i$ does not exist}
        \STATE create $L_i$ with a sentinel; $p_i\gets$ that sentinel
    \ENDIF
    \STATE splice $x$ into $L_i$ after $p_i$, pointing down to its copy in $L_{i-1}$
\ENDWHILE
\end{algorithmic}
\end{algorithm}
```

::: {#fig-skip-lists-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab,tick] at (-1.30,0.00) {$L_0$};
\node[box] (s0) at (0,0) {$-\infty$};
\node[box] (n1_0) at (1.40,0) {$1$};
\draw[->] (s0)--(n1_0);
\node[box] (n3_0) at (2.80,0) {$3$};
\draw[->] (n1_0)--(n3_0);
\node[box] (n4_0) at (4.20,0) {$4$};
\draw[->] (n3_0)--(n4_0);
\node[box] (n6_0) at (5.60,0) {$6$};
\draw[->] (n4_0)--(n6_0);
\node[hl box] (n7_0) at (7.00,0) {$7$};
\draw[->, hl] (n6_0)--(n7_0);
\node[box] (n8_0) at (8.40,0) {$8$};
\draw[->] (n7_0)--(n8_0);
\node[box] (n9_0) at (9.80,0) {$9$};
\draw[->] (n8_0)--(n9_0);
\node[box] (n12_0) at (11.20,0) {$12$};
\draw[->] (n9_0)--(n12_0);
\node[lab,tick] at (-1.30,1.00) {$L_1$};
\node[box] (s1) at (0,1) {$-\infty$};
\node[box] (n3_1) at (2.80,1) {$3$};
\draw[->] (s1)--(n3_1);
\node[box] (n6_1) at (5.60,1) {$6$};
\draw[->] (n3_1)--(n6_1);
\node[hl box] (n7_1) at (7.00,1) {$7$};
\draw[->, hl] (n6_1)--(n7_1);
\node[box] (n9_1) at (9.80,1) {$9$};
\draw[->] (n7_1)--(n9_1);
\node[box] (n12_1) at (11.20,1) {$12$};
\draw[->] (n9_1)--(n12_1);
\node[lab,tick] at (-1.30,2.00) {$L_2$};
\node[box] (s2) at (0,2) {$-\infty$};
\node[box] (n6_2) at (5.60,2) {$6$};
\draw[->] (s2)--(n6_2);
\node[hl box] (n7_2) at (7.00,2) {$7$};
\draw[->, hl] (n6_2)--(n7_2);
\node[box] (n12_2) at (11.20,2) {$12$};
\draw[->] (n7_2)--(n12_2);
\node[lab,tick] at (-1.30,3.00) {$L_3$};
\node[box] (s3) at (0,3) {$-\infty$};
\node[box] (n6_3) at (5.60,3) {$6$};
\draw[->] (s3)--(n6_3);
\draw[hl,->] (s3)--(n6_3); \draw[hl,->] (n6_3)--(n6_2); \draw[hl,->] (n6_2)--(n6_1); \draw[hl,->] (n6_1)--(n6_0);
\node[lab,tick] at (7.00,-0.75) {coin: H, H, T};
\end{tikzpicture}
\end{center}
```

Inserting $7$ into the skip list of @fig-skip-lists-1. The search for $7$ (highlighted path) stops at $6$ in every list, so $6$ is the node to splice after. $7$ goes into $L_0$; the coin then shows heads, heads, tails, so $7$ is also spliced into $L_1$ and $L_2$ after $6$, and the promotion stops.

:::

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
