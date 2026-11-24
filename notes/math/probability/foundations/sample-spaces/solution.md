<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-probability-1-01"}
(a) Let $W$ be the set of five-letter English words, with $|W| = N$. An
    outcome is a word together with a position in it:
    $$U = W\times\{1,2,3,4,5\},\qquad |U| = 5N.$$
    With no reason to prefer any word or position, use the uniform
    distribution: $\Pr\bigl((w,i)\bigr) = \frac{1}{5N}$ for every $(w,i)\in U$.

(b) The probability of a letter $\ell$ is
    $$\Pr(\ell) = \frac{\text{number of occurrences of }\ell\text{ in all five-letter words}}{5N}.$$
    One way to count the occurrences:

    ```
    tr '[:upper:]' '[:lower:]' < /usr/share/dict/words \
      | grep -x '[a-z]\{5\}' | grep -o . | sort | uniq -c | sort -nr
    ```

    `grep -x` keeps the lines that are exactly five letters, `grep -o .`
    puts each letter on its own line, and `uniq -c` counts them. Divide each
    count by $5N$, where $N$ is the number of words (`grep -c` with the same
    pattern). The counts depend on the word list installed.
:::

::: {.solution for="prob-probability-1-02"}
$$U = \{\mathrm{HHH},\mathrm{HHT},\mathrm{HTH},\mathrm{HTT},\mathrm{THH},\mathrm{THT},\mathrm{TTH},\mathrm{TTT}\} = \{\mathrm H,\mathrm T\}^3,$$
with each of the $8$ outcomes having probability $\frac18 = \bigl(\frac12\bigr)^3$,
since the tosses are fair and independent.
:::

::: {.solution for="prob-probability-1-03"}
The outcomes are $k$ Tails followed by a Head, for $k = 0,1,2,\dots$:
$$U = \{\mathrm H,\ \mathrm{TH},\ \mathrm{TTH},\ \dots\} = \{\mathrm T^k\mathrm H : k\ge 0\},$$
$$\Pr(\mathrm T^k\mathrm H) = \Bigl(\frac12\Bigr)^{k+1}.$$

These probabilities add up to $\sum_{k\ge0}2^{-(k+1)} = 1$. So the infinite
sequence of Tails, which never stops, has probability $0$ and can be left out.
:::

::: {.solution for="prob-probability-1-04"}
The $36$ ordered outcomes are equally likely, and the number of outcomes with
total $t$ is $6 - |t-7|$.

(a) The prime totals are $2,3,5,7,11$, with $1+2+4+6+2 = 15$ outcomes:
    $$\Pr(T\text{ prime}) = \frac{15}{36} = \frac5{12}.$$

(b) $|T-7|\ge 5$ means $T\in\{2,12\}$, with probability
    $\frac2{36}\approx 0.056\le 0.1$. And $|T-7|\ge 4$ means
    $T\in\{2,3,11,12\}$, with probability $\frac6{36}\approx 0.167 > 0.1$.
    So the minimum is $d = 5$.
:::

::: {.solution for="prob-probability-1-05"}
All $\binom{52}5$ hands are equally likely. A hand with no diamonds uses only
the $39$ other cards:
$$\Pr(\text{no diamonds}) = \frac{\binom{39}5}{\binom{52}5} = \frac{575{,}757}{2{,}598{,}960}\approx 0.2215.$$
:::

::: {.solution for="prob-probability-1-06"}
There are $\lfloor100/3\rfloor = 33$ multiples of $3$, and
$\lfloor100/9\rfloor = 11$ of them are multiples of $9$. So
$$\Pr = \frac{33 - 11}{100} = \frac{22}{100} = 0.22.$$
:::

::: {.solution for="prob-probability-1-07"}
Assume $365$ equally likely birthdays (ignore 29 February), chosen
independently.

(a) For $n\le 365$, the probability that all $n$ birthdays are different is
    $$\frac{365\cdot364\cdots(365-n+1)}{365^n} = \prod_{k=0}^{n-1}\Bigl(1-\frac{k}{365}\Bigr).$$
    So
    $$\Pr(\text{at least two share}) = 1 - \prod_{k=0}^{n-1}\Bigl(1-\frac{k}{365}\Bigr),$$
    and the probability is $1$ for $n > 365$ (pigeonhole principle).

(b) For $n = 22$ the probability is about $0.476$, and for $n = 23$ it is
    about $0.507$. So the minimum is $n = 23$.
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-9-q4" status="draft"}
(a) $|\Omega|=2^5=32$ sequences.

(b) Choose the positions of the heads: $\binom53=10$.

