::: {.problem #prob-eecs126hw-2-q4 origin="external" source="eecs126hw-2-q4"}
**Borel-Cantelli & Strong Law.** In this problem, we walk through a proof of the strong law (assuming finite 4th moments) that relies only on basic probability. In class we covered the Borel-Cantelli lemma, which states that for events $(A_n)_{n=1}^{\infty}$, if $\sum_{n=1}^{\infty}P(A_n)<\infty$, then
$$P(A_n\text{ i.o.})=0,$$
where we define the event $\{A_n\text{ i.o.}\}=\cap_{n\ge1}\cup_{m\ge n}A_n$ as the event where infinitely many $A_n$ occur.

(a) Let $X_1,X_2,\dots$ be i.i.d. with $EX_i=0$ and $EX_i^4<\infty$ (and so we also have finite second and third moments). Let $S_n=X_1+\dots+X_n$, and compute $E[S_n^4]$. Write your answer in terms of the moments $E[X_i^2],E[X_i^3],E[X_i^4]$.

(b) Fix an $\epsilon>0$, and use Markov's inequality to show that, for any $n$,
$$P(|S_n/n|>\epsilon)\le O(n^{-2}).$$

(c) Finally, use Borel-Cantelli to conclude that $P(\lim_{n\to\infty}S_n/n=0)=1$. This a weaker (the full theorem assumes only finite first moments) form of the strong law of large numbers.
:::

::: {.problem #prob-eecs126hw-4-q3 origin="external" source="eecs126hw-4-q3"}
**Convergence in Probability.** Let $(X_n)_{n=1}^{\infty}$, be a sequence of i.i.d. random variables distributed uniformly in $[-1,1]$. Show that the following sequences $(Y_n)_{n=1}^{\infty}$ converge in probability to some limit.

(a) $Y_n=\prod_{i=1}^{n}X_i$.

(b) $Y_n=\max\{X_1,X_2,\dots,X_n\}$.

(c) $Y_n=(X_1^2+\dots+X_n^2)/n$.
:::

::: {.problem #prob-eecs126hw-4-q4 origin="external" source="eecs126hw-4-q4"}
**Gambling Game.** Let's play a game. You stake a positive initial amount of money $w_0$. You toss a fair coin. If it is heads you earn an amount equal to three times your stake, so you quadruple your wealth. If it comes up tails you lose everything. There is one requirement though, you are not allowed to quit and have to keep playing, by staking all your available wealth, over and over again. Let $W_n$ be a random variable which is equal to your wealth after $n$ plays.

(a) Find $E[W_n]$ and show that $\lim_{n\to\infty}E[W_n]=\infty$.

(b) Since $\lim_{n\to\infty}E[W_n]=\infty$, this game sounds like a good deal! But wait a moment!! Where does the sequence of random variables $\{W_n\}_{n\ge0}$ converge almost surely (i.e. with probability 1) to?
:::

::: {.problem #prob-eecs126hw-6-q1 origin="external" source="eecs126hw-6-q1"}
**The CLT Implies the WLLN.**

(a) Let $\{X_n\}_{n\in\mathbb N}$ be a sequence of random variables. Show that if $X_n\xrightarrow{d}c$, where $c$ is a constant, then $X_n\xrightarrow{P}c$.

(b) Let $\{X_n\}_{n\in\mathbb N}$ be a sequence of i.i.d. random variables, with mean $\mu$ and finite variance $\sigma^2$. Show that the CLT implies the WLLN, i.e. if
$$\frac{1}{\sigma\sqrt n}\sum_{i=1}^{n}(X_i-\mu)\xrightarrow{d}N(0,1),$$
then
$$\frac1n\sum_{i=1}^{n}X_i\xrightarrow{P}\mu.$$
:::

::: {.problem #prob-eecs126d-4-q3 origin="external" source="eecs126d-4-q3"}
**More Almost Sure Convergence.**

(a) Suppose that, with probability 1, the sequence $(X_n)_{n\in\mathbb N}$ oscillates between two values $a\ne b$ infinitely often. Is this enough to prove that $(X_n)_{n\in\mathbb N}$ does not converge almost surely? Justify your answer.

(b) Suppose that $Y$ is uniform on $[-1,1]$, and $X_n$ has distribution
$$P\bigl(X_n=(y+n^{-1})^{-1}\mid Y=y\bigr)=1.$$
Does $(X_n)_{n=1}^{\infty}$ converge a.s.?

(c) Define random variables $(X_n)_{n\in\mathbb N}$ in the following way: first, set each $X_n$ to $0$. Then, for each $k\in\mathbb N$, pick $j$ uniformly randomly in $\{2^k,\dots,2^{k+1}-1\}$ and set $X_j=2^k$. Does the sequence $(X_n)_{n\in\mathbb N}$ converge a.s.?

(d) Does the sequence $(X_n)_{n\in\mathbb N}$ from the previous part converge in probability to some $X$? If so, is it true that $E[X_n]\to E[X]$ as $n\to\infty$?
:::

::: {.problem #prob-eecs126d-5-q1 origin="external" source="eecs126d-5-q1"}
**Curse of Dimensionality.** In this problem, we will use the law of large numbers to illustrate a statistical phenomenon. In particular, consider the hypercube $[-1,1]^n$ in $\mathbb R^n$, and let $X_1,\dots,X_n$ be iid $\text{Uniform}([-1,1])$.

(a) For $\epsilon>0$ consider the set
$$A_{n,\epsilon}:=\Bigl\{x\in\mathbb R^n:(1-\epsilon)\sqrt{n/3}<\|x\|_2<(1+\epsilon)\sqrt{n/3}\Bigr\},$$
which is the $\epsilon$-boundary of a ball with radius $\sqrt{n/3}$ centered at the origin. For low dimensions $n=1,2$ and $\epsilon=1/10$, compute the fraction of volume of $[-1,1]^n$ which comes from $A_{n,\epsilon}$.

(b) Show that as $n$ gets large, most of the volume of the hypercube comes from $A_{n,\epsilon}$. Comment on why this contradicts the intuition developed in part (a).
:::

::: {.problem #prob-eecs126d-6-q1 origin="external" source="eecs126d-6-q1"}
**Finite Boundary Times.** Consider the random walk $S_n=\sum_{i=1}^{n}X_i$, where the $X_i$ are iid with mean zero and variance 1 (note that they do not have to be discrete). Show that almost surely the random walk will leave the interval $[-a,a]$ in finite time.

Hint: Let $T$ be the first time that the walk leaves the interval $[-a,a]$, and show that $\lim_{n\to\infty}P(T>n)=0$.
:::

::: {.problem #prob-mit6041f10-9-q1 origin="external" source="mit6041f10-9-q1"}
Random variable $X$ is uniformly distributed between $-1.0$ and $1.0$. Let $X_1, X_2, \ldots$, be independent identically distributed random variables with the same distribution as $X$. Determine which, if any, of the following sequences (all with $i = 1, 2, \ldots$) are convergent in probability. Fully justify your answers. Include the limits if they exist.

(a) $U_i = \dfrac{X_1 + X_2 + \ldots + X_i}{i}$
(b) $W_i = \max(X_1, \ldots, X_i)$
(c) $V_i = X_1 \cdot X_2 \cdot \ldots \cdot X_i$
:::

::: {.problem #prob-mit18650f16-1-q1 origin="external" source="mit18650f16-1-q1"}
Convergence of random variables

1. For $n\in\mathbb{N}^*$, let $X_n$ be a random variable such that $\mathbb{P}\bigl[X_n=\frac1n\bigr]=1-\frac1{n^2}$ and $\mathbb{P}[X_n=n]=\frac1{n^2}$. Does $X_n$ converge in probability? In $L^2$?

2. Let $(X_n)_{n\in\mathbb{N}^*}$ be a sequence of i.i.d. Bernoulli random variables with parameter $p\in[0,1]$. For $n\in\mathbb{N}^*$, let $\bar X_n=\frac1n\sum_{i=1}^nX_i$.

   a) What is the distribution of $n\bar X_n$?

   b) Prove that $\bar X_n$ converges to $p$ in $L^2$?

3. For $n\in\mathbb{N}^*$, let $X_n$ be a Poisson random variable with parameter $1/n$.

   a) Prove that $X_n\xrightarrow[n\to\infty]{\mathbb{P}}0$.

   b) Prove that $nX_n\xrightarrow[n\to\infty]{\mathbb{P}}0$.
:::

::: {.problem #prob-mit18650f16-1-q2 origin="external" source="mit18650f16-1-q2"}
True or false

For each of the following statement, say whether it is true or false. When your answer is "false", give a counter example.

1. If $X_n\xrightarrow[n\to\infty]{a.s.}X$ and $Y_n\xrightarrow[n\to\infty]{a.s.}Y$, then $X_n+Y_n\xrightarrow[n\to\infty]{a.s.}X+Y$.

2. If $X_n\xrightarrow[n\to\infty]{\mathbb{P}}X$ and $Y_n\xrightarrow[n\to\infty]{\mathbb{P}}Y$, then $X_n+Y_n\xrightarrow[n\to\infty]{\mathbb{P}}X+Y$.

3. If $X_n\xrightarrow[n\to\infty]{(d)}X$ and $Y_n\xrightarrow[n\to\infty]{(d)}Y$, then $X_n+Y_n\xrightarrow[n\to\infty]{(d)}X+Y$.

4. Consider a coin that shows Heads with some unknown probability $p$ when it is tossed. After tossing this coin 100 times, Heads have shown up 43 times. The unknown parameter $p$ is contained in the interval $[.33,.53]$ with probability 95%.
:::
