---
title: "Priority Queues and Binary Heaps"
sources: [mit6006-8, mit6006r-8]
requires: [cs/data-structures/avl-trees]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 8 and Recitation 8, in our own wording; proofs written out in steps. -->

## Priority queues

::: {#def-priority-queue .definition name="Priority queue"}

A *priority queue* stores items with keys (priorities) and supports `build(X)`, `insert(x)`, `find_max()` and `delete_max()` (remove and return an item of largest key). A *min* priority queue has `find_min()` and `delete_min()` instead.

:::

Priority queues schedule processes in an operating system, decide which packet a router sends next, find the next event in a simulation, and drive graph algorithms such as Dijkstra's (@sec-cs-graph-algorithms-dijkstra).

::: {#rmk-binary-heaps-pq-sort .remark name="Priority queue sort"}

Any priority queue sorts: insert all $n$ items, then call `delete_max` $n$ times to get the items in decreasing order. The time is at most $n\cdot T_{\text{insert}}+n\cdot T_{\text{delete\_max}}$. With an unsorted dynamic array as the queue this is selection sort; with a sorted dynamic array it is insertion sort; with a set AVL tree it is AVL sort, $O(n\log n)$ but not in place. A binary heap gives an $O(n\log n)$ sort that *is* in place.

:::

## Complete binary trees stored in arrays

::: {#def-complete-binary-tree .definition name="Complete binary tree, array representation"}

A binary tree is *complete* if every depth $d$ has the full $2^d$ nodes except possibly the largest depth, whose nodes are as far left as possible. An array $Q[0..n-1]$ represents the complete binary tree with $n$ nodes in which the nodes are numbered in reading order (by depth, and left to right within a depth). Then
$$\mathrm{left}(i)=2i+1,\qquad\mathrm{right}(i)=2i+2,\qquad\mathrm{parent}(i)=\Bigl\lfloor\frac{i-1}2\Bigr\rfloor,$$
so no pointers are stored. The height is $\lfloor\log_2n\rfloor$.

:::

The formulas hold because depth $d$ occupies indices $2^d-1,\dots,2^{d+1}-2$, and the children of the $j$-th node at depth $d$ are the $(2j)$-th and $(2j+1)$-th nodes at depth $d+1$.

## Binary heaps

::: {#def-max-heap .definition name="Max-heap"}

An array $Q$ is a *max-heap* if every node is at least as large as its children: $Q[i]\ge Q[j]$ for $j\in\{\mathrm{left}(i),\mathrm{right}(i)\}$ with $j<n$ (comparing keys).

:::

::: {#prp-heap-root-max .proposition name="The root is a maximum"}

In a max-heap, every node is at least as large as every node of its subtree. In particular $Q[0]$ is a largest item.

:::

::: {.proof}

Let $j$ be in the subtree of $i$, and induct on $d=\operatorname{depth}(j)-\operatorname{depth}(i)$. If $d=0$ then $j=i$. If $d>0$, the parent of $j$ is in the subtree of $i$ at distance $d-1$, so $Q[i]\ge Q[\mathrm{parent}(j)]$ by induction, and $Q[\mathrm{parent}(j)]\ge Q[j]$ by the heap property.

:::

::: {#prp-heap-insert-delete .proposition name="Insert and delete_max"}

1. *Insert:* append $x$ at index $n$ and *heapify up*: while $x$ is not the root and is larger than its parent, swap it with its parent.
2. *Delete_max:* swap $Q[0]$ with $Q[n-1]$, remove and return the last item, and *heapify down* from the root: while the current item is smaller than one of its children, swap it with its larger child.

Both keep the max-heap property and take $O(\log n)$ time (amortized, because of the dynamic array).

:::

::: {.proof}

1. *Heapify up.* Invariant: the heap property holds everywhere except possibly between $x$ and its parent. Initially only that pair can be wrong. If $x$ is larger than its parent $p$, swap them. Now $x$ is larger than its new children (the old $p$, and $p$'s other child, which was at most $p$), and the items below the old $p$ were at most $p$, which is at most $x$. The old $p$ in $x$'s former place is larger than the children it inherits, which were in its subtree. So again only the pair ($x$, new parent) can be wrong. When the loop stops, the heap is valid.

2. *Heapify down* is symmetric. Invariant: the property holds everywhere except possibly between the current item $y$ and its children. If $y$ is smaller than a child, swapping with the *larger* child $c$ puts $c$ above $y$ and above its sibling, which were both at most $c$; only the pair ($y$, its new children) can now be wrong.

3. Each swap moves one level, and the height is $\lfloor\log_2n\rfloor$, so $O(\log n)$ swaps.

:::

## Heap sort and linear-time build

::: {#def-heap-sort .definition name="Heap sort"}

*Heap sort* of an array $A$ of length $n$: treat a prefix $A[0..s-1]$ as a max-heap, with $s=0$ at first. Insert $A[s]$ for $s=0,\dots,n-1$ (grow the prefix by one and heapify up). Then $n$ times delete the maximum: swap $A[0]$ with $A[s-1]$, shrink the prefix by one and heapify down. The removed maxima fill the array from the end, so $A$ ends up sorted.

:::

Heap sort is in place and runs in $O(n\log n)$ time; it is not stable. Building the heap can even be done in linear time.

::: {#thm-build-heap .theorem name="Building a heap in $O(n)$ time"}

Heapifying down at every index $i=n-1,n-2,\dots,0$ (from the leaves up) turns any array into a max-heap in $O(n)$ time.

:::

::: {.proof}

1. *Correctness*, by induction on the number of indices processed: after processing $i$, the subtree of every processed index is a max-heap. When $i$ is processed its children's subtrees are already heaps, so the only possible violation is at $i$, and heapifying down from $i$ fixes it (@prp-heap-insert-delete).

2. *Time.* Heapifying down from a node of height $k$ costs $O(1+k)$. At most $\lceil n/2^{k+1}\rceil$ nodes have height $k$. So the total is
   $$O\Bigl(\sum_{k\ge0}\frac n{2^{k+1}}(1+k)\Bigr)=O\Bigl(n\sum_{k\ge0}\frac{k+1}{2^{k+1}}\Bigr)=O(2n)=O(n),$$
   using $\sum_{k\ge1}k/2^k=2$.

:::

Inserting the items one by one instead costs $\sum_i\Theta(\log i)=\Theta(\log n!)=\Theta(n\log n)$ in the worst case: most nodes are deep, and heapify up pays for depth, while heapify down pays for height, which is small for most nodes.

::: {#rmk-binary-heaps-avl-pq .remark name="Other priority queues"}

A sequence AVL tree storing the items in any order and augmented with the location of the maximum of each subtree is also a priority queue: `build` in $O(n)$, `find_max` in $O(1)$, `insert` and `delete_max` in $O(\log n)$. The binary heap is simpler and in place. Both structures also work for *multisets* (repeated keys) if the comparisons are taken with $\le$.

:::

| priority queue | `build` | `insert` | `delete_max` | sort time | in place | sort |
|---|---|---|---|---|---|---|
| dynamic array | $n$ | $1$ (a) | $n$ | $n^2$ | yes | selection sort |
| sorted dynamic array | $n\log n$ | $n$ | $1$ (a) | $n^2$ | yes | insertion sort |
| set AVL tree | $n\log n$ | $\log n$ | $\log n$ | $n\log n$ | no | AVL sort |
| binary heap | $n$ | $\log n$ (a) | $\log n$ (a) | $n\log n$ | yes | heap sort |
