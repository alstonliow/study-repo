<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6042f10-2-q3" status="draft"}
The clue is *perimeter*. Think of each student as a unit square, and let the perimeter of the infected set be the number of square sides that separate an infected square from a non-infected square or from the outside.

1. *The perimeter never increases.* Within one time step, add the newly infected squares one at a time. Each has at least two infected neighbours already (its neighbours infected at the previous step stay infected). Adding a square removes from the perimeter the sides it shares with infected neighbours (at least $2$) and adds its other sides (at most $2$). So the perimeter does not increase.

2. By induction on the number of steps (@thm-invariant-principle), the perimeter is always at most its initial value, which is at most $4$ per infected square: less than $4n$ if fewer than $n$ students start infected.

3. The whole class, the full $n\times n$ square, has perimeter exactly $4n$. So it can never be completely infected.
:::

::: {.solution for="prob-mit6042f10-2-q6" status="draft"}
(a) No. A row move slides a tile left or right into the blank in the same row. The order lists only tiles, read row by row, so the moved tile keeps its place relative to all others.

(b) Exactly $3$. A column move moves a tile up or down one row, into the blank. In the reading order it jumps over the tiles between its old and new positions: the remaining $3$ squares of the row it leaves (on one side) and of the row it enters (on the other side), $3$ tiles in all since the blank is not a tile. Its order relative to these $3$ tiles changes and nothing else changes.

(c) None: by (a) the order, and so the set of inversions, is unchanged.

(d) It changes the parity. By (b) exactly $3$ pairs swap their relative order, and each swap turns an inversion into a non-inversion or the reverse, changing the count by $\pm1$. Three changes of $\pm1$ change the count by an odd number.

(e) Use the invariant principle (@thm-invariant-principle) with $P$ = "the number of inversions and the row of the blank have different parities".

1. *Start:* the only inversion is O before N, so there is $1$ inversion, and the blank is in row $4$: odd versus even.

2. *Row moves* change neither the inversions (c) nor the blank's row.

3. *Column moves* change the parity of the number of inversions (d) and move the blank one row up or down, changing the parity of its row. Both parities flip, so they stay different.

(f) The target board has $0$ inversions (even) and the blank in row $4$ (even): the parities are equal. By the lemma it is not reachable.
:::

::: {.solution for="prob-mit6042f10-2-q7" status="draft"}
Let $z_t$ and $b_t$ be the numbers of Z-lings and B-lings in generation $t$. We prove the stronger statement $z_t\le b_t$ for all $t$, which gives $z_t\le b_t\le2b_t$.

1. *Base case:* $z_1=200\le800=b_1$.

2. *Step:* suppose $z\le b$ in some generation. Then $z$ Z-B pairs form, and the $b-z$ remaining B-lings form $m=\lfloor\frac{b-z}2\rfloor$ B-B pairs (one B-ling dies if $b-z$ is odd, which happens exactly when $z+b$ is odd).

3. The next generation has $z'=z+m$ Z-lings ($z$ from the mixed pairs, $m$ from the B-B pairs) and $b'=z+2m$ B-lings. Since $m\ge0$, $z'=z+m\le z+2m=b'$.

The weaker hypothesis $z\le2b$ is not preserved by itself: with $z=2b$, the next generation would have $z'=b+3\lfloor\frac b2\rfloor$ Z-lings and only $b$ B-lings. That is why the stronger invariant is needed.
:::
