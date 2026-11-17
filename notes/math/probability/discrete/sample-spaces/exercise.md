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

*Note (these notes):* The dice are drawn in the original as three faces each; each number appears on two opposite faces.
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
