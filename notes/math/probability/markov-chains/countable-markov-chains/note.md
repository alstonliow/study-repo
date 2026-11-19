---
title: "Countable-State Markov Chains"
sources: [eecs126-3]
requires: [math/probability/markov-chains/periodicity-and-convergence, math/probability/markov-chains/hitting-times]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley EECS126 (Fall 2021), note "Markov Chains", Section 2, in our own wording; proofs written out in steps. -->

With infinitely many states (a queue length, a random walk on $\mathbb{Z}$), irreducibility and aperiodicity no longer guarantee an invariant distribution: the chain may wander off. The finite theory (@def-markov-chain) carries over with the same transition rule on a countable state space.

::: {#def-recurrent-transient .definition name="Recurrent and transient states"}

Let $T_i^+=\min\{n\ge1:X_n=i\}$ be the first *return* time to state $i$. State $i$ is
$$\text{recurrent if }\Pr_i(T_i^+<\infty)=1,\qquad\text{transient otherwise.}$$
A recurrent state is *positive recurrent* if $E_i[T_i^+]<\infty$ and *null recurrent* if $E_i[T_i^+]=\infty$.

:::

::: {#thm-recurrence-visits .theorem name="Recurrence and the number of visits"}

Let $V_i=\sum_{n\ge0}\mathbf 1\{X_n=i\}$ be the number of visits to $i$. Starting from $i$:

1. if $i$ is recurrent, $V_i=\infty$ with probability $1$;
2. if $i$ is transient, $V_i$ is geometric with $E_i[V_i]=1/(1-f)<\infty$, where $f=\Pr_i(T_i^+<\infty)$.

Hence $i$ is recurrent if and only if $\sum_{n\ge0}P^n(i,i)=\infty$.

:::

::: {.proof}

1. By the Markov property at each return time, each return is followed by a fresh copy of the chain started at $i$ (@prp-markov-fresh-start, applied at a stopping time). So $\Pr_i(V_i\ge k+1)=f^k$.

2. If $f=1$ this is $1$ for all $k$, so $V_i=\infty$ almost surely. If $f<1$, $V_i$ is geometric with success probability $1-f$, and $E_i[V_i]=1/(1-f)$.

3. By linearity, $E_i[V_i]=\sum_n\Pr_i(X_n=i)=\sum_nP^n(i,i)$, which is finite exactly when $f<1$.

:::

::: {#thm-class-properties .theorem name="Class properties"}

In a communicating class, either all states are recurrent or all are transient; either all are positive recurrent or none is; and all have the same period.

:::

::: {.proof}

1. Let $i\leftrightarrow j$, with $P^a(i,j)>0$ and $P^b(j,i)>0$. For every $n$, $P^{a+n+b}(i,i)\ge P^a(i,j)P^n(j,j)P^b(j,i)$.

2. Summing over $n$, if $\sum_nP^n(j,j)=\infty$ then $\sum_nP^n(i,i)=\infty$; by symmetry and @thm-recurrence-visits, $i$ and $j$ are both recurrent or both transient.

3. Positive recurrence follows from @thm-positive-recurrence-invariant below (an invariant distribution charges all states of the class); the period statement is @prp-period-class.

:::

::: {#thm-positive-recurrence-invariant .theorem name="Invariant distributions on a countable state space"}

An irreducible chain has an invariant distribution $\pi$ if and only if it is positive recurrent. Then $\pi$ is unique and
$$\pi(i)=\frac{1}{E_i[T_i^+]}\quad\text{for every state }i.$$
If moreover the chain is aperiodic, $\Pr(X_n=i)\to\pi(i)$ from every initial distribution.

:::

The formula is the countable version of the long-run fraction of time (@thm-markov-fraction-of-time): between consecutive visits to $i$ the chain spends on average $E_i[T_i^+]$ steps. We state the theorem without proof; the convergence part uses the same coupling argument as @thm-markov-convergence.

::: {#exm-random-walk-on-integers .example name="Random walk on the integers"}

On $\mathbb{Z}$ step $+1$ with probability $p$ and $-1$ with probability $1-p$. A return to $0$ at time $2n$ needs $n$ steps each way, so
$$P^{2n}(0,0)=\binom{2n}{n}p^n(1-p)^n\approx\frac{(4p(1-p))^n}{\sqrt{\pi n}}.$$
If $p\ne\tfrac12$ then $4p(1-p)<1$, the series converges, and the walk is transient. If $p=\tfrac12$ the terms are about $1/\sqrt{\pi n}$, the series diverges, and the walk is recurrent; it is null recurrent, since a uniform "distribution" on $\mathbb{Z}$ is the only candidate invariant measure and it cannot be normalised.

:::

::: {#exm-birth-death-chain .example name="Reflected random walk"}

On $\{0,1,2,\dots\}$ move up with probability $p$ and down with probability $q=1-p$ (staying at $0$ instead of going down). The balance equations $\pi(i)p=\pi(i+1)q$ give $\pi(i)=\pi(0)(p/q)^i$. If $p<q$ this sums to a distribution, $\pi(i)=(1-\rho)\rho^i$ with $\rho=p/q$, and the chain is positive recurrent; if $p\ge q$ there is no invariant distribution.

:::
