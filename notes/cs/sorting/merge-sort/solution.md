<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

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