(c) Swapping H and T is a bijection between sequences with $\ge3$ heads and sequences with $\le2$ heads (i.e. $\ge3$ tails), so each set has half of the $32$: $16$.

(d) Each sequence has probability $\frac1{32}$, so both are $\frac1{32}$.

(e) $1-\Pr(\text{TTTTT})=1-\frac1{32}=\frac{31}{32}$.

(f) $\frac{16}{32}=\frac12$, by (c).

(g) $\Pr(\text{HHHTT})=(\frac23)^3(\frac13)^2=\frac8{243}$ and $\Pr(\text{HHHHT})=(\frac23)^4\frac13=\frac{16}{243}$.

(h) $1-(\frac13)^5=\frac{242}{243}$.

(i) $\sum_{k=3}^5\binom5k(\frac23)^k(\frac13)^{5-k}=\frac{10\cdot8+5\cdot16+32}{243}=\frac{192}{243}=\frac{64}{81}$.
:::

::: {.solution for="prob-cs70hw-9-q5" status="draft"}
All $5^7=78125$ assignments of balls to bins are equally likely.

1. Choose the $3$ balls in bin $1$, and put the other $4$ in the other $4$ bins: $\frac{\binom73\cdot4^4}{5^7}=\frac{8960}{78125}\approx0.115$.

2. Subtract the cases with $0$, $1$ or $2$ balls in bin $3$: $1-\frac{4^7+7\cdot4^6+21\cdot4^5}{5^7}=1-\frac{66560}{78125}=\frac{11565}{78125}\approx0.148$.

3. Let $A_i$ be "bin $i$ has exactly $3$ balls". Three bins cannot each have $3$ of $7$ balls. Two bins: choose their $3+3$ balls and put the last ball in one of the other $3$ bins: $\binom73\binom43\cdot3=420$ assignments. By inclusion–exclusion (@thm-general-case),
   $$\Pr\Bigl(\bigcup_iA_i\Bigr)=\frac{5\cdot8960-\binom52\cdot420}{78125}=\frac{40600}{78125}\approx0.520.$$
:::

::: {.solution for="prob-mit6042f10-10-q3" status="draft"}
Each die shows each of its three numbers with probability $\frac13$ (each number appears on two faces), so a pair of rolls gives $9$ equally likely ordered pairs, and two players' sums give $81$ equally likely combinations.

The sums of two rolls (with multiplicities out of $9$) are:

- $A$: $4\,(1),\ 8\,(2),\ 9\,(2),\ 12\,(1),\ 13\,(2),\ 14\,(1)$;
- $B$: $2\,(1),\ 6\,(2),\ 10\,(3),\ 14\,(2),\ 18\,(1)$;
- $C$: $6\,(1),\ 7\,(2),\ 8\,(1),\ 11\,(2),\ 12\,(2),\ 16\,(1)$.

Counting the combinations in which one sum exceeds the other:

(a) $C$ beats $B$ in $42$ of $81$ cases, $B$ beats $C$ in $37$, with $2$ ties: $\frac{42}{81}>\frac{37}{81}$.

(b) $A$ beats $C$ in $44$ cases and $C$ beats $A$ in $33$ ($4$ ties).

(c) $B$ beats $A$ in $42$ cases and $A$ beats $B$ in $37$ ($2$ ties).

So with two rolls $C>B$, $A>C$ and $B>A$: each relation is reversed. (The counts were checked by computer.)
:::

::: {.solution for="prob-mit6042f10-10-q4" status="draft"}
You win with probability $\frac23$.

1. Tails before the first $H$ change nothing, so start at the first $H$.

2. If the next flip is also $H$ (probability $\frac12$), you have $HH$, and you win for sure: from $HH$ the flips continue $H\dots HT$, and the first $T$ completes $HHT$ before $HTT$ can appear (an $HTT$ would need $HT$ first, but every $T$ after $HH$ completes your $HHT$ immediately).

3. If the next flip is $T$, we have $HT$. Now a $T$ (probability $\frac12$) completes $HTT$ and I win; an $H$ (probability $\frac12$) puts us back at a fresh $H$.

4. Let $w$ be your winning probability from a fresh $H$. Then $w=\frac12\cdot1+\frac12\cdot\frac12\cdot0+\frac12\cdot\frac12\cdot w$, so $\frac34w=\frac12$ and $w=\frac23$.

Summing the tree directly gives the same: you win along $H(TH)^kH\dots$, with probability $\frac12\sum_{k\ge0}\bigl(\frac14\bigr)^k=\frac23$.
:::

