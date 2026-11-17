<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-probability-1-01" status="draft"}
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

::: {.solution for="prob-probability-1-02" status="draft"}
$$U = \{\mathrm{HHH},\mathrm{HHT},\mathrm{HTH},\mathrm{HTT},\mathrm{THH},\mathrm{THT},\mathrm{TTH},\mathrm{TTT}\} = \{\mathrm H,\mathrm T\}^3,$$
with each of the $8$ outcomes having probability $\frac18 = \bigl(\frac12\bigr)^3$,
since the tosses are fair and independent.
:::

::: {.solution for="prob-probability-1-03" status="draft"}
The outcomes are $k$ Tails followed by a Head, for $k = 0,1,2,\dots$:
$$U = \{\mathrm H,\ \mathrm{TH},\ \mathrm{TTH},\ \dots\} = \{\mathrm T^k\mathrm H : k\ge 0\},$$
$$\Pr(\mathrm T^k\mathrm H) = \Bigl(\frac12\Bigr)^{k+1}.$$

These probabilities add up to $\sum_{k\ge0}2^{-(k+1)} = 1$. So the infinite
sequence of Tails, which never stops, has probability $0$ and can be left out.
:::

::: {.solution for="prob-probability-1-04" status="draft"}
The $36$ ordered outcomes are equally likely, and the number of outcomes with
total $t$ is $6 - |t-7|$.

(a) The prime totals are $2,3,5,7,11$, with $1+2+4+6+2 = 15$ outcomes:
    $$\Pr(T\text{ prime}) = \frac{15}{36} = \frac5{12}.$$

(b) $|T-7|\ge 5$ means $T\in\{2,12\}$, with probability
    $\frac2{36}\approx 0.056\le 0.1$. And $|T-7|\ge 4$ means
    $T\in\{2,3,11,12\}$, with probability $\frac6{36}\approx 0.167 > 0.1$.
    So the minimum is $d = 5$.
:::

::: {.solution for="prob-probability-1-05" status="draft"}
All $\binom{52}5$ hands are equally likely. A hand with no diamonds uses only
the $39$ other cards:
$$\Pr(\text{no diamonds}) = \frac{\binom{39}5}{\binom{52}5} = \frac{575{,}757}{2{,}598{,}960}\approx 0.2215.$$
:::

::: {.solution for="prob-probability-1-06" status="draft"}
There are $\lfloor100/3\rfloor = 33$ multiples of $3$, and
$\lfloor100/9\rfloor = 11$ of them are multiples of $9$. So
$$\Pr = \frac{33 - 11}{100} = \frac{22}{100} = 0.22.$$
:::

::: {.solution for="prob-probability-1-07" status="draft"}
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
