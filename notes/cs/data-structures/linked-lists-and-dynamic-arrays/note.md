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

::: {#fig-linked-lists-and-dynamic-arrays-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab] (ha) at (-1.5,1.2) {head};
\node[box] (na0) at (0.0,1.2) {$9$};
\draw[->] (ha) -- (na0);
\node[box] (na1) at (1.7,1.2) {$4$};
\draw[->] (na0) -- (na1);
\node[box] (na2) at (3.4,1.2) {$7$};
\draw[->] (na1) -- (na2);
\node[lab] (za) at (4.70,1.2) {none};
\draw[->] (na2) -- (za);
\node[lab] (hb) at (-1.5,0) {head};
\node[hl box] (nb0) at (0.0,0) {$2$};
\draw[->] (hb) -- (nb0);
\node[box] (nb1) at (1.7,0) {$9$};
\draw[->] (nb0) -- (nb1);
\node[box] (nb2) at (3.4,0) {$4$};
\draw[->] (nb1) -- (nb2);
\node[box] (nb3) at (5.1,0) {$7$};
\draw[->] (nb2) -- (nb3);
\node[lab] (zb) at (6.40,0) {none};
\draw[->] (nb3) -- (zb);
\node[lab, anchor=west] at (7.0,1.2) {before};
\node[lab, anchor=west] at (7.0,0) {after \texttt{insert\_first(2)}};
\end{tikzpicture}
\end{center}
```

Inserting at the front of a linked list: the new node points to the old head and becomes the head. Only two pointers change, whatever the length.

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

::: {#fig-linked-lists-and-dynamic-arrays-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$1$};
\node[lab, anchor=east] at (-0.100,0.275) {length 1};
\draw[cell frame] (0.000,-0.850) rectangle (0.550,-0.300);
\node[lab] at (0.275,-0.575) {$1$};
\draw[hl cell] (0.550,-0.850) rectangle (1.100,-0.300);
\node[lab] at (0.825,-0.575) {$2$};
\node[lab, anchor=east] at (-0.100,-0.575) {length 2};
\draw[cell frame] (0.000,-1.700) rectangle (0.550,-1.150);
\node[lab] at (0.275,-1.425) {$1$};
\draw[cell frame] (0.550,-1.700) rectangle (1.100,-1.150);
\node[lab] at (0.825,-1.425) {$2$};
\draw[cell frame] (1.100,-1.700) rectangle (1.650,-1.150);
\node[lab] at (1.375,-1.425) {$3$};
\draw[hl cell] (1.650,-1.700) rectangle (2.200,-1.150);
\node[lab] at (1.925,-1.425) {$4$};
\node[lab, anchor=east] at (-0.100,-1.425) {length 4};
\draw[cell frame] (0.000,-2.550) rectangle (0.550,-2.000);
\node[lab] at (0.275,-2.275) {$1$};
\draw[cell frame] (0.550,-2.550) rectangle (1.100,-2.000);
\node[lab] at (0.825,-2.275) {$2$};
\draw[cell frame] (1.100,-2.550) rectangle (1.650,-2.000);
\node[lab] at (1.375,-2.275) {$3$};
\draw[cell frame] (1.650,-2.550) rectangle (2.200,-2.000);
\node[lab] at (1.925,-2.275) {$4$};
\draw[hl cell] (2.200,-2.550) rectangle (2.750,-2.000);
\node[lab] at (2.475,-2.275) {$5$};
\draw[cell frame] (2.750,-2.550) rectangle (3.300,-2.000);
\draw[cell frame] (3.300,-2.550) rectangle (3.850,-2.000);
\draw[cell frame] (3.850,-2.550) rectangle (4.400,-2.000);
\node[lab, anchor=east] at (-0.100,-2.275) {length 8};
\node[lab, anchor=west] at (4.8,-1.0) {each row is a new array:};
\node[lab, anchor=west] at (4.8,-1.45) {the old items are copied over};
\end{tikzpicture}
\end{center}
```

Appending $1,2,\dots,5$ to a dynamic array. The array is reallocated only when full, at lengths $1,2,4,8$; the highlighted item is the one whose append triggered the copy (or, in the last row, the latest one). The copies cost $1+2+4<2\cdot5$ in total.

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
