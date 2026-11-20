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

::: {.problem #prob-mit6041f10-2-q1 origin="external" source="mit6041f10-2-q1"}
Most mornings, Victor checks the weather report before deciding whether to carry an umbrella. If the forecast is "rain," the probability of actually having rain that day is 80%. On the other hand, if the forecast is "no rain," the probability of it actually raining is equal to 10%. During fall and winter the forecast is "rain" 70% of the time and during summer and spring it is 20%.

(a) One day, Victor missed the forecast and it rained. What is the probability that the forecast was "rain" if it was during the winter? What is the probability that the forecast was "rain" if it was during the summer?
(b) The probability of Victor missing the morning forecast is equal to 0.2 on any day in the year. If he misses the forecast, Victor will flip a fair coin to decide whether to carry an umbrella. On any day of a given season he sees the forecast, if it says "rain" he will always carry an umbrella, and if it says "no rain," he will not carry an umbrella. Are the events "Victor is carrying an umbrella," and "The forecast is no rain" independent? Does your answer depend on the season?
(c) Victor is carrying an umbrella and it is not raining. What is the probability that he saw the forecast? Does it depend on the season?
:::

::: {.problem #prob-mit6041f10-2-q3 origin="external" source="mit6041f10-2-q3"}
The local widget factory is having a blowout widget sale. Everything must go, old and new. The factory has 500 old widgets, and 1500 new widgets in stock. The problem is that 15% of the old widgets are defective, and 5% of the new ones are defective as well. You can assume that widgets are selected at random when an order comes in. You are the first customer since the sale was announced.

(a) You flip a fair coin once to decide whether to buy old or new widgets. You order two widgets of the same type, chosen based on the outcome of the coin toss. What is the probability that they will both be defective?
(b) Given that both widgets turn out to be defective, what is the probability that they were old widgets?
:::

::: {.problem #prob-mit6041f10-2-q4 origin="external" source="mit6041f10-2-q4"}
Oscar has lost his dog in either forest A (with a priori probability 0.4) or in forest B (with a priori probability 0.6).

On any given day, if the dog is in A and Oscar spends a day searching for it in A, the conditional probability that he will find the dog that day is 0.25. Similarly, if the dog is in B and Oscar spends a day looking for it there, the conditional probability that he will find the dog that day is 0.15.

The dog cannot go from one forest to the other. Oscar can search only in the daytime, and he can travel from one forest to the other only at night.

(a) In which forest should Oscar look to maximize the probability he finds his dog on the first day of the search?
(b) Given that Oscar looked in A on the first day but didn't find his dog, what is the probability that the dog is in A?
(c) If Oscar flips a fair coin to determine where to look on the first day and finds the dog on the first day, what is the probability that he looked in A?
(d) If the dog is alive and not found by the $N$th day of the search, it will die that evening with probability $\frac{N}{N+2}$. Oscar has decided to look in A for the first two days. What is the probability that he will find a live dog for the first time on the second day?
:::
