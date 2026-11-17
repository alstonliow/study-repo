::: {.problem #prob-mit6006s20-1-q3 origin="external" source="mit6006s20-1-q3"}
**Binder Bookmarks**

Sisa Limpson is a very organized second grade student who keeps all of her course notes on individual pages stored in a three-ring binder. If she has $n$ pages of notes in her binder, the first page is at index $0$ and the last page is at index $n-1$. While studying, Sisa often reorders pages of her notes. To help her reorganize, she has two bookmarks, $A$ and $B$, which help her keep track of locations in the binder.

Describe a database to keep track of pages in Sisa's binder, supporting the following operations, where $n$ is the number of pages in the binder at the time of the operation. Assume that both bookmarks will be placed in the binder before any shift or move operation can occur, and that bookmark $A$ will always be at a lower index than $B$. For each operation, state whether your running time is worst-case or amortized.

| operation | specification |
|---|---|
| `build(X)` | Initialize database with pages from iterator $X$ in $O(|X|)$ time. |
| `place_mark(i, m)` | Place bookmark $m\in\{A,B\}$ between the page at index $i$ and the page at index $i+1$ in $O(n)$ time. |
| `read_page(i)` | Return the page at index $i$ in $O(1)$ time. |
| `shift_mark(m, d)` | Take the bookmark $m\in\{A,B\}$, currently in front of the page at index $i$, and move it in front of the page at index $i+d$ for $d\in\{-1,1\}$ in $O(1)$ time. |
| `move_page(m)` | Take the page currently in front of bookmark $m\in\{A,B\}$, and move it in front of the other bookmark in $O(1)$ time. |
:::

::: {.problem #prob-mit6006s20-1-q4 origin="external" source="mit6006s20-1-q4"}
**Doubly Linked List**

In Lecture 2, we described a singly linked list. In this problem, you will implement a doubly linked list, supporting some additional constant-time operations. Each node `x` of a doubly linked list maintains an `x.prev` pointer to the node preceeding it in the sequence, in addition to an `x.next` pointer to the node following it in the sequence. A doubly linked list `L` maintains a pointer to `L.tail`, the last node in the sequence, in addition to `L.head`, the first node in the sequence. For this problem, doubly linked lists should not maintain their length.

(a) Given a doubly linked list as described above, describe algorithms to implement the following sequence operations, each in $O(1)$ time.

`insert_first(x)` `insert_last(x)` `delete_first()` `delete_last()`

(b) Given two nodes `x1` and `x2` from a doubly linked list `L`, where `x1` occurs before `x2`, describe a constant-time algorithm to remove all nodes from `x1` to `x2` inclusive from `L`, and return them as a new doubly linked list.

(c) Given node `x` from a doubly linked list `L1` and second doubly linked list `L2`, describe a constant-time algorithm to splice list `L2` into list `L1` after node `x`. After the splice operation, `L1` should contain all items previously in either list, and `L2` should be empty.

(d) Implement the operations above in the `Doubly_Linked_List_Seq` class in the provided code template; do not modify the `Doubly_Linked_List_Node` class. You can download the code template including some test cases from the website.
:::
