<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-probability-1-16 origin="external" source="fit1058-cn-9.10-q16"}
At a cricket match the ball is hit towards a fielder, who could be any of
Alex, Chris, Kim and Sam (indistinguishable at this distance). Alex catches
with probability 0.9 (drops with 0.1). Each of Chris, Kim and Sam catches with
probability 0.4 (drops with 0.6).

(a) What is the probability that the ball is caught?

(b) Given that the ball is caught, what is the probability that the
    fielder was Alex? That it was not Alex?
:::

::: {.problem #prob-probability-1-17 origin="external" source="fit1058-cn-9.10-q17"}
A serious crime is committed in a big city; 5 million people cannot be ruled
out. A degraded DNA fragment from the criminal is found; there is no other
evidence. A random person has a one-in-a-million chance of matching. A
database search finds a match with someone who provided DNA in an irrelevant
context years ago. How likely is it that this person committed the crime? Are
they guilty beyond reasonable doubt?
:::

::: {.problem #prob-probability-1-18 origin="external" source="fit1058-cn-9.10-q18"}
In the three-coins example (from p.337 in §9.9), suppose we observe two
coin tosses instead of one. For each observation, determine the prior and
posterior probabilities of the chosen coin being Fair, DoubleHead,
DoubleTail:

(a) both tosses are Heads;

(b) both tosses are Tails;

(c) the first toss is Heads, the second is Tails.
:::

::: {.problem #prob-cs70-14-q2 origin="external" source="cs70-14.5-q2"}
Show (4) and (5).

*Note (these notes):* In CS70 Note 14, (4) is the law of total probability for a partition $A_1,\dots,A_n$ of the sample space (@thm-law-of-total-probability) and (5) is Bayes' rule for such a partition (@thm-bayes-theorem).
:::

::: {.problem #prob-cs70hw-10-q2 origin="external" source="cs70hw-10-q2"}
**Lie Detector.** A lie detector is known to be $4/5$ reliable when the person is guilty and $9/10$ reliable when the person is innocent. If a suspect is chosen from a group of suspects of which only $1/100$ have ever committed a crime, and the test indicates that the person is guilty, what is the probability that he is guilty?
:::

::: {.problem #prob-mit6042f10-11-q2 origin="external" source="mit6042f10-11-q2"}
Professor Plum, Mr. Green, and Miss Scarlet are all plotting to shoot Colonel Mustard. If one of these three has both an opportunity and the revolver, then that person shoots Colonel Mustard. Otherwise, Colonel Mustard escapes. Exactly one of the three has an opportunity with the following probabilities:
$$\Pr\{\text{Plum has opportunity}\} = 1/6,\quad \Pr\{\text{Green has opportunity}\} = 2/6,\quad \Pr\{\text{Scarlet has opportunity}\} = 3/6$$
Exactly one has the revolver with the following probabilities, regardless of who has an opportuntity:
$$\Pr\{\text{Plum has revolver}\} = 4/8,\quad \Pr\{\text{Green has revolver}\} = 3/8,\quad \Pr\{\text{Scarlet has revolver}\} = 1/8$$

(a) Draw a tree diagram for this problem. Indicate edge and outcome probabilities.

(b) What is the probability that Colonel Mustard is shot?

(c) What is the probability that Colonel Mustard is shot, given that Miss Scarlet does not have the revolver?

(d) What is the probability that Mr. Green had an opportunity, given that Colonel Mustard was shot?
:::

::: {.problem #prob-eecs126hw-1-q3 origin="external" source="eecs126hw-1-q3"}
**Expanding the NBA.** The NBA is looking to expand to another city. In order to decide which city will receive a new team, the commissioner interviews potential owners from each of the $N$ potential cities ($N$ is a positive integer), one at a time. Unfortunately, the owners would like to know immediately after the interview whether their city will receive the team or not. The commissioner decides to use the following strategy: she will interview the first $m$ owners and reject all of them ($m\in\{1,\dots,N\}$). After the $m$th owner is interviewed, she will pick the first city that is better than all previous cities. The cities are interviewed in a uniformly random order. What is the probability that the best city is selected? Assume that the commissioner has an objective method of scoring each city and that each city receives a unique score.

You should arrive at an exact answer for the probability in terms of a summation. Approximate your answer using $\sum_{i=1}^{n}i^{-1}\approx\ln n$ and find the optimal value of $m$ that maximizes the probability that the best city is selected. You can also say $\ln(n-1)\approx\ln n$.

Hint: Consider the events $B_i=\{i\text{-th city is the best}\}$ and $A=\{\text{best city is chosen}\}$.
:::

::: {.problem #prob-eecs126hw-2-q1 origin="external" source="eecs126hw-2-q1"}
**Among Us.** In the game of Among Us, there are 9 players. 4 of them are imposters and 5 of them are crewmates. There is also a deck of 17 cards containing 11 "sabotage" cards and 6 "task" cards. Imposters want to play sabotage cards, and crewmates want to play task cards. Here's how the play proceeds.

- A captain and a first mate are chosen uniformly at random from the 9 players.
- The captain draws 3 cards from the deck and gives 2 to the first mate, discarding the third.
- The first mate chooses one to play.

Now suppose you are the first mate, but the captain gave you 2 sabotage cards. Being a crewmate, you wonder, did the captain just happen to have 3 sabotage cards, or was the captain an imposter who secretly discarded a task card. In this scenario, what's the probability that the captain is an imposter? Let's assume that imposter captains always try to discard task cards, and crewmate captains always try to discard sabotage cards.
:::
