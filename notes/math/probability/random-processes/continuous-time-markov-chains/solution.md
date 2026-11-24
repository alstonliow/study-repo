<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-eecs126hw-8-q3" status="draft"}
(a) $X_t$ is a birth–death CTMC on $\{0,1,2,3\}$ with $q(i,i+1)=2(3-i)$ and $q(i,i-1)=i$. Balancing each cut, $\pi(i)\cdot2(3-i)=\pi(i+1)(i+1)$, gives $\pi(1)=6\pi(0)$, $\pi(2)=12\pi(0)$, $\pi(3)=8\pi(0)$, so
$$\pi=\Bigl(\frac1{27},\frac6{27},\frac{12}{27},\frac8{27}\Bigr).$$

(b) One frog alternates between sun (leaving at rate $1$) and lake (leaving at rate $2$); its stationary probability of being in the sun solves $\pi_{\text{sun}}\cdot1=\pi_{\text{lake}}\cdot2$, so it is $\frac23$. The frogs are independent, so in steady state $X\sim\text{Bin}(3,\frac23)$, and $\binom3i\bigl(\frac23\bigr)^i\bigl(\frac13\bigr)^{3-i}$ gives the same four numbers.
:::

::: {.solution for="prob-eecs126hw-8-q4" status="draft"}
The answer is $\frac{13}{15}$ minute.

1. The number waiting is a birth–death CTMC on $\{0,\dots,4\}$ with up-rate $1$ and down-rate $2$; balance gives $\pi(n)\propto2^{-n}$.
2. John arrives at a fixed time, so he sees the steady state; he joins iff fewer than four are waiting. Given that, $P(n\text{ ahead})\propto1,\frac12,\frac14,\frac18$ for $n=0,1,2,3$, total $\frac{15}8$.
3. With $n$ ahead he leaves with the $(n+1)$st taxi; taxi gaps are $\text{Exp}(2)$ (memoryless), so his mean wait is $\frac{n+1}2$.
4. $E[W]=\frac{8}{15}\cdot\frac12\bigl(1+2\cdot\frac12+3\cdot\frac14+4\cdot\frac18\bigr)=\frac{8}{15}\cdot\frac{13}{8}=\frac{13}{15}$.
:::

::: {.solution for="prob-eecs126hw-8-q5" status="draft"}
(a) Given $X(t)=n$, the future depends only on the time to the next arrival and the residual service times of the $\min(n,2)$ customers in service. All are exponential, hence memoryless and independent of the past, so the future given the present does not depend on the past.

(b) States $0,1,2,\dots$ in a line. Arrows $n\to n+1$ with rate $\lambda$ for all $n\ge0$; $1\to0$ with rate $\mu$; $n\to n-1$ with rate $2\mu$ for $n\ge2$ (two exponential services race, @prp-min-of-exponentials).

(c) Let $\rho=\frac{\lambda}{2\mu}$. Cut balance gives $\pi(1)=\frac{\lambda}{\mu}\pi(0)=2\rho\,\pi(0)$ and $\pi(n+1)=\rho\,\pi(n)$ for $n\ge1$, so $\pi(n)=2\rho^n\pi(0)$ for $n\ge1$. This is normalisable iff $\rho<1$, i.e. $\mu>\lambda/2$, and then the chain is positive recurrent with
$$\pi(0)=\frac{1-\rho}{1+\rho},\qquad\pi(n)=\frac{2(1-\rho)}{1+\rho}\rho^n\quad(n\ge1).$$
For $\mu\le\lambda/2$ there is no stationary distribution.
:::

::: {.solution for="prob-eecs126hw-9-q1" status="draft"}
1. Fix $j$ and sum detailed balance over $i\ne j$: $\sum_{i\ne j}p_iq_{ij}=p_j\sum_{i\ne j}q_{ji}=p_jq_j$, which is the balance equation of @def-ctmc-stationary. So $pQ=0$.
2. The embedded (jump) chain has $P_{ij}=q_{ij}/q_i$, and by @thm-jump-chain-stationary its stationary distribution is $\tilde p_i=p_iq_i/c$ with $c=\sum_kp_kq_k$ (assumed finite). Then
$$\tilde p_iP_{ij}=\frac{p_iq_{ij}}{c}=\frac{p_jq_{ji}}{c}=\tilde p_jP_{ji},$$
the detailed balance equations for the jump chain (@def-detailed-balance).
:::

::: {.solution for="prob-eecs126hw-9-q2" status="draft"}
The uniform distribution over all $\binom{10000}{1278}$ configurations (sets of occupied squares).

