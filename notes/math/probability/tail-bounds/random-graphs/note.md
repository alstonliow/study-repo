---
title: "Random Graphs"
sources: [eecs126-5]
requires: [math/probability/tail-bounds/concentration-inequalities]
aliases: [math/probability/discrete/random-graphs]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley EECS126 (Fall 2021), note "Random Graphs", in our own wording; proofs written out in steps. -->

The Erdős–Rényi random graph is the simplest model of a random network. Many of its properties switch on abruptly as the edge probability crosses a threshold.

::: {#def-erdos-renyi-graph .definition name="Erdős–Rényi random graph"}

$G(n,p)$ is the random graph on vertices $\{1,\dots,n\}$ in which each of the $\binom n2$ possible edges is present with probability $p$, independently of the others.

:::

Each vertex has $\operatorname{Bin}(n-1,p)$ neighbours, so the mean degree is $(n-1)p$, and the expected number of edges is $\binom n2p$.

::: {#lem-second-moment-method .lemma name="First and second moment methods"}

Let $Z\ge0$ be an integer-valued random variable.

1. $\Pr(Z>0)\le E[Z]$.
2. If $E[Z]>0$, then $\Pr(Z=0)\le\dfrac{\operatorname{Var}(Z)}{E[Z]^2}$.

:::

::: {.proof}

1. $\mathbf 1\{Z>0\}\le Z$; take expectations (or use Markov's inequality, @thm-markov-inequality).

2. If $Z=0$ then $|Z-E[Z]|\ge E[Z]$, so Chebyshev's inequality (@thm-chebyshev-s-inequality) gives $\Pr(Z=0)\le\operatorname{Var}(Z)/E[Z]^2$.

:::

::: {#thm-connectivity-threshold .theorem name="Sharp threshold for connectivity"}

Let $p=p(n)=\lambda\dfrac{\ln n}{n}$ for a constant $\lambda>0$.

1. If $\lambda>1$, then $\Pr(G(n,p)\text{ is connected})\to1$.
2. If $\lambda<1$, then $\Pr(G(n,p)\text{ is connected})\to0$.

:::

::: {#fig-random-graphs-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (7.4,0) node[lab, right] {$c$};
\draw[->] (0,0) -- (0,2.6) node[lab, above] {$\Pr(\text{connected})$};
\draw[emph, domain=0:7.2, samples=80, smooth, variable=\x] plot ({\x}, {2.2*exp(-exp(-(\x-3.5)))});
\draw (3.5,0) -- (3.5,-0.08) node[tick, below] {$0$};
\draw (1.5,0) -- (1.5,-0.08) node[tick, below] {$-2$};
\draw (5.5,0) -- (5.5,-0.08) node[tick, below] {$2$};
\draw (0,2.2) -- (-0.08,2.2) node[tick, left] {$1$};
\end{tikzpicture}
\end{center}
```

With $p=(\ln n+c)/n$ the probability that $G(n,p)$ is connected tends to $e^{-e^{-c}}$: the jump from $0$ to $1$ happens in a window of width $O(1/n)$ around $p=\ln n/n$

:::

::: {#fig-random-graphs-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\coordinate (v0) at (1.72,0.53);
\coordinate (v1) at (1.08,1.44);
\coordinate (v2) at (0.03,1.80);
\coordinate (v3) at (-1.04,1.47);
\coordinate (v4) at (-1.70,0.58);
\coordinate (v5) at (-1.72,-0.53);
\coordinate (v6) at (-1.08,-1.44);
\coordinate (v7) at (-0.03,-1.80);
\coordinate (v8) at (1.04,-1.47);
\coordinate (v9) at (1.70,-0.58);
\draw[emph] (v0) -- (v1);
\draw[emph] (v0) -- (v7);
\draw[emph] (v1) -- (v2);
\draw[emph] (v1) -- (v8);
\draw[emph] (v2) -- (v7);
\draw[emph] (v3) -- (v5);
\draw[emph] (v5) -- (v8);
\draw[emph] (v5) -- (v9);
\node[small vertex] at (v0) {};
\node[small vertex] at (v1) {};
\node[small vertex] at (v2) {};
\node[small vertex] at (v3) {};
\node[small vertex, fill=accentLight, draw=accent] at (v4) {};
\node[small vertex] at (v5) {};
\node[small vertex, fill=accentLight, draw=accent] at (v6) {};
\node[small vertex] at (v7) {};
\node[small vertex] at (v8) {};
\node[small vertex] at (v9) {};
\end{tikzpicture}
\end{center}
```

A sample of $G(10,0.25)$ with 8 edges. The two highlighted vertices are isolated, so the graph is not connected. Near the threshold of @thm-connectivity-threshold, isolated vertices are the typical obstacle to connectivity.

:::

We prove part 2 and the matching statement for isolated vertices, which is the heart of part 1: when $\lambda>1$ there are no isolated vertices, and one shows separately (by bounding the expected number of small components) that no other obstacle to connectivity survives.

::: {.proof}

1. Let $Z$ be the number of isolated vertices, $Z=\sum_v\mathbf 1_{A_v}$ with $A_v$ the event that $v$ has no neighbour. Then $\Pr(A_v)=(1-p)^{n-1}$ and $E[Z]=n(1-p)^{n-1}$.

2. Since $\ln(1-p)=-p+O(p^2)$ and $np^2\to0$, $E[Z]=n\,e^{-(n-1)p+O(np^2)}=n^{1-\lambda+o(1)}$. For $\lambda>1$ this tends to $0$, so by the first moment method there are no isolated vertices with probability tending to $1$.

3. For $\lambda<1$, $E[Z]\to\infty$. For $u\ne v$, $\Pr(A_u\cap A_v)=(1-p)^{2n-3}$ (the edge $uv$ is counted once), so
   $$E[Z^2]=E[Z]+n(n-1)(1-p)^{2n-3},\qquad\operatorname{Var}(Z)\le E[Z]+E[Z]^2\Bigl(\frac{1}{1-p}-1\Bigr).$$

4. Hence $\operatorname{Var}(Z)/E[Z]^2\le1/E[Z]+p/(1-p)\to0$, and by the second moment method $\Pr(Z=0)\to0$. A graph with an isolated vertex (and $n\ge2$) is disconnected, which proves part 2.

:::

::: {#exm-random-graphs-isolated .example name="A thousand vertices"}

With $n=1000$ and $\lambda=2$, $p=2\ln1000/1000\approx0.0138$, the mean degree is about $13.8$ and the expected number of isolated vertices is $1000(1-p)^{999}\approx9.2\times10^{-4}$. With $\lambda=\tfrac12$, $p\approx0.0035$ and the expected number of isolated vertices is about $31$.

:::

::: {#rmk-random-graphs-giant .remark name="Other thresholds"}

Thresholds are typical of $G(n,p)$. With $p=c/n$, if $c<1$ all components have $O(\ln n)$ vertices, while if $c>1$ one *giant component* has a constant fraction of the vertices; the size of that fraction is found from a branching-process (Poisson offspring) approximation of the neighbourhood of a vertex.

:::
