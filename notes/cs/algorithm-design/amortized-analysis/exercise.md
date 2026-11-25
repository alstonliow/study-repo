::: {.problem #prob-mit6046s15-4-q1 origin="external" source="mit6046s15-4-q1"}
**Extreme FIFO Queues**

Design a data structure that maintains a FIFO queue of integers, supporting operations ENQUEUE, DEQUEUE, and FIND-MIN, each in $O(1)$ amortized time. In other words, any sequence of $m$ operations should take time $O(m)$. You may assume that, in any execution, all the items that get enqueued are distinct.

(a) Describe your data structure. Include clear invariants describing its key properties. *Hint:* Use an actual queue plus auxiliary data structure(s) for bookkeeping.

(b) Describe carefully, in words or pseudo-code, your ENQUEUE, DEQUEUE and FIND-MIN procedures.

(c) Prove that your operations give the right answers. *Hint:* You may want to prove that their correctness follows from your data structure invariants. In that case you should also sketch arguments for why the invariants hold.

(d) Analyze the time complexity: the worst-case cost for each operation, and the amortized cost of any sequence of $m$ operations.
:::
