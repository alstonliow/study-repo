<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-probability-1-01 origin="external" source="fit1058-cn-9.10-q1"}
A random word is chosen from a list of all five-letter English words, and
then one of that word’s five letters is chosen.

(a) What is a suitable sample space? What should the probabilities of
    its elements be?

(b) Challenge: use Linux and `/usr/share/dict/words` to
    determine the probability of each English letter in this
    experiment.
:::

::: {.problem #prob-probability-1-02 origin="external" source="fit1058-cn-9.10-q2"}
A fair coin is tossed three times; the outcome is the sequence of results (H
or T). Specify a suitable sample space, with associated probabilities.
:::

::: {.problem #prob-probability-1-03 origin="external" source="fit1058-cn-9.10-q3"}
A fair coin is tossed repeatedly until it comes up Heads for the first time;
the outcome is the sequence of results (e.g. TTH). Specify a suitable sample
space, with associated probabilities.
:::

::: {.problem #prob-probability-1-04 origin="external" source="fit1058-cn-9.10-q4"}
Two fair dice are thrown and their numbers added; let $T$ be the total.

(a) What is the probability that $T$ is prime?

(b) What is the minimum $d$ such that $\Pr(|T-7|\ge d)\le0.1$?
:::

::: {.problem #prob-probability-1-05 origin="external" source="fit1058-cn-9.10-q5"}
Find the probability that a random poker hand contains no diamonds.
:::

::: {.problem #prob-probability-1-06 origin="external" source="fit1058-cn-9.10-q6"}
A random positive integer $\le100$ is chosen uniformly. What is the
probability that it is divisible by 3 but not by 9?
:::

::: {.problem #prob-probability-1-07 origin="external" source="fit1058-cn-9.10-q7"}
(Birthday Paradox) Let $n\in\mathbb{N}$, and suppose $n$ people are chosen at random.

(a) What is the probability that at least two of them share a
    birthday?

(b) What is the minimum $n$ such that it is more likely than not that
    at least two share a birthday?
:::

::: {.problem #prob-cs70hw-9-q4 origin="external" source="cs70hw-9-q4"}
**Five Up.** Say you toss a coin five times, and record the outcomes. For the three questions below, you can assume that order matters in the outcome, and that the probability of heads is some $p$ in $0 < p < 1$, but not that the coin is fair ($p = 0.5$).

(a) What is the size of the sample space, $|\Omega|$?

(b) How many elements of $\Omega$ have exactly three heads?

(c) How many elements of $\Omega$ have three or more heads? (Hint: Argue by symmetry.)

For the next three questions, you can assume that the coin is fair (i.e. heads comes up with $p = 0.5$, and tails otherwise).

(d) What is the probability that you will observe the sequence HHHTT? What about HHHHT?

(e) What is the chance of observing at least one head?

(f) What about the chance of observing three or more heads?

For the final three questions, you can instead assume the coin is biased so that it comes up heads with probability $p = \frac{2}{3}$.

(g) What is the chance of observing the outcome HHHTT? What about HHHHT?

(h) What about the chance of at least one head?

(i) What about the chance of $\ge 3$ heads?
:::

::: {.problem #prob-cs70hw-9-q5 origin="external" source="cs70hw-9-q5"}
**Ball-and-Bin Counting Problems.** Say you have 5 bins, and randomly throw 7 balls into them.

1. What is the probability that the first bin has precisely 3 balls in it?

2. What is the probability that the third bin has at least 3 balls in it?

3. What is the probability that at least one of the bins has precisely 3 balls in it?
:::

::: {.problem #prob-mit6042f10-10-q3 origin="external" source="mit6042f10-10-q3"}
Recall the strange dice from lecture:

| A | B | C |
|---|---|---|
| 2, 6, 7 | 1, 5, 9 | 3, 4, 8 |

In the book we proved that if we roll each die once, then die A beats B more often, die B beats die C more often, and die C beats die A more often. Thus, contrary to our intuition, the "beats" relation $>$ is not transitive. That is, we have $A > B > C > A$.

We then looked at what happens if we roll each die twice, and add the result. In this problem we will show that the "beats" relation reverses in this game, that is, $A < B < C < A$, which is very counterintuitive!

(a) Show that rolling die C twice is more likely to win than rolling die B twice.

(b) Show that rolling die A twice is more likely to win that rolling die C twice.

(c) Show that rolling die B twice is more likely to win than rolling die A twice.

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab] at (0.9,2.2) {die A};
\draw[cell frame] (0.6,1.2) rectangle (1.2,1.7999999999999998);
\node[lbl] at (0.8999999999999999,1.5) {$2$};
\draw[cell frame] (0,0.6) rectangle (0.6,1.2);
\node[lbl] at (0.3,0.8999999999999999) {$6$};
\draw[cell frame] (0.6,0.6) rectangle (1.2,1.2);
\node[lbl] at (0.8999999999999999,0.8999999999999999) {$7$};
\draw[cell frame] (1.2,0.6) rectangle (1.7999999999999998,1.2);
\node[lbl] at (1.5,0.8999999999999999) {$6$};
\draw[cell frame] (0.6,0) rectangle (1.2,0.6);
\node[lbl] at (0.8999999999999999,0.3) {$2$};
\draw[cell frame] (0.6,-0.6) rectangle (1.2,0.0);
\node[lbl] at (0.8999999999999999,-0.3) {$7$};
\node[lab] at (3.6999999999999997,2.2) {die B};
\draw[cell frame] (3.4,1.2) rectangle (4.0,1.7999999999999998);
\node[lbl] at (3.6999999999999997,1.5) {$1$};
\draw[cell frame] (2.8,0.6) rectangle (3.4,1.2);
\node[lbl] at (3.0999999999999996,0.8999999999999999) {$5$};
\draw[cell frame] (3.4,0.6) rectangle (4.0,1.2);
\node[lbl] at (3.6999999999999997,0.8999999999999999) {$9$};
\draw[cell frame] (4.0,0.6) rectangle (4.6,1.2);
\node[lbl] at (4.3,0.8999999999999999) {$5$};
\draw[cell frame] (3.4,0) rectangle (4.0,0.6);
\node[lbl] at (3.6999999999999997,0.3) {$1$};
\draw[cell frame] (3.4,-0.6) rectangle (4.0,0.0);
\node[lbl] at (3.6999999999999997,-0.3) {$9$};
\node[lab] at (6.5,2.2) {die C};
\draw[cell frame] (6.199999999999999,1.2) rectangle (6.799999999999999,1.7999999999999998);
\node[lbl] at (6.499999999999999,1.5) {$3$};
\draw[cell frame] (5.6,0.6) rectangle (6.199999999999999,1.2);
\node[lbl] at (5.8999999999999995,0.8999999999999999) {$4$};
\draw[cell frame] (6.199999999999999,0.6) rectangle (6.799999999999999,1.2);
\node[lbl] at (6.499999999999999,0.8999999999999999) {$8$};
\draw[cell frame] (6.8,0.6) rectangle (7.3999999999999995,1.2);
\node[lbl] at (7.1,0.8999999999999999) {$4$};
\draw[cell frame] (6.199999999999999,0) rectangle (6.799999999999999,0.6);
\node[lbl] at (6.499999999999999,0.3) {$3$};
\draw[cell frame] (6.199999999999999,-0.6) rectangle (6.799999999999999,0.0);
\node[lbl] at (6.499999999999999,-0.3) {$8$};
\end{tikzpicture}
\end{center}
```
:::

::: {.problem #prob-mit6042f10-10-q4 origin="external" source="mit6042f10-10-q4"}
Let's play a game! We repeatedly flip a fair coin. You have the sequence $HHT$, and I have the sequence $HTT$. If your sequence comes up first, then you win. If my sequence comes up first, then I win. For example, if the sequence of tosses is:
$$TTHTHTHHT$$
then you win. What is the probability that you win? It may come as a surprise that the answer is very different from 1/2.

This problem is tricky, because the game could go on for an arbitrarily long time. Draw enough of the tree diagram to see a pattern, and then sum up the probabilities of the (infinitely many) outcomes in which you win.

It turns out that for any sequence of three flips, there is another sequence that is likely to come up before it. So there is no sequence of three flips which turns up earliest! ... and given any sequence of three flips, knowing how to pick another sequence that comes up sooner more than half the time gives you a nice chance to fool people gambling at a bar :-)
:::

::: {.problem #prob-mit6042f10-10-q5 origin="external" source="mit6042f10-10-q5"}
We're interested in the probability that a randomly chosen poker hand (5 cards from a standard 52-card deck) contains cards from at most two suits.

(a) What is an appropriate sample space to use for this problem? What are the outcomes in the event, $E$, we are interested in? What are the probabilities of the individual outcomes in this sample space?

(b) What is $\Pr(E)$?
:::

::: {#prob-flush-enumeration-code .problem .coding origin="adapted" source="res-ucb-eecs126-labs-simulation"}
A deck has $r$ ranks $0,\dots,r-1$ and $s$ suits, with one card of each rank and suit. A hand of $k$ cards is drawn at random, so all $\binom{rs}{k}$ hands are equally likely (@def-probability-equally-likely-case). Call a hand a *flush* if all its cards have the same suit and its ranks are not $k$ consecutive numbers (a run such as $3,4,5$).

Write `flush_probability(r, s, k)`. It returns the probability of a flush as an exact `Fraction`, found by listing every hand (`itertools.combinations`) and counting the flushes. A real deck ($r=13$, $s=4$, $k=5$) already has about 2.6 million hands, so the tests use small decks.

```{.python .starter}
from fractions import Fraction
from itertools import combinations, product


def flush_probability(r, s, k):
    """Exact probability (a Fraction) that k cards drawn from a deck of r ranks
    and s suits are all of one suit but their ranks are not k consecutive values."""
    ...
```

```{.python .tests}
from fractions import Fraction
from math import comb


def formula(r, s, k):
    # choose a suit, then k ranks that are not one of the r-k+1 runs
    return Fraction(s * (comb(r, k) - (r - k + 1)), comb(r * s, k))


def test_two_cards():
    # 5 ranks, 2 suits: 20 same-suit pairs, 8 of them adjacent ranks
    assert flush_probability(5, 2, 2) == Fraction(12, 45)


def test_returns_exact_fraction():
    assert isinstance(flush_probability(4, 2, 2), Fraction)


def test_against_formula():
    for r, s, k in [(6, 3, 3), (7, 2, 4), (8, 4, 3), (5, 4, 5)]:
        assert flush_probability(r, s, k) == formula(r, s, k), (r, s, k)


def test_single_card_is_a_straight():
    assert flush_probability(4, 3, 1) == 0


def test_one_suit_deck():
    # every hand is one suit; only the non-runs count
    assert flush_probability(6, 1, 3) == Fraction(comb(6, 3) - 4, comb(6, 3))
```
:::

::: {#prob-palindrome-hands-code .problem .coding origin="adapted" source="res-ucb-eecs126-labs-simulation"}
A deck has $r$ ranks and $s$ suits, with one card of each rank and suit, and a hand of $k$ cards is drawn at random. Call the hand *symmetric* if its cards can be laid in a row whose ranks read the same from both ends. This holds exactly when at most one rank occurs an odd number of times in the hand.

Write `palindrome_probability(k, r=13, s=4)` that returns the probability of a symmetric hand as an exact `Fraction`. Listing hands is hopeless for a full deck ($\binom{52}{9}\approx3.7\times10^{9}$). Instead, group the hands by their *rank counts* $(c_0,\dots,c_{r-1})$ with $0\le c_i\le s$ and $\sum_i c_i=k$. These groups are not equally likely, but the group with counts $c$ holds exactly $\prod_i\binom{s}{c_i}$ hands. The tests include $k=9$ on a full deck.

```{.python .starter}
from fractions import Fraction
from math import comb


def palindrome_probability(k, r=13, s=4):
    """Exact probability (a Fraction) that the ranks of k cards drawn from a deck
    of r ranks and s suits can be laid out as a palindrome."""
    ...
```

```{.python .tests}
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb


def brute_force(k, r, s):
    deck = list(product(range(r), range(s)))
    good = total = 0
    for hand in combinations(deck, k):
        total += 1
        odd = sum(c % 2 for c in Counter(rank for rank, _ in hand).values())
        good += odd <= 1
    return Fraction(good, total)


def test_small_decks():
    for k, r, s in [(3, 4, 3), (4, 4, 3), (5, 5, 2), (6, 3, 4)]:
        assert palindrome_probability(k, r, s) == brute_force(k, r, s), (k, r, s)


def test_one_and_two_cards():
    assert palindrome_probability(1) == 1
    assert palindrome_probability(2) == Fraction(13 * comb(4, 2), comb(52, 2))


def test_too_many_odd_ranks():
    # 3 ranks, 1 suit, 2 cards: always two different ranks
    assert palindrome_probability(2, 3, 1) == 0


def test_full_deck_fast():
    # C(52, 9) hands are far too many to list; count rank patterns instead
    p = palindrome_probability(9)
    assert isinstance(p, Fraction) and 0 < p < Fraction(1, 10)
    assert p == Fraction(_reference_count(9), comb(52, 9))


def _reference_count(k):
    # generating function: product over ranks of (even part + y * odd part)
    poly = {(0, 0): 1}                      # (cards, odd ranks) -> count
    for _ in range(13):
        new = Counter()
        for (n, o), w in poly.items():
            for c in range(5):
                if n + c <= k and o + c % 2 <= 1:
                    new[(n + c, o + c % 2)] += w * comb(4, c)
        poly = new
    return poly[(k, 0)] + poly[(k, 1)]
```
:::

::: {.problem #prob-mit6041f10-1-q2 origin="external" source="mit6041f10-1-q2"}
You flip a fair coin 3 times, determine the probability of the below events. Assume all sequences are equally likely.

(a) Three heads: HHH
(b) The sequence head, tail, head: HTH
(c) Any sequence with 2 heads and 1 tail
(d) Any sequence where the number of heads is greater than or equal to the number of tails
:::

::: {.problem #prob-mit6041f10-1-q3 origin="external" source="mit6041f10-1-q3"}
Bob has a peculiar pair of four-sided dice. When he rolls the dice, the probability of any particular outcome is proportional to the sum of the results of each die. All outcomes that result in a particular sum are equally likely.

(a) What is the probability of the sum being even?
(b) What is the probability of Bob rolling a 2 and a 3, in any order?
:::

::: {.problem #prob-mit6041f10-1-q4 origin="external" source="mit6041f10-1-q4"}
Alice and Bob each choose at random a number in the interval $[0, 2]$. We assume a uniform probability law under which the probability of an event is proportional to its area. Consider the following events:

$A$ : The magnitude of the difference of the two numbers is greater than $1/3$.
$B$ : At least one of the numbers is greater than $1/3$.
$C$ : The two numbers are equal.
$D$ : Alice's number is greater than $1/3$.

Find the probabilities $\mathbf{P}(B)$, $\mathbf{P}(C)$, and $\mathbf{P}(A \cap D)$.
:::

::: {.problem #prob-mit6041f10-1-q5 origin="external" source="mit6041f10-1-q5"}
Mike and John are playing a friendly game of darts where the dart board is a disk with radius of 10in.

Whenever a dart falls within 1in of the center, 50 points are scored. If the point of impact is between 1 and 3in from the center, 30 points are scored, if it is at a distance of 3 to 5in 20 points are scored and if it is further that 5in, 10 points are scored.

Assume that both players are skilled enough to be able to throw the dart within the boundaries of the board.

Mike can place the dart uniformly on the board (i.e., the probability of the dart falling in a given region is proportional to its area).

(a) What is the probability that Mike scores 50 points on one throw?
(b) What is the probability of him scoring 30 points on one throw?
(c) John is right handed and is twice more likely to throw in the right half of the board than in the left half. Across each half, the dart falls uniformly in that region. Answer the previous questions for John's throw.
:::

::: {.problem #prob-mit6041f10-3-q1 origin="external" source="mit6041f10-3-q1"}
The hats of $n$ persons are thrown into a box. The persons then pick up their hats at random (i.e., so that every assignment of the hats to the persons is equally likely). What is the probability that

(a) every person gets his or her hat back?
(b) the first $m$ persons who picked hats get their own hats back?
(c) everyone among the first $m$ persons to pick up the hats gets back a hat belonging to one of the last $m$ persons to pick up the hats?

Now assume, in addition, that every hat thrown into the box has probability $p$ of getting dirty (independently of what happens to the other hats or who has dropped or picked it up). What is the probability that

(d) the first $m$ persons will pick up clean hats?
(e) exactly $m$ persons will pick up clean hats?
:::

::: {.problem #prob-mit6041f10-3-q2 origin="external" source="mit6041f10-3-q2"}
Alice plays with Bob the following game. First Alice randomly chooses 4 cards out of a 52-card deck, memorizes them, and places them back into the deck. Then Bob randomly chooses 8 cards out of the same deck. Alice wins if Bob's cards include all cards selected by her. What is the probability of this happening?
:::

::: {.problem #prob-mit1805s22-1-q2 origin="external" source="mit1805s22-1-q2"}
(Non-transitive dice)
In class we worked with non-transitive dice:

Blue: 3 3 3 3 3 6; Orange: 1 4 4 4 4 4; White: 2 2 2 5 5 5.

(a) Find the probability that white beats orange, the probability that orange beats blue and the probability that blue beats white.
Can you line the dice up in order from best to worst? (Hint: this is why these are called 'non-transitive'.)

(b) Suppose you roll two white dice against two blue dice. What is the probability that the sum of the white dice is greater than the sum of the blue dice?

For hints on this problem and ways to make money with your dice, watch at least the first six minutes of the following video.
<https://www.youtube.com/watch?v=zWUrwhaqq_c>

Here a tree is used to organize the calculation rather than a table. We will discuss this method in Week 2.
:::
