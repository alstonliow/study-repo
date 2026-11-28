::: {.problem #prob-mit6042f10-12-q3 origin="external" source="mit6042f10-12-q3"}
MIT students sometimes delay laundry for a few days (to the chagrin of their roommates). Assume all random variables described below are mutually independent.

(a) A busy student must complete 3 problem sets before doing laundry. Each problem set requires 1 day with probability 2/3 and 2 days with probability 1/3. Let $B$ be the number of days a busy student delays laundry. What is $E[B]$?

Example: If the first problem set requires 1 day and the second and third problem sets each require 2 days, then the student delays for $B = 5$ days.

(b) A relaxed student rolls a fair, 6-sided die in the morning. If he rolls a 1, then he does his laundry immediately (with zero days of delay). Otherwise, he delays for one day and repeats the experiment the following morning. Let $R$ be the number of days a relaxed student delays laundry. What is $E[R]$?

Example: If the student rolls a 2 the first morning, a 5 the second morning, and a 1 the third morning, then he delays for $R = 2$ days.

(c) Before doing laundry, an unlucky student must recover from illness for a number of days equal to the product of the numbers rolled on two fair, 6-sided dice. Let $U$ be the expected number of days an unlucky student delays laundry. What is $E[U]$?

Example: If the rolls are 5 and 3, then the student delays for $U = 15$ days.

(d) A student is busy with probability 1/2, relaxed with probability 1/3, and unlucky with probability 1/6. Let $D$ be the number of days the student delays laundry. What is $E[D]$?
:::

::: {.problem #prob-mit6042f10-12-q5 origin="external" source="mit6042f10-12-q5"}
Each 6.042 final exam (out of 100 points) will be graded according to a rigorous procedure:

- With probability $\frac47$ the exam is graded by a TA; with probability $\frac27$ it is graded by a lecturer; and with probability $\frac17$, it is accidentally dropped behind the radiator and arbitrarily given a score of 84.
- TAs score an exam by scoring each problem individually and then taking the sum.
  - There are ten true/false questions worth 2 points each. For each, full credit is given with probability 3/4, and no credit is given with probability 1/4.
  - There are four questions worth 15 points each. For each, the score is determined by rolling two fair dice, summing the results, and adding 3.
  - The single 20 point question is awarded either 12 or 18 points with equal probability.
- Lecturers score an exam by rolling a fair die twice, multiplying the results, and then adding a "general impression" score.
  - With probability $\frac4{10}$, the general impression score is 40.
  - With probability $\frac3{10}$, the general impression score is 50.
  - With probability $\frac3{10}$, the general impression score is 60.

Assume all random choices during the grading process are independent.

(a) What is the expected score on an exam graded by a TA?

(b) What is the expected score on an exam graded by a lecturer?

(c) What is the expected score on a 6.042 final exam?
:::

::: {.problem #prob-mit6041f10-4-q1 origin="external" source="mit6041f10-4-q1"}
Random variables $X$ and $Y$ have the joint PMF
$$p_{X,Y}(x,y) = \begin{cases} c(x^2 + y^2), & \text{if } x \in \{1, 2, 4\} \text{ and } y \in \{1, 3\},\\ 0, & \text{otherwise.}\end{cases}$$

(a) What is the value of the constant $c$?
(b) What is $\mathbf{P}(Y < X)$?
(c) What is $\mathbf{P}(Y > X)$?
(d) What is $\mathbf{P}(Y = X)$?
(e) What is $\mathbf{P}(Y = 3)$?
(f) Find the marginal PMFs $p_X(x)$ and $p_Y(y)$.
(g) Find the expectations $\mathbf{E}[X]$, $\mathbf{E}[Y]$ and $\mathbf{E}[XY]$.
(h) Find the variances $\mathrm{var}(X)$, $\mathrm{var}(Y)$ and $\mathrm{var}(X + Y)$.
(i) Let $A$ denote the event $X \geq Y$. Find $\mathbf{E}[X \mid A]$ and $\mathrm{var}(X \mid A)$.
:::

::: {.problem #prob-mit1805s22-2-q3 origin="external" source="mit1805s22-2-q3"}
(Trees of cards) There are 8 cards in a hat:

$$\{1\heartsuit, 1\spadesuit, 1\diamondsuit, 1\clubsuit, 2\heartsuit, 2\spadesuit, 2\diamondsuit, 2\clubsuit\}$$

You draw one card at random. If its rank is 1 you draw one more card; if its rank is two you draw two more cards. Let $X$ be the sum of the ranks on the 2 or 3 cards drawn. Find $E[X]$. (Note: all the draws are done without replacement.)
:::
