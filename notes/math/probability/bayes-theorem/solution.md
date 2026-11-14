<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-probability-1-16" status="draft"}
Each of the four fielders is equally likely, with probability $\frac14$.

(a) By the law of total probability,
    $$\Pr(\text{caught}) = \tfrac14\cdot0.9 + \tfrac34\cdot0.4 = 0.225 + 0.3 = 0.525.$$

(b) By Bayes' Theorem,
    $$\Pr(\text{Alex}\mid\text{caught}) = \frac{0.9\cdot\frac14}{0.525} = \frac{0.225}{0.525} = \frac37\approx 0.43,$$
    and $\Pr(\text{not Alex}\mid\text{caught}) = \frac47\approx 0.57$.

    Seeing the catch raises the probability that it was Alex from $\frac14$
    to $\frac37$.
:::

::: {.solution for="prob-probability-1-17" status="draft"}
Let $M = 10^6$. Treat each of the $5M$ people as equally likely to be the
criminal, so $\Pr(\text{Guilty}) = \frac1{5M}$ for the matched person. The
criminal certainly matches, and an innocent person matches with probability
$\frac1M$.

1. By the law of total probability,
   $$\Pr(\text{Match}) = 1\cdot\frac1{5M} + \frac1M\cdot\frac{5M-1}{5M} = \frac{6M-1}{5M^2}.$$

2. By Bayes' Theorem,
   $$\Pr(\text{Guilty}\mid\text{Match}) = \frac{1\cdot\frac1{5M}}{\frac{6M-1}{5M^2}} = \frac{M}{6M-1}\approx\frac16.$$

3. So the matched person is guilty with probability only about $17\%$. That
   is far from "beyond reasonable doubt".

4. The intuition: among $5$ million people, about $5$ innocent people are
   expected to match by chance, in addition to the criminal. The database
   search found one of about six people who match, with no other evidence to
   tell them apart.
:::

::: {.solution for="prob-probability-1-18" status="draft"}
In every case the prior is $\frac13$ for each coin. Given the coin, the
tosses are independent:

| coin | $\Pr(\mathrm{HH})$ | $\Pr(\mathrm{TT})$ | $\Pr(\mathrm{HT})$ |
|---|---|---|---|
| Fair | $\frac14$ | $\frac14$ | $\frac14$ |
| DoubleHead | $1$ | $0$ | $0$ |
| DoubleTail | $0$ | $1$ | $0$ |

(a) $\Pr(\mathrm{HH}) = \frac13\bigl(\frac14+1+0\bigr) = \frac5{12}$. Posteriors:
    $$\text{Fair: }\frac{\frac13\cdot\frac14}{\frac5{12}} = \frac15,\qquad
      \text{DoubleHead: }\frac{\frac13\cdot1}{\frac5{12}} = \frac45,\qquad
      \text{DoubleTail: }0.$$

(b) By symmetry: Fair $\frac15$, DoubleHead $0$, DoubleTail $\frac45$.

(c) Only the fair coin can give one Head and one Tail:
    $\Pr(\mathrm{HT}) = \frac13\cdot\frac14 = \frac1{12}$, and the posteriors are
    Fair $1$, DoubleHead $0$, DoubleTail $0$.

Compared with one toss (posterior $\frac13$ for Fair after a Head), a second
Head lowers belief in Fair further, from $\frac13$ to $\frac15$.
:::
