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

::: {.solution for="prob-cs70-10-q1"}
<!-- TODO: solution -->
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-6-q5" status="draft"}
(a) A path is a sequence of $8$ moves, $4$ right and $4$ up; choose the positions of the up moves: $\binom84=70$.

(b) Count the bad paths, those that visit some point with $y=x+1$. Reflect the part of a bad path after its first such point across the line $y=x+1$ (swap right and up moves). This is a bijection from bad paths to all paths from $(0,0)$ to $(3,5)$, of which there are $\binom83=56$. So the good paths number $70-56=14$ (the Catalan number $\frac1{5}\binom84$).

(c) A sequence of $4$ "(" and $4$ ")" is matched exactly when every prefix has at least as many "(" as ")". Reading "(" as a right move and ")" as an up move, matched sequences are the paths of (b). There are $70$ sequences in all, so $70-14=56$ are mismatched.
:::

::: {.solution for="prob-cs70hw-7-q3" status="draft"}
(a) $\binom{2n}n$: choose which $n$ of the $2n$ moves go up.

(b) $\binom{2n}{n-1}$: $2n$ moves, of which $n-1$ go right.

(c)

i. A path is bad if it visits a point with $y=x+1$. Swap right and up moves after its first such point $(i,i+1)$: the remaining part had $n-i$ right and $n-i-1$ up moves, so the new path ends at $(i+n-i-1,\,i+1+n-i)=(n-1,n+1)$. Every path to $(n-1,n+1)$ crosses the line $y=x+1$, and swapping after its first visit gives back a bad path to $(n,n)$. So bad paths are in bijection with the paths of (b), and the number of legal paths is
$$\binom{2n}n-\binom{2n}{n-1}=\frac1{n+1}\binom{2n}n.$$

ii. Let $(i,i)$ be the last diagonal point before $(n,n)$, $0\le i<n$. The part up to $(i,i)$ is any $i$-legal path: $F_i$ choices. After it the path must step right to $(i+1,i)$, stay strictly below the diagonal, and step up into $(n,n)$ at the end; the middle part is a legal path in the maze shifted by $(i+1,i)$ of side $n-i-1$: $F_{n-i-1}$ choices. Summing over $i$,
$$F_n=\sum_{i=0}^{n-1}F_iF_{n-1-i},\qquad F_0=1.$$

iii. Read the question as asking for the number $T_n$ of binary trees with $n$ nodes in the sense of the definition, where trees are compared by their left and right subtrees (and $T_0=1$ for the empty tree). Removing the root leaves a left subtree with $i$ nodes and a right subtree with $n-1-i$ nodes, chosen independently:
$$T_n=\sum_{i=0}^{n-1}T_iT_{n-1-i}.$$
It is the same recursion with the same start as in (ii), so $T_n=F_n=\frac1{n+1}\binom{2n}n$, the Catalan numbers.
:::
