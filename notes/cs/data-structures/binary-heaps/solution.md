<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6006s20-4-q2" status="draft"}
Index $i$ has children $2i+1$ and $2i+2$ (@def-complete-binary-tree).

(a) Root $4$ with children $12,8$; $12$ has children $21,14$; $8$ has children $9,17$. Every parent is smaller than its children: a *min-heap*.

(b) Root $701$ with children $253,24$; $253$ has children $229,17$; $24$ has child $22$. Every parent is larger: a *max-heap*.

(c) Root $2$ with children $9,13$; $9$ has children $8,0$; $13$ has child $2$. Neither ($9>0$ but $2<9$). Heapify down from the last parent to the root:

1. swap $13$ and its child $2$: `[2, 9, 2, 8, 0, 13]`;
2. swap $9$ and its smaller child $0$: `[2, 0, 2, 8, 9, 13]`;
3. swap the root $2$ and its smaller child $0$: `[0, 2, 2, 8, 9, 13]`; now $2$ at index $1$ is at most its children $8,9$.

The result is a min-heap.

(d) Root $1$ with children $3,6$; $3$ has children $5,4$; $6$ has children $9,7$: a *min-heap*.
:::

::: {.solution for="prob-mit6006s20-4-q3" status="draft"}
(a) Build a max-heap on the pairs keyed by score in $O(|A|)$ time (@thm-build-heap), then call `delete_max` $k$ times, each $O(\log|A|)$, and return the registration numbers removed. Each removed pair has a score at least that of every pair still in the heap, so the $k$ removed pairs have the highest scores. Total $O(|A|+k\log|A|)$.

(b) Search the heap from the root, visiting a node only if its score exceeds $x$: start at index $0$; at a node with score $>x$, output its registration number and visit both children; at a node with score $\le x$ (or past the end of the array), stop. By @prp-heap-root-max every node below a node with score $\le x$ also has score $\le x$, so no qualifying garden is missed. Every visited node is either output or a child of an output node, so at most $n_x+2n_x+1$ nodes are visited: $O(n_x)$ time. (The heap is not modified.)
:::

::: {.solution for="prob-mit6006s20-4-q4" status="draft"}
*Data.*

1. A max-heap $H$ of the farms keyed by *available capacity* (initially $c_i$), with each farm record storing its current index in $H$; every swap inside $H$ updates the two indices, so a farm's key can be raised or lowered in $O(\log n)$ by heapifying up or down from its position.
2. For each farm, a doubly linked list of the buildings it supplies.
3. A hash table $F$ from address to farm record, and a hash table $G$ from building name to (farm record, demand, node in that farm's list).

*Operations.*

- `initialize(S)`: create the records, build $H$ in $O(n)$ (@thm-build-heap) and $F$ in $O(n)$ expected time. *Expected* $O(n)$.
- `power_on(b, d)`: the root of $H$ has the largest available capacity. If it is less than $d$, no farm can take the building. Otherwise connect to it: append $b$ to its list, insert $b$ into $G$, and lower its key by $d$ with a heapify down. $O(\log n)$, *expected amortized* (because of the insertion into $G$).
- `power_off(b)`: look $b$ up in $G$, unlink its node from the farm's list in $O(1)$, remove $b$ from $G$, and raise the farm's key by $d$ with a heapify up. $O(\log n)$ *expected amortized*.
- `customers(s)`: find the farm in $F$ ($O(1)$ expected) and list its buildings: $O(k)$ *expected* (worst case once the record is found).
:::

::: {.solution for="prob-mit6006r-8-q4" status="draft"}
Write $r(x)$ for the sorted position of item $x$, so the item at index $i$ has $|i-r(A[i])|\le k$.

(a)

1. Insertion sort spends $O(1)$ per swap plus $O(n)$ overall, and the number of swaps equals the number of *inversions* (pairs $s<t$ with $A[s]>A[t]$).

2. Fix $t$ and count the $s<t$ with $A[s]>A[t]$. Every such $A[s]$ has rank above $r(A[t])\ge t-k$, so $r(A[s])>t-k$ and hence $s\ge r(A[s])-k>t-2k$. So $s\in(t-2k,t)$: fewer than $2k$ choices.

3. Summing over $t$, there are fewer than $2kn$ inversions, so insertion sort takes $O(nk)$ time.

(b) Keep a min-heap of at most $k+1$ items. Insert $A[0],\dots,A[k]$. Then for $j=0,1,\dots,n-1$: delete the minimum and write it to output position $j$, and insert $A[j+k+1]$ if it exists.

*Correctness.* The item $x$ with $r(x)=j$ sits at an index $i\le j+k$, so it has been inserted by the time output position $j$ is filled. All smaller items were output before (by induction), so $x$ is the minimum of the heap at that moment.

*Time.* The heap never holds more than $k+1$ items, so each of the $n$ inserts and $n$ deletions costs $O(\log k)$: $O(n\log k)$ in total. Since $k<n$, this is never slower than $O(n\log n)$.
:::
