<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6046s15-5-q1" status="draft"}
(a) Assume $k>x.key$ (the other case is the mirror image, moving left via predecessor pointers or by symmetry). Write $v.up$ for the copy of $v$'s key one level up (if any) and $v.next$ for the next node on $v$'s level.

```text
FINGER-SEARCH(x, k):
    v = x
    # climb: go up when possible, otherwise go right, while not passing k
    while True:
        if v.up exists and v.up.next.key <= k:   v = v.up
        elif v.next.key <= k:                    v = v.next
        else: break
    # descend: ordinary skip-list search from v
    while v.key != k or v is not at level 0:
        if v.next.key <= k: v = v.next
        else: v = v.down
    return v
```

*Analysis.* The climb never passes $k$, so it stays among the $m$ keys between $x$ and $k$. Reading the climb backwards is like the backward analysis of @thm-skip-list-search restricted to these $m$ keys: each step is "up" with probability $\frac12$. Among $m$ keys, the probability that some key reaches level $(\alpha+1)\lg m$ is at most $m\cdot m^{-(\alpha+1)}$, so with probability $1-m^{-\alpha}$ the climb reaches at most level $O(\lg m)$, and by the coin-tossing claim (Chernoff bound) it takes $O(\lg m)$ steps with probability $1-m^{-\alpha}$. The descent from a node at height $O(\lg m)$ towards a key at most $m$ ranks away is a search in a skip list on those $m$ keys, also $O(\lg m)$ steps w.h.p. in $m$.

(b) Store with every forward pointer $v.next$ at level $\ell\ge1$ its *span*: the number of level-0 nodes it jumps over (the difference in rank between $v.next$ and $v$); at level $0$ every span is $1$. A search keeps the visited path, which has $O(\lg n)$ nodes w.h.p. *Insert* of a key: every pointer on the search path that jumps over the new key gets span $+1$; when the key is promoted to level $\ell$, the pointer at level $\ell$ that it splits is divided into two spans, computed from ranks accumulated along the search path. *Delete* reverses this. Each level costs $O(1)$ extra, so the bounds stay $O(\lg n)$ w.h.p.

(c) Same climb-then-descend as (a), steering by accumulated span instead of keys: keep $s$, the rank offset from $x$ reached so far.

```text
RANK-SEARCH(x, r):
    v = x; s = 0
    while True:                                    # climb
        if v.up exists and s + span(v.up.next) <= r:   v = v.up
        elif s + span(v.next) <= r:   s = s + span(v.next); v = v.next
        else: break
    while s < r or v is not at level 0:            # descend
        if s + span(v.next) <= r:   s = s + span(v.next); v = v.next
        else: v = v.down
    return v
```

The path is the one FINGER-SEARCH would take to the key of rank $\mathrm{rank}(x)+r$, so the analysis of (a) with $m=r+1$ applies: $O(\lg m)$ steps with probability at least $1-m^{-\alpha}$.
:::
