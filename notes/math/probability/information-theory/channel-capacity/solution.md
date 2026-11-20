<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-eecs126hw-4-q5" status="draft"}
(a) After $k$ chunks are recovered, a packet of current degree $d$ is attached to $d$ of the $n-k$ unrecovered chunks, by symmetry a uniformly random $d$-subset. It contains the chunk about to be peeled with probability $\frac{d}{n-k}$, so in expectation $\frac{d\,f_k(d)}{n-k}$ packets of degree $d$ drop to degree $d-1$.

(b) Degree-$d$ packets after the next peeling are the ones that stayed plus the degree-$(d+1)$ ones that dropped:
$$f_{k+1}(d)=f_k(d)-\frac{d\,f_k(d)}{n-k}+\frac{(d+1)f_k(d+1)}{n-k}\quad(d\ge2),\qquad f_{k+1}(1)=\frac{2f_k(2)}{n-k},$$
since the one degree-one packet is used up and new ones come only from degree $2$.

1. $f_{k+1}(1)=1$ forces $f_k(2)=\frac{n-k}{2}$ for all $k$.
2. Suppose $f_k(d)=\frac{n-k}{d(d-1)}$ for all $d\ge2$. Then $\frac{d f_k(d)}{n-k}=\frac1{d-1}$ and $\frac{(d+1)f_k(d+1)}{n-k}=\frac1d$, so the recursion gives $f_{k+1}(d)=\frac{n-k}{d(d-1)}-\frac1{d-1}+\frac1d=\frac{n-k-1}{d(d-1)}$, the same form at $k+1$. Conversely, solving the recursion downward from $f_k(2)$ fixes each $f_k(d)$, so this is the only solution.
3. At $k=0$ the $n$ packets have degrees drawn from $p$, so $np(d)=f_0(d)$: $p(1)=\frac1n$ and $p(d)=\frac{1}{d(d-1)}$ for $d=2,\dots,n$. These sum to $\frac1n+\sum_{d=2}^{n}\bigl(\frac1{d-1}-\frac1d\bigr)=1$.

(c) $E[D]=\frac1n+\sum_{d=2}^{n}\frac{d}{d(d-1)}=\frac1n+H_{n-1}\approx\ln n$, where $H_{n-1}=\sum_{j=1}^{n-1}\frac1j$.
:::

::: {.solution for="prob-peeling-decoder-code" status="draft"}
```{.python}
def peel(n, packets):
    """Peeling decoder. Chunks are numbered 0..n-1 and hold ints. Each packet is
    a pair (indices, value): value is the XOR of the chunks at those indices.
    Return a list of length n with each chunk's value, or None where unknown."""
    chunks = [None] * n
    pending = [[set(ix), v] for ix, v in packets]
    ripple = [p for p in pending if len(p[0]) == 1]
    holding = {}                                  # chunk -> packets that contain it
    for p in pending:
        for i in p[0]:
            holding.setdefault(i, []).append(p)
    while ripple:
        ix, v = ripple.pop()
        if len(ix) != 1:                          # emptied by an earlier peel
            continue
        i = ix.pop()
        if chunks[i] is not None:
            continue
        chunks[i] = v
        for p in holding.get(i, []):              # peel chunk i off every packet
            if i in p[0]:
                p[0].discard(i)
                p[1] ^= v
                if len(p[0]) == 1:
                    ripple.append(p)
    return chunks
```

1. Copy each packet as a mutable pair [set, value], and index the packets by the chunks they contain.
2. The *ripple* is a stack of packets that have one unknown index. Popping one gives a chunk $x_i$ (if not already known); then $x_i$ is XOR-ed out of every packet holding $i$, and any packet left with one index joins the ripple.
3. A popped packet whose set has meanwhile become empty, or whose chunk is already known, is skipped. Each index is removed from each packet at most once, so the total work is proportional to $\sum|I|$.
4. Decoding stops exactly when no packet has one unknown index, as the last test checks. Some chunks can then stay unknown even though the packets determine them, since peeling never combines two packets of degree two or more.
:::
