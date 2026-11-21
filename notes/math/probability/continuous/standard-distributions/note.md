---
title: "Standard Distributions"
sources: []
requires: [math/probability/discrete/uniform-distribution, math/probability/discrete/hypergeometric-distribution, math/probability/discrete/poisson-distribution, math/probability/continuous/exponential-distribution, math/probability/continuous/central-limit-theorem]
aliases: [math/probability/standard-distributions, math/probability/discrete/standard-distributions]   # old ids (moved)
status: draft
---

<!-- Overview of the standard distributions. Started after the split of 2026-11-16 (SPEC §2.6); expanded on 2026-11-17 to all discrete and continuous distributions in these notes and moved to the end of the continuous branch. The comparison is our own; no external source. -->

Each distribution has its own note; this note puts them side by side and shows how they are related.

## Discrete distributions

|  | values | $E[X]$ | $\mathrm{Var}(X)$ | $X$ is |
|---|---|---|---|---|
| $\mathrm{Unif}(a,b)$ (@def-discrete-uniform-distribution) | $a,\dots,b$ | $\frac{a+b}2$ | $\frac{(b-a+1)^2-1}{12}$ | one of $a,\dots,b$, all equally likely |
| $\mathrm{Bernoulli}(p)$ (@def-bernoulli-distribution) | $0,1$ | $p$ | $p(1-p)$ | $1$ if a single trial succeeds |
| $\mathrm{Bin}(n,p)$ (@def-binomial-distribution) | $0,\dots,n$ | $np$ | $np(1-p)$ | the number of successes in $n$ independent trials |
| $\mathrm{Hypergeometric}(N,B,n)$ (@def-hypergeometric-distribution) | $0,\dots,n$ | $n\frac BN$ | $n\frac BN\bigl(1-\frac BN\bigr)\frac{N-n}{N-1}$ | the number of black balls in $n$ draws without replacement |
| $\mathrm{Poisson}(\mu)$ (@def-poisson-distribution) | $0,1,2,\dots$ | $\mu$ | $\mu$ | the number of events in an interval, at a steady rate |
| $\mathrm{Geom}(p)$ (@def-geometric-distribution) | $1,2,3,\dots$ | $\frac1p$ | $\frac{1-p}{p^2}$ | the number of trials up to the first success |

## Continuous distributions

|  | density | $E[X]$ | $\mathrm{Var}(X)$ | $X$ is |
|---|---|---|---|---|
| $U[a,b]$ (@def-continuous-uniform-distribution) | $\frac1{b-a}$ | $\frac{a+b}2$ | $\frac{(b-a)^2}{12}$ | a uniformly random point of $[a,b]$ |
| $\mathrm{Exp}(\lambda)$ (@def-exponential-distribution) | $\lambda e^{-\lambda x}$ | $\frac1\lambda$ | $\frac1{\lambda^2}$ | a waiting time at a constant rate |
| $N(\mu,\sigma^2)$ (@def-normal-distribution) | $\frac1{\sqrt{2\pi\sigma^2}}e^{-(x-\mu)^2/(2\sigma^2)}$ | $\mu$ | $\sigma^2$ | approximately, a sum of many independent effects |

The variance of $U[a,b]$ follows from @prp-continuous-uniform-mean-variance by shifting: $U[a,b]$ is $a$ plus $U[0,b-a]$. The mean and variance of the hypergeometric distribution are @prp-hypergeometric-mean-variance.

## How they are related

