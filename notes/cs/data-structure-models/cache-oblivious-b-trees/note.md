---
title: "Cache-Oblivious B-Trees"
sources: [mit6851-7, mit6851-8]
requires: [cs/data-structure-models/ordered-file-maintenance, cs/data-structure-models/cache-oblivious-algorithms]
aliases: [cs/algorithm-topics/cache-oblivious-b-trees]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-27 from MIT 6.851 (Spring 2012), Lectures 7 and 8, in our own wording; proofs written out in steps. The external-memory results of Lecture 7 and the cache-oblivious sorting, priority queue and range-search structures of Lectures 8 and 9 are listed in the remark and are not proved. The existing note cs/algorithm-topics/cache-oblivious-algorithms contains the static search tree in the van Emde Boas layout (@thm-veb-layout); merge candidates are proposed to the owner. -->

The static van Emde Boas layout (@thm-veb-layout) searches in $O(\log_{B+1}N)$ transfers without knowing $B$. Making the tree dynamic needs a place for new keys: an ordered file (@thm-ofm) under the tree.

::: {#def-co-b-tree .definition name="Cache-oblivious B-tree"}

Keep the $N$ keys in an ordered-file array (with gaps). Build a complete binary tree over the array's slots, stored in the van Emde Boas layout, whose leaves point to the slots; an inner node stores the maximum key below it (a gap counts as $-\infty$). To reduce update cost, group the keys into $\Theta(N/\log N)$ groups of $\Theta(\log N)$ keys, keep each group between $25\%$ and $100\%$ full in its own array, and build the tree and the ordered file over the group minima only.

:::

::: {#thm-co-b-tree .theorem name="Cache-oblivious B-tree"}

The structure supports search in $O(\log_{B+1}N)$ and insertion and deletion in $O(\log_{B+1}N)$ amortised memory transfers, for every $B$ and without knowing $B$.

:::

::: {.proof}

1. *Search* in the tree over the group minima takes $O(\log_{B+1}(N/\log N))\subseteq O(\log_{B+1}N)$ transfers by @thm-veb-layout, plus one scan of a group, $O(1+\log N/B)=O(\log_BN)$ transfers.

2. *Update without indirection.* Finding the place costs $O(\log_{B+1}N)$. The ordered file rearranges $O(\log^2N)$ items by $O(1)$ scans: $O(1+\log^2N/B)$ transfers. Then the tree is updated in post-order for the changed leaves: in the lowest two levels, a vEB triangle of size at most $B$ spans at most two blocks, so $O(1)$ blocks per triangle are loaded in an amortised sense and there are $O(1+\log^2N/B)$ such triangles; the roots of the larger triangles form a tree with the same number of nodes, which can be updated by one block read each; and the remaining path to the root costs $O(\log_{B+1}N)$. The total is $O(\log_{B+1}N+\log^2N/B)$, too much only when $B=o(\log N\log\log N)$.

3. *Indirection.* A group has $\Theta(\log N)$ keys, so reorganising one costs $O(\log N/B+1)=O(\log_BN)$ transfers, and the tree and the file now hold only $N/\log N$ entries, with $O(1+\log^2(N/\log N)/B)$ cost that is dominated.

4. *Splits and merges.* A group that becomes too full is split, a too-empty one is merged with a neighbour and split if needed; each such step needs $\Omega(\log N)$ updates, so its cost is $O(1)$ amortised per update.

:::

::: {#rmk-co-b-trees-1 .remark name="Other results of the memory-hierarchy lectures"}

In the external-memory model (cache of $M$ words, blocks of $B$): scanning costs $\lceil N/B\rceil$; a B-tree with branching factor $\Theta(B)$ searches in $O(\log_{B+1}N)$, which is optimal; sorting costs $O\bigl(\tfrac NB\log_{M/B}\tfrac NB\bigr)$ by $\tfrac MB$-way merge sort, optimal in the comparison model, and inserting into a B-tree is not optimal for sorting; permuting costs $\min\{N,\ \tfrac NB\log_{M/B}\tfrac NB\}$ in the indivisible model; buffer trees process batched updates in $O\bigl(\tfrac1B\log_{M/B}\tfrac NB\bigr)$ amortised each. Cache-obliviously (under the tall-cache assumption $M=\Omega(B^{1+\varepsilon})$) sorting reaches the same bound by *lazy funnelsort* (a $K$-funnel is a binary tree of buffers, merging $K^3$ items in $O\bigl(\tfrac{K^3}B\log_{M/B}\tfrac{K^3}B+K\bigr)$ transfers, and funnelsort is a $N^{1/3}$-way merge sort with an $N^{1/3}$-funnel), the priority queue in $O\bigl(\tfrac1B\log_{M/B}\tfrac NB\bigr)$ amortised per operation (levels of size $N,N^{2/3},N^{4/9},\dots$ with up and down buffers), and funnelsort with a sweep gives batched orthogonal range searching. LRU or FIFO with a cache twice as large is $O(1)$-competitive with the optimal offline paging, which justifies assuming optimal caching.

:::
