---
title: "The Poisson Process"
sources: [eecs126hw-8, eecs126d-7, eecs126d-8]
requires: [math/probability/joint-distributions/joint-distributions, math/probability/distributions/poisson-distribution]
aliases: [math/probability/random-processes/poisson-process]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley EECS126 (Fall 2021), Homework 8 and Discussions 7–8, in our own wording; proofs written out in steps. -->

Arrivals that happen "completely at random in time" (calls, packets, radioactive decays) are modelled by the Poisson process.

::: {#def-poisson-process .definition name="Poisson process"}

Let $S_1,S_2,\dots$ be independent $\operatorname{Exp}(\lambda)$ random variables and $T_n=S_1+\dots+S_n$. The counting process
$$N(t)=\max\{n\ge0:T_n\le t\},\qquad t\ge0,$$
is a *Poisson process of rate $\lambda$*. The $T_n$ are the *arrival times* and the $S_n$ the *interarrival times*.

:::

::: {#fig-poisson-process-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.1]
\draw[->] (0,0) -- (6.6,0) node[lab, right] {$t$};
\draw[->] (0,0) -- (0,3.6);
\draw[emph, primary] (0,0.0) -- (0.6,0.0);
\draw[faint, dashed] (0.6,0.0) -- (0.6,0.45);
\draw[emph, primary] (0.6,0.45) -- (1.1,0.45);
\draw[faint, dashed] (1.1,0.45) -- (1.1,0.9);
\draw[emph, primary] (1.1,0.9) -- (2.4,0.9);
\draw[faint, dashed] (2.4,0.9) -- (2.4,1.35);
\draw[emph, primary] (2.4,1.35) -- (2.9,1.35);
\draw[faint, dashed] (2.9,1.35) -- (2.9,1.8);
\draw[emph, primary] (2.9,1.8) -- (3.2,1.8);
\draw[faint, dashed] (3.2,1.8) -- (3.2,2.25);
\draw[emph, primary] (3.2,2.25) -- (4.6,2.25);
\draw[faint, dashed] (4.6,2.25) -- (4.6,2.7);
\draw[emph, primary] (4.6,2.7) -- (5.5,2.7);
\draw[faint, dashed] (5.5,2.7) -- (5.5,3.15);
\draw[emph, primary] (5.5,3.15) -- (6.2,3.15) node[lab, right] {$N(t)$};
\fill[ink] (0.6,0) circle[pt];
\fill[ink] (1.1,0) circle[pt];
\fill[ink] (2.4,0) circle[pt];
\fill[ink] (2.9,0) circle[pt];
\fill[ink] (3.2,0) circle[pt];
\fill[ink] (4.6,0) circle[pt];
\fill[ink] (5.5,0) circle[pt];
\node[tick, below] at (0.6,0) {$T_1$}; \node[tick, below] at (1.1,0) {$T_2$}; \node[tick, below] at (2.4,0) {$T_3$};
\draw[decorate, decoration={brace, mirror, amplitude=3pt}, accent] (0,-0.45) -- node[lab, below=2pt] {$S_1$} (0.6,-0.45);
\draw[decorate, decoration={brace, mirror, amplitude=3pt}, accent] (1.1,-0.45) -- node[lab, below=2pt] {$S_3$} (2.4,-0.45);
\foreach \k in {1,2,3} \node[tick, left] at (0,{\k*0.9}) {$\pgfmathparse{int(2*\k)}\pgfmathresult$};
\end{tikzpicture}
\end{center}
```

A path of a Poisson process: arrivals $T_1<T_2<\dots$ on the time axis, separated by independent $\operatorname{Exp}(\lambda)$ gaps $S_n$, and the count $N(t)$, which jumps by $1$ at each arrival.

:::

::: {#thm-poisson-process-counts .theorem name="Counts of a Poisson process"}

For a Poisson process of rate $\lambda$:

1. $T_n$ has the Erlang (gamma) density $f_{T_n}(t)=\lambda^nt^{n-1}e^{-\lambda t}/(n-1)!$ for $t>0$;
2. $N(t)\sim\operatorname{Poisson}(\lambda t)$;
3. for $0\le t_0<t_1<\dots<t_k$, the increments $N(t_1)-N(t_0),\dots,N(t_k)-N(t_{k-1})$ are independent, with $N(t_j)-N(t_{j-1})\sim\operatorname{Poisson}(\lambda(t_j-t_{j-1}))$.

:::

::: {.proof}

1. By induction on $n$. For $n=1$ it is the exponential density. If it holds for $n$, the density of $T_{n+1}=T_n+S_{n+1}$ is the convolution
   $$\int_0^t\frac{\lambda^ns^{n-1}e^{-\lambda s}}{(n-1)!}\,\lambda e^{-\lambda(t-s)}\,ds=\frac{\lambda^{n+1}e^{-\lambda t}}{(n-1)!}\int_0^ts^{n-1}\,ds=\frac{\lambda^{n+1}t^ne^{-\lambda t}}{n!}.$$

2. $N(t)=n$ means $T_n\le t<T_n+S_{n+1}$. Conditioning on $T_n=s$ and using independence of $S_{n+1}$,
   $$\Pr(N(t)=n)=\int_0^tf_{T_n}(s)e^{-\lambda(t-s)}\,ds=\frac{\lambda^ne^{-\lambda t}}{(n-1)!}\int_0^ts^{n-1}\,ds=e^{-\lambda t}\frac{(\lambda t)^n}{n!}.$$

3. By memorylessness (@def-exponential-distribution), at time $t_1$ the time to the next arrival is again $\operatorname{Exp}(\lambda)$ and independent of the past, and later interarrival times are fresh. So the process after $t_1$, shifted, is a new Poisson process independent of $N$ on $[0,t_1]$; apply step 2 to each interval and repeat.

:::

::: {#fig-poisson-process-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (6.6,0) node[lab, right] {$t$};
\draw[->] (0,0) -- (0,2.9) node[lab, above] {$N(t)$};
\draw[emph] (0.000,0.000) -- (1.551,0.000) -- (1.551,0.300) -- (2.733,0.300) -- (2.733,0.600) -- (3.187,0.600) -- (3.187,0.900) -- (3.437,0.900) -- (3.437,1.200) -- (4.034,1.200) -- (4.034,1.500) -- (4.466,1.500) -- (4.466,1.800) -- (5.743,1.800) -- (5.743,2.100) -- (5.943,2.100);
\draw[hl, dashed] (0,0) -- (6,2.16);
\node[tick, text=accent] at (5.6,2.5) {$\lambda t$};
\end{tikzpicture}
\end{center}
```

The counting path $N(t)$ of a Poisson process of rate $\lambda=1.2$: it jumps by $1$ at each arrival, and $N(t)\sim\operatorname{Poisson}(\lambda t)$ grows along the line $\lambda t$ on average

:::

::: {#thm-poisson-merging-splitting .theorem name="Merging and splitting"}

1. *Merging.* If $N_1$ and $N_2$ are independent Poisson processes of rates $\lambda_1,\lambda_2$, then $N_1+N_2$ is a Poisson process of rate $\lambda_1+\lambda_2$, and each arrival comes from $N_1$ with probability $\lambda_1/(\lambda_1+\lambda_2)$, independently of everything else.
2. *Splitting.* If each arrival of a Poisson process of rate $\lambda$ is marked type 1 with probability $p$ and type 2 otherwise, independently, then the type-1 and type-2 arrivals form *independent* Poisson processes of rates $\lambda p$ and $\lambda(1-p)$.

:::

::: {.proof}

1. After any arrival of the merged process, both component processes restart afresh (memorylessness), so the time to the next merged arrival is the minimum of independent $\operatorname{Exp}(\lambda_1)$ and $\operatorname{Exp}(\lambda_2)$ variables. By @prp-min-of-exponentials it is $\operatorname{Exp}(\lambda_1+\lambda_2)$ and comes from $N_1$ with probability $\lambda_1/(\lambda_1+\lambda_2)$, independently of its length. Successive gaps are therefore i.i.d. exponential.

2. For splitting, it is enough to check increments over one interval of length $t$ (independence over disjoint intervals is inherited). Given $N(t)=n$, the number of type-1 arrivals is $\operatorname{Bin}(n,p)$, so
   $$\Pr(N_1=a,N_2=b)=e^{-\lambda t}\frac{(\lambda t)^{a+b}}{(a+b)!}\binom{a+b}{a}p^a(1-p)^b=e^{-\lambda pt}\frac{(\lambda pt)^a}{a!}\cdot e^{-\lambda(1-p)t}\frac{(\lambda(1-p)t)^b}{b!}.$$

3. The joint probability factorises into two Poisson probabilities, so the counts are independent Poisson variables with the stated means.

:::

::: {#fig-poisson-process-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0,1.2) -- (6.4,1.2);
\node[tick, left] at (0,1.2) {$\lambda_1$};
\node[hl dot] at (0.34,1.2) {};
\node[hl dot] at (0.47,1.2) {};
\node[hl dot] at (1.10,1.2) {};
\node[hl dot] at (1.31,1.2) {};
\node[hl dot] at (1.40,1.2) {};
\node[hl dot] at (2.04,1.2) {};
\node[hl dot] at (5.17,1.2) {};
\draw[faint] (0,0.6) -- (6.4,0.6);
\node[tick, left] at (0,0.6) {$\lambda_2$};
\node[dot] at (2.90,0.6) {};
\node[dot] at (3.40,0.6) {};
\node[dot] at (4.94,0.6) {};
\node[dot] at (5.59,0.6) {};
\node[dot] at (5.97,0.6) {};
\node[dot] at (6.19,0.6) {};
\draw[faint] (0,0) -- (6.4,0);
\node[tick, left] at (0,0) {$\lambda_1+\lambda_2$};
\node[hl dot] at (0.34,0) {};
\node[hl dot] at (0.47,0) {};
\node[hl dot] at (1.10,0) {};
\node[hl dot] at (1.31,0) {};
\node[hl dot] at (1.40,0) {};
\node[hl dot] at (2.04,0) {};
\node[hl dot] at (2.90,0) {};
\node[hl dot] at (3.40,0) {};
\node[hl dot] at (4.94,0) {};
\node[hl dot] at (5.17,0) {};
\node[hl dot] at (5.59,0) {};
\node[hl dot] at (5.97,0) {};
\node[hl dot] at (6.19,0) {};
\end{tikzpicture}
\end{center}
```

Merging independent Poisson processes of rates $\lambda_1$ and $\lambda_2$ gives a Poisson process of rate $\lambda_1+\lambda_2$; each merged arrival came from the first with probability $\lambda_1/(\lambda_1+\lambda_2)$

:::

::: {#thm-poisson-arrivals-uniform .theorem name="Arrivals given the count"}

Given $N(t)=n$, the arrival times $T_1<\dots<T_n$ have the same joint distribution as the sorted values of $n$ independent uniform random variables on $[0,t]$.

:::

::: {.proof}

1. The interarrival times have joint density $\prod_{k=1}^{n+1}\lambda e^{-\lambda s_k}$. Changing variables to $t_k=s_1+\dots+s_k$ (Jacobian $1$, @thm-change-of-variables-density), $(T_1,\dots,T_{n+1})$ has density $\lambda^{n+1}e^{-\lambda t_{n+1}}$ on $0<t_1<\dots<t_{n+1}$.

2. The event $N(t)=n$ is $T_n\le t<T_{n+1}$. Integrating out $t_{n+1}>t$ gives density $\lambda^ne^{-\lambda t}$ for $(T_1,\dots,T_n)$ on $0<t_1<\dots<t_n\le t$, together with $N(t)=n$.

3. Dividing by $\Pr(N(t)=n)=e^{-\lambda t}(\lambda t)^n/n!$ gives the constant density $n!/t^n$ on the ordered region, which is the density of the order statistics of $n$ uniform points.

:::

::: {#fig-poisson-process-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[emph] (0,0) -- (6,0);
\draw (0,0.1) -- (0,-0.1) node[tick, below] {$0$};
\draw (6,0.1) -- (6,-0.1) node[tick, below] {$t$};
\node[hl dot] at (0.07,0) {};
\node[hl dot] at (0.86,0) {};
\node[hl dot] at (2.25,0) {};
\node[hl dot] at (2.85,0) {};
\node[hl dot] at (3.94,0) {};
\node[hl dot] at (4.00,0) {};
\node[tick, above] at (3,0.25) {given $N(t)=6$};
\end{tikzpicture}
\end{center}
```

Given that $6$ arrivals fall in $[0,t]$, their times are distributed like $6$ independent uniform points on $[0,t]$, sorted

:::

::: {#exm-poisson-process-bus .example name="Waiting for a bus"}

Buses arrive as a Poisson process of rate $\lambda=6$ per hour. The number in a 20-minute window is $\operatorname{Poisson}(2)$, so no bus comes with probability $e^{-2}\approx0.135$. If red and blue buses each arrive at rate $3$ per hour (splitting with $p=\tfrac12$), the probability that the next two buses are both red is $\tfrac14$, and the expected wait for the first blue bus is $20$ minutes no matter how many red ones have passed.

:::
