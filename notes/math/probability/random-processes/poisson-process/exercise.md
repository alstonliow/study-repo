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
