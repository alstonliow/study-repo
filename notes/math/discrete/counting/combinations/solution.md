<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-counting-04" status="draft"}
(a) Swanston is three streets east of William, and La Trobe is four streets
    north of Flinders. A route that always moves away from the start is a
    sequence of $3$ moves west (W) and $4$ moves north (N) in some order. It
    is fixed by choosing which $3$ of the $7$ moves are W:
    $$\binom73 = \frac{7\cdot6\cdot5}{3!} = 35.$$

(b) Russell is the next street east of Swanston, and Flinders is the
    southernmost street. So the first move must be N or W, and since we
    never turn back, every move is N or W. Each of the $4$ moves is a free
    choice, so there are $2^4 = 16$ routes.

    | destination | moves | routes |
    |---|---|---|
    | Swanston / La Trobe | 4N | $\binom40 = 1$ |
    | Elizabeth / Lonsdale | 3N, 1W | $\binom41 = 4$ |
    | Queen / Bourke | 2N, 2W | $\binom42 = 6$ |
    | William / Collins | 1N, 3W | $\binom43 = 4$ |
    | King / Flinders | 4W | $\binom44 = 1$ |

    The numbers are row $4$ of Pascal's triangle, and they add up to $2^4$:
    $$\sum_{k=0}^4\binom4k = 2^4.$$

(c) From Flinders/Spencer to La Trobe/Spring is $8$ blocks east and $4$
    north, $12$ moves in all:
    $$\binom{12}4 = \frac{12\cdot11\cdot10\cdot9}{4!} = 495.$$
:::

::: {.solution for="prob-counting-08" status="draft"}
An $n$-digit number has no leading $0$. Choosing the *set* (or multiset) of
digits fixes the number, because the order is forced.

(a) Strictly ascending: $0$ cannot occur, because it would have to come first.
    Choose $n$ distinct digits from $\{1,\dots,9\}$:
    $$\binom9n.$$

(b) Strictly descending: choose $n$ distinct digits from $\{0,\dots,9\}$.
    A $0$ can only come last, so the leading digit is nonzero whenever
    $n\ge2$:
    $$\binom{10}n\quad (n\ge 2),$$
    and $9$ when $n = 1$ (the number $0$ is not positive).

(c) Nondecreasing: again $0$ cannot occur. Choose a multiset of size $n$
    from $9$ digits (stars and bars):
    $$\binom{n+8}{n}.$$

(d) Nonincreasing: choose a multiset of size $n$ from $10$ digits, and exclude
    the all-zero string:
    $$\binom{n+9}{n} - 1.$$
:::

::: {.solution for="prob-counting-09" status="draft"}
(a) $\binom{52}5 = 2{,}598{,}960$.

(b) A straight flush is fixed by its suit and its lowest card, which can be
    any of $A,2,\dots,10$:
    $$4\cdot10 = 40.$$

(c) Choose the rank of the four ($13$ ways) and then any one of the other
    $48$ cards: $13\cdot48 = 624$.

(d) Choose the rank of the three and of the two ($13\cdot12$ ordered ways),
    then their suits:
    $$13\cdot12\cdot\binom43\binom42 = 13\cdot12\cdot4\cdot6 = 3{,}744.$$

(e) All same suit: $4\binom{13}5 = 5{,}148$. Remove the $40$ straight
    flushes: $5{,}108$.

(f) Five consecutive ranks ($10$ ways), each card in any suit: $10\cdot4^5 = 10{,}240$.
    Remove the straight flushes: $10{,}200$.

(g) Choose the rank of the three ($13$) and its suits ($\binom43 = 4$). Choose
    the other two ranks from the remaining $12$ ($\binom{12}2 = 66$), and a
    suit for each ($4^2$):
    $$13\cdot4\cdot66\cdot16 = 54{,}912.$$

(h) Choose the two pair ranks ($\binom{13}2 = 78$), their suits
    ($\binom42^2 = 36$), and the fifth card from the other $11$ ranks
    ($11\cdot4$):
    $$78\cdot36\cdot44 = 123{,}552.$$

(i) Choose the pair rank ($13$) and its suits ($6$). Choose the three other
    ranks ($\binom{12}3 = 220$) and their suits ($4^3$):
    $$13\cdot6\cdot220\cdot64 = 1{,}098{,}240.$$

(j) Everything else:
    $$2{,}598{,}960 - 40 - 624 - 3{,}744 - 5{,}108 - 10{,}200 - 54{,}912 - 123{,}552 - 1{,}098{,}240 = 1{,}302{,}540.$$

    As a check, count directly: $5$ different ranks that are not consecutive,
    $\binom{13}5 - 10 = 1{,}277$, with suits not all equal, $4^5 - 4 = 1{,}020$.
    The product is $1{,}277\cdot1{,}020 = 1{,}302{,}540$.
:::
