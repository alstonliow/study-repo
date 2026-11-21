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

::: {#fig-invariant-distributions-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[vertex] (z) at (0,0) {$0$};
\node[vertex] (o) at (3.2,0) {$1$};
\draw[->] (z) to[bend left=30] node[lab, tick, auto] {$a$} (o);
\draw[->] (o) to[bend left=30] node[lab, tick, auto] {$b$} (z);
\node[tick, above] at (1.6,0.75) {flow $\pi_0a$};
\node[tick, below] at (1.6,-0.75) {flow $\pi_1b$};
\end{tikzpicture}
\end{center}
```

In the invariant distribution of the two-state chain the probability flow from $0$ to $1$ equals the flow back, $\pi_0a=\pi_1b$, so $\pi=\bigl(\frac b{a+b},\frac a{a+b}\bigr)$

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

::: {#fig-invariant-distributions-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (6.4,0) node[lab, right] {$n$};
\draw[->] (0,0) -- (0,2.6) node[lab, above] {fraction of time in $0$};
\draw[emph] (0.010,2.400) -- (0.040,1.200) -- (0.070,1.714) -- (0.100,1.200) -- (0.130,1.477) -- (0.160,1.500) -- (0.190,1.263) -- (0.220,1.091) -- (0.250,0.960) -- (0.280,0.857) -- (0.310,0.852) -- (0.340,0.776) -- (0.370,0.714) -- (0.400,0.840) -- (0.430,0.781) -- (0.460,0.730) -- (0.490,0.686) -- (0.520,0.692) -- (0.550,0.698) -- (0.580,0.662) -- (0.610,0.708) -- (0.640,0.675) -- (0.670,0.752) -- (0.700,0.720) -- (0.730,0.690) -- (0.760,0.663) -- (0.790,0.729) -- (0.820,0.761) -- (0.850,0.734) -- (0.880,0.709) -- (0.910,0.738) -- (0.940,0.766) -- (0.970,0.767) -- (1.000,0.768) -- (1.030,0.816) -- (1.060,0.838) -- (1.090,0.815) -- (1.120,0.793) -- (1.150,0.772) -- (1.180,0.753) -- (1.210,0.774) -- (1.240,0.755) -- (1.270,0.756) -- (1.300,0.738) -- (1.330,0.722) -- (1.360,0.741) -- (1.390,0.742) -- (1.420,0.727) -- (1.450,0.712) -- (1.480,0.697) -- (1.510,0.699) -- (1.540,0.701) -- (1.570,0.718) -- (1.600,0.705) -- (1.630,0.692) -- (1.660,0.680) -- (1.690,0.710) -- (1.720,0.740) -- (1.750,0.741) -- (1.780,0.728) -- (1.810,0.716) -- (1.840,0.704) -- (1.870,0.732) -- (1.900,0.733) -- (1.930,0.721) -- (1.960,0.747) -- (1.990,0.760) -- (2.020,0.749) -- (2.050,0.773) -- (2.080,0.773) -- (2.110,0.773) -- (2.140,0.796) -- (2.170,0.807) -- (2.200,0.796) -- (2.230,0.786) -- (2.260,0.775) -- (2.290,0.765) -- (2.320,0.755) -- (2.350,0.746) -- (2.380,0.736) -- (2.410,0.737) -- (2.440,0.738) -- (2.470,0.738) -- (2.500,0.730) -- (2.530,0.721) -- (2.560,0.713) -- (2.590,0.723) -- (2.620,0.715) -- (2.650,0.706) -- (2.680,0.699) -- (2.710,0.691) -- (2.740,0.683) -- (2.770,0.676) -- (2.800,0.669) -- (2.830,0.661) -- (2.860,0.655) -- (2.890,0.648) -- (2.920,0.658) -- (2.950,0.675) -- (2.980,0.685) -- (3.010,0.678) -- (3.040,0.679) -- (3.070,0.680) -- (3.100,0.697) -- (3.130,0.713) -- (3.160,0.714) -- (3.190,0.707) -- (3.220,0.701) -- (3.250,0.702) -- (3.280,0.702) -- (3.310,0.696) -- (3.340,0.690) -- (3.370,0.684) -- (3.400,0.678) -- (3.430,0.672) -- (3.460,0.673) -- (3.490,0.674) -- (3.520,0.668) -- (3.550,0.663) -- (3.580,0.657) -- (3.610,0.652) -- (3.640,0.666) -- (3.670,0.680) -- (3.700,0.694) -- (3.730,0.688) -- (3.760,0.683) -- (3.790,0.678) -- (3.820,0.672) -- (3.850,0.686) -- (3.880,0.680) -- (3.910,0.681) -- (3.940,0.694) -- (3.970,0.695) -- (4.000,0.690) -- (4.030,0.685) -- (4.060,0.680) -- (4.090,0.675) -- (4.120,0.670) -- (4.150,0.665) -- (4.180,0.678) -- (4.210,0.673) -- (4.240,0.674) -- (4.270,0.686) -- (4.300,0.692) -- (4.330,0.693) -- (4.360,0.688) -- (4.390,0.683) -- (4.420,0.679) -- (4.450,0.685) -- (4.480,0.686) -- (4.510,0.681) -- (4.540,0.687) -- (4.570,0.693) -- (4.600,0.689) -- (4.630,0.684) -- (4.660,0.680) -- (4.690,0.691) -- (4.720,0.692) -- (4.750,0.687) -- (4.780,0.683) -- (4.810,0.679) -- (4.840,0.689) -- (4.870,0.690) -- (4.900,0.686) -- (4.930,0.696) -- (4.960,0.706) -- (4.990,0.712) -- (5.020,0.712) -- (5.050,0.708) -- (5.080,0.704) -- (5.110,0.700) -- (5.140,0.696) -- (5.170,0.692) -- (5.200,0.688) -- (5.230,0.684) -- (5.260,0.680) -- (5.290,0.681) -- (5.320,0.690) -- (5.350,0.686) -- (5.380,0.683) -- (5.410,0.679) -- (5.440,0.679) -- (5.470,0.684) -- (5.500,0.689) -- (5.530,0.699) -- (5.560,0.708) -- (5.590,0.713) -- (5.620,0.709) -- (5.650,0.705) -- (5.680,0.701) -- (5.710,0.698) -- (5.740,0.702) -- (5.770,0.711) -- (5.800,0.708) -- (5.830,0.708) -- (5.860,0.713) -- (5.890,0.713) -- (5.920,0.718) -- (5.950,0.718) -- (5.980,0.714);
\draw[hl, dashed] (0,0.6) -- (6.1,0.6);
\draw (0,0.6) -- (-0.08,0.6) node[tick, left] {$\pi_0$};
\draw (0,2.4) -- (-0.08,2.4) node[tick, left] {$1$};
\draw (6,0) -- (6,-0.08) node[tick, below] {$600$};
\end{tikzpicture}
\end{center}
```

The fraction of the first $n$ steps spent in state $0$ by one run of the two-state chain with $a=0.3$, $b=0.1$. It approaches $\pi_0=\tfrac14$

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
