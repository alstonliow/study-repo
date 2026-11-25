---
title: "Linked Lists and Dynamic Arrays"
sources: [mit6006-2, mit6006r-2]
requires: [cs/data-structures/interfaces]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 2 and Recitation 2, in our own wording; proofs written out in steps. On 2026-11-25 linked lists and dynamic arrays moved to their own notes (SPEC §8.6); this note is their overview. -->

Three ways to implement the sequence interface (@def-sequence-interface), with their worst-case costs collected at the end.

## Arrays

::: {#def-array-sequence .definition name="Array sequence"}

An *array sequence* stores the $n$ items in a static array (@def-static-array) of length exactly $n$. Reading and writing slot $i$ take $O(1)$ time. To insert or delete an item, allocate a new array of the new length and copy the items over, shifting those after the changed position; this takes $\Theta(n)$ time.

:::

## Linked lists and dynamic arrays

Linked lists (@sec-cs-data-structures-linked-lists) make the operations at the front fast; dynamic arrays (@sec-cs-data-structures-dynamic-arrays) keep the fast reads of an array and make the operations at the end fast.

## Summary

| data structure | `build(X)` | `get_at`, `set_at` | `insert_first`, `delete_first` | `insert_last`, `delete_last` | `insert_at`, `delete_at` |
|---|---|---|---|---|---|
| array | $n$ | $1$ | $n$ | $n$ | $n$ |
| linked list | $n$ | $n$ | $1$ | $n$ | $n$ |
| dynamic array | $n$ | $1$ | $n$ | $1$ (amortized) | $n$ |

All entries are $O(\cdot)$ worst-case bounds unless marked amortized. A doubly linked list with a tail pointer also makes the operations at the end $O(1)$, and a dynamic array with free room at both ends makes the operations at the front $O(1)$ amortized. Making every operation logarithmic needs trees (@sec-cs-data-structures-avl-trees).
