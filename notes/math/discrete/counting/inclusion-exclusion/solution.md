<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-counting-05"}
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

::: {.solution for="prob-counting-06"}
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

::: {.solution for="prob-counting-07"}
Let $F$ be all functions from the $6$-set to $\{1,2,3,4\}$, and let $M_i$
be those that miss the value $i$. A surjection misses nothing.

1. $|F| = 4^6$. Missing a given set of $k$ values leaves $4-k$ possible
   values, so a $k$-fold intersection of the $M_i$ has $(4-k)^6$ functions.

2. By inclusion–exclusion,
   $$\#\text{surjections} = 4^6 - \binom41 3^6 + \binom42 2^6 - \binom43 1^6 + \binom44 0^6.$$

3. Evaluating:
   $$4096 - 4\cdot729 + 6\cdot64 - 4\cdot1 + 0 = 4096 - 2916 + 384 - 4 = 1560.$$
:::

::: {.solution for="prob-cs70-10-q3"}
<!-- TODO: solution -->
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-6-q7" status="draft"}
Groups are unlabelled.

(a) The group containing $1$, together with any subset of the other $n-1$ elements, determines the division; the other group must be non-empty, so $g(n)=2^{n-1}-1$.

(b) Look at element $n$. Either it forms a group alone, and the rest are split into $2$ groups: $g(n-1)$ ways; or it joins one of the $3$ groups of a division of $\{1,\dots,n-1\}$ into $3$ groups: $3f(n-1)$ ways. So
$$f(n)=3f(n-1)+g(n-1),\qquad f(3)=1,$$
and one checks by induction that $f(n)=\frac{3^{n-1}-2^n+1}2$ (true for $n=3$; and $3\cdot\frac{3^{n-2}-2^{n-1}+1}2+2^{n-2}-1=\frac{3^{n-1}-2^n+1}2$).

(c) A surjection $\{1,\dots,7\}\to\{1,2,3\}$ is a division into $3$ non-empty groups (the preimages) together with a labelling of the groups by $1,2,3$: $3!\,f(7)=6\cdot301=1806$. Check by inclusion–exclusion (@thm-inclusion-exclusion): $3^7-3\cdot2^7+3\cdot1^7=2187-384+3=1806$.
:::

::: {.solution for="prob-cs70hw-7-q1" status="draft"}
We take strings of length $5$, as the official solution does.

1. Each of the $5$ positions has $3$ choices: $3^5=243$ strings.

2. Let $E_A$ be the set of strings with no $A$, and similarly $E_B$, $E_C$. Then $|E_A|=2^5$, $|E_A\cap E_B|=1^5$ (all $C$), and $E_A\cap E_B\cap E_C=\emptyset$. By inclusion–exclusion (@thm-inclusion-exclusion),
   $$|E_A\cup E_B\cup E_C|=3\cdot32-3\cdot1+0=93.$$

3. So $243-93=150$ strings contain each letter at least once. (For length $n$: $3^n-3\cdot2^n+3$.)
:::

::: {.solution for="prob-mit6042f10-9-q2" status="draft"}
The passwords are the $10!$ orderings of the ten digits. Let $A_1,A_2,A_3$ be the orderings containing $18062$, $6042$, $35876$.

1. Treating a forbidden string of $k$ digits as one symbol leaves $11-k$ symbols: $|A_1|=6!=720$, $|A_2|=7!=5040$, $|A_3|=6!=720$.

2. $A_1\cap A_2=\emptyset$: in $18062$ the $6$ is followed by $2$, in $6042$ by $0$, and each digit occurs once. $A_1\cap A_3=\emptyset$: the $8$ would be followed by $0$ and by $7$.

3. $A_2\cap A_3$: the strings overlap only as $35876042$ (the $6$ ending $35876$ starts $6042$), an $8$-digit block, so $|A_2\cap A_3|=3!=6$. The triple intersection is empty.

4. By inclusion–exclusion (@thm-inclusion-exclusion), $|A_1\cup A_2\cup A_3|=720+5040+720-6=6474$, and the answer is $10!-6474=3\,622\,326$ (checked by computer).
:::

::: {.solution for="prob-mit18065ps-19-q3" status="draft"}
By inclusion–exclusion, subtract those counted twice, the multiples of $21$ (since $3$ and $7$ are coprime): $\frac13+\frac17-\frac1{21}=\frac{7+3-1}{21}=\frac9{21}=\frac37$. (Here "fraction" means the limiting proportion among $1,\dots,N$ as $N\to\infty$.)
:::
