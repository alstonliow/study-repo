<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6006s20-1-q3" status="draft"}
The bookmarks split the pages into three blocks: $P_1$ (before $A$), $P_2$ (between $A$ and $B$) and $P_3$ (after $B$). All operations act at the boundaries of the blocks, so we keep each block in an array with free room at both boundaries, like a dynamic array.

*Representation.* One static array $S$ of length $3n+3$ holds $P_1$ at its start, then a gap, then $P_2$, then a gap, then $P_3$ at its end. We store the indices where $P_1$ ends, $P_2$ starts and ends, and $P_3$ starts. *Rebuild* means: allocate $S$ afresh for the current $n$ with gaps of about $n$ empty slots each, and copy the pages, in $O(n)$ time.

- `build(X)`: store the pages in a static array (no bookmarks yet), $O(|X|)$ worst case. `place_mark(i, m)` records the position and, once both bookmarks are placed, rebuilds: $O(n)$ worst case.
- `read_page(i)`: with $n_1=|P_1|$ and $n_2=|P_2|$ (from the stored indices), page $i$ is at $S[i]$ if $i<n_1$, at (start of $P_2$)$+(i-n_1)$ if $i<n_1+n_2$, and at (start of $P_3$)$+(i-n_1-n_2)$ otherwise. $O(1)$ worst case.
- `shift_mark(m, d)`: moving a bookmark by one page moves one page across one gap: copy the last page of the block on one side into the free slot next to the block on the other side and update two indices. The gap sizes do not change. $O(1)$ worst case.
- `move_page(m)`: the page in front of bookmark $A$ is the last page of $P_1$; it moves to just in front of $B$, that is, to the end of $P_2$ (into the gap after $P_2$). The page in front of $B$ is the last page of $P_2$; it moves to just in front of $A$, the end of $P_1$ (into the gap after $P_1$). Each move copies one page, uses one free slot of one gap and frees one slot of another, and updates two indices. If a gap becomes empty, rebuild.

*Analysis.* Between two rebuilds at least about $n$ moves happen (a gap starts with about $n$ free slots and loses at most one per operation), so each rebuild of cost $O(n)$ is paid for by $\Omega(n)$ cheap operations, and `move_page` is $O(1)$ *amortized*. (Since moves do not change $n$, sizes stay within a constant factor between rebuilds.)
:::
