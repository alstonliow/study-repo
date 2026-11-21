<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-probability-2-05 origin="external" source="fit1058-cn-10.12-q5"}
Define the random variable $W$ by

| $k$ | $\Pr(W=k)$ |
|:---:|:----------:|
|  0  | $\frac12$  |
|  1  | $\frac13$  |
|  2  | $\frac16$  |

Determine the expectation, median, mode, variance and standard deviation of
$W$.
:::

::: {.problem #prob-probability-2-06 origin="external" source="fit1058-cn-10.12-q6"}
Find the variance of the sum of the numbers shown on two fair dice. What is
the probability that this sum is at least two standard deviations away from
its mean? Compare with what Chebyshev’s Inequality says.
:::

::: {.problem #prob-mit6042f10-12-q1 origin="external" source="mit6042f10-12-q1"}
In this problem, we will (hopefully) be making tons of money! Use your knowledge of probability and statistics to keep from going broke!

Suppose the stock market contains $N$ types of stocks, which can be modelled by independent random variables. Suppose furthermore that the behavior of these stocks is modelled by a double-or-nothing coin flip. That is, stock $S_i$ has half probability of doubling its value and half probability of going to 0. The stocks all cost a dollar, and you have $N$ dollars. Say you only keep these stocks for one time-step (that is, at the end of this timestep, all stocks would have doubled in value or gone to 0).

(a) What is your expected amount of money if you spend all your money on one stock? Your variance?

(b) Suppose instead you diversified your purchases and bought $N$ shares of all different stocks. What is your expected amount of money then? Your variance?

(c) The money that you have invested came from your financially conservative mother. As a result, your goals are much aligned with hers. Given this, which investment strategy should you take?

(d) Now instead say that you make money on rolls of dice. Specifically, you play a game where you roll a standard six-sided dice, and get paid an amount (in dollars) equal to the number that comes up. What is your expected payoff? What is the variance?

(e) We change the rules of the game so that your payoff is the cube of the number that comes up. In that case, what is your expected payoff? What is its variance?
:::

::: {.problem #prob-mit6006s20-0-q2 origin="external" source="mit6006s20-0-q2"}
Let $X$ be the random variable representing the number of heads seen after flipping a fair coin three times. Let $Y$ be the random variable representing the outcome of rolling two fair six-sided dice and multiplying their values. Please compute the following expected values.

Evaluate: (a) $\mathrm E[X]$ (b) $\mathrm E[Y]$ (c) $\mathrm E[X+Y]$
:::

::: {.problem #prob-mit6041f10-3-q3 origin="external" source="mit6041f10-3-q3"}
(a) Let $X$ be a random variable that takes nonnegative integer values. Show that
$$\mathbf{E}[X] = \sum_{k=1}^{\infty} \mathbf{P}(X \geq k).$$
Hint: Express the right-hand side of the above formula as a double summation then interchange the order of the summations.
(b) Use the formula in the previous part to find the expectation of a random variable $Y$ whose PMF is defined as follows:
$$p_Y(y) = \frac{1}{b-a+1}, \qquad y = a, a+1, \ldots, b$$
where $a$ and $b$ are nonnegative integers with $b > a$. Note that for $y = a, a+1, \ldots, b$, $p_Y(y)$ does not depend explicitly on $y$ since it is a uniform PMF.
:::

::: {.problem #prob-mit1805s22-3-q3 origin="external" source="mit1805s22-3-q3"}
Dice
Let $X$ be the result of rolling a fair 4-sided die. Let $Y$ be the result of rolling a fair 6-sided die. Let $Z$ be the average of $X$ and $Y$.

(a) Find the standard deviation of $X$, of $Y$, and of $Z$.

(b) Carefully graph the pmf and cdf of $Z$.

(c) Here is a gambling game: You win $2X$ dollars if $X > Y$ and lose 1 dollar otherwise. After playing this game 60 times, what is your expected total gain (positive) or loss (negative)?
:::

::: {.problem #prob-mit18065ps-19-q8 origin="external" source="mit18065ps-19-q8"}
Equation (4) gave a second equivalent form for $S^2$ (the variance using samples):
$$S^2=\frac1{N-1}\text{ sum of }(x_i-m)^2=\frac1{N-1}\Big[\big(\text{sum of }x_i^2\big)-Nm^2\Big].$$
Verify the matching identity for the expected variance $\sigma^2$ (using $m=\Sigma p_ix_i$) :
$$\sigma^2=\text{ sum of }p_i(x_i-m)^2=\big(\text{sum of }p_ix_i^2\big)-m^2 .$$
:::

::: {.problem #prob-mit18065ps-20-q12 origin="external" source="mit18065ps-20-q12"}
For any function $f(x)$ the expected value is $\mathrm{E}[f]=\sum p_i\,f(x_i)$ or $\int p(x)\,f(x)\,dx$ (discrete or continuous probability). The function can be $x$ or $(x-m)^2$ or $x^2$.

If the mean is $\mathrm{E}[x]=m$ and the variance is $\mathrm{E}[(x-m)^2]=\sigma^2$ what is $\mathrm{E}[x^2]$ ?
:::
