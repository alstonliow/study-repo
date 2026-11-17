---
title: "Linked Lists and Dynamic Arrays"
sources: [mit6006-2, mit6006r-2]
requires: [cs/data-structures/interfaces]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 2 and Recitation 2, in our own wording; proofs written out in steps. -->

Three ways to implement the sequence interface (@def-sequence-interface), with their worst-case costs collected at the end.

## Arrays

::: {#def-array-sequence .definition name="Array sequence"}

An *array sequence* stores the $n$ items in a static array (@def-static-array) of length exactly $n$. Reading and writing slot $i$ take $O(1)$ time. To insert or delete an item, allocate a new array of the new length and copy the items over, shifting those after the changed position; this takes $\Theta(n)$ time.

:::

## Linked lists

::: {#def-linked-list .definition name="Linked list"}

A *(singly) linked list* stores each item in a *node* with two fields, `item` and `next`, the address of the next node (or none for the last node). The list keeps the address of the first node, its *head*. A *doubly linked list* also gives each node a `prev` field and keeps the address of the last node, its *tail*.

:::

Changing a few addresses changes the list, so `insert_first` and `delete_first` take $O(1)$ time: the new node points to the old head and becomes the head. But reaching item $i$ means following $i$ links, so `get_at(i)` and `set_at(i, x)` take $\Theta(i)$ time in the worst case.

## Dynamic arrays

A dynamic array keeps the fast reads of an array and makes the operations at the end fast as well, by allocating more room than it needs.

::: {#def-dynamic-array .definition name="Dynamic array"}

A *dynamic array* stores the $n$ items in the first $n$ slots of a static array of some length $m\ge n$. `insert_last(x)` writes $x$ into slot $n$ if $n<m$; if the array is full ($n=m$), it first allocates a new array of length $2m$ (length $1$ if $m=0$), copies the items over, and frees the old one. `delete_last()` simply forgets the last item. Python's `list` is a dynamic array.

:::

A single `insert_last` can take $\Theta(n)$ time, but such expensive steps are rare. To capture this we average over a sequence of operations.

::: {#def-amortized-cost .definition name="Amortized cost"}

An operation has *amortized cost* $T(n)$ if, for every $k$, any sequence of $k$ operations, starting from an empty structure, takes at most $k\,T(n)$ time in total.

:::

::: {#thm-dynamic-array-append .theorem name="Appending is constant amortized time"}

Starting from an empty dynamic array, any sequence of $k$ `insert_last` operations takes $O(k)$ time. So `insert_last` takes $O(1)$ amortized time.

:::

::: {.proof}

1. Each operation does $O(1)$ work besides copying. Copying happens only when the array is full, at sizes $n=1,2,4,\dots,2^j$ with $2^j<k$, and copying $n$ items costs $O(n)$.

2. The total copying cost is at most a constant times $1+2+4+\dots+2^j=2^{j+1}-1<2k$ (geometric sum, @exm-well-ordering-geometric-sum).

3. So the $k$ operations cost $O(k)+O(2k)=O(k)$ in total.

:::

::: {#rmk-linked-lists-and-dynamic-arrays-growth .remark name="Any constant factor works"}

Growing by any constant factor $c>1$ instead of $2$ also works: the copying costs form a geometric series with ratio $c$, summing to $O(k)$. Growing by a constant *amount* does not: copies at sizes $d,2d,3d,\dots$ cost $\Theta(k^2/d)$ in total.

:::

To keep the space linear when items are deleted, the array must also shrink, but shrinking as soon as it is half full would let alternating inserts and deletes at the boundary cost $\Theta(n)$ each.

::: {#prp-dynamic-array-shrink .proposition name="Shrinking without thrashing"}

Let a dynamic array double when full and, after a deletion, reallocate to length $2n$ whenever $n<m/4$. Then `insert_last` and `delete_last` take $O(1)$ amortized time and the array always has length $O(n)$ (for $n\ge1$).

:::

::: {.proof}

1. Right after any reallocation, and before the item that triggered a growth is written, the array is exactly half full: $n=m/2$.

2. The next reallocation happens when $n$ reaches $m$ or drops below $m/4$, so at least $m/4$ operations happen between two reallocations.

3. That reallocation copies at most $m$ items, which is $O(m/4)$, so it can be charged at $O(1)$ to each of the at least $m/4$ operations since the previous one. Every operation is charged by at most one reallocation, so $k$ operations cost $O(k)$ in total.

4. Between reallocations $m/4\le n\le m$, so $m\le4n$.

:::

## Summary

| data structure | `build(X)` | `get_at`, `set_at` | `insert_first`, `delete_first` | `insert_last`, `delete_last` | `insert_at`, `delete_at` |
|---|---|---|---|---|---|
| array | $n$ | $1$ | $n$ | $n$ | $n$ |
| linked list | $n$ | $n$ | $1$ | $n$ | $n$ |
| dynamic array | $n$ | $1$ | $n$ | $1$ (amortized) | $n$ |

All entries are $O(\cdot)$ worst-case bounds unless marked amortized. A doubly linked list with a tail pointer also makes the operations at the end $O(1)$, and a dynamic array with free room at both ends makes the operations at the front $O(1)$ amortized. Making every operation logarithmic needs trees (@sec-cs-data-structures-avl-trees).