::: {.solution for="prob-mit6042f10-10-q5" status="draft"}
(a) The sample space is the set of all $5$-card subsets of the deck, $\binom{52}5=2\,598\,960$ outcomes, each with probability $1/\binom{52}5$. The event $E$ consists of the hands whose cards come from at most two suits.

(b) One suit: $4\binom{13}5=5148$ hands. Exactly two suits: choose the suits ($\binom42=6$) and a hand from their $26$ cards that is not within a single suit: $\binom{26}5-2\binom{13}5=63\,206$, giving $379\,236$. So
$$\Pr(E)=\frac{5148+379\,236}{2\,598\,960}=\frac{384\,384}{2\,598\,960}\approx0.148.$$
:::

::: {.solution for="prob-flush-enumeration-code" status="draft"}
```{.python}
from fractions import Fraction
from itertools import combinations, product


def flush_probability(r, s, k):
    """Exact probability (a Fraction) that k cards drawn from a deck of r ranks
    and s suits are all of one suit but their ranks are not k consecutive values."""
    deck = list(product(range(r), range(s)))      # card = (rank, suit)
    total = favourable = 0
    for hand in combinations(deck, k):            # equally likely outcomes
        total += 1
        ranks = sorted(rank for rank, _ in hand)
        one_suit = len({suit for _, suit in hand}) == 1
        straight = ranks == list(range(ranks[0], ranks[0] + k))
        if one_suit and not straight:
            favourable += 1
    return Fraction(favourable, total)
```

1. The sample space is the set of $k$-subsets of the $rs$ cards, all equally likely, so the probability is the number of flushes divided by the number of hands (@def-probability-equally-likely-case).
2. A hand is one suit when its set of suits has one element, and a run when its sorted ranks are $m,m+1,\dots,m+k-1$ for its smallest rank $m$.
3. Check against a count: choose the suit ($s$ ways) and $k$ ranks that are not one of the $r-k+1$ runs, so the answer is $s\bigl(\binom rk-(r-k+1)\bigr)/\binom{rs}{k}$; the tests use this formula.
:::

::: {.solution for="prob-palindrome-hands-code" status="draft"}
```{.python}
from fractions import Fraction
from math import comb


def palindrome_probability(k, r=13, s=4):
    """Exact probability (a Fraction) that the ranks of k cards drawn from a deck
    of r ranks and s suits can be laid out as a palindrome."""
    def count(i, left, odd):
        # hands using ranks i..r-1 with `left` cards still to choose,
        # where `odd` ranks so far have an odd number of cards
        if i == r:
            return 1 if left == 0 and odd <= 1 else 0
        total = 0
        for c in range(min(s, left) + 1):         # c cards of rank i
            o = odd + c % 2
            if o <= 1:
                total += comb(s, c) * count(i + 1, left - c, o)
        return total
    return Fraction(count(0, k, 0), comb(r * s, k))
```

1. By the product rule, a hand with rank counts $c$ is fixed by choosing, for each rank $i$, which $c_i$ of its $s$ suits appear, so the group has $\prod_i\binom{s}{c_i}$ hands.
2. The function `count(i, left, odd)` adds these weights over all count vectors, choosing $c_i$ for one rank at a time. It tracks the cards still to choose and how many ranks so far have an odd count, and stops a branch as soon as two ranks are odd.
3. The probability is the total weight of the symmetric groups divided by $\binom{rs}{k}$, the weight of all groups. The recursion visits at most $(s+1)^r$ partial vectors and in practice far fewer, because of the two bounds.
:::

::: {.solution for="prob-mit6041f10-1-q2" status="draft"}
The sample space has $2^3=8$ equally likely sequences, so each event has probability (number of its sequences)$/8$.

(a) One sequence: $1/8$.
(b) One sequence: $1/8$.
(c) HHT, HTH, THH: $3/8$.
(d) With three tosses heads $\ge$ tails means at least two heads: HHH and the three sequences of (c), so $4/8=1/2$.
:::

::: {.solution for="prob-mit6041f10-1-q3" status="draft"}
Outcomes are ordered pairs $(i,j)$, $1\le i,j\le4$, with $\Pr(i,j)=c(i+j)$.

1. Normalise: $\sum_{i,j}(i+j)=2\cdot4\cdot(1+2+3+4)=80$, so $c=1/80$.

2. (a) Even sums are $2,4,6,8$, reached by $1,3,3,1$ pairs, total weight $2\cdot1+4\cdot3+6\cdot3+8\cdot1=40$. So $\Pr(\text{even})=40/80=1/2$.

3. (b) The outcomes $(2,3)$ and $(3,2)$ each have weight $5$, so the probability is $10/80=1/8$.
:::

