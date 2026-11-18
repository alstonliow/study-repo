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

::: {.solution for="prob-mit6006s20-1-q4" status="draft"}
(a) `insert_first(x)`: make a node $u$ with item $x$, `u.prev = None`, `u.next = L.head`; if the list was empty set `L.tail = u`, else `L.head.prev = u`; then `L.head = u`. `delete_first()`: let $u$ = `L.head`; set `L.head = u.next`; if that is `None` the list is now empty and `L.tail = None`, else `L.head.prev = None`; return `u.item`. The operations at the tail are symmetric (swap `head`/`tail` and `prev`/`next`). Each changes $O(1)$ pointers.

(b) Let $a$ = `x1.prev` and $b$ = `x2.next`. Link around the segment: if $a$ is `None` set `L.head = b`, else `a.next = b`; if $b$ is `None` set `L.tail = a`, else `b.prev = a`. Make a new list `L2` with `L2.head = x1`, `L2.tail = x2`, and cut its ends: `x1.prev = None`, `x2.next = None`. No traversal is needed, so $O(1)$.

(c) If `L2` is empty, do nothing. Otherwise let $h$, $t$ be its head and tail and $y$ = `x.next`. Set `x.next = h`, `h.prev = x`, `t.next = y`; if $y$ is `None` set `L1.tail = t`, else `y.prev = t`. Finally `L2.head = L2.tail = None`. $O(1)$.

(d) A sketch (the template's node class has fields `item`, `prev`, `next`):

```python
class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = self.tail = None

    def insert_first(self, x):
        u = Doubly_Linked_List_Node(x)
        u.next = self.head
        if self.head is None: self.tail = u
        else: self.head.prev = u
        self.head = u

    def insert_last(self, x):
        u = Doubly_Linked_List_Node(x)
        u.prev = self.tail
        if self.tail is None: self.head = u
        else: self.tail.next = u
        self.tail = u

    def delete_first(self):
        u = self.head
        self.head = u.next
        if self.head is None: self.tail = None
        else: self.head.prev = None
        return u.item

    def delete_last(self):
        u = self.tail
        self.tail = u.prev
        if self.tail is None: self.head = None
        else: self.tail.next = None
        return u.item

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        a, b = x1.prev, x2.next
        if a is None: self.head = b
        else: a.next = b
        if b is None: self.tail = a
        else: b.prev = a
        x1.prev = x2.next = None
        L2.head, L2.tail = x1, x2
        return L2

    def splice(self, x, L2):
        if L2.head is None: return
        h, t, y = L2.head, L2.tail, x.next
        x.next, h.prev, t.next = h, x, y
        if y is None: self.tail = t
        else: y.prev = t
        L2.head = L2.tail = None
```
:::

::: {.solution for="prob-mit6006r-2-q1" status="draft"}
Yes, with two pointers and $O(1)$ extra space (Floyd's "tortoise and hare").

1. Start pointers $p$ and $q$ at the head. Repeat: move $p$ one node and $q$ two nodes, until $p=q$.

2. *They meet.* Once both pointers are on the cycle (of length $c$), the gap from $p$ forward to $q$ shrinks by exactly $1$ each step, so it reaches $0$ within $c$ steps.

3. *Linear time.* Let $\mu$ be the number of nodes before the cycle. $p$ enters the cycle after $\mu$ steps and the pointers meet at most $c$ steps later, so phase 1 takes at most $\mu+c=n$ steps.

4. From the meeting node $v$, walk $p$ forward and count the steps until it returns to $v$; the count is $c$. This takes $c\le n$ further steps.

Only two pointers and a counter are stored, so the extra space is $O(1)$ and the time is $O(n)$.
:::
