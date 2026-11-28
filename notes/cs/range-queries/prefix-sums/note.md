---
title: "Prefix Sums"
sources: []
requires: [cs/data-structures/hashing]
aliases: [cs/algorithm-patterns/prefix-sums]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-26 in our own words (owner decision 2026-11-26: new notes for the LeetCode Hot 100 problems without a fitting note). No single source; TODO: add a source if one is integrated later. The examples and figures are our own. -->

Precomputing running totals turns every range sum into a difference of two numbers.

::: {#def-prefix-sums .definition name="Prefix sums"}

The *prefix sums* of $A[1..n]$ are
$$
S_0=0,\qquad S_i=S_{i-1}+A[i]=\sum_{k=1}^{i}A[k]\quad(1\le i\le n).
$$

:::

::: {#prp-prefix-sums-range .proposition name="Range sums"}

For $1\le i\le j\le n$,
$$
\sum_{k=i}^{j}A[k]=S_j-S_{i-1}.
$$
So after $O(n)$ preprocessing every range sum takes $O(1)$ time.

:::

::: {.proof}

1. $S_j=\sum_{k=1}^{i-1}A[k]+\sum_{k=i}^{j}A[k]$ by splitting the sum at $i$.

2. The first part is $S_{i-1}$; subtract it.

:::

::: {#fig-prefix-sums-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.75cm,y=0.7cm]
\node[lab,anchor=east] at (-0.5,0.5) {$A$}; \node[lab,anchor=east] at (-0.5,-0.7) {$S$};
\foreach \v [count=\i] in {3,-1,4,1,5,-2} { \draw[cell frame] (\i-1,0) rectangle (\i,1); \node[lab] at (\i-0.5,0.5) {$\v$}; }
\draw[hl cell] (1,0) rectangle (4,1); \node[lab] at (1.5,0.5) {$-1$}; \node[lab] at (2.5,0.5) {$4$}; \node[lab] at (3.5,0.5) {$1$};
\foreach \s [count=\i from 0] in {0,3,2,6,7,12,10} { \node[lab] at (\i,-0.7) {$\s$}; }
\draw[->] (1,-1.1) to[bend right=25] node[lab,tick,below] {$S_4-S_1=7-3=4$} (4,-1.1);
\end{tikzpicture}
\end{center}
```

The prefix sums sit at the boundaries between cells. The highlighted range $A[2..4]$ sums to $S_4-S_1=4$.

:::

::: {#prp-prefix-sums-count .proposition name="Counting subarrays with a given sum"}

The number of pairs $i\le j$ with $\sum_{k=i}^{j}A[k]=t$ can be computed in $O(n)$ expected time, for arbitrary integer entries.

:::

::: {.proof}

1. By @prp-prefix-sums-range, the pair $(i,j)$ qualifies exactly when $S_{i-1}=S_j-t$.

2. Scan $j=1,\dots,n$, keeping a hash table (@def-hash-table) that maps each value $v$ to the number of indices $0\le p<j$ with $S_p=v$, starting with $\{0\mapsto1\}$.

3. At step $j$, add the count of $S_j-t$ to the answer, then increment the count of $S_j$. Each step is $O(1)$ expected time.

:::

Negative entries rule out a sliding window here, because a window sum is then not monotone in its width; the prefix-sum method does not need monotonicity.

::: {#rmk-prefix-sums-tree .remark name="Paths in a tree"}

The same counting works for downward paths in a rooted tree with weighted nodes. During a depth-first search, the prefix sum of a node is the total weight on the path from the root to it, and the hash table holds the prefix sums of the current node's ancestors only: add a node's prefix sum on entering it, and remove it on leaving. A downward path ending at $v$ has sum $t$ exactly when an ancestor's prefix sum equals $S_v-t$.

:::

## Prefix and suffix products

::: {#exm-prefix-sums-product .example name="Products of all other entries"}

To compute $B[i]=\prod_{k\ne i}A[k]$ for every $i$ without division (which fails when an entry is $0$), let $P_i=\prod_{k<i}A[k]$ and $Q_i=\prod_{k>i}A[k]$, with empty products equal to $1$. Then $B[i]=P_iQ_i$. One pass from the left computes every $P_i$ and one pass from the right multiplies in $Q_i$, so the time is $O(n)$ and the only extra space is the output and one running product.

:::

::: {#fig-prefix-sums-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.9cm,y=0.65cm]
\node[lab,anchor=east] at (-0.2,0.5) {$A$}; \node[lab,anchor=east] at (-0.2,-0.5) {$P$};
\node[lab,anchor=east] at (-0.2,-1.5) {$Q$}; \node[lab,anchor=east] at (-0.2,-2.5) {$B$};
\foreach \a/\p/\q/\b [count=\i] in {1/1/24/24,2/1/12/12,3/2/4/8,4/6/1/6} {
  \draw[cell frame] (\i-1,0) rectangle (\i,1); \node[lab] at (\i-0.5,0.5) {$\a$};
  \node[lab] at (\i-0.5,-0.5) {$\p$}; \node[lab] at (\i-0.5,-1.5) {$\q$};
  \draw[hl cell] (\i-1,-3) rectangle (\i,-2); \node[lab] at (\i-0.5,-2.5) {$\b$};
}
\end{tikzpicture}
\end{center}
```

For $A=1,2,3,4$: the products to the left $P$, the products to the right $Q$, and their product $B$, which is the product of all entries but one.

:::
