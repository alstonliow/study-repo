::: {.problem #prob-mit1805s22-7-q2 origin="external" source="mit1805s22-7-q2"}
Prediction
We are going to explore the dice problem from class further. I have five dice (4, 6, 8, 12, or 20 sides) and pick one at random (uniform probability). I then roll this die $n$ times and tell you that, miraculously, every roll resulted in the value 7. As I am in a position of authority, assume that I am telling the truth!

(a) First, consider just the first roll. Find the prior predictive probability that the first roll will be a 7 and the posterior (after the first roll) predictive probability that the second roll will be a 7. Also find the posterior (after the first roll) probabilities for the chosen die.

(b) Find the posterior probability $P(H\mid\text{data})$ for each die given the data of all $n$ rolls (your answers should involve $n$). What is the limit of each of these probabilities as $n$ grows to infinity? Explain why this makes sense.

(c) Given that my first 10 rolls resulted in 7 (i.e., $n = 10$), rank the possible values for my next roll from most likely to least likely. Note any ties in rank and explain your reasoning carefully. You need not do any computations to solve this problem.

(d) Let $x_i$ is the result of the $i$th roll.

Find the posterior predictive pmf for the $(n + 1)$st roll given the data. That is, find $P(x_{n+1}\mid x_1 = 7, \cdots, x_n = 7)$ for $x_{n+1} = 1, \ldots, 20$. (Hint: use part (b) and the law of total probability. Many values of the pmf coincide, so you do not need to do 20 separate computations. You should check that your answer is consistent with your ranking in part (c) for $n = 10$).

(e) What function does the pmf in part (d) converge to as $n$ grows to infinity? Explain why this makes sense.
:::

::: {.problem #prob-mit1805s22-7-q3 origin="external" source="mit1805s22-7-q3"}
(Odds)
You have a drawer that contains 50 coins. 10 coins have probability $p = 0.3$ of heads, 30 coins have probability $p = 0.5$ and 10 coins have probability $p = 0.7$. You pick one coin at random from the drawer and flip it.

(a) What are the (prior) odds you chose a 0.3 coin? A 0.7 coin?

(b) What are the (prior predictive) odds of flipping a heads?

(c) Suppose the flip lands heads.

   (i) What are the posterior odds the coin is a 0.3 coin?

   (ii) What are the posterior odds the coin is a 0.7 coin?

(d) What are the posterior predictive odds of heads on the next (second) flip?
:::

::: {.problem #prob-mit1805s22-7-q5 origin="external" source="mit1805s22-7-q5"}
(Bayes at the movies)
A local theater employs two ticket collectors, Oscar and Emmy, although only one of them works on any given day. The number of tickets $X$ that a ticket collector can collect in an hour is modeled by a distribution which has mean $\lambda$, and probability mass function
$$P(X = k) = \frac{\lambda^k}{k!}e^{-\lambda}$$
for $k = 0, 1, 2, \ldots$. (This distribution is called a Poisson distribution. It is an important discrete distribution in biology and physics.)

Suppose that Oscar collects, on average, 10 tickets an hour and Emmy collects, on average, 15 tickets an hour. One day the manager stays home sick. They know Emmy is supposed to work that day, but thinks there are 1 to 10 odds that Oscar is filling in for Emmy (based on Emmy's prior history of taking advantage of Oscar's generous nature when the manager is away). The suspicious manager monitors ticket sales online and observes that over the span of 5 hours there are 12, 10, 11, 4, and 11 tickets collected. What are the manager's posterior odds that Oscar is filling in for Emmy?
:::

::: {.problem #prob-mit1805s22-7-q7 origin="external" source="mit1805s22-7-q7"}
(Censored data)
Sometimes data is not reported in full. This can mean only reporting values in a certain range or not reporting exact values. We call such data censored.

We have a 4-sided die and a 6-sided die. One of them is chosen at random and rolled 5 times. Instead of reporting the number of spots on a roll we censor the data and just report

1 if the roll is a 1; 0 if the roll is not a 1.

(a) Suppose the data for the five rolls is 1, 0, 1, 1, 1. Starting from a flat prior on the choice of die, update in sequence and report, after each roll, the posterior odds that the chosen die is the 4-sided die.

(b) A censored value of 1 is evidence in favor of which die? What about 0? How is this reflected in the posterior odds in part (a)?
:::
