---
title: "Sorting in Linear Time"
sources: [mit6006-5, mit6006r-5]
requires: [cs/data-structures/hashing]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 5 and Recitation 5, in our own wording; proofs written out in steps. -->

The $\Omega(n\log n)$ bound (@thm-comparison-sort-lower-bound) applies only to comparison sorts. If the keys are integers in a range $\{0,\dots,u-1\}$, using them as array indices sorts faster. Throughout, $n$ is the number of items.

::: {#def-direct-access-sort .definition name="Direct access array sort"}

If the keys are *distinct* integers in $\{0,\dots,u-1\}$: insert every item into a direct access array of length $u$ (@def-direct-access-array), then read the slots in order $0,1,\dots,u-1$ and output the items found. This takes $\Theta(n+u)$ time.

:::

## Counting sort

To allow equal keys, each slot holds a sequence of items instead of a single item, as in chaining.

::: {#def-counting-sort .definition name="Counting sort"}

*Counting sort* of items with integer keys in $\{0,\dots,u-1\}$: make an array of $u$ empty sequences; for each item in input order, append it to the sequence at index equal to its key; then output the sequences in order $0,1,\dots,u-1$, each from first to last.

:::

::: {#prp-counting-sort .proposition name="Counting sort"}

Counting sort is a stable sort that runs in $\Theta(n+u)$ time.

:::

::: {.proof}

1. Items are output in non-decreasing order of key, because sequence $k$ is output before sequence $k+1$.

2. Items with equal key $k$ all lie in sequence $k$, in the order they were appended, which is their input order. So the sort is stable.

3. Creating the sequences and reading them out takes $\Theta(u)$, and each item is appended and output once in $O(1)$ (amortized) time, so $\Theta(n+u)$ in total.

:::

::: {#rmk-linear-sorting-counting .remark name="Why it is called counting sort"}

A common implementation avoids sequences: count how many items have each key, turn the counts into prefix sums (the first output position of each key), and place the items in input order at those positions. The bounds are the same.

:::

## Tuple sort and radix sort

::: {#lem-tuple-sort .lemma name="Tuple sort"}

Let each key be a tuple $(k_1,\dots,k_c)$, ordered lexicographically ($k_1$ most significant). Sorting the items by $k_c$, then by $k_{c-1}$, …, then by $k_1$, each time with a *stable* sort, sorts them lexicographically.

:::

::: {.proof}

1. Claim: after the passes on $k_c,k_{c-1},\dots,k_j$, the items are sorted lexicographically by $(k_j,\dots,k_c)$. We prove it by induction on the number of passes.

2. After the first pass the items are sorted by $k_c$.

3. Suppose after the pass on $k_{j+1}$ they are sorted by $(k_{j+1},\dots,k_c)$, and consider the stable pass on $k_j$. Take two items $x$ and $y$ with $(x_j,\dots,x_c)<(y_j,\dots,y_c)$ lexicographically. If $x_j<y_j$, the pass puts $x$ first. If $x_j=y_j$, then $(x_{j+1},\dots,x_c)<(y_{j+1},\dots,y_c)$, so $x$ was before $y$ before the pass, and stability keeps it there.

4. After the pass on $k_1$ the items are sorted by the whole tuple.

:::

The order matters: sorting from the most significant entry first would let the later passes destroy the earlier order.

::: {#def-radix-sort .definition name="Radix sort"}

*Radix sort* of items with integer keys in $\{0,\dots,u-1\}$: write each key in base $n$ as a $c$-digit number with $c=\lceil\log_nu\rceil$ (at least $1$), and tuple-sort the digit tuples using counting sort for each digit.

:::

::: {#thm-radix-sort .theorem name="Radix sort"}

Radix sort sorts $n$ items with keys in $\{0,\dots,u-1\}$, stably, in $O\bigl(n\,(1+\log_nu)\bigr)$ time. In particular, if $u\le n^c$ for a constant $c$, it runs in $O(n)$ time.

:::

::: {.proof}

1. Correctness follows from @lem-tuple-sort, since counting sort is stable (@prp-counting-sort) and the lexicographic order of the base-$n$ digit tuples is the order of the keys.

2. Computing the digits takes $O(c)$ arithmetic operations per key. Each of the $c$ passes is a counting sort with $n$ items and digit range $n$, costing $\Theta(n+n)=\Theta(n)$.

3. The total is $O(cn)$ with $c=O(1+\log_nu)$.

:::

For example, with $n=5$ the keys $17,3,24,22,12$ become the base-$5$ pairs $32,03,44,42,22$; sorting by the last digit gives $32,42,22,03,44$, and then by the first digit $03,22,32,42,44$, that is $3,12,17,22,24$.

| algorithm | time | in place | stable | note |
|---|---|---|---|---|
| insertion sort | $n^2$ | yes | yes | $O(nk)$ if items are at most $k$ places off |
| selection sort | $n^2$ | yes | no | $O(n)$ swaps |
| merge sort | $n\log n$ | no | yes | optimal comparison sort |
| counting sort | $n+u$ | no | yes | $O(n)$ when $u=O(n)$ |
| radix sort | $n+n\log_nu$ | no | yes | $O(n)$ when $u=O(n^c)$ |
