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

::: {.solution for="prob-mit6006r-15-q1" status="draft"}
*Subproblems.* $x(i)$ = the maximum number of rounds the player can still win when the next round starts with card $c_i$, for $1\le i\le n+1$. A round is played only when at least $5$ cards remain.

*Win test.* For a round starting at $i$ and the choice $h\in\{0,1\}$ (hit or not), let
$$w(i,h)=\begin{cases}1 & \text{if } c_{i+2}+c_{i+3}+h\,c_{i+4}\le 21 \text{ and } c_{i+2}+c_{i+3}+h\,c_{i+4}>c_i+c_{i+1},\\ 0 & \text{otherwise.}\end{cases}$$

*Relation.* If $n-i+1<5$, then $x(i)=0$. Otherwise
$$x(i)=\max\{\,w(i,0)+x(i+4),\; w(i,1)+x(i+5)\,\},$$
With at least $5$ cards left there is always a card to hit, and $i+5\le n+1$.

*Order and answer.* $x(i)$ depends only on larger indices, so compute $i=n+1,n,\dots,1$; the answer is $x(1)$. Store the maximizing choice to recover the hits.

*Time.* $O(n)$ subproblems, $O(1)$ work each: $O(n)$.
:::

::: {.solution for="prob-mit6006r-15-q2" status="draft"}
*Subproblems.* $x(i)$ = the minimum total badness for setting the suffix of words $i,\dots,n$, for $1\le i\le n+1$.

*Relation.* The first line of the suffix holds words $i,\dots,j-1$ for some $j>i$:
$$x(i)=\min_{i<j\le n+1}\bigl\{\,b(i,j-1)+x(j)\,\bigr\}.$$

*Base.* $x(n+1)=0$.

*Order and answer.* Compute $i=n+1,\dots,1$; the answer is $x(1)$. Store the minimizing $j$ to recover the line breaks.

*Time.* With prefix sums $P_k=w_1+\dots+w_k$ (computed once in $O(n)$), $w_i+\dots+w_j=P_j-P_{i-1}$, so each $b(i,j)$ costs $O(1)$. There are $O(n)$ subproblems with $O(n)$ choices each: $O(n^2)$.
:::

::: {.solution for="prob-mit6046r-5-q1" status="draft"}
1. *Order.* Sort the blocks by length, then width, both non-increasing: $O(n\log n)$. In any valid tower each block has $l$ and $w$ no larger than the block below it, so reading the tower from bottom to top gives the blocks in an order consistent with this sorted order (blocks with equal bases can be swapped freely). So we may assume a tower uses the blocks in increasing sorted index from bottom to top.

2. *Subproblems.* $H[i]$ = the height of the tallest tower whose *top* block is $B_i$.

3. *Relation.* The block under $B_i$, if any, is some earlier $B_j$ with a larger-or-equal base:
$$H[i]=h_i+\max\Bigl(\{0\}\cup\{H[j]: j<i,\ l_i\le l_j,\ w_i\le w_j\}\Bigr).$$

4. *Answer.* $\max_i H[i]$, computed for $i=1,\dots,n$ in order.

*Time.* $O(n)$ choices for each of $n$ subproblems: $O(n^2)$.
:::

::: {.solution for="prob-mit6006-16-q1" status="draft"}
1. *What each subproblem asks.* $x(i)=1+\max\{x(j):j>i,\ A[j]>A[i]\}$ (or $1$ if no such $j$). This is a range-maximum query over the already solved suffix, restricted to keys greater than $A[i]$.

2. *Data structure.* Keep an AVL tree storing one node per solved index $j$, keyed by $(A[j],j)$. Augment every node with $m=$ the largest $x(j)$ in its subtree. The augmentation depends only on the node and its two children, so it is maintained through insertions and rotations in $O(1)$ per changed node.

3. *Query.* To find $\max\{x(j):A[j]>a\}$, walk from the root down the search path for $a$. Whenever the walk goes left from a node with key greater than $a$, that node and its whole right subtree have keys $>a$: take its $x$ and its right child's $m$. Taking the maximum of these $O(\log|A|)$ candidates answers the query in $O(\log|A|)$.

4. *Algorithm.* For $i=|A|-1$ down to $0$: query with $a=A[i]$, set $x(i)=1+\text{answer}$ (or $1$ if no key is larger), and insert $(A[i],i)$ with value $x(i)$. Record the index that achieved the maximum as the parent pointer.

5. *Time.* $|A|$ subproblems with one query and one insertion each: $O(|A|\log|A|)$. The answer is still $\max_ix(i)$.
:::

::: {.solution for="prob-mit6006-16-q2" status="draft"}
1. *Subproblems for the sums.* $S(i,j)=\sum_{k=i}^jv_k$ for $0\le i\le j<n$.

2. *Relation.* $S(i,j)=S(i,j-1)+v_j$, with base $S(i,i)=v_i$. Order: increasing $j-i$ (or, for each $i$, increasing $j$).

3. *Cost of the sums.* $\Theta(n^2)$ subproblems, $O(1)$ work each: $\Theta(n^2)$.

4. *Game DP.* With $S$ stored in a table, each $x(i,j)=\max\{S(i,j)-x(i+1,j),\ S(i,j)-x(i,j-1)\}$ takes $O(1)$. So all $\Theta(n^2)$ subproblems take $\Theta(n^2)$ time, and so does the whole algorithm.
:::
