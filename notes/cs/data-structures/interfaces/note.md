---
title: "Sequence and Set Interfaces"
sources: [mit6006-1, mit6006-2, mit6006r-2]
requires: [cs/algorithms/problems-and-algorithms]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lectures 1-2 and Recitation 2, in our own wording. Operation names follow the course. -->

An *interface* (also called an abstract data type or API) says *what* operations are supported; a *data structure* says *how* they are supported. One interface can have several data structures with different costs. Two interfaces cover most of what follows.

::: {#def-sequence-interface .definition name="Sequence interface"}

A *sequence* stores items $x_0,x_1,\dots,x_{n-1}$ in an order chosen from outside (the *extrinsic* order: first, last, $i$-th). Its operations are

| kind | operation | meaning |
|---|---|---|
| container | `build(X)` | make a sequence from the items of $X$ |
| | `len()` | the number of items $n$ |
| static | `iter_seq()` | list the items in sequence order |
| | `get_at(i)`, `set_at(i, x)` | read or replace the $i$-th item |
| dynamic | `insert_at(i, x)`, `delete_at(i)` | add $x$ as the $i$-th item; remove and return the $i$-th item |
| | `insert_first(x)`, `delete_first()`, `insert_last(x)`, `delete_last()` | the same at the two ends |

A *stack* is a sequence used only through `insert_last` and `delete_last`; a *queue* only through `insert_last` and `delete_first`.

:::

::: {#def-set-interface .definition name="Set interface"}

A *set* stores items with distinct *keys* (item $x$ has key $x.\mathrm{key}$), and its order comes from the keys (the *intrinsic* order). Its operations are

| kind | operation | meaning |
|---|---|---|
| container | `build(X)`, `len()` | as for sequences |
| static | `find(k)` | the item with key $k$, if any |
| dynamic | `insert(x)` | add $x$, replacing an item with the same key |
| | `delete(k)` | remove and return the item with key $k$ |
| order | `iter_ord()` | list the items in increasing key order |
| | `find_min()`, `find_max()` | the item with the smallest or largest key |
| | `find_next(k)`, `find_prev(k)` | the item with the smallest key $>k$, or the largest key $<k$ |

A set without the order operations is a *dictionary*.

:::

The key may be the whole item, but usually an item carries more data than its key (a student record keyed by student number).

::: {#def-static-array .definition name="Static array"}

A *static array* of length $n$ is a block of $n$ consecutive words of memory. In the word-RAM (@def-word-ram) the address of slot $i$ is the start address plus $i$, so `get_at(i)` and `set_at(i, x)` take $O(1)$ time; allocating the array takes $\Theta(n)$ time. A slot can hold the address of a larger object, so arrays can store arbitrary items.

:::

::: {#rmk-interfaces-set-from-sequence .remark name="A set from a sequence"}

Any sequence data structure gives a (slow) set: store the items in any order and answer `find(k)` and the order operations by scanning all $n$ items, in $O(n)$ time. Faster sets come from keeping the items sorted (@sec-cs-data-structures-comparison-sorting), from hashing (@sec-cs-data-structures-hashing), or from balanced search trees (@sec-cs-data-structures-avl-trees).

:::
