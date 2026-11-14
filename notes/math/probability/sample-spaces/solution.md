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
