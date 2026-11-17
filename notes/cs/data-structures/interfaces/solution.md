<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6006s20-1-q2" status="draft"}
(a) For $m=0,\dots,k-2$: $x=$ `D.delete_at(i + k - 1)`, then `D.insert_at(i + m, x)`. Before step $m$, positions $i,\dots,i+m-1$ hold the last $m$ items of the block in reverse order and positions $i+m,\dots,i+k-1$ hold the remaining items in their original order; step $m$ moves the last of these to position $i+m$, which keeps the invariant. After $k-1$ steps the block is reversed. Each step is two operations of $O(\log n)$ time (the size stays $n$), so $O(k\log n)$.

(b) If $j<i$: for $m=0,\dots,k-1$, $x=$ `D.delete_at(i + m)`, `D.insert_at(j + m, x)`. Each item of the block, taken in order, is removed from its place (still at $i+m$, since the items moved so far are now in front of it) and inserted just after the previously moved ones, in front of the item that was at index $j$. If $j\ge i+k$: $k$ times, $x=$ `D.delete_at(i)` and `D.insert_at(j - 1, x)`. Removing the first remaining item of the block shifts the item formerly at $j$ to index $j-1$, and inserting at $j-1$ puts $x$ right in front of it, after the items moved before. Either way $2k$ operations, $O(k\log n)$ time.
:::
