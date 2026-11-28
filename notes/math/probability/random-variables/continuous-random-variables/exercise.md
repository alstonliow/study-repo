::: {.problem #prob-cs70hw-13-q4 origin="external" source="cs70hw-13-q4"}
**Lunch Meeting.** Alice and Bob agree to try to meet for lunch between 12 PM and 1 PM at their favorite sushi restaurant. Being extremely busy, they are unable to specify their arrival times exactly, and can say only that each of them will arrive (independently) at a time that is uniformly distributed within the hour. In order to avoid wasting precious time, if the other person is not there when they arrive they agree to wait exactly fifteen minutes before leaving. What is the probability that they will actually meet for lunch? (hint: Sketch the joint distribution of the arrival times of Alice and Bob. What parts of the distribution corresponds to them meeting for lunch?)
:::

::: {.problem #prob-cs70hw-14-q1 origin="external" source="cs70hw-14-q1"}
**Short Answer.**

(a) Let $X$ be uniform on the interval $[0, 2]$, and define $Y = 2X + 1$. Find the PDF, CDF, expectation, and variance of $Y$.

(b) Let $X$ and $Y$ have joint distribution
$$f(x, y) = \begin{cases} cxy + 1/4 & x \in [1, 2] \text{ and } y \in [0, 2] \\ 0 & \text{else} \end{cases}$$
Find the constant $c$. Are $X$ and $Y$ independent?
:::

::: {.problem #prob-cs70hw-14-q4 origin="external" source="cs70hw-14-q4"}
**Useful Uniforms.** Let $X$ be a continuous random variable whose image is all of $\mathbb{R}$; that is, $P[X \in (a, b)] > 0$ for all $a, b \in \mathbb{R}$ and $a \ne b$.

(a) Give an example of a distribution that $X$ could have, and one that it could not.

(b) Show that the CDF $F$ of $X$ is strictly increasing. That is, $F(x + \varepsilon) > F(x)$ for any $\varepsilon > 0$. Argue why this implies that $F: \mathbb{R} \to (0, 1)$ must be invertible.

(c) Let $U$ be a uniform random variable on $(0, 1)$. What is the distribution of $F^{-1}(U)$?

(d) Your work in part (c) shows that in order to sample $X$, it is enough to be able to sample $U$. If $X$ was a discrete random variable instead, taking finitely many values, can we still use $U$ to sample $X$?
:::

::: {.problem #prob-cs70hw-14-q5 origin="external" source="cs70hw-14-q5"}
**Uniform Means.** To keep the doctor away, Bob goes to the supermarket to buy an apple. Let $X_1, X_2, \ldots, X_n$ be $n$ independent and identically distributed uniform random variables on the interval $[0, 1]$ (where $n$ is a positive integer), where $X_i$ is the quality of the $i$th apple Bob sees.

(a) Let $Y = \min\{X_1, X_2, \ldots, X_n\}$ be the quality of the worst apple Bob will see. Find $E(Y)$. [Hint: Use the tail sum formula, which says the expected value of a nonnegative random variable is $E(X) = \int_0^\infty P(X > x)\, dx$. Note that we can use the tail sum formula since $Y \ge 0$.]

(b) Let $Z = \max\{X_1, X_2, \ldots, X_n\}$ be the quality of the best apple Bob will see. Find $E(Z)$. [Hint: Find the CDF.]
:::

::: {.problem #prob-cs70hw-14-q6 origin="external" source="cs70hw-14-q6"}
**Darts but with ML.** Suppose Alice and Bob are playing darts on a circular board with radius 1. When Alice throws a dart, the distance of the dart from the center is uniform $[0, 1]$. When Bob throws the dart, the location of the dart is uniform over the whole board. Let $X$ be the random variable corresponding to the distance of the player's dart from the center of the board.

(a) What is the pdf of $X$ if Alice throws

(b) What is the pdf of $X$ if Bob throws

(c) Suppose we let Alice throw the dart with probability $p$, and let Bob throw otherwise. What is the pdf of $X$ (your answer should be in terms of $p$)?

(d) Using the same premise as in part c, suppose you observe a dart on the board but don't know who threw it. Let $x$ be the dart's distance from the center. We would like to come up with a decision rule to determine whether Alice or Bob is more likely to have thrown the dart given your observation, $x$. Specifically, if we let $A$ be the event that Alice threw the dart and $B$ be the event that Bob threw, we want to guess $A$ if $P[A \mid X \in [x, x + dx]] > P[B \mid X \in [x, x + dx]]$ (what do these two probabilities have to sum up to?). For what values of $x$ would we guess $A$? (your answer should be in terms of $p$)
:::

::: {.problem #prob-mit1805s22-3-q4 origin="external" source="mit1805s22-3-q4"}
Two scoops
Boxes of Raisin Bran cereal are 30cm tall. Due to settling, boxes have a higher density of raisins at the bottom ($h = 0$) than at the top ($h = 30$). Suppose the density (in raisins per cm of height) is given by $f(h) = 40 - h$.

(a) How many raisins are in a box?

(b) Let $H$ be the height of a random raisin. Find and graph the pdf $g(h)$ of $H$.

(c) Find and graph the cdf $G(h)$ of $H$.

(d) What is the probability that a random raisin is in the bottom third of the box?
:::
