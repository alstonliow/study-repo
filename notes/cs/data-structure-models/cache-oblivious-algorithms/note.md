---
title: "External Memory and Cache-Oblivious Algorithms"
sources: [mit6046-23, mit6046-24]
requires: [cs/data-structures/two-three-trees, cs/sorting/median-of-medians]
aliases: [cs/models-of-computation/cache-oblivious-algorithms, cs/algorithm-topics/cache-oblivious-algorithms]   # old ids (moved)
relations:
  related: [math/numerical/direct-solvers/caches-and-blocking]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lectures 23-24, in our own wording; proofs written out in steps. -->

Real memory is a hierarchy: registers, several levels of cache, main memory, disk. Each level is larger but slower, and data moves between levels in *blocks*. Counting operations ignores this; counting *block transfers* captures it.

::: {#def-external-memory-model .definition name="External-memory and cache-oblivious models"}

In the *external-memory model* there is a fast memory (*cache*) of $M$ words and an unbounded slow memory, both divided into blocks of $B$ words. Computation on data in the cache is free; the cost of an algorithm is the number $MT(N)$ of *memory transfers* (blocks moved between the levels) on an input of size $N$. An algorithm is *cache-oblivious* if it does not know $M$ and $B$: the transfers are made automatically by an optimal (or LRU) replacement policy, and the bound must hold for all $M$ and $B$.

:::

A cache-oblivious algorithm that is efficient for one pair of levels is efficient for every pair at once, since it never used $M$ or $B$. LRU replacement with a cache of size $2M$ makes at most twice the transfers of the optimal policy with size $M$, so assuming the optimal policy costs only constant factors.

::: {#prp-scanning .proposition name="Scanning"}

Reading $N$ consecutive words costs $O(\lceil N/B\rceil+1)$ memory transfers. Hence reversing an array, or a constant number of parallel scans, also costs $O(N/B+1)$.

:::

::: {.proof}

$N$ consecutive words occupy at most $\lceil N/B\rceil+1$ blocks, each read once (one block in cache per scan suffices).

:::

## Divide and conquer

The analysis of a recursive cache-oblivious algorithm uses the recursion tree, but stops at the level where the subproblem fits in cache: below that level all work is free, apart from loading the subproblem once.

::: {#prp-co-median .proposition name="Median finding"}

The linear-time selection algorithm (@def-median-of-medians), implemented with scans, uses $O(N/B+1)$ memory transfers.

:::

::: {.proof}

1. Each level does a constant number of scans: $MT(N)\le MT(N/5)+MT(7N/10+6)+O(N/B+1)$.

2. Stop the recursion at subproblems of size $O(B)$, which cost $O(1)$ transfers each: $MT(O(B))=O(1)$.

3. At depth $i$ of the recursion tree the subproblem sizes add up to at most $(\frac9{10})^iN$, because $\frac15+\frac7{10}=\frac9{10}$. So the $N/B$ parts of the scanning costs form a decreasing geometric series and sum to $O(N/B)$.

4. The "$+1$" parts are paid once per node of the tree. The number of nodes is dominated by the number $\ell(N)$ of leaves, with $\ell(N)=\ell(N/5)+\ell(7N/10)$ and $\ell(B)=1$, so $\ell(N)=O((N/B)^c)$ where $(\frac15)^c+(\frac7{10})^c=1$, that is $c\approx0.84<1$. This is $O(N/B+1)$ as well.

:::

::: {#prp-co-matrix .proposition name="Matrix multiplication"}

Multiplying $N\times N$ matrices by recursive block multiplication (four quadrants, eight recursive products), with matrices stored recursively quadrant by quadrant, uses $O\bigl(N^3/(B\sqrt M)+N^2/B+1\bigr)$ memory transfers.

:::

::: {.proof}

1. $MT(N)=8\,MT(N/2)+O(N^2/B+1)$ for the additions.

2. When $3N^2\le M$, the three matrices fit in cache and cost $O(N^2/B+1)$ to load, then nothing more.

3. The recursion reaches that size after depth $\log_2(N/\sqrt{M/3})$, with $8^{\text{depth}}=(N/\sqrt{M/3})^3$ leaves, each costing $O(M/B)$: $O\bigl(\frac{N^3}{M^{3/2}}\cdot\frac MB\bigr)=O\bigl(\frac{N^3}{B\sqrt M}\bigr)$. The levels above cost less (a geometric series dominated by the leaves).

:::

The naive triple loop costs about $N^3/B$ transfers, so recursion saves a factor $\sqrt M$.

## Searching: the van Emde Boas layout

A B-tree (@def-b-tree) with nodes of $\Theta(B)$ keys searches in $O(\log_BN)$ transfers, which is optimal, but it needs to know $B$. A binary search tree stored in sorted order or in BFS order costs $\Theta(\log(N/B))$ transfers.

::: {#thm-veb-layout .theorem name="Cache-oblivious search"}

Store a complete binary search tree of $N$ keys in the *van Emde Boas layout*: cut the tree at the middle level of edges into a top tree of height $\frac h2$ and about $\sqrt N$ bottom trees of height $\frac h2$; lay out the top tree recursively, followed by each bottom tree recursively. Then a root-to-leaf search costs $O(\log_BN)$ memory transfers, for every $B$.

:::

::: {.proof}

1. Consider the level of the recursion at which the pieces first have at most $B$ nodes. Each piece then has height between $\frac12\log_2B$ and $\log_2B$ and is stored contiguously, so it occupies at most $2$ blocks.

2. A search path of length $\log_2N$ passes through at most $\frac{\log_2N}{\frac12\log_2B}=2\log_BN$ such pieces.

3. So it costs at most $4\log_BN$ transfers.

:::

::: {#fig-cache-oblivious-algorithms-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (n1) at (4.00,0.00) {1};
\node[small vertex] (n2) at (2.00,-0.90) {2};
\draw (n1) -- (n2);
\node[small vertex] (n3) at (6.00,-0.90) {3};
\draw (n1) -- (n3);
\node[small vertex, fill=accentLight, draw=accent] (n4) at (1.00,-1.80) {4};
\draw (n2) -- (n4);
\node[small vertex, fill=accentLight, draw=accent] (n5) at (3.00,-1.80) {7};
\draw (n2) -- (n5);
\node[small vertex, fill=accentLight, draw=accent] (n6) at (5.00,-1.80) {10};
\draw (n3) -- (n6);
\node[small vertex, fill=accentLight, draw=accent] (n7) at (7.00,-1.80) {13};
\draw (n3) -- (n7);
\node[small vertex, fill=accentLight, draw=accent] (n8) at (0.50,-2.70) {5};
\draw (n4) -- (n8);
\node[small vertex, fill=accentLight, draw=accent] (n9) at (1.50,-2.70) {6};
\draw (n4) -- (n9);
\node[small vertex, fill=accentLight, draw=accent] (n10) at (2.50,-2.70) {8};
\draw (n5) -- (n10);
\node[small vertex, fill=accentLight, draw=accent] (n11) at (3.50,-2.70) {9};
\draw (n5) -- (n11);
\node[small vertex, fill=accentLight, draw=accent] (n12) at (4.50,-2.70) {11};
\draw (n6) -- (n12);
\node[small vertex, fill=accentLight, draw=accent] (n13) at (5.50,-2.70) {12};
\draw (n6) -- (n13);
\node[small vertex, fill=accentLight, draw=accent] (n14) at (6.50,-2.70) {14};
\draw (n7) -- (n14);
\node[small vertex, fill=accentLight, draw=accent] (n15) at (7.50,-2.70) {15};
\draw (n7) -- (n15);
\draw[faint, dashed] (-0.3,-1.35) -- (8.3,-1.35);
\end{tikzpicture}
\end{center}
```

The van Emde Boas layout of a complete binary tree with $15$ nodes; each node shows its position in memory. The tree is cut at the middle level (dashed): the top tree (positions $1$–$3$) is stored first, then each of the four bottom trees (highlighted) contiguously. Recursively, every subtree of the right size occupies consecutive memory.

:::

## Sorting

Merge sort with binary merges costs $O(\frac NB\log_2\frac NM)$ transfers. External-memory *$M/B$-way merge sort*, which merges $M/B$ runs at once (one block of each in cache), achieves the optimal $O(\frac NB\log_{M/B}\frac NB)$; cache-oblivious algorithms such as *funnelsort* reach the same bound without knowing $M$ and $B$ (assuming $M=\Omega(B^2)$).