::: {.solution for="prob-mit6041f10-1-q4" status="draft"}
Let $x$ be Alice's number and $y$ Bob's; the sample space is the square $[0,2]^2$ of area $4$, and $\Pr(E)=\text{area}(E)/4$.

1. $B^c$ is the square $[0,1/3]^2$ of area $1/9$, so $\Pr(B)=1-\frac{1/9}4=\frac{35}{36}$.

2. $C$ is the diagonal $y=x$, a line segment of area $0$, so $\Pr(C)=0$.

3. $A\cap D$ is $\{x>1/3\}$ intersected with two triangles. Below the diagonal: $y<x-1/3$, which already forces $x>1/3$; it is the triangle with legs $5/3$, area $\frac12(5/3)^2=25/18$. Above the diagonal: $y>x+1/3$ and $x>1/3$, the triangle with vertices $(1/3,2/3)$, $(1/3,2)$, $(5/3,2)$, legs $4/3$, area $\frac12(4/3)^2=16/18$.

4. So $\Pr(A\cap D)=\frac{41/18}4=\frac{41}{72}$.
:::

::: {.solution for="prob-mit6041f10-1-q5" status="draft"}
The board has area $100\pi$.

(a) The inner disk has area $\pi$, so the probability is $\pi/(100\pi)=0.01$.

(b) The ring between radii $1$ and $3$ has area $9\pi-\pi=8\pi$, so the probability is $0.08$.

(c) John lands in the right half with probability $2/3$ and the left half with probability $1/3$, uniformly within each half (area $50\pi$). Every scoring region is a disk or ring centred at the centre, so it is cut exactly in half by the vertical diameter. For a region of area $a$,
$$\Pr=\frac23\cdot\frac{a/2}{50\pi}+\frac13\cdot\frac{a/2}{50\pi}=\frac a{100\pi},$$
the same as for Mike: $0.01$ for 50 points and $0.08$ for 30 points.
:::

::: {.solution for="prob-mit6041f10-3-q1" status="draft"}
The $n!$ assignments of hats to persons are equally likely.

(a) Only one assignment works: $1/n!$.

(b) The first $m$ persons are fixed and the other $n-m$ hats go anywhere: $(n-m)!/n!$.

(c) The first $m$ persons receive the $m$ hats of the last $m$ persons in some order ($m!$ ways) and the remaining $n-m$ hats go to the rest ($(n-m)!$ ways): $\frac{m!\,(n-m)!}{n!}=1/\binom nm$.

(d) Whatever hats they get, those are $m$ distinct hats, each clean with probability $1-p$ independently of the assignment: $(1-p)^m$.

(e) Every person picks up exactly one hat, so this is the probability that exactly $m$ of the $n$ hats are clean: $\binom nm(1-p)^mp^{n-m}$.
:::

::: {.solution for="prob-mit6041f10-3-q2" status="draft"}
Fix Alice's 4 cards. Bob's hand is one of $\binom{52}8$ equally likely sets, and it contains Alice's cards exactly when its other 4 cards come from the remaining 48. So
$$\Pr(\text{Alice wins})=\frac{\binom{48}4}{\binom{52}8}=\frac2{7735}\approx2.6\times10^{-4}.$$
:::

::: {.solution for="prob-mit1805s22-1-q2" status="draft"}
(a) Each pair of faces has probability $1/36$; count the winning pairs.

1. White beats orange: a white $5$ beats every orange face ($3\cdot6=18$ pairs), a white $2$ beats only the orange $1$ ($3$ pairs): $21/36=7/12$.

2. Orange beats blue: an orange $4$ beats the five blue $3$s: $5\cdot5=25$ pairs, probability $25/36$.

3. Blue beats white: a blue $3$ beats a white $2$ ($5\cdot3=15$ pairs), the blue $6$ beats every white face ($6$ pairs): $21/36=7/12$.

Each die beats the next with probability above $\frac12$ in the cycle white $\to$ orange $\to$ blue $\to$ white, so no ordering from best to worst is consistent with "beats more often than not".

(b) A sum of two blue dice is $6$ (probability $25/36$), $9$ ($10/36$) or $12$ ($1/36$). A sum of two white dice is $4$ ($9/36$), $7$ ($18/36$) or $10$ ($9/36$). White wins when it has $7$ against $6$, or $10$ against $6$ or $9$:
$$\frac{18}{36}\cdot\frac{25}{36}+\frac9{36}\cdot\frac{35}{36}=\frac{450+315}{1296}=\frac{85}{144}\approx0.59.$$
With two dice each, white now beats blue, reversing part (a).
:::
