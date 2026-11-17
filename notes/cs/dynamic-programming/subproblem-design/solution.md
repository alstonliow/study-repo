<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6006s20-7-q2" status="draft"}
Sort the tigers by decreasing age, $T_1,\dots,T_n$ (oldest first), and the cages by increasing distance, $K_1,\dots,K_{n^2}$, in $O(n^2\log n)$ time. An assignment favours older tigers exactly when the cages of $T_1,T_2,\dots,T_n$ appear in increasing order of index: it chooses $n$ of the cages in order. Let $\mathrm{dis}(i,j)=\max(0,s_i-c_j)$ for tiger $T_i$ in cage $K_j$.

1. *Subproblems:* $x(i,j)$, the least total discomfort for tigers $T_i,\dots,T_n$ using only cages $K_j,\dots,K_{n^2}$, for $1\le i\le n+1$, $1\le j\le n^2+1$.
2. *Relation:* cage $K_j$ is either unused or taken by $T_i$ (the oldest remaining tiger must get the closest cage used): $x(i,j)=\min\{x(i,j+1),\ \mathrm{dis}(i,j)+x(i+1,j+1)\}$.
3. *Order:* decreasing $j$ (then any $i$); dependencies have larger $j$.
4. *Base:* $x(n+1,j)=0$ (no tigers left); $x(i,n^2+1)=\infty$ for $i\le n$ (tigers but no cages).
5. *Original:* $x(1,1)$; parent pointers give the assignment.
6. *Time:* $(n+1)(n^2+1)$ subproblems with $O(1)$ work: $O(n^3)$, plus the sorting.
:::

::: {.solution for="prob-mit6006s20-7-q4" status="draft"}
*Structure.* Index slices mod $2n$. The first move eats a half pizza, $n$ consecutive slices. Afterwards the uneaten slices always form an arc of $L\le n$ consecutive slices $i,\dots,i+L-1$. A proper cut through such an arc at a boundary $\alpha_k$ inside it eats either the part after $\alpha_k$ (choosing $\alpha_k$) or the part before it (choosing the opposite angle $\alpha_{k+n}$), because the arc fits in a half pizza. So a move eats a nonempty proper prefix or suffix of the arc, and any of these can be chosen; angles outside the arc are not proper.

1. *Subproblems:* $x(i,L,p)$, the most Liza can guarantee when the uneaten slices are the arc of length $L$ starting at $i$ and $p\in\{\text{Liza},\text{Lie}\}$ chooses next; $0\le i<2n$, $1\le L\le n$.
2. *Relation:* with $\sigma(i,m)$ the total tastiness of the $m$ slices starting at $i$, the chooser eats a prefix of length $m$ (leaving the arc $(i+m,L-m)$) or a suffix of length $m$ (leaving $(i,L-m)$), for $1\le m<L$:
   $$x(i,L,\text{Liza})=\max_m\max\{\sigma(i,m)+x(i+m,L-m,\text{Lie}),\ \sigma(i+L-m,m)+x(i,L-m,\text{Lie})\},$$
   $$x(i,L,\text{Lie})=\min_m\min\{x(i+m,L-m,\text{Liza}),\ x(i,L-m,\text{Liza})\},$$
   since Liza gets nothing from Lie's moves, and Lie may play to minimise Liza's total.
3. *Order:* increasing $L$.
4. *Base:* $x(i,1,\text{Liza})=t_i$ and $x(i,1,\text{Lie})=0$.
5. *Original:* $\max_{0\le i<2n}\{\sigma(i,n)+x(i+n,n,\text{Lie})\}$ (Liza's first cut eats the half starting at $i$).
6. *Time:* precompute prefix sums so that each $\sigma$ costs $O(1)$. There are $O(n^2)$ subproblems with $O(n)$ work each: $O(n^3)$.

This was checked against a brute-force game search on small random pizzas.
:::

::: {.solution for="prob-mit6006s20-7-q5" status="draft"}
(a) "Doesn't skip days" means that consecutive chosen prices lie on the same day or on adjacent days. For one company with prices $p_0,\dots,p_{nk-1}$, where price $q$ is on day $\lfloor q/k\rfloor$, this is a longest increasing subsequence problem with a constraint (as in @exm-lis):

1. *Subproblems:* $x(q)$, the length of a longest valid decreasing subsequence that *starts* with $p_q$, for $0\le q<nk$.
2. *Relation:* guess the next price: $x(q)=\max\bigl(\{1+x(r):q<r,\ \lfloor r/k\rfloor\le\lfloor q/k\rfloor+1,\ p_r<p_q\}\cup\{1\}\bigr)$.
3. *Order:* decreasing $q$. 4. *Base:* none needed (the option $1$).
5. *Original:* the shorting value is $\max_qx(q)$; parent pointers give the subsequence. Do this for every company and return the best.
6. *Time:* each $q$ looks at the at most $2k$ later prices of its own day and the next, so $O(nk\cdot k)$ per company and $O(snk^2)$ in all.

(b)

```python
def short_company(C, P, n, k):
    best_c, best_S = C[0], []
    for c, prices in zip(C, P):
        N = n * k
        x = [1] * N                    # x[i]: longest valid run starting at i
        nxt = [None] * N               # parent pointer to the next price
        for i in reversed(range(N)):
            end = min(N, (i // k + 2) * k)       # same day or the next day
            for j in range(i + 1, end):
                if prices[j] < prices[i] and 1 + x[j] > x[i]:
                    x[i], nxt[i] = 1 + x[j], j
        i = max(range(N), key=lambda m: x[m]) if N else None
        if i is not None and x[i] > len(best_S):
            S = []
            while i is not None:
                S.append(prices[i])
                i = nxt[i]
            best_c, best_S = c, S
    return (best_c, best_S)
```

It was checked against brute force over all subsequences on small random inputs.
:::
