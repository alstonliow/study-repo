---
title: "Sorting by Comparisons"
sources: [mit6006-3, mit6006r-3]
requires: [cs/data-structures/linked-lists-and-dynamic-arrays, math/discrete/sequences/solving-recurrences]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 3 and Recitation 3, in our own wording; proofs written out in steps. Algorithms are described in words, not copied code. -->

## Sorted arrays as sets

Storing the items of a set (@def-set-interface) in an array *sorted by key* makes `find_min` and `find_max` take $O(1)$ time (first and last slot) and `find` take $O(\log n)$ time by binary search.

::: {#prp-binary-search .proposition name="Binary search"}

Let $A[0],\dots,A[n-1]$ be sorted increasingly. To find key $k$, compare $k$ with the middle item $A[m]$, $m=\lfloor n/2\rfloor$: stop if equal, otherwise search $A[0..m-1]$ if $k$ is smaller and $A[m+1..n-1]$ if $k$ is larger, and report "absent" on an empty range. This finds $k$ (or correctly reports it absent) using at most $\lfloor\log_2n\rfloor+1$ comparisons.

:::

::: {.proof}

1. *Correctness*, by strong induction on $n$. For $n=0$ the answer "absent" is right. For $n\ge1$, if $k<A[m]$ then $k$ is not at any position $\ge m$ because the array is sorted, so it suffices to search the left part, which is done correctly by induction; the case $k>A[m]$ is symmetric.

2. *Count.* Each comparison leaves a range of at most $\lfloor n/2\rfloor$ items. After $j$ comparisons at most $\lfloor n/2^j\rfloor$ items remain, which is $0$ once $2^j>n$, that is, after $\lfloor\log_2n\rfloor+1$ comparisons.

:::

But inserting into or deleting from a sorted array shifts items and takes $\Theta(n)$ time, and building one requires sorting.

## The sorting problem

::: {#def-sorting-problem .definition name="Sorting"}

*Sorting*: given an array $A$ of $n$ items with keys, output a permutation $B$ of $A$ with $B[i-1].\mathrm{key}\le B[i].\mathrm{key}$ for $1\le i<n$. A sorting algorithm is

1. *destructive* if it overwrites $A$ instead of producing a new array,
2. *in place* if it uses only $O(1)$ extra space (so it is destructive), and
3. *stable* if items with equal keys appear in $B$ in the same relative order as in $A$.

:::

Trying all $n!$ permutations and checking each in $\Theta(n)$ time ("permutation sort") is correct by exhaustion but takes $\Omega(n!\cdot n)$ time. The following algorithms do much better.

## Selection sort and insertion sort

::: {#def-selection-sort .definition name="Selection sort"}

*Selection sort* of $A[0..i]$: if $i>0$, find the index $j$ of a largest item of $A[0..i]$, swap $A[j]$ and $A[i]$, and selection sort $A[0..i-1]$.

:::

::: {#def-insertion-sort .definition name="Insertion sort"}

*Insertion sort* of $A[0..i]$: if $i>0$, insertion sort $A[0..i-1]$, then *insert* $A[i]$: while it is smaller than its left neighbour, swap it with that neighbour.

:::

::: {#thm-selection-insertion-sort .theorem name="Selection and insertion sort"}

Both algorithms sort $A$ in place, in $\Theta(n^2)$ time in the worst case. Insertion sort is stable.

:::

::: {.proof}

1. *Selection sort is correct*, by induction on $i$. One item is sorted. For $i>0$, the item moved to position $i$ is a largest one, which is a correct last item of a sorted order of $A[0..i]$, and $A[0..i-1]$ is then sorted by induction.

2. *Insertion sort is correct*, by induction on $i$. After $A[0..i-1]$ is sorted, the swaps move $A[i]$ left past exactly the items larger than it and stop at the first item that is not larger, so $A[0..i]$ is sorted. Equal items are never swapped past each other, so the sort is stable.

3. *Time.* Finding a largest item of $A[0..i]$ takes $\Theta(i)$ comparisons, and inserting $A[i]$ takes up to $i$ swaps (exactly $i$ when the input is in decreasing order). Both satisfy $T(n)=T(n-1)+\Theta(n)$, so $T(n)=\Theta\bigl(\sum_{i=1}^ni\bigr)=\Theta(n^2)$.

4. Both use only a constant number of extra words (written as loops instead of recursion), so they are in place.

:::

::: {#rmk-comparison-sorting-swaps .remark name="Strengths of the two"}

Selection sort makes only $O(n)$ swaps, which matters if moving an item is expensive. Insertion sort does one swap per *inversion* (pair out of order), so on an almost sorted array, with each item at most $k$ places from its final position, it runs in $O(nk)$ time.

:::

## Merge sort

::: {#def-merge-sort .definition name="Merge sort"}

*Merge sort* of $A[a..b-1]$: if it has at least two items, let $c=\lceil(a+b)/2\rceil$, merge sort $A[a..c-1]$ and $A[c..b-1]$, copy the two sorted halves to arrays $L$ and $R$, and *merge* them back into $A[a..b-1]$: repeatedly move the smaller of the first remaining items of $L$ and $R$ (the one from $L$ on a tie) to the next slot of $A$, until both are empty.

:::

::: {#thm-merge-sort .theorem name="Merge sort" related="exm-merge-sort-extra"}

Merge sort is a stable sort that runs in $\Theta(n\log n)$ time and uses $\Theta(n)$ extra space.

:::

::: {.proof}

1. *Merging is correct.* At each step the smallest remaining item overall is the smaller of the first remaining items of $L$ and $R$, because both are sorted. So the items are written in non-decreasing order. Taking from $L$ on ties keeps equal items in their original order.

2. *Merge sort is correct*, by strong induction on the length: a range of $0$ or $1$ items is sorted, and a longer range is split into two shorter ones, sorted by induction and then merged correctly by step 1.

3. *Time.* Merging $n$ items costs $\Theta(n)$, so $T(n)=2T(n/2)+\Theta(n)$ (for $n$ a power of $2$; other $n$ only change constants). In the recursion tree, level $i$ has $2^i$ calls on $n/2^i$ items each, $\Theta(n)$ work per level, and there are $\log_2n+1$ levels, so $T(n)=\Theta(n\log n)$; this is case 2 of the master theorem (@thm-master-theorem).

4. *Space.* The copies $L$ and $R$ at the top level have $n$ items; lower levels can reuse one buffer of size $n$.

:::

::: {#rmk-comparison-sorting-solving-recurrences .remark name="Three ways to solve a recurrence"}

The recurrences of this note can be solved by *substitution* (guess the answer and check it by induction), by a *recursion tree* (add up the work at the nodes level by level), or by the *master theorem* (@thm-master-theorem), which packages the recursion-tree computation for $T(n)=aT(n/b)+f(n)$.

:::
