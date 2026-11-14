<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-counting-05" status="draft"}
Let $C$, $S$, $W$ be the sets of catalogue entries containing CSIRAC,
SILLIAC and WREDAC. A Basic Search for several terms returns the entries
containing all of them, so it gives the sizes of intersections directly.

1. Run seven searches: the three single terms, the three pairs, and all
   three terms together.

2. By inclusion–exclusion,
   $$|C\cup S\cup W| = |C|+|S|+|W| - |C\cap S| - |C\cap W| - |S\cap W| + |C\cap S\cap W|.$$

3. Substitute the seven counts.

<!-- TODO: the numbers depend on the date of the search. Owner to run the
     searches and fill them in. -->
:::

::: {.solution for="prob-counting-06" status="draft"}
(a) Let $A_3, A_5, A_7$ be the multiples of $3$, $5$, $7$ in
    $\{1,\dots,100\}$. A number is in $A_3\cap A_5$ when it is a multiple of
    $15$, and so on:
    $$|A_3| = 33,\ |A_5| = 20,\ |A_7| = 14,$$
    $$|A_3\cap A_5| = 6,\ |A_3\cap A_7| = 4,\ |A_5\cap A_7| = 2,\ |A_3\cap A_5\cap A_7| = 0.$$
    So
    $$|A_3\cup A_5\cup A_7| = 33+20+14 - 6-4-2 + 0 = 55,$$
    and the answer is $100 - 55 = 45$.

(b) Use periodicity. Whether $n$ is a multiple of $3$, $5$ or $7$ depends
    only on $n\bmod 105$. In each block of $105$ consecutive integers the
    count is
    $$105\cdot\tfrac23\cdot\tfrac45\cdot\tfrac67 = 48.$$
    Among $101,\dots,105$, the numbers $101, 103, 104$ are not multiples
    of $3$, $5$ or $7$. So the count up to $100$ is $48 - 3 = 45$.
:::

::: {.solution for="prob-counting-07" status="draft"}
Let $F$ be all functions from the $6$-set to $\{1,2,3,4\}$, and let $M_i$
be those that miss the value $i$. A surjection misses nothing.

1. $|F| = 4^6$. Missing a given set of $k$ values leaves $4-k$ possible
   values, so a $k$-fold intersection of the $M_i$ has $(4-k)^6$ functions.

2. By inclusion–exclusion,
   $$\#\text{surjections} = 4^6 - \binom41 3^6 + \binom42 2^6 - \binom43 1^6 + \binom44 0^6.$$

3. Evaluating:
   $$4096 - 4\cdot729 + 6\cdot64 - 4\cdot1 + 0 = 4096 - 2916 + 384 - 4 = 1560.$$
:::
