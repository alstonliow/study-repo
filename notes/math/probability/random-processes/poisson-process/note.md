---
title: "The Poisson Process"
sources: [eecs126hw-8, eecs126d-7, eecs126d-8]
requires: [math/probability/continuous/joint-distributions, math/probability/discrete/poisson-distribution]
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

::: {#thm-poisson-arrivals-uniform .theorem name="Arrivals given the count"}

Given $N(t)=n$, the arrival times $T_1<\dots<T_n$ have the same joint distribution as the sorted values of $n$ independent uniform random variables on $[0,t]$.

:::

::: {.proof}

1. The interarrival times have joint density $\prod_{k=1}^{n+1}\lambda e^{-\lambda s_k}$. Changing variables to $t_k=s_1+\dots+s_k$ (Jacobian $1$, @thm-change-of-variables-density), $(T_1,\dots,T_{n+1})$ has density $\lambda^{n+1}e^{-\lambda t_{n+1}}$ on $0<t_1<\dots<t_{n+1}$.

2. The event $N(t)=n$ is $T_n\le t<T_{n+1}$. Integrating out $t_{n+1}>t$ gives density $\lambda^ne^{-\lambda t}$ for $(T_1,\dots,T_n)$ on $0<t_1<\dots<t_n\le t$, together with $N(t)=n$.

3. Dividing by $\Pr(N(t)=n)=e^{-\lambda t}(\lambda t)^n/n!$ gives the constant density $n!/t^n$ on the ordered region, which is the density of the order statistics of $n$ uniform points.

:::

::: {#exm-poisson-process-bus .example name="Waiting for a bus"}

Buses arrive as a Poisson process of rate $\lambda=6$ per hour. The number in a 20-minute window is $\operatorname{Poisson}(2)$, so no bus comes with probability $e^{-2}\approx0.135$. If red and blue buses each arrive at rate $3$ per hour (splitting with $p=\tfrac12$), the probability that the next two buses are both red is $\tfrac14$, and the expected wait for the first blue bus is $20$ minutes no matter how many red ones have passed.

:::
