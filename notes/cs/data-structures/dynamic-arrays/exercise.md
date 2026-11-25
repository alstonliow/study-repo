::: {.problem #prob-mit6006s20-1-q3 origin="external" source="mit6006s20-1-q3"}
**Binder Bookmarks**

Sisa Limpson is a very organized second grade student who keeps all of her course notes on individual pages stored in a three-ring binder. If she has $n$ pages of notes in her binder, the first page is at index $0$ and the last page is at index $n-1$. While studying, Sisa often reorders pages of her notes. To help her reorganize, she has two bookmarks, $A$ and $B$, which help her keep track of locations in the binder.

Describe a database to keep track of pages in Sisa's binder, supporting the following operations, where $n$ is the number of pages in the binder at the time of the operation. Assume that both bookmarks will be placed in the binder before any shift or move operation can occur, and that bookmark $A$ will always be at a lower index than $B$. For each operation, state whether your running time is worst-case or amortized.

| operation | specification |
|---|---|
| `build(X)` | Initialize database with pages from iterator $X$ in $O(|X|)$ time. |
| `place_mark(i, m)` | Place bookmark $m\in\{A,B\}$ between the page at index $i$ and the page at index $i+1$ in $O(n)$ time. |
| `read_page(i)` | Return the page at index $i$ in $O(1)$ time. |
| `shift_mark(m, d)` | Take the bookmark $m\in\{A,B\}$, currently in front of the page at index $i$, and move it in front of the page at index $i+d$ for $d\in\{-1,1\}$ in $O(1)$ time. |
| `move_page(m)` | Take the page currently in front of bookmark $m\in\{A,B\}$, and move it in front of the other bookmark in $O(1)$ time. |
:::
