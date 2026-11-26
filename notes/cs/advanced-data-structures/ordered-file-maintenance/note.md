---
title: "Ordered File Maintenance and Order Maintenance"
sources: [mit6851-8]
requires: [cs/algorithm-design/amortized-analysis]
status: draft
---

<!-- Added 2026-11-27 from MIT 6.851 (Spring 2012), Lecture 8, in our own wording; proofs written out in steps. The cache-oblivious priority queue of the same lecture is only mentioned. The picture is our own. -->

Keep $N$ items in a given order in an array of size $O(N)$ with only $O(1)$-sized gaps (so that scanning $k$ items costs $O(1+k/B)$ transfers), under insertion next to a given item and deletion. Moving items is unavoidable; the structure keeps the moves local.

::: {#def-ofm .definition name="Ordered file maintenance"}

Store the items in an array of $\Theta(N)$ slots, in order, with gaps of $O(1)$ empty slots between neighbours. Imagine a complete binary tree over the array whose leaves are chunks of $\Theta(\log N)$ slots (the tree is never built; it is implicit in the indices). The *density* of a node is the number of items in its interval divided by its number of slots. With the root at depth $0$ and the leaves at depth $h=\Theta(\log N)$, a node at depth $d$ is *within threshold* if

$$
\frac12-\frac14\cdot\frac dh\ \le\ \rho\ \le\ \frac34+\frac14\cdot\frac dh .
$$

(So the root must have density in $[\tfrac12,\tfrac34]$ and a leaf chunk in $[\tfrac14,1]$.) To insert or delete next to an item, change its leaf chunk, then walk up to the nearest ancestor that is within threshold and redistribute the items of its interval evenly.

:::

::: {#thm-ofm .theorem name="Ordered file maintenance"}

Each insertion or deletion rearranges an interval of $O(\log^2N)$ items in amortised time, by $O(1)$ interleaved scans; that is $O(1+\log^2N/B)$ amortised memory transfers. (The bound is conjectured optimal; worst-case versions exist.)

:::

::: {.proof}

1. Let $D$ be a node at depth $d$ that is rebuilt, so $D$ is within threshold and the redistribution gives every descendant of $D$ the same density as $D$.

2. The thresholds of the children (depth $d+1$) are wider than those of $D$ by $1/(4h)$ on each side, so after the rebuild a child with an interval of $m$ slots is at least $m/(4h)=\Omega(m/\log N)$ updates away from violating them.

3. Rebuilding $D$ costs $O(m)$ (its interval has $\le2m$ slots). Charge it to the $\Omega(m/\log N)$ updates that must have happened in a child since the last rebuild of $D$: each update is charged $O(\log N)$ at this level.

4. An update lies below $O(\log N)$ ancestors, and may be charged at each of them, so the amortised cost is $O(\log N)\cdot O(\log N)=O(\log^2N)$ moves.

:::

::: {#def-list-labeling .definition name="List labeling and order maintenance"}

*List labeling* keeps integer labels on the items of a list, increasing along the list, under insertion between two items and deletion. *Order maintenance* keeps a list under insertion and deletion and answers "does $x$ precede $y$?" Depending on the size of the label space, list labeling costs $O(\log^2N)$ for labels in $\{1,\dots,(1+\varepsilon)N\}$ to $\{1,\dots,N\log N\}$ (use @thm-ofm), $\Theta(\log N)$ for labels up to $N^{1+\varepsilon}\dots N^{O(1)}$ (same method with thresholds that tighten geometrically), and $\Theta(1)$ amortised for $2^N$ labels (bisect the label interval, rebuild after about $N$ operations).

:::

::: {#thm-order-maintenance .theorem name="Order maintenance in $O(1)$ (Dietz–Sleator)"}

Order maintenance supports insertion, deletion and precedence queries in $O(1)$ amortised time (worst-case bounds exist as well).

:::

::: {.proof}

1. Partition the list into $\Theta(N/\log N)$ groups of $\Theta(\log N)$ consecutive items. Within a group use list labeling with exponentially large labels ($2^{\log N}=N$ values, which is affordable): $O(1)$ amortised per update inside a group.

2. The groups themselves are kept in a list labelled with the $\Theta(\log N)$ method, in a label space of polynomial size. A group splits or merges only after $\Omega(\log N)$ updates inside it, so the $O(\log N)$ cost of relabelling the group list is $O(1)$ amortised per update.

3. The label of an item is the pair (label of its group, label inside its group), of $O(\log N)$ bits, so two items are compared in $O(1)$ time. (One top-level relabelling changes the labels of many items at once, which is why this beats the table's optimum for plain list labeling.)

:::

::: {#rmk-ofm-1 .remark name="Where it is used"}

Order maintenance linearises the version tree in fully persistent structures (@sec-cs-advanced-data-structures-persistent-data-structures) and the time axis of retroactive structures (@def-retroactive). OFM is the dynamic array under the cache-oblivious B-tree (@thm-co-b-tree).

:::
