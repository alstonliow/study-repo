<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1805s22-7-q2" status="draft"}
Write $H_s$ for the $s$-sided die; only $s=8,12,20$ can show a $7$.

(a) Prior predictive: $P(x_1=7)=\frac15\bigl(\frac18+\frac1{12}+\frac1{20}\bigr)=\frac{31}{600}\approx0.0517$. The Bayes numerators $\frac15\cdot\frac18,\frac15\cdot\frac1{12},\frac15\cdot\frac1{20}$ give posteriors $P(H_8)=\frac{15}{31}\approx0.484$, $P(H_{12})=\frac{10}{31}\approx0.323$, $P(H_{20})=\frac6{31}\approx0.194$, and $0$ for $H_4,H_6$. Posterior predictive (@prp-posterior-predictive): $P(x_2=7\mid x_1=7)=\frac{15}{31}\cdot\frac18+\frac{10}{31}\cdot\frac1{12}+\frac6{31}\cdot\frac1{20}\approx0.0970$.

(b) The likelihood of $n$ sevens is $s^{-n}$ for $s\ge8$, so with $T_n=8^{-n}+12^{-n}+20^{-n}$,
$$P(H_8\mid\text{data})=\frac{8^{-n}}{T_n},\quad P(H_{12}\mid\text{data})=\frac{12^{-n}}{T_n},\quad P(H_{20}\mid\text{data})=\frac{20^{-n}}{T_n}.$$
Dividing by $8^{-n}$ shows the limits are $1,0,0$: the D8 makes a long run of sevens far more likely than the bigger dice do.

(c) Every die that can show a value shows it with probability $1/s$. Values $1$–$8$ are possible on all three remaining dice, $9$–$12$ only on the D12 and D20, $13$–$20$ only on the D20. So $1,\dots,8$ are tied as most likely, then $9,\dots,12$ tied, then $13,\dots,20$ tied as least likely.

(d) With the posteriors $p_8,p_{12},p_{20}$ of (b),
$$P(x_{n+1}=k\mid\text{data})=\begin{cases}\frac{p_8}8+\frac{p_{12}}{12}+\frac{p_{20}}{20},&1\le k\le8,\\[2pt]\frac{p_{12}}{12}+\frac{p_{20}}{20},&9\le k\le12,\\[2pt]\frac{p_{20}}{20},&13\le k\le20.\end{cases}$$
For $n=10$ these are about $0.1243$, $0.00143$ and $5.2\times10^{-6}$, consistent with (c).

(e) As $n\to\infty$, $p_8\to1$, so the pmf tends to $\frac18$ on $1,\dots,8$ and $0$ elsewhere: we become sure the die is the D8, and predict as for that die.
:::

::: {.solution for="prob-mit1805s22-7-q3" status="draft"}
(a) $P(0.3\text{ coin})=0.2$, so the odds are $0.2/0.8=\frac14$; the same for a $0.7$ coin.

(b) $P(H)=0.2\cdot0.3+0.6\cdot0.5+0.2\cdot0.7=0.5$, so the odds of heads are $1$.

(c) The Bayes numerators are $0.06$, $0.30$, $0.14$ (total $0.5$), so the posterior is $0.12,0.60,0.28$.
(i) Odds of a $0.3$ coin: $0.12/0.88=\frac3{22}\approx0.136$. (ii) Odds of a $0.7$ coin: $0.28/0.72=\frac7{18}\approx0.389$.
Check with @thm-odds-form-of-bayes for (ii): the Bayes factor is $0.7/P(H\mid\text{not }0.7)=0.7/\frac{0.06+0.30}{0.8}=\frac{14}9$, and $\frac{14}9\cdot\frac14=\frac7{18}$.

(d) $P(\text{second }H\mid\text{first }H)=0.12\cdot0.3+0.6\cdot0.5+0.28\cdot0.7=0.532$, so the odds are $0.532/0.468\approx1.137$.
:::

::: {.solution for="prob-mit1805s22-7-q5" status="draft"}
1. Treat the hourly counts as independent given the collector. The likelihood of the data under rate $\lambda$ is $\prod_i\frac{\lambda^{k_i}}{k_i!}e^{-\lambda}$, with $\sum k_i=48$ over $5$ hours.

2. The factorials cancel in the Bayes factor:
$$\mathrm{BF}=\frac{10^{48}e^{-50}}{15^{48}e^{-75}}=\Bigl(\frac23\Bigr)^{48}e^{25}\approx254.1 .$$

3. By @thm-odds-form-of-bayes the posterior odds are $254.1\cdot\frac1{10}\approx25.4$: Oscar is very probably filling in (probability $\approx0.96$).
:::

::: {.solution for="prob-mit1805s22-7-q7" status="draft"}
(a) Let $H$ = "4-sided die". The Bayes factor of a reported $1$ is $\frac{1/4}{1/6}=\frac32$, of a reported $0$ is $\frac{3/4}{5/6}=\frac9{10}$. Starting from odds $1$ and multiplying (@cor-log-odds):
$$1\cdot\tfrac32=1.5,\quad1.5\cdot0.9=1.35,\quad2.025,\quad3.0375,\quad4.556 .$$

(b) A $1$ has Bayes factor above $1$, so it is evidence for the 4-sided die; a $0$ has Bayes factor below $1$, weak evidence for the 6-sided die. In (a) the odds rise after every $1$ and fall (only slightly, since $0.9$ is close to $1$) after the $0$.
:::
