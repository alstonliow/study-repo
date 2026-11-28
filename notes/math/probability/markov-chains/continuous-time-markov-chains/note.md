---
title: "Continuous-Time Markov Chains"
sources: [eecs126-6]
requires: [math/probability/markov-chains/poisson-process, math/probability/markov-chains/countable-markov-chains]
aliases: [math/probability/random-processes/continuous-time-markov-chains]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley EECS126 (Fall 2021), note "Continuous Time Markov Chains", in our own wording; proofs written out in steps. -->

A continuous-time Markov chain (CTMC) moves between states at random times. The Markov property in continuous time forces the holding times to be exponential, so the chain is described by jump *rates* instead of jump probabilities.

::: {#def-ctmc .definition name="Continuous-time Markov chain, rate matrix"}

Let $\mathcal X$ be a countable state space and let $q(i,j)\ge0$ for $i\ne j$ be *rates* with $q(i)=\sum_{j\ne i}q(i,j)<\infty$. The CTMC with these rates, started at $X(0)$, does the following: in state $i$ it waits an $\operatorname{Exp}(q(i))$ time, then jumps to $j\neq i$ with probability $q(i,j)/q(i)$, independently of the past. The *rate matrix* (generator) $Q$ has entries $Q(i,j)=q(i,j)$ for $i\ne j$ and $Q(i,i)=-q(i)$, so each row sums to $0$.

:::

::: {#fig-continuous-time-markov-chains-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[vertex] (a) at (0,0) {$0$};
\node[vertex] (b) at (2.6,0) {$1$};
\node[vertex] (c) at (5.2,0) {$2$};
\draw[->] (a) to[bend left=30] node[lab, tick, auto] {$1$} (b);
\draw[->] (b) to[bend left=30] node[lab, tick, auto] {$\frac12$} (a);
\draw[->] (b) to[bend left=30] node[lab, tick, auto] {$1$} (c);
\draw[->] (c) to[bend left=30] node[lab, tick, auto] {$\frac32$} (b);
\end{tikzpicture}
\end{center}
```

A continuous-time chain is drawn with transition rates $q_{ij}$ on the edges instead of probabilities; @fig-continuous-time-markov-chains-2 shows a path of this chain

:::

Equivalently, from state $i$ an independent $\operatorname{Exp}(q(i,j))$ clock runs for each $j$, and the chain follows the first clock to ring (@prp-min-of-exponentials). For small $h$, $\Pr(X(t+h)=j\mid X(t)=i)=q(i,j)h+o(h)$ for $j\ne i$.

::: {#rmk-ctmc-why-exponential .remark name="Why the holding times are exponential"}

The Markov property says that, given that the chain is still in $i$ after time $s$, the remaining holding time has the same law as at the start: $\Pr(H>s+t\mid H>s)=\Pr(H>t)$. The only continuous distributions with this memoryless property are the exponential ones.

:::

::: {#def-ctmc-stationary .definition name="Stationary distribution of a CTMC"}

A distribution $\pi$ on $\mathcal X$ is *stationary* for the CTMC with rate matrix $Q$ if
$$\pi Q=0,\quad\text{that is,}\quad\pi(j)q(j)=\sum_{i\ne j}\pi(i)q(i,j)\quad\text{for all }j.$$

:::

The second form is a flow balance: in the long run, the rate of leaving $j$ equals the rate of entering $j$. For an irreducible chain with a stationary distribution, $\Pr(X(t)=j)\to\pi(j)$ as $t\to\infty$ from every starting state (there is no periodicity in continuous time), and $\pi(j)$ is the long-run fraction of time spent in $j$.

::: {#def-jump-chain .definition name="Jump chain"}

The *jump chain* of a CTMC is the discrete-time Markov chain of the states it visits, with transition matrix $P(i,j)=q(i,j)/q(i)$ for $j\ne i$ and $P(i,i)=0$.

:::

::: {#fig-continuous-time-markov-chains-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,-0.3) -- (6.5,-0.3) node[lab, right] {$t$};
\draw[faint] (0,0.0) -- (6.2,0.0);
\node[tick, left] at (0,0.0) {$0$};
\draw[faint] (0,0.6) -- (6.2,0.6);
\node[tick, left] at (0,0.6) {$1$};
\draw[faint] (0,1.2) -- (6.2,1.2);
\node[tick, left] at (0,1.2) {$2$};
\draw[hl] (0.00,0.0) -- (0.98,0.0);
\node[hl dot] at (0.00,0.0) {};
\draw[hl] (0.98,0.6) -- (2.03,0.6);
\node[hl dot] at (0.98,0.6) {};
\draw[hl] (2.03,1.2) -- (2.93,1.2);
\node[hl dot] at (2.03,1.2) {};
\draw[hl] (2.93,0.6) -- (2.95,0.6);
\node[hl dot] at (2.93,0.6) {};
\draw[hl] (2.95,1.2) -- (4.86,1.2);
\node[hl dot] at (2.95,1.2) {};
\draw[hl] (4.86,0.6) -- (6.20,0.6);
\node[hl dot] at (4.86,0.6) {};
\end{tikzpicture}
\end{center}
```

A path of a continuous-time chain: it holds in each state for an exponential time, then jumps according to the jump chain. Recording only the visited states gives the jump chain

:::

::: {#thm-jump-chain-stationary .theorem name="Stationary distributions of the CTMC and its jump chain"}

Let $\pi$ be a stationary distribution of the CTMC and suppose $c=\sum_i\pi(i)q(i)<\infty$. Then
$$\tilde\pi(i)=\frac{\pi(i)q(i)}{c}$$
is an invariant distribution of the jump chain. Conversely, if $\tilde\pi$ is invariant for the jump chain, $\pi(i)\propto\tilde\pi(i)/q(i)$ is stationary for the CTMC whenever it can be normalised.

:::

::: {.proof}

1. Using $q(i,j)=q(i)P(i,j)$, the balance equations of @def-ctmc-stationary read $\pi(j)q(j)=\sum_{i}\pi(i)q(i)P(i,j)$ (with $P(j,j)=0$).

2. Writing $\mu(i)=\pi(i)q(i)$, this is exactly $\mu P=\mu$. Dividing by $c$ gives an invariant distribution of the jump chain.

3. The converse reads the same identities backwards with $\pi(i)=\mu(i)/q(i)$.

:::

The jump chain visits $i$ a fraction $\tilde\pi(i)$ of its steps, and each visit lasts on average $1/q(i)$; weighting by the mean holding time turns $\tilde\pi$ into $\pi$.

::: {#exm-mm1-queue .example name="The M/M/1 queue"}

Customers arrive as a Poisson process of rate $\lambda$ and one server serves them in order, each service taking an independent $\operatorname{Exp}(\mu)$ time. The number in the system is a CTMC on $\{0,1,2,\dots\}$ with $q(n,n+1)=\lambda$ and $q(n,n-1)=\mu$ for $n\ge1$. Balance across the cut between $n$ and $n+1$ gives $\pi(n)\lambda=\pi(n+1)\mu$, so with $\rho=\lambda/\mu<1$
$$\pi(n)=(1-\rho)\rho^n,\qquad E[\text{number in system}]=\frac{\rho}{1-\rho}.$$
With $\lambda=1$ and $\mu=2$ the server is idle half the time and the mean number in the system is $1$. If $\rho\ge1$ there is no stationary distribution: the queue grows without bound.

:::

::: {#fig-continuous-time-markov-chains-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \i/\l in {0/0,1/1,2/n,3/n+1} \node[small vertex] (s\i) at (2.2*\i,0) {$\l$};
\node[lab] at (1.1+2.2*1.0,0) {$\cdots$};
\node[lab] (s4) at (8.6,0) {$\cdots$};
\foreach \i/\j in {0/1,2/3,3/4} { \draw[->] (s\i) to[bend left=30] node[edge label, above, pos=0.3] {$\lambda$} (s\j); \draw[->] (s\j) to[bend left=30] node[edge label, below, pos=0.3] {$\mu$} (s\i); }
\draw[accent, dashed, emph] (5.5,-1.1) -- (5.5,1.1) node[lab, above] {cut};
\end{tikzpicture}
\end{center}
```

The M/M/1 queue as a birth–death chain (@exm-mm1-queue): arrivals at rate $\lambda$, services at rate $\mu$. In equilibrium the flow across the cut between $n$ and $n+1$ is the same in both directions, $\pi(n)\lambda=\pi(n+1)\mu$.

:::

::: {#rmk-ctmc-hitting-times .remark name="Hitting times"}

First-step analysis (@thm-first-step-hitting-time) works in continuous time with the mean holding time added: if $\beta(i)$ is the expected time to reach a set $A$ from $i\notin A$, then $\beta(i)=\frac{1}{q(i)}+\sum_{j\ne i}\frac{q(i,j)}{q(i)}\beta(j)$, with $\beta=0$ on $A$.

:::
