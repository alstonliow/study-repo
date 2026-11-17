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

::: {.solution for="prob-cs70-14-q2"}
<!-- TODO: solution -->
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-10-q2" status="draft"}
Let $G$ be "guilty" and $T$ "the test says guilty". Then $\Pr(G)=\frac1{100}$, $\Pr(T\mid G)=\frac45$ and $\Pr(T\mid\overline G)=1-\frac9{10}=\frac1{10}$. By Bayes' theorem (@thm-bayes-two-events),
$$\Pr(G\mid T)=\frac{\frac1{100}\cdot\frac45}{\frac1{100}\cdot\frac45+\frac{99}{100}\cdot\frac1{10}}=\frac{0.008}{0.008+0.099}=\frac8{107}\approx0.075.$$
Most positive tests come from the many innocent suspects.
:::

::: {.solution for="prob-mit6042f10-11-q2" status="draft"}
(a) First level: who has the opportunity (Plum $\frac16$, Green $\frac26$, Scarlet $\frac36$); second level, below each: who has the revolver ($\frac48,\frac38,\frac18$). The $9$ outcomes have the product probabilities, for example (Green, Plum) has $\frac26\cdot\frac48=\frac8{48}$. Mustard is shot in the three outcomes where the same person has both.

(b) $\Pr(\text{shot})=\frac16\cdot\frac48+\frac26\cdot\frac38+\frac36\cdot\frac18=\frac{4+6+3}{48}=\frac{13}{48}$.

(c) Given that Scarlet does not have the revolver, it is with Plum or Green with probabilities $\frac47$ and $\frac37$, still independent of the opportunity. So $\Pr=\frac16\cdot\frac47+\frac26\cdot\frac37=\frac{10}{42}=\frac5{21}$.

(d) By Bayes' theorem (@thm-bayes-two-events), $\Pr(\text{Green opportunity}\mid\text{shot})=\frac{(2/6)(3/8)}{13/48}=\frac{6/48}{13/48}=\frac6{13}$.
:::
