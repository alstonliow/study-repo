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

::: {#fig-countable-markov-chains-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (6.4,0) node[lab, right] {$n$};
\draw[->] (0,-1.6) -- (0,2.6) node[lab, above] {$X_n$};
\draw[emph] (0.000,0.000) -- (0.050,0.083) -- (0.100,0.000) -- (0.150,-0.083) -- (0.200,-0.167) -- (0.250,-0.083) -- (0.300,0.000) -- (0.350,0.083) -- (0.400,0.167) -- (0.450,0.083) -- (0.500,0.167) -- (0.550,0.083) -- (0.600,0.167) -- (0.650,0.250) -- (0.700,0.333) -- (0.750,0.250) -- (0.800,0.167) -- (0.850,0.250) -- (0.900,0.333) -- (0.950,0.417) -- (1.000,0.333) -- (1.050,0.250) -- (1.100,0.167) -- (1.150,0.083) -- (1.200,0.000) -- (1.250,-0.083) -- (1.300,-0.167) -- (1.350,-0.083) -- (1.400,-0.167) -- (1.450,-0.083) -- (1.500,-0.167) -- (1.550,-0.250) -- (1.600,-0.167) -- (1.650,-0.083) -- (1.700,0.000) -- (1.750,0.083) -- (1.800,0.167) -- (1.850,0.083) -- (1.900,0.000) -- (1.950,-0.083) -- (2.000,-0.167) -- (2.050,-0.250) -- (2.100,-0.333) -- (2.150,-0.250) -- (2.200,-0.333) -- (2.250,-0.250) -- (2.300,-0.167) -- (2.350,-0.083) -- (2.400,-0.167) -- (2.450,-0.083) -- (2.500,0.000) -- (2.550,-0.083) -- (2.600,0.000) -- (2.650,0.083) -- (2.700,0.167) -- (2.750,0.250) -- (2.800,0.333) -- (2.850,0.417) -- (2.900,0.500) -- (2.950,0.583) -- (3.000,0.500) -- (3.050,0.417) -- (3.100,0.500) -- (3.150,0.417) -- (3.200,0.333) -- (3.250,0.417) -- (3.300,0.500) -- (3.350,0.417) -- (3.400,0.333) -- (3.450,0.250) -- (3.500,0.333) -- (3.550,0.417) -- (3.600,0.333) -- (3.650,0.250) -- (3.700,0.167) -- (3.750,0.250) -- (3.800,0.167) -- (3.850,0.250) -- (3.900,0.167) -- (3.950,0.250) -- (4.000,0.167) -- (4.050,0.083) -- (4.100,0.000) -- (4.150,0.083) -- (4.200,0.000) -- (4.250,-0.083) -- (4.300,-0.167) -- (4.350,-0.083) -- (4.400,-0.167) -- (4.450,-0.083) -- (4.500,0.000) -- (4.550,0.083) -- (4.600,0.000) -- (4.650,0.083) -- (4.700,0.167) -- (4.750,0.250) -- (4.800,0.167) -- (4.850,0.083) -- (4.900,0.000) -- (4.950,0.083) -- (5.000,0.167) -- (5.050,0.250) -- (5.100,0.333) -- (5.150,0.417) -- (5.200,0.333) -- (5.250,0.417) -- (5.300,0.500) -- (5.350,0.583) -- (5.400,0.500) -- (5.450,0.583) -- (5.500,0.667) -- (5.550,0.750) -- (5.600,0.667) -- (5.650,0.750) -- (5.700,0.833) -- (5.750,0.917) -- (5.800,0.833) -- (5.850,0.750) -- (5.900,0.833) -- (5.950,0.750) -- (6.000,0.833);
\draw[hl] (0.000,0.000) -- (0.050,0.083) -- (0.100,0.167) -- (0.150,0.083) -- (0.200,0.000) -- (0.250,0.083) -- (0.300,0.000) -- (0.350,-0.083) -- (0.400,0.000) -- (0.450,0.083) -- (0.500,0.167) -- (0.550,0.250) -- (0.600,0.333) -- (0.650,0.417) -- (0.700,0.500) -- (0.750,0.583) -- (0.800,0.667) -- (0.850,0.750) -- (0.900,0.667) -- (0.950,0.750) -- (1.000,0.833) -- (1.050,0.750) -- (1.100,0.833) -- (1.150,0.917) -- (1.200,1.000) -- (1.250,1.083) -- (1.300,1.167) -- (1.350,1.250) -- (1.400,1.333) -- (1.450,1.250) -- (1.500,1.333) -- (1.550,1.250) -- (1.600,1.333) -- (1.650,1.417) -- (1.700,1.500) -- (1.750,1.583) -- (1.800,1.667) -- (1.850,1.750) -- (1.900,1.833) -- (1.950,1.750) -- (2.000,1.667) -- (2.050,1.750) -- (2.100,1.833) -- (2.150,1.917) -- (2.200,1.833) -- (2.250,1.917) -- (2.300,1.833) -- (2.350,1.917) -- (2.400,2.000) -- (2.450,2.083) -- (2.500,2.167) -- (2.550,2.083) -- (2.600,2.167) -- (2.650,2.250) -- (2.700,2.333) -- (2.750,2.417) -- (2.800,2.333) -- (2.850,2.417) -- (2.900,2.333) -- (2.950,2.250) -- (3.000,2.167) -- (3.050,2.250) -- (3.100,2.167) -- (3.150,2.250) -- (3.200,2.333) -- (3.250,2.417) -- (3.300,2.333) -- (3.350,2.250) -- (3.400,2.333) -- (3.450,2.417) -- (3.500,2.500) -- (3.550,2.417) -- (3.600,2.500) -- (3.650,2.583) -- (3.700,2.500) -- (3.750,2.583) -- (3.800,2.667) -- (3.850,2.750) -- (3.900,2.833) -- (3.950,2.750) -- (4.000,2.833) -- (4.050,2.750) -- (4.100,2.667) -- (4.150,2.583) -- (4.200,2.500) -- (4.250,2.583) -- (4.300,2.667) -- (4.350,2.583) -- (4.400,2.500) -- (4.450,2.583) -- (4.500,2.500) -- (4.550,2.583) -- (4.600,2.667) -- (4.650,2.583) -- (4.700,2.667) -- (4.750,2.750) -- (4.800,2.667) -- (4.850,2.750) -- (4.900,2.833) -- (4.950,2.917) -- (5.000,3.000) -- (5.050,3.083) -- (5.100,3.000) -- (5.150,3.083) -- (5.200,3.000) -- (5.250,2.917) -- (5.300,3.000) -- (5.350,2.917) -- (5.400,2.833) -- (5.450,2.917) -- (5.500,3.000) -- (5.550,3.083) -- (5.600,3.000) -- (5.650,3.083) -- (5.700,3.167) -- (5.750,3.250) -- (5.800,3.333) -- (5.850,3.417) -- (5.900,3.500) -- (5.950,3.583) -- (6.000,3.500);
\node[tick] at (5.6,-0.9) {$p=\tfrac12$};
\node[tick, text=accent] at (5.2,2.4) {$p=0.65$};
\end{tikzpicture}
\end{center}
```

Two walks on $\mathbb Z$ from $0$. The symmetric walk keeps coming back to $0$ (recurrent); with upward drift the walk leaves and returns only finitely often (transient)

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

::: {#fig-countable-markov-chains-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[vertex] (n0) at (0,0) {$-2$};
\node[vertex] (n1) at (1.5,0) {$-1$};
\node[vertex] (n2) at (3.0,0) {$0$};
\node[vertex] (n3) at (4.5,0) {$1$};
\node[vertex] (n4) at (6.0,0) {$2$};
\node[vertex] (n5) at (7.5,0) {$3$};
\draw[->] (n0) to[bend left=30] node[lab, tick, auto] {$p$} (n1);
\draw[->] (n1) to[bend left=30] node[lab, tick, auto] {$q$} (n0);
\draw[->] (n1) to[bend left=30] node[lab, tick, auto] {$p$} (n2);
\draw[->] (n2) to[bend left=30] node[lab, tick, auto] {$q$} (n1);
\draw[->] (n2) to[bend left=30] node[lab, tick, auto] {$p$} (n3);
\draw[->] (n3) to[bend left=30] node[lab, tick, auto] {$q$} (n2);
\draw[->] (n3) to[bend left=30] node[lab, tick, auto] {$p$} (n4);
\draw[->] (n4) to[bend left=30] node[lab, tick, auto] {$q$} (n3);
\draw[->] (n4) to[bend left=30] node[lab, tick, auto] {$p$} (n5);
\draw[->] (n5) to[bend left=30] node[lab, tick, auto] {$q$} (n4);
\node[lab] at (-1.0,0) {$\cdots$};
\node[lab] at (8.5,0) {$\cdots$};
\end{tikzpicture}
\end{center}
```

The random walk on $\mathbb Z$: up with probability $p$, down with $q=1-p$. It is recurrent when $p=\tfrac12$ and transient otherwise

:::

::: {#exm-birth-death-chain .example name="Reflected random walk"}

On $\{0,1,2,\dots\}$ move up with probability $p$ and down with probability $q=1-p$ (staying at $0$ instead of going down). The balance equations $\pi(i)p=\pi(i+1)q$ give $\pi(i)=\pi(0)(p/q)^i$. If $p<q$ this sums to a distribution, $\pi(i)=(1-\rho)\rho^i$ with $\rho=p/q$, and the chain is positive recurrent; if $p\ge q$ there is no invariant distribution.

:::

::: {#fig-countable-markov-chains-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \i in {0,...,3} \node[small vertex] (s\i) at (1.8*\i,0) {$\i$};
\node[lab] (s4) at (7.2,0) {$\cdots$};
\foreach \i/\j in {0/1,1/2,2/3,3/4} { \draw[->] (s\i) to[bend left=30] node[edge label, above] {$p$} (s\j); \draw[->] (s\j) to[bend left=30] node[edge label, below] {$q$} (s\i); }
\draw[->] (s0) to[out=200, in=160, looseness=6] node[edge label, left] {$q$} (s0);
\end{tikzpicture}
\end{center}
```

The reflected random walk of @exm-birth-death-chain. Up with probability $p$, down with probability $q$, and at $0$ a down step stays put. When $p<q$ the drift towards $0$ makes the chain positive recurrent with $\pi(i)=(1-\rho)\rho^i$.

:::
