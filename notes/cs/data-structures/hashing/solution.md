<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6006s20-3-q1" status="draft"}
(a) The hashes are $h(47)=5$, $h(61)=5$, $h(36)=0$, $h(52)=6$, $h(56)=4$, $h(33)=5$, $h(92)=0$. So

| slot | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| chain | 36 → 92 | | | | 56 | 47 → 61 → 33 | 52 |

(b) Seven keys and seven slots, so no collision means the hashes are exactly $0,\dots,6$ in some order. For $c\le6$ the inner value $(10k+4)\bmod c$ takes at most $6$ values, so a collision is unavoidable. Checking $c=7,\dots,12$ directly, each gives a collision (for example $c=12$ sends $56$ and $92$ both to $0$). For $c=13$ the values $(10k+4)\bmod13$ are $6,3,0,4,5,9,1$, whose remainders mod $7$ are $6,3,0,4,5,2,1$, all different. So the answer is $c=13$.
:::

::: {.solution for="prob-mit6006s20-3-q2" status="draft"}
(a) *Guaranteed.* Choose $k_1\equiv k_2\pmod n$, for example $k_1=1$ and $k_2=n+1$ (both less than $u$). Then $ak_1+b\equiv ak_2+b\pmod n$ for every $a,b$, so every function in $\mathcal H$ puts them in the same room.

(b) *Guaranteed.* Choose $k_1,k_2$ with $\lfloor k_1n/u\rfloor=\lfloor k_2n/u\rfloor$, for example $k_1=1$ and $k_2=2$: since $u>2n$, both floors are $0$. Then $h_a(k_1)=h_a(k_2)$ for every $a$.

(c) *Not possible.* This family is universal (@thm-universal-hash-family), so for any $k_1\ne k_2$ the probability of a collision is at most $\frac1n$. In fact the proof shows more: for every pair of distinct keys, the pair $(r,s)=((ak_1+b)\bmod p,(ak_2+b)\bmod p)$ is uniform over the $p(p-1)$ pairs with $r\ne s$, *whatever the keys are*. So every choice of IDs gives the same probability,
$$\frac{\#\{(r,s):r\ne s,\ r\equiv s\pmod n\}}{p(p-1)}=\frac{\sum_jc_j(c_j-1)}{p(p-1)}\le\frac1n,$$
where $c_j$ is the number of $r\in\{0,\dots,p-1\}$ with $r\equiv j\pmod n$. The best they can achieve is this value, which is at most (and close to) $\frac1n$.
:::

::: {.solution for="prob-mit6006s20-3-q5" status="draft"}
Two strings are anagrams exactly when they have the same *letter-count vector*: the $26$ numbers of `a`s, `b`s, …, `z`s.

(a) Slide a window of length $k$ along $A$, keeping its count vector: moving the window one step adds one letter and removes one, $O(1)$ updates. For each of the $|A|-k+1$ windows, increment the entry for its count vector (a tuple of $26$ integers, so $O(1)$ words) in a hash table that maps count vectors to numbers of windows. This takes $O(|A|)$ expected time. To answer a query $B$, compute its count vector in $O(k)$ and look it up (answer $0$ if absent), $O(1)$ expected.

(b) Build the structure of (a) for $A=T$ once, in $O(|T|)$, then answer the $n$ queries in $O(k)$ each: $O(|T|+nk)$ expected time.

(c)

```python
def count_anagram_substrings(T, S):
    if not S:
        return ()
    k = len(S[0])
    counts = [0] * 26                  # letter counts of the current window
    table = {}                         # count tuple -> number of windows
    for i, c in enumerate(T):
        counts[ord(c) - ord('a')] += 1
        if i >= k:                     # drop the letter that left the window
            counts[ord(T[i - k]) - ord('a')] -= 1
        if i >= k - 1:
            key = tuple(counts)
            table[key] = table.get(key, 0) + 1
    A = []
    for B in S:
        b = [0] * 26
        for c in B:
            b[ord(c) - ord('a')] += 1
        A.append(table.get(tuple(b), 0))
    return tuple(A)
```

On the example it returns `(3,)`.
:::
