::: {.problem #prob-cs70hw-14-q2 origin="external" source="cs70hw-14-q2"}
**Continuous Probability Continued.** For the following questions, please briefly justify your answers or show your work.

(a) Assume $\mathrm{Bob}_1, \mathrm{Bob}_2, \ldots, \mathrm{Bob}_k$ each hold a fair coin whose two sides show numbers instead of heads and tails, with the numbers on $\mathrm{Bob}_i$'s coin being $i$ and $-i$. Each Bob tosses their coin $n$ times and sums up the numbers he sees; let's call this number $X_i$. For large $n$, what is the distribution of $(X_1 + \cdots + X_k)/\sqrt{n}$ approximately equal to?

(b) If $X_1, X_2, \ldots$ is a sequence of i.i.d. random variables of mean $\mu$ and variance $\sigma^2$, what is $\lim_{n\to\infty} \mathbb{P}\left[\sum_{k=1}^{n} \frac{X_k - \mu}{\sigma n^\alpha} \in [-1, 1]\right]$ for $\alpha \in [0, 1]$ (your answer may depend on $\alpha$ and $\Phi$, the CDF of a $N(0, 1)$ variable)?
:::

::: {.problem #prob-mit6041f10-10-q1 origin="external" source="mit6041f10-10-q1"}
A financial parable. An investment bank is managing \$1 billion, which it invests in various financial instruments ("assets") related to the housing market (e.g., the infamous "mortgage backed securities"). Because the bank is investing with borrowed money, its actual assets are only \$50 million (5%). Accordingly, if the bank loses more than 5%, it becomes insolvent. (Which means that it will have to be bailed out, and the bankers may need to forgo any huge bonuses for a few months.)

(a) The bank considers investing in a single asset, whose gain (over a 1-year period, and measured in percentage points) is modeled as a normal random variable $R$, with mean 7 and standard deviation 10. (That is, the asset is expected to yield a 7% profit.) What is the probability that the bank will become insolvent? Would you accept this level of risk?
(b) In order to safeguard its position, the bank decides to diversify its investments. It considers investing \$50 million in each of twenty different assets, with the $i$th one having a gain $R_i$, which is again normal with mean 7 and standard deviation 10; the bank's gain will be $(R_1 + \cdots + R_{20})/20$. These twenty assets are chosen to reflect the housing sectors at different states or even countries, and the bank's rocket scientists choose to model the $R_i$ as independent random variables. According to this model, what is the probability that the bank becomes insolvent?
(c) Based on the calculations in part (b), the bank goes ahead with the diversified investment strategy. It turns out that a global economic phenomenon can affect the housing sectors in different states and countries simultaneously, and therefore the gains $R_i$ are in fact positively correlated. Suppose that for every $i$ and $j$ where $i \neq j$, the correlation coefficient $\rho(R_i, R_j)$ is equal to $1/2$. What is the probability that the bank becomes insolvent? You can assume that $(R_1 + \cdots + R_{20})/20$ is normal.
:::

::: {.problem #prob-mit6041f10-10-q2 origin="external" source="mit6041f10-10-q2"}
The adult population of Nowhereville consists of 300 males and 196 females. Each male (respectively, female) has a probability of 0.4 (respectively, 0.5) of casting a vote in the local elections, independently of everyone else. Find a good numerical approximation for the probability that more males than females cast a vote.
:::

::: {.problem #prob-mit6041f10-10-q3 origin="external" source="mit6041f10-10-q3"}
Let $S_n$ be the number of successes in $n$ independent Bernoulli trials, where the probability of success in each trial is $p = \frac{1}{2}$. Provide a numerical value for the limit as $n$ tends to infinity for each of the following three expressions:

(a) $\mathbf{P}\left(\frac{n}{2} - 10 \leq S_n \leq \frac{n}{2} + 10\right)$
(b) $\mathbf{P}\left(\frac{n}{2} - \frac{n}{10} \leq S_n \leq \frac{n}{2} + \frac{n}{10}\right)$
(c) $\mathbf{P}\left(\frac{n}{2} - \frac{\sqrt{n}}{2} \leq S_n \leq \frac{n}{2} + \frac{\sqrt{n}}{2}\right)$
:::
