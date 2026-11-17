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

::: {#fig-binary-heaps-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.900) rectangle (0.550,1.450);
\node[lab] at (0.275,1.175) {$9$};
\node[lab,tick] at (0.275,0.720) {0};
\draw[cell frame] (0.550,0.900) rectangle (1.100,1.450);
\node[lab] at (0.825,1.175) {$7$};
\node[lab,tick] at (0.825,0.720) {1};
\draw[cell frame] (1.100,0.900) rectangle (1.650,1.450);
\node[lab] at (1.375,1.175) {$8$};
\node[lab,tick] at (1.375,0.720) {2};
\draw[cell frame] (1.650,0.900) rectangle (2.200,1.450);
\node[lab] at (1.925,1.175) {$3$};
\node[lab,tick] at (1.925,0.720) {3};
\draw[cell frame] (2.200,0.900) rectangle (2.750,1.450);
\node[lab] at (2.475,1.175) {$5$};
\node[lab,tick] at (2.475,0.720) {4};
\draw[cell frame] (2.750,0.900) rectangle (3.300,1.450);
\node[lab] at (3.025,1.175) {$6$};
\node[lab,tick] at (3.025,0.720) {5};
\draw[cell frame] (3.300,0.900) rectangle (3.850,1.450);
\node[lab] at (3.575,1.175) {$2$};
\node[lab,tick] at (3.575,0.720) {6};
\draw[cell frame] (3.850,0.900) rectangle (4.400,1.450);
\node[lab] at (4.125,1.175) {$1$};
\node[lab,tick] at (4.125,0.720) {7};
\draw[cell frame] (4.400,0.900) rectangle (4.950,1.450);
\node[lab] at (4.675,1.175) {$0$};
\node[lab,tick] at (4.675,0.720) {8};
\draw[cell frame] (4.950,0.900) rectangle (5.500,1.450);
\node[lab] at (5.225,1.175) {$4$};
\node[lab,tick] at (5.225,0.720) {9};
\node[small vertex] (q0) at (2.75,0.00) {$9$};
\node[lab,tick] at (3.13,0.22) {0};
\node[small vertex] (q1) at (0.95,-0.85) {$7$};
\node[lab,tick] at (1.33,-0.63) {1};
\draw (q0) -- (q1);
\node[small vertex] (q2) at (4.55,-0.85) {$8$};
\node[lab,tick] at (4.93,-0.63) {2};
\draw (q0) -- (q2);
\node[small vertex] (q3) at (0.05,-1.70) {$3$};
\node[lab,tick] at (0.43,-1.48) {3};
\draw (q1) -- (q3);
\node[small vertex] (q4) at (1.85,-1.70) {$5$};
\node[lab,tick] at (2.23,-1.48) {4};
\draw (q1) -- (q4);
\node[small vertex] (q5) at (3.65,-1.70) {$6$};
\node[lab,tick] at (4.03,-1.48) {5};
\draw (q2) -- (q5);
\node[small vertex] (q6) at (5.45,-1.70) {$2$};
\node[lab,tick] at (5.83,-1.48) {6};
\draw (q2) -- (q6);
\node[small vertex] (q7) at (-0.40,-2.55) {$1$};
\node[lab,tick] at (-0.02,-2.33) {7};
\draw (q3) -- (q7);
\node[small vertex] (q8) at (0.50,-2.55) {$0$};
\node[lab,tick] at (0.88,-2.33) {8};
\draw (q3) -- (q8);
\node[small vertex] (q9) at (1.40,-2.55) {$4$};
\node[lab,tick] at (1.78,-2.33) {9};
\draw (q4) -- (q9);
\end{tikzpicture}
\end{center}
```

An array of length $10$ and the complete binary tree it represents (small numbers are indices). The children of index $i$ are $2i+1$ and $2i+2$; this array is a max-heap.

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

::: {#fig-binary-heaps-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$9$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$7$};
\draw[cell frame] (1.100,0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$8$};
\draw[cell frame] (1.650,0.000) rectangle (2.200,0.550);
\node[lab] at (1.925,0.275) {$3$};
\draw[cell frame] (2.200,0.000) rectangle (2.750,0.550);
\node[lab] at (2.475,0.275) {$5$};
\draw[cell frame] (2.750,0.000) rectangle (3.300,0.550);
\node[lab] at (3.025,0.275) {$6$};
\draw[cell frame] (3.300,0.000) rectangle (3.850,0.550);
\node[lab] at (3.575,0.275) {$2$};
\draw[cell frame] (3.850,0.000) rectangle (4.400,0.550);
\node[lab] at (4.125,0.275) {$1$};
\draw[cell frame] (4.400,0.000) rectangle (4.950,0.550);
\node[lab] at (4.675,0.275) {$0$};
\draw[hl cell] (4.950,0.000) rectangle (5.500,0.550);
\node[lab] at (5.225,0.275) {$10$};
\node[lab, anchor=east] at (-0.100,0.275) {append};
\draw[cell frame] (0.000,-0.800) rectangle (0.550,-0.250);
\node[lab] at (0.275,-0.525) {$9$};
\draw[cell frame] (0.550,-0.800) rectangle (1.100,-0.250);
\node[lab] at (0.825,-0.525) {$7$};
\draw[cell frame] (1.100,-0.800) rectangle (1.650,-0.250);
\node[lab] at (1.375,-0.525) {$8$};
\draw[cell frame] (1.650,-0.800) rectangle (2.200,-0.250);
\node[lab] at (1.925,-0.525) {$3$};
\draw[hl cell] (2.200,-0.800) rectangle (2.750,-0.250);
\node[lab] at (2.475,-0.525) {$10$};
\draw[cell frame] (2.750,-0.800) rectangle (3.300,-0.250);
\node[lab] at (3.025,-0.525) {$6$};
\draw[cell frame] (3.300,-0.800) rectangle (3.850,-0.250);
\node[lab] at (3.575,-0.525) {$2$};
\draw[cell frame] (3.850,-0.800) rectangle (4.400,-0.250);
\node[lab] at (4.125,-0.525) {$1$};
\draw[cell frame] (4.400,-0.800) rectangle (4.950,-0.250);
\node[lab] at (4.675,-0.525) {$0$};
\draw[hl cell] (4.950,-0.800) rectangle (5.500,-0.250);
\node[lab] at (5.225,-0.525) {$5$};
\node[lab, anchor=east] at (-0.100,-0.525) {swap};
\draw[cell frame] (0.000,-1.600) rectangle (0.550,-1.050);
\node[lab] at (0.275,-1.325) {$9$};
\draw[hl cell] (0.550,-1.600) rectangle (1.100,-1.050);
\node[lab] at (0.825,-1.325) {$10$};
\draw[cell frame] (1.100,-1.600) rectangle (1.650,-1.050);
\node[lab] at (1.375,-1.325) {$8$};
\draw[cell frame] (1.650,-1.600) rectangle (2.200,-1.050);
\node[lab] at (1.925,-1.325) {$3$};
\draw[hl cell] (2.200,-1.600) rectangle (2.750,-1.050);
\node[lab] at (2.475,-1.325) {$7$};
\draw[cell frame] (2.750,-1.600) rectangle (3.300,-1.050);
\node[lab] at (3.025,-1.325) {$6$};
\draw[cell frame] (3.300,-1.600) rectangle (3.850,-1.050);
\node[lab] at (3.575,-1.325) {$2$};
\draw[cell frame] (3.850,-1.600) rectangle (4.400,-1.050);
\node[lab] at (4.125,-1.325) {$1$};
\draw[cell frame] (4.400,-1.600) rectangle (4.950,-1.050);
\node[lab] at (4.675,-1.325) {$0$};
\draw[cell frame] (4.950,-1.600) rectangle (5.500,-1.050);
\node[lab] at (5.225,-1.325) {$5$};
\node[lab, anchor=east] at (-0.100,-1.325) {swap};
\draw[hl cell] (0.000,-2.400) rectangle (0.550,-1.850);
\node[lab] at (0.275,-2.125) {$10$};
\node[lab,tick] at (0.275,-2.580) {0};
\draw[hl cell] (0.550,-2.400) rectangle (1.100,-1.850);
\node[lab] at (0.825,-2.125) {$9$};
\node[lab,tick] at (0.825,-2.580) {1};
\draw[cell frame] (1.100,-2.400) rectangle (1.650,-1.850);
\node[lab] at (1.375,-2.125) {$8$};
\node[lab,tick] at (1.375,-2.580) {2};
\draw[cell frame] (1.650,-2.400) rectangle (2.200,-1.850);
\node[lab] at (1.925,-2.125) {$3$};
\node[lab,tick] at (1.925,-2.580) {3};
\draw[cell frame] (2.200,-2.400) rectangle (2.750,-1.850);
\node[lab] at (2.475,-2.125) {$7$};
\node[lab,tick] at (2.475,-2.580) {4};
\draw[cell frame] (2.750,-2.400) rectangle (3.300,-1.850);
\node[lab] at (3.025,-2.125) {$6$};
\node[lab,tick] at (3.025,-2.580) {5};
\draw[cell frame] (3.300,-2.400) rectangle (3.850,-1.850);
\node[lab] at (3.575,-2.125) {$2$};
\node[lab,tick] at (3.575,-2.580) {6};
\draw[cell frame] (3.850,-2.400) rectangle (4.400,-1.850);
\node[lab] at (4.125,-2.125) {$1$};
\node[lab,tick] at (4.125,-2.580) {7};
\draw[cell frame] (4.400,-2.400) rectangle (4.950,-1.850);
\node[lab] at (4.675,-2.125) {$0$};
\node[lab,tick] at (4.675,-2.580) {8};
\draw[cell frame] (4.950,-2.400) rectangle (5.500,-1.850);
\node[lab] at (5.225,-2.125) {$5$};
\node[lab,tick] at (5.225,-2.580) {9};
\node[lab, anchor=east] at (-0.100,-2.125) {swap};
\end{tikzpicture}
\end{center}
```

Inserting $10$ into the max-heap $9,7,8,3,5,6,2,1,0$: append it at index $9$, then swap it with its parent (indices $4$, $1$, $0$) while it is larger. Highlighted cells are the pair just swapped. Each swap moves one level up the tree, so there are $O(\log n)$ of them.

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

::: {#fig-binary-heaps-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$2$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$9$};
\draw[cell frame] (1.100,0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$4$};
\draw[cell frame] (1.650,0.000) rectangle (2.200,0.550);
\node[lab] at (1.925,0.275) {$7$};
\draw[cell frame] (2.200,0.000) rectangle (2.750,0.550);
\node[lab] at (2.475,0.275) {$1$};
\draw[cell frame] (2.750,0.000) rectangle (3.300,0.550);
\node[lab] at (3.025,0.275) {$8$};
\draw[cell frame] (3.300,0.000) rectangle (3.850,0.550);
\node[lab] at (3.575,0.275) {$6$};
\draw[cell frame] (3.850,0.000) rectangle (4.400,0.550);
\node[lab] at (4.125,0.275) {$3$};
\node[lab, anchor=east] at (-0.100,0.275) {start};
\draw[cell frame] (0.000,-0.800) rectangle (0.550,-0.250);
\node[lab] at (0.275,-0.525) {$2$};
\draw[cell frame] (0.550,-0.800) rectangle (1.100,-0.250);
\node[lab] at (0.825,-0.525) {$9$};
\draw[hl cell] (1.100,-0.800) rectangle (1.650,-0.250);
\node[lab] at (1.375,-0.525) {$8$};
\draw[cell frame] (1.650,-0.800) rectangle (2.200,-0.250);
\node[lab] at (1.925,-0.525) {$7$};
\draw[cell frame] (2.200,-0.800) rectangle (2.750,-0.250);
\node[lab] at (2.475,-0.525) {$1$};
\draw[hl cell] (2.750,-0.800) rectangle (3.300,-0.250);
\node[lab] at (3.025,-0.525) {$4$};
\draw[cell frame] (3.300,-0.800) rectangle (3.850,-0.250);
\node[lab] at (3.575,-0.525) {$6$};
\draw[cell frame] (3.850,-0.800) rectangle (4.400,-0.250);
\node[lab] at (4.125,-0.525) {$3$};
\node[lab, anchor=east] at (-0.100,-0.525) {down from 2};
\draw[hl cell] (0.000,-1.600) rectangle (0.550,-1.050);
\node[lab] at (0.275,-1.325) {$9$};
\draw[hl cell] (0.550,-1.600) rectangle (1.100,-1.050);
\node[lab] at (0.825,-1.325) {$2$};
\draw[cell frame] (1.100,-1.600) rectangle (1.650,-1.050);
\node[lab] at (1.375,-1.325) {$8$};
\draw[cell frame] (1.650,-1.600) rectangle (2.200,-1.050);
\node[lab] at (1.925,-1.325) {$7$};
\draw[cell frame] (2.200,-1.600) rectangle (2.750,-1.050);
\node[lab] at (2.475,-1.325) {$1$};
\draw[cell frame] (2.750,-1.600) rectangle (3.300,-1.050);
\node[lab] at (3.025,-1.325) {$4$};
\draw[cell frame] (3.300,-1.600) rectangle (3.850,-1.050);
\node[lab] at (3.575,-1.325) {$6$};
\draw[cell frame] (3.850,-1.600) rectangle (4.400,-1.050);
\node[lab] at (4.125,-1.325) {$3$};
\node[lab, anchor=east] at (-0.100,-1.325) {down from 0};
\draw[cell frame] (0.000,-2.400) rectangle (0.550,-1.850);
\node[lab] at (0.275,-2.125) {$9$};
\draw[hl cell] (0.550,-2.400) rectangle (1.100,-1.850);
\node[lab] at (0.825,-2.125) {$7$};
\draw[cell frame] (1.100,-2.400) rectangle (1.650,-1.850);
\node[lab] at (1.375,-2.125) {$8$};
\draw[hl cell] (1.650,-2.400) rectangle (2.200,-1.850);
\node[lab] at (1.925,-2.125) {$2$};
\draw[cell frame] (2.200,-2.400) rectangle (2.750,-1.850);
\node[lab] at (2.475,-2.125) {$1$};
\draw[cell frame] (2.750,-2.400) rectangle (3.300,-1.850);
\node[lab] at (3.025,-2.125) {$4$};
\draw[cell frame] (3.300,-2.400) rectangle (3.850,-1.850);
\node[lab] at (3.575,-2.125) {$6$};
\draw[cell frame] (3.850,-2.400) rectangle (4.400,-1.850);
\node[lab] at (4.125,-2.125) {$3$};
\node[lab, anchor=east] at (-0.100,-2.125) {down from 0};
\draw[cell frame] (0.000,-3.200) rectangle (0.550,-2.650);
\node[lab] at (0.275,-2.925) {$9$};
\draw[cell frame] (0.550,-3.200) rectangle (1.100,-2.650);
\node[lab] at (0.825,-2.925) {$7$};
\draw[cell frame] (1.100,-3.200) rectangle (1.650,-2.650);
\node[lab] at (1.375,-2.925) {$8$};
\draw[hl cell] (1.650,-3.200) rectangle (2.200,-2.650);
\node[lab] at (1.925,-2.925) {$3$};
\draw[cell frame] (2.200,-3.200) rectangle (2.750,-2.650);
\node[lab] at (2.475,-2.925) {$1$};
\draw[cell frame] (2.750,-3.200) rectangle (3.300,-2.650);
\node[lab] at (3.025,-2.925) {$4$};
\draw[cell frame] (3.300,-3.200) rectangle (3.850,-2.650);
\node[lab] at (3.575,-2.925) {$6$};
\draw[hl cell] (3.850,-3.200) rectangle (4.400,-2.650);
\node[lab] at (4.125,-2.925) {$2$};
\node[lab, anchor=east] at (-0.100,-2.925) {down from 0};
\end{tikzpicture}
\end{center}
```

Building a max-heap from $2,9,4,7,1,8,6,3$ by heapifying down at indices $3,2,1,0$. Each row shows one swap (highlighted); nodes near the bottom move little, which is why the total is $O(n)$. The last row is a max-heap.

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
