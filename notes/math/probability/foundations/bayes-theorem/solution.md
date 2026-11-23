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

::: {.solution for="prob-eecs126hw-1-q3" status="draft"}
1. $\Pr(B_i)=1/N$. If $i\le m$ the best city is rejected. If $i>m$, the best city is chosen iff no city among positions $m+1,\dots,i-1$ beats all earlier ones, i.e. iff the best of the first $i-1$ cities is among the first $m$, which has probability $m/(i-1)$.
2. By the law of total probability (@thm-law-of-total-probability),
$$\Pr(A)=\sum_{i=m+1}^{N}\frac1N\cdot\frac{m}{i-1}=\frac mN\sum_{j=m}^{N-1}\frac1j\approx\frac mN\ln\frac Nm.$$
3. With $x=m/N$, $x\ln(1/x)$ has derivative $\ln(1/x)-1$, zero at $x=1/e$. So $m\approx N/e$, and the success probability is about $1/e\approx0.37$.
:::

::: {.solution for="prob-eecs126hw-2-q1" status="draft"}
The answer is $\tfrac34$.

1. You are a crewmate, so the captain is one of the other $8$ players: $4$ imposters and $4$ crewmates, prior $\Pr(I)=\tfrac12$.
2. Of the $\binom{17}{3}=680$ hands, $\binom{11}3=165$ have three sabotage cards and $\binom{11}2\cdot6=330$ have exactly two.
3. An imposter passes two sabotage cards whenever he holds at least two, $\Pr(2S\mid I)=\frac{495}{680}$; a crewmate does so only with three, $\Pr(2S\mid C)=\frac{165}{680}$.
4. By Bayes' theorem (@thm-bayes-two-events), $\Pr(I\mid2S)=\frac{495}{495+165}=\frac34$.
:::

::: {.solution for="prob-mit6041f10-2-q1" status="draft"}
Let $F$ be "forecast is rain", $R$ "it rains", $M$ "Victor misses the forecast", $U$ "he carries an umbrella", and $f=\Pr(F)$: $0.7$ in winter, $0.2$ in summer. Missing the forecast is independent of the weather and the forecast.

(a) Missing the forecast tells nothing, so by Bayes' theorem
$$\Pr(F\mid R)=\frac{0.8f}{0.8f+0.1(1-f)}.$$
Winter: $\frac{0.56}{0.59}\approx0.949$. Summer: $\frac{0.16}{0.24}=\frac23$.

(b) Given forecast "no rain", he carries an umbrella only if he missed the forecast and the coin said so: $\Pr(U\mid F^c)=0.2\cdot0.5=0.1$. Overall $\Pr(U)=0.1+0.8f$, which is $0.66$ in winter and $0.26$ in summer. Since $\Pr(U\mid F^c)\ne\Pr(U)$ in both seasons, the events are dependent in every season (they would be independent only if $f=0$).

(c) Split $U\cap R^c$ on $M$:

1. Saw the forecast: he carries only if it said rain, and then it stays dry with probability $0.2$: $\Pr(M^c\cap U\cap R^c)=0.8\cdot f\cdot0.2$.
2. Missed it: $\Pr(M\cap U\cap R^c)=0.2\cdot0.5\cdot\Pr(R^c)$ with $\Pr(R^c)=0.2f+0.9(1-f)$.
3. Winter: $0.112$ and $0.1\cdot0.41=0.041$, so $\Pr(M^c\mid U\cap R^c)=\frac{0.112}{0.153}\approx0.732$. Summer: $0.032$ and $0.1\cdot0.76=0.076$, so $\frac{0.032}{0.108}\approx0.296$.

It depends on the season.
:::

::: {.solution for="prob-mit6041f10-2-q3" status="draft"}
There are $75$ defective old widgets out of $500$ and $75$ defective new ones out of $1500$; two widgets are drawn without replacement.

(a) $\Pr(\text{both defective}\mid\text{old})=\frac{75}{500}\cdot\frac{74}{499}\approx0.02224$ and $\Pr(\text{both defective}\mid\text{new})=\frac{75}{1500}\cdot\frac{74}{1499}\approx0.002468$. By total probability the answer is $\frac12(0.02224+0.002468)\approx0.01236$. (Drawing with replacement would give $\frac12(0.15^2+0.05^2)=0.0125$, nearly the same.)

(b) By Bayes' theorem, $\Pr(\text{old}\mid\text{both defective})=\frac{0.02224}{0.02224+0.002468}\approx0.900$.
:::

::: {.solution for="prob-mit6041f10-2-q4" status="draft"}
(a) Looking in A finds the dog with probability $0.4\cdot0.25=0.1$, looking in B with probability $0.6\cdot0.15=0.09$. Look in A.

(b) $\Pr(\text{in }A\mid\text{not found in }A)=\frac{0.4\cdot0.75}{0.4\cdot0.75+0.6\cdot1}=\frac{0.3}{0.9}=\frac13$.

(c) $\Pr(\text{looked in }A\mid\text{found})=\frac{0.5\cdot0.1}{0.5\cdot0.1+0.5\cdot0.09}=\frac{10}{19}\approx0.526$.

(d) He must have: the dog in A ($0.4$), no find on day 1 ($0.75$), the dog surviving the first evening ($1-\frac13=\frac23$), and a find on day 2 ($0.25$). The product is $0.4\cdot0.75\cdot\frac23\cdot0.25=0.05$.
:::

::: {.solution for="prob-mit1805s22-2-q2" status="draft"}
A speech built on a table of $10{,}000$ imagined nights like the one in question:

| | witness says "blue" | witness says "green" | total |
|---|---|---|---|
| the taxi really was blue | $99$ | $1$ | $100$ |
| the taxi really was green | $198$ | $9702$ | $9900$ |

"Ladies and gentlemen, there is one blue taxi in this city and ninety-nine green ones. Out of $10{,}000$ such accidents, about $100$ involve the blue taxi, and the witness would call $99$ of them blue. But $9900$ involve green taxis, and even a witness who errs only $2\%$ of the time would call $198$ of those blue. So of all the times this witness says 'blue', only $99$ out of $297$ — one in three — really were blue. Two times out of three the taxi was green. That is not proof beyond reasonable doubt."

By Bayes' theorem, $P(\text{blue}\mid\text{says blue})=\frac{0.01\cdot0.99}{0.01\cdot0.99+0.99\cdot0.02}=\frac13$.
:::

::: {.solution for="prob-mit1805s22-2-q4" status="draft"}
(a) $p_S(4)=\frac14$, $p_S(6)=\frac14$, $p_S(8)=\frac12$.

(b) The likelihoods of $R=3$ are $\frac14,\frac16,\frac18$. The Bayes numerators are $\frac1{16},\frac1{24},\frac1{16}$ with total $\frac16$, so
$$P(S=4\mid R=3)=\tfrac38,\quad P(S=6\mid R=3)=\tfrac14,\quad P(S=8\mid R=3)=\tfrac38.$$
The D4 and the D8 are equally most likely.

(c) $R=6$ rules out the D4. The numerators for D6 and D8 are $\frac1{24}$ and $\frac1{16}$, giving posteriors $\frac25$ and $\frac35$: the D8 is most likely.

(d) Only the D8 can show $7$, so its posterior probability is $1$.
:::
