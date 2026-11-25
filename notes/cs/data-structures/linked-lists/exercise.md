::: {.problem #prob-mit6006s20-1-q4 origin="external" source="mit6006s20-1-q4"}
**Doubly Linked List**

In Lecture 2, we described a singly linked list. In this problem, you will implement a doubly linked list, supporting some additional constant-time operations. Each node `x` of a doubly linked list maintains an `x.prev` pointer to the node preceeding it in the sequence, in addition to an `x.next` pointer to the node following it in the sequence. A doubly linked list `L` maintains a pointer to `L.tail`, the last node in the sequence, in addition to `L.head`, the first node in the sequence. For this problem, doubly linked lists should not maintain their length.

(a) Given a doubly linked list as described above, describe algorithms to implement the following sequence operations, each in $O(1)$ time.

`insert_first(x)` `insert_last(x)` `delete_first()` `delete_last()`

(b) Given two nodes `x1` and `x2` from a doubly linked list `L`, where `x1` occurs before `x2`, describe a constant-time algorithm to remove all nodes from `x1` to `x2` inclusive from `L`, and return them as a new doubly linked list.

(c) Given node `x` from a doubly linked list `L1` and second doubly linked list `L2`, describe a constant-time algorithm to splice list `L2` into list `L1` after node `x`. After the splice operation, `L1` should contain all items previously in either list, and `L2` should be empty.

(d) Implement the operations above in the `Doubly_Linked_List_Seq` class in the provided code template; do not modify the `Doubly_Linked_List_Node` class. You can download the code template including some test cases from the website.
:::

::: {.problem #prob-mit6006r-2-q1 origin="external" source="mit6006r-2-q1"}
Suppose the next pointer of the last node of a linked list points to an earlier node in the list, creating a cycle. Given a pointer to the head of the list (without knowing its size), describe a linear-time algorithm to find the number of nodes in the cycle. Can you do this while using only constant additional space outside of the original linked list?
:::