1. The configuration is a CTMC. A transition moves one particle to an adjacent empty square, at rate $\frac14$ (rate $1$ of attempting, times $\frac14$ for the direction).
2. The reverse move, the same particle stepping back, is also allowed and also has rate $\frac14$. So $q(\eta,\eta')=q(\eta',\eta)$ for all configurations, and the uniform distribution satisfies detailed balance, hence is stationary (Problem 1 of this set, or @thm-detailed-balance-invariant).
3. The chain is irreducible (there are empty squares, and particles can be shuffled into any arrangement), so the stationary distribution is unique.
:::

::: {.solution for="prob-eecs126hw-9-q3" status="draft"}
(a) As for the M/M/1 queue (@exm-mm1-queue), all clocks are exponential and memoryless, so the queue length is a CTMC. Diagram: states $0,1,2,\dots$; $k\to k+1$ at rate $\lambda$; $k\to k-1$ at rate $k\mu$ (the first of $k$ independent $\text{Exp}(\mu)$ services, @prp-min-of-exponentials).

(b) Cut balance $\pi(k)\lambda=\pi(k+1)(k+1)\mu$ gives $\pi(k)=\pi(0)\frac{(\lambda/\mu)^k}{k!}$, which sums to $\pi(0)e^{\lambda/\mu}$ for every $\lambda,\mu$. So $\pi$ is $\text{Poisson}(\lambda/\mu)$. An irreducible CTMC with a stationary distribution is positive recurrent (@thm-positive-recurrence-invariant, applied to the jump chain via @thm-jump-chain-stationary).
:::

::: {.solution for="prob-eecs126d-8-q3" status="draft"}
(a) The queue length is a CTMC on $\{0,1,2,\dots\}$ with $q(n,n+1)=\lambda$ for all $n$ and $q(n,0)=\mu$ for $n\ge1$. The balance equations (@def-ctmc-stationary) are
$$\pi(n)(\lambda+\mu)=\lambda\pi(n-1)\ (n\ge1),\qquad\lambda\pi(0)=\mu\bigl(1-\pi(0)\bigr).$$
So $\pi(0)=\frac{\mu}{\lambda+\mu}$ and
$$\pi(n)=\frac{\mu}{\lambda+\mu}\Bigl(\frac{\lambda}{\lambda+\mu}\Bigr)^n,\qquad n\ge0.$$

(b) This geometric distribution has mean $\frac{\lambda/(\lambda+\mu)}{\mu/(\lambda+\mu)}=\frac\lambda\mu$. (Directly: the time since the last visit is $\text{Exp}(\mu)$, and on average $\lambda$ customers arrive per unit time.)
:::

::: {.solution for="prob-eecs126d-9-q2" status="draft"}
The answer is $\frac{\mu^2}{\lambda^2+\lambda\mu+\mu^2}$.

1. Let the state be the number of working servers. Only one server runs, so failures happen at rate $\mu$ in states $2$ and $1$; repairs happen at rate $\lambda$ in states $1$ and $0$. This is a birth–death CTMC: $2\to1$ and $1\to0$ at rate $\mu$, $0\to1$ and $1\to2$ at rate $\lambda$.
2. Cut balance gives $\pi(1)\lambda=\pi(2)\mu$ and $\pi(0)\lambda=\pi(1)\mu$, so with $r=\mu/\lambda$, $(\pi(0),\pi(1),\pi(2))\propto(r^2,r,1)$.
3. Normalising, $\pi(0)=\frac{r^2}{1+r+r^2}=\frac{\mu^2}{\lambda^2+\lambda\mu+\mu^2}$, the long-run fraction of time with no server working.
:::

::: {.solution for="prob-eecs126-6-q1" status="draft"}
1. *Balance equations* ("rate out = rate in"; each is one column of $\pi Q=0$):
   - state 1: $\pi_1\cdot1=2.5\pi_2+3\pi_3$;
   - state 2: $\pi_2\cdot5=\pi_1\cdot1$;
   - state 3: $\pi_3\cdot3=2.5\pi_2$.

2. *Solve in terms of $\pi_1$.* State 2 gives $\pi_2=\pi_1/5$. State 3 gives $\pi_3=\frac{2.5}{3}\pi_2=\frac56\cdot\frac{\pi_1}5=\pi_1/6$. The equation for state 1 is then automatic: $2.5\cdot\frac{\pi_1}5+3\cdot\frac{\pi_1}6=\frac{\pi_1}2+\frac{\pi_1}2=\pi_1$. (The three equations sum to $0=0$, so one of them is always redundant.)

3. *Normalize.* $\pi_1\bigl(1+\frac15+\frac16\bigr)=\pi_1\cdot\frac{41}{30}=1$, so $\pi_1=\frac{30}{41}$, $\pi_2=\frac6{41}$, $\pi_3=\frac5{41}$.

4. The chain is irreducible on three states ($1\to2\to3\to1$), so this stationary distribution is unique.
:::
