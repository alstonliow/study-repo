---
title: "Range Minimum Queries"
sources: [mit6851-15]
requires: [cs/advanced-data-structures/cartesian-trees, cs/advanced-data-structures/lowest-common-ancestor]
status: draft
---

<!-- Added 2026-11-26 from MIT 6.851 (Spring 2012), Lecture 15, in our own wording; proofs written out in steps. -->

The range-minimum query (RMQ) problem is the static core of many contest tasks. A sparse table answers queries in $O(1)$ with $O(n\log n)$ space; combining it with lookup tables for tiny blocks gives $O(1)$ queries in $O(n)$ space (Harel–Tarjan; the version here is due to Bender and Farach-Colton).

::: {#def-rmq .definition name="Range minimum query"}

Given an array $A[0..n-1]$ of values from an ordered set, preprocess it so that a query $\operatorname{rmq}(i,j)$ with $i\le j$ returns a position $k\in[i,j]$ with $A[k]=\min A[i..j]$. Returning the position (not the value) is the harder form, since the value is then one lookup away.

:::

::: {#def-sparse-table .definition name="Sparse table"}

For $0\le k\le\lfloor\log_2 n\rfloor$ and $0\le i\le n-2^k$ let

$$
M[k][i]=\operatorname{rmq}\bigl(i,\,i+2^k-1\bigr),\qquad M[0][i]=i,
$$

$$
M[k][i]=\text{the better of } M[k-1][i] \text{ and } M[k-1][i+2^{k-1}] \text{ by } A.
$$

:::

::: {#thm-sparse-table .theorem name="Sparse table"}

The table has $O(n\log n)$ entries and is built in $O(n\log n)$ time, and for $i\le j$ with $k=\lfloor\log_2(j-i+1)\rfloor$

$$
\operatorname{rmq}(i,j)=\text{the better of } M[k][i] \text{ and } M[k][j-2^k+1].
$$

So each query takes $O(1)$ time (with a precomputed table of $\lfloor\log_2 \ell\rfloor$ or a leading-zero count).

:::

::: {.proof}

1. *Size and time.* There are $\lfloor\log_2 n\rfloor+1$ rows of at most $n$ entries, and each entry is one comparison of two entries of the row above.

2. *Query.* The two intervals $[i,i+2^k-1]$ and $[j-2^k+1,j]$ both have length $2^k\le j-i+1<2^{k+1}$, so together they cover $[i,j]$ (their lengths add to at least $j-i+1$ and they reach both ends).

3. Since the minimum of a union is the minimum of the minima, and covering an element twice does no harm for a minimum, the better of the two stored answers is a minimum of $A[i..j]$.

:::

::: {#exm-range-minimum-query-1 .example name="A sparse table"}

For $A=[8,7,2,8,6,9,4,5]$ the table stores (values shown instead of positions) the rows $[8,7,2,8,6,9,4,5]$, $[7,2,2,6,6,4,4]$, $[2,2,2,4,4]$, $[2]$. The query $\operatorname{rmq}(0,4)$ has length $5$, so $k=2$; it combines the entries at $i=0$ and $i=1$ of row $2$, both with value $2$, so the answer is position $2$.

:::

::: {#fig-range-minimum-query-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \v [count=\i from 0] in {8,7,2,8,6,9,4,5} {\draw[cell frame] (0.55*\i,0) rectangle +(0.55,0.55); \node[lab] at (0.55*\i+0.275,0.275) {$\v$};}
\foreach \v [count=\i from 0] in {7,2,2,6,6,4,4} {\draw[cell frame] (0.55*\i,0.8) rectangle +(0.55,0.55); \node[lab] at (0.55*\i+0.275,1.075) {$\v$};}
\foreach \v [count=\i from 0] in {2,2,2,4,4} {\draw[cell frame] (0.55*\i,1.6) rectangle +(0.55,0.55); \node[lab] at (0.55*\i+0.275,1.875) {$\v$};}
\draw[hl cell] (0,1.6) rectangle +(0.55,0.55);
\draw[hl cell] (0.55,1.6) rectangle +(0.55,0.55);
\node[lab, anchor=east] at (-0.1,0.275) {$k=0$};
\node[lab, anchor=east] at (-0.1,1.075) {$k=1$};
\node[lab, anchor=east] at (-0.1,1.875) {$k=2$};
\end{tikzpicture}
\end{center}
```

Rows $k=0,1,2$ of the sparse table of $A$ (the row $k=3$ is the single value $2$). The two highlighted entries of row $2$ answer $\operatorname{rmq}(0,4)$: they cover $A[0..3]$ and $A[1..4]$.

:::

Two ideas remove the logarithm from the space. First, the problem for arbitrary values reduces to one with small integers, and then to differences $\pm1$.

::: {#prp-rmq-pm1 .proposition name="Reduction to $\pm1$ RMQ"}

Every range-minimum problem reduces in linear time to one on an array whose adjacent entries differ by exactly $1$: build the Cartesian tree of $A$ (@thm-cartesian-linear), write down the depths of the nodes visited by an Euler tour of the tree (length $2n-1$, consecutive depths differ by $\pm1$), and remember for each position of $A$ the first visit of its node. Then $\operatorname{rmq}_A(i,j)$ is the node whose depth is minimal between the first visits of $i$ and $j$, which is $\operatorname{lca}(i,j)$ by @thm-cartesian-range-minimum.

:::

::: {#thm-rmq-linear .theorem name="Constant-time RMQ in linear space"}

An array of length $n$ with adjacent differences $\pm1$ can be preprocessed in $O(n)$ time and space so that $\operatorname{rmq}$ takes $O(1)$ time on the word RAM. With @prp-rmq-pm1 this holds for every array, and for $\operatorname{lca}$ in a tree.

:::

::: {.proof}

1. *Blocks.* Cut the array into blocks of $b=\tfrac12\log_2 n$ entries. Store the minimum of each block in an array of $n/b$ entries and build a sparse table on it: $O\bigl(\tfrac nb\log\tfrac nb\bigr)=O(n)$ entries.

2. *Query.* A query $[i,j]$ is a suffix of one block, then a run of whole blocks (one sparse-table query), then a prefix of another block; or lies inside one block. The block minima give the middle part, and at most two in-block queries remain.

3. *Blocks are few kinds.* Subtract the first entry of a block: the block is then determined by its $b-1$ differences $\pm1$, so there are at most $2^{b-1}\le\sqrt n$ distinct blocks. The position of a minimum inside a block depends only on this shape.

4. *Tables.* For each shape store the answers to all $b^2$ pairs $(i,j)$ inside the block, each a number below $b$: $\sqrt n\cdot b^2\cdot O(\log b)$ bits, which is $o(n)$. Each block keeps a pointer to the table of its shape.

5. Every query therefore costs a constant number of table lookups and comparisons.

:::

For contests the plain sparse table of @thm-sparse-table is almost always enough: it is short to write, and $n\log n$ entries fit for $n$ up to a few million. The idempotent trick (overlapping intervals) works for any operation with $x\circ x=x$ such as min, max or gcd, but not for sums.
