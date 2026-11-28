::: {.problem #prob-eecs126hw-3-q3 origin="external" source="eecs126hw-3-q3"}
**Packet Routing.** Packets arriving at a switch are routed to either destination $A$ (with probability $p$) or destination $B$ (with probability $1-p$). The destination of each packet is chosen independently of each other. In the time interval $[0,1]$, the number of arriving packets is $\text{Poisson}(\lambda)$.

(a) Show that the number of packets routed to $A$ is Poisson distributed. With what parameter?

(b) Are the number of packets routed to $A$ and to $B$ independent?
:::

::: {.problem #prob-eecs126hw-7-q2 origin="external" source="eecs126hw-7-q2"}
**Poisson Branching.** Consider a branching process such that at generation $n$, each individual in the population survives until generation $n+1$ with probability $0<p<1$, independently, and a Poisson number (with parameter $\lambda$) of immigrants enters the population. Let $X_n$ denote the number of people in the population at generation $n$.

(a) Suppose that at generation $0$, the number of people in the population is a Poisson random variable with parameter $\lambda_0$. What is the distribution at generation $1$? What is the distribution at generation $n$?

(b) What is the distribution of $X_n$ as $n\to\infty$? What if at generation $0$, the number of individuals is an arbitrary probability distribution over the non-negative integers; does the distribution still converge? (Justify the convergence rigorously.)
:::

::: {.problem #prob-eecs126hw-7-q4 origin="external" source="eecs126hw-7-q4"}
**Poisson Practice.** Let $(N(t),t\ge0)$ be a Poisson process with rate $\lambda$. Let $T_k$ denote the time of $k$-th arrival, for $k\in\mathbb N$, and given $0\le s<t$, we write $N(s,t)=N(t)-N(s)$. Compute:

(a) $P(N(1)+N(2,4)+N(3,5)=0)$.

(b) $E(N(1,3)\mid N(1,2)=3)$.

(c) $E(T_2\mid N(2)=1)$.
:::

::: {.problem #prob-eecs126hw-7-q5 origin="external" source="eecs126hw-7-q5"}
**Basketball II.** Team $A$ and Team $B$ are playing an untimed basketball game in which the two teams score points according to independent Poisson processes. Team $A$ scores points according to a Poisson process with rate $\lambda_A$ and Team $B$ scores points according to a Poisson process with rate $\lambda_B$. The game is over when one of the teams has scored $k$ more points than the other team.

(a) Suppose $\lambda_A=\lambda_B$, and Team $A$ has a head start of $m<k$ points. Find the probability that Team $A$ wins.

(b) Keeping the assumptions from part (b), find the expected time $E[T]$ it will take for the game to end.
:::

::: {.problem #prob-eecs126hw-8-q1 origin="external" source="eecs126hw-8-q1"}
**Geometric Sum of Exponentials.** Let $X_1,X_2,\dots$ be iid exponentials with parameter $\lambda$. If $N\sim\text{Geom}(p)$ taking values on $\{1,2,\dots\}$, then show that
$$\sum_{i=1}^{N}X_i$$
is exponential and determine its parameter. Hint: Consider Poisson thinning.
:::

::: {.problem #prob-eecs126hw-8-q2 origin="external" source="eecs126hw-8-q2"}
**Bus Arrivals at Cory Hall.** Starting at time $0$, the 52 line makes stops at Cory Hall according to a Poisson process of rate $\lambda$. Students arrive at the stop according to an independent Poisson process of rate $\mu$. Every time the bus arrives, all students waiting get on.

(a) Given that the interarrival time between bus $i-1$ and bus $i$ is $x$, find the distribution for the number of students entering the $i$th bus. (Here, $x$ is a given number, not a random quantity.)

(b) Given that a bus arrived at 9:30 AM, find the distribution for the number of students that will get on the next bus.

(c) Find the distribution of the number of students getting on the next bus to arrive after 9:30 AM, assuming that time $0$ was infinitely far in the past.
:::

::: {.problem #prob-eecs126d-7-q3 origin="external" source="eecs126d-7-q3"}
**Illegal U-Turns.** Each morning, as you pull out of your driveway, you would like to make a U-turn rather than drive around the block. Unfortunately, U-turns are illegal and police cars drive by according to a Poisson process with rate $\lambda$. You decide to make a U-turn once you see that the road has been clear of police cars for $\tau>0$ units of time. Let $N$ be the number of police cars you see before you make a U-turn.

(a) Find $E[N]$.

(b) Let $n$ be a positive integer $\ge2$. Find the conditional expectation of the time elapsed between police cars $n-1$ and $n$, given that $N\ge n$.

(c) Find the expected time that you wait until you make a U-turn.
:::

::: {.problem #prob-mit6041f10-7-q3 origin="external" source="mit6041f10-7-q3"}
Let $T_1$ and $T_2$ be exponential random variables with parameter $\lambda$, and let $S$ be an exponential random variable with parameter $\mu$. We assume that all three of these random variables are independent. Derive an expression for the expected value of $\min\{T_1 + T_2, S\}$. Hint: See Problem 6.19 in the text.
:::

::: {.problem #prob-mit6041f10-7-q4 origin="external" source="mit6041f10-7-q4"}
A single dot is placed on a very long length of yarn at the textile mill. The yarn is then cut into lengths requested by different customers. The lengths are independent of each other, but all distributed according to the PDF $f_L(\ell)$. Let $R$ be be the length of yarn purchased by that customer whose purchase included the dot. Determine the expected value of $R$ in the following cases:

(a) $f_L(\ell) = \lambda e^{-\lambda\ell}, \quad \ell \geq 0$
(b) $f_L(\ell) = \dfrac{\lambda^3 \ell^2 e^{-\lambda\ell}}{2}, \quad \ell \geq 0$
(c) $f_L(\ell) = \ell e^{\ell}, \quad 0 \leq \ell \leq 1$
:::

::: {.problem #prob-mit6041f10-7-q5 origin="external" source="mit6041f10-7-q5"}
Consider a Poisson process of rate $\lambda$. Let random variable $N$ be the number of arrivals in $(0, t]$ and $M$ be the number of arrivals in $(0, t + s]$, where $t, s \geq 0$.

(a) Find the conditional PMF of $M$ given $N$, $p_{M|N}(m|n)$, for $m \geq n$.
(b) Find the joint PMF of $N$ and $M$, $p_{N,M}(n, m)$.
(c) Find the conditional PMF of $N$ given $M$, $p_{N|M}(n|m)$, for $n \leq m$, using your answer to part (b).
(d) Rederive your answer to part (c) without using part (b). As a hint, consider what kind of distribution the $k$th arrival time has if we are given the event $\{M = m\}$, where $k \leq m$.
(e) Find $\mathbf{E}[NM]$.
:::

::: {.problem #prob-mit6041f10-7-q6 origin="external" source="mit6041f10-7-q6"}
The interarrival times for cars passing a checkpoint are independent random variables with PDF
$$f_T(t) = \begin{cases} 2e^{-2t}, & \text{for } t > 0,\\ 0, & \text{otherwise,}\end{cases}$$
where the interarrival times are measured in minutes. The successive experimental values of the durations of these interarrival times are recorded on small computer cards. The recording operation occupies a negligible time period following each arrival. Each card has space for three entries. As soon as a card is filled, it is replaced by the next card.

(a) Determine the mean and the third moment of the interarrival times.
(b) Given that no car has arrived in the last four minutes, determine the PMF for random variable $K$, the number of cars to arrive in the next six minutes.
(c) Determine the PDF and the expected value for the total time required to use up the first dozen computer cards.
(d) Consider the following two experiments:
  i. Pick a card at random from a group of completed cards and note the total time, $Y$, the card was in service. Find $\mathbf{E}[Y]$ and $\mathrm{var}(Y)$.
  ii. Come to the corner at a random time. When the card in use at the time of your arrival is completed, note the total time it was in service (the time from the start of its service to its completion). Call this time $W$. Determine $\mathbf{E}[W]$ and $\mathrm{var}(W)$.
:::
