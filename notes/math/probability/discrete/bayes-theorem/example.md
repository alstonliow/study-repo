<!-- Adapted (own wording) from UC Berkeley CS 70, Fall 2020, Note 14, §2 and §3.1 (source keys cs70-14.2, cs70-14.3.1, in note.md). -->

::: {#exm-medical-test .example name="A medical test" level="medium"}
A test for a disorder is positive for $90\%$ of affected people and for $20\%$ of healthy people (false positives). $5\%$ of the population is affected. A random person tests positive: how likely is it that they are affected?

Let $A$ be "affected" and $B$ "tests positive". Then $\Pr(A)=0.05$, $\Pr(B\mid A)=0.9$ and $\Pr(B\mid\overline A)=0.2$.

1. By @thm-law-of-total-probability, $\Pr(B)=0.9\cdot0.05+0.2\cdot0.95=0.235$.

2. By @thm-bayes-two-events,
   $$\Pr(A\mid B)=\frac{0.9\cdot0.05}{0.235}=\frac9{47}\approx0.19.$$

So a positive result raises the probability from the prior $0.05$ to the posterior $0.19$, but most people who test positive are still healthy, because healthy people are so much more common.
:::

::: {#exm-tennis-opponent .example name="An unknown opponent" level="easy"}
Your tennis opponent is $X$ with probability $0.6$ and $Y$ with probability $0.4$. You beat $X$ with probability $0.7$ and $Y$ with probability $0.3$. By @thm-law-of-total-probability,
$$\Pr(\text{win})=0.7\cdot0.6+0.3\cdot0.4=0.54.$$
:::

::: {#exm-two-bins-white-ball .example name="Which bin was it?" level="medium"}
Bin $1$ holds $2$ white and $3$ black balls; bin $2$ holds $1$ white and $1$ black ball. A bin is chosen at random and a ball drawn from it at random. The ball is white: what is the probability that it came from bin $1$?

1. $\Pr(\text{white})=\frac25\cdot\frac12+\frac12\cdot\frac12=\frac9{20}$ by @thm-law-of-total-probability.

2. By @thm-bayes-two-events, $\Pr(\text{bin }1\mid\text{white})=\dfrac{\frac25\cdot\frac12}{9/20}=\dfrac49$.

The tempting answer $\frac23$ (two of the three white balls are in bin $1$) is wrong: a white ball is less likely to be drawn from bin $1$, which has more balls.
:::
