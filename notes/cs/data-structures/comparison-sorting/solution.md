<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6006s20-2-q2" status="draft"}
(a) *Selection sort.* Writes are expensive and reads cheap. Selection sort makes $\Theta(n^2)$ reads but only $O(n)$ swaps, that is $O(n)$ calls of `set_at`, costing $O(n\cdot n\log n)$; total $\Theta(n^2\log n)$. Insertion sort may do $\Theta(n^2)$ swaps, costing $\Theta(n^3\log n)$, and merge sort is not in place (and writes $\Theta(n\log n)$ times anyway, $\Theta(n^2\log^2n)$).

(b) *Merge sort.* Now comparisons are expensive and moving a pointer is cheap. Merge sort makes $O(n\log n)$ comparisons, $O(n\log^2n)$ time in total; selection and insertion sort make $\Theta(n^2)$ comparisons in the worst case, $\Theta(n^2\log n)$.

(c) *Insertion sort.* Each adjacent swap creates at most one inversion, so $A$ has at most $\log\log n$ inversions. Insertion sort does $O(n)$ comparisons plus one swap per inversion (@sec-cs-data-structures-comparison-sorting), so it runs in $O(n+\log\log n)=O(n)$ time, while merge sort takes $\Theta(n\log n)$ and selection sort $\Theta(n^2)$ regardless of the input.
:::

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

::: {.solution for="prob-mit6006s20-2-q5" status="draft"}
(a) A schedule describes a step function: the number of rooms booked at each time. The rooms needed for $R_1\cup R_2$ are the sum of the two step functions. Merge the sorted lists of boundary times of $B_1$ and $B_2$ with two fingers, as in merge sort, into one sorted list $T$ of $O(n)$ times. Between consecutive times $a<b$ in $T$ both functions are constant; advance a finger in each schedule to read their values at $a$, and if the sum $k$ is positive output $(k,a,b)$, joining it with the previous booking when that one ends at $a$ with the same $k$. The result has disjoint, increasing bookings with different counts on adjacent ones, and books exactly the sum, so it is the unique satisfying schedule. Each time and each booking is handled $O(1)$ times: $O(n)$.

(b) Divide and conquer, like merge sort: a single request $(s,t)$ has schedule $((1,s,t))$; otherwise split $R$ into halves, solve each recursively and merge the two schedules with (a). A schedule for $m$ requests has at most $2m-1$ bookings (it changes only at the $2m$ endpoints), so merging costs $O(m)$ and $T(n)=2T(n/2)+O(n)=O(n\log n)$.

(c)

```python
def merge_schedules(B1, B2):
    # all boundary times of both schedules, merged in sorted order (two fingers)
    def times(B):
        T = []
        for (k, s, t) in B:
            if not T or T[-1] != s: T.append(s)
            T.append(t)
        return T
    T1, T2, T = times(B1), times(B2), []
    i = j = 0
    while i < len(T1) or j < len(T2):
        if j == len(T2) or (i < len(T1) and T1[i] <= T2[j]):
            x = T1[i]; i += 1
        else:
            x = T2[j]; j += 1
        if not T or T[-1] != x: T.append(x)
    # rooms booked on [a, b) for consecutive boundary times a < b
    B, p, q = [], 0, 0
    for a, b in zip(T, T[1:]):
        while p < len(B1) and B1[p][2] <= a: p += 1
        while q < len(B2) and B2[q][2] <= a: q += 1
        k = 0
        if p < len(B1) and B1[p][1] <= a: k += B1[p][0]
        if q < len(B2) and B2[q][1] <= a: k += B2[q][0]
        if k == 0: continue
        if B and B[-1][2] == a and B[-1][0] == k:
            B[-1] = (k, B[-1][1], b)          # same count as the adjacent booking
        else:
            B.append((k, a, b))
    return B

def satisfying_booking(R):
    R = list(R)
    def solve(lo, hi):
        if hi - lo == 1:
            s, t = R[lo]
            return [(1, s, t)]
        mid = (lo + hi) // 2
        return merge_schedules(solve(lo, mid), solve(mid, hi))
    return tuple(solve(0, len(R))) if R else ()
```

On the example it returns exactly the schedule $B$ given in the statement.
:::
