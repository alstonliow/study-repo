---
title: "Dynamic Programming on Intervals"
sources: [mit6046-10, mit6046-1, mit6046r-1, mit6046r-5]
requires: [cs/dynamic-programming/pseudopolynomial-time]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lectures 1 and 10 and Recitations 1 and 5, in our own wording; examples our own (checked by computation); proofs written out in steps. The alternating coin game of Lecture 10 is @exm-coin-game. -->

Many problems on sequences use *substring* subproblems $x(i,j)$, one for each contiguous piece, and guess where the piece splits. There are $O(n^2)$ of them, so the running time is $O(n^2)$ times the work per subproblem.

::: {#exm-weighted-interval-scheduling .example name="Weighted interval scheduling"}

Requests $[s(i),f(i))$ have weights $w(i)$; choose compatible requests of largest total weight (the unweighted version is @def-interval-scheduling). Sort the requests by starting time, $s(1)\le\dots\le s(n)$, and let $\mathrm{next}(i)$ be the first request $j>i$ with $s(j)\ge f(i)$, found by binary search.

1. *Subproblems:* $x(i)$, the best total weight using only requests $i,\dots,n$ (a suffix).
2. *Relation:* request $i$ is not used, or it is used and then the next usable request is $\mathrm{next}(i)$: $x(i)=\max\{x(i+1),\ w(i)+x(\mathrm{next}(i))\}$.
3. *Order:* decreasing $i$. 4. *Base:* $x(n+1)=0$. 5. *Original:* $x(1)$.
6. *Time:* sorting and the binary searches take $O(n\log n)$, and the $n$ subproblems $O(1)$ each.

:::

::: {#exm-longest-palindromic-subsequence .example name="Longest palindromic subsequence"}

A *palindrome* reads the same forwards and backwards. Given a string $X=x_1\cdots x_n$, find a longest subsequence of $X$ that is a palindrome. For `CHARACTER` the answer has length $5$, for example `CARAC`.

1. *Subproblems:* $L(i,j)$, the length of a longest palindromic subsequence of $x_i\cdots x_j$, for $1\le i\le j\le n$.
2. *Relation:* if $x_i=x_j$ (and $i<j$), use both ends: $L(i,j)=2+L(i+1,j-1)$; otherwise one end is unused: $L(i,j)=\max\{L(i+1,j),L(i,j-1)\}$.
3. *Order:* increasing $j-i$.
4. *Base:* $L(i,i)=1$, and $L(i,i-1)=0$ for the empty string.
5. *Original:* $L(1,n)$; parent pointers give the palindrome.
6. *Time:* $O(n^2)$ subproblems with $O(1)$ work: $O(n^2)$.

The relation is right by the same exchange argument as for LCS (@lem-lcs-relation): if the two ends are equal, some longest palindrome uses them as its outer letters.

:::

::: {#exm-optimal-bst .example name="Optimal binary search tree"}

Keys $k_1<\dots<k_n$ are searched with known weights (frequencies) $w_1,\dots,w_n$. A search for $k_r$ costs the number of nodes on the path to it, that is $\mathrm{depth}(k_r)+1$. Find a binary search tree minimising $\sum_rw_r(\mathrm{depth}(k_r)+1)$.

1. *Subproblems:* $e(i,j)$, the least cost of a search tree on $k_i,\dots,k_j$, for $1\le i\le j+1\le n+1$; let $W(i,j)=w_i+\dots+w_j$.
2. *Relation:* guess the root $k_r$. Every key of the subtree then lies one level deeper than in its own subtree, which adds $W(i,j)$:
   $$e(i,j)=W(i,j)+\min_{i\le r\le j}\bigl\{e(i,r-1)+e(r+1,j)\bigr\}.$$
3. *Order:* increasing $j-i$. 4. *Base:* $e(i,i-1)=0$ (an empty tree).
5. *Original:* $e(1,n)$, with the chosen roots recorded to build the tree.
6. *Time:* $O(n^2)$ subproblems, $O(n)$ work each with prefix sums for $W$: $O(n^3)$.

Greedily putting the most frequent key at the root is not optimal: with weights $10,8,9$ for keys $1,2,3$, that tree costs $10+2\cdot9+3\cdot8=52$, while the balanced tree with root $2$ costs $8+2\cdot(10+9)=46$.

:::

::: {#fig-interval-subproblems-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (a) at (0,0) {$1$}; \node[small vertex] (b) at (0.8,-0.9) {$3$}; \node[small vertex] (c) at (0.3,-1.8) {$2$};
\draw (a)--(b) (b)--(c);
\node[lab,tick] at (0.4,-2.5) {cost $10+2\cdot9+3\cdot8=52$};
\node[small vertex] (d) at (5,0) {$2$}; \node[small vertex] (e) at (4.3,-0.9) {$1$}; \node[small vertex] (f) at (5.7,-0.9) {$3$};
\draw (d)--(e) (d)--(f);
\node[lab,tick] at (5,-2.5) {cost $8+2\cdot(10+9)=46$};
\node[lab,tick] at (0.4,0.6) {greedy: heaviest key at the root};
\node[lab,tick] at (5,0.6) {optimal};
\end{tikzpicture}
\end{center}
```

Search trees for keys $1,2,3$ with weights $10,8,9$. Putting the heaviest key at the root (left) costs $52$; the balanced tree found by the dynamic program (right) costs $46$.

:::

::: {#exm-stacking-blocks .example name="Stacking blocks"}

Given boxes with dimensions $(\ell_i,w_i,h_i)$, each usable in any rotation and any number of times, build the tallest tower in which every box sits on one whose base is strictly larger in both directions. List each box in its three rotations (taking $\ell\ge w$), sort the $3n$ oriented boxes by base area, and let $x(i)$ be the tallest tower with oriented box $i$ on top: $x(i)=h_i+\max\{x(j):\ell_j>\ell_i,\ w_j>w_i\}$ (or $h_i$ alone). This is a longest path in a DAG, $O(n^2)$ time, like the longest increasing subsequence (@exm-lis).

:::
