::: {.problem #prob-eecs126hw-8-q3 origin="external" source="eecs126hw-8-q3"}
**Frogs.** Three frogs are playing near a pond. When they are in the sun they get too hot and jump in the lake at rate $1$. When they are in the lake they get too cold and jump onto the land at rate $2$. The rates here refer to the rate in exponential distribution. Let $X_t$ be the number of frogs in the sun at time $t\ge0$.

(a) Find the stationary distribution for $(X_t)_{t\ge0}$.

(b) Check the answer to (a) by noting that the three frogs are independent two-state Markov chains.
:::

::: {.problem #prob-eecs126hw-8-q4 origin="external" source="eecs126hw-8-q4"}
**Taxi Queue.** Empty taxis pass by a street corner according to a Poisson process of rate two per minute and pick up a passenger if one is waiting there. Passengers arrive at the street corner according to a Poisson process of rate one per minute and wait for a taxi only if there are less than four persons waiting; otherwise they leave and never return. John arrives at the street corner at a given time. Find his expected waiting time, given that he joins the queue. Assume that the process is in steady state.
:::

::: {.problem #prob-eecs126hw-8-q5 origin="external" source="eecs126hw-8-q5"}
**M/M/2 Queue.** A queue has Poisson arrivals with rate $\lambda$. It has two servers that work in parallel. When there are at least two customers in the queue, two are being served. When there is only one customer, only one server is active. The service times are i.i.d. exponential random variables with rate $\mu$. Let $X(t)$ be the number of customers either in the queue or in service at time $t$.

(a) Argue that the process $(X(t),t\ge0)$ is a Markov process.

(b) Draw the state transition diagram.

(c) Find the range of values of $\mu$ for which the Markov chain is positive-recurrent and for this range of values calculate the stationary distribution of the Markov chain.
:::

::: {.problem #prob-eecs126hw-9-q1 origin="external" source="eecs126hw-9-q1"}
**Reversibility of CTMCs.** We say a CTMC with rate matrix $Q$ is reversible if there is a distribution $p$ satisfying the detailed balance equations:
$$p_iq_{ij}=p_jq_{ji}\quad\forall i,j.$$
Show that if a CTMC is reversible w.r.t. $p$, then $p$ is a stationary distribution for the chain. Furthermore, show that in this case the embedded chain is also reversible. Remark. The converse is true too, i.e. the CTMC is reversible given that the embedded chain is reversible.
:::

::: {.problem #prob-eecs126hw-9-q2 origin="external" source="eecs126hw-9-q2"}
**Particles Moving on a Checkerboard.** There are 1278 particles on a $100\times100$ checkerboard. Each location on the checkerboard can have at most one particle. Each particle, at rate $1$, independently over the particles, attempts to jump, and when it does it tries to move in one of the four directions, up, down, left, and right, equiprobably. However, if this movement would either take it out of the checkerboard or onto a location that is already occupied by another particle then the jump is suppressed, and nothing happens.

What is the stationary distribution of the configuration of the particles on the checkerboard?
:::

::: {.problem #prob-eecs126hw-9-q3 origin="external" source="eecs126hw-9-q3"}
**Poisson Queues.** A continuous-time queue has Poisson arrivals with rate $\lambda$, and it is equipped with infinitely many servers. The servers can work in parallel on multiple customers, but they are non-cooperative in the sense that a single customer can only be served by one server. Thus, when there are $k$ customers in the queue ($k\in\mathbb N$), $k$ servers are active. Suppose that the service time of each customer is exponentially distributed with rate $\mu$ and they are i.i.d.

(a) Argue that the queue-length is a Markov chain. Draw the transition diagram of the Markov chain.

(b) Prove that for all finite values of $\lambda$ and $\mu$ the Markov chain is positive-recurrent and find the invariant distribution.
:::

::: {.problem #prob-eecs126d-8-q3 origin="external" source="eecs126d-8-q3"}
**Lazy Server.** Customers arrive at a queue in a service facility at the times of a Poisson process of rate $\lambda$. The service facility has infinite capacity. There is an infinitely powerful but lazy server who visits the service facility at the times of a Poisson process of rate $\mu$. These two processes are independent. When the server visits the facility she instantaneously serves all the customers that are in the queue and then immediately leaves (until her next visit).

Thus, for instance, at any time, any customers that are waiting in the queue would only be those that arrived after the most recent visit of the server.

(a) Model the queue length as a CTMC and find the stationary distribution.

(b) Suppose tha the CTMC is at stationary, and find the mean number of customers waiting in the queue at any given time.
:::

::: {.problem #prob-eecs126d-9-q2 origin="external" source="eecs126d-9-q2"}
**Two-Server System.** A company has two servers (the second server is a backup in case the first server fails, so only one server is ever used at a time). When a server is running, the time until it breaks down is exponentially distributed with rate $\mu$. When a server is broken, it is taken to the repair shop. The repair shop can only fix one server at a time, and its repair time is exponentially distributed with rate $\lambda$. Find the long-run probability that no servers are operational.
:::

::: {.problem #prob-eecs126-6-q1 origin="external" source="eecs126-6-q1"}
Say our application has a normal state (1) and a test state (2) and a repair state (3).

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (1) at (0,0) {$1$};
\node[small vertex] (2) at (2.8,0) {$2$};
\node[small vertex] (3) at (1.4,-2.0) {$3$};
\draw[->] (1) to[bend left=25] node[lab,tick,above] {$1$} (2);
\draw[->] (2) to[bend left=25] node[lab,tick,below] {$2.5$} (1);
\draw[->] (2) to node[lab,tick,right] {$2.5$} (3);
\draw[->] (3) to node[lab,tick,left] {$3$} (1);
\end{tikzpicture}
\end{center}
```

What is the stationary distribution of this Markov Chain? Note we have
$$Q=\begin{pmatrix}-1&1&0\\2.5&-5&2.5\\3&0&-3\end{pmatrix}.$$
Write out the balance equations, either by examining $\pi Q=0$ or by just looking at the "rate in = rate out" for each state. Show that
$$\pi=(30/41,\ 6/41,\ 5/41).$$

*Note (these notes):* The notes mark this as problem 7.14 of Bertsekas and Tsitsiklis, *Introduction to Probability*; the owner approved adding it (2026-11-24). The figure is our redrawing of the transition diagram: the edge labels are the rates of $Q$. Stationary distributions of a CTMC are defined in @def-ctmc-stationary.
:::
