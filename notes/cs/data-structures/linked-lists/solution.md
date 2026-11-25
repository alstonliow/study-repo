<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

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
