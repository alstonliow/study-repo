::: {.problem #prob-mit6006s20-1-q2 origin="external" source="mit6006s20-1-q2"}
Given a data structure $D$ that supports Sequence operations:

- `D.build(X)` in $O(n)$ time, and
- `D.insert_at(i, x)` and `D.delete_at(i)`, each in $O(\log n)$ time,

where $n$ is the number of items stored in $D$ at the time of the operation, describe algorithms to implement the following higher-level operations in terms of the provided lower-level operations. Each operation below should run in $O(k\log n)$ time. Recall, `delete_at` returns the deleted item.

(a) `reverse(D, i, k)`: Reverse in $D$ the order of the $k$ items starting at index $i$ (up to index $i+k-1$).

(b) `move(D, i, k, j)`: Move the $k$ items in $D$ starting at index $i$, in order, to be in front of the item at index $j$. Assume that expression $i\le j<i+k$ is false.
:::
