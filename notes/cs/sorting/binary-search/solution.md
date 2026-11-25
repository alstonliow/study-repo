<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6006s20-2-q3" status="draft"}
Search outwards from both ends at once with doubling steps, then finish with binary search.

1. Measure positions in kilometers from the north end. For $j=0,1,2,\dots$: teleport to kilometer $2^j$ and ask the tracker, then teleport to kilometer $n-2^j$ and ask. Stop at the first $j$ for which Datum is found, or is *not south* of kilometer $2^j$ (then he lies between kilometers $2^{j-1}$ and $2^j$), or is *not north* of kilometer $n-2^j$ (then he lies between $n-2^j$ and $n-2^{j-1}$).

2. Binary search (@prp-binary-search) inside that interval of length $2^{j-1}$, using the tracker as the comparison.

*Correctness.* While $2^j<k$, Datum is strictly between the two probes, so the loop continues; it stops at the first $j$ with $2^j\ge k$ (at the latest), and the stopping test identifies an interval that contains him.

*Count.* The loop runs for at most $\lceil\log_2k\rceil+1$ values of $j$, two probes each, and the binary search over an interval of length at most $2^j<2k$ takes $O(\log k)$ probes. In total $O(\log k)$ locations.
:::

::: {.solution for="prob-mit6006s20-2-q4" status="draft"}
*Data.* The chat is a doubly linked list of message nodes in sending order, with a tail pointer. The viewers are stored in an array sorted by ID; each viewer record has a "banned" flag and a linked list of pointers to that viewer's message nodes.

- `build(V)`: sort the viewers by ID (merge sort), create empty records and an empty chat: $O(n\log n)$.
- `send(v, m)`: find $v$'s record by binary search, $O(\log n)$. If $v$ is banned do nothing; otherwise append a node for $m$ at the tail of the chat and a pointer to it to $v$'s list, $O(1)$.
- `recent(k)`: walk back from the tail through at most $k$ nodes: $O(k)$.
- `ban(v)`: find $v$ in $O(\log n)$, set the flag, and for each of $v$'s $n_v$ message nodes unlink it from the chat in $O(1)$ (doubly linked: `prev` and `next` are known). Total $O(n_v+\log n)$.

All bounds are worst case (the viewer array is static, so no amortization is needed).
:::
