---
title: "The Bernoulli Process"
sources: [mit6041-13]
requires: [math/probability/discrete/binomial-distribution, math/probability/discrete/geometric-distribution]
status: draft
---

<!-- Added 2026-11-20 from MIT 6.041 (Fall 2010), Lecture 13, in our own wording; proofs written out in steps. -->

The Bernoulli process is the discrete-time model of arrivals: in each time slot an arrival happens or not, independently. Its continuous-time limit is the Poisson process (@sec-math-probability-random-processes-poisson-process).

::: {#def-bernoulli-process .definition name="Bernoulli process"}

A *Bernoulli process with parameter $p$* is a sequence $X_1,X_2,\dots$ of independent random variables with $\Pr(X_t=1)=p$ and $\Pr(X_t=0)=1-p$. Slot $t$ has an *arrival* (success) when $X_t=1$. Write
$$S_n=X_1+\dots+X_n$$
for the number of arrivals in the first $n$ slots, $Y_k$ for the time of the $k$-th arrival, and $T_1=Y_1$, $T_k=Y_k-Y_{k-1}$ for the *interarrival times*.

:::

::: {#fig-bernoulli-process-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[xscale=0.75]
\draw[->] (0.3,0) -- (12.9,0) node[lab, right] {$t$};
\draw (1,-0.08) -- (1,0.08); \node[tick, below] at (1,-0.08) {$1$};
\draw (2,-0.08) -- (2,0.08); \node[tick, below] at (2,-0.08) {$2$};
\draw (3,-0.08) -- (3,0.08); \node[tick, below] at (3,-0.08) {$3$};
\draw (4,-0.08) -- (4,0.08); \node[tick, below] at (4,-0.08) {$4$};
\draw (5,-0.08) -- (5,0.08); \node[tick, below] at (5,-0.08) {$5$};
\draw (6,-0.08) -- (6,0.08); \node[tick, below] at (6,-0.08) {$6$};
\draw (7,-0.08) -- (7,0.08); \node[tick, below] at (7,-0.08) {$7$};
\draw (8,-0.08) -- (8,0.08); \node[tick, below] at (8,-0.08) {$8$};
\draw (9,-0.08) -- (9,0.08); \node[tick, below] at (9,-0.08) {$9$};
\draw (10,-0.08) -- (10,0.08); \node[tick, below] at (10,-0.08) {$10$};
\draw (11,-0.08) -- (11,0.08); \node[tick, below] at (11,-0.08) {$11$};
\draw (12,-0.08) -- (12,0.08); \node[tick, below] at (12,-0.08) {$12$};
\draw[emph, primary] (2,0) -- (2,0.7); \fill[ink] (2,0.7) circle[pt];
\draw[emph, primary] (3,0) -- (3,0.7); \fill[ink] (3,0.7) circle[pt];
\draw[emph, primary] (7,0) -- (7,0.7); \fill[ink] (7,0.7) circle[pt];
\draw[emph, primary] (11,0) -- (11,0.7); \fill[ink] (11,0.7) circle[pt];
\draw[faint, <->] (0.5,1.05) -- (1.95,1.05) node[lab, midway, above] {$T_1$};
\draw[faint, <->] (2.05,1.05) -- (2.95,1.05) node[lab, midway, above] {$T_2$};
\draw[faint, <->] (3.05,1.05) -- (6.95,1.05) node[lab, midway, above] {$T_3$};
\draw[faint, <->] (7.05,1.05) -- (10.95,1.05) node[lab, midway, above] {$T_4$};
\end{tikzpicture}
\end{center}
```

A Bernoulli process with arrivals in slots $2,3,7,11$: $Y_1,\dots,Y_4=2,3,7,11$ and interarrival times $2,1,4,4$.

:::

::: {#prp-bernoulli-counts .proposition name="Counts and first arrival"}

$S_n\sim\mathrm{Bin}(n,p)$, with mean $np$ and variance $np(1-p)$, and $T_1\sim\mathrm{Geom}(p)$, with mean $1/p$ and variance $(1-p)/p^2$.

:::

::: {.proof}

1. $S_n$ counts successes in $n$ independent trials, which is the binomial model (@def-binomial-distribution).

2. $T_1=k$ exactly when slots $1,\dots,k-1$ are empty and slot $k$ has an arrival, with probability $(1-p)^{k-1}p$: the geometric law (@def-geometric-distribution).

:::

::: {#fig-bernoulli-process-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (6.6,0) node[lab, right] {$t$};
\draw[->] (0,0) -- (0,2.8) node[lab, above] {$N_t$};
\draw[emph] (0.000,0.000) -- (0.200,0.000) -- (0.200,0.250) -- (0.400,0.250) -- (0.400,0.250) -- (0.600,0.250) -- (0.600,0.250) -- (0.800,0.250) -- (0.800,0.250) -- (1.000,0.250) -- (1.000,0.250) -- (1.200,0.250) -- (1.200,0.500) -- (1.400,0.500) -- (1.400,0.750) -- (1.600,0.750) -- (1.600,0.750) -- (1.800,0.750) -- (1.800,1.000) -- (2.000,1.000) -- (2.000,1.250) -- (2.200,1.250) -- (2.200,1.250) -- (2.400,1.250) -- (2.400,1.250) -- (2.600,1.250) -- (2.600,1.250) -- (2.800,1.250) -- (2.800,1.250) -- (3.000,1.250) -- (3.000,1.250) -- (3.200,1.250) -- (3.200,1.500) -- (3.400,1.500) -- (3.400,1.500) -- (3.600,1.500) -- (3.600,1.500) -- (3.800,1.500) -- (3.800,1.500) -- (4.000,1.500) -- (4.000,1.500) -- (4.200,1.500) -- (4.200,1.500) -- (4.400,1.500) -- (4.400,1.750) -- (4.600,1.750) -- (4.600,1.750) -- (4.800,1.750) -- (4.800,1.750) -- (5.000,1.750) -- (5.000,1.750) -- (5.200,1.750) -- (5.200,2.000) -- (5.400,2.000) -- (5.400,2.000) -- (5.600,2.000) -- (5.600,2.000) -- (5.800,2.000) -- (5.800,2.000) -- (6.000,2.000) -- (6.000,2.000) -- (6.200,2.000);
\draw[hl, dashed] (0,0) -- (6.0,2.25);
\node[tick, text=accent] at (5.3,2.2) {$E[N_t]=pt$};
\end{tikzpicture}
\end{center}
```

The number of arrivals $N_t$ in the first $t$ slots of a Bernoulli process with $p=0.3$. It is $\operatorname{Bin}(t,p)$, so it grows along the line $pt$

:::

::: {#thm-bernoulli-fresh-start .theorem name="Fresh start"}

1. For every fixed $n$, the process $X_{n+1},X_{n+2},\dots$ is a Bernoulli process with parameter $p$, independent of $X_1,\dots,X_n$.
2. The same holds after a random time $N$ when the event $\{N=n\}$ is determined by $X_1,\dots,X_n$ alone (for example $N=Y_k$, the time of the $k$-th arrival).

:::

::: {.proof}

1. Part 1 is independence of the $X_t$: the future slots are independent, each with parameter $p$, and independent of the past slots.

2. For part 2 fix slots $x_1,\dots,x_m$ of the future and an event $B$ about the past. Split on the value of $N$:
$$\Pr(X_{N+1}=x_1,\dots,X_{N+m}=x_m,\ B)=\sum_n\Pr(N=n,\ B,\ X_{n+1}=x_1,\dots,X_{n+m}=x_m).$$

3. The event $\{N=n\}\cap B$ depends on $X_1,\dots,X_n$ only, so by part 1 each term factors as $\Pr(N=n,B)\prod_ip^{x_i}(1-p)^{1-x_i}$.

4. Summing over $n$ gives $\Pr(B)\prod_ip^{x_i}(1-p)^{1-x_i}$: the future after $N$ is a Bernoulli process independent of the past.

:::

Part 1 is *memorylessness*: given that slots $1,\dots,n$ were empty, the remaining wait $T_1-n$ is again $\mathrm{Geom}(p)$.

::: {#thm-bernoulli-interarrivals .theorem name="Interarrival and arrival times"}

The interarrival times $T_1,T_2,\dots$ are independent $\mathrm{Geom}(p)$ random variables. The $k$-th arrival time $Y_k=T_1+\dots+T_k$ has the *Pascal* PMF
$$\Pr(Y_k=t)=\binom{t-1}{k-1}p^k(1-p)^{t-k},\qquad t=k,k+1,\dots,$$
with $E[Y_k]=k/p$ and $\mathrm{Var}(Y_k)=k(1-p)/p^2$.

:::

::: {.proof}

1. By @thm-bernoulli-fresh-start applied at $N=Y_{k-1}$, the process after $Y_{k-1}$ is a fresh Bernoulli process independent of $T_1,\dots,T_{k-1}$, and $T_k$ is its first arrival time. So $T_k\sim\mathrm{Geom}(p)$, independent of the earlier ones.

2. $Y_k=t$ means: slot $t$ has an arrival and slots $1,\dots,t-1$ contain exactly $k-1$ arrivals. These are independent events with probabilities $p$ and $\binom{t-1}{k-1}p^{k-1}(1-p)^{t-k}$.

3. Mean and variance add over the independent $T_i$ (@prp-bernoulli-counts).

:::

::: {#thm-bernoulli-split-merge .theorem name="Splitting and merging"}

1. *Splitting.* Keep each arrival of a Bernoulli($p$) process independently with probability $q$. The kept arrivals form a Bernoulli($pq$) process, and so do the discarded ones with parameter $p(1-q)$; these two are not independent.
2. *Merging.* For independent Bernoulli processes with parameters $p$ and $q$, the slots with an arrival in at least one of them form a Bernoulli($p+q-pq$) process.

:::

::: {.proof}

1. Slot $t$ has a kept arrival when it has an arrival and the coin for it says keep: probability $pq$. Different slots use independent arrivals and independent coins, so the kept slots are independent.

2. The two split processes never both have an arrival in the same slot. So when $0<p$ and $0<q<1$, the probability of that is $0\ne pq\cdot p(1-q)$, and they are dependent.

3. For merging, slot $t$ is empty in the merged process exactly when it is empty in both, with probability $(1-p)(1-q)$, independently over $t$. So the arrival probability is $1-(1-p)(1-q)=p+q-pq$.

:::

::: {#fig-bernoulli-process-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0,1.2) -- (6.4,1.2);
\node[tick, left] at (0,1.2) {$p$};
\node[hl dot] at (0.60,1.2) {};
\node[hl dot] at (1.80,1.2) {};
\node[hl dot] at (3.40,1.2) {};
\node[hl dot] at (5.40,1.2) {};
\draw[faint] (0,0.6) -- (6.4,0.6);
\node[tick, left] at (0,0.6) {$q$};
\node[dot] at (1.00,0.6) {};
\node[dot] at (3.40,0.6) {};
\node[dot] at (4.60,0.6) {};
\draw[faint] (0,0) -- (6.4,0);
\node[tick, left] at (0,0) {merged};
\node[hl dot] at (0.60,0) {};
\node[hl dot] at (1.00,0) {};
\node[hl dot] at (1.80,0) {};
\node[hl dot] at (3.40,0) {};
\node[hl dot] at (4.60,0) {};
\node[hl dot] at (5.40,0) {};
\end{tikzpicture}
\end{center}
```

Merging two independent Bernoulli processes with parameters $p$ and $q$: a slot has an arrival if either has one, which gives a Bernoulli process with parameter $1-(1-p)(1-q)$

:::

::: {#rmk-bernoulli-to-poisson .remark name="From Bernoulli to Poisson" related="thm-poisson-as-a-limit-of"}

Cut time into slots of length $\delta$ and let $p=\lambda\delta$. In a fixed interval of length $t$ there are $t/\delta$ slots, so the count is $\mathrm{Bin}(t/\delta,\lambda\delta)$, which tends to $\mathrm{Poisson}(\lambda t)$ as $\delta\to0$; the geometric interarrival times, multiplied by $\delta$, tend to $\operatorname{Exp}(\lambda)$. The limit is the Poisson process (@def-poisson-process), and its merging and splitting rules (@thm-poisson-merging-splitting) are the limits of @thm-bernoulli-split-merge.

:::
