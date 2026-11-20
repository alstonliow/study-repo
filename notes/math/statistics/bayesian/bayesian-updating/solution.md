<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1805s22-7-q1" status="draft"}
All priors are $\frac13$; $D$ = "Monty opens $B$ and shows a goat".

(a) Sober Monty: $P(D\mid H_A)=\frac12$ (he picks $B$ or $C$ at random), $P(D\mid H_B)=0$, $P(D\mid H_C)=1$ (he must avoid the car).

| | prior | likelihood | numerator | posterior |
|---|---|---|---|---|
| $H_A$ | $1/3$ | $1/2$ | $1/6$ | $1/3$ |
| $H_B$ | $1/3$ | $0$ | $0$ | $0$ |
| $H_C$ | $1/3$ | $1$ | $1/3$ | $2/3$ |

Switching wins with probability $\frac23$: switch.

(b) Drunk Monty opens $B$ with probability $\frac12$ whatever the hypothesis, and shows a goat unless the car is there: likelihoods $\frac12,0,\frac12$. The posterior is $\frac12,0,\frac12$, so staying and switching are equally good.

(c) By the law of total probability over Monty's state, the likelihoods are $P(D\mid H_A)=0.7\cdot\frac12+0.3\cdot\frac12=\frac12$, $P(D\mid H_B)=0$, $P(D\mid H_C)=0.7\cdot1+0.3\cdot\frac12=0.85$. The numerators are $\frac16,0,\frac{0.85}3$, so the posterior is $\frac{10}{27}\approx0.37$, $0$, $\frac{17}{27}\approx0.63$: still switch.
:::

::: {.solution for="prob-mit1805s22-7-q4" status="draft"}
(a) It is a trick. The lawyer's figure is $P(M\mid B)=\frac1{1000}$, the probability *before* we know Mrs S was killed. The relevant probability is $P(M\mid K,B)$. Conditioning on $B$ throughout, Bayes' theorem gives
$$P(M\mid K,B)=\frac{P(K\mid M,B)\,P(M\mid B)}{P(K\mid B)},$$
with $P(K\mid M,B)=1$ (if he murdered her she was killed) and $P(K\mid B)=P(M\mid B)+P(K\cap M^c\mid B)$. The second term is the chance she was killed by someone else, which is much smaller than $\frac1{1000}$; if it is, say, $\frac1{20000}$, then $P(M\mid K,B)=\frac{0.001}{0.001+0.00005}\approx0.95$. Given that she was murdered, a history of beating makes the husband a very likely culprit; the lawyer replaced the posterior by a prior.

(b) Two errors.

1. *Independence.* Squaring $\frac1{8543}$ assumes the two deaths are independent. Genetic and environmental factors make a second cot death in the same family far more likely than in a random family, so $1$ in $73$ million is much too small.

2. *Prosecutor's fallacy.* A small $P(\text{two deaths}\mid\text{innocent})$ is not a small $P(\text{innocent}\mid\text{two deaths})$. The data must be compared under both hypotheses: double murder of infants by a mother is itself extremely rare, possibly rarer than a double cot death, and Bayes' theorem weighs the two. Ignoring the alternative's small prior is the base rate fallacy (@exm-base-rate-fallacy).

(Also, "once every hundred years" in Britain is not "never": rare events do happen somewhere, and the existence of one such family is not evidence of guilt.)
:::