::: {#fig-standard-distributions-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\node[box] (geo) at (-4.8,2.4) {$\mathrm{Geom}(p)$};
\node[box] (bern) at (0,2.4) {Bernoulli$(p)$};
\node[box] (exp) at (-4.8,0) {$\mathrm{Exp}(\lambda)$};
\node[box] (bin) at (0,0) {$\mathrm{Bin}(n,p)$};
\node[box] (poi) at (5,0) {$\mathrm{Poisson}(np)$};
\node[box] (hyp) at (0,-2.4) {Hypergeometric};
\node[hl box] (nor) at (5,-2.4) {$N(\mu,\sigma^2)$};
\draw[->] (bern) -- node[edge label] {sum of $n$} (bin);
\draw[->] (bern) -- node[edge label] {first success} (geo);
\draw[->] (geo) -- node[edge label] {time step $\to0$} (exp);
\draw[->] (hyp) -- node[edge label] {$N\to\infty$} (bin);
\draw[->] (bin) -- node[edge label] {$n\to\infty$, $np$ fixed} (poi);
\draw[->] (bin) -- node[edge label] {$n\to\infty$ (CLT)} (nor);
\draw[->] (poi) -- node[edge label] {$\mu\to\infty$} (nor);
\end{tikzpicture}
\end{center}
```

How the standard distributions arise from each other. An arrow is an exact construction (a sum, a waiting time) or a limit.

:::

::: {#fig-standard-distributions-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[shift={(0,0)}]
\draw[faint] (0,0) -- (2.2,0);
\path[bar] (0.525,0) rectangle (0.875,0.720);
\path[bar] (1.325,0) rectangle (1.675,1.080);
\node[tick, below] at (1.1,0) {Bernoulli};
\end{scope}
\begin{scope}[shift={(2.8,0)}]
\draw[faint] (0,0) -- (2.2,0);
\path[bar] (0.075,0) rectangle (0.225,0.067);
\path[bar] (0.315,0) rectangle (0.465,0.358);
\path[bar] (0.555,0) rectangle (0.705,0.836);
\path[bar] (0.795,0) rectangle (0.945,1.115);
\path[bar] (1.035,0) rectangle (1.185,0.929);
\path[bar] (1.275,0) rectangle (1.425,0.495);
\path[bar] (1.515,0) rectangle (1.665,0.165);
\path[bar] (1.755,0) rectangle (1.905,0.031);
\path[bar] (1.995,0) rectangle (2.145,0.003);
\node[tick, below] at (1.1,0) {binomial};
\end{scope}
\begin{scope}[shift={(5.6,0)}]
\draw[faint] (0,0) -- (2.2,0);
\path[bar] (0.075,0) rectangle (0.225,1.050);
\path[bar] (0.315,0) rectangle (0.465,0.682);
\path[bar] (0.555,0) rectangle (0.705,0.444);
\path[bar] (0.795,0) rectangle (0.945,0.288);
\path[bar] (1.035,0) rectangle (1.185,0.187);
\path[bar] (1.275,0) rectangle (1.425,0.122);
\path[bar] (1.515,0) rectangle (1.665,0.079);
\path[bar] (1.755,0) rectangle (1.905,0.051);
\path[bar] (1.995,0) rectangle (2.145,0.033);
\node[tick, below] at (1.1,0) {geometric};
\end{scope}
\begin{scope}[shift={(8.4,0)}]
\draw[faint] (0,0) -- (2.2,0);
\path[bar] (0.075,0) rectangle (0.225,0.474);
\path[bar] (0.315,0) rectangle (0.465,0.947);
\path[bar] (0.555,0) rectangle (0.705,0.947);
\path[bar] (0.795,0) rectangle (0.945,0.632);
\path[bar] (1.035,0) rectangle (1.185,0.316);
\path[bar] (1.275,0) rectangle (1.425,0.126);
\path[bar] (1.515,0) rectangle (1.665,0.042);
\path[bar] (1.755,0) rectangle (1.905,0.012);
\path[bar] (1.995,0) rectangle (2.145,0.003);
\node[tick, below] at (1.1,0) {Poisson};
\end{scope}
\begin{scope}[shift={(0,-1.8)}]
\draw[faint] (0,0) -- (2.2,0);
\draw[emph] (0.3,0) -- (0.3,0.8) -- (1.9,0.8) -- (1.9,0);
\node[tick, below] at (1.1,0) {uniform};
\end{scope}
\begin{scope}[shift={(2.8,-1.8)}]
\draw[faint] (0,0) -- (2.2,0);
\draw[emph, domain=0.05:2.2, samples=80, smooth, variable=\x] plot ({\x}, {1.1*exp(-1.6*\x)});
\node[tick, below] at (1.1,0) {exponential};
\end{scope}
\begin{scope}[shift={(5.6,-1.8)}]
\draw[faint] (0,0) -- (2.2,0);
\draw[emph, domain=0:2.2, samples=80, smooth, variable=\x] plot ({\x}, {0.9*exp(-((\x-1.1)^2)/(2*0.4^2))/(0.4*sqrt(2*pi))});
\node[tick, below] at (1.1,0) {normal};
\end{scope}
\begin{scope}[shift={(8.4,-1.8)}]
\draw[faint] (0,0) -- (2.2,0);
\draw[emph, domain=0:2.2, samples=80, smooth, variable=\x] plot ({\x}, {2.2*\x*\x*exp(-2.5*\x)*1.6});
\node[tick, below] at (1.1,0) {gamma};
\end{scope}
\end{tikzpicture}
\end{center}
```

The shapes of the standard distributions: discrete ones on the top row (bars) and continuous densities below

:::

- **Sums of Bernoulli trials.** $\mathrm{Bin}(n,p)$ is the sum of $n$ independent $\mathrm{Bernoulli}(p)$ variables, and $\mathrm{Geom}(p)$ is the number of them up to the first success.
- **With and without replacement.** For $N$ much larger than $n$, the factor $\frac{N-n}{N-1}$ is close to $1$, and $\mathrm{Hypergeometric}(N,B,n)\approx\mathrm{Bin}(n,\frac BN)$ (@sec-math-probability-discrete-hypergeometric-distribution).
- **Rare events.** For large $n$ and small $p$, $\mathrm{Bin}(n,p)\approx\mathrm{Poisson}(np)$ (@thm-poisson-as-a-limit-of).
- **Discrete to continuous time.** Geometric waiting times with success probability $\lambda\delta$ per step of length $\delta$ tend to $\mathrm{Exp}(\lambda)$ (@prp-exponential-geometric-limit).
- **Many small effects.** By the central limit theorem (@thm-central-limit-theorem), a standardized sum of many i.i.d. variables is close to $N(0,1)$. So $\mathrm{Bin}(n,p)$ for large $n$, and $\mathrm{Poisson}(\mu)$ for large $\mu$ (a sum of $\mu$ independent $\mathrm{Poisson}(1)$ variables when $\mu$ is a whole number, @thm-sum-of-poissons), are close to normal.
- **Memorylessness.** Among these, only the geometric (discrete) and the exponential (continuous) distributions are memoryless (@prp-exponential-memoryless).
- **Shape.** Binomial, hypergeometric and both uniforms are bounded; Poisson, geometric and exponential have no upper limit; the normal is unbounded in both directions.
