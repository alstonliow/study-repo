<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6046s15-2-q2" status="draft"}
(Minimum degree $t$: non-root nodes have between $t-1$ and $2t-1$ keys; the root has at least $1$.)

(a) Make a new root holding only $k$, with children the roots of $T_1$ and $T_2$. All leaves are at depth $h_1+1$, keys are in order, and the old roots, now non-root nodes, may have too few keys only if they had fewer than $t-1$; in that case fix that child as in (b) by borrowing from or merging with its sibling through $k$. Constant time, since $t$ is constant.

(b) Append $k$ as the last key of $T_1$'s root and the root of $T_2$ as its last child; leaves stay at one depth because $T_2$ is one level lower. Two local repairs, each $O(t)=O(1)$: if the new child (the old root of $T_2$) has fewer than $t-1$ keys, borrow keys from its left sibling through $k$, or merge with it if the sibling has exactly $t-1$ keys; if the root of $T_1$ now has $2t$ keys, split it and create a new root.

(c) Store at each node the height $x.h$ of its subtree (leaves $0$). Heights change only when the tree gains or loses a level: a root split creates a new root with height one more than its children, and when the root becomes empty after a merge, its only child becomes the root and keeps its height. Splits and merges below the root produce nodes at the same height as before. So every update sets $O(1)$ height fields per structural change, and all operations keep their running times.

(d) Assume $h_1\ge h_2$ (the other case is symmetric, along the leftmost spine of $T_2$). Walk down the rightmost path of $T_1$ for $h_1-h_2-1$ steps, to the node $x$ of height $h_2+1$, using the stored heights. Attach $k$ and the root of $T_2$ to $x$ as in (b). The fix-up may split $x$, which adds a key to its parent, which may split in turn, and so on up the path: at most $h_1-h_2+1$ splits, each $O(1)$. Total $O(h_1-h_2+1)$; if $h_1=h_2$, use (a).
:::
