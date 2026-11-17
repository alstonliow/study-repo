---
title: "Invariant Distributions"
sources: [cs70-21]
requires: [math/probability/markov-chains/finite-markov-chains]
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 21 (cs70-21), in our own wording; proofs written out in steps. -->

## Balance equations

::: {#def-invariant-distribution .definition name="Invariant distribution"}

A distribution $\pi$ on $\mathcal X$ (a row vector with $\pi(i)\ge0$ and $\sum_i\pi(i)=1$) is *invariant* for $P$ if it satisfies the *balance equations*
$$\pi=\pi P,\qquad\text{that is,}\qquad \pi(j)=\sum_{i}\pi(i)P(i,j)\ \text{ for all }j.$$

:::

::: {#thm-invariant-iff-constant .theorem name="Invariant means unchanged in time"}

$\pi_n=\pi_0$ for all $n\ge0$ if and only if $\pi_0$ is invariant.

:::

::: {.proof}

1. If $\pi_n=\pi_0$ for all $n$, then in particular $\pi_0=\pi_1=\pi_0P$ (@thm-markov-distribution-at-time-n), so $\pi_0$ is invariant.

2. Conversely, let $\pi_0P=\pi_0$. We show $\pi_n=\pi_0$ by induction on $n$. It holds for $n=0$, and if $\pi_n=\pi_0$, then $\pi_{n+1}=\pi_0P^{n+1}=\pi_nP=\pi_0P=\pi_0$.

:::

::: {#rmk-invariant-distributions-solving}

The $K$ balance equations are linearly dependent (their sum is $\sum_j\pi(j)=\sum_i\pi(i)$, which always holds), so they never determine $\pi$ by themselves. Add the condition $\sum_i\pi(i)=1$. A practical method: set one component to $1$, drop one balance equation, solve the rest, and rescale so the components sum to $1$ (@exm-web-chain-invariant).

:::

::: {#exm-two-state-invariant .example name="Invariant distributions of the two-state chain"}

For the chain of @prp-two-state-chain, each balance equation reads $\pi(0)=(1-a)\pi(0)+a\pi(1)$, i.e. $a\pi(0)=a\pi(1)$. If $a>0$, this gives $\pi(0)=\pi(1)$, and with $\pi(0)+\pi(1)=1$ the only invariant distribution is $\bigl(\frac12,\frac12\bigr)$. If $a=0$, then $P$ is the identity, the chain never moves, and *every* distribution is invariant.

:::

## Irreducible chains

::: {#def-irreducible .definition name="Irreducible"}

State $j$ is *reachable* from $i$ if $P^n(i,j)>0$ for some $n\ge0$, that is, the transition diagram has a directed walk from $i$ to $j$. A Markov chain is *irreducible* if every state is reachable from every other state, i.e. its transition diagram is strongly connected.

:::

The two-state chain is irreducible if $a>0$ and not if $a=0$. Irreducibility is what makes the invariant distribution unique.

::: {#thm-markov-fraction-of-time .theorem name="Long-run fraction of time"}

Let a finite Markov chain be irreducible. Then it has exactly one invariant distribution $\pi$, all of whose entries are positive, and for every initial distribution and every state $i$, the fraction of the first $n$ steps spent in $i$ tends to $\pi(i)$:
$$\frac1n\sum_{m=0}^{n-1}\mathbf 1\{X_m=i\}\to\pi(i)\qquad\text{as }n\to\infty,$$
in probability and with probability $1$. Moreover $\pi(i)=1/E[T_i]$, where $T_i$ is the time the chain started at $i$ takes to return to $i$.

:::

::: {#rmk-markov-fraction-of-time-sketch .remark name="Why it is true (sketch)"}

We do not give the full proof; here are its main steps.

1. *Visits renew.* Each time the chain enters $i$, its future is a fresh copy of the chain started at $i$ (Markov property). So the times between successive visits to $i$ are i.i.d. copies of $T_i$, and by @thm-law-of-large-numbers the chain visits $i$ about $n/E[T_i]$ times in $n$ steps. With irreducibility one checks that every state is visited infinitely often and $E[T_i]<\infty$, so these rates $\pi(i)=1/E[T_i]$ are positive and sum to $1$.

2. *Rates balance.* In $n$ steps the chain is in $j$ about $n\pi(j)$ times, and each visit is followed by a move to $i$ with probability $P(j,i)$. Every visit to $i$ comes right after a visit to some $j$, so $n\pi(i)\approx\sum_j n\pi(j)P(j,i)$: $\pi$ solves the balance equations.

3. *Uniqueness.* If $\nu$ is any invariant distribution, start the chain from $\nu$. Then $\Pr(X_m=i)=\nu(i)$ for every $m$ (@thm-invariant-iff-constant), so the fraction of time in $i$ has expectation $\nu(i)$ for every $n$. Since that fraction lies in $[0,1]$ and tends to $\pi(i)$, its expectation tends to $\pi(i)$ too, so $\nu(i)=\pi(i)$.

:::

::: {#rmk-invariant-distributions-pagerank .remark name="PageRank"}

Model a web surfer who, on each page, follows one of its links uniformly at random. If this chain is irreducible, $\pi(i)$ is the long-run fraction of time spent on page $i$, and ranking pages by $\pi(i)$ is the idea behind Google's *PageRank* (combined, in practice, with other signals). @exm-web-chain-invariant computes it for five pages.

:::
